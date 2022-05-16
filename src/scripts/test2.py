from converter import *
import matplotlib.pyplot as plt

compare_list = []
thresholds =[]
num = 1
while num <= 100: 
  num+=1 
  if num % 10 == 0: 
    thresholds.append(num)

for t in thresholds:
#for t in [80,90]:
  compare_list.append(converter('../../data/FR/FR_2020.csv', 'FR','fr', t,'split+ratio'))

compare_df = pd.DataFrame (compare_list, columns = ['threshold','correctness(%)', 'errorness(%)'])
compare_df.to_csv('../../data/FR/compare.csv', index=False)
compare_df.plot(x ='threshold', y='correctness(%)', kind = 'scatter', color = 'green')
compare_df.plot(x ='threshold', y='errorness(%)', kind = 'scatter', color = 'red')
plt.show()