from converter2 import *

'''thresholds =[]
num = 1
while num <= 100: 
  num+=1 
  if num % 10 == 0: 
    thresholds.append(num)'''

#for t in thresholds:
for t in [80,90]:
    converter('../../../../data/FR/FR_2020.csv', 'FR', 1,t)

compareDf = pd.DataFrame (compareList, columns = ['threshold','correctness(%)'])
compareDf.to_csv('../../../../data/FR/compare.csv', index=False)