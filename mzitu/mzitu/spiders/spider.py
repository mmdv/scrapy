from scrapy import Request
from scrapy import CrawlSpider,Rule
from scrapy.Linkextractors import LinkExtrator
from mzitu.items import MzituItem

class Spider(CrawlSpider):
    name = 'mzitu'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://www.mzitu.com/']
    img_urls = []
    rules = (
        Rule(LinkExtractor(allow=('http://www.mzitu.com/\d{1,6}',), deny=('http://www.mzitu.com/\d{1,6}/\d{1,6}')), callback='parse_item', follow=True),
    )
	
	def parse_item(self, response):
		print(response.url)