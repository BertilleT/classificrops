Tutorials 
==============

How to use it : the workflow
-----------------------------
#. :ref:`Download the classification`.
#. :ref:`Rename the classification labels`.
#. If not already installed, :ref:`install` python3, numpy, and pandas.  
#. :ref:`Download the code` the source code from Github.
#. :ref:`Go to` the folder src/scripts/classificrops/ 
#. :ref:`Choose your inputs`. 
#. :ref:`Run` the script converter.py with the source classification path and the inputs chosen in parameters. 

Step by step
-------------
Download the classification
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. _Download the classification:
First, the source classification should be downloaded at CSV format. It can be found in the LPIS website of the country/region under study. 
Here is a an index of 3 LPIS classifications references: 

.. _WL_url_c: https://geoservices.wallonie.be/arcgis/rest/services/AGRICULTURE/SIGEC_PARC_AGRI_ANON__2020/MapServer/legend 
.. _FR_url_c: https://geoservices.ign.fr/documentation/donnees/vecteur/rpg
.. _CAT_url_c: http://agricultura.gencat.cat/ca/ambits/desenvolupament-rural/sigpac/mapa-cultius/

+-----------+-------------+------------------------------------------------------------------------------------------------------------------+
| Area      | url         | note                                                                                                             |
+===========+=============+==================================================================================================================+
| Wallonia  | `WL_url_c`_ | It can be downloaded in csv format from html website with the script src/modules/download/download_WL_to_csv.py  |
+-----------+-------------+------------------------------------------------------------------------------------------------------------------+
| France    | `FR_url_c`_ | The LPIS classification is called "Table référentielle des cultures et des groupes de cultures"                  |
+-----------+-------------+------------------------------------------------------------------------------------------------------------------+
| Catalonia | `CAT_url_c`_| To extract the LPIS classification from Catalonia, you need to download the LPIS data, open it in QGIS, and make |
|           |             | a request on the attributes table to extract unique "Cultiu". You can stock the result into a csv file, and      |
|           |             | lower every items using : src/modules/download/download_WL_to_csv.py                                             |
+-----------+-------------+------------------------------------------------------------------------------------------------------------------+
Actually, the LPIS classifications from Wallonia, France and Catalonia are already downloaded and prepared for the year 2020 : 
::

    Classificrops
    ├── data          
    │   ├── CAT
    |   │   └── CAT_2020.csv
    │   └── FR
    |   |   └── FR_2020.csv
    │   └── WL
    |   |   └── WL_2020.csv
    
    

.. _Rename the classification labels:

Rename the classification labels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Rename the labels of the classification by choosing a value in each column and concatenating with an "\_". X can be replaced by a value of your choice.

+-------+---------+---------+
| ID    | class   | PLACE   |
+=======+=========+=========+
| - ID  | - GROUP | - FR    |
| -     | - CROPS | - WL    |
|       |         | - CAT   |
|       |         | - X     |
+-------+---------+---------+

Column names examples : 
 - GROUP_CAT   
 - CROPS_CAT  
 - ID_CROPS_FR   
 - GROUP_IT (X replaced by IT that stands for Italy) 

.. _install:

Install
~~~~~~~~~
From your terminal : 
``pip install python3``  
``pip install numpy``  
``pip install pandas``  

.. _Download the code:

Download the code
~~~~~~~~~~~~~~~~~~
    - From your terminal : ``git clone https://github.com/BertilleT/Classificrops``
    - Or from your browser : 

.. image:: ../images/dwl2_screen.png
    :width: 800

.. _Go to:

Go to 
~~~~~~
    - From your terminal : ``cd Classificrops/src/scripts_Classificrops``

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