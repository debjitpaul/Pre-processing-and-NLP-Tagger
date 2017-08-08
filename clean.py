#!/usr/bin/env python3

'''
Copyright 2017, Debjit Paul

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
        file = open(data)
    graph = []
    clean_graph=[]
    for line in file:
    # assumes the .txt file is valid      
            line = line.split(' ')
            graph.append(line)
    for index in range (1,len(graph)):
             print(graph[index]+'\n')  
    file.close()
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help=".pos file containing the input text", nargs='?')
    args = parser.parse_args()
    read_pos_tree_file(args.file)


if __name__ == '__main__':
    main()
