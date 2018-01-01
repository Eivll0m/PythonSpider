# -*- coding: utf-8 -*-
import scrapy
from mzitu.items import MzituItem
from lxml import etree
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class MymzituSpider(scrapy.Spider):
    def get_urls():
        url = 'http://www.mzitu.com'
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        r = requests.get(url,headers=headers)
        html = etree.HTML(r.text)
        urls = html.xpath('//*[@id="pins"]/li/a/@href')
        return urls

    name = 'Mymzitu'
    allowed_domains = ['www.mzitu.com']
    start_urls = get_urls()

    def parse(self, response):
        item = MzituItem()
        #item['title'] = response.xpath('//h2[@class="main-title"]/text()')[0] .extract()
        item['title'] = response.xpath('//h2[@class="main-title"]/text()')[0] .extract().split('（')[0]
        item['img'] = response.xpath('//div[@class="main-image"]/p/a/img/@src')[0].extract()
        item['name'] = response.xpath('//div[@class="main-image"]/p/a/img/@src')[0].extract().split('/')[-1]
        yield item

        next_url = response.xpath('//div[@class="pagenavi"]/a/@href')[-1].extract()
        if next_url is not None:
            yield scrapy.Request(next_url, callback=self.parse)