import csv
import json
from products.models import Product


def export_products_to_csv(path="products.csv"):
    products = Product.objects.all()

    headers = [
        "Name", "Price", "Sale price", "Code", "Reviews",
        "Color", "Memory", "Manufacturer", "Display size",
        "Screen resolution", "Images", "Characteristics"
    ]

    with open(path, "w", newline="", encoding="utf-8-sig") as f:

        writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_ALL)
        writer.writerow(headers)

        for p in products:

            images_str = ", ".join(p.images) if isinstance(p.images, list) else str(p.images)


            if isinstance(p.characteristics, dict):
                chars_str = "\n".join([f"{k}: {v}" for k, v in p.characteristics.items()])
            else:
                chars_str = str(p.characteristics)

            writer.writerow([
                p.name,
                p.price,
                p.sale_price or "",
                p.product_code,
                p.reviews_count,
                p.color or "",
                p.memory or "",
                p.manufacturer or "",
                p.display_size or "",
                p.screen_resolution or "",
                images_str,
                chars_str
            ])