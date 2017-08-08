#!/usr/bin/env python3

'''
Perform Couple on a given word
Copyright 2017, Debjit Paul.
'''

import os
import argparse
import random
import ntpath
import sys
import itertools

def read_pos_tree_file(data):
    if data is None:
        file = sys.stdin
    else:
        file = open(data,"r")#,encoding='utf-8', errors='ignore')
    graph = []
    clean_graph=[]
    for line in file:
    # assumes the .txt file is valid      
            line = line.split(' ')
            if len(line)>4:
               graph.append(line)
    for index in range (0,len(graph)):
       for i in range(0,len(graph[index])):
              if graph[index][i]=='&MD;' or '-LRB-' in graph[index][i] or '--' in graph[index][i] or '-RRB-' in graph[index][i] or '&UR;' in graph[index][i]:
                  i=i
              else:
                  print(graph[index][i]) 
    file.close()
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("txtfile", help=".txt file containing the input text", nargs='?')
    args = parser.parse_args()
    read_pos_tree_file(args.txtfile)


if __name__ == '__main__':
    main()
