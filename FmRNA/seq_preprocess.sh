#/bin/bash

tac $1 | sed -e '/Sequence unavailable/,+1d' | tac  > $3
grep '^>.*$' $3 | sed -e 's/|/_/'> $2
#wc -l $2
cat $3 | sed -e 's/^>.*$/ /g;'| sed -e ':label;N;s/\n//;b label'| sed -e 's/\s\+/ /g' -e 's/ /\n/g' | tail -n +2 | head -n -1 > $3