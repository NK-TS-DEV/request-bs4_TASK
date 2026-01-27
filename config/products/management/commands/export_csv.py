import csv
from django.core.management.base import BaseCommand
from products.services.export_to_csv import export_products_to_csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        export_products_to_csv()
        self.stdout.write("CSV exported")
