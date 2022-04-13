import csv 
import pandas as pd
import numpy as np
import itertools
from fuzzywuzzy import fuzz, process

resultList = [] # example : [['BRO',3,0.8]]

srcDf = pd.read_csv('../../data/FR/FR_2020.csv')
srcDf2 = srcDf.drop_duplicates(subset = ["GROUP_FR"])

jcmDf = pd.read_csv('../../data/JECAM/JECAM_fr.csv')
columns = list(jcmDf) 
levelsT = []
IDsT = []
for c in columns: 
    if '_fr' in c:
        levelsT.append(c)
    if 'ID_' in c:
        IDsT.append(c)
jcmLevelsDf = jcmDf[levelsT]
jcmIDsDf = jcmDf[IDsT]

print (jcmLevelsDf)
print (jcmIDsDf)

def scanTarget(g, idS):
    for jcmClass in levelsT: 
        jcmDf2=jcmDf.drop_duplicates(subset = jcmClass)
        idT = 'ID_' + jcmClass[:-3]
        print(idT)
        #print('--------------------------------------------scanTarget is launched')
        print(jcmDf2.dtypes)
        jcmDf2.apply(lambda x: matching(idS,g,x[jcmClass],jcmClass,x[idT]), axis=1)

def matching(idS,g,c,l,idT): 
    '''print('source : ')
    print(g)
    print('target : ')
    print(c)'''
    nb = 0
    #print(c)
    if c != 'NaN' and c != 'NaN':
        print(type(c))
        #print('--------------------------------------------fuzz_ratio is called')
        nb = fuzz.ratio(g,c)
        #rint(nb)
        if nb > 75: 
            resultList.append([idS, g, c, l, nb, idT])

srcDf2.apply(lambda x:scanTarget(x.GROUP_FR, x.ID_GROUP_FR), axis=1)
print(resultList)