import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from collections import defaultdict

print('module needed downloaded')
def let_user_pick(options):
    my_list=[]
    print("Please choose:")

    for idx, element in enumerate(options):
        print("{}) {}".format(idx + 1, element))

    inp = input("Enter 2 numbers with a space between them: ")
    l = list(inp.split(" "))
    for n in l: 
        my_list.append(options[int(n) - 1])
    return my_list

def autopct(pct): # only show the label when it's > 10%
    return ('%.2f' % pct) if pct > 5 else ''

def create_keys(my_array):
    my_keys = defaultdict(list)
    for i in my_array: 
        my_keys[i[0:3]].append(i)
    doublons=[]
    for k,l in my_keys.items():
        if len(l) > 1:
            doublons.append(k)
        my_keys[k] = l[0]
    for k in doublons:
        del my_keys[k]
    return my_keys

def view_stats(path_regions_outline, path_dep_outline, path_prov_outline, path_Occ_crops, path_Cat_crops):
    ##download outlines
    #OCCITANIA
    regions_outline = gpd.read_file(path_regions_outline)
    Occitania_outline = regions_outline.loc[regions_outline.loc[:,'LbRegion'] == 'Occitanie']
    Occitania_outline.to_crs(4326,inplace=True)
    print('regions_outline downloaded')
    departments_outline = gpd.read_file(path_dep_outline)
    departments_Occ_outline = gpd.sjoin(Occitania_outline, departments_outline, predicate='intersects')
    dep_Occ = list(departments_Occ_outline["nom"].unique())
    print('departments_outline downloaded and departments from Occitania selected into dep_Occ')
    #CATALONIA
    provincia_Cat_outline = gpd.read_file(path_prov_outline)
    prov_Cat = list(provincia_Cat_outline["nom_prov"].unique())

    ##download crops
    #OCCITANIA
    Occitania_crops = gpd.read_file(path_Occ_crops)
    Occitania_crops.to_crs(4326,inplace=True)
    print('Occitania_crops downloaded and crs converted')
    #CATALONIA
    Catalunya_crops = gpd.read_file(path_Cat_crops)
    Catalunya_crops.to_crs(4326, inplace=True)

    ##download the ICC classification, to be shared by the 2 areas under study
    parent = Path(__file__).parents[2]
    path_icc = parent.joinpath('ICC','ICC_src.csv')
    icc_df = pd.read_csv(path_icc, encoding= 'unicode_escape')
    icc_df['code'] = icc_df['code'].astype('str')
    mask_0 = (icc_df['code'].str.len() == 1)
    LEVEL_0 = icc_df.loc[mask_0]
    LEVEL_0.drop(['broader'],axis=1,inplace=True)
    LEVEL_0.set_index('code', inplace = True)
    d_icc_0 = LEVEL_0.to_dict('dict')
    group_dict_icc_0 = d_icc_0['label_en']
    print("groups dict prepared")
    
    ##define the areas that can selected and ask the user to choose
    options = dep_Occ + prov_Cat
    print('options possibilities initialized')
    deps = let_user_pick(options)
    list_resulting_per = []
    list_resulting_gdf = []
    for dep in deps:
        if dep in dep_Occ: 
            selected_outline = departments_outline.loc[departments_outline.loc[:,'nom']==dep]
            selected_crops = gpd.sjoin(Occitania_crops, selected_outline, predicate='intersects')
            selected_crops.loc[:,'validity'] = selected_crops.loc[:,'geometry'].is_valid
            conversion_Occ_ICC_path = parent.joinpath('data', 'FR', 'handmade_Nicolas_light.csv')
            conversion_fr_icc = pd.read_csv(conversion_Occ_ICC_path, encoding= 'unicode_escape')
            conversion_fr_icc['ID_GROUP_ICC'] = conversion_fr_icc['ICC1.1'].str[:1]
            conversion_fr_icc.drop(['ICC1.1'],axis=1, inplace=True)
            conversion_fr_icc.rename(columns = {'ID_CROPS_FR':'CODE_CULTU'}, inplace=True)
            selected_icc_merged = selected_crops.merge(conversion_fr_icc, how='left', on='CODE_CULTU')
            surf_tot_crops = selected_crops["SURF_PARC"].sum()
            percentages_icc = {}
            for k,v in group_dict_icc_0.items(): 
                a = selected_icc_merged[selected_icc_merged['ID_GROUP_ICC']==str(k)]
                s = a["SURF_PARC"].sum()
                p = (s*100) / surf_tot_crops
                percentages_icc[v] = p
            issue = selected_icc_merged['ID_GROUP_ICC'].loc[selected_icc_merged['ID_GROUP_ICC']=='#']
            no_match = len(issue)*100/len(selected_icc_merged)
            percentages_icc['no_match'] = no_match
            list_resulting_per.append(percentages_icc)
            df_icc_2 = pd.DataFrame.from_dict(percentages_icc,orient='index',columns=['per'])
            list_resulting_gdf.append(selected_icc_merged)
            selected_icc_merged['place'] = dep

        if dep in prov_Cat:
            selected_crops = Catalunya_crops.loc[Catalunya_crops.loc[:,'Provincia']==dep]
            selected_crops = selected_crops[['Grup','Cultiu','HA','geometry']]
            conversion_Cat_ICC_path = parent.joinpath('data', 'CAT', 'handmade_Nicolas_light.csv')
            conversion_cat_icc = pd.read_csv(conversion_Cat_ICC_path, encoding= 'unicode_escape')
            conversion_cat_icc['ID_GROUP_ICC'] = conversion_cat_icc['ICC1.1'].str[:1]
            conversion_cat_icc.drop(['ICC1.1'],axis=1, inplace=True)
            conversion_cat_icc.rename(columns = {'ID_CROPS_CAT':'Cultiu'}, inplace=True)
            selected_crops['Cultiu'] = selected_crops['Cultiu'].str.lower()
            selected_icc_merged = selected_crops.merge(conversion_cat_icc, how='left', on='Cultiu')
            print(selected_icc_merged)
            surf_tot_selected = selected_crops["HA"].sum()
            percentages_icc = {}
            for k,v in group_dict_icc_0.items(): 
                a = selected_icc_merged[selected_icc_merged['ID_GROUP_ICC']==str(k)]
                s = a["HA"].sum()
                p = (s*100) / surf_tot_selected
                percentages_icc[v] = p

            issue = selected_icc_merged['ID_GROUP_ICC'].loc[selected_icc_merged['ID_GROUP_ICC']=='#']
            no_match = len(issue)*100/len(selected_icc_merged)
            percentages_icc['no_match'] = no_match
            list_resulting_per.append(percentages_icc)
            df_icc_3 = pd.DataFrame.from_dict(percentages_icc,orient='index',columns=['per'])
            Grups = selected_icc_merged['Grup'].unique()
            Cultius = selected_icc_merged['Cultiu'].unique()
            Grups_keys = create_keys(Grups)
            Cultius_keys = create_keys(Cultius)
            selected_icc_merged['CODE_GROUP'] = selected_icc_merged['Grup'].apply(lambda x : k if (x == v for k,v in Grups_keys) else x)
            selected_icc_merged['CODE_CULTU'] = selected_icc_merged['Cultiu'].apply(lambda x : k if (x == v for k,v in Cultius_keys) else x)
            selected_icc_merged.drop(['Grup','Cultiu'],axis=1,inplace=True)
            selected_icc_merged.rename(columns={'HA':'SURF_PARC'},inplace=True)
            list_resulting_gdf.append(selected_icc_merged)
            selected_icc_merged['place'] = dep
    mask_1 = (icc_df['broader'].str.len() == 1)
    LEVEL_1 = icc_df.loc[mask_1]
    LEVEL_1.drop(['broader'],axis=1,inplace=True)
    LEVEL_1.set_index('code', inplace = True)
    d_icc_1 = LEVEL_1.to_dict('dict')
    group_dict_icc_1 = d_icc_1['label_en']
    other_detailed = LEVEL_1.iloc[lambda x: x.index.str[:1] == '9']
    string = ', '.join(other_detailed.label_en)

    fig, (ax1,ax2) = plt.subplots(1,2,figsize=(20,10))
    ax1.pie(list_resulting_per[0].values(), autopct=autopct) #plot first pie
    ax2.pie(list_resulting_per[1].values(), autopct=autopct) #plot second pie

    ax1.set_title(deps[0])
    ax2.set_title(deps[1])
    if df_icc_2.loc[ 'Other crops' ,'per'] > 10 or df_icc_3.loc[ 'Other crops' ,'per'] > 10:
        df_icc_2.rename(index = lambda x: x + ' : ' + string if x == 'Other crops' else x, inplace=True)
    fig.legend(df_icc_2.index, loc=8, title = "ICC classification")
    return fig