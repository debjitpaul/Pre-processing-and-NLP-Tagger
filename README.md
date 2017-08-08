# Pre-processing-and-NLP Tagger
The tool is made to do pre-processing raw text file to CONLL data format. Then can be used to tag words using artificial taggers such as Senna http://ml.nec-labs.com/senna//  or Brill Tagger source: http://gposttl.sourceforge.net/. 

## Requirements 
python3

[Stanford-parser](https://nlp.stanford.edu/software/lex-parser.shtml)

[Senna]{http://ml.nec-labs.com/senna//) 

[Brill Tagger](http://gposttl.sourceforge.net/)



## Pre-processing steps: 
1) Sentence seperator using standorf tool https://nlp.stanford.edu/software/tokenizer.shtml
2) Then transfering the text into CONLL format.

## Tagging with Tagger:
1) Tagging with Senna or Brill Tagger

## Post-processing step: 
1) Sentence seperator after tagging the words  

# Flow of the tool: 
If you have html file as text 
Keep your htlm file in raw folder --> execute pre [GitHub Pages](https://debjit.github.com/)

** Raw text (html file)--> Extracting Text --> Sentence Seperator --> Extracting word --> Brill Tagger --> Raw Tag --> Sentence wise tagged and with Seperator  


