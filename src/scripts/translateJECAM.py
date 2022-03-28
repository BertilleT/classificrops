import csv
import translator

f = open('../../data/csv/JECAM/JECAM_en.csv')
jecam = csv.reader(f)

#the function below is dedicated to the translation of JECAM crops groups to french. In a second time, I will have to apply the function to all languages, and also to crops inside a group. 
for row in jecam:
    translator.translate(f"{row[2]}", "fr")
