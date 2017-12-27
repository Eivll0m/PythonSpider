#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2017/12/20 14:15
# @Author   : Eivll0m
# @Site     : https://github.com/Eivll0m
# @File     : 多线程2.py
# @Software : PyCharm


import requests
import re
import datetime
import time
import json
import threading
import Queue
import sys
reload(sys)
sys.setdefaultencoding('utf8')

urlqueue = Queue.Queue()
class GetHshfyData:
    def __init__(self):
        self.url = 'http://www.hshfy.sh.cn/shfy/gweb/ktgg_search_content.jsp'
        self.data = {
            'pktrqks': datetime.date.today(),
            'ktrqjs': datetime.date.today(),
        }
        self.headers = {}
        self.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'

    def get_html(self):
        respones = requests.get(self.url,self.data,headers=self.headers)
        return respones.text

    def get_page_nums(self):
        try:
            html = self.get_html()
            page_nums = int(re.search(r'<font.*?<strong>(.*?)</strong>',html,re.S).group(1))
            pages = page_nums // 15 if page_nums % 15 == 0 else page_nums // 15 + 1
            #print '爬取的总页数为：',pages
            return pages
        except:
            print '系统繁忙!'
            exit()


class GetUrl(threading.Thread):
    def __init__(self,urlqueue):
        threading.Thread.__init__(self)
        self.pages = GetHshfyData().get_page_nums()
        self.url = GetHshfyData().url
        self.data = GetHshfyData().data
        self.headers = GetHshfyData().headers
        self.urlqueue = urlqueue

    def run(self):
        for l in range(1,self.pages + 1):
            try:
                self.data['pagesnum'] = l
                respones = requests.get(self.url,self.data,headers=self.headers)
                url = respones.url
                self.urlqueue.put(url)
                self.urlqueue.task_done()
            except:
                time.sleep(1)

def parse_html(html):
    cases = re.findall(r'<TR>(.*?)</TR>',html,re.S)
    for c in cases:
        case = [
            re.search(r'<TD.*?color.*?>(.*?)<',c.split('\r\n')[1]).group(1), #法院字段
            re.search(r'<TD.*?color.*?>(.*?)&',c.split('\r\n')[2]).group(1), #法庭
            re.search(r'<TD.*?>(.*?)&',c.split('\r\n')[3]).group(1), #开庭日期
            re.search(r'<TD.*?>(.*?)&',c.split('\r\n')[4]).group(1), #案号
            re.search(r'<TD.*?>(.*?)&',c.split('\r\n')[5]).group(1), #案由
            re.search(r'<TD.*?center">(.*?)&',c.split('\r\n')[6]).group(1), #承办部门
            re.search(r'<TD.*?center">(.*?)&',c.split('\r\n')[7]).group(1), #审判长/主审人
            re.search(r'<TD.*?>(.*?)&',c.split('\r\n')[8]).group(1), #原告/上诉人
            re.search(r'<TD.*?>(.*?)&',c.split('\r\n')[9]).group(1)  #被告/被上诉人
        ]
        yield case


def write_data(file, content):
    with open(file, 'a') as f:
        f.write(json.dumps(content, encoding='UTF-8', ensure_ascii=False) + '\n')

class GetContext(threading.Thread):
    def __init__(self,urlqueue):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue
        self.headers = GetHshfyData().headers

    def run(self):
        p = 1
        while True:
            try:
                url = self.urlqueue.get()
                html = requests.get(url,headers=self.headers).text
                for h in parse_html(html):
                    write_data('result2.txt', h)
                print '爬取完第【%s】页' % p
                p += 1
            except:
                time.sleep(1)

class Controller(threading.Thread):
    def __init__(self,urlqueue):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue

    def run(self):
        while True:
            print '程序执行中.....'
            time.sleep(20)
            if self.urlqueue.empty():
                print '程序执行完毕!'
                exit()

t1 = GetUrl(urlqueue)
t1.start()
t2 = GetContext(urlqueue)
t2.start()
t3 = Controller(urlqueue)
t3.start()