# from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Customer
from .forms import CustomerForm


def is_member(user):
    return user.groups.filter(name='member').exists()

# adding cache control for demo purposes
# @cache_control(public=True, max_age=600)
def home(request):
    customers = Customer.objects.all()
    return render(request, 'customers/index.html', {
        "customers": customers
    })


@login_required
@user_passes_test(is_member, login_url=reverse_lazy('limited'))
def create(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('customers-home'))

    return render(request, 'customers/create.html', {
        "form": form
    })

@login_required
def edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('customers-home'))

    return render(request, 'customers/create.html', {
        "form": form
    })

@login_required
def delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return HttpResponseRedirect(reverse('customers-home'))

