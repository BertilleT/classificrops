import pandas as pd
import requests
import csv

URL=input("URL to parse?")
src=requests.get(URL).content
nametosave=input("what name to save tables by?")
df_list = pd.read_html(src)
for i, df in enumerate(df_list):
    df.to_csv(f'{nametosave} {i}.csv'.format(i))
#Pretty neat and tiny.

