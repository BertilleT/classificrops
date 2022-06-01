from converter import *
import matplotlib.pyplot as plt
import os

def optimal_threshold(path, place, lg,sim_method): 
  compare_list = []
  thresholds =[]
  num = 1
  while num <= 100: 
    num+=1 
    if num % 10 == 0: 
      thresholds.append(num)

  for t in thresholds:
    compare_list.append(converter(path, place,lg, t,sim_method))

  compare_df = pd.DataFrame (compare_list, columns = ['threshold','correctness(%)', 'errorness(%)'])
  
<<<<<<< HEAD
  rel_path_compare = '../../data/'+place+'/compare.csv'
=======
  rel_path_compare = '../../data/FR/compare.csv'
>>>>>>> 3f2cbac508812f96c9995d010ddefcdd997a845b
  abs_path_compare = os.path.abspath(rel_path_compare)
  compare_df.to_csv(abs_path_compare, index=False)

  ax = plt.axis([0, 100, 0, 100])
  ax = plt.gca()

  compare_df.plot(kind='line',x='threshold',y='correctness(%)', color = 'green',ax=ax)
  compare_df.plot(kind='line',x='threshold',y='errorness(%)', color='red', ax=ax)
  plt.title('Wallonia : similarity method = '+sim_method)
  plt.show()

#optimal_threshold('../../data/WL/WL_2020.csv', 'WL','fr', 'token_set_ratio')