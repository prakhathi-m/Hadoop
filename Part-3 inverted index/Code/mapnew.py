#!/usr/bin/env python3
import io
import re
import numpy as np
import sys
import os
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#list storing set of stop words in english
stopwordslist = set(stopwords.words('english'))

#function definitio for stemming
ps = PorterStemmer()


#inputs a line from standard input
for line in sys.stdin:
    
    #gets current path from the operating system environment
    File_path = os.getenv('map_input_file')
    #retrieves file name from the file path
    doc_id = os.path.split(File_path)[-1]
    
    #converts input line to lowercase
    data=line.lower()
    #regular expression retrieving alphabetic words only
    data=re.sub('[^A-Za-z\s]+', '', data)
    #stores words in the line to a list
    data=data.split()
    
    #interate through the words in the list
    for term in data:
        #performing stemming on each word
        term = ps.stem(term)
        #checking if the stemmed word is not in the set of stop words
        if term not in stopwordslist:
            #outputting each word and its file name
            print( '{0}\t{1}'. format(term,doc_id))


