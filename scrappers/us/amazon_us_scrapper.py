from bs4 import BeautifulSoup
from re import sub
from decimal import Decimal
import requests

class AmazonUsScrapper:
    def __init__(self):
        self.userAgent = '"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"'

    # TODO: complete this 
    def scrap(self, url):
        return 'Scrapping US amazon ...'

    def searchByTitle(self, title):
        return f'Searching US amazon by {title} ...'
