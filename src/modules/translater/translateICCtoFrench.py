import csv
import pandas as pd
import deepl
import os

# Create a Translator object providing your DeepL API authentication key.
# To avoid writing your key in source code, you can set it in an environment
# variable DEEPL_AUTH_KEY, then read the variable in your Python code:
translator = deepl.Translator(os.getenv("DEEPL_AUTH_KEY"))

# Translate text into a target language, in this case, French
def translate(word, language):
    result = translator.translate_text(word, target_lang=language)
    return result
    
iccDf = pd.read_csv('../../data/ICC/ICC_src.csv')
#iccDf.apply(lambda x: x['label_fr'] == translate(x['label_en']))
iccDf['label_fr'] = iccDf['label_en'].apply(lambda label_en: translate(label_en, 'fr'))
iccDf.to_csv('../../data/ICC/ICC_fr.csv')