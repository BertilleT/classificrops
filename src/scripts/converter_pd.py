import csv 
import pandas as pd
import numpy as np
import itertools
from fuzzywuzzy import fuzz, process


'''class match: 
    level: #level of match : 1.1|1.2|1.3|1.4|2.1|2.2|2.3|2.4
    full_match: #TRUE|FALSE
    src_words:
    src_id: 
    target_words:
    target_id:'''

#list of class names of the source data
srcAttributes=['GROUP_FR', 'CROPS_FR']

#list of class names of the target data
jcmAttributes=['GROUP_fr', 'CROPS_fr', 'SUB-CROPS_fr', 'SUB-SUB-CROPS_fr']

#list of words not discriminatory to filter
notDiscrimnantWords = ["à", "de", "ou", "et"]

#list of resuts. To avoid adding rows the resulting panda dataframe one by one (takes a lot of energy), we will add all rows in one time into the resulting dataframe, thanks to this list.
resultList = []

#initialize 2 empty pandas dataframes : srcDf stands for source dataframe and jcmDf for jecam dataframe. 
srcDf = pd.DataFrame()
jcmDf = pd.DataFrame()

#to pass from a classification from a country/region and from a specific year to a unified/european one, the user should call the following function
def converter(country, year):
    genericPath = '../../data/'

    #read the origin data into a pandas dataframe. 
    srcDf = pd.read_csv(genericPath + '/' + country + '/' + country + '_' + year + '.csv')

    #read the target data into a pandas dataframe. Until now and in this whole script, the target data is JECAM classification. 
    jcmDf = pd.read_csv(genericPath + 'JECAM/JECAM_fr.csv')

    #create the conversion table into the folder of the country/region we are working with
    specificPath = country + '/conversionTable_'+ country + '.csv'
    path = genericPath + specificPath
    '''print("srcDf.GROUP_FR.unique() : ")
    print(srcDf.GROUP_FR.unique())
    print('-------------------------------------------')
    print(srcDf.columns)
    print(jcmDf.head)'''

    for i,rowS in srcDf.iterrows(): 
        '''print('i')
        print(i)
        print('-------------------------------------------')
        print('rowS')
        print(rowS)
        print('-------------------------------------------')
        print('srcDf.loc[i,srcDf.GROUP_FR[i]]')
        print(srcDf.loc[i,srcDf.GROUP_FR[i]])'''
        scanSource(i,rowS)

    #order list from the higher to the lower group by id_Crops_fr
    conversionDf = pd.DataFrame(resultList, columns=['ID_CROPS_FR', 'ID_GROUP_JECAM', 'matching'])
    conversionDf.to_csv(path)

def scanTarget(s,rowS):
    #the condition below is dedicated to stop the recursive loop from scanSource() when all source attributes have been scanned and no matching have been found. 
    if s != len(srcAttributes): 
        #for every level of JECAM classification
        for t in range(len(jcmAttributes)-1): 
            jcmLevel = jcmAttributes[t]
            for rowT in jcmDf: 
                nb = matching(rowS.srcLevel,rowT.jcmLevel)
                '''if nb == 1: #if match at 100%, then we stop to scan other words in tergetted classes, and go to the follwing crop in source data. break all the nested loops
                    break  '''
    else:
        #match.result.append(null) 
        print('zero matching have been found') #for the value : ' + value)


def scanSource(i,rowS):
    s=0
    srcLevel = srcAttributes[s]
    '''print('srcLevel')
    print(srcLevel)
    print('-------------------------------------------')
    print('type(srcLevel)')    
    print(type(srcLevel))
    print('-------------------------------------------')'''
    scanTarget(s,rowS)
    '''L=[]
    for item in resultList:
        L.append(item[0])'''
    print(rowS)

    if rowS['ID_CROPS_FR'] not in [item[0] for item in resultList]:
        #match.result != [] -- this condition could be replaced by something like : if maximum match pourcentage already found is superior to 50 %
        return scanSource(i,s+1)#add value to df conversion

def matching(s,t): 
    #First idea : to use .contains method
    #srcDf[srcDf[].str.contains(word)]

    #Second idea : use fuzz.token_sort_ratio
    nb == fuzz.token_sort_ratio(s,t)
    if nb != 0: 
        resultList.append(s.ID_CROPS_FR, t.ID_GROUP, nb)
    return nb

converter("FR", "2020")
