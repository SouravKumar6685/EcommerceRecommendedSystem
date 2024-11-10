from django.core.management.base import BaseCommand
from myapp.models import Product

class Command(BaseCommand):
    help = "Update search vectors for all products."

    def handle(self, *args, **kwargs):
        for product in Product.objects.all():
            product.save()  # This will trigger the save method with search vector
        self.stdout.write(self.style.SUCCESS('Successfully updated search vectors'))
