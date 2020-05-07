#!/usr/bin/env python3


import io
import regex as re
from more_itertools import locate
import numpy as np
import copy
from nltk.corpus import stopwords
import sys

for line in sys.stdin:
    data=line.lower()
    data= data.strip()
    data=re.sub('[^A-Za-z0-9\s]+', '', data)
    #print(data)
    data=np.array(data.split())
    #wsw = [ w for w in data if not w in sw]
    #wsw=" ".join(wsw)
    #data=" ".join(data)
    #data=np.array(data.split())
    for i in data:
        print( '{0}\t\t{1}'. format(i, 1))
