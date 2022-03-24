import csv

inputfile = csv.reader(open("../data/csv/grpCulture_2020_France.csv", 'r', newline=''), delimiter=';')
with open('../data/csv/grpCulture_2020_France_grp.csv', 'w', newline='') as f:
    write = csv.writer(f)
    groups=[]
    for row in inputfile: 
        if row[3] not in groups:
            groups.append(row[3])
    for group in groups:
        write.writerow( [ group ] )