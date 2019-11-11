#/bin/bash
### ---------------
###
### Create: bigbug4
### Date: 2019-11-7
### Usage: bash precesss.sh path_name
###
### ---------------
echo progressing start ...
echo

# 判断文件夹是否存在，不存在就新建一个
if [ ! -d "$1" ];then
mkdir /$1
fi

head='matrix_identifier\tposition\tcore_match\tmatrix_match\tsequence\tfactor_names'

file=(`ls $1`)
cd $1

for i in ${!file[@]}; do
    string=${file[$i]}
    name=(${string//./ })
    echo ">"${name[0]} >> results1.txt
    head  -n -5 $string | sed -e "s/\s\{2,\}/\t/g" | awk -F "\t" '{if($3==1.000 && $4>0.95) print $0}' >> results1.txt
done

sed  -i "1i ${head}" results1.txt
echo finished.
echo please check files in: $1 .

