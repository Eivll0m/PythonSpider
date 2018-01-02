# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HshfyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    fayuan = scrapy.Field()
    fating = scrapy.Field()
    date = scrapy.Field()
    anhao = scrapy.Field()
    anyou = scrapy.Field()
    bumen = scrapy.Field()
    shenpanzhang = scrapy.Field()
    yuangao = scrapy.Field()
    beigao = scrapy.Field()
