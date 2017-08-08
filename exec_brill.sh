#!/bin/bash
#
# Brill Tagger:
	# input: 
		# word1
		# word2
		# word3
		#  :
		#  :
		# wordn
	# output:
		# word1/tag1
		# word2/tag2
		# word3/tag3
		# word4/tag4
		#  :
		#  :
		# wordn/tagn

for file in ./word/*;
do
    BASENAME= basename $file
    echo $BASENAME
    /BRILL_TAGGER_NEWLISP_V1.14/Bin_and_Data/tagger LEXICON "$file" BIGRAMS LEXICALRULEFILE CONTEXTUALRULEFILE > ../raw_tag/$file
done
