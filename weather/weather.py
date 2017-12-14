#!/usr/bin/env python
#coding:utf-8

import requests
from colorama import Fore
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Weather:
    def __init__(self):
        self.url = 'http://wthrcdn.etouch.cn/weather_mini?city='
    
    def get_color(self,color,string):
        if color == 'LIGHTGREEN_EX':
            return Fore.LIGHTGREEN_EX + string + Fore.RESET
        elif color == 'LIGHTRED_EX':
            return Fore.LIGHTRED_EX + string + Fore.RESET
        elif color == 'LIGHTBLUE_EX':
            return Fore.LIGHTBLUE_EX + string + Fore.RESET
        elif color == 'LIGHTCYAN_EX':
            return Fore.LIGHTCYAN_EX + string + Fore.RESET
        elif color == 'LIGHTMAGENTA_EX':
            return Fore.LIGHTMAGENTA_EX + string + Fore.RESET
        elif color == 'GREEN':
            return Fore.GREEN + string + Fore.RESET
        elif color == 'RED':
            return Fore.RED + string + Fore.RESET
        elif color == 'BLUE':
            return Fore.BLUE + string + Fore.RESET
        elif color == 'CYAN':
            return Fore.CYAN + string + Fore.RESET
        elif color == 'MAGENTA':
            return Fore.MAGENTA + string + Fore.RESET
        else:
            return Fore.WHITE + string + Fore.RESET


    def get_weather(self):
        while True:
            self.city = raw_input('请输入您想查询的城市名称：')
            if self.city:
                break
        url = self.url + self.city
        weather = requests.get(url).json()
        if weather['desc'] == 'OK':
            print self.get_color('RED','城市：') + self.get_color('RED',weather['data']['city'])
            print self.get_color('GREEN','温度：') + self.get_color('GREEN',weather['data']['wendu']) + self.get_color('GREEN','℃')
            print self.get_color('BLUE','感冒：') + self.get_color('BLUE',weather['data']['ganmao'])
            print self.get_color('CYAN','风向：') + self.get_color('CYAN',weather['data']['forecast'][0]['fengxiang'])
            print self.get_color('MAGENTA','风级：') + self.get_color('MAGENTA',weather['data']['forecast'][0]['fengli'])
            print self.get_color('LIGHTGREEN_EX','高温：') + self.get_color('LIGHTGREEN_EX',weather['data']['forecast'][0]['high'])
            print self.get_color('LIGHTRED_EX','低温：') + self.get_color('LIGHTRED_EX',weather['data']['forecast'][0]['low'])
            print self.get_color('LIGHTBLUE_EX','天气：') + self.get_color('LIGHTBLUE_EX',weather['data']['forecast'][0]['type'])
            print self.get_color('LIGHTCYAN_EX','日期：') + self.get_color('LIGHTCYAN_EX',weather['data']['forecast'][0]['date'])
            print self.get_color('LIGHTMAGENTA_EX','*' * 80)
            while True:
                key = raw_input('是否显示未来四天的天气情况？（Y/N）')
                if key.upper() == 'Y':
                    break
                elif key.upper() == 'N':
                    exit()
                else:
                    print '输入有误，请重新输入!'
            for i in range(1, 5):
                print '日期：' + weather['data']['forecast'][i]['date']
                print '风向：' + weather['data']['forecast'][i]['fengxiang']
                print '风级：' + weather['data']['forecast'][i]['fengli']
                print '高温：' + weather['data']['forecast'][i]['high']
                print '低温：' + weather['data']['forecast'][i]['low']
                print '天气：' + weather['data']['forecast'][i]['type']
                print self.get_color('RED','-' * 80)

        else:
            print '您输入的城市有误，或者天气中心未收录您输入的城市。'


if __name__ == '__main__':
    W = Weather()
    W.get_weather()
