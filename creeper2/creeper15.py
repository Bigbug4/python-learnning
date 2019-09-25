#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def imgurl(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    # 获取总页数
    page = int(soup.select('.pagenavi span')[-2].text)
    # 获取图片链接
    a = soup.select('.main-image a')[0]
    src = a.select('img')[0].get('src')
    meiziid = src[-9:-6]
    print('开始下载妹子:',format(meiziid))
    for i in range(1, page+1):
        i = '%02d' % i
        img = src.replace('01.jpg', str(i)+'.jpg')
        headers = {
            'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
            'Referer':'http://www.mzitu.com'
        }
        #此请求头破解防盗链
        response = requests.get(img,headers=headers)
        f = open('E:\\download\\meizi\\'+meiziid+'%s.jpg' % i, 'wb')
        f.write(response.content)
        f.close()
        print( '===> %s 完成 ' % (meiziid + i))
    print('妹子 %s 下载好了，请享用！\n' % meiziid)

def imgpage(page=''):
    res = requests.get('http://www.mzitu.com/page/' + page)
    soup = BeautifulSoup(res.text, 'html.parser')
    href = soup.select('#pins a')
    # 链接去重
    list = set([i.get('href') for i in href])
    # 遍历下载
    [imgurl(i) for i in list]

result = input('你要下载哪一页的妹子：')
imgpage(result)
