#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from lxml import etree

PumbMedID = raw_input("请输入PumbMedID：")
print  "开始爬取摘要 ..."
url = "https://www.ncbi.nlm.nih.gov/pubmed/" + PumbMedID

html = requests.get(url)
# xmlContent = etree.HTML(html.text)
xmlContent = etree.HTML(html.content)
contents = xmlContent.xpath('//*[@id="maincontent"]/div/div[5]/div/div[4]/div')

print "获取摘要如下:\n\nAbstract:"
title = xmlContent.xpath('//*[@id="maincontent"]/div/div[5]/div')
print title[0].xpath('h1/text()')[0]

abstracts = contents[0].xpath('p/text()')

#for abstract in abstracts:
print abstracts[0]