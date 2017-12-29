import re
import scrapy #导入scrapy包
from bs4 import BeautifulSoup
from scrapy.http import Request ##一个单独的request的模块，需要跟进URL的时候，需要用它
from dingdian.items import DingdianItem ##这是我定义的需要保存的字段，（导入dingdian项目中，items文件中的DingdianItem类）
from lxml import  etree

class Myspider(scrapy.Spider):

    name = 'dingdian'
    allowed_domains = ['23wx.com']
    bash_url = 'http://www.23us.so/list/'
    bashurl = '.html'

    def start_requests(self):
        # for i in range(1, 10):
        #     url = self.bash_url + str(i) + '_1' + self.bashurl
        #     yield Request(url, self.parse)
        yield Request('http://www.23us.so/list/6_1.html', self.parse)

    def parse(self, response):
        print(response.text)
        selector = etree.HTML(response.text)
        # content = selector.xpath('//div[@id="content"]/ul[@id="ul"]/li/text()')
        # print(content)
        item = DingdianItem()
        item['name'] = selector.xpath('//tr/td[1]/a/text()')
        item['author'] = selector.xpath('//tr/td[3]/text()')
        item['name_id'] = 0
        item['category'] = selector.xpath('//dl[@id="content"]/dt/text()')
        yield item

        # max_num = BeautifulSoup(response.text,'lxml').find('div',class_='pagelink').find_all('a')[-1].get_text()
        # bashurl = str(response.url)[:-7]
        # for num in range(1,int(max_num)+1):
        #     url = bashurl + '_' + str(num) + self.bash_url
        # yield  Request(url,callback=self.get_name)

    # def get_name(self,response):
    #     tds = BeautifulSoup(response.text,'lxml').find_all('tr',bgcolor="#FFFFFF")
    #     for td in tds:
    #         novelname = td.find('a').get_text()
    #         novelurl = td.find('a')['href']
    #         yield Request(novelurl,callback=self.get_chapterurl,meta={'name':novelname,'url':novelurl})
    # def get_chapterurl(self,response):
    #     item = DingdianItem()
    #     item['name'] = str(response.meta['name']).replace('\xa0','')
    #     item['novelurl'] = response.meta['url']
    #     category = BeautifulSoup(response.text,'lxml').find('table').find('a').get_text()
    #     author = BeautifulSoup(response.text,'lxml').find('table').find('td')[1].get_text()
    #     bash_url = BeautifulSoup(response.text,'lxml').find('p',class_='btnlink').find('a',class_='read')['href']
    #     name_id = str(bash_url)[-6:-1].replace('/','')
    #     item['category'] = str(category).replace('/','')
    #     item['author'] = str(author).replace('/','')
    #     item['name_id'] = name_id
    #     return item