import csv 
import pandas as pd
import numpy as np
import itertools
from fuzzywuzzy import fuzz, process

#load the source dataframe
srcDf = pd.read_csv('../../data/FR/FR_2020.csv')

#load the target dataframe
iccDf = pd.read_csv('../../data/ICC/ICC_fr.csv')

resultList = [] 

#transform the code "1.34.28" from indicative crop classification into "13428" to work with integers. 
def parserICCCode(x):
    return "".join(x.split('.'))

iccDf['code'] = iccDf['code'].apply(lambda code:parserICCCode(code))
iccDf['code'] = iccDf['code'].astype('int')

#select the first digit of the code, which corresponds to the group crop code
iccDf['group_code'] = iccDf['code'].astype('str').str[:1].astype('int')

resultDf = srcDf[['ID_CROPS_FR','ID_GROUP_FR']]
print(resultDf)

def scanTarget(c, idS,g):
    iccDf.apply(lambda x: matching(c, idS,g,x.label_fr,x.group_code), axis=1)

def matching(c,idS,src,trg,idT): 
    nb = 0
    nb = fuzz.ratio(src,trg)
    if nb > 75: 
        resultList.append([c,idS, src, trg, idT, nb])
        #resultList.append([idS, idT, nb])

srcClasses=[]
columns = list(srcDf)
for col in columns:
    if 'ID' not in col: 
        srcClasses.append(col)

for c in srcClasses: 
    srcDf2 = srcDf.drop_duplicates(subset = ['ID_' + c])
    srcDf2.apply(lambda x:scanTarget(c,x['ID_' + c],x[c]), axis=1)
    if 'ID_' + c in resultList[:][1]:
        break




cols = ['class_level_src', 'id_src',' words_src', 'words_trg', 'id_trg', 'similarity']
matchingDf = pd.DataFrame(resultList, columns=cols)
print(matchingDf)

#my variables : resultDf.ID_CROPS_FR, resultDf.ID_GROUP_FR,  resultDf.ID_GROUP_ICC, matchingDf.class_level_src, matchingDf.id_src, matchingDf.id_trg
#if there is a match at group source level, then all the crops into this group src should herit the matching target group found for the father group. 

def fct2(id_src,id_trg):
    resultDf.loc[resultDf.ID_GROUP_FR == id_src, 'ID_GROUP_ICC'] = id_trg

rows = matchingDf.loc[matchingDf['class_level_src'] == 'GROUP_FR']
r = rows.apply(lambda x: fct2(x.id_src, x.id_trg), axis=1)

print(resultDf.head(50))

#my variables : resultDf.ID_GROUP_ICC, resultDf.ID_CROPS_FR, matchingDf.id_src, matchingDf.id_trg
missings = resultDf['ID_GROUP_ICC'].isna()
#missings = missings['ID_GROUP_ICC', 'ID_CROPS_FR']
#print(type(missings)) #missings is a pandas serie
print(missings)

mis = missings.loc(True)
print(mis.head(50))

def fct(resultGroupFound,id_src_crop): 
    if resultGroupFound == 'NaN':
        print('hey')
        i = matchingDf.loc[matchingDf.id_src == id_src_crop]
        return i.id_trg

resultDf.apply(lambda x: x.ID_GROUP_ICC == fct(x.ID_GROUP_ICC, x.ID_CROPS_FR), axis=1)