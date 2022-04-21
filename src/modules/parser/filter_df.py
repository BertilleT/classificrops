import csv 
import pandas as pd

#this script is dedicated to filter non discriminatory words as "and", and punctuations in the classification under study.
#when looking at ICC we identify : 'n.e.c.' ',', '(', ')', ',', '.', '-', 'spp'=several species, 'other', 'crops', 'and', 'or'
#when it comes to french classification, we identify '/'

#we will use regular expressions

def filter(df, col):
    mylist=['other','crops','and','or','n.e.c.', 'spp'] #we should retrieve one word + one space before or after the word if there is one
    mydict = {f'(?i){word}':'' for word in mylist}
    df[col] = df[col].replace(mydict, regex=True)
    df[col] = df[col].str.replace(r'[^\w\s]+', '')
    df[col] = df[col].str.replace('   ', ' ')
    df[col] = df[col].str.replace('  ', ' ')
    return df[col]
