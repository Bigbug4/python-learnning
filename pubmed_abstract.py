#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup
import re

PumbMedID = raw_input("请输入PumbMedID：")
print  "开始爬取摘要 ..."
url = "https://www.ncbi.nlm.nih.gov/pubmed/" + PumbMedID
response = urllib.urlopen(url)
# print response.getcode()
html = response.read()
# print len(html)


soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8")

print "获取摘要如下："

# 标签匹配
p_node = soup.find('div', class_='rprt abstract')
p_h1 = soup.find_all('h1')

for p_title in p_h1:
	print p_title.get_text()

# 正则表达式匹配"

'''
# title
title = p_node.get_text()
reg = re.compile("\[Epub ahead of print\](.*?\.)")
title = reg.search(title)
print title.group(1)
'''

# 摘要
abstract = p_node.get_text()
reg = re.compile("Abstract(.*)Share")
abstract = reg.search(abstract)
print "Abstract:"
print abstract.group(1)