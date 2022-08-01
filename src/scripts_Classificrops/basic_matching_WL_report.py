#script to test similarity function on Wallonia group and France. Illustration of how matching function works for the report. 
import pandas as pd
from fuzzywuzzy import fuzz
import numpy as np
import deepl

#download the source classification and keep only the classes. Class is understood an a synonym of group, or parent. 
#In this code we will work with Wallonia and France classification. 
def download_src_df(path, place):    
    df = pd.read_csv(path)
    df = df.filter(['GROUP_'+place])
    src_df = df.drop_duplicates(subset = ['GROUP_'+place])
    src_df.reset_index(drop=True, inplace = True)
    src_df['GROUP_'+place] = src_df['GROUP_'+place].str.lower()
    #return the 8 first classes available in the source dataframe, Their names are stored into the columns 'GROUP_'+place. For Wallonia, for example : 'GROUP_WL'
    return src_df.head(8)

WL_df = download_src_df('/home/BTemple-Boyer-Dury/Documents/Classificrops/data/WL/WL_2020.csv', 'WL')
FR_df = download_src_df('/home/BTemple-Boyer-Dury/Documents/Classificrops/data/FR/FR_2020.csv', 'FR')

#download icc classification, and translate it toward the language of the source classification. 
lg = 'fr'
icc_df = pd.read_csv("/home/BTemple-Boyer-Dury/Documents/Classificrops/data/ICC/ICC_group.csv")
DEEPL_AUTH_KEY = "47c6c989-9eaa-5b30-4ee6-b2e4f1ebd530:fx"
translator = deepl.Translator(DEEPL_AUTH_KEY)
icc_df['label_'+lg] = icc_df['label_en'].apply(lambda group: translator.translate_text(group, target_lang=lg.upper()) if (pd.notna(group)) else group)

def match_row_row(src, trg): 
    #we use the similarity function defined by the module fuzz : token_set_ratio as it was described above in the report. 
    nb = fuzz.ratio(str(src), str(trg))
    #as a starting point, we say that the source row and the target row should be similar at least at 60% to say there is a match
    if nb > -1:
        return (trg, nb)
    else: 
        return('null', 0)

def match_row_df(word_src, df_target):     
    #compute similarity between word_source and class for each class from icc classification
    result = [match_row_row(word_src, trg) for trg in df_target['label_fr']]
    my_list = list(filter(None, result))
    result_max = sorted(my_list,key=lambda x: x[1], reverse=True)[0]
    #this function returns a tuple (group_icc_matched, similarity) with the group icc matched that has the best similarity score (and that is > to 60)
    return result_max

def match(src_df,place): 
    src_df['result'] = src_df['GROUP_'+place].apply(lambda group : match_row_df(group, icc_df))
    src_df['GROUP_icc'], src_df['similarity'] = src_df.result.str
    src_df = src_df.filter(['GROUP_'+place, 'GROUP_icc', 'similarity'])
    #this function returns the source dataframe with one column added  that stores the icc group matched, and one column that contains the similarity score. 
    return src_df

WL_df = match(WL_df, 'WL')
FR_df = match(FR_df, 'FR')

print(WL_df)
print(FR_df)