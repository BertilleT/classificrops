import csv 
import pandas as pd
import numpy as np
import itertools
from fuzzywuzzy import fuzz, process

#load the source dataframe
srcDf = pd.read_csv('../../data/FR/FR_2020.csv')

#load the target dataframe
iccDf = pd.read_csv('../../data/ICC/ICC_fr.csv')

#initialise the list where we will store the results from the matching. 
matchingList = [] 
resultDf = srcDf[['ID_CROPS_FR','ID_GROUP_FR']]
print(resultDf.dtypes)
#Note that we have matchingList and resultDf which are different.
#matchingList is dedicated to print the result found into the terminal. It allows to print the names of associated crops. 
#resultDf is less explicit and contains only codes with similarity found during the matching. This df will be translated into csv file. 

#transform the code "1.34.28" from indicative crop classification into "13428"
def parserICCCode(x):
    return "".join(x.split('.'))

iccDf['code'] = iccDf['code'].apply(lambda code:parserICCCode(code))
#now that '.' have been filtered from codes, we can translate codes into integers. 
iccDf['code'] = iccDf['code'].astype('int')

#select the first digit of the code, which corresponds to the group crop code
iccDf['group_code'] = iccDf['code'].astype('str').str[:1].astype('int')
'''def scanTarget(c, idS,g):
    iccDf.apply(lambda x: matching(c, idS,g,x.label_fr,x.group_code), axis=1)'''

#if match > threshold, add the result to the matchingList
def matching(c,idS,src,trg,idT): 
    nb = 0
    nb = fuzz.token_sort_ratio(src,trg)
    if nb > 60: 
        matchingList.append([c,idS, src, trg, idT, nb])
        #matchingList.append([idS, idT, nb])

#create an empty list to store all the classes frome the origin data. In the French example, we have only 2 levels of classes : GROUP_FR and CROPS_FR.
srcClasses=[]
columns = list(srcDf)
for col in columns:
    if 'ID' not in col: 
        srcClasses.append(col)
#the 4 lines above admits that in columns names of the source file, we can have only 'ID_+class' or classes names.
#this is true for French source file, but might be false for others source files. 
#in the future, the user should be told to prepare the entering data to get the same format, or the lines above should be updated. 

#for each class of the source file
for c in srcClasses: 
    #drop the duplicates for the class under study. This step is made to avoid to compute the matching several times for the same source class instance. 
    srcDf2 = srcDf.drop_duplicates(subset = ['ID_' + c])
    '''srcDf2.apply(lambda x:scanTarget(c,x['ID_' + c],x[c]), axis=1)'''
    #in the line below, we will replace '_fr' from y.label_fr passed in argument by a variable. It could be it, en and others languages. 
    srcDf2.apply(lambda x:iccDf.apply(lambda y: matching(c, x['ID_' + c],x[c],y.label_fr,y.group_code), axis=1), axis=1)
    #if the matching step found a relevant match for the instance of the class under study, we do not need to level up to the next level of classes. 
    #for example, if at source level=group, a match have been found, then for the source group under study, there is no need to compute the matching at the source level = crops. 
    if 'ID_' + c in matchingList[:][1]:
        break

#the matchingList is turned into a pandas dataframe. Note that this solution (write a list row by row and transform the list into a pd dataframe once)
#consumes less energy than filling a pd dataframe row by row. 
cols = ['class_level_src', 'id_src',' words_src', 'words_trg', 'id_trg', 'similarity']
matchingDf = pd.DataFrame(matchingList, columns=cols)
print(matchingDf.dtypes)



#if there is a match at group source level, then all the crops into this group src should herit the matching target group found for the father group. 

def spreadMatch(id_src,id_trg):
    resultDf.loc[resultDf.ID_GROUP_FR == id_src, 'ID_GROUP_ICC'] = id_trg

#if in the matchingDf we get a result raw at first level source level (GROUP_FR), then stock this raw into raws
rows = matchingDf.loc[matchingDf['class_level_src'] == 'GROUP_FR']
#for the match found at level source 1 (group in french example), spread the result found to the level 2 (crops) children of the group under study. 
r = rows.apply(lambda x: spreadMatch(x.id_src, x.id_trg), axis=1)
print(resultDf.dtypes)

#missings stores the values when matching with source level 1 was not convincing. The attribute is evaluated to True when there is no match found. 
#in this case, we should level up to level 2 (crops) and for each crops in the source file, add the matching group if one have been found. 
'''missings = resultDf['ID_GROUP_ICC'].isna()
print(missings)'''

'''def fct(ID_G,ID_C): 
    print(ID_G)
    if pd.isna(ID_G):
        i = matchingDf.loc[[matchingDf.id_src == ID_C]]
        print('i.id_trg')
        print(i.id_trg)
        if pd.isna(i.id_trg):
            return NULL
        else:
            print(i)
            print('----------------------id_src_crop-----------------------------')
            print(id_src_crop)
            print('----------------------i.id_trg-----------------------------')
            print(i.id_trg)
            return i.id_trg

resultDf.apply(lambda x: x['ID_GROUP_ICC'] == fct(x.ID_CROPS_FR) if , axis=1)
print(resultDf.head(50))
'''
df1 = matchingDf.loc[(matchingDf["class_level_src"] == "CROPS_FR")]
print(df1)
df = df1[['id_src','id_trg']]
df.rename(columns={"id_src" : "ID_CROPS_FR", "id_trg" : "ID_GROUP_FR"}, inplace=True)

#df.columns = ['ID_CROPS_FR' if x=='id_src' else x for x in df.columns]
DFRESULT = pd.merge(resultDf, df, on='ID_CROPS_FR',how='left')
print(DFRESULT)