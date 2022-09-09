Explanation 
=============
Context
--------
This Github is dedicated to help to build an European dataset from existing
national and regional agricultural data(LPIS data). It aims at simplifying the reuse of those data, especially for
Artificial Intelligence at the European level(to increase the size of AI datasets). In order to build this set, first a data format has to
be chosen, including geographical coordinates systems, language and an agricultural classification
that suits everyone. Then the existing data has to be converted into this common format. With this
in mind, I developed converter, a tool that helps matching a national crop nomenclature with
a common crop nomenclature, here the Indicative Crop Classification from the Food Agriculture
Organisation, in a semi-automated way. The scope of the LPIS data harmonisation should not be limited to its use in machine learning. 
To illustrate the broad field of application of the LPIS data harmonisation eased by the converter function, 
I developed a tool that uses LPIS harmonized data to visualise statistics
on agricultural crops in Occitania and Catalonia. This second tool, called view_stats, could be
useful for public policies on land use planning.

Alternatives approach
---------------------
LPIS data could be harmonized with other classification than ICC. For example, the Eurocrops project made by researchers from Munich University did it with the HCAT taxonomy, inpired from the EAGLE matrix: https://github.com/maja601/EuroCrops