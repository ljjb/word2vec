#!/bin/bash

# 3570000
for (( length=357000; length <= 357000; length+=357000 ))
do
  echo $length
  echo "HI"
done

for ((ik=1;ik<=25;ik+=1)
do
    echo $i
done
# ./word2vec -train text8 -output vectors.bin -cbow 1 -size 300 -window 5 -negative 5 -hs 0 -sample 5e-3 -threads 8 -binary 0 -iter 1
