Reference 
==========
Let us take a look at the 3 functions of Classificrops:  

#.  converter: |br|
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
   
#.  The view_stats function view croplands statistics from Occitania and Catalonia, grouped according to the icc classification. 

.. |br| raw:: html

      <br>