#!/usr/bin/env python
# -*- coding:utf-8 -*-

from urllib import request
from urllib import parse

url = 'http://www.someserver.com/register.cgi'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name': 'WHY', 'location': 'SDU', 'language': 'Python'}
data = parse.urlencode(values).encode(encoding='UTF8')
headers = {'User-Agent': user_agent}
req = request.Request(url, data, headers)
req.get_method = lambda : 'HEAD'
response1 = request.urlopen(req)
the_page = response1.read()
print(response1.getcode())
print(len(the_page))

