#!/usr/bin/env python3


import io
import regex as re
from more_itertools import locate
import numpy as np
import copy
from nltk.corpus import stopwords
import sys

lines=""
final=[]
wsw=[]
sw = set(stopwords.words('english'))
for line in sys.stdin:
    data=line.lower()
    data=re.sub('[^A-Za-z0-9\s]+', '', data)
    #print(data)
    data=np.array(data.split())
 
    #wsw = [ w for w in data if not w in sw]
    #wsw=" ".join(wsw)
    data=" ".join(data)
    final.append(data)
final= " ".join(final)
final=np.array(final.split())


keys=['science','sea','fire']
for k in keys:
  all = list(locate(final, lambda condition: condition==k))
  data1=copy.deepcopy(final)
  data1[all]="$"
  for i in all:
      #data1=copy.deepcopy(data)
      #data1[i]='$'
      trigram1=data1[i-2:i+1]
      trigram1='_'.join(trigram1)

      trigram2=data1[i-1:i+2]
      trigram2='_'.join(trigram2)

      trigram3=data1[i:i+3]
      trigram3='_'.join(trigram3)
      
      print( '{0}\t{1}'. format(trigram1, 1))
      print( '{0}\t{1}'. format(trigram2, 1))
      print( '{0}\t{1}'. format(trigram3, 1))
