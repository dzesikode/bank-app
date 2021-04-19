from django.conf import settings
from django.core.management.base import BaseCommand
from bankapp.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        if Product.objects.count() == 0:
            for default_product in settings.DEFAULT_PRODUCTS:
                print(f'Creating product {default_product["name"]}...')
                new_product = Product.objects.create(name=default_product['name'],
                                                     age=default_product['age'],
                                                     student=default_product['student'],
                                                     income=default_product['income'])
                new_product.save()
        else:
            print('Products already exist.')

