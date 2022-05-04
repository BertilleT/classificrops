User guide
==============
Description
------------
Classificrops is a tool able to convert one crops classification from an european country/region to the Indicative Crop Classification made by the FAO. 
To match 2 classes, the tool uses a function that compute similarity between 2 words based on the letters they contains. It is not semantic based. 
Thus, this tool is limited when it comes to match strings that need semantic interpretation. 
As a consequence, this tool is not able to automate fully the conversion from a classification to the ICC one, but at least to semi-automate it. 
To sum up, Classificrops must be viewed as a helping tool to pre-work the conversion and save the user time by making the easy and basic matching. 

How to use it
--------------
First, check you have all the inputs in the expected formats. If not, formate the inputs to get the expected format. 
Then, download the source code from Github and add the source classification in the folder data/country.
Then, check you have python3, pandas and numpy installed on your computer. 
Finally, go to the folder src/scripts/classificrops/ and run the script converter.py with the inputs well formatted passed in parameters. 

Input
------
+-----------------------+-----------------------+----------------+
| name input            | format                | domain         |
+=======================+=======================+================+
| source classification | csv table             |                |
+-----------------------+-----------------------+----------------+
| language              | 2 lowercase letters   | [en,fr,it,...] |
+-----------------------+-----------------------+----------------+
| place                 | 2 capitalized letters | [WL,CT,FR,IT]  |
+-----------------------+-----------------------+----------------+
| threshold             | a number              | [0,100]        |
+-----------------------+-----------------------+----------------+

The source classification table should stick to the the following expectations : 
    - table name : place+'_'+year+'.csv' --> example : FR_2020.csv
    - column name : class+'_'+language        or        'ID_'+class+'_'+language --> example : GROUP_fr, CROPS_fr or ID_GROUP_FR, ID_CROPS_fr
    - column name should be written in english. 


Main issues
------------
    - How to go from a classification written in one language to the ICC classification written in english ? **Translation**
    - Which **shared classification** should we choose ? 
    - How to compute **similarity** between 2 strings ? 
    
    
    
Analysis and conception notes
==============================

Wallonia and France classification
-----------------------------------
This section is dedicated to the comparison of croplands classification between Wallonia and France. We focus on the level 1 of classification (by group of crops). 

1) In Wallonia  
| source data : https://geoservices.wallonie.be/arcgis/rest/services/AGRICULTURE/SIGEC_PARC_AGRI_ANON__2020/MapServer/legend  

2) In France  
| source data : https://geoservices.ign.fr/documentation/donnees/vecteur/rpg  


.. csv-table:: Wallonia and France side by side
   :file: ../../data/comparison_WL_FR.csv
   :header-rows: 1
   :class: longtable
   :widths: 1,10,1,1,10


France and Wallonia classification are different. To study a group crops evolution in both country, we could start by matching the different classes one by one. 


When it comes to a classification with much more classes, the complexity of the matching task increases. Indeed, 
what happen if you decide now to study a crop and not a group of crops. In Wallonia, 143 crops are listed against 352 in France. We would have to match both lists, ie to do a matching task. 
To go further, let's imagine that you want to study the evolution of a crop in France, Wallonia, Flandres, Netherlands, Germany and Austria. How to deal with it ? 

Let's go even further : you want now to study a cropland in all european union countries. There are 27 of them. Then we would have to compute (27*(27+1)/2 = ) 328 matching tasks, 
and without taking into account that sometimes, crop classification are not centralized but managed at a regional level (as in Belgium for example). 
So in reality, it would represent even more than 378 matching tasks. 

We understand why, to study agricultural croplands at an european level, we have to draw a shared classification for all countries from Europe... If we consider that we have to study n classifications, 
in the first case we would have to compute (n*(n+1)/2) matching tasks. In the second case, we would have to compute n task. (to match the source classification to the shared classification).
negative delta and a positive >> n²-n is never inferior to 0. n²+n-2n > 0 ie n(n+1) > 2n ie n*(n+1)/2 > n.

This brings us to the following question : how to define a shared classification ? 

European classification
-----------------------

Instead of creating a shared classification from scratch, we will choose an existing classification as a reference. 
At first glance, the Indicative Crop Classification (ICC), issued by the Food and Agricultural Organization (FAO) seems to fit well. 
| source data : https://www.fao.org/3/a0135e/A0135E10.htm#app3 

The following characteristics are interesting to qualify a crop : 
    - growing cycle (temporary/permanent), 
    - crop species, 
    - crop variety (for example, hybrid/ordinary maize), 
    - season (for example, winter/spring wheat), 
    - land type (for example, wetland/dryland rice), 
    - crop use (for example, pumpkin for food/fodder), 
    - type of product (for example, fresh/dried beans), 
    - how the crop is processed (for example, industrial crops), 
    - cultivation methods (for example, crops grown under protective cover).


ICC does not do the distinction between the pumpkin for food or pumpkin for fodder. If you need this information for your analysys, thus ICC does not fit well. 
The EAGLE si another classification that seems really interesting by its oriented object approach. 
Regarding the botanic classification, EPPO is very precise. 
Recap of the classification under study : 
   - ICC (FAO)
   - LUCAS (selected by Dominique in NIVA project)
   - EAGLE
   - EPPO.


Languages
----------
How to compare croplands classification when they are written in various languages ? If we stick to the large run goal which is to study all countries from EU, we have 
at least **24** official languages. 
The idea is to create a table that contains ICC classification written in the 24 official languages.
To do so : 2 alternatives studies :
   - Use Deepl library : https://github.com/DeepLcom/deepl-python. But the number of source languages from Europe available is limited : there are only german, spanish, french, italian, dutsh, polish and portugese.
   - Use google translation. to be studied.

Comparison pros and cons of each method


Tool
----
The goal is to semi automate the crossover between classification from a specific country to the "european" one.
Please run the script src/scripts/classificrops/converter.py. 
result with threshold = 99: correctness = 56%
errorness = 2%

Similarity computing
--------------------
Levenhestein distance with fuzzy research. 

