from django.core.management.base import BaseCommand, CommandError
from customers.models import Customer

class Command(BaseCommand):
    help = 'Generate random data to populate the database'

    def add_arguments(self, parser):
        #parser.add_argument('customer_id', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        customer = Customer()
        customer.name = 'sample'
        customer.save()