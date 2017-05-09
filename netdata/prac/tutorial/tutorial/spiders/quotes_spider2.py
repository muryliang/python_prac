import scrapy

class QuotesSpider2(scrapy.Spider):
    name = "quotes2"

    start_urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
            ]
    def parse(self, reponse):
        page = reponse.url.split("/")[-2]
        filename = 'quotes-%s.html' %page
        with open(filanem, 'wb') as f:
            f.write(filename)

