from django.core.management.base import BaseCommand, CommandError
from customers.models import Customer

class Command(BaseCommand):
    help = 'Test integrations'

    def add_arguments(self, parser):
        #parser.add_argument('customer_id', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        """
        Things to check:
        1. can access databases
        2. can access apis
        3. can access files/directories
        :param args:
        :param options:
        :return:
        """
        messages = []
        try:
            Customer.objects.all()[0]
        except:
            messages.append('Cannot fetch customers')

        self.stdout.write("\n".join(messages))
