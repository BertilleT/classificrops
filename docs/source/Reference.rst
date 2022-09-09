Reference 
==========
Let us take a look at the 3 functions of Classificrops:  

#.  **converter**: |br|
    Function: to make automatically at least 30% of the conversion table of the matching between a LPIS classification source and the ICC.  |br|
    Note: To match 2 classes, the converter uses a function that compute similarity between 2 words based on the letters they contains. It is not semantic based. 
    Thus, this tool is limited when it comes to match strings that need semantic interpretation. As a consequence, this tool is not able to automate fully the conversion from a classification to the ICC one, but at least to semi-automate it. 
    To sum up, converter must be viewed as a helping tool to pre-work the conversion and save the user time by making the easy and basic matching. |br|
    Function steps: 
        - download the classifications
        - filter the classifications (retrieve words not discriminatory)
        - translate icc in the language of the source classification
        - match the classifications (uses string matching functions)
        - if there is a match found with a parent class from source classification, spread the match to the child of this class. 
        - save the matching table (in csv format)

    The matching is at the crux of the converter functions. Let us exlplain the similarity method and the matching algorithm.  
        - The similarity method computes similarity between 2 words based on the letters they contains. It outputs a score between 0 and 100. If the score is 80, the 2 strings are similar at 80% according to the similarity method used. 

        - The matching algorithm can be indented into 3 steps, and is represented in the figure below:
        .. image:: ../images/algo.png
            :width: 800
   
#.  **view_stats** |br|
    Function: to view croplands statistics with LPIS data from Occitania and Catalonia, grouped according to the icc classification. |br|
    Note: it makes sense to select Occitania and Catalonia as they are border regions. 
    The user should select one department from Occitania, and one community from Catalonia. |br|
    Function steps:
        - download LPIS data, ICC and conversion tables from LPIS to ICC
        - convert LPIS data to the same crs with EPSG code 4326 (projection)
        - ask user to choose 2 areas (one in Occitania, the other in Catalonia)
        - keep data on the selected areas
        - correct the geometry for Occ data (some LPIS data geometries are incorrect)
        - convert LPIS data for each area selected to ICC 
        - for each area, view LPIS stats in pie charts with ICC

    As a result, you can get the image below. 
        .. image:: ../images/stats_PO_Girona_ICC.png
            :width: 800

#.  **optimal_threshold** |br|
    Function: compare handmade and scriptmade conversion tables for one specific similarity method, tested with thresholds from 0 to 100 in steps of 10. |br|
    Function steps:
        - for each threshold in [0,10,20,30,40,50,60,70,80,90,100] compute the conversion table with the converter function. 
        - for each conversion table computed, merged it with the conversion table handmade
        - compute the correctness which is the percentage rate of correct matches found by the algorithm. correctness = number of correct matches*100/number total of LPIS classes
        - compute the errorness which is the percentage rate of error(when the algorithm does not find a match, it is not a error)found by the algorithm. errorness = number of errors*100/number total of LPIS classes.
        - find the threshold for which the errorness is minimum and the correctness is maximum. This threshold is the optimal one. 
        - plot a graph with threshold in the x-axis, errorness and correcntess in the y-axis. The graph points out the optimal threshold. 

    As a result, you can get the image below. 
        .. image:: ../images/CAT_token_set_ratio.png
            :width: 800

.. |br| raw:: html

      <br>