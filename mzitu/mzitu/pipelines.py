# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import os

class MzituPipeline(object):
    def process_item(self, item, spider):
        headers = {
            'Referer': 'http://www.mzitu.com/'
        }
        local_dir = 'E:\\data\\mzitu\\' + item['title']
        local_file = local_dir + '\\' + item['name']
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)
        with open(local_file,'wb') as f:
            f.write(requests.get(item['img'],headers=headers).content)
        return item
