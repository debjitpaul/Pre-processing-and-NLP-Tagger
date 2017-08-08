#!/bin/bash
#
# Extract words from the sentence and arrange in CONLL form 

for file in ./sentence/*;
do
    BASENAME= basename $file
    echo $BASENAME
    python3 word.py "$file" > ../word/$file
done
