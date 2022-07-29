import pandas as pd
import numpy as np

detail_cat = pd.read_csv("/home/BTemple-Boyer-Dury/Documents/Classificrops/data/result/match_df_detailed_CAT.csv")
hd = pd.read_csv("/home/BTemple-Boyer-Dury/Documents/Classificrops/data/CAT/handmade_Nicolas_light.csv")
print(detail_cat.head())
print(hd.head())

def fct(x): 
    return hd.apply(lambda y: y['ICC1.1'][:1] if y['ID_CROPS_CAT'] == x['CROPS_CAT'] else y, axis = 1)[0]


detail_cat["ID_GROUP_ICC_handmade"] = detail_cat.apply(lambda x : fct(x), axis = 1)
print(detail_cat.head())