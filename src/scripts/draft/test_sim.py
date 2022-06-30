#test sim_method == 'split+ratio+symetric':
from fuzzywuzzy import fuzz
import pandas as pd
trg='céréales et graminés'
src='graminé'

nb = 0
src_l = src.split()
len_src = len(src_l)
trg_l = trg.split()
myList=[]
for w in src_l:
    for x in trg_l:
        myList.append([src_l.index(w),fuzz.ratio(w,x)])
cols = ['index', 'sim']
print(myList)
myDf = pd.DataFrame(myList, columns=cols)
r = myDf.groupby('index')['sim'].max().reset_index()
print(r.head())

'''if len(trg_l) == 1 :
    #ranger r par ordre de similarité décroissante 
    sorted_r = r.sort_values(["sim"], ascending=False)
    #selectionner premier element de r
    nb = sorted_r.iloc[0,1]
else : '''
total = r['sim'].sum()
nb = total / len_src

print(nb)