import scrapy


class CnnSpider(scrapy.Spider):
    name = 'CNN'
    allowed_domains = ['edition.cnn.com']
    start_urls = ['http://edition.cnn.com/']

    def parse(self, response):
        pass
