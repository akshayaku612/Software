import scrapy


class ApnewsSpider(scrapy.Spider):
    name = 'apnews'
    allowed_domains = ['apnews.com']
    start_urls = ['http://apnews.com/']

    def parse(self, response):
        pass
