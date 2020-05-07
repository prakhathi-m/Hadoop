#!/usr/bin/env python3


import sys
from operator import itemgetter

current_word = None
current_count = 0
word = None
final=[]
reduce_final=[]
count=0
j=0

for line in sys.stdin:
	if len(line)>2:
		line=line.strip()
		word, count = line.split('\t', 1)
		count=int(count)


		if current_word == word:
			current_count += count
		else:
			if current_word:
				reduce_final.append({"word":current_word,"count":current_count})   
		    
			current_count = count
			current_word = word

if current_word == word:
	reduce_final.append({"word":current_word,"count":current_count})
	for i in reduce_final:
		print('{0}\t{1}'.format(i["word"], i["count"]))
			
	
