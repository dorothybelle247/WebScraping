import scrapy

class PoseSpider(scrapy.Spider):
    name = "post"

    start_urls = [
        "https://freshchef.online/about/",
        "https://freshchef.online/order-now/"
    ]

    def parse(self, response):
        page = response.url.split('/')[-1]
        filename = 'post-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)


