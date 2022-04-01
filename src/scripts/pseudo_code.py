#pseudo code

#User wants to know where on a map is located a crop in Wallonia, France and Catalunya. 

map (crop, area, time): 
#user chosses crops among a list of crops classified according to JECAM classification. 

#locate function returns all the entities that are included in the area selected by the user. Entities can be countries when we have countries data or regions when we have the data at regional level. 
locate(area): 
    (...)
    countries = []
    return countries

places=[]
for c in countries: 
    if conversion_$c does not exist:
        conversion_$c = converte(c)
        #for every entity concerned by the area, if the conversion table does not exist yet, create it. 
    p = SELECT location, superficies FROM CAP_DB_$c INNER JOIN conversion_$c ON CAP_DB_$c.key = conversion_$c.key 
    #location is conceived as a list of vertex coordinates. Superficie is asked also in case we would like to generate statistics too. 
    places.append(p)
    displayMap(places) #display on QGIS map all th places location returned by the select requests 
    