#!/usr/bin/env python3

import sys

emp_dict ={}
details_dict={}

for line in sys.stdin:
    line = line.strip()
    # read the output from mapper. output => key and value separated by tab.
    id, value = line.split('\t')
    value_arr = value.split(';')   # value is split by ;


    # if the value list length > 1, then it must be from join2.csv data. It has salary,country,passcode details.
    # so append it into details dictionary with employee id as key
    if len(value_arr) > 1:
        details_dict[id] = value_arr
    
    # otherwise, data must be from join1.csv. It contains name. so append it to emp_dic 
    else:
        emp_dict[id] = value_arr[0]

# iterate over both dictionaries and get values for each employee and print the output.
# in details_dict, first value is salary and last is passcode, in between these two, forms country
# this is because if any country has comma in it and got splitted into two parts.
for id in sorted(details_dict.keys(), reverse=True):
    try:    
      salary = details_dict[id][0]
      country = ','.join(details_dict[id][1:-1])
      password = details_dict[id][-1]
      name = emp_dict[id]
    except ValueError:
      continue

    print('%s\t%s\t%s\t%s\t%s'% (id, name, salary, country, password))
