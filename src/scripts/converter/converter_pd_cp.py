import csv 
import pandas as pd
import deepl
from fuzzywuzzy import fuzz, process

##My global variables
matchingList = [] 
resultDf = pd.DataFrame()
srcClasses=[]

def classes(df):
    #create an empty list to store all the classes from the origin data. In the French example, we have only 2 levels of classes : GROUP_FR and CROPS_FR.
    global srcClasses
    columns = list(df)
    for col in columns:
        if 'ID' not in col: 
            srcClasses.append(col)
    return srcClasses
    #the 4 lines above admits that in columns names of the source file, we can have only 'ID_+class' or classes names.
    #this is true for French source file, but might be false for others source files. 
    #in the future, the user should be told to prepare the entering data to get the same format, or the lines above should be updated. 

def filter(df, col, filters):
    mydict = {f'(?i){word}':'' for word in filters}
    df[col+'_filtered'] = df[col].replace(mydict, regex=True)
    df[col+'_filtered'] = df[col+'_filtered'].str.replace(r'[^\w\s]+', '')
    df[col+'_filtered'] = df[col+'_filtered'].str.replace('   ', ' ')
    df[col+'_filtered'] = df[col+'_filtered'].str.replace('  ', ' ')
    df[col+'_filtered'] = df[col+'_filtered'].str.strip()
    return df[col+'_filtered']

# Translate text into a target language, in this case, French
def translateWord(translator, word, language):
    if word != 'none':
        result = translator.translate_text(word, target_lang=language)
        return result
    else:
        return word

def translateICC(df, lg):
    # Create a Translator object providing your DeepL API authentication key.
    DEEPL_AUTH_KEY="47c6c989-9eaa-5b30-4ee6-b2e4f1ebd530:fx"
    translator = deepl.Translator(DEEPL_AUTH_KEY)
    df['label_'+lg.lower()+'_filtered'] = df['label_en_filtered'].apply(lambda crop: translateWord(translator,crop, lg))
    return df['label_'+lg.lower()+'_filtered']

def parserICCCode(x):
    return "".join(x.split('.'))
   
#if match > threshold, add the result to the matchingList
def matchRow(c,idS,src,trg,idT): 
    global matchingList
    nb = 0
    nb = fuzz.token_sort_ratio(src,trg)
    if nb > 75: 
        matchingList.append([c,idS, src, trg, idT, nb])
        #matchingList.append([idS, idT, nb])

def matchDf(srcDf,iccDf):
    #for each class of the source file
    for c in srcClasses: 
        #drop the duplicates for the class under study. This step is made to avoid to compute the matching several times for the same source class instance. 
        srcDf2 = srcDf.drop_duplicates(subset = ['ID_' + c])
        #in the line below, we will replace '_fr' from y.label_fr passed in argument by a variable. It could be 'it' for italian, 'en' for english, etc. 
        srcDf2.apply(lambda x:iccDf.apply(lambda y: matchRow(c, x['ID_' + c],x[c],y.label_fr_filtered,y.group_code), axis=1), axis=1)
        #if the matching step found a relevant match for the instance of the class under study, we do not need to level up to the next level of classes. 
        #for example, if at source level=group, a match have been found, then for the source group under study, there is no need to compute the matching at the source level = crops. 
        if 'ID_' + c in matchingList[:][1]:
            break

    #the matchingList is turned into a pandas dataframe. Note that this solution 
    #(write a list row by row and transform the list into a pd dataframe once)consumes less energy than filling a pd dataframe row by row. 
    cols = ['class_level_src', 'id_src',' words_src', 'words_trg', 'id_trg', 'similarity']
    return pd.DataFrame(matchingList, columns=cols)

#if there is a match at group source level, then all the crops into this group src should herit the matching target group found for the father group. 
def spreadMatch(id_src,id_trg):
    global resultDf
    '''print('print global resultDf from spreadMatch function before processing')
    print(resultDf.head(50))'''
    resultDf.loc[resultDf.ID_GROUP_FR == id_src, 'ID_GROUP_ICC'] = id_trg
    '''print('print global resultDf from spreadMatch function after processing')
    print(resultDf.head(50))'''

#incDepth stands for increment depth
#if no matching group have been found after match at source level = group and after the spreading, then go to the source level = crops in matchingDf
#if matchingDf has a match at source crops level, then fill the resultDf with this value. 
def incDepth(x): 
    ID_C = x.ID_CROPS_FR
    ID_G = x.ID_GROUP_ICC
    if pd.isna(ID_G):
        i = matchingDf.loc[matchingDf['id_src'] == ID_C]
        if len(i.index) != 0:
            ID_G = i.id_trg



def converter(pathCsv, lg, srcDepth):
    global resultDf
    ##Loading
    print('loading df ...')
    srcDf = pd.read_csv(pathCsv)
    iccDf = pd.read_csv('../../../data/ICC/ICC_src.csv')
    print('df loaded')

    ##Listing
    #list classes from source data
    classes(srcDf)

    ##Filtering1
    #filter non discrimnantory words and punctuations from the target df
    print('filtering 1 - ICC ...')
    englishFilters=['other','crops',' and ',' or ','n.e.c.', 'spp']
    iccDf['label_en_filtered'] = filter(iccDf,'label_en',englishFilters)
    iccDf.label_en_filtered = iccDf.label_en_filtered.fillna('none')
    r=iccDf.iloc[[162]]
    v=r.label_en_filtered
    print('hh'+v+'hh')
    print(type(v))
    
    iccDf.to_csv('../../../data/ICC/ICC.csv')
    print('ICC filtered')

    ##Filtering2
    #filter non discrimnantory words and punctuations from the source df
    print('filtering 2 - source classification ...')
    frenchFilters = ['autres','autre',' et ',' ou ']
    for c in srcClasses:
        srcDf[c] = filter(srcDf,c,frenchFilters)
    print('source classification filtered')

    ##Translating
    #if the target df is not yet translated into the source language, translate it
    if 'label_'+lg.lower()+'_filtered' not in iccDf:
        print('translating ICC ...')
        iccDf['label_'+lg.lower()+'_filtered'] = translateICC(iccDf, lg)
        iccDf.to_csv('../../../data/ICC/ICC.csv')
        print('ICC translated')

    ##Formating
    #transform the code "1.34.28" from indicative crop classification into "13428"
    print('formating ICC codes ...')
    iccDf['code'] = iccDf['code'].apply(lambda code:parserICCCode(code))
    #now that '.' have been filtered from codes, we can translate codes into integers. 
    iccDf['code'] = iccDf['code'].astype('int')
    #select the first digit of the code, which corresponds to the group crop code. This is when the target depth is equal to 0. 
    iccDf['group_code'] = iccDf['code'].astype('str').str[:1].astype('int')
    print('ICC codes formated')

    ##Initializing
    #initialise the list where we will store the results from the matching. 
    print('initializing resultDf ...')
    resultDf = srcDf[['ID_CROPS_FR', 'ID_GROUP_FR']]
    '''print(resultDf)'''
    print('resultDf initialized')

    ##Matching all
    print('matching df...')
    matchingDf = matchDf(srcDf,iccDf)
    print('df matched...')
    print(matchingDf.head(50))

    ##Spreading
    #if in the matchingDf we get a result raw at first level source level (GROUP_FR), then stock this raw into rows
    print('spreading match...')
    rows = matchingDf.loc[matchingDf['class_level_src'] == 'GROUP_FR']
    '''print(rows)'''
    #for the match found at level source 1 (group in french example), ie for each row from rows, spread the result found to the level 2 (crops) children of the group under study. 
    resultDf = rows.apply(lambda x: spreadMatch(x.id_src, x.id_trg), axis=1)
    '''print(resultDf)'''
    print('match spread')

    ##Incrementing depth   
    print('incrementing depth...') 
    resultDf = resultDf[['ID_CROPS_FR','ID_GROUP_ICC']]
    resultDf.apply(lambda x: incDepth(x), axis=1)
    print('depth incremented')

    #Writting
    print('writting resultDf into csv...') 
    resultDf.to_csv('conversionTableFrICC_Test.csv')
    print('resultDf written into csv') 

converter('../../../data/FR/FR_2020.csv', 'FR', 1)