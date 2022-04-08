import csv 
import pandas as pd
import numpy as np
import itertools
from fuzzywuzzy import fuzz, process

#list of class names of the source data
srcAttributes=['GROUP_FR', 'CROPS_FR']

#list of class names of the target data
jcmAttributes=['GROUP_fr', 'CROPS_fr', 'SUB-CROPS_fr', 'SUB-SUB-CROPS_fr']

#list of words not discriminatory to filter
notDiscrimnantWords = ["à", "de", "ou", "et"]

#list of resuts. To avoid adding rows to the resulting panda dataframe one by one (takes a lot of energy), we will add all rows in one time into the resulting dataframe, using this list as an intermediary.
resultList = [] # example : [['BRO',3,0.8]]

#initialize 2 empty pandas dataframes : srcDf stands for source dataframe and jcmDf for jecam dataframe. 
srcDf = pd.DataFrame()
jcmDf = pd.DataFrame()


#to pass from a classification from a country/region and from a specific year to a unified/european one, the user should call the following function
def converter(country, year):
    global jcmDf
    genericPath = '../../data/'
    #read the origin data into a pandas dataframe. 
    srcDf = pd.read_csv(genericPath + '/' + country + '/' + country + '_' + year + '.csv')
    #read the target data into a pandas dataframe. Until now and in this whole script, the target data is JECAM classification. 
    jcmDf = pd.read_csv(genericPath + '/' + 'JECAM/JECAM_fr.csv')
    #create the conversion table into the folder of the country/region we are working with
    specificPath = country + '/conversionTable_'+ country + '.csv'
    path = genericPath + specificPath


    '''srcDf.apply(
    lambda rowS: scanSource(rowS), axis=1
    )'''
    print(srcDf)
    for line in srcDf.itertuples():
        scanSource(line)    

    #order list from the higher to the lower group by id_Crops_fr
    conversionDf = pd.DataFrame(resultList, columns=['ID_CROPS_FR', 'ID_GROUP_JECAM', 'similarity'])
    conversionDf.to_csv(path)

def scanSource(rowS):
    print('---------------------------------------begin scan source')
    print(f" type {type(rowS)}")
    print(rowS)
    print(rowS[1])
    for srcClass in srcAttributes: 
        print(type(srcClass))
        scanTarget(srcClass,rowS)
        if rowS.srcClass in [item[0] for item in resultList]:
            break
        else: 
            if index(srcClass) == len(srcAttributes)-1:
                return print('zero matching have been found') #for the value : ' + value)

def scanTarget(srcClass,rowS):
    print('---------------------------------------begin scan target')
    #for every level of JECAM classification
    print(rowS)
    for jcmClass in jcmAttributes: 
        print("I am in the first loop")
        print(jcmClass)
        for rowT in jcmDf.itertuples():
            print(rowT)
            print(type(rowT))
            print("I am in the secondloop")
            nb = matching(rowS.srcClass, rowT.jcmClass)  
    print('---------------------------------------end scan target')    

def matching(s,t): 
    print('---------------------------------------begin scan target')
    #First idea : to use .contains method
    #srcDf[srcDf[].str.contains(word)]

    #Second idea : use fuzz.token_sort_ratio
    nb = fuzz.token_sort_ratio(s,t)
    print(nb)
    if nb != 0: 
        resultList.append(s.ID_CROPS_FR, t.ID_GROUP, nb)
    return nb

converter("FR", "2020")
'''for trg in jcmDf.itertuples():
    print(trg)

print(jcmDf)'''