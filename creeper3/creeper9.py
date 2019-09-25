#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import re
import os
import urllib

#根据给定的网址来获取网页详细信息，得到的html就是网页的源代码
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    print(page.getcode())
    return html.decode('UTF-8')

def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)    #转换成一个正则对象
    imglist = imgre.findall(html)    #表示在整个网页中过滤出所有图片的地址，放在imglist中

#    try:
#       os.mkdir('.\\photo')
#    except:
#        os.path.exists('.\\photo')

    x = 0    #声明一个变量赋值
    path = '.\\photo'    #设置保存地址

    if not os.path.isdir(path):
        os.makedirs(path)    #将图片保存到文件夹中
    paths = path+'\\'    #保存在路径下

    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'{0}{1}.jpg'.format(paths,x))
        # 打开imglist，下载图片保存在本地,format格式化字符串
        x = x + 1
        print('图片已开始下载，注意查看文件夹')

    return imglist

html = getHtml("https://tieba.baidu.com/p/6237988334")    #获取该网址网页详细信息，html就是网页的源代码
print (html)    #从网页源代码中分析并下载保存图片
getImg(html)