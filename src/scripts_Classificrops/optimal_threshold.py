from converter import *
import matplotlib.pyplot as plt
import os
from pathlib import Path

parent = Path(__file__).parents[2]
data_path = parent.joinpath('data')
handmade_path = data_path.joinpath(place,'conversion_table_'+place+'_handmade.csv')

def compare(handmade_path,computed,threshold):
    handmade = pd.read_csv(handmade_path)
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

def optimal_threshold(path, place, lg,sim_method): 
  compare_list = []
  thresholds =[]
  num = 1
  while num <= 100: 
    num+=1 
    if num % 10 == 0: 
      thresholds.append(num)

  for t in thresholds:
    compare_list.append(handmade_path,converter(path, place,lg, t,sim_method),t)

  compare_df = pd.DataFrame (compare_list, columns = ['threshold','correctness(%)', 'errorness(%)'])
  
  rel_path_compare = '../../data/'+place+'/compare.csv'
  abs_path_compare = os.path.abspath(rel_path_compare)
  compare_df.to_csv(abs_path_compare, index=False)

  ax = plt.axis([0, 100, 0, 100])
  ax = plt.gca()

  compare_df.plot(kind='line',x='threshold',y='correctness(%)', color = 'green',ax=ax)
  compare_df.plot(kind='line',x='threshold',y='errorness(%)', color='red', ax=ax)
  plt.title(place +' : similarity method = '+sim_method)
  plt.show()

#optimal_threshold('../../data/WL/WL_2020.csv', 'WL','fr', 'token_set_ratio')