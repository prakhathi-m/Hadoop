#!/usr/bin/env python3

import sys

for lines in sys.stdin:
    line = lines.strip()
    line = line.split(",")

    # split the line by comma. since salary has comma in it as default, it got split into two parts
    # concatenate the two parts and delete those two parts from list and insert the concatenated string into the list.
    if len(line) > 4:
       currency = line[1] + ',' + line[2]
       line.pop(1)
       line.pop(1)
       line.insert(1, currency)


    # fist element of the list is employee id which is a key, and rest of the list is converted into string, separated by ; and sent as value (key, value)
    value = ';'.join(map(str, line[1:]))
    print('%s\t%s' % (line[0], value))


			
