import pandas as pd
from translation_fct import *
from converter_fct import *
icc_df = pd.read_csv('data/ICC/ICC.csv')

#the place is the place from which is issued the source classification under study. 
#the language is the language in wich the source classification is written
#src_classification_path is the path toward the source classification
#filters is an array that contains the words to be filtered when computing similarity between 2 tokens. 

def converter(place, language, src_classification_path, filters):
    src_df = pd.read_csv('src_classification_path')
    src_col = list(src_df)

    ##-----TRANSLATION-----
    #if the ICC classification have not been translated yet into the language of the source classification : 
    if "label_"+lg not in list(icc_df.columns) :
        #list source languages available with deepl API
        source_languages = []
        for l in translator.get_source_languages():
            source_languages.append(l.code)
        #if the language of the source classification under study is available with Deepl API
        if lg.upper() in source_languages:
            icc_df["label_"+lg] = deepl_translate_ICC(icc_df,lg)
            icc_df.to_csv(ICC_path, index = False)
        else: 
            icc_df["label_"+lg] = googletrans_translate_ICC(icc_df,lg)
            icc_df.to_csv(ICC_path, index = False)

    ##-----FILTER-----
    #we filter the words not discrimminatory. For example, filters could be equal to ['other','crops',' and',' or']
    mydict = {f'(?i){word}':'' for word in filters}
    icc_df['label_'+language+'_filtered'] = icc_df['label_'+language].replace(mydict, regex=True)
    
    ##-----CONVERSION-----
    #in src dataframe, we create a new column that stores a list of all the matching strings with icc. 
    #to get the matching string with icc, we call the function match_df_df with in arguments : language source, source dataframe, icc dataframe, 
    #threshold similarity and method of similarity. 
    #To match one string from source dataframe and one string from icc dataframe, we can use differents way to compute similarity between 2 strings. 
    #this is why, sim_method in one argument of the function match_df_df. 
    #Moreover, the matching between 2 strings outputs a similarity score between 0 and 100 (equal to 100 when the 2 strings are scritly the same)
    #match_df_df says there is a match between 2 strings when the similarity computed is higher than a threshold passed in argument. 
    #For example we could say there is a match when string A and string B match at more than 70%. Then threshold would be equal to 70. 
    src_df['match'] = match_df_df(lg,src_df,icc_df,threshold,sim_method)
    #on the src_match column we have a list of arrays as following : ['class_level_src', 'id_src',' words_src', 'words_trg', 'id_trg', 'similarity']
    #we select the array with the similarity maximum and store this array into the column max_match
    src_df["max_match"] = src_df.apply(lambda x: max(x.match), axis = 1)
    #we say that the id of the target string stored in max_match (with the similarity maximum) is the identifier of the group icc 
    #associated to the crops under study from the source classification. 
    src_df['ID_GROUP_ICC'] = src_df.apply(lambda x : x['max_match'][4] if x['max_match'] != [] else np.nan, axis=1)
    #in the column sim, we add the detail of whiwh is the similarity computed for the ICC group selected to be matched to the crop under study. 
    src_df['sim'] = src_df.apply(lambda x : x['max_match'][5] if x['max_match'] != [] else np.nan, axis=1)
    #result_df is a datframe that have on one side the keys of crops from sources, and on the other side, the keys of icc groups associated to the source crops. 
    result_df = src_df[['ID_CROPS_'+place, 'ID_GROUP_ICC']]
    src_col.append('ID_GROUP_ICC')
    src_icc_df = src_df.merge(result_df, how='left', on='ID_CROPS_' + place)
    src_icc_df = src_df.filter(src_col)
    src_with_ICC_col_path = 'result/src_with_ICC.csv'
    src_icc_df.to_csv('result/src_with_ICC.csv', index=False)
    print("Your classification has been successfully converted to ICC classification. You can download it in the following folder : ")
    print(result_path)

converter('WL', 'fr', '/home/bertille/Documents/P22/Classificrops/data/WL/WL.csv', ['autres','autre',' et',' ou'])