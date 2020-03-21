from scrappers.us.amazon_us_scrapper import AmazonUsScrapper

class AmazonUsService:

    def __init__(self):
        self.amazonUsScrapper = AmazonUsScrapper()

    def scrap(self, url):
        return self.amazonUsScrapper.scrap(url)

    def search(self, title):
        return self.amazonUsScrapper.searchByTitle(title)