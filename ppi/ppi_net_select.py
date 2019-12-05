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
    'referer': 'https://string-db.org/cgi/input.pl?sessionId=0t5TnAdL3Kwi&input_page_show_search=on',
    'User-Agent': userAgent
}

header2 = {
    'origin': 'https://string-db.org',
    'referer': 'https://string-db.org/cgi/network.pl',
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
def postdata1(Url,Data,Gene):

    response = requests.post(url=Url, headers = header, data=Data, allow_redirects = True)
    #print(response.status_code)
    #print(response.text)

    pattern = re.compile(r"id='identifier_(\d+)'")
    result = re.findall(pattern, response.text)
    #print(result)

    if result:
        result = result[0]
    else :
        print(Gene + " Network not found,Please search manually.")

    return result

def postdata2(Url,Data,Gene):

    response = requests.post(url=Url, headers = header2, data=Data, allow_redirects = True)
    #print(response.status_code)
    #print(response.text)

    pattern = re.compile(r"href='(/cgi/generate_task_specific_download_file.pl\?[^\']+download_data_format=tsv[^\']+.tsv)'")
    result = re.findall(pattern, response.text)
    if result:
        result = 'https://string-db.org' + result[0]
        # https://string-db.org/cgi/generate_task_specific_download_file.pl?taskId=mvJwtHyyzYBK%26download_data_format=tsv%26download_file_name=string_interactions.tsv
    else :
        print(Gene + " Network not found,Does not meet the set threshold.")

    return result
# 下载tsv文件
def getdata(Url):

    response = requests.get(url=Url, headers=header)

    with open("results/" + gene + ".tsv","wb") as f:
        f.write(response.content)

if __name__ == "__main__":
    # 基因名文件
    gene_name = "results/not_found.txt"
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
            'sessionId': '0t5TnAdL3Kwi'
            #'custom_score': 0.070
            # 这个阈值无法同时设置太高，只能默认0.400
             }

        identifier = postdata1(url,data,gene)
        #print(identifier)
        if identifier:
            data2 = {
                'identifier': identifier,
                'sessionId': '0t5TnAdL3Kwi',
                'additional_network_nodes': 0,
                'block_structure_pics_in_bubbles': 0,
                'chemicalmode': 0,
                'direct_neighbor': 1,
                'ge_fdr': 0.01,
                'ge_sort_column': 3,
                'have_user_input': 1,
                'hide_disconnected_nodes': 0,
                'hide_node_labels': 0,
                'input_query_species': 'auto_detect',
                'internal_call': 1,
                'interpret_call': 0,
                'limit': 10,
                'minprotchem': 0,
                'multi_input': 0,
                'network_display_mode': 'svg',
                'network_flavor': 'evidence',
                'query_data_use_permission': 'off',
                'required_score': 400,
                'targetmode': 'proteins',
                 'custom_score': 0.900
                # 阈值根据要求调整
             }

            tsv_url = postdata2(url,data2,gene)

            if tsv_url:
                print(tsv_url)
                getdata(tsv_url)
