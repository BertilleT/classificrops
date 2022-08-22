import pandas as pd
df = pd.read_csv('/home/BTemple-Boyer-Dury/Documents/Classificrops/data/CAT/handmade_Nicolas_light.csv')
print(df)
#df['GROUP_CAT'] = df['GROUP_CAT'].apply(lambda x : x.lower())
#df['CROPS_CAT'] = df['CROPS_CAT'].apply(lambda x : x.lower())
df['ID_CROPS_CAT'] = df['ID_CROPS_CAT'].apply(lambda x : x.lower())
print(df)

df.to_csv('/home/BTemple-Boyer-Dury/Documents/Classificrops/data/CAT/handmade_Nicolas_light.csv', index = False)
