from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Customer
from .forms import CustomerForm


def home(request):
    customers = Customer.objects.all()
    return render(request, 'customers/index.html', {
        "customers": customers
    })

def create(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('customers-home'))

    return render(request, 'customers/create.html', {
        "form": form
    })

def edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('customers-home'))

    return render(request, 'customers/create.html', {
        "form": form
    })

def delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return HttpResponseRedirect(reverse('customers-home'))

