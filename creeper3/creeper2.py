#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import re
import random
import time

# 设置目标url，使用urllib.request.Request创建请求
url0 = "http://newcar.xcar.com.cn/257/review/0.htm"
req0 = request.Request(url0)

# 使用add_header设置请求头，将代码伪装成浏览器py
req0.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")

# 使用urllib.request.urlopen打开页面，使用read方法保存html代码
html0 = request.urlopen(req0).read()

# 使用BeautifulSoup创建html代码的BeautifulSoup实例，存为soup0
soup0 = BeautifulSoup(html0,"html.parser", from_encoding="utf-8")

# 获取尾页（对照前一小节获取尾页的内容看你就明白了）
total_page = int(soup0.find("div",class_= "pagers").findAll("a")[-2].get_text())
myfile = open("aika_qc_gn_1_1_1.txt","a")
print("user","来源","认为有用人数","类型","评论时间","comment",sep="|",file=myfile)
for i in list(range(1,total_page+1)):
    # 设置随机暂停时间
    stop = random.uniform(1, 3)
    url = "http://newcar.xcar.com.cn/257/review/0/0_" + str(i) + ".htm"
    req = request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")
    html = request.urlopen(req).read()
    soup = BeautifulSoup(html,"html.parser", from_encoding="utf-8")
    contents = soup.find('div', class_="review_comments").findAll("dl")
    l = len(contents)
    for content in contents:
        tiaoshu = contents.index(content)
        try:
            ss = "正在爬取第%d页的第%d的评论，网址为%s" % (i, tiaoshu + 1, url)
            print(ss)
            try:
                comment_jiaodu = content.find("dt").find("em").find("a").get_text().strip().replace("\n","").replace("\t","").replace("\r","")
            except:
                comment_jiaodu = ""
            try:
                comment_type0 = content.find("dt").get_text().strip().replace("\n","").replace("\t","").replace("\r","")
                comment_type1 = comment_type0.split("【")[1]
                comment_type = comment_type1.split("】")[0]
            except:
                comment_type = "好评"
            # 认为该条评价有用的人数
            try:
                useful = int(content.find("dd").find("div",class_ = "useful").find("i").find("span").get_text().strip().replace("\n","").replace("\t","").replace("\r",""))
            except:
                useful = ""
            # 评论来源
            try:
                comment_region = content.find("dd").find("p").find("a").get_text().strip().replace("\n","").replace("\t","").replace("\r","")
            except:
                comment_region = ""
            # 评论者名称
            try:
                user = content.find("dd").find("p").get_text().strip().replace("\n","").replace("\t","").replace("\r","").split("：")[-1]
            except:
                user = ""
            # 评论内容
            try:
                comment_url = content.find('dt').findAll('a')[-1]['href']
                urlc = comment_url
                reqc = request.Request(urlc)
                reqc.add_header("User-Agent",
                                "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36")
                htmlc = request.urlopen(reqc).read()
                soupc = BeautifulSoup(htmlc)
                comment0 = \
                soupc.find('div', id='mainNew').find('div', class_='maintable').findAll('form')[1].find('table',class_='t_msg').findAll('tr')[1]
                try:
                    comment = comment0.find('font').get_text().strip().replace("\n", "").replace("\t", "")
                except:
                    comment = ""
                try:
                    comment_time = soupc.find('div', id='mainNew').find('div', class_='maintable').findAll('form')[1].find('table', class_='t_msg').\
                    find('div', style='padding-top: 4px;float:left').get_text().strip().replace("\n","").replace( "\t", "")[4:]
                except:
                    comment_time = ""
            except:
                try:
                    comment = content.find("dd").get_text().split("\n")[-1].split('\r')[-1].strip().replace("\n", "").replace("\t","").replace("\r", "").split("：")[-1]
                except:
                    comment = ""
            # time.sleep(stop)
            print(user,comment_region,useful,comment_type,comment_time,comment, sep="|", file=myfile)
        except:
            s = "爬取第%d页的第%d的评论失败，网址为%s" % (i, tiaoshu + 1, url)
            print(s)
            pass
myfile.close()
