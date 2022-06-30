from calendar import c
import pandas as pd
import googletrans
from googletrans import Translator
import numpy as np
import translators as ts
ts.google

catalan_df = pd.read_csv('../../data/CAT/CAT_2020.csv')
catalan_df.drop_duplicates(subset=['CROPS'], inplace = True)


translated_dict = pd.read_csv('../../data/CAT/translation.csv')
print(catalan_df.head())
print(translated_dict.head())
print(list(catalan_df.columns))
print(catalan_df['CROPS'])

print(catalan_df.dtypes)
translator = Translator()
catalan_df['CROPS_CAT_fr'] = catalan_df.apply(lambda x : xtranslator.translate(x['CROPS']).text)# if x['CROPS']!=[] else np.nan)
print(catalan_df.head())
print(googletrans.LANGUAGES)
print(ts._google.language_map)

#catalan_df['CROPS_CAT_fr'] = catalan_df['CROPS'].apply(lambda x: ts.google(x, from_language='en', to_language='cy'))