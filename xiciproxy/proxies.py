#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/1/2 15:56
# @Author   : Eivll0m
# @Site     : https://github.com/Eivll0m
# @File     : proxies.py
# @Software : PyCharm

import requests
import re

class GetXiciProxyData:
    def __init__(self):
        self.url = 'http://www.xicidaili.com/nn/'
        self.headers = {}
        self.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        self.proxy_list = []

    def get_html(self):
        respones = requests.get(self.url,headers=self.headers)
        if respones.status_code == 200:
            return respones.text

    @property
    def get_proxy(self):
        html = self.get_html()
        http = re.findall(r'<td>(\d+\.\d+\.\d+\.\d+)</td>.*?<td>(\d+)</td>.*?<td>.*?</td>.*?<td>(HTTP)</td>',html,re.S)
        for h in http:
            p = h[0] + ':' + h[1]
            yield p

    def cheak_proxy(self,proxy):
        try:
            requests.get('http://www.baidu.com',headers=self.headers,proxies=proxy,timeout=1)
        except:
            print proxy,'connect failed'
        else:
            return True

    def main(self):
        url = self.url
        for u in range(5):
            url = url + str(u)
            for i in self.get_proxy:
                self.proxy_list.append(i)
        for p in self.proxy_list:
            http_ip_port = 'http://' + p
            proxy = {'http':http_ip_port}
            if self.cheak_proxy(proxy):
                self.write_data('E:\Code\Py-Pj\hshfy\hshfy\proxies.txt',http_ip_port)

    def write_data(self,file,context):
        with open(file,'a') as f:
            f.write(context + '\n')

if __name__ == '__main__':
    GetXiciProxyData().main()