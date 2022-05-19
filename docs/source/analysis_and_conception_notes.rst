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

Similarity computing
--------------------
Compare similarity computing and optimize the threshold : 

   .. image:: ../images/FR_basic.png
      :width: 800

   .. image:: ../images/FR_split+ratio.png
      :width: 800

   .. image:: ../images/FR_token_set_ratio.png
      :width: 800