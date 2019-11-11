#/bin/bash
### ---------------
###
### Create: bigbug4
### Date: 2019-11-11
### Usage: bash seq_precesss.sh file1(seq_file) file2(seq_name) file3(mRNAseq)
###
### ---------------

echo progressing start ...
echo

# 去除 Sequence unavailable 的行

tac $1 | sed -e '/Sequence unavailable/,+1d' | tac > $3

# 正则去除序列名称生成一个seq_name文件
grep '^>.*$' $3 | sed -e 's/|/_/' > $2

# 统计行数
#wc -l $2
# 去掉fasta格式以‘>’开头的行，输出纯序列到一个mRNAseq文件
tac $1 | sed -e '/Sequence unavailable/,+1d' | tac | sed -e 's/^>.*$/ /g;' | awk -v RS="" '{gsub("\n","");print}' | sed -e 's/ /\n/g' | sed -e '/^$/d'> $3

echo finished.
echo please check files: $2 $3 .