from django.shortcuts import render
from .models import Customer

# Create your views here.
def home(request):
    customers = Customer.objects.all()
    return render(request, 'customers/index.html', {"customers": customers})