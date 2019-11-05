# -*- coding: utf-8 -*-

import requests
import http.cookiejar as cookielib
from bs4 import BeautifulSoup
import re

# session代表某一次连接
Session = requests.session()
# 因为原始的session.cookies 没有save()方法，所以需要用到cookielib中的方法LWPCookieJar，这个类实例化的cookie对象，就可以直接调用save方法。
Session.cookies = cookielib.LWPCookieJar(filename="D:\\PyCharm Community Edition 2017.2.1\\scripts\\creeper3\\Cookies.txt")

userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
header = {
    # "origin": "https://http://gene-regulation.com",
    "Referer": "https://http://gene-regulation.com/",
    'User-Agent': userAgent,
}

seq="TACCAATATTTTAACTGTGAAATAGTACAACTTTTCTACTAATAGTTGACATTGTATTCCCTATAGTAATTAGATTATGGGTGTTTCTTTCCCATTTTTTTTGTAATCAGTTTAAATCCTTTTTGAAATGTTAAACTAGTCTTTGGGAAAACATTTTTTGTCCCAAACTTAGGATATGCATTACTCCCTCATTCTTATATTTTAAAATATGTCTACAAATTTAGATCTCATTCTTTGATACCATCTACATAGCTAGTTTTATCTTATTTCCTCTTTTCTTATAAATTGACAACTTTCAGTGATGTTAGGTAAACATTGACTGTATGTCTAAGTCCTTCATCCTCCTGCCTGACTTCATAGGTCCCAAAGGTACCTCTTAGATTTGTGTTTGTGTTAGAGAGTGTCCACCATCTGTCGGCCTCATGTTGATTCTTCTATACCCTTCTGTTTATCAGAGTAGTAGGAAGACTGCAAAATACATTTCCCAAAATCCCTTGCTAGCTGGCATCCAATGGAGGGCAGGACATGAATGAAGGCTGGAGGGAAGAAGCCATTTTTTAAAAATACTTTCTGCTTGCACCTGTGGCAGTGCCAGCAGCAGCAGCCACATGGACAGCAACAGTGGTGACAGCAACAGCAAGATTAGCAGTTTGGGCAAGAACATAGAAGCAAGGGTGCCTGGTGAGCACAGGTTCCTGAGGCGCTGCTCAGGCAGCAGTTCTCCAAAGGAAGCAGCCTCTATGGCACAGTGTCCATGGGCTGTGGGTAAAATCATTTTCCCTATTGTCCTCCAGCTCTATGTGCAATCACAGTTTAGTGCAATTGCCAGTCCTTGGATAACCTAACCCTTCTTGTTTTACTCCTCTAACCCATTTCTATATTTTCATAACAGATTCCTTACATTAAATGCCCTCTGTCAAACACAGATCTGTTACTGTTCTCCTGATTGAGTAGCGTCCAAGGCAAGCTGGTAGGAATTTCAGCATGTGTGTGCAACATCAGCAGATGCAGTGCACCCAGAATGAATTTCATCATATCCTGGAAAAACGTTTGAGGAAGACTCGATTGACAATGTCAACTCTGCACACCACTGTTCTTTATCTCTTGGTAAAGAATCATCAACCTCTCAGATCCAGTGAAAGATTTTATGTTATTTACTGGCATTTAAAGACACTTGTTTGTGCTGTGCTTATTTCCCAGGAGGTCTGCATTCAAATTACTGGGGAAAAAATGCAAGACTTTTGCATCTGTTGAGCCCTTTCTTCTTTAAGGCATATGATTCATCACTCTCATCTCCCTGCTTTTTTCTTCCCCTTAGTCTCCTAAGAATTTTGAATGTATTTTCTTTTGATATTTCTTCTTCCCTTTTCTTTAGGAACTCTTCATCTTTGCAGATAAGCTGGCATTCAGAAGGAGGACACTTGAGAAAGAAAGGAAGCCAGTAGAATAATGCTATCACAGAAGAAAGGATGAGGTCAGTGTGGGCTCTAGTCTTACGCCACAGGTTAATTATCATCATATGTAGCCTCTAATTAAGATAAAATATGGAGAATATCTTATTCCCCCACAAAATGAAAGGGAACTTAGCTTAAACTATGGAATAATTTCATAGGTTACCACAGGCAAATTCATGCCCATACCTCTATATTCAGGAACTCTTCCTTCATCATCCTGAGCAATGAGGAAGGGGACTACTGACTCCAAATTTTGGAAATATTTATGTCATGGCCCATTGCCCTGATGGATTTGTTGACCTTTAATATTTAGAATCTCTGCCTCTATGCATGTTACCCCCGATATCTGCATGTAACACAGATATGGTAGATTTAGAAGATGACACTTGATTAGACACAAAATGTGGAAGAAAAAATATCAAACTGTGTAGCTGAATGTTACCCAGAAGTGAAGAAAGGCATGCAGCCAGATTTCCCCAGCTCTTTGTTTCATCACATGATGTTGCTTGGATATCAGCTTATCAACAGACTTCCACCACCACCACCAGCATATAAACAGAGTCCGCGTAAGAAAACTACACTGAATAGGAATGGCAGCTTTTAAAAGTGGGGGAACTACAGTATAGGGTATAGGATAAACG"

def gene_regulationLogin(account, password):

    print ("开始模拟登录gene-regulation:")

    postUrl = "http://gene-regulation.com/login"
    postData = {
        "user": account,
        "password": password
    }
    responseRes = Session.post(postUrl, data = postData, headers = header)
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    print("statusCode : "+ str(responseRes.status_code))
    print("text :\n" + responseRes.text)
    Session.cookies.save()

def isLoginStatus(seq):
    # 通过访问个人中心页面的返回状态码来判断是否为登录状态
    routeUrl = "http://gene-regulation.com/cgi-bin/pub/programs/match/bin/match.cgi"
    # 下面有两个关键点
    # 第一个是header，如果不设置，会返回500的错误
    # 第二个是allow_redirects，如果不设置，session访问时，服务器返回302，
    # 然后session会自动重定向到登录页面，获取到登录页面之后，变成200的状态码
    # allow_redirects = False  就是不允许重定向

    seqData = {
		"Status": "First",
		"searchName": "default",
		"usr_seq": "default.seq",
		"seqStat": "DEL",
		"sequenceName": "default",
		"theSequence": seq,
		"SearchMode": "ALL",
		"group": "vertebrates",
		"quality": "high",
		"allMode": "FP",
		"cut-off": "0.7",
		"core": "0.75",
		"ourProfile": "cell_cycle_specific.prf"
	}
    responseRes = Session.post(routeUrl, headers = header, data=seqData, allow_redirects = False)
    #print("isLoginStatus "+ str(responseRes.status_code))

    return responseRes

def table(text):
    soup = BeautifulSoup(isLogin.text, 'lxml')
    p_node = soup.find_all('pre')
    contents = p_node[1].get_text()

    return contents

if __name__ == "__main__":

    #gene_regulationLogin("zengwei201411090205", "(v)TTY}A")
    Session.cookies.load()
    isLogin = isLoginStatus(seq)
    #print(isLogin.text)
    text= table(isLogin)

    print(text)
    #print(type(text))
    #print(len(text))
    with open("seq.txt","w") as f:
        f.write(text)
