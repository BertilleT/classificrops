import pandas as pd
import requests

src=requests.get('https://geoservices.wallonie.be/arcgis/rest/services/AGRICULTURE/SIGEC_PARC_AGRI_ANON__2020/MapServer/legend').content
df_list = pd.read_html(src)
predata = df_list[6].drop(columns=df_list[6].columns[0])
data = predata.drop(labels=1, axis=0)
data.to_csv('grpCulture_2020_Wallonie.csv')