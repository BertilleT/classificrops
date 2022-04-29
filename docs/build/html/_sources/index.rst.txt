.. Agrivolution documentation master file, created by
   sphinx-quickstart on Mon Mar 21 11:00:50 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Agrivolution's documentation
============================
The project is divided into 2 parts. 

1) classification standardization
    expected deliverable : a tool coded in python, able to convert one crops classification to another one, with a clean documentation written in sphinx. 
    Data storage need ? No. 

2) SIG software to study crops evolution and repartition in Europe.
    expected deliverable : to be detailed. 
    Data ? Yes : SIG database with anonymous geographic data used to receive funds from the agricole common policy. 
    [Agrivolution will be an interface able to request easily a database that stores anonymous data about agricultural lands in Europe. The answer of the request should be viewable on a map.]

-----

.. toctree::
   :numbered:
   
   classificrops
   agrivolution


Installation
------------

Install by running:

    install agrivolution


Languages spoken in ... 
------------------------

... the project code 
~~~~~~~~~~~~~~~~~~~~~~

- language : python  
- library : pandas  

Python vs R ?   

Python is already used by the team.  


Pandas vs Numpy ?   

Numpy is adapted when working with the same type of data (numbers) stored into matrices. It allows to make quick computation.  
In this project, we deal with different types of data, as textual (name of groups of cultures) stored in data tables. Moreover, we do not need to make quick computation for now, so pandas fits well. 

... the documentation 
~~~~~~~~~~~~~~~~~~~~~~

- language : reStructuredText  
- library : Sphinx   


reStructuredText vs Markdown ?   

Markdown is purely presentational, whereas reStructuredText provides a set of roles and directives as the math role to write a mathematical 
equation. We could argue that Markdown offers the possibility to extend syntax by choosing a flavor and that's true, but one should admit that it is easy to lose oneself among the variety of 
flavors available.  
Regarding the ability to support different languages, Sphinx (that works with rst) has a better output than Dioxygen (that works with rm).
To sum up, Markdown is dedicated to write for the Web, reStructuredText and Sphinx are dedicated to write technical documentation. 
As we want to write a technical documentation, we wil use rst and Shpinx. 

Contribute
----------

- Issue Tracker: github.com/BertilleT/Agrivolution/issues
- Source Code: github.com/BertilleT/Agrivolution

Support
-------

If you are having issues, please let me know at btemple-boyer-dury@ign.fr

License
-------

Open source. 