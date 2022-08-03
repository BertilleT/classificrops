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

def spread(place, src_df2,x,c):
    m = src_df2.loc[src_df2[c] == x[c],'match']
    return m.iloc[0]

def max(matches_list):
    t = [np.nan, 0]       
    for l in matches_list:
        if l[1] > t[1]:
            t = l
    return t

def match(src_df,place):     
    #match at source level = GROUP (parent)
    c = 'GROUP_' + place
    src_df2 = src_df.drop_duplicates(subset = [c])
    #create a column match in src_df2 to store the match
    src_df2['match'] = src_df2[c].apply(lambda group: match_row_df(group, icc_df))
    #spread the match identified at source parent level to the child crops of this parent.  
    src_df['match'] = src_df.apply(lambda x: spread(place, src_df2,x,c))
    
    #match df source at level = CROPS (child)
    c = 'CROPS_' + place
    #in srcv_df2 concatenate the result already get in match at column level + the match get at crops level
    src_df['match'] = src_df[c].apply(lambda crop: crop['match'] + match_row_df(crop, icc_df))
    src_df["max_match"] = src_df.apply(lambda x: max(x.match))
    src_df['GROUP_ICC'] = src_df.apply(lambda x : x['max_match'][0])
    src_df['sim'] = src_df.apply(lambda x : x['max_match'][1])
    return src_df

FR_df = match(FR_df, 'FR')