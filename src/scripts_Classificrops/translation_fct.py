##PSEUDO-CODE
#translation functions definition
import pandas as pd
import numpy as np
import deepl
import googletrans
from googletrans import Translator

def translate_word(translator, word, language):
    result = translator.translate_text(word, target_lang=language.upper())
    return result

def deepl_translate_ICC(df, lg):
    #the DEEPL_AUTH_KEY is a string containing my API authentication key that I generated from my Deepl account
    #the authentication key is fetched from an environment variable
    translator = deepl.Translator(DEEPL_AUTH_KEY)
    df["label_"+lg] = df["label_en"].apply(lambda crop: translate_word(translator, crop, lg) if (pd.notna(crop)) else crop, axis = 1)
    return df["label_"+lg]

def googletrans_translate_ICC(df, lg):
    translator = Translator()
    df['label_']+lg = df['label_en'].apply(lambda crop : translator.translate(crop, dest = lg))
    df['label_'+lg+'_str'] = df['label_'+lg].astype(str)
    df['label_'+lg] = df['label_'+lg+'_str'].apply(lambda x : x.split(',')[2].split('=')[1])
    return df['label_']+lg