# -*- coding: utf-8 -*-
import scrapy
from mzitu.items import MzituItem
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class MymzituSpider(scrapy.Spider):
    name = 'Mymzitu'
    allowed_domains = ['www.mzitu.com']
    #start_urls = response.xpath('//*[@id="pins"]/li/a/@href').extract()
    start_urls = [u'http://www.mzitu.com/114291',
                 u'http://www.mzitu.com/114244',
                 u'http://www.mzitu.com/114203',
                 u'http://www.mzitu.com/114154',
                 u'http://www.mzitu.com/114103',
                 u'http://www.mzitu.com/114055',
                 u'http://www.mzitu.com/113989',
                 u'http://www.mzitu.com/113946',
                 u'http://www.mzitu.com/113895',
                 u'http://www.mzitu.com/113834',
                 u'http://www.mzitu.com/113803',
                 u'http://www.mzitu.com/113782',
                 u'http://www.mzitu.com/113731',
                 u'http://www.mzitu.com/113690',
                 u'http://www.mzitu.com/113659',
                 u'http://www.mzitu.com/113609',
                 u'http://www.mzitu.com/113562',
                 u'http://www.mzitu.com/113515',
                 u'http://www.mzitu.com/113473',
                 u'http://www.mzitu.com/113376',
                 u'http://www.mzitu.com/113427',
                 u'http://www.mzitu.com/113261',
                 u'http://www.mzitu.com/113310',
                 u'http://www.mzitu.com/113200']

    def parse(self, response):
        item = MzituItem()
        item['title'] = response.xpath('//h2[@class="main-title"]/text()')[0] .extract().split('（')[0]
        item['img'] = response.xpath('//div[@class="main-image"]/p/a/img/@src')[0].extract()
        item['name'] = response.xpath('//div[@class="main-image"]/p/a/img/@src')[0].extract().split('/')[-1]
        yield item

        next_url = response.xpath('//div[@class="pagenavi"]/a/@href')[-1].extract()
        if next_url is not None:
            yield scrapy.Request(next_url, callback=self.parse)
