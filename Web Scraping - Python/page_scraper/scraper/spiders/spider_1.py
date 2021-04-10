import scrapy


class Spider1Spider(scrapy.Spider):
    name = 'spider_1'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        title=response.xpath('//span[@class="title"]/text()').get()
        subhead=response.xpath('//span[@class="subheading"]/text()').getall()
        description=response.xpath('//meta[@name="DC.Description.Abstract"]/@content').get()
        rfc=response.xpath('//span[@class="rfc-no"]/text()').get()
        phone=response.xpath('//span[@class="phone"]/text()').get()
        address=response.xpath('//span[@class="address"]/text()').get()
        name=response.xpath('//span[@class="author-name"]/text()').get()
        date=response.xpath('//span[@class="date"]/text()').get()
        #text=w3lib.html.remove_tags(response.xpath('//div[@class="text"]').get())
        return {"RFC":rfc,"Author name":name,"Publishing date":date,"Phone num":phone,"title":title,"subheading":subhead,"Address":address,"Description":description}
