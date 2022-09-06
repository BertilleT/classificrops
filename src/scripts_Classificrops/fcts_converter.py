#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import deepl
from fuzzywuzzy import fuzz
import numpy as np
from pathlib import Path

def filter(df, col, filters):
    return df[col+'_filtered']

def translate_word(translator, word, language):
    return result

def translate_ICC(df, lg):
    return df['label_'+lg+'_filtered']

def parse(x):
    return "".join(x.split('.'))

def spread(place, src_df2,x):
    return m.iloc[0]

def match_row_row(c,idS,src,trg,idT,threshold,sim_method): 
    if nb >= threshold: 
        #return the following information when there is a match : ['class_level_src', 'id_src',' words_src', 'words_trg', 'id_trg', 'similarity']
        return [c,idS, src, trg, idT, nb]
    else:
        return []

def match_row_df(lg,c,id_src,src,icc_df,threshold,sim_method):
    if new_list:
        return new_list
    else:
        return []

def match_df_df(place, lg,src_df,icc_df,threshold,sim_method):
    return src_df['match']

def max(matches_list):
    return t

def converter(src_path_input, place, lg, threshold = 90,sim_method = 'split+ratio+symetric', src_df = None, icc_df = None, opt=None):
    print(result_path)
        return (result_df)
