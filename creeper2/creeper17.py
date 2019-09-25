#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def get_html(urllist):
	res = requests.get(urllist)
	soup = BeautifulSoup(res.text, 'html.parser')
	src = soup.find_all("img",class_="BDE_Image")
	return src


def write_img(url):
	for link in url:
		picurl = link.get('src')

		picres = requests.get(picurl).content

		file = open(r"D:\PyCharm Community Edition 2017.2.1\photo\%s.jpg"%picurl[-9:-4],"wb")

		file.write(picres)

		file.close()

url = get_html("http://tieba.baidu.com/p/6093906752")

write_img(url)
print ("sucessfully download!")