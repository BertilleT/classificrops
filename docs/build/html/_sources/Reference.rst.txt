Reference 
==========
Let us take a look at the 3 functions of Classificrops : 
#. convert: To match 2 classes. The converter uses a function that compute similarity between 2 words based on the letters they contains. It is not semantic based. 
Thus, this tool is limited when it comes to match strings that need semantic interpretation. As a consequence, this tool is not able to automate fully the conversion from a classification to the ICC one, but at least to semi-automate it. 
To sum up, converter must be viewed as a helping tool to pre-work the conversion and save the user time by making the easy and basic matching. 
Function: to make automatically at least 30% of the conversion table of the matching between a LPIS classification source and the ICC. 
Steps: 
 - download the classifications
 - filter the classifications (retrieve words not discriminatory)
 - translate icc in the language of the source classification
 - match the classifications (uses string matching functions)
 - if there is a match found with a parent class from source classification, spread the match to the child of this class. 
 - save the matching table (in csv format)

The matching is at the crux of the converter functions. Let us exlplain the matching algorithm, and the similarity method. 
The matching algorithm can be indented into 3 steps, and is represented in the figure below:


The similarity method computes similarity between 2 words based on the letters they contains


Classificrops helps to convert one LPIS classification toward the Indicative Crops Classification(ICC) made by the FAO, in a semi-automated way. 
Classificrops is a tool able to convert one crops classification from an european country/region to the Indicative Crop Classification made by the FAO in a semi-automated way.

Agrivolution is a tool able 
- The convert function converts one LPIS classification toward the Indicative Crops Classification(ICC) made by the FAO, in a semi-automated way. 
    - 
    - 
    - 
    
- The view_stats function view croplands statistics from Occitania and Catalonia, grouped according to the icc classification. 