##PSEUDO-CODE
#converter functions definition
import pandas as pd

def spread(place, src_df2,x):
    m = src_df2.loc[src_df2['ID_GROUP_'+place] == x['ID_GROUP_'+place],'match']
    return m.iloc[0]

def match_row_row(c,idS,src,trg,idT,threshold,sim_method): 
    nb = 0
    if sim_method == 'split+ratio':
        if type(src) == str and type(trg) == str:
            #split the string into tokens
            src_l = src.split()
            len_src = len(src_l)
            trg_l = trg.split()
            myList=[]
            #for each token of the source string
            for w in src_l:
                #for each token of the target string
                for x in trg_l:
                    #add to my list  : (index of the source token among the string under study,ratio_similarity computed between token source and token target) 
                    myList.append([src_l.index(w),fuzz.ratio(w,x)])
            cols = ['index', 'sim']
            myDf = pd.DataFrame(myList, columns=cols)
            #for each token of the source string, take the similarity maximum. 
            r = myDf.groupby('index')['sim'].max().reset_index()
            #sum the best similarity computed for each token of the source string
            total = r['sim'].sum()
            #devide the sum by the number of tokens into the source string
            nb = total / len_src

    if nb >= threshold: 
        #return the following information when the similarity computed between 2 strings is superioir to the threshold : ['class_level_src', 'id_src',' words_src', 'words_trg', 'id_trg', 'similarity']
        return [c,idS, src, trg, idT, nb]
    else:
        return []

def match_row_df(lg,c,id_src,src,icc_df,threshold,sim_method):
    #in icc_df, create a column name "temp" that will be updated for each new row of src_df
    #"temp" column stores the result matches
    icc_df['temp'] = icc_df.apply(lambda y : match_row_row(c,id_src,src,y['label_'+lg+'_filtered'],y['ID_GROUP'],threshold,sim_method), axis=1)
    my_list = icc_df['temp'].to_list()
    new_list = [e for e in my_list if e != []]
    if new_list:
        return new_list
    else:
        return []

def match_df_df(place, lg,src_df,icc_df,threshold,sim_method):
    #match df source at level = GROUP
    c = 'GROUP_' + place
    src_df2 = src_df.drop_duplicates(subset = ['ID_GROUP_' + place])
    #create a column match in src_df2 to store the match
    src_df2['match'] = src_df2.apply(lambda x: match_row_df(lg,c, x['ID_' + c], x[c+ '_filtered'],icc_df,threshold,sim_method), axis=1)
    #spread the match identifies in src_df2 with unique values of group to the source dataframe. 
    src_df['match'] = src_df.apply(lambda x: spread(place, src_df2,x), axis=1)
    
    #match df source at level = CROPS
    #--------------------------------------------
    c = 'CROPS_' + place
    #in srcv_df2 concatenate the result already get in match at group level + the match get at crops level
    src_df['match'] = src_df.apply(lambda x: x['match'] + match_row_df(lg,c, x['ID_' + c], x[c+ '_filtered'],icc_df,threshold,sim_method), axis=1)
    return src_df['match']

def max(matches_list):
    t = [np.nan, np.nan, np.nan, np.nan, np.nan, 0]       
    for l in matches_list:
        if l[5] > t[5]:
            t = l
    return t