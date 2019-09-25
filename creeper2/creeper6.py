#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

from bs4 import BeautifulSoup

html_doc = """
</html>
<body>
</div>
        <div class="rprt_all">
		<div class="rprt abstract">
		<div class="cit">
		<a href="#" title="Bioorganic chemistry." abstractLink="yes" alsec="jour" alterm="Bioorg Chem.">Bioorg Chem.</a> 
		<h4>2019 Aug 21;92:103214. doi: 10.1016/j.bioorg.2019.103214. [Epub ahead of print]</h4>
		</div>
		<h1>The role of <span class="highlight" style="background-color:">long noncoding RNA</span> in major human disease.</h1>
		<div class="auths">
		<a href="/pubmed/?term=Zhang%20X%5BAuthor%5D&amp;cauthor=true&amp;cauthor_uid=31499258">Zhang X</a>
		<sup>1</sup>, <a href="/pubmed/?term=Hong%20R%5BAuthor%5D&amp;cauthor=true&amp;cauthor_uid=31499258">Hong R</a>
		<sup>2</sup>, <a href="/pubmed/?term=Chen%20W%5BAuthor%5D&amp;cauthor=true&amp;cauthor_uid=31499258">Chen W</a>
		<sup>1</sup>, <a href="/pubmed/?term=Xu%20M%5BAuthor%5D&amp;cauthor=true&amp;cauthor_uid=31499258">Xu M</a>
		<sup>2</sup>, <a href="/pubmed/?term=Wang%20L%5BAuthor%5D&amp;cauthor=true&amp;cauthor_uid=31499258">Wang L</a>
		<sup>3</sup>.</div><div class="afflist">
		<h3>
		<a title="Open/close author information list" class="jig-ncbitoggler-open" href="#">Author information</a>
		</h3>
		<dl class="ui-ncbi-toggler-slave-open">
		<dt>1</dt><dd>Department of Biotechnology, Gannan Medical University, Ganzhou 341000, China.</dd>
		<dt>2</dt><dd>First Affiliated Hospital of Gannan Medical University, Ganzhou 341000, China.</dd>
		<dt>3</dt><dd>Department of Biotechnology, Gannan Medical University, Ganzhou 341000, China. Electronic address: 469730795@qq.com.</dd>
		</dl>
		</div>
		<div class="abstr">
		<h3>Abstract</h3>
		<div class="">
		<h4>BACKGROUND: </h4><p><span class="highlight" style="background-color:">Long</span> <span class="highlight" style="background-color:">noncoding</span> RNAs (lncRNAs) are RNAs whose transcripts are longer than 200nt in length and lack the ability to encode proteins due to lack of specific open reading frames. lncRNAs were once thought to represent transcriptome noise or garbage sequences and a byproduct of <span class="highlight" style="background-color:">RNA</span> polymerase II (Pol II), and thereby ignored by researchers. In fact, <span class="highlight" style="background-color:">lncRNA</span> was involved in a wide variety of physiological and pathological processes in organisms. Comprehensive study of <span class="highlight" style="background-color:">lncRNA</span> does not only provide explanations to the physiological and pathological processes of living organisms, but also gives us new perspectives to the diagnosis, prevention and treatment of some clinical diseases. Therefore, the study of <span class="highlight" style="background-color:">lncRNA</span> is a very broad field of great research value and significance.</p>
		<h4>RESULTS: </h4><p>This article reviews the function of lncRNAs and their role in major human diseases.</p>
		<h4>CONCLUSIONS: </h4><p>Numerous studies show that <span class="highlight" style="background-color:">lncRNA</span> might serve as a biomarker for diagnosis and prognosis of various diseases. Compared to conventional biomarkers, <span class="highlight" style="background-color:">lncRNA</span> seems to have a higher diagnostic and prognostic values, not only because of their tissue and disease specific expression patterns, but also due to their highly stable physical and chemical properties.</p>
		<p class="copyright">Copyright ? 2019 Elsevier Inc. All rights reserved.</p>
		</div>
		</div>
		<div class="keywords">
		<h4>KEYWORDS: </h4><p>Aging related diseases; Chromatin remodeling; Chromosome dose compensation; Tumor; <span class="highlight" style="background-color:">lncRNA</span></p>
		</div>
		<div class="aux">
		<div class="resc">
		<dl class="rprtid">
		<dt>PMID:</dt> <dd>31499258</dd>  <dt>DOI:</dt> <dd><a href="//doi.org/10.1016/j.bioorg.2019.103214" ref="aid_type=doi" target="_blank">10.1016/j.bioorg.2019.103214</a></dd> 
		</dl>
		</div>        
    </div> </div> </body> </html>
"""
# 创建一个BeautifulSoup解析对象
soup = BeautifulSoup(html_doc, "html.parser", from_encoding="utf-8")

# 获取摘要
print "获取摘要"

# 获取标题
abstracts_h = soup.find_all('h4')
for abstract_h in abstracts_h:
	print abstract_h.get_text()

# 获取段落
abstracts_p = soup.find_all('p')
for abstract_p in abstracts_p:
	print abstract_p.get_text()