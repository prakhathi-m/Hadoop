#!/usr/bin/env python3

from sys import stdin
import re
import io

#ijnitializing empty dictionary
dictionary= {}

#inputing each line from standard input
for line in stdin:
    
    #split and store word and filename using tab delimiter
    word, filename = line.split('\t')
    
    #assign word and values as key and value pair in the dictionary
    dictionary.setdefault(word,{})
    dictionary[word].setdefault(filename,0)
    
#print(dictionary)
#iterating through the dictionary
for word in dictionary:
    filename_list = []
    for docid in dictionary[word]:
        #print(",",docid)
        filename_list.append(docid)                  
        #posting_list.append(",")
    #printing word name filename separated by comma
    filenames = '\t,'.join(filename_list)
    print( '{0}\t{1}'. format(word,filenames))
        


