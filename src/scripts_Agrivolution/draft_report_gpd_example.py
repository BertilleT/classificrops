import geopandas as gpd 

Occitania_example = gpd.read_file("/home/BTemple-Boyer-Dury/Documents/Agrivolution/data/shp/RPG_2-0_SHP_LAMB93_R76_2020/PARCELLES_GRAPHIQUES.shp")

Occitania_example.to_csv("/home/BTemple-Boyer-Dury/Documents/Classificrops/data/result/geog_data_example_gpd.csv")