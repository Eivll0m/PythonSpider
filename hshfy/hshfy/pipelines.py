# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HshfyPipeline(object):
    def __init__(self):
        self.file = open(r'E:\data\result.txt', 'w')

    def process_item(self, item, spider):
        line = '["%s","%s","%s","%s","%s","%s","%s","%s","%s"]\n' %(item['fayuan'],
                                                item['fating'],
                                                item['date'],
                                                item['anhao'],
                                                item['anyou'],
                                                item['bumen'],
                                                item['shenpanzhang'],
                                                item['yuangao'],
                                                item['beigao']
                                                )
        self.file.write(line.encode('utf-8'))
        return item

    def close_spider(self, spider):
        self.file.close()