#/bin/bash

echo progressing start ...
echo
head='matrix_identifier\tposition\tcore_match\tmatrix_match\tsequence\tfactor_names'
file=(`ls $1`)
cd $1
for i in ${!file[@]}; do
    string=${file[$i]}
    name=(${string//./ })
    tail -n +4 $string | head  -n -5 | sed -e "s/\s\{2,\}/\t/g" -e "1i ${head}" > ${name[0]}"-1.txt"
    awk -F "\t" '{if($3==1.000 && $4>0.95) print $0}' ${name[0]}"-1.txt" | sed  -e "1i ${head}" > ${name[0]}"-2.txt"
done

echo finished.


