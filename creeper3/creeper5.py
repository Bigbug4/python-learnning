#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http import cookiejar
from urllib import request

url = "http://www.baidu.com"
response1 = request.urlopen(url)
print ("第一种方法")
# 获取状态码，200表示成功
print (response1.getcode())
# 获取网页内容的长度
print (len(response1.read()))

print ("第二种方法")
request1 = request.Request(url)
# 模拟Mozilla浏览器进行爬虫
request1.add_header("user-agent", "Mozilla/5.0")
response2 = request.urlopen(request1)
print (response2.getcode())
print (len(response2.read()))

print ("第三种方法")
cookie = cookiejar.CookieJar()
# 加入request2处理cookie的能力
opener = request.build_opener(request.HTTPCookieProcessor(cookie))
request.install_opener(opener)
response3 = request.urlopen(url)
print (response3.getcode())
print (len(response3.read()))
print (cookie)