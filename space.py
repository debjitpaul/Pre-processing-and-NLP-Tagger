#python script to helps to re-create sentence seprator after Brill-tagger
#!/usr/bin/env python3

'''
Copyright 2017, Debjit Paul.
'''
import glob
import os
import subprocess
import sys
import argparse

def read_file(data):
    graph = []
    clean_graph=[]
    n=0
    a=0
    words=[]
    space=[]
    chunk_tags=[]
    count=0
    print("Creating :"+str(data))
    file1=open("../sentence_tag/"+str(data),"w")
    file2=open("../raw_tag/"+str(data),"r") 
    file3=open("../word/"+str(data),'r') 
    lines=file3.readlines()
    for line in lines:                             
        if line=='\n':
            a=a+1
            count=count+1
            space.append(a-count)
        else:
            a=a+1
    
    
    lines=file2.readlines()
    for line in lines: 
        n=n+1        
        if n in space:
            
            words=str(line).rsplit('/')[0].strip('\n')
            #line=line.rsplit(' ',1)[0] 
            pos_tags=str(line).rsplit('/')[-1].strip('\n')
            s=str(words)+'\t'+str(pos_tags)+'\n'
            file1.write(s)
            file1.write('\n')
            
        else:
            words=str(line).rsplit('/')[0].strip('\n')
            #line=line.rsplit(' ',1)[0] 
            pos_tags=str(line).rsplit('/')[-1].strip('\n')
            s=str(words)+'\t'+str(pos_tags)+'\n'
            file1.write(s)

    return
 	

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("txtfile", help=".txt file containing the input text", nargs='?')
    args = parser.parse_args()
    read_file(args.txtfile)
    #print(args.txtfile)
     ##newgraph, V, E = perform_BFS(graph, V, E, args.center, args.radius)


if __name__ == '__main__':
    main()


   
            
