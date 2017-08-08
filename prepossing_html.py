#python script to preprocess as text from html file


'''
Copyright 2017, Debjit Paul.
'''
#!/usr/bin/env python3
#import bs4
#from bs4 import BeautifulSoup
##from BeautifulSoup import BeautifulSoup
import os
import argparse
import sys
import re
import nltk   
#from urllib import urlopen


def read_pos_text_file(data):
    if data is None:
        file = sys.stdin
    else:
        file = open(data,encoding='utf-8', errors='ignore')
    text = []
    for line in file:
    # assumes the .txt file is valid      
            
            if '<TEXT>' in line:
                #while '</TEXT>' not in line:
                for line in file:
                   if '</TEXT>' not in line:
                     if '<p>' not in line:
                        print(line)
                   else:
                     break
            else: 
                  continue
             
                    
    file.close()
    return -1
   
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("txtfile", help=".txt file containing the input text", nargs='?')
    args = parser.parse_args()
    read_pos_text_file(args.txtfile)
    #cleaning(text)


if __name__ == '__main__':
    main()



