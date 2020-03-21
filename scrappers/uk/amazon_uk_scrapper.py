from bs4 import BeautifulSoup
from re import sub
from decimal import Decimal
import requests

class AmazonUkScrapper:
    def __init__(self):
        self.userAgent = '"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"'

    def scrapByUrl(self, url):
        page = requests.get(url, headers= {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        })

        soup = BeautifulSoup(page.content, 'html')

        # Get product price 
        # TODO: some products do not have the price in that id
        price = soup.find(id='priceblock_ourprice').getText()

        # Get product information
        # TODO: Check if that exists, some products do not have this
        technical_details = {}
        product_information_section     = soup.find(id='product-details-grid_feature_div') 
        product_information_table       = product_information_section.find('tbody')
        product_information_table_rows  = product_information_table.find_all('tr')
    
        # Loop through each item(tr) in the table
        for row in product_information_table_rows:
            tds = row.find_all('td')
            technical_details[tds[0].get_text()] = tds[1].get_text()


        # Get product details
        # TODO: Check if that exists, some products do not have this
        # product_details = {}
        # product_details_section = soup.find(id='detail_bullets_id').getText()
        # product_details_table = product_details_section.find('table')
        # product_details_table_list = product_details_table.find('ul')

        # # Loop through each item(tr) in the table
        # for item in product_details_table_list:
        #     lis = item.find_all('li')

        return {
            "price": price,
            "technical_details": technical_details,
        }


   
    def searchByUrl(self, url):
        page = requests.get(url, headers= {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        })

        soup = BeautifulSoup(page.content, 'html')

        # data-cel-widget="search_result_1"
        # data-cel-widget="search_result_2"
        # data-cel-widget="search_result_3"
        
        # return 'searching ...'
        return str(soup.prettify)
