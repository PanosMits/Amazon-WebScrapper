from bs4 import BeautifulSoup
from re import sub
from decimal import Decimal
import requests

class Product:
    def __init__(self, url):
        self.url = url

    def price_has_droppped(self):
        # Page to get content from
        page = requests.get(self.url, headers= {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        })

        # Get content
        soup = BeautifulSoup(page.content, 'html.parser')

        # Get price
        price = soup.find(id='priceblock_ourprice').getText().strip('£')
        price_without_cents_value = price[:-3]
        price_in_cents = Decimal(sub(r'[^\d.]', '', price_without_cents_value)) * 100
 
        # return 'True' if price_in_cents < 1000 * 100 else 'False' # returns False
        return 'True' if price_in_cents > 1000 * 100 else 'False' # return True
