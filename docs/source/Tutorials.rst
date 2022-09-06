Tutorials 
==============
The first tutorial refers to the installation, the second deals with the basic use of the converter function. 
To use the Classificrops, first of all you need to pass by the installation step. 

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