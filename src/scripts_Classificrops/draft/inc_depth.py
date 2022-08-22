#depth +1 when other more than 10 %

import pandas as pd
from scripts_Classificrops.draft.converter_v1 import *
icc_df = pd.read_csv('/home/BTemple-Boyer-Dury/Documents/Classificrops/data/ICC/ICC_src.csv')
print(icc_df)
print(icc_df.dtypes)

#LEVEL_0 = icc_df.loc[icc_df.loc[:,'code'].str.contains('.')]
#LEVEL_0 = icc_df.loc[len(icc_df.loc[:,'code'])==1]

#print(LEVEL_0)

icc_df['code'] = icc_df['code'].astype('str')
mask_0 = (icc_df['code'].str.len() == 1)
LEVEL_0 = icc_df.loc[mask_0]
print(LEVEL_0)

icc_df['broader'] = icc_df['broader'].astype('str')
mask_1 = (icc_df['broader'].str.len() == 1)
LEVEL_1 = icc_df.loc[mask_1]
print(LEVEL_1)

def inc_depth():
    