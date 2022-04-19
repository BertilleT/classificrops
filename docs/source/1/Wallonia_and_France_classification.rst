Wallonia and France classification
==================================

This section is dedicated to the comparison of croplands classification between Wallonia and France. We focus on the level 1 of classification (by group of crops). 

1) In Wallonia  
| source data : https://geoservices.wallonie.be/arcgis/rest/services/AGRICULTURE/SIGEC_PARC_AGRI_ANON__2020/MapServer/legend  

2) In France  
| source data : https://geoservices.ign.fr/documentation/donnees/vecteur/rpg  


.. csv-table:: Wallonia and France side by side
   :file: ../../../data/comparison_WL_FR.csv
   :header-rows: 1
   :class: longtable
   :widths: 1,10,1,1,10


France and Wallonia classification are different. To study a group crops evolution in both country, we could starts by matching the different classes one by one. 
Yet, this solution is not really satisfying.  

When it comes to a classification with much more classes, the complexity of the matching task increases. Indeed, 
what happen if you decide now to study a crop and not a group of crops. In Wallonia, 143 crops are listed against 352 in France. We would have to match both lists. 
To go further, let's imagine that you want to study the evolution of a crop in France, Wallonia, Flandres, Netherlands, Germany and Austria. How to deal with it ? 

Let's go even further : you want now to study a cropland in all european union countries. There are 27 of them. Then we would have to compute (27*(27+1)/2 = ) 328 matching tasks, 
and without taking into account that sometimes, crop classification are not centralized but managed at a regional level (as in Belgium for example). 
So in reality, it would represent even more than 378 matching tasks. 

We understand why, to study agricultural croplands at an european level, we have to draw a shared classification for all countries from Europe... 
which brings us to the following question : how to define a shared classification ? 