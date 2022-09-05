Tutorials 
==============
To use the toolbox, first of all you need to pass by the installation step. 

How to install the toolbox
--------------------------------------
#. If not already installed, :ref:`Install` python3, numpy, deepl and pandas.  
#. :ref:`Download the code` the source code from Github.
#. :ref:`Go to the scripts_Classificrops folder`

.. _Install:

Install
~~~~~~~~~
From your terminal : 
 -  ``pip install python3``   
 -  ``pip install numpy``   
 -  ``pip install pandas``   
 -  ``pip install deepl``   
 -  ``pip install deopandas``   
 
.. _Download the code:

Download the code
~~~~~~~~~~~~~~~~~~
    - From your terminal : ``git clone https://github.com/BertilleT/Classificrops``
    - Or from your browser : 

.. image:: ../images/dwl2_screen.png
    :width: 800
--> do not forget to dezip the folder  

.. _Go to the scripts_Classificrops folder:

Go to the scripts_Classificrops folder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
From your terminal : ``cd Classificrops/src/scripts_Classificrops``

How to convert 2020 Wallonia LPIS classification to ICC
-----------------------------------------------------------
Run 
~~~
``python3 parser.py -f converter``

How to view statistics on Catalonia and Girona LPIS data from 2020, harmonized with ICC
----------------------------------------------------------------------------------------
#. :ref:`Download the geo-data` in a separated folder from Classificrops 
#. :ref:`Go to the scripts_Classificrops folder`
#. :ref:`Write paths into json` file options_view_stats.json
#. :ref:`Run the command` 

.. _Download the geo-data: 

Download the geo-data
~~~~~~~~~~~~~~~~~~~~~~
Downlaod the LPIS data, be careful to NOT download it in Classificrops.  

.. list-table:: Url sources of LPIS data and outlines for Occitania and Catalonia
   :widths: 30 20 30
   :header-rows: 1

   * - url
     - file name
     - note
   * - `Regions outline of France <https://geo.data.gouv.fr/fr/datasets/abd5ac0296e370c97d3ee440c7d126ee12106df5>`_
     - Region2020.shp
     - 
   * - `Departments outline of France <https://osm13.openstreetmap.fr/~cquest/openfla/export/>`_
     - departements-20220101-shp.zip
     -
   * - `Provinces outline of Catalonia <https://analisi.transparenciacatalunya.cat/Urbanisme-infraestructures/L-mits-administratius-provincials-de-Catalunya/ghr8-wp3h>`_
     - 
     - On the right part of the screen, click on "exportar" and "ShapeFile"
   * - `LPIS data from Occitania 2020 <ftp://RPG_ext:quoojaicaiqu6ahD@ftp3.ign.fr/RPG_2-0__SHP_LAMB93_R76_2020-01-01.7z>`_
     - 
     - if you use linux, use "wget url_copied_from_here" command from your terminal to download this file. Do not forget to dezip it too
   * - `LPIS data from Catalonia 2020 <http://agricultura.gencat.cat/ca/ambits/desenvolupament-rural/sigpac/mapa-cultius/>`_
     -  Mapa de cultius 2020
     - 


.. _Go to the scripts_Classificrops folder:

Go to the scripts_Classificrops folder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
From your terminal : ``cd Classificrops/src/scripts_Classificrops``

.. _Write paths into json:

Write paths into json
~~~~~~~~~~~~~~~~~~~~~~~~
Inside the options_view_stats.json file, overwrite the registered paths by the paths that lead to the shapefiles data freshly downloaded on your local computer. 

.. _Run the command:

Run 
~~~
``python3 parser.py -f view_stats``