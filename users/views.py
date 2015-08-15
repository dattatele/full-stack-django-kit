from django.views.decorators.cache import cache_control
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .forms import RegistrationForm



def register(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        #form.save()
        return HttpResponseRedirect(reverse('customers-home'))

    return render(request, 'users/register.html', {
        'form': form
    })
