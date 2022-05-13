import pandas as pd
import deepl
from fuzzywuzzy import fuzz
import numpy as np

##My global variables
matching_list = [] 
result_df = pd.DataFrame()
src_classes = ['GROUP','CROPS']
compare_list = []

def classes(classes,place):
    src_classes = [c+'_'+place for c in classes]
    return src_classes

def filter(df, col, filters):
    mydict = {f'(?i){word}':'' for word in filters}
    df[col+'_filtered'] = df[col].replace(mydict, regex=True)
    df[col+'_filtered'] = df[col+'_filtered'].str.replace(r'[^\w\s]+', '', regex=True)
    df[col+'_filtered'] = df[col+'_filtered'].str.replace('   ', ' ')
    df[col+'_filtered'] = df[col+'_filtered'].str.replace('  ', ' ')
    df[col+'_filtered'] = df[col+'_filtered'].str.strip()
    return df[col+'_filtered']

def translateWord(translator, word, language):
    result = translator.translate_text(word, target_lang=language.upper())
    return result

def translateICC(df, lg):
    DEEPL_AUTH_KEY="47c6c989-9eaa-5b30-4ee6-b2e4f1ebd530:fx"
    translator = deepl.Translator(DEEPL_AUTH_KEY)
    df['label_'+lg+'_filtered'] = df['label_en_filtered'].apply(lambda crop: translateWord(translator, crop, lg) if (pd.notna(crop)) else crop)
    return df['label_'+lg+'_filtered']

def parse(x):
    return "".join(x.split('.'))

def matchRow(c,idS,src,trg,idT,threshold,sim_method): 
    global matching_list
    nb = 0
    if sim_method == 'token_set_ratio':
        nb = fuzz.token_set_ratio(src,trg)
    elif sim_method == 'split+ratio':
        if type(src) == str and type(trg) == str:
            srcA = src.split()
            length = len(srcA)
            trgA = trg.split()
            myList=[]
            for w in srcA:
                for x in trgA:
                    myList.append([srcA.index(w),fuzz.ratio(w,x)])
            cols = ['index', 'sim']
            myDf = pd.DataFrame(myList, columns=cols)
            r = myDf.groupby('index')['sim'].max().reset_index()
            total = r['sim'].sum()
            nb = total / length
    elif sim_method == 'basic':
        if src == trg:
            nb = 100
    if nb > threshold: 
        matching_list.append([c,idS, src, trg, idT, nb])

def matchDf(srcDf,iccDf,threshold,sim_method):
    for c in src_classes: 
        srcDf2 = srcDf.drop_duplicates(subset = ['ID_' + c])
        srcDf2.apply(lambda x: iccDf.apply(lambda y: matchRow(c, x['ID_' + c],x[c],y.label_fr_filtered,y.group_code,threshold,sim_method), axis=1), axis=1)

    cols = ['class_level_src', 'id_src',' words_src', 'words_trg', 'id_trg', 'similarity']
    mDf = pd.DataFrame(matching_list, columns=cols)
    idx = mDf.groupby(['id_src'])['similarity'].transform(max) == mDf['similarity']
    return mDf[idx]
    #return mDf

def spreadMatch(id_src,id_trg,sim):
    global result_df
    result_df.loc[result_df['ID_GROUP_'+place] == id_src, 'ID_GROUP_ICC'] = id_trg
    result_df.loc[result_df['ID_GROUP_'+place] == id_src, 'similarity'] = sim


def incDepth(x): 
    global matching_df
    ID_C = x['ID_CROPS_'+place]
    ID_G = x.ID_GROUP_ICC
    sim = x.similarity
    i = matching_df.loc[matching_df['id_src'] == ID_C]
    if len(i.index) != 0:
        if pd.isna(ID_G) or sim < i.similarity.iloc[0]:
            ID_G = i.id_trg.iloc[0]
    return ID_G

def spreadSim(id_src,sim):
    global result_df
    result_df.loc[result_df['ID_CROPS_'+place] == id_src, 'similarity'] = sim

def compare(pathHandMade,computed,threshold):
    handmade = pd.read_csv(pathHandMade)
    compare = handmade.copy()
    compare.rename(columns={'ID_GROUP_ICC':'ID_GROUP_ICC_handmade'}, inplace=True)
    compare['ID_GROUP_ICC_computed'] = computed['ID_GROUP_ICC']
    compare2=compare.copy()

    booleanSerie = compare.apply(lambda x : True if (x.ID_GROUP_ICC_handmade==x.ID_GROUP_ICC_computed) else False,axis=1)
    booleanSerie2 = compare2.apply(lambda x : True if not (np.isnan(x.ID_GROUP_ICC_computed)) and (x.ID_GROUP_ICC_handmade!=x.ID_GROUP_ICC_computed)  else False,axis=1)
    booleanDf = booleanSerie.to_frame()
    booleanDf2 = booleanSerie2.to_frame()
    booleanDf = booleanDf.rename(columns = {0:'bool'})
    booleanDf2 = booleanDf2.rename(columns = {0:'bool'})

    tot = len(compare)
    match = booleanDf['bool'].sum()
    error = booleanDf2['bool'].sum()
    per = round((match*100)/tot)
    err = round((error*100)/tot)

    print('The conversion table computed with the threshold = ' + str(threshold) + ', fits to the expected output at ' + str(per) + '%.')
    print('The conversion script made '+str(err)+'%'+' of errors.')
    return (threshold,per)

def converter(pathCsv, pl, lg, threshold,sim_method):
    global result_df
    global matching_df
    global compare_list
    global place
    place = pl
    target = '../../data/ICC/ICC.csv'

    ##Loading
    srcDf = pd.read_csv(pathCsv)
    iccDf = pd.read_csv(target)

    ##Listing
    src_classes = classes(src_classes,place)

    ##Filtering1a
    if 'label_en_filtered' not in list(iccDf.columns): 
        englishFilters1=['n.e.c.', 'spp','n.e.c']
        iccDf['label_en_filtered'] = filter(iccDf,'label_en',englishFilters1)
        iccDf.replace('',np.nan,regex = True,inplace=True)


    ##Translating
    if 'label_'+lg+'_filtered' not in list(iccDf.columns):
        iccDf['label_'+lg+'_filtered'] = translateICC(iccDf, lg)
        iccDf.to_csv(target, index=False)

    #the ICC filtering is divided into 2 parts because if you do it in one step before translating
    #you get "Grasses and other fodder crops" that becomes "Grasses fodder" translated into 
    #"Fourrage de graminées whereas it should be translated into "Fourrages et graminées" or "Fourrages graminées". 
    
    ##Filtering1b
    if 'label_en_filtered' not in list(iccDf.columns): 
        englishFilters2=['other','crops',' and',' or']
        iccDf['label_en_filtered'] = filter(iccDf,'label_en_filtered',englishFilters2)
        iccDf.replace('',np.nan,regex = True,inplace=True)
        iccDf.to_csv(target, index=False)

    ##Filtering2
    frenchFilters = ['autres','autre',' et',' ou']
    for c in src_classes:
        srcDf[c+'_filtered'] = filter(srcDf,c,frenchFilters)
        srcDf.replace('',np.nan,regex = True,inplace=True)
        if 'ID_'+c not in list(srcDf.columns):
            srcDf['ID_'+c] = srcDf[c] #we could make an identifier generator more sophisticated in the future. 

    ##Formating ICC
    iccDf['code'] = iccDf['code'].apply(lambda code:parse(code))
    iccDf['code'] = iccDf['code'].astype('int')
    iccDf['group_code'] = iccDf['code'].astype('str').str[:1].astype('int')

    ##Initializing
    result_df = srcDf[['ID_CROPS_'+place, 'ID_GROUP_'+place]]

    ##Matching all
    matching_df = matchDf(srcDf,iccDf,threshold,sim_method)

    ##Spreading
    rows = matching_df.loc[matching_df['class_level_src'] == 'GROUP_'+place]
    rows2 = rows.copy()
    rows2.apply(lambda x: spreadMatch(x.id_src, x.id_trg,x.similarity), axis=1)

    ##Incrementing depth   
    print(matching_df)
    cp = matching_df.copy()
    cp.apply(lambda x: spreadSim(x.id_src, x.similarity), axis=1)
    print(result_df.head(50))
    result_df['ID_GROUP_ICC'] = result_df.apply(lambda x: incDepth(x), axis=1)

    #Writting result
    result_df.to_csv('../../data/'+place+'/conversionTable_'+place+'_scriptMade.csv', index=False)
    matching_df.to_csv('../../data/'+place+'/matching_df_'+place+'_scriptMade.csv', index=False)
    result_df['ID_GROUP_ICC'] = result_df.loc[:, ['ID_GROUP_ICC']].astype(float)
    compare_list.append(compare('../../data/'+place+'/conversionTable_'+place+'_handMade.csv',result_df,threshold))

converter('../../data/FR/FR_2020.csv', 'FR','fr', 80,'basic')
#converter('../../data/WL/WL_2020.csv', 'WL','FR', 1,50)
