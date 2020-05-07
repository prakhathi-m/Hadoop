#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""mapper.py"""

import sys
import numpy as np
import pandas as pd


# read the test data. 
pf = pd.read_csv('norm-test.csv')
x_test = pf.values

#print(x_test, len(x_test))


# get train data row
for lines in sys.stdin:
    lines = lines.strip()
    x_train = lines.split(',')   # split the line by comma
    y = x_train[-1]           # last element of the train data is label

    # print('y',y)
    # convert the x_train into numpy array and each of type float. 
    x_train = np.asarray(x_train[:-1], dtype=np.float32)  

    # print(type(x_train[0]), type(y), int(y)==4)
    if int(y) != 48:   # find the distance between test and train only when the train data row passed is not header. If it is header, Y=48
        for i in range(len(x_test)):
            # find the distance between each sample of test data with the incoming train data. 
            dist = np.linalg.norm(x_train - x_test[i])

            # converting the test data into string; this is easy to pass on
            key = ','.join(map(str, x_test[i]))
#           print(';'.join(map(str, res)))

            # output (key, value) => (test_data_row, (y, distance))
            print('%s\t%s\t%s' % (key, y, dist))

