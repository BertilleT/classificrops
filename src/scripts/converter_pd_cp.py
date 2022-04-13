import csv 
import pandas as pd
import numpy as np
import itertools
from fuzzywuzzy import fuzz, process

resultList = [] 

srcDf = pd.read_csv('../../data/FR/FR_2020.csv')
srcDf2 = srcDf.drop_duplicates(subset = ["GROUP_FR"])
iccDf = pd.read_csv('../../data/ICC/ICC_fr.csv')

#transform the code "1.34.28" into "13428" to work with integers. 
def parserICCCode(x):
    return "".join(x.split('.'))

iccDf['code'] = iccDf['code'].apply(lambda code:parserICCCode(code))
iccDf['code'] = iccDf['code'].astype('int')

#select the first digit of the code, which corresponds to the group crop code
iccDf['group_code'] = iccDf['code'].astype('str').str[:1].astype('int')

def scanTarget(idS,g):
    iccDf.apply(lambda x: matching(idS,g,x.label_fr,x.group_code), axis=1)

def matching(idS,src,trg,idT): 
    nb = 0
    nb = fuzz.ratio(src,trg)
    if nb > 75: 
        #resultList.append([idS, src, trg, idT, nb])
        resultList.append([idS, idT, nb])

#def scanSource():


srcDf2.apply(lambda x:scanTarget(x.ID_GROUP_FR,x.GROUP_FR), axis=1)
print(resultList)