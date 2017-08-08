#!/bin/bash
#
# Runs the standford sentence seperator on North American Text Corpus
i=0
for file in ../raw_clean/*;
do
    
    BASENAME=$(basename $file)
    echo $BASENAME
    java -cp stanford-parser.jar edu.stanford.nlp.process.DocumentPreprocessor $file > ./sentence/$BASENAME
done
