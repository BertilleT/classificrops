import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#place = input("place ? ")
#sim_method = input("sim method ? ")

def best_sim_one_area(place, sim_method): 

    compare_df = pd.read_csv('/home/BTemple-Boyer-Dury/Documents/Classificrops/data/result/optimize_threshold_'+place+'_'+sim_method+'.csv')

    ax = plt.axis([0, 100, 0, 100])
    ax = plt.gca()

    #compare_df.plot(kind='line',x='threshold',y='correctness(%)', color = 'green',ax=ax)
    #compare_df.plot(kind='line',x='threshold',y='errorness(%)', color='red', ax=ax)

    if 0 in compare_df['errorness(%)'].unique():
        index_min = compare_df[compare_df['errorness(%)']==0].index[0] 
    else:
        index_min = compare_df['errorness(%)'].idxmin()
    #if index_min == np.nan:
    #    index_min = compare_df['errorness(%)'].idxmin()

    '''threshold_optimal = compare_df.iloc[index_min]['threshold']

    plt.axvline(threshold_optimal, 0, 100, label='minimum errorness reached', linestyle='--')
    plt.plot(threshold_optimal,0, "ro", color="red")
    plt.text(  
        threshold_optimal+1,1, threshold_optimal,  
        ha='left', 
        color='red'
    )'''

    cor_max = compare_df.iloc[index_min]['correctness(%)']
    '''plt.axhline(y = cor_max, linestyle = '--')
    plt.plot(0,cor_max, "ro", color="green")
    plt.text(  
        1,cor_max+1, cor_max,  
        ha='left', 
        color='green'
    )

    plt.title(place +' : similarity method = '+sim_method)
    plt.savefig('/home/BTemple-Boyer-Dury/Documents/Classificrops/docs/images/optimal_threshold/'+place+'_'+sim_method+'.png')
    plt.show()'''

    return (sim_method, index_min, compare_df.iloc[index_min]['errorness(%)'], cor_max)

def compute_matches_all_threshold(place): 
    all_sim_results =[]
    for s in sim_methods: 
        all_sim_results.append(best_sim_one_area(place,s))
    all_sim_df_one = pd.DataFrame(all_sim_results, columns = ['sim_method','index_min', 'errorness', 'correctness'])
    return all_sim_df_one

def choose_best_match(df):    
    err_min = df[df['errorness']== df['errorness'].min()]
    id_cor_max = df['correctness'].idxmax()
    #print(df.iloc[id_cor_max]['sim_method'])
    return df.iloc[id_cor_max].to_dict()


sim_methods = ['basic', 'ratio', 'token_sort_ratio', 'token_set_ratio', 'partial_ratio', 'split+ratio', 'split+ratio+symetric']

all_matching_by_classif = []
best_matching_by_classif = []
places_under_study = ['WL', 'FR', 'CAT']
for p in places_under_study: 
    all_sim_df_one = compute_matches_all_threshold(p)
    all_sim_df_one['place'] = p
    all_matching_by_classif.append(all_sim_df_one)
    best_matching_by_classif.append(choose_best_match(all_sim_df_one))

wl = all_matching_by_classif[0]
fr = all_matching_by_classif[1]
cat = all_matching_by_classif[2]
ax = wl.plot(x ='sim_method', y='correctness', color = 'green')
fr.plot(ax=ax, x ='sim_method', y='correctness', color = 'blue')
cat.plot(ax = ax, x ='sim_method', y='correctness', color = 'red')
ax.legend(["Wallonia", "Francia", "Catalunya"])
plt.title('Best correctness for each similarity method tested, for 3 LPIS different classifications (Wallonia, Francia and Catalunya)')
plt.xlabel('similarity method')
plt.ylabel('correctness')
#plt.annotate(xy=(2,2),'*correctness is defined as the percentages of good matching find by the semi-automatic converter tool. '\
#'**LPIS stands for Lands Parcel Identification System')
plt.show()
print(best_matching_by_classif)