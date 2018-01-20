#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/1/20 13:01
# @Author   : Eivll0m
# @Site     : https://github.com/Eivll0m
# @File     : lagou.py.py
# @Software : PyCharm

import requests
import json
import mymongo
import re
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class LagouSpider:
    def __init__(self):
        self.headers = {}
        self.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
        self.headers['Host'] = 'www.lagou.com'
        self.headers['Referer'] = 'https://www.lagou.com/jobs/list_python?px=default&city=%E5%85%A8%E5%9B%BD'
        self.headers['X-Anit-Forge-Code'] = '0'
        self.headers['X-Anit-Forge-Token'] = None
        self.headers['X-Requested-With'] = 'XMLHttpRequest'
        self.url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false&isSchoolJob=0'

    def get_data(self,page):
        while 1:
            try:
                form_data = {
                    'first' : 'true',
                    'pn' :  page,
                    'kd' : 'python'
                }
                result = requests.post(self.url,data=form_data,headers=self.headers)
                return result.json()['content']['positionResult']['result']
            except:
                time.sleep(1)

    def get_detail(self,positionId):
        url = 'https://www.lagou.com/jobs/%s.html' % positionId
        text = requests.get(url,headers=self.headers).text
        jobdescriptions = re.findall(r'<h3 class="description">(.*?)</div>',text,re.S)
        jobdescriptions = [re.sub(r'</?h3>|</?div>|</?p>|</?br>|^\s+|</?li>','',j) for j in jobdescriptions]
        return jobdescriptions

if __name__ == '__main__':
    Lagou = LagouSpider()
    mongo = mymongo.MongodbOPT('xxx.xxx.xxx.xxx',27017,'Mydb','FjyUuQhCoeDG#TwR','lagou')
    for page in range(1,31):
        for position in Lagou.get_data(page):
            result = {}
            result['positionName'] = position['positionName']
            result['createTime'] = position['createTime']
            result['secondType'] = position['secondType']
            result['city'] = position['city']
            result['workYear'] = position['workYear']
            result['education'] = position['education']
            result['companyFullName'] = position['companyFullName']
            result['financeStage'] = position['financeStage']
            result['jobNature'] = position['jobNature']
            result['salary'] = position['salary']
            result['jobdescriptions'] = Lagou.get_detail(position['positionId'])
            result['positionLables'] = position['positionLables']
            result['positionId'] = position['positionId']
            print result
            mongo.insertData(result)
        print '已爬完第%s页!' % page
