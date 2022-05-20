from converter import *
import matplotlib.pyplot as plt

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
  compare_df.to_csv('../../data/FR/compare.csv', index=False)

  ax = plt.axis([0, 100, 0, 100])
  ax = plt.gca()

  compare_df.plot(kind='line',x='threshold',y='correctness(%)', color = 'green',ax=ax)
  compare_df.plot(kind='line',x='threshold',y='errorness(%)', color='red', ax=ax)
  plt.title('Wallonia : similarity method = '+sim_method)
  plt.show()

#optimal_threshold('../../data/WL/WL_2020.csv', 'WL','fr', 'token_set_ratio')