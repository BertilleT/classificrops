import csv 
import pandas as pd
import numpy as np
import itertools
from fuzzywuzzy import fuzz, process

srcDf = pd.read_csv('../../../data/FR/FR_2020.csv')
iccDf = pd.read_csv('../../../data/ICC/ICC_fr.csv')
def parserICCCode(x):
    return "".join(x.split('.'))

iccDf['code'] = iccDf['code'].apply(lambda code:parserICCCode(code))
iccDf['code'] = iccDf['code'].astype('int')

#this script is dedicated to filter non discriminatory words as "and", and punctuations in the classification under study.
#when looking at ICC we identify : 'n.e.c.' ',', '(', ')', ',', '.', '-', 'spp'=several species, 'other', 'crops', 'and', 'or'
#when it comes to french classification, we identify '/'

#we will use regular expressions

def filter(df, col):
    mylist=['other','crops',' and ',' or ',' n.e.c.', ' spp'] #we should retrieve one word + one space before or after the word if there is one
    mydict = {f'(?i){word}':'' for word in mylist}
    #mydict['[:-]'] = ''
    df[col] = df[col].replace(mydict, regex=True)
    df[col] = df[col].str.replace(r'[^\w\s]+', '')
    return df[col]
print(iccDf.head(50))
iccDf.labels_en = filter(iccDf,'label_en')
print(iccDf.head(50))

