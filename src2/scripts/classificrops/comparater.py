import pandas as pd
##this file is dedicated to compare the conversion table handmade expected and the one got with the script converter.py
def compare(pathHandMade,pathResultGet,threshold):
    handmade = pd.read_csv(pathHandMade)
    computed = pd.read_csv(pathResultGet)
    compare = handmade.copy()
    compare.rename(columns={'ID_GROUP_ICC':'ID_GROUP_ICC_handmade'}, inplace=True)
    compare['ID_GROUP_ICC_computed'] = computed['ID_GROUP_ICC']

    booleanSerie = compare.apply(lambda x : True if (x.ID_GROUP_ICC_handmade==x.ID_GROUP_ICC_computed) else False,axis=1)
    booleanDf = booleanSerie.to_frame()
    booleanDf = booleanDf.rename(columns = {0:'bool'})
    tot = len(compare)
    match = booleanDf['bool'].sum()
    per = round((match*100)/tot)

    print('The conversion table computed with the threshold = ' + str(threshold) + ', fits to the expected output at ' + str(per) + '%.')
    return (threshold,per)