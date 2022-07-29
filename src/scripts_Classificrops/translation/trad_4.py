import geopandas as gpd 
import pandas as pd
#cat_classification = gpd.read_file("/home/BTemple-Boyer-Dury/Documents/Agrivolution/data/shp/Cultius_DUN2020_SHP/Cultius_DUN2020.shp")
#cat_classification.drop_duplicates(subset=['Cultiu'], inplace = True)
#catalan_df = cat_classification[['Grup', 'Cultiu']]
#catalan_df.to_csv('/home/BTemple-Boyer-Dury/Documents/Classificrops/data/CAT/CAT_classification_src.csv', index=False)
cat_classification = pd.read_csv('/home/BTemple-Boyer-Dury/Documents/Classificrops/data/CAT/CAT_classification_src.csv')
print(cat_classification.head())

icc_df = pd.read_csv('/home/BTemple-Boyer-Dury/Documents/Classificrops/data/ICC/ICC.csv')
icc_df['label_cat'] = cat_classification['Cultiu']