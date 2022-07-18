Classification harmonization with Classificrops
=================================================
Description
------------
To match 2 classes, the tool uses a function that compute similarity between 2 words based on the letters they contains. It is not semantic based. 
Thus, this tool is limited when it comes to match strings that need semantic interpretation. 
As a consequence, this tool is not able to automate fully the conversion from a classification to the ICC one, but at least to semi-automate it. 
To sum up, Classificrops must be viewed as a helping tool to pre-work the conversion and save the user time by making the easy and basic matching. 

  .. image:: ../images/goal.png
    :width: 800

How to use it : the workflow
-----------------------------
#. :ref:`Prepare the data`.
#. If not already installed, :ref:`install` python3, numpy, and pandas.  
#. :ref:`Download` the source code from Github.
#. :ref:`Go to` the folder src/scripts/classificrops/ 
#. :ref:`Choose your inputs`. 
#. :ref:`Run` the script converter.py with the source classification path and the inputs chosen in parameters. 

Step by step
-------------
.. _Prepare the data:

Prepare the data
~~~~~~~~~~~~~~~~
The source classification table should stick to the the following expectations : 
    - format : csv
    - table name : place+'_'+year+'.csv' --> example : FR_2020.csv
    - column name : class+'_'+language        or        '\I\D_'+class+'_'+language --> example : GROUP_fr, CROPS_fr or ID_GROUP_fr, ID_CROPS_fr
    - column name should be written in english (this will be updated soon)
    - Once the third step done (download classificrops code available on Github), the source classification well formatted should be put into the folder data/country. For example, if you are working with a crops classification of Wallonia, you can put it into data/WL. 

.. _install:

Install
~~~~~~~~~
From your terminal : 
``pip install python3``  
``pip install numpy``  
``pip install pandas``  

.. _Download:

Download
~~~~~~~~~
    - From your terminal : ``git clone https://github.com/BertilleT/Classificrops``
    - Or from your browser : 

.. image:: ../images/dwl2_screen.png
    :width: 800

.. _Go to:

Go to 
~~~~~~
    - From your terminal : ``cd src/scripts/classificrops/``
    - Or : from your graphic interface.

.. _Choose your inputs:

Choose your inputs
~~~~~~~~~~~~~~~~~~
+-----------------------+-----------------------------------+-------------------------------------------+
| name input            | format                            | domain                                    |
+=======================+===================================+===========================================+
| path                  | 'data/' + place + '/' + tablename |                                           |
+-----------------------+-----------------------------------+-------------------------------------------+
| place                 | 2 capitalized letters             | [WL,CT,FR,IT]                             |
+-----------------------+-----------------------------------+-------------------------------------------+
| language              | 2 lowercase letters               | [en,fr,it,...]                            |
+-----------------------+-----------------------------------+-------------------------------------------+
| threshold             | a number                          | [0,100]                                   |
+-----------------------+-----------------------------------+-------------------------------------------+
| sim_method            | a string                          | ['basic','split+ratio','token_set_ratio'] |
+-----------------------+-----------------------------------+-------------------------------------------+

.. _Run:

Run 
~~~
``python3 converter.py -c path language place threshold sim_method``
If you want to test different hreshold between 0 and 100 for a same similarity measure, please run : 
``python3 converter.py -t path language place sim_method``

Main issues
------------
    - How to go from a classification written in one language to the ICC classification written in english ? **Translation**
    - Which **shared classification** should we choose ? 
    - How to compute **similarity** between 2 strings ? 
    
