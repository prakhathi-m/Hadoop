#!/usr/bin/env python3

""
"reducer.py"
""

#!/usr/bin / env python3
import sys

K = 8      #initialize k value
distances = {}

for lines in sys.stdin:
    lines = lines.strip()

    # input is (key \t label \t dist), here key = test_data
    test_data, label, dist  = lines.split('\t')
    # test_data is of string format separated by comma. so split it by comma and convert it to a tuple.
    test = tuple(test_data.split(','))

    # set the tuple as a key in distance dictionary, and its value is of type list of lists. {test_row_1: [[y1, dist1] [y2, dist2]...]}
    # convert the label and dist to float and append it in dictionary
    if distances.get(test):

        distances[test].append([float(label), float(dist)])
    else :
        distances[test] = [[float(label), float(dist)]]  # print   (y, dist)

# print('before sort', distances)
for k in distances.keys():
    distances[k] = sorted(distances[k], key = lambda x: x[-1])   #sort the dictionary values by distances


neighbours = []
res = []
for j in distances.keys(): 
    if len(distances[j]) > K:
        try:
          for i in range(K):
              neighbours.append(distances[j][: K][i][0])   #take top k list in the dictionary for each key. pick only the K labels

          label = max(set(neighbours), key = neighbours.count) #find the most occuring label
          neighbours = []         
          for item in j:           # append the predicted label to the corresponding test data
            res.append(item)
          res.append(label)
          #print(j[0], label)
          print(', '.join(map(str, res)))     #convert the result to string and print it.
          res = []
        except ValueError:
          continue


