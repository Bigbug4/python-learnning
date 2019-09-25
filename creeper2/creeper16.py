#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests
import sys

# 设置编码
reload(sys)
sys.setdefaultencoding('utf-8')
circle = requests.get("http://www.pythonscraping.com/x/")
# text和content的内容有不同
ccontent = circle.text
# 这里是正则的坑  括号的东西是分组的 外面没有括号之前 只会匹配到jpg和png不会匹配全部
# 外面多一层括号才会匹配整个  但是特别的是 里面的括号也会匹配  所以
# 真正findall的是整个list  list里面每个都是元组  元组里面有xxx.jpg和jpg
pattern = "(http:[^\s]*?(jpg|png|PNG|JPG))"
finder = re.findall(pattern, circle.text)

# 匹配到之后获取匹配开头和末尾位置
# finder = re.search(pattern, test)
# start = finder.start()
# end = finder.end()
# print test[start:end]
# 匹配http 获取文件名
truepicture = ".*photo/p0.*"
# 匹配图片网址
picpattern = "http:[^\s]*/"
# 匹配标题
titlepattern = '<p class="title" title=".*?"'
imgfinder = re.findall(titlepattern, circle.text)
imglen = 0
for n in xrange(0, len(finder)):
	if re.match(truepicture, finder[n][0]):
		print
		finder[n][0]

		# p0改为r0后变成了大图目录的地址，
		bigpicture = finder[n][0].replace('photo/p0', 'photo/r0')
		newimg = requests.get(bigpicture)

		# 替换掉无关的字符串
		temp = imgfinder[imglen].replace('<p class="title" title="', '')
		newfinder = re.search(picpattern, finder[n][0])

		# 截取title
		temp = "D:/PyCharm Community Edition 2017.2.1/photo" + temp[0:len(temp) - 1] + '.jpg'
		# 下载文件，超级简单 设定好目录  content的意义也在于这里
		with open(temp, 'wb') as newfile:
			newfile.write(newimg.content)

		imglen = imglen + 1
