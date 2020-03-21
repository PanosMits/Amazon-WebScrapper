from scrappers.uk.amazon_uk_scrapper import AmazonUkScrapper

class AmazonUkService:
    def __init__(self):
        self.amazonUkScrapper = AmazonUkScrapper()

    def scrapByUrl(self, url):
        return self.amazonUkScrapper.scrapByUrl(url)

    def search(self, title):
        baseSearchUrl = 'https://www.amazon.co.uk/s?k='
        title = title.replace(" ", "+")
        url = baseSearchUrl + title
        return self.amazonUkScrapper.searchByUrl(url)