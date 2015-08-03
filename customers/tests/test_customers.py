from django.test import TestCase, Client
from django.core.urlresolvers import reverse
import pytest
from customers.models import Customer



class CustomersTestCase(TestCase):

    def setUp(self):
        pass

    def test_customer(self):
        customer = Customer()
        customer.name = 'John Doe'
        customer.save()

    @pytest.mark.slow
    def test_customer_slow(self):
        customer = Customer()
        customer.name = 'John Doe'
        customer.save()
        customers = Customer.objects.all()
        print customers.count()

    @pytest.mark.integration
    def test_customer_integration(self):
        """
        This is a placeholder for a test
        :return:
        """
        customer = Customer()
        customer.name = 'John Doe'
        customer.save()
        customers = Customer.objects.all()
        print customers.count()

    @pytest.mark.env("integration")
    def test_environment(self):
        """
        Test on some environment
        :return:
        """
        pass