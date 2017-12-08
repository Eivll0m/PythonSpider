#!/usr/bin/env python
#-*- coding=utf-8 -*-
from __future__ import unicode_literals
import re
import requests
import pprint
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9035'
response = requests.get(url,verify=False)
stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
d = pprint.pformat(dict(stations),indent=4).decode("unicode-escape").replace('u','')
with open("stations.json","w") as f:
	f.write(d)


