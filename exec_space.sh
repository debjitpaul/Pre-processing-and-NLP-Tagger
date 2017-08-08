#!/bin/bash
#
# Extract words from the sentence and arrange in CONLL form 

for file in ./raw_tag/*;
do
    BASENAME= basename $file
    echo $BASENAME
    python3 space.py "$file" > ../sentence_tag/$file
done
