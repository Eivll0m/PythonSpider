#!/usr/bin/env python
#-*- coding=utf-8 -*-

import requests
import re
import datetime
import time
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')


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
            return pages
        except:
            print '系统繁忙!'
            exit()

    def parse_html(self):
        html = self.get_html()
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

    def write_data(self,file,content):
        with open(file,'a') as f:
            f.write(json.dumps(content, encoding='UTF-8', ensure_ascii=False)+'\n')

    def main(self):
        page_num = 1
        data = self.data
        data['pagesnum'] = page_num
        while page_num <= self.get_page_nums():
            for h in self.parse_html():
                self.write_data('result.txt',h)
            print '爬取完第【%s】页,总共【%s】页' %(page_num,self.get_page_nums())
            page_num += 1
            data['pagesnum'] = page_num
            time.sleep(1)
        else:
            print '爬取完毕'

if __name__ == '__main__':
    H = GetHshfyData()
    H.main()
