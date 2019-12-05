# -*- coding: utf-8 -*-

import requests
import os
import re

# 切换工作路径
path=r'C:\Users\Administrator\Desktop\FmRNA1\ppi'
os.chdir(path)

# 创建results文件夹
if not os.path.exists('results'):
    os.mkdir('results')

userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"

header = {
    'origin': 'https://string-db.org',
    'referer': 'https://string-db.org/cgi/input.pl',
    'User-Agent': userAgent
}

# network.pl 网址
url = "https://string-db.org/cgi/network.pl"


# 导入基因名
def geneload(genename):

    with open(genename, 'r') as f:
        genes = f.readlines()

    return genes

# post表单
def postdata(Url,Data,Gene):

    response = requests.post(url=Url, headers = header, data=Data, allow_redirects = True)
    #print(response.status_code)
    # print(response.text)

    #pattern = re.compile(r"href='/cgi/generate_task_specific_download_file.pl\?[^\']+download_data_format=tsv[^\']+.tsv'")
    pattern = re.compile(r"href='(/cgi/generate_task_specific_download_file.pl\?[^\']+download_data_format=tsv[^\']+.tsv)'")
    result = re.findall(pattern, response.text)
    if result:
        #result = 'https://string-db.org' + result[0][6:-1]
        result = 'https://string-db.org' + result[0]
        # https://string-db.org/cgi/generate_task_specific_download_file.pl?taskId=mvJwtHyyzYBK%26download_data_format=tsv%26download_file_name=string_interactions.tsv
    else :
        print(Gene + " Network not found,Please search manually.")

        #with open("results/not_found.txt","a") as f:
            #f.write(Gene + "\n")

    return result

# 下载tsv文件
def getdata(Url):

    response = requests.get(url=Url, headers=header)

    with open("results/" + gene + ".tsv","wb") as f:
        f.write(response.content)

if __name__ == "__main__":
    # 基因名文件
    gene_name = "gene_name.txt"
    genes = geneload(gene_name)
    n = len(genes)
    for i in range(n):
        gene = genes[i].strip('\n')

        # 提交表单信息
        data = {
            'identifier': gene,
            # 基因名
            'species_text_single_identifier': 'Homo sapiens',
            # 物种名
            'custom_score': 0.900
            # 这个阈值无法同时设置太高，只能默认0.400
             }

        tsv_url = postdata(url,data,gene)

        if tsv_url:
            print(tsv_url)
            getdata(tsv_url)
