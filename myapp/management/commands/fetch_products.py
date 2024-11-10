import requests
from django.core.management.base import BaseCommand
from myapp.models import Product

class Command(BaseCommand):
    help = "Fetch and populate product data from dummyjson API"

    def handle(self, *args, **kwargs):
        url = "https://dummyjson.com/products"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json().get("products", [])
            for item in data:
                Product.objects.update_or_create(
                    id=item.get("id"),
                    defaults={
                        "title": item.get("title", ""),
                        "description": item.get("description", ""),
                        "category": item.get("category", ""),
                        "price": item.get("price", 0.0),
                        "discount_percentage": item.get("discountPercentage", 0.0),
                        "rating": item.get("rating", 0.0),
                        "stock": item.get("stock", 0),
                        "brand": item.get("brand", ""),  # Using get() with default value
                        "sku": item.get("sku", ""),
                        "weight": item.get("weight", 0),
                        "dimensions": item.get("dimensions", {}),
                        "warranty_information": item.get("warrantyInformation", ""),
                        "shipping_information": item.get("shippingInformation", ""),
                        "availability_status": item.get("availabilityStatus", ""),
                        "return_policy": item.get("returnPolicy", ""),
                        "minimum_order_quantity": item.get("minimumOrderQuantity", 1),
                        "thumbnail": item.get("thumbnail", 'https://via.placeholder.com/150'),
                    }
                )
            self.stdout.write(self.style.SUCCESS("Product data successfully populated!"))
        else:
            self.stdout.write(self.style.ERROR("Failed to fetch data from API"))
