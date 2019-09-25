#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import urllib
import os

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html


def getImg(html):
	reg = r'src="(.+?\.jpg)"'
	imgre = re.compile(reg)
	imglist = imgre.findall(html)
	x = 0
	path = '.\\photo'  # 设置保存地址

	if not os.path.isdir(path):
		os.makedirs(path)  # 将图片保存到文件夹中
	paths = path + '\\'  # 保存在路径

	for imgurl in imglist:
		urllib.urlretrieve(imgurl, '%s%s.jpg' % (paths,x))
		x = x + 1
	print '图片已开始下载，注意查看文件夹'

html = getHtml("https://tieba.baidu.com/p/6237988334")
print html
getImg(html)
