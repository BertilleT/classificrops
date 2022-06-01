#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import pandas as pd
import deepl
from fuzzywuzzy import fuzz
import numpy as np
<<<<<<< HEAD
from pathlib import Path
=======
>>>>>>> 3f2cbac508812f96c9995d010ddefcdd997a845b

def filter(df, col, filters):
    df[col+'_filtered'] = df[col].str.replace(r"[\(\[].*?[\)\]]", '', regex=True)
    mydict = {f'(?i){word}':'' for word in filters}
    df[col+'_filtered'] = df[col+'_filtered'].replace(mydict, regex=True)
    df[col+'_filtered'] = df[col+'_filtered'].str.replace(r'[^\w\s]+', '', regex=True)
    df[col+'_filtered'] = df[col+'_filtered'].str.replace('   ', ' ')
    df[col+'_filtered'] = df[col+'_filtered'].str.replace('  ', ' ')
    df[col+'_filtered'] = df[col+'_filtered'].str.strip()
    return df[col+'_filtered']

def translate_word(translator, word, language):
    result = translator.translate_text(word, target_lang=language.upper())
    return result

def translate_ICC(df, lg):
    DEEPL_AUTH_KEY="47c6c989-9eaa-5b30-4ee6-b2e4f1ebd530:fx"
    translator = deepl.Translator(DEEPL_AUTH_KEY)
    df['label_'+lg+'_filtered'] = df['label_en_filtered'].apply(lambda crop: translate_word(translator, crop, lg) if (pd.notna(crop)) else crop)
    return df['label_'+lg+'_filtered']

def parse(x):
    return "".join(x.split('.'))

def spread(place, src_df2,x):
    m = src_df2.loc[src_df2['ID_GROUP_'+place] == x['ID_GROUP_'+place],'match']
    return m.iloc[0]

def match_row_row(c,idS,src,trg,idT,threshold,sim_method): 
    nb = 0
    if sim_method == 'token_set_ratio':
        nb = fuzz.token_set_ratio(src,trg)
    elif sim_method == 'split+ratio':
        if type(src) == str and type(trg) == str:
            src_l = src.split()
            len_src = len(src_l)
            trg_l = trg.split()
            myList=[]
            for w in src_l:
                for x in trg_l:
                    myList.append([src_l.index(w),fuzz.ratio(w,x)])
            cols = ['index', 'sim']
            myDf = pd.DataFrame(myList, columns=cols)
            r = myDf.groupby('index')['sim'].max().reset_index()
            total = r['sim'].sum()
            nb = total / len_src
    
    elif sim_method == 'split+ratio+symetric':
        nb = 0
        if type(src) == str and type(trg) == str:
            src_l = src.split()
            len_src = len(src_l)
            trg_l = trg.split()
            myList=[]
            for w in src_l:
                for x in trg_l:
                    myList.append([src_l.index(w),fuzz.ratio(w,x)])
            cols = ['index', 'sim']
            myDf = pd.DataFrame(myList, columns=cols)
            r = myDf.groupby('index')['sim'].max().reset_index()

            if len(trg_l) == 1 :
                #ranger r par ordre de similarité décroissante 
                sorted_r = r.sort_values(["sim"], ascending=False)
                #selectionner premier elment de r
                nb = sorted_r.iloc[0,1]
            else : 
                total = r['sim'].sum()
                nb = total / len_src
            #total = r['sim'].sum()
            #if len(trg_l) < len(src_l):
            #    nb = total / len(trg_l)
            #else : 
            #    nb = total / len(src_l)

    elif sim_method == 'basic':
        if src == trg:
            nb = 100

    if nb >= threshold: 
        #return the following information when there is a match : ['class_level_src', 'id_src',' words_src', 'words_trg', 'id_trg', 'similarity']
        return [c,idS, src, trg, idT, nb]
    else:
        return []

def match_row_df(lg,c,id_src,src,icc_df,threshold,sim_method):
    #in icc_df, create a column name "temp" that will be updated for each new raw of src_df
    #"temp" column stores the result matches
    icc_df['temp'] = icc_df.apply(lambda y : match_row_row(c,id_src,src,y['label_'+lg+'_filtered'],y['ID_GROUP'],threshold,sim_method), axis=1)
    my_list = icc_df['temp'].to_list()
    new_list = [e for e in my_list if e != []]
    if new_list:
        return new_list
    else:
        return []

def match_df_df(place, lg,src_df,icc_df,threshold,sim_method):
    #match df source at level = GROUP
    c = 'GROUP_' + place
    src_df2 = src_df.drop_duplicates(subset = ['ID_GROUP_' + place])
    #create a column match in srcDf2 to store the match
<<<<<<< HEAD
    src_df2['match'] = src_df2.apply(lambda x: match_row_df(lg,c, x['ID_' + c], x[c+ '_filtered'],icc_df,threshold,sim_method), axis=1)
=======
    src_df2['match'] = src_df2.apply(lambda x: match_row_df(lg,c, x['ID_' + c], x[c],icc_df,threshold,sim_method), axis=1)
>>>>>>> 3f2cbac508812f96c9995d010ddefcdd997a845b
    #spread the match identifies in src_df2 with unique values of group to the source dataframe. 
    #src_df['match'] = src_df2.apply(lambda x: spread(place, src_df,x), axis=1)
    src_df['match'] = src_df.apply(lambda x: spread(place, src_df2,x), axis=1)
    
    #CROPS
    #--------------------------------------------
    c = 'CROPS_' + place
    #in srcv_df2 concatenate the result already get in match at column level + the match get at crops level
<<<<<<< HEAD
    src_df['match'] = src_df.apply(lambda x: x['match'] + match_row_df(lg,c, x['ID_' + c], x[c+ '_filtered'],icc_df,threshold,sim_method), axis=1)
=======
    src_df['match'] = src_df.apply(lambda x: x['match'] + match_row_df(lg,c, x['ID_' + c], x[c],icc_df,threshold,sim_method), axis=1)
>>>>>>> 3f2cbac508812f96c9995d010ddefcdd997a845b
    return src_df['match']

def max(matches_list):
    t = [np.nan, np.nan, np.nan, np.nan, np.nan, 0]       
    for l in matches_list:
        if l[5] > t[5]:
            t = l
    return t

<<<<<<< HEAD
def compare(handmade_path,computed,threshold):
    handmade = pd.read_csv(handmade_path)
=======
def compare(pathHandMade,computed,threshold):
    handmade = pd.read_csv(pathHandMade)
>>>>>>> 3f2cbac508812f96c9995d010ddefcdd997a845b
    compare = handmade.copy()
    compare.rename(columns={'ID_GROUP_ICC':'ID_GROUP_ICC_handmade'}, inplace=True)
    compare['ID_GROUP_ICC_computed'] = computed['ID_GROUP_ICC']
    compare2=compare.copy()

    booleanSerie = compare.apply(lambda x : True if (x.ID_GROUP_ICC_handmade==x.ID_GROUP_ICC_computed) else False,axis=1)
    booleanSerie2 = compare2.apply(lambda x : True if not (np.isnan(x.ID_GROUP_ICC_computed)) and (x.ID_GROUP_ICC_handmade!=x.ID_GROUP_ICC_computed)  else False,axis=1)
    booleanDf = booleanSerie.to_frame()
    booleanDf2 = booleanSerie2.to_frame()
    booleanDf = booleanDf.rename(columns = {0:'bool'})
    booleanDf2 = booleanDf2.rename(columns = {0:'bool'})

    tot = len(compare)
    match = booleanDf['bool'].sum()
    error = booleanDf2['bool'].sum()
    per = round((match*100)/tot)
    err = round((error*100)/tot)

    print('The conversion table computed with the threshold = ' + str(threshold) + ', fits to the expected output at ' + str(per) + '%.')
    print('The conversion script made '+str(err)+'%'+' of errors.')
    return (threshold, per, err)

<<<<<<< HEAD
def converter(src_file, place, lg, threshold,sim_method):
    src_classes = ['GROUP','CROPS']
    parent = Path(__file__).parents[2]
    data_path = parent.joinpath('data')
    ICC_path = data_path.joinpath('ICC','ICC.csv')

    src_path = data_path.joinpath(place, src_file)
    ##Loading
    src_df = pd.read_csv(src_path)
    icc_df = pd.read_csv(ICC_path)
=======
def converter(path_csv, place, lg, threshold,sim_method):
    src_classes = ['GROUP','CROPS']
    rel_path_ICC = '../../data/ICC/ICC.csv'
    abs_path_ICC = os.path.abspath(rel_path_ICC)
    target = abs_path_ICC

    ##Loading
    src_df = pd.read_csv(path_csv)
    icc_df = pd.read_csv(target)
>>>>>>> 3f2cbac508812f96c9995d010ddefcdd997a845b

    ##Listing classes
    src_classes = [c+'_'+place for c in src_classes]

    ##Filtering1a
    if 'label_en_filtered' not in list(icc_df.columns): 
        englishFilters1=['n.e.c.', 'spp','n.e.c']
        icc_df['label_en_filtered'] = filter(icc_df,'label_en',englishFilters1)
        icc_df.replace('',np.nan,regex = True,inplace=True)

    ##Translating
    if 'label_'+lg+'_filtered' not in list(icc_df.columns):
        icc_df['label_'+lg+'_filtered'] = translate_ICC(icc_df, lg)
        icc_df.to_csv(target, index=False)

    #the ICC filtering is divided into 2 parts because if you do it in one step before translating
    #you get "Grasses and other fodder crops" that becomes "Grasses fodder" translated into 
    #"Fourrage de graminées whereas it should be translated into "Fourrages et graminées" or into "Fourrages graminées". 
    
    ##Filtering1b
    if 'label_en_filtered' not in list(icc_df.columns): 
        englishFilters2=['other','crops',' and',' or']
        icc_df['label_en_filtered'] = filter(icc_df,'label_en_filtered',englishFilters2)
        icc_df.replace('',np.nan,regex = True,inplace=True)

    ##Filtering2
    french_filters = ['autres','autre',' et',' ou']
    #we should deal with all the languages ... 
    for c in src_classes:
        src_df[c+'_filtered'] = filter(src_df,c,french_filters)
        src_df.replace('',np.nan,regex = True,inplace=True)
        if 'ID_'+c not in list(src_df.columns):
            src_df['ID_'+c] = src_df[c] #we could make an identifier generator more sophisticated in the future. example : take the 3 first letters. 

    ##Formating ICC
    icc_df['ID'] = icc_df['ID'].apply(lambda ID:parse(ID))
    icc_df['ID'] = icc_df['ID'].astype('int')
    icc_df['ID_GROUP'] = icc_df['ID'].astype('str').str[:1].astype('int')

    ##Matching all
    src_df['match'] = match_df_df(place,lg,src_df,icc_df,threshold,sim_method)
    
    src_df["max_match"] = src_df.apply(lambda x: max(x.match) if x.match != [] else [], axis = 1)

    src_df['ID_GROUP_ICC'] = src_df.apply(lambda x : x['max_match'][4] if x['max_match'] != [] else np.nan, axis = 1)
    src_df['sim'] = src_df.apply(lambda x : x['max_match'][5] if x['max_match'] != [] else np.nan, axis = 1)

    result_df = src_df[['ID_CROPS_'+place, 'ID_GROUP_ICC']]

    #Writting result
<<<<<<< HEAD
    result_path = data_path.joinpath(place,'conversion_table_'+place+'_scriptMade.csv')
    result_df.to_csv(result_path, index=False)

    result_df['ID_GROUP_ICC'] = result_df.loc[:, ['ID_GROUP_ICC']].astype(float)
    details_path = data_path.joinpath(place,'match_df_detailed_'+place+'.csv')
    src_df.to_csv(details_path, index=False)

    handmade_path = data_path.joinpath(place,'conversion_table_'+place+'_handmade.csv')
    print(handmade_path)
    return compare(handmade_path,result_df,threshold)

#converter('../../data/FR/FR_2020.csv', 'FR','fr', 60,'split+ratio')

converter('FR_2020.csv', 'FR','fr', 90,'split+ratio')

#print(hey)
=======
    rel_path_result = '../../data/'+place+'/conversionTable_'+place+'_scriptMade.csv'
    abs_path_result = os.path.abspath(rel_path_result)
    result_df.to_csv(abs_path_result, index=False)

    result_df['ID_GROUP_ICC'] = result_df.loc[:, ['ID_GROUP_ICC']].astype(float)
    rel_path_det = '../../data/'+place+'/match_df_detailed_'+place+'.csv'
    abs_path_det = os.path.abspath(rel_path_det)
    src_df.to_csv(abs_path_det, index=False)
    
    rel_path_handmade = '../../data/'+place+'/conversionTable_'+place+'_handMade.csv'
    abs_path_handmade = os.path.abspath(rel_path_handmade)
    return compare(abs_path_handmade,result_df,threshold)

#converter('../../data/FR/FR_2020.csv', 'FR','fr', 60,'split+ratio')
hey = converter('data/WL/WL_2020.csv', 'WL','fr', 1,'basic')

print(hey)
>>>>>>> 3f2cbac508812f96c9995d010ddefcdd997a845b
