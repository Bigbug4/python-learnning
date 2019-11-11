# -*- coding: utf-8 -*-

import requests
import http.cookiejar as cookielib
from bs4 import BeautifulSoup
import os

#这个路径修改为脚本和文件所在路径
path=r'C:\Users\Administrator\Desktop\FmRNA'
os.chdir(path)
# 生成results文件夹
if not os.path.exists('results'):
    os.mkdir('results')

# session代表某一次连接
Session = requests.session()
# 用cookielib中的方法LWPCookieJar，这个类实例化的cookie对象，就可以直接调用save方法
Session.cookies = cookielib.LWPCookieJar(filename="Cookies.txt")

# 模拟代理
userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
header = {
    # "origin": "https://http://gene-regulation.com",
    "Referer": "https://http://gene-regulation.com/",
    'User-Agent': userAgent,
}

# 模拟登陆,登录1次获取cookies即可
def gene_regulationLogin(account, passwd):

    print ("开始模拟登录 gene-regulation:")

    postUrl = "http://gene-regulation.com/login"
    postData = {
        "user": account,
        "password": passwd
    }
    responseRes = Session.post(postUrl, data = postData, headers = header)
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    print("statusCode : "+ str(responseRes.status_code))
    print("text :\n" + responseRes.text)
    Session.cookies.save()

# 导入序列
def seqload(seqfile,seqname):
   with open(seqfile, 'r') as f:
       sequences = f.readlines()
   with open(seqname, 'r') as f:
       names = f.readlines()
   
   return sequences, names

# 上传序列
def postseq(seq):
    # 通过访问个人中心页面的返回状态码来判断是否为登录状态
    matchUrl = "http://gene-regulation.com/cgi-bin/pub/programs/match/bin/match.cgi"
    # 下面有两个关键点
    # 第一个是header，如果不设置，会返回500的错误
    # 第二个是allow_redirects，如果不设置，session访问时，服务器返回302，
    # 然后session会自动重定向到登录页面，获取到登录页面之后，变成200的状态码
    # allow_redirects = False  就是不允许重定向

    # 提交的表单数据如下：
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
    responseRes = Session.post(matchUrl, headers = header, data=seqData, allow_redirects = False)
    #print(responseRes.status_code)

    return responseRes

# 解析结果
def parsing_results(results):
    soup = BeautifulSoup(results.text, 'lxml')
    p_node = soup.find_all('pre')
    contents = p_node[1].get_text()

    return contents

if __name__ == "__main__":

#    user = input("请输入登录用户:\n")
#    # zengwei201411090205
#    password = input("请输入登录密码:\n")
#    # (v)TTY}A
#    gene_regulationLogin(user, password)
    
    Session.cookies.load()
# 以下文件名为seq_process脚本处理后生成的文件
    seq_file = "mRNA1seq.txt" 
    seq_name = "seq_name1.txt"
    seqs, names = seqload(seq_file,seq_name)
    n=len(seqs)
    for i in range(n):
        seq = seqs[i].strip('\n')
        name = names[i].strip('\n')
        results = postseq(seq)
        #print(result_promoters.text)
        
        results_promoters= parsing_results(results)
        #print(results_promoters)
        #print(type(results_promoters))
        #print(len(results_promoters))
    
        with open("results/"+ name[1:-16] +".txt","a") as f:
            f.write(results_promoters)
