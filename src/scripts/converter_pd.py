import csv 
import pandas as pd

class match: 
    attribut_origin: ''
    attribut_target: ''
    result: []

def converter(country, year):
    #read the origin data from France into a panda dataframe
    genericPath = '../../data/'
    srcDf = pd.read_csv(genericPath + '/' + country + '/' + country + '_' + year + '.csv')
    jcmDf = pd.read_csv(genericPath + 'JECAM/JECAM_fr.csv')

    #create the conversion table into the folder of the country/region we are working with
    specificPath = country + '/conversionTable_'+ country + '.csv'
    path = genericPath + specificPath
    #df.converion.to_csv(path)

    print(srcDf.head)
    print(jcmDf.head)

    sourceAttributes=['GROUP', 'CROPS']
    targetAttributes=['GROUP', 'CROP', 'SUB-CROP', 'SUB-SUB-CROP']
    for every line in srcDf:
        scanSource(line)
    


def scanTarget(s):
    if s !== len(sourceAttributes):
        for t in len(targetAttributes-1): 
            return matching(s,targetAttributes[t])

    #the condition below is dedicated to stop the recursive loop from scanSource when the all source attributes have been scanned and no mtaching have been found. 
    else 
        match.result.append(null) 
        print('zero matching have been found for the value : ' + value)


def scanSource():
    s=0
    if match.result !== []
        return #add value to df conversion
    else 
        return scanSource(s+1)

def matching(s,t): 
    #to be defined

converter("FR", "2020")