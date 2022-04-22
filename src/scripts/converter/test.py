import csv 
import pandas as pd
import numpy as np

#test fillna
d = {'col1': [0, 1, 2, 3], 'col2': ['','','he', 'hey']}
df = pd.DataFrame(data=d, index=[0, 1, 2, 3])
def isNaN(num):
    return num != num

print(df)
r=df.iloc[[0]]
v=r.col2
print(v)

'''df['col2'].fillna('h', inplace = True)
print(df)'''
df.replace('',np.nan,regex = True,inplace=True)
print(df)
if isNaN(v.any()):
    print('this is a nan')