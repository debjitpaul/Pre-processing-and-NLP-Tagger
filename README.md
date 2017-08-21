# Pre-processing-and-NLP Tagger
The tool is made to do pre-processing raw text file to CONLL data format. Then can be used to tag words using artificial taggers such as [Senna](http://ml.nec-labs.com/senna//)  or [Brill Tagger](http://gposttl.sourceforge.net/). 

## Requirements 
python3

[Stanford-parser](https://nlp.stanford.edu/software/lex-parser.shtml)

[Senna](http://ml.nec-labs.com/senna//) 

[Brill Tagger](http://gposttl.sourceforge.net/)



## Pre-processing steps: 
1) Sentence seperator using [standorf](https://nlp.stanford.edu/software/tokenizer.shtml) tool.  
2) Then transfering the text into CONLL format.

## Tagging with Tagger:
1) Tagging with Senna or Brill Tagger

## Post-processing step: 
1) Sentence seperator after tagging the words  

## Flow of the tool: 
### HTML file as input:
Keep your html file in raw folder -->  Execute [Prepossing Task](https://github.com/debjitpaul/Pre-processing-and-NLP-Tagger/blob/master/execute_prepossing.sh) to generate raw clean text--> Execute [Sentence Separator](https://github.com/debjitpaul/Pre-processing-and-NLP-Tagger/blob/master/exec_sentence_seperator.sh) to generate seperate sentences --> Execute [extraction of word in CONLL Format](https://github.com/debjitpaul/Pre-processing-and-NLP-Tagger/blob/master/exec_word.sh) --> Apply [Brill Tagger](https://github.com/debjitpaul/Pre-processing-and-NLP-Tagger/blob/master/exec_brill.sh) to tag words with POS tagging --> Finally to generate senetence seperated tags in [CONLL format](https://github.com/debjitpaul/Pre-processing-and-NLP-Tagger/blob/master/exec_space.sh)

### Text file as input:
Skip the [Prepossing Task](https://github.com/debjitpaul/Pre-processing-and-NLP-Tagger/blob/master/execute_prepossing.sh) and apply the above steps. 



