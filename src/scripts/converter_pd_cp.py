import csv 
import pandas as pd
import numpy as np
import itertools
from fuzzywuzzy import fuzz, process

#list of class names of the target data
jcmAttributes=['GROUP_fr', 'CROPS_fr', 'SUB-CROPS_fr', 'SUB-SUB-CROPS_fr']

resultList = [] # example : [['BRO',3,0.8]]

srcDf = pd.read_csv('../../data/FR/FR_2020.csv')
jcmDf = pd.read_csv('../../data/JECAM/JECAM_fr.csv')
columns = list(jcmDf) 
#print(columns)
srcDf2 = srcDf.drop_duplicates(subset = ["GROUP_FR"])
print(srcDf2)

def scanTarget(g):
    for jcmClass in columns: 
        jcmDf2=jcmDf.drop_duplicates(subset = jcmClass)
        #print(g)
        #print(jcmDf2[jcmClass])
        #print('--------------------------------------------scanTarget is launched')
        jcmDf2.apply(lambda x: matching(g,x[jcmClass],jcmClass), axis=1)

def matching(g,c,l): 
    '''print('source : ')
    print(g)
    print('target : ')
    print(c)'''
    nb = 0
    #print(c)
    if c != 'NaN' and type(c) == str:
        #print('--------------------------------------------fuzz_ratio is called')
        nb = fuzz.ratio(g,c)
        #rint(nb)
        if nb > 75: 
            resultList.append([g, c, l, nb])

srcDf2.apply(lambda x:scanTarget(x.GROUP_FR), axis=1)
print(resultList)