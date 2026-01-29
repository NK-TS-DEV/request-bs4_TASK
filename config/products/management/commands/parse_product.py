from django.core.management.base import BaseCommand
from products.services.parser import ProductParser
from products.models import Product

class Command(BaseCommand):
    help = "Parse product from brain.com.ua"

    def handle(self, *args, **options):
        url = "https://brain.com.ua/ukr/Mobilniy_telefon_Apple_iPhone_16_Pro_Max_256GB_Black_Titanium-p1145443.html"
        data = ProductParser(url).parse()

        Product.objects.update_or_create(product_code=data["product_code"],defaults={
            "name": data["Name"],
            "price": data.get("price"),
            "currency": data.get("currency"),
            "sale_price": data.get("sale_price"),
            "color": data.get("color"),
            "memory": data.get("memory"),
            "manufacturer": data.get("manufacturer"),
            "reviews_count": data.get("reviews"),
            "display_size": data.get("display"),
            "screen_resolution": data.get("screen_resolution"),
            "images": data.get("photo"),
            "characteristics": data.get("all_characteristics"),})



