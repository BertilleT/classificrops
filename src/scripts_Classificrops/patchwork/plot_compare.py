import pandas as pd
import matplotlib.pyplot as plt

compare_df = pd.read_csv('../../data/FR/compare.csv')

ax = plt.axis([0, 100, 0, 100])
ax = plt.gca()

compare_df.plot(kind='line',x='threshold',y='correctness(%)', color = 'green',ax=ax)
compare_df.plot(kind='line',x='threshold',y='errorness(%)', color='red', ax=ax)
plt.title('similarity method = split+ratio')
plt.show()