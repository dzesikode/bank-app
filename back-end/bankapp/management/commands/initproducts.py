from django.core.management.base import BaseCommand
from bankapp.models import Product


DEFAULT_PRODUCTS = [
    {
        'name': 'Current Account',
        'age': ['ADULT', 'SENIOR'],
        'student': False,
        'income': ['LOW_INCOME', 'MEDIUM_INCOME', 'HIGH_INCOME'],
    },
    {
        'name': 'Current Account Plus',
        'age': ['ADULT', 'SENIOR'],
        'student': False,
        'income': ['HIGH_INCOME'],
    },
    {
        'name': 'Junior Saver Account',
        'age': ['JUNIOR'],
        'student': False,
        'income': ['NO_INCOME', 'LOW_INCOME', 'MEDIUM_INCOME', 'HIGH_INCOME'],
    },
    {
        'name': 'Student Account',
        'age': ['ADULT', 'SENIOR'],
        'student': True,
        'income': ['NO_INCOME', 'LOW_INCOME', 'MEDIUM_INCOME', 'HIGH_INCOME'],
    },
    {
        'name': 'Debit Card',
        'age': ['ADULT', 'SENIOR'],
        'student': False,
        'income': ['NO_INCOME', 'LOW_INCOME'],
    },
    {
        'name': 'Credit Card',
        'age': ['ADULT', 'SENIOR'],
        'student': False,
        'income': ['MEDIUM_INCOME', 'HIGH_INCOME'],
    },
    {
        'name': 'Gold Credit Card',
        'age': ['ADULT', 'SENIOR'],
        'student': False,
        'income': ['HIGH_INCOME'],
    },
]

class Command(BaseCommand):

    def handle(self, *args, **options):
        if Product.objects.count() == 0:
            for default_product in DEFAULT_PRODUCTS:
                print(f'Creating product {default_product["name"]}...')
                new_product = Product.objects.create(name=default_product['name'],
                                                     age=default_product['age'],
                                                     student=default_product['student'],
                                                     income=default_product['income'])
                new_product.save()
        else:
            print('Products already exist.')

