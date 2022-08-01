import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from converter_2 import * 


'''def download_handmade(place){
    parent = Path(__file__).parents[2]
    data_path = parent.joinpath('data')
    handmade_path = data_path.joinpath(place,'handmade_Nicolas_light.csv')
    Nicolas_df = pd.read_csv(data_path, encoding= 'unicode_escape')
    Nicolas_df.drop(columns = ["ICC1.1"], axis = 1, inplace = True)
    return Nicolas_df
}'''

def compare(handmade,computed,threshold):
    #handmade = download_handmade(place)
    print(handmade.dtypes)
    print(computed.dtypes)
    compare = handmade.copy()
    compare.rename(columns={'ID_GROUP_ICC':'ID_GROUP_ICC_handmade'}, inplace=True)
    compare['ID_GROUP_ICC_computed'] = computed['ID_GROUP_ICC']
    compare2 = compare.copy()

    boolean_serie = compare.apply(lambda x : True if (x.ID_GROUP_ICC_handmade == x.ID_GROUP_ICC_computed) else False,axis=1)
    boolean_serie2 = compare2.apply(lambda x : True if not (np.isnan(x.ID_GROUP_ICC_computed)) and (x.ID_GROUP_ICC_handmade != x.ID_GROUP_ICC_computed)  else False,axis=1)
    boolean_df = boolean_serie.to_frame()
    boolean_df2 = boolean_serie2.to_frame()
    boolean_df = boolean_df.rename(columns = {0:'bool'})
    boolean_df2 = boolean_df2.rename(columns = {0:'bool'})

    tot = len(compare)
    match = boolean_df['bool'].sum()
    error = boolean_df2['bool'].sum()
    per = round((match*100)/tot)
    err = round((error*100)/tot)

    print('The conversion table computed with the threshold = ' + str(threshold) + ', fits to the expected output at ' + str(per) + '%.')
    print('The conversion script made '+str(err)+'%'+' of errors.')
    return (threshold, per, err)

def optimal_threshold(src_path_input, place, lg,sim_method, handmade_path): 
    compare_list = []
    thresholds =[]
    num = 1
    while num <= 100: 
        num+=1 
        if num % 10 == 0: 
            thresholds.append(num)
    
    handmade = pd.read_csv(handmade_path, encoding= 'unicode_escape')
    handmade['ID_GROUP_ICC_str'] = handmade['ICC1.1'].str[:1]
    handmade['ID_GROUP_ICC'] = pd.to_numeric(handmade['ID_GROUP_ICC_str'], errors='coerce')
    handmade.drop(columns = ["ICC1.1", "ID_GROUP_ICC_str"], axis = 1, inplace = True)
    src_formatted = converter(src_path_input, place, lg, 0, 'basic')[0]
    icc_formatted = converter(src_path_input, place, lg, 0, 'basic')[1]
    for t in thresholds:
        print('conversion table with sim_method: '+ sim_method + ', and threshold: '+ str(t) + ' starts to be computed...')
        computed = converter(src_path_input, place, lg, t, sim_method, src_formatted, icc_formatted)[2]
        print('conversion table with sim_method: '+ sim_method + ', and threshold: '+ str(t) + ' successfully computed !')
        compare_list.append(compare(handmade,computed,t))

    compare_df = pd.DataFrame (compare_list, columns = ['threshold','correctness(%)', 'errorness(%)'])
    print(compare_df)
    parent = Path(__file__).parents[2]
    compare_path = parent.joinpath('data', 'result','optimize_threshold_'+place+'_'+sim_method+'.csv')
    compare_df.to_csv(compare_path, index=False)
    ax = plt.axis([0, 100, 0, 100])
    ax = plt.gca()

    compare_df.plot(kind='line',x='threshold',y='correctness(%)', color = 'green',ax=ax)
    compare_df.plot(kind='line',x='threshold',y='errorness(%)', color='red', ax=ax)

    if 0 in compare_df['errorness(%)'].unique():
        index_min = compare_df[compare_df['errorness(%)']==0].index[0] 
    else:
        index_min = compare_df['errorness(%)'].idxmin()
    #if index_min == np.nan:
    #    index_min = compare_df['errorness(%)'].idxmin()

    print(index_min)
    print(compare_df.iloc[index_min]['threshold'])
    threshold_optimal = compare_df.iloc[index_min]['threshold']

    plt.axvline(threshold_optimal, 0, 100, label='minimum errorness reached', linestyle='--')
    plt.plot(threshold_optimal,0, color="red")
    plt.text(  
        threshold_optimal+1,1, threshold_optimal,  
        ha='left', 
        color='red'
    )

    cor_max = compare_df.iloc[index_min]['correctness(%)']
    plt.axhline(y = cor_max, linestyle = '--')
    plt.plot(0,cor_max, color="green")
    plt.text(  
        1,cor_max+1, cor_max,  
        ha='left', 
        color='green'
    )

    plt.title(place +' : similarity method = '+sim_method)
    plt.show()
    #plt.savefig('/home/BTemple-Boyer-Dury/Documents/Classificrops/docs/images/optimal_threshold/'+place+'_'+sim_method+'.png')

optimal_threshold('/home/BTemple-Boyer-Dury/Documents/Classificrops/data/FR/FR_2020.csv', 'FR', 'fr','token_sort_ratio', '/home/BTemple-Boyer-Dury/Documents/Classificrops/data/FR/handmade_Nicolas_light.csv')

'''handmade = pd.read_csv('/home/BTemple-Boyer-Dury/Documents/Classificrops/data/FR/handmade_Nicolas_light.csv', encoding= 'unicode_escape')
handmade['ID_GROUP_ICC_str'] = handmade['ICC1.1'].str[:1]
handmade['ID_GROUP_ICC'] = pd.to_numeric(handmade['ID_GROUP_ICC_str'], errors='coerce')
handmade.drop(columns = ["ICC1.1", "ID_GROUP_ICC_str"], axis = 1, inplace = True)
print(compare(handmade,converter('/home/BTemple-Boyer-Dury/Documents/Classificrops/data/FR/FR_2020.csv', 'FR', 'fr',90,'split+ratio+'),90))'''