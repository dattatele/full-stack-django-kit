from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core import signing
from .forms import RegistrationForm, LoginForm


def register(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        group_names = ['new_user']
        for name in group_names:
            (group, created) = Group.objects.get_or_create(name=name)
            user.groups.add(group)
        user.email = form.cleaned_data['email']
        user.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        user.send_confirmation_email(request)
        return HttpResponseRedirect(reverse('confirmation-sent'))

    return render(request, 'users/register.html', {
        'form': form
    })


def login_view(request):
    form = LoginForm()
    return render(request, 'users/login.html', {
        'form': form,
        'messages': messages.get_messages(request),
        'next': request.GET.get('next', '')
    })


def auth(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
    except:
        return redirect('login')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            next_url = request.POST.get('next')
            if not next_url:
                next_url = 'home'
            return redirect(next_url)
        else:
            # Return a 'disabled account' error message
            pass
    else:
        # Return an 'invalid login' error message.
        messages.error(request, 'Invalid credentials')
    return HttpResponseRedirect(reverse('login'))


def confirm_email(request, code):
    from django.core.signing import BadSignature
    signer = signing.Signer()
    try:
        email = signer.unsign(code)
    except BadSignature:
        # todo: improve error messaging for bad signatures
        return HttpResponseRedirect('/')
    user = get_object_or_404(get_user_model(), email=email)
    (group, created) = Group.objects.get_or_create(name='member')
    user.groups.add(group)
    return redirect('home')


@login_required
def home(request):
    return render(request, 'users/home.html')


@login_required
def limited(request):
    if request.user.groups.filter(name='member').exists():
        return HttpResponseRedirect(reverse('customers-home'))
    return render(request, 'users/confirm-email.html')


@login_required
def send_email_confirmation(request):
    user = request.user
    if user.groups.filter(name='member').exists():
        # email already confirmed
        return redirect('customers-home')
    user.send_confirmation_email(request)
    return render(request, 'users/confirmation-email-sent.html')

