import pandas as pd
import os
import geopandas as gpd
import numpy as np

import googletrans
from googletrans import Translator

translation_df = pd.read_excel('../../data/CAT/translation.xlsx')

translator = Translator()
source_df = gpd.read_file("/home/BTemple-Boyer-Dury/Documents/Classificrops/data/CAT/Cultius_DUN2020_GPKG/Cultius_DUN2020.gpkg")
source_df.drop_duplicates(subset=['Cultiu'], inplace = True)
catalan_df = source_df[['Grup', 'Cultiu']]

print(catalan_df.head())
print(list(catalan_df.columns))


catalan_df['CROPS_CAT_fr'] = catalan_df['Cultiu'].apply(lambda x : translator.translate(x, src='ca',dest = 'fr').text)

catalan_df.to_csv("trad_fr.csv")
