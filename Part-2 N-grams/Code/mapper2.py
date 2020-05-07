#!/usr/bin/env python3

import sys 


for line in sys.stdin:
	if len(line)>2:
		line=line.strip()
		word, count = line.split('\t', 1)
		count=int(count)
		print('reduce\t{0}.{1}'.format(word, count))
	
