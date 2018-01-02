# -*- coding: utf-8 -*-
import scrapy
from hshfy.items import HshfyItem
import datetime


class MyhshfySpider(scrapy.Spider):
    name = 'Myhshfy'
    allowed_domains = ['www.hshfy.sh.cn']
    start_urls = ['http://www.hshfy.sh.cn/shfy/gweb/ktgg_search_content.jsp']

    def parse(self, response):
        item = HshfyItem()
        trs = response.xpath('//tr')
        for tr in range(4,len(trs)):
            item['fayuan'] = trs[tr].xpath('./td//text()').extract()[0]
            item['fating'] = trs[tr].xpath('./td//text()').extract()[3]
            item['date'] = trs[tr].xpath('./td//text()').extract()[4]
            item['anhao'] = trs[tr].xpath('./td//text()').extract()[5]
            item['anyou'] = trs[tr].xpath('./td//text()').extract()[6]
            item['bumen'] = trs[tr].xpath('./td//text()').extract()[7]
            item['shenpanzhang'] = trs[tr].xpath('./td//text()').extract()[8]
            item['yuangao'] = trs[tr].xpath('./td//text()').extract()[9]
            item['beigao'] = trs[tr].xpath('./td//text()').extract()[10]
            yield item

        page_nums = int(response.xpath('//strong/text()').extract()[0])
        p = len(trs) - 4
        #pages = page_nums // 15 if page_nums % 15 == 0 else page_nums // 15 + 1
        pages = page_nums // p if page_nums % p  == 0 else page_nums // p + 1
        t = datetime.date.today()
        for page in range(2,pages):
            next_url = 'http://www.hshfy.sh.cn/shfy/gweb/ktgg_search_content.jsp?pagesnum=' + str(page) + 'ktrqjs=' + str(t) + '&pktrqks=' + str(t)
            yield scrapy.Request(next_url, callback=self.parse)