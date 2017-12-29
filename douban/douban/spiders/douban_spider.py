from scrapy import Request, Spider
from douban.items import DoubanItem

class DoubanScrapy(Spider):
    name = 'douban'
    # 爬虫起始url
    start_urls = ["https://movie.douban.com/top250"]

    def start_request(self):
        yield Request(self.start_urls, callback = self.parse)

    def parse(self, response):
        for msg in response.xpath('//div[@class="item"]'):

            item = DoubanItem()
            item['url'] = msg.xpath('div[@class="pic"]/a/@href').extract()[0]
            item['rank'] = msg.xpath('div[@class="pic"]/em/text()').extract()[0]
            item['movie_name'] = msg.xpath('div[@class="pic"]/a/img/@alt').extract()[0]
            item['price'] = msg.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            comment = msg.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract()

            # 爬取过程中，有些没有直接的评论，做些处理
            if comment:
                item['comment'] = comment[0]
            yield item

        #获取当前url的下一页链接
        next_page = response.xpath('//span[@class="next"]/a/@href').extract_first()

        if next_page:
            request_url = response.urljoin(next_page)
            print (request_url)
            yield Request(request_url, callback = self.parse)