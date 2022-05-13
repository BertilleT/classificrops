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

def translate_word(translator, word, language):
    result = translator.translate_text(word, target_lang=language.upper())
    return result

def translate_ICC(df, lg):
    DEEPL_AUTH_KEY="47c6c989-9eaa-5b30-4ee6-b2e4f1ebd530:fx"
    translator = deepl.Translator(DEEPL_AUTH_KEY)
    df['label_'+lg+'_filtered'] = df['label_en_filtered'].apply(lambda crop: translate_word(translator, crop, lg) if (pd.notna(crop)) else crop)
    return df['label_'+lg+'_filtered']

def parse(x):
    return "".join(x.split('.'))

def spread(src_df,x):
    src_df.loc[src_df['ID_GROUP_'+lg] == x['ID_GROUP_'+lg], 'match'] = x.match
    return src_df

def match_row_row(c,idS,src,trg,idT,threshold,sim_method): 
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
        return [c,idS, src, trg, idT, nb]
    else:
        return np.nan

def match_row_df(lg,c,id_src,src,icc_df,threshold,sim_method):
    icc_df['temp'] = icc_df.apply(lambda y : match_row_row(c,id_src,src,y['label_'+lg+'_filtered'],y.ID_GROUP,threshold,sim_method))
    my_list = icc_df['temp'].to_list()
    new_list = [e for e in my_list if np.isnan(e) == False]
    if new_list:
        return new_list
    else:
        return np.nan

def match_df_df(lg,src_df,icc_df,threshold,sim_method):
    #GROUP
    c = 'GROUP_' + lg
    src_df2 = src_df.drop_duplicates(subset = ['ID_GROUP_' + lg])
    src_df2['match'] = src_df2.apply(lambda x: match_row_df(lg,c, x['ID_' + c], x[c],icc_df,threshold,sim_method), axis=1)
    src_df = src_df2.apply(lambda x: spread (src_df,x), axis=1)
    
    #CROPS
    #--------------------------------------------
    c = 'CROPS_' + lg
    src_df2['match'] = src_df2.apply(lambda x: x['match'] + match_row_df(lg,c, x['ID_' + c], x[c],icc_df,threshold,sim_method), axis=1)


    #cols = ['class_level_src', 'id_src',' words_src', 'words_trg', 'id_trg', 'similarity']
    #mDf = pd.DataFrame(matching_list, columns=cols)
    #idx = mDf.groupby(['id_src'])['similarity'].transform(max) == mDf['similarity']
    #return mDf[idx]
    #return mDf
    return src_df2['match']

#def spread_match(id_src,id_trg,sim):
#    global result_df
#    result_df.loc[result_df['ID_GROUP_'+place] == id_src, 'ID_GROUP_ICC'] = id_trg
#    result_df.loc[result_df['ID_GROUP_'+place] == id_src, 'similarity'] = sim

def inc_depth(x): 
    global matching_df
    ID_C = x['ID_CROPS_'+place]
    ID_G = x.ID_GROUP_ICC
    sim = x.similarity
    i = matching_df.loc[matching_df['id_src'] == ID_C]
    if len(i.index) != 0:
        if pd.isna(ID_G) or sim < i.similarity.iloc[0]:
            ID_G = i.id_trg.iloc[0]
    return ID_G

def spread_sim(id_src,sim):
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
    src_df = pd.read_csv(pathCsv)
    icc_df = pd.read_csv(target)

    ##Listing
    src_classes = classes(src_classes,place)

    ##Filtering1a
    if 'label_en_filtered' not in list(icc_df.columns): 
        englishFilters1=['n.e.c.', 'spp','n.e.c']
        icc_df['label_en_filtered'] = filter(icc_df,'label_en',englishFilters1)
        icc_df.replace('',np.nan,regex = True,inplace=True)


    ##Translating
    if 'label_'+lg+'_filtered' not in list(icc_df.columns):
        icc_df['label_'+lg+'_filtered'] = translate_ICC(icc_df, lg)
        icc_df.to_csv(target, index=False)

    #the ICC filtering is divided into 2 parts because if you do it in one step before translating
    #you get "Grasses and other fodder crops" that becomes "Grasses fodder" translated into 
    #"Fourrage de graminées whereas it should be translated into "Fourrages et graminées" or into "Fourrages graminées". 
    
    ##Filtering1b
    if 'label_en_filtered' not in list(icc_df.columns): 
        englishFilters2=['other','crops',' and',' or']
        icc_df['label_en_filtered'] = filter(icc_df,'label_en_filtered',englishFilters2)
        icc_df.replace('',np.nan,regex = True,inplace=True)
        icc_df.to_csv(target, index=False)

    ##Filtering2
    frenchFilters = ['autres','autre',' et',' ou']
    for c in src_classes:
        src_df[c+'_filtered'] = filter(src_df,c,frenchFilters)
        src_df.replace('',np.nan,regex = True,inplace=True)
        if 'ID_'+c not in list(src_df.columns):
            src_df['ID_'+c] = src_df[c] #we could make an identifier generator more sophisticated in the future. 

    ##Formating ICC
    icc_df['ID'] = icc_df['ID'].apply(lambda ID:parse(ID))
    icc_df['ID'] = icc_df['ID'].astype('int')
    icc_df['ID_GROUP'] = icc_df['ID'].astype('str').str[:1].astype('int')

    ##Initializing
    result_df = src_df[['ID_CROPS_'+place, 'ID_GROUP_'+place]]

    ##Matching all
    src_df['match'] = match_df_df(lg,src_df,icc_df,threshold,sim_method)
    #########to be continued here

    ##Spreading
    rows = matching_df.loc[matching_df['class_level_src'] == 'GROUP_'+place]
    rows2 = rows.copy()
    rows2.apply(lambda x: spread_match(x.id_src, x.id_trg,x.similarity), axis=1)

    ##Incrementing depth   
    print(matching_df)
    cp = matching_df.copy()
    cp.apply(lambda x: spread_sim(x.id_src, x.similarity), axis=1)
    print(result_df.head(50))
    result_df['ID_GROUP_ICC'] = result_df.apply(lambda x: inc_depth(x), axis=1)

    #Writting result
    result_df.to_csv('../../data/'+place+'/conversionTable_'+place+'_scriptMade.csv', index=False)
    matching_df.to_csv('../../data/'+place+'/matching_df_'+place+'_scriptMade.csv', index=False)
    result_df['ID_GROUP_ICC'] = result_df.loc[:, ['ID_GROUP_ICC']].astype(float)
    compare_list.append(compare('../../data/'+place+'/conversionTable_'+place+'_handMade.csv',result_df,threshold))

converter('../../data/FR/FR_2020.csv', 'FR','fr', 80,'basic')
#converter('../../data/WL/WL_2020.csv', 'WL','FR', 1,50)
