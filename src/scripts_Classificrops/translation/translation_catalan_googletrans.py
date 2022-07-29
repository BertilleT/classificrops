import pandas as pd
import os
import geopandas as gpd
import numpy as np

#import googletrans
from googletrans import Translator
translator = Translator()

cat_classification = pd.read_csv('/home/BTemple-Boyer-Dury/Documents/Classificrops/data/CAT/CAT_classification_src.csv')

print(cat_classification.head())

icc_df = pd.read_csv('/home/BTemple-Boyer-Dury/Documents/Classificrops/data/ICC/ICC.csv')
print(icc_df.head())

icc_df['label_c'] = icc_df['label_en_filtered'].apply(lambda x : translator.translate(x, dest = 'ca'))

print(icc_df.head())
print(icc_df.dtypes)
icc_df['label_c_str'] = icc_df['label_c'].astype(str)
icc_df['label_cat_filtered'] = icc_df['label_c_str'].apply(lambda x : x.split(',')[2].split('=')[1])
print(icc_df.head())

icc_df.drop(['label_c', 'label_c_str'], axis = 1, inplace=True)
print(icc_df.head())

icc_df.to_csv('/home/BTemple-Boyer-Dury/Documents/Classificrops/data/ICC/ICC.csv', index=False)