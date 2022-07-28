import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#place = input("place ? ")
#sim_method = input("sim method ? ")

def best_sim_one_area(place, sim_method): 

    compare_df = pd.read_csv('/home/BTemple-Boyer-Dury/Documents/Classificrops/data/result/optimize_threshold_'+place+'_'+sim_method+'.csv')

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
    plt.plot(threshold_optimal,0, "ro", color="red")
    plt.text(  
        threshold_optimal+1,1, threshold_optimal,  
        ha='left', 
        color='red'
    )

    cor_max = compare_df.iloc[index_min]['correctness(%)']
    plt.axhline(y = cor_max, linestyle = '--')
    plt.plot(0,cor_max, "ro", color="green")
    plt.text(  
        1,cor_max+1, cor_max,  
        ha='left', 
        color='green'
    )

    plt.title(place +' : similarity method = '+sim_method)
    plt.savefig('/home/BTemple-Boyer-Dury/Documents/Classificrops/docs/images/optimal_threshold/'+place+'_'+sim_method+'.png')
    #plt.show()

    return (sim_method, index_min, compare_df.iloc[index_min]['errorness(%)'], cor_max)

sim_methods = ['basic', 'ratio', 'token_sort_ratio', 'token_set_ratio', 'partial_ratio', 'split+ratio', 'split+ratio+symetric']
all_sim_results =[]
for s in sim_methods: 
    all_sim_results.append(best_sim_one_area('WL',s))
print(all_sim_results)
all_sim_df = pd.DataFrame(all_sim_results, columns = ['sim_method','index_min', 'errorness', 'correctness'])
err_min = all_sim_df[all_sim_df['errorness']== all_sim_df['errorness'].min()]
id_cor_max = all_sim_df['correctness'].idxmax()
print(all_sim_df.iloc[id_cor_max]['sim_method'])
