from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import lxml
import re
from decimal import Decimal

class ProductParser:
    def __init__(self, url):
        self.url = url
        self.soup = None
        self.data = {}

    def fetch_data(self):
        response = requests.get(self.url)
        response.encoding = 'utf-8'
        response.raise_for_status()
        self.soup = BeautifulSoup(response.text, 'lxml')


    def parse_main(self):
        full_name = self.soup.find('h1', class_='main-title')
        self.data["Name"] = full_name.get_text(strip=True) if full_name else None
        product_code = self.soup.find('div', class_='product-code-num')
        self.data["product_code"] = product_code.get_text(strip=True) if product_code else None



    def parse_price(self):
        price_block = self.soup.find('div', class_='price-wrapper')
        if price_block:
            price_text = price_block.get_text(strip=True)
            price, currency = clean_price(price_text)
            self.data["price"] = price
            self.data["currency"] = currency
        else:
            self.data["price"] = None
            self.data["currency"] = "₴"

    def parse_images(self):
        photo = []
        list_of_photo = self.soup.find_all("img", class_="br-main-img")

        for img in list_of_photo:
            scr = img.get('src')
            if scr:
                photo.append(urljoin(self.url, scr))

        self.data["photo"] = photo


    def parse_characteristics(self):
        memory = self.soup.find("a",title=lambda x: x and "Вбудована пам'ять 256 Gb" in x).get_text(strip=True)
        self.data["memory"] = memory
        color = self.soup.find("a", title = lambda x: x and "Колір чорний" in x).get_text(strip=True)
        self.data["color"] = color


        for item in self.soup.find_all('div', class_='br-pr-chr-item'):
            spans = item.find_all('span')
            if len(spans) < 2:
                continue
            name = spans[0].get_text(strip=True)

            if name == "Виробник":
                value = spans[1].get_text(strip=True)
                self.data["manufacturer"] = value
                return

    def all_characteristics(self):
        chars_dict = {}
        items = self.soup.find_all('div', class_='br-pr-chr-item')

        for item in items:
            name_node = item.find('span')

            value_node = item.find('div', class_='br-pr-chr-value') or item.find('a')

            if name_node and value_node:
                key = name_node.get_text(strip=True).replace(':', '')
                value = value_node.get_text(strip=True)

                chars_dict[key] = value

        self.data["all_characteristics"] = chars_dict

    def parse_reviews(self):
        reviews = self.soup.select('div.deep-1')
        self.data["reviews"] = len(reviews)

    def parse_display(self):
        display = self.soup.find("a",title = lambda x: x and "Діагональ екрану " in x).get_text(strip=True)
        self.data["display"] = display
        Screen_resolution = self.soup.find("a", title = lambda x:x and "Роздільна здатність екрану" in x ).get_text(strip=True)
        self.data["screen_resolution"] = Screen_resolution

    def parse(self):
        self.fetch_data()
        self.parse_main()
        self.parse_price()
        self.parse_display()
        self.parse_characteristics()
        self.parse_images()
        self.parse_reviews()
        self.all_characteristics()



        return self.data


def clean_price(price_str):
    """
    Преобразует строку вида "65 799₴" в Decimal("65799.00") и возвращает валюту "₴"
    """
    if not price_str:
        return None, None
    # Выделяем цифры и точки/запятые
    num = re.sub(r"[^\d.,]", "", price_str).replace(",", "")
    currency = re.sub(r"[\d\s.,]", "", price_str)
    try:
        return Decimal(num), currency
    except:
        return None, currency
