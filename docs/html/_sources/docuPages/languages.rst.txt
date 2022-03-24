Languages spoken in ... 
========================

... the project code 
---------------------
- language : python  
- library : pandas  

Python vs R ?   

Python is already used by the team.  


Pandas vs Numpy ?   

Numpy is adapted when working with the same type of data (numbers) stored into matrices. It allows to make quick computation.  
In this project, we deal with different types of data, as textual (name of groups of cultures) stored in data tables. Moreover, we do not need to make quick computation for now, so pandas fits well. 

... the documentation 
----------------------
- language : reStructuredText  
- library : Sphinx   


reStructuredText vs Markdown ?   

Markdown is purely presentationnal, whereas reStructuredText provides a set of roles and directives as the math role to write a mathematical 
equation. We could argue that Markdown offers the possibility to extend syntax by choosing a flavor and that's true, but one should admit that it is easy to lose oneself among the variety of 
flavors available.  
Regarding the ability to support different languages, Sphinx (that works with rst) has a better output than Dioxygen (that works with rm).
To sum up, Markdown is dedicated to write for the Web, reStructuredText and Sphinx are dedicated to write technical documentation. 
As we want to write a techniqual documentation, we wil use rst and Shpinx. 