User guide
==============
Description
------------
Classificrops is a tool able to convert one crops classification from an european country/region to the Indicative Crop Classification made by the FAO. 
To match 2 classes, the tool uses a function that compute similarity between 2 words based on the letters they contains. It is not semantic based. 
Thus, this tool is limited when it comes to match strings that need semantic interpretation. 
As a consequence, this tool is not able to automate fully the conversion from a classification to the ICC one, but at least to semi-automate it. 
To sum up, Classificrops must be viewed as a helping tool to pre-work the conversion and save the user time by making the easy and basic matching. 

How to use it : the workflow
-----------------------------
#. :ref:`Prepare the data`.
#. If not already installed, :ref:`install` python3, numpy, and pandas.  
#. :ref:`Download` the source code from Github and add the source classification you are working with in the folder data/country. For example you could download a classification of Wallonia into data/WL. 
#. Go to the folder src/scripts/classificrops/ 
#. :ref:`Choose your inputs`. 
#. Run the script converter.py with the source classification path and the inputs chosen in parameters. 

Step by step
-------------
.. _Prepare the data:

Prepare the data
~~~~~~~~~~~~~~~~
The source classification table should stick to the the following expectations : 
    - format : csv
    - table name : place+'_'+year+'.csv' --> example : FR_2020.csv
    - column name : class+'_'+language        or        'ID_'+class+'_'+language --> example : GROUP_fr, CROPS_fr or ID_GROUP_FR, ID_CROPS_fr
    - column name should be written in english. 

.. _install:

Install
~~~~~~~~~
pip install python3
pip install numpy
pip install pandas

.. _Download:

Download
~~~~~~~~~
git clone https://github.com/BertilleT/Classificrops

.. _Choose your inputs:

Choose your inputs
~~~~~~~~~~~~~~~~~~
+-----------------------+-----------------------+----------------+
| name input            | format                | domain         |
+=======================+=======================+================+
| language              | 2 lowercase letters   | [en,fr,it,...] |
+-----------------------+-----------------------+----------------+
| place                 | 2 capitalized letters | [WL,CT,FR,IT]  |
+-----------------------+-----------------------+----------------+
| threshold             | a number              | [0,100]        |
+-----------------------+-----------------------+----------------+

Main issues
------------
    - How to go from a classification written in one language to the ICC classification written in english ? **Translation**
    - Which **shared classification** should we choose ? 
    - How to compute **similarity** between 2 strings ? 
    
