import pandas as pd

def normalize(df):
    result = df.copy()
    for column in df.columns:
        max_value = df[column].max()
        min_value = df[column].min()
        result[column] = (df[column] - min_value) / (max_value - min_value)
    return result

pf = pd.read_csv("~/knn/Train.csv", header=None)
print(pf.shape)

# Last column of the dataset is the label
y_train = pf.iloc[1:,-1]

# drop the last column and take the rest of the column as x_train
x_train=pf.iloc[1:, :-1]
x = normalize(x_train)
print('x_train', x.shape)
print('y_train', y_train)

# create a dataframe with normalized x_train
df = pd.DataFrame(x) 

# append y_train to the dataframe
df['48'] = y_train.values
print('Total shape of new train csv',df.shape)

# write the dataframe as csv, omitting the column index
df.to_csv('~/knn/norm-train.csv', index=False)


# repeat the same for test data and create the new csv with normalized test data
pf = pd.read_csv("~/knn/Test.csv", header=None)
print('x_test',pf.shape)
x_test=pf.iloc[1:, :]
x = normalize(x_test)
df = pd.DataFrame(x) 
df.to_csv('~/knn/norm-test.csv', index=False)
