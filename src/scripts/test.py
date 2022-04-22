import pandas as pd
def compare(handmade,computed):
    compare = handmade.copy()
    compare.rename(columns={'A':'A_hd'}, inplace=True)
    compare['A_cp'] = computed['A']

    booleanSerie = compare.apply(lambda x : True if (x.A_hd==x.A_cp) else False,axis=1)
    booleanDf = booleanSerie.to_frame()
    booleanDf = booleanDf.rename(columns = {0:'bool'})
    tot = len(compare)
    match = booleanDf['bool'].sum()
    per = round((match*100)/tot)
    return per

d1 = {'A': [1, 2, 3, 4, 5]}
df1 = pd.DataFrame(data=d1)
d2 = {'A': [1, 1, 1, 1, 1]}
df2 = pd.DataFrame(data=d2)

d3 = {'A': [1, 2, 2, 2, 2]}
df3 = pd.DataFrame(data=d3)
d4 = {'A': [1, 2, 2, 2, 3]}
df4 = pd.DataFrame(data=d4)
L=[(df1,df2),(df3,df4)]
T=[]



for (i,j) in L:
    T.append(compare(i,j))
print(T)
    