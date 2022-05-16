#test3.py
import pandas as pd
import matplotlib.pyplot as plt

compare_df = pd.read_csv('../../data/FR/compare.csv')
#plt.axis([0, 100, 0, 100])
#compare_df.plot(x ='threshold', y='correctness(%)', color = 'green')
compare_df.plot(x ='threshold', y='errorness(%)', color = 'red', x ='threshold', y='correctness(%)', color = 'green')
plt.axis([0, 100, 0, 100])
plt.show()