import csv 
import pandas as pd

class match: 
    level: #level of match : 1.1|1.2|1.3|1.4|2.1|2.2|2.3|2.4
    full_match: #TRUE|FALSE
    src_words:
    src_id: 
    target_words:
    target_id:

nonDiscrimnantWords = ["à", "de", "ou", "et"]

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

    '''for every line in srcDf:
        scanSource(line)
    
    srcDf[srcDf[sourceAttributes[s]].str.contains(word)]'''

def scanTarget(s):
    #the condition below is dedicated to stop the recursive loop from scanSource() when all source attributes have been scanned and no matching have been found. 
    if s !== len(sourceAttributes): 
        #for every level of JECAM classification
        for t in range(len(targetAttributes-1)): 
            srcLevel = sourceAttributes[s]
            trgLevel = sourceAttributes[t]
            return matching(srcLevel,trgLevel)
    else 
        match.result.append(null) 
        print('zero matching have been found for the value : ' + value)


def scanSource():
    s=0
    if match.result !== [] #this condition could be replaced by something like : if maximum match pourcentage already found is superior to 50 %
        return #add value to df conversion
    else 
        return scanSource(s+1)

def matching(s,t): 
    srcDf[srcDf[].str.contains(word)]

converter("FR", "2020")

#next idea : use fuzz.token_sort_ratio
