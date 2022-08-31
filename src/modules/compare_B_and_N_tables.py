#compare my handmade script and Nicolas one. 
from cmath import nan
import pandas as pd
import numpy as np

Nicolas_df = pd.read_csv("../../../data/WL/handmade_Nicolas_detailed.csv", encoding= 'unicode_escape')
Bertille_df = pd.read_csv("../../../data/WL/handmade_Bertille_light.csv")

#print(Nicolas_df.head())
#print(Bertille_df.head())
#print(Nicolas_df.dtypes)
Nicolas_df['Nicolas_match'] = Nicolas_df['ICC1.1'].str[:1]
compare_df = Nicolas_df.copy()
compare_df.drop(columns=['ICC_REM','ID_GROUP_WL'], axis=1, inplace=True)
compare_df['Nicolas_match'] = pd.to_numeric(Nicolas_df['Nicolas_match'], errors='coerce')
compare_df['Bertille_match'] = Bertille_df['ID_GROUP_ICC']
compare_df['same'] = compare_df.apply(lambda x : True if x.Nicolas_match == x.Bertille_match else False, axis = 1)
print(compare_df.head())
print(compare_df['same'].value_counts())
m = compare_df.loc[compare_df['same'] == False]
m.to_csv("../../../data/WL/compare_Bertille_Nicolas.csv")

'''
Nicolas_df['ICC1.1'] = Nicolas_df['ICC1.1'].apply(lambda x: x if (x not in ['#indef','#exclude', 'n']) else np.nan)
Nicolas_df['Nicolas_match'] = Nicolas_df['ICC1.1'].astype('str').str[:1].astype('int')
Nicolas_df.drop(['ICC1.1'], axis = 1, inplace = True)
Nicolas_df['Bertille_match'] = Bertille_df['ID_GROUP_ICC']
Nicolas_df['same'] = Nicolas_df.apply(lambda x : True if x.Nicolas_match == x.Bertille_match else False, axis = 1)
print(Nicolas_df.head())
#my_list = []
#Nicolas_df['Nicolas_match'].apply(lambda x : x if x is)
'''