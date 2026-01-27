from config.products.services.parser import ProductParser
from tabulate import tabulate

url = "https://brain.com.ua/ukr/Mobilniy_telefon_Apple_iPhone_16_Pro_Max_256GB_Black_Titanium-p1145443.html"

parser = ProductParser(url)
product_data = parser.parse()
table = []
for key, value in product_data.items():
    table.append([key, value])
print(tabulate(table,headers=["Поле","Значення"],tablefmt = "grid"))

