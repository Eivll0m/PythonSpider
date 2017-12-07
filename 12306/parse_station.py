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

# def byteify(input):
#     if isinstance(input, dict):
#         return {byteify(key): byteify(value) for key, value in input.iteritems()}
#     elif isinstance(input, list):
#         return [byteify(element) for element in input]
#     elif isinstance(input, unicode):
#         return input.encode('utf-8')
#     else:
#         return input

# d = byteify(p)
# print d
# with open("a.json","w")as f:
# # 	p = pprint.pformat(dict(stations),indent=4)
#  	f.write(p)


#with open("stations.json","w") as f:
#	f.write(pprint(dict(stations),indent=4))
#json.dump(pprint(dict(stations),indent=4),open("a.json","w"))
#result = pprint.pformat(dict(stations),indent=4)
#json.dump(result,open("a.json","w"))

