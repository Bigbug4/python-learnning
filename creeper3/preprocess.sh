#/bin/bash

head='matrix_identifier\tposition\tcore_match\tmatrix_match\tsequence\tfactor_names'
tail -n +4 $1 | head  -n -5 | sed -e "s/\s\{2,\}/\t/g" | sed  -e "1i ${head}" >$2
awk -F "\t" '{if($3==1.000 && $4>0.95) print $0}' $2 | sed  -e "1i ${head}" > $3


