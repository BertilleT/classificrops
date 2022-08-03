#simplified piece of code to translate icc classification in another language using deepl API

import pandas as pd
import deepl
from googletrans import Translator

lg = input("Language of the source classification ? ") 
ICC_path = input("ICC path ? ") 
icc_df = pd.read_csv(ICC_path)

def translate_word(translator, word, language):
    result = translator.translate_text(word, target_lang=language.upper())
    return result

def deepl_translate(df, lg):
    #the DEEPL_AUTH_KEY is a string containing my API authentication key that I generated from my Deepl account
    #the authentication key is fetched from an environment variable
    translator = deepl.Translator(DEEPL_AUTH_KEY)
    df["label_"+lg] = df["label_en"].apply(lambda crop: translate_word(translator, crop, lg) if (pd.notna(crop)) else crop)
    return df["label_"+lg]


def google_translate(df, lg):
    translator = Translator()
    df["label_"+lg] = df["label_en"].apply(lambda x : translator.translate(x, dest = lg))
    df["label_"+lg] = df["label_"+lg].astype(str)
    df["label_"+lg] = df["label_"+lg].apply(lambda x : x.split(',')[2].split('=')[1])
    return df["label_"+lg]

#if the ICC classification have not been translated yet into the language of the source classification : 
if "label_"+lg not in list(icc_df.columns) :
    #list source languages available with deepl API
    source_languages = []
    for l in translator.get_source_languages():
        source_languages.append(l.code)
    #if the language of the source classification under study is available with Deepl API
    if lg.upper() in source_languages:
        icc_df["label_"+lg] = deepl_translate(icc_df,lg)
    #if not, we should use another solution, as the Google Translate API (googletrans)
    else: 
        icc_df["label_"+lg] = google_translate(icc_df,lg)
    #add the translation to the origin csv file to avoid retranslating classes already translated in previous iterations. 
    icc_df.to_csv(ICC_path, index = False)
