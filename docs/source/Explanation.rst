Explanation 
=============
 .. image:: ../images/goal.pdf
    :width: 800

Description
------------
To match 2 classes, the tool uses a function that compute similarity between 2 words based on the letters they contains. It is not semantic based. 
Thus, this tool is limited when it comes to match strings that need semantic interpretation. 
As a consequence, this tool is not able to automate fully the conversion from a classification to the ICC one, but at least to semi-automate it. 
To sum up, Classificrops must be viewed as a helping tool to pre-work the conversion and save the user time by making the easy and basic matching. 


Main issues
------------
    - How to go from a classification written in one language to the ICC classification written in english ? **Translation**
    - Which **shared classification** should we choose ? 
    - How to compute **similarity** between 2 strings ? 



Generate statistics on croplands with Agrivolution
---------------------------------------------------

Analysis
----------

SIG software to study crops evolution and repartition in Europe.
expected deliverable : to be detailed. 
Data ? Yes : SIG database with anonymous geographic data used to receive funds from the agricole common policy. 
[Agrivolution will be an interface able to request easily a database that stores anonymous data about agricultural lands in Europe. The answer of the request should be viewable on a map.]

Actors
~~~~~~~~

    - standard user. For example : land use planning consultant, employee of a local authority, agriculture's minister, agricultural historian, common citizen
    - programmer


Specifications
~~~~~~~~~~~~~~~
    
The standard user should be able to :  
    - select an area of several parcels. The area can be selected at an european level. (example : select all the agricultural lands from Italia and Slovenia).
    - make specific request about the growing type of an area (example : where in Catalonia tomatoes are cultivated ?). 
    - to generate statistics on an area (example : what is the proportion of barley growing in Wallonia ?)
    - to visualize the evolution of agricultural parcels in a specific period of time (example : in Occitania, where agricultural lands have disappeared ?)


Restrictions
~~~~~~~~~~~~~~~~
To begin with, we will focus on France and border countries from EU : Belgium, Luxembourg, Germany, Suisse, Italy, Spain. 


Conception
-----------

Use cases
~~~~~~~~~~

  .. image:: ../images/useCases.png
    :width: 800

Classes
~~~~~~~~
    .. image:: ../images/classes.png
      :width: 800