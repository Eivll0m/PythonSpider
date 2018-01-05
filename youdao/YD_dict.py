#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2018/1/5 16:55
# @Author   : Eivll0m
# @Site     : https://github.com/Eivll0m
# @File     : YD_dict.py
# @Software : PyCharm

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class YoudaoDict:
    def __init__(self):
        self.url = 'http://fanyi.youdao.com'
        self.agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        self.dcap = dict(DesiredCapabilities.PHANTOMJS)
        self.dcap["phantomjs.page.settings.userAgent"] = self.agent
        self.service_args = []
        self.service_args.append('--load-images=no')  ##关闭图片加载
        self.service_args.append('--disk-cache=yes')  ##开启缓存
        self.service_args.append('--ignore-ssl-errors=true')  ##忽略https错误
        self.browser = webdriver.PhantomJS('D:\\Program Files\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe',service_args=self.service_args)

    def transTarget(self):
        browser = self.browser
        browser.implicitly_wait(3)
        browser.get(self.url)
        text = browser.find_element_by_id('inputOriginal')
        text.clear()
        while 1:
            key = str(raw_input('请输入您需要翻译的内容：'))
            if key:
                break
        text.send_keys(key.decode('utf-8'))
        while 1:
            try:
                bro = browser.find_element_by_css_selector('#transTarget > p > span')
                break
            except:
                print '还未定位到元素!'
        return bro.text

if __name__ == '__main__':
    D = YoudaoDict()
    while 1:
        print D.transTarget()