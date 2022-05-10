[33mcommit 1cd2d1ce5ce54c539b8b9f350ddaa8537a4d7fe3[m[33m ([m[1;36mHEAD -> [m[1;32mimprove_converter[m[33m, [m[1;31morigin/main[m[33m, [m[1;32mmain[m[33m)[m
Author: Bertille Temple-Boyer-Dury <bertilletemple@yahoo.fr>
Date:   Thu May 5 14:03:02 2022 +0200

    minor changes in user guide

[1mdiff --git a/docs/build/doctrees/environment.pickle b/docs/build/doctrees/environment.pickle[m
[1mindex dd3113e..bea0544 100644[m
Binary files a/docs/build/doctrees/environment.pickle and b/docs/build/doctrees/environment.pickle differ
[1mdiff --git a/docs/build/doctrees/index.doctree b/docs/build/doctrees/index.doctree[m
[1mindex 14f4ade..c757c5c 100644[m
Binary files a/docs/build/doctrees/index.doctree and b/docs/build/doctrees/index.doctree differ
[1mdiff --git a/docs/build/doctrees/user guide.doctree b/docs/build/doctrees/user guide.doctree[m
[1mindex 7d76503..84314f2 100644[m
Binary files a/docs/build/doctrees/user guide.doctree and b/docs/build/doctrees/user guide.doctree differ
[1mdiff --git a/docs/build/html/_images/dwl2_screen.png b/docs/build/html/_images/dwl2_screen.png[m
[1mnew file mode 100644[m
[1mindex 0000000..be4fb3b[m
Binary files /dev/null and b/docs/build/html/_images/dwl2_screen.png differ
[1mdiff --git a/docs/build/html/_images/goal.png b/docs/build/html/_images/goal.png[m
[1mnew file mode 100644[m
[1mindex 0000000..61e704f[m
Binary files /dev/null and b/docs/build/html/_images/goal.png differ
[1mdiff --git a/docs/build/html/_sources/index.rst.txt b/docs/build/html/_sources/index.rst.txt[m
[1mindex a0b5182..f26c7de 100644[m
[1m--- a/docs/build/html/_sources/index.rst.txt[m
[1m+++ b/docs/build/html/_sources/index.rst.txt[m
[36m@@ -27,4 +27,4 @@[m [mIf you are having issues, please let me know at bertilletemple@yahoo.fr[m
 License[m
 -------[m
 [m
[31m-Open source. [m
\ No newline at end of file[m
[32m+[m[32mGNU General Public License v3.0[m
\ No newline at end of file[m
[1mdiff --git a/docs/build/html/_sources/user guide.rst.txt b/docs/build/html/_sources/user guide.rst.txt[m
[1mindex 6cdc4f1..30e1363 100644[m
[1m--- a/docs/build/html/_sources/user guide.rst.txt[m	
[1m+++ b/docs/build/html/_sources/user guide.rst.txt[m	
[36m@@ -7,15 +7,17 @@[m [mTo match 2 classes, the tool uses a function that compute similarity between 2 w[m
 Thus, this tool is limited when it comes to match strings that need semantic interpretation. [m
 As a consequence, this tool is not able to automate fully the conversion from a classification to the ICC one, but at least to semi-automate it. [m
 To sum up, Classificrops must be viewed as a helping tool to pre-work the conversion and save the user time by making the easy and basic matching. [m
[32m+[m[32m    .. image:: ../images/goal.png[m
[32m+[m[32m      :width: 800[m
 [m
 How to use it : the workflow[m
 -----------------------------[m
 #. :ref:`Prepare the data`.[m
 #. If not already installed, :ref:`install` python3, numpy, and pandas.  [m
[31m-#. :ref:`Download` the source code from Github and add the source classification you are working with in the folder data/country. For example you could download a classification of Wallonia into data/WL. [m
[31m-#. Go to the folder src/scripts/classificrops/ [m
[32m+[m[32m#. :ref:`Download` the source code from Github.[m
[32m+[m[32m#. :ref:`Go to` the folder src/scripts/classificrops/[m[41m [m
 #. :ref:`Choose your inputs`. [m
[31m-#. Run the script converter.py with the source classification path and the inputs chosen in parameters. [m
[32m+[m[32m#. :ref:`Run` the script converter.py with the source classification path and the inputs chosen in parameters.[m[41m [m
 [m
 Step by step[m
 -------------[m
[36m@@ -26,36 +28,56 @@[m [mPrepare the data[m
 The source classification table should stick to the the following expectations : [m
     - format : csv[m
     - table name : place+'_'+year+'.csv' --> example : FR_2020.csv[m
[31m-    - column name : class+'_'+language        or        'ID_'+class+'_'+language --> example : GROUP_fr, CROPS_fr or ID_GROUP_FR, ID_CROPS_fr[m
[31m-    - column name should be written in english. [m
[32m+[m[32m    - column name : class+'_'+language        or        'ID_'+class+'_'+language --> example : GROUP_fr, CROPS_fr or ID_GROUP_fr, ID_CROPS_fr[m
[32m+[m[32m    - column name should be written in english (this will be updated soon)[m
[32m+[m[32m    - Once the third step done (download classificrops code available on Github), the source classification well formatted should be put into the folder data/country. For example, if you are working with a crops classification of Wallonia, you can put it into data/WL.[m[41m [m
 [m
 .. _install:[m
 [m
 Install[m
 ~~~~~~~~~[m
[31m-pip install python3[m
[31m-pip install numpy[m
[31m-pip install pandas[m
[32m+[m[32mFrom your terminal :[m[41m [m
[32m+[m[32m``pip install python3``[m[41m  [m
[32m+[m[32m``pip install numpy``[m[41m  [m
[32m+[m[32m``pip install pandas``[m[41m  [m
 [m
 .. _Download:[m
 [m
 Download[m
 ~~~~~~~~~[m
[31m-git clone https://github.com/BertilleT/Classificrops[m
[32m+[m[32m    - From your terminal : ``git clone https://github.com/BertilleT/Classificrops``[m
[32m+[m[32m    - Or from your browser :[m[41m [m
[32m+[m[32m    .. image:: ../images/dwl2_screen.png[m
[32m+[m[32m      :width: 800[m
[32m+[m
[32m+[m[32m.. _Go to:[m
[32m+[m
[32m+[m[32mGo to[m[41m [m
[32m+[m[32m~~~~~~[m
[32m+[m[32m    - From your terminal : ``cd src/scripts/classificrops/``[m
[32m+[m[32m    - Or : from your graphic interface.[m
 [m
 .. _Choose your inputs:[m
 [m
 Choose your inputs[m
 ~~~~~~~~~~~~~~~~~~[m
[31m-+-----------------------+-----------------------+----------------+[m
[31m-| name input            | format                | domain         |[m
[31m-+=======================+=======================+================+[m
[31m-| language              | 2 lowercase letters   | [en,fr,it,...] |[m
[31m-+-----------------------+-----------------------+----------------+[m
[31m-| place                 | 2 capitalized letters | [WL,CT,FR,IT]  |[m
[31m-+-----------------------+-----------------------+----------------+[m
[31m-| threshold             | a number              | [0,100]        |[m
[31m-+-----------------------+-----------------------+----------------+[m
[32m+[m[32m+-----------------------+-----------------------------------+----------------+[m
[32m+[m[32m| name input            | format                            | domain         |[m
[32m+[m[32m+=======================+===================================+================+[m
[32m+[m[32m| path                  | 'data/' + place + '/' + tablename |                |[m
[32m+[m[32m+-----------------------+-----------------------------------+----------------+[m
[32m+[m[32m| language              | 2 lowercase letters               | [en,fr,it,...] |[m
[32m+[m[32m+-----------------------+-----------------------------------+----------------+[m
[32m+[m[32m| place                 | 2 capitalized letters             | [WL,CT,FR,IT]  |[m
[32m+[m[32m+-----------------------+-----------------------------------+----------------+[m
[32m+[m[32m| threshold             | a number                          | [0,100]        |[m
[32m+[m[32m+-----------------------+-----------------------------------+----------------+[m
[32m+[m
[32m+[m[32m.. _Run:[m
[32m+[m
[32m+[m[32mRun[m[41m [m
[32m+[m[32m~~~[m
[32m+[m[32m``python3 converter.py path language place threshold``[m
 [m
 Main issues[m
 ------------[m
[1mdiff --git a/docs/build/html/index.html b/docs/build/html/index.html[m
[1mindex ad7398f..1934355 100644[m
[1m--- a/docs/build/html/index.html[m
[1m+++ b/docs/build/html/index.html[m
[36m@@ -44,7 +44,9 @@[m
 <li class="toctree-l3"><a class="reference internal" href="user%20guide.html#prepare-the-data">1.3.1. Prepare the data</a></li>[m
 <li class="toctree-l3"><a class="reference internal" href="user%20guide.html#install">1.3.2. Install</a></li>[m
 <li class="toctree-l3"><a class="reference internal" href="user%20guide.html#download">1.3.3. Download</a></li>[m
[31m-<li class="toctree-l3"><a class="reference internal" href="user%20guide.html#choose-your-inputs">1.3.4. Choose your inputs</a></li>[m
[32m+[m[32m<li class="toctree-l3"><a class="reference internal" href="user%20guide.html#go-to">1.3.4. Go to</a></li>[m
[32m+[m[32m<li class="toctree-l3"><a class="reference internal" href="user%20guide.html#choose-your-inputs">1.3.5. Choose your inputs</a></li>[m
[32m+[m[32m<li class="toctree-l3"><a class="reference internal" href="user%20guide.html#run">1.3.6. Run</a></li>[m
 </ul>[m
 </li>[m
 <li class="toctree-l2"><a class="reference internal" href="user%20guide.html#main-issues">1.4. Main issues</a></li>[m
[36m@@ -73,7 +75,7 @@[m
 </section>[m
 <section id="license">[m
 <h2>License<a class="headerlink" href="#license" title="Permalink to this headline">¬∂</a></h2>[m
[31m-<p>Open source.</p>[m
[32m+[m[32m<p>GNU General Public License v3.0</p>[m
 </section>[m
 </section>[m
 [m
[1mdiff --git a/docs/build/html/objects.inv b/docs/build/html/objects.inv[m
[1mindex acd064f..2c83293 100644[m
[1m--- a/docs/build/html/objects.inv[m
[1m+++ b/docs/build/html/objects.inv[m
[36m@@ -2,6 +2,4 @@[m
 # Project: Classificrops[m
 # Version: [m
 # The remainder of this file is compressed using zlib.[m
[31m-x⁄Öë;Nƒ0Ü{üb$†4J:¥4[¨	qÄ¡Ké«ÚCêékp=NÇgŸÑE§±bœ˜?Ï†C;Dù≈NëOÜ8N!&}ØYÅº-Û[m
[31m-^››¥¨'∏l&¸∫KΩÖáˇÖÍò#¡¿9Äq>ßbÒÖÏì#Ö‚◊f£iÚª®[m
[31m-9*‰¨ÿùôÕoŒ2Í-∑KxúI—í3N”˚Zr<≠óŸèü‚ÑÕè± vc4ØFˆÒÎ„3BarO.·xÌ¢ç	≠›ÓµØ†ËYˇQÀÚ8®π÷Ÿ“\–ÚRG†1·V⁄ÃÀ¬Àâo~àEﬁFëfH]˘Ω´>ë0®n-¨gUÛTÁ∂$∆v0u[æYgx˛·ƒ7™Í˜°[m
\ No newline at end of file[m
[32m+[m[32mx⁄ÖíœJƒ0áÔyäıQèﬁdŸ√BQ|Ä±€@ö)˘ÉˆÊk¯z>âI”uªÆòKI3ﬂ|øLZ¥h&Ø=†U–≤miö-X‰¡u´∏yùÍº∏πJhz‡Ù2„ó}‹˝gmœÏ	&é¥c(!_»‰òË…%_µ¢ŸwV:dÓêK«ÊD"øY√®j∂s∏_H—ë’V—˚qÀ~∑≥ÕK—1Æô;ñ	z»®8xó€[)7Ω◊Ø∫u<˙ØèOââŸÄ˘ûRØhL}êm≈¿Íè9∆IÓ%w«*Z&çËBO†0`-m·e‚ÂÃ7øbïW9H3Ö>˝GÁq—÷~åVxB◊ˆ«lŸ+ÚßRo∞#ë0÷ü‚ƒœ?ú¯õd[m
\ No newline at end of file[m
[1mdiff --git a/docs/build/html/searchindex.js b/docs/build/html/searchindex.js[m
[1mindex b2c0646..ac481f9 100644[m
[1m--- a/docs/build/html/searchindex.js[m
[1m+++ b/docs/build/html/searchindex.js[m
[36m@@ -1 +1 @@[m
[31m-Search.setIndex({docnames:["analysis and conception notes","index","user guide"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":3,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":2,"sphinx.domains.rst":2,"sphinx.domains.std":1,sphinx:56},filenames:["analysis and conception notes.rst","index.rst","user guide.rst"],objects:{},objnames:{},objtypes:{},terms:{"100":2,"143":0,"328":0,"352":0,"378":0,"assimil\u00e9":0,"bl\u00e9":0,"c\u00e9r\u00e9ale":0,"case":0,"class":[0,2],"final":[],"fourrag\u00e8r":0,"function":2,"gel\u00e9":0,"l\u00e9gume":0,"l\u00e9gumineus":0,"ma\u00ef":0,"mara\u00eech\u00e8r":0,"ol\u00e9agineux":0,"prot\u00e9agineux":0,"true":[],But:0,For:2,The:[0,2],Then:0,There:0,Use:0,a0135:0,a0135e10:0,abil:[],abl:2,account:0,adapt:[],add:2,admit:[],against:0,agricultur:0,all:0,allow:[],alreadi:2,altern:0,among:[],analysi:1,anoth:0,app3:0,approach:0,arcgi:0,argu:[],austria:0,autom:[0,2],autr:0,avail:0,base:2,basic:2,bean:0,belgium:0,bertillet:[1,2],bertilletempl:1,better:[],between:[0,2],botan:0,both:0,bring:0,cann:0,capit:2,central:0,characterist:0,check:[],choos:[0,1],chosen:2,classif:[1,2],classificrop:[0,2],clone:2,code:[1,2],column:2,colza:0,com:[0,1,2],come:[0,2],compar:0,comparison:0,complex:0,comput:[1,2],con:0,concept:1,consequ:2,consid:0,contain:[0,2],convers:2,convert:[0,2],coqu:0,correct:0,could:[0,2],countri:[0,2],cover:0,creat:0,crop:[0,2],cropland:0,crops_fr:2,crossov:0,csv:2,cultiv:0,cultur:0,cycl:0,data:[0,1],deal:0,decid:0,dedic:0,deepl:0,deeplcom:0,defin:0,delta:0,descript:1,differ:0,dioxygen:[],direct:[],distanc:0,distinct:0,diver:0,document:0,doe:0,domain:2,dominiqu:0,donne:0,download:1,draw:0,dri:0,dryland:0,dutsh:0,each:0,eagl:0,easi:2,english:2,ensilag:0,eppo:0,equat:[],error:0,estiv:0,europ:0,european:[1,2],even:0,evolut:0,exampl:[0,2],exist:0,expect:2,extend:[],fao:[0,2],fibr:0,first:0,fit:0,flandr:0,flavor:[],fleur:0,focu:0,fodder:0,folder:2,follow:[0,2],food:0,format:2,fourrag:0,fr_2020:2,franc:1,french:0,fresh:0,from:[0,2],fruit:0,fulli:2,further:0,fuzzi:0,gel:0,geoservic:0,german:0,germani:0,get:[],git:2,github:[0,1,2],glanc:0,goal:0,googl:0,grain:0,group:0,group_fr:[0,2],group_wl:0,grow:0,grown:0,guid:1,happen:0,has:[],have:[0,1],help:2,horticol:0,how:[0,1],htm:0,http:[0,2],hybrid:0,icc:[0,2],id_:2,id_crops_fr:2,id_group_fr:2,idea:0,ign:0,imagin:0,increas:0,inde:0,index:0,indic:[0,2],industri:0,industriel:0,inferior:0,inform:0,input:1,instal:1,instead:0,interest:0,interpret:2,issu:[0,1],italian:0,its:0,know:1,land:0,languag:[1,2],larg:0,least:[0,2],legend:0,let:[0,1],letter:2,level:0,levenhestein:0,librari:0,limit:[0,2],list:0,lose:[],lowercas:2,luca:0,made:2,main:1,maiz:0,make:2,manag:0,mapserv:0,markdown:[],match:[0,2],math:[],mathemat:[],matric:[],method:0,more:0,moreov:[],much:0,must:2,name:2,need:[0,2],neg:0,netherland:0,never:0,niva:0,note:1,now:0,number:[0,2],numpi:2,object:0,offer:[],offici:0,olivi:0,one:[0,2],oneself:[],onli:0,open:1,ordinari:0,org:0,organ:0,orient:0,output:[],panda:2,paramet:2,pass:[],path:2,perman:0,permanent:0,pip:2,place:2,plant:0,pleas:[0,1],polish:0,pomm:0,portuges:0,posit:0,possibl:[],prairi:0,pre:2,precis:0,prepar:1,present:[],pro:0,process:0,product:0,project:0,protect:0,provid:[],pumpkin:0,pure:[],python3:2,python:0,qualifi:0,question:0,quick:[],realiti:0,realli:0,recap:0,refer:0,regard:0,region:[0,2],repres:0,research:0,rest:0,restructuredtext:[],result:0,rice:0,riz:0,role:[],rpg:0,rst:[],run:[0,2],same:[],san:0,save:2,scratch:0,script:[0,2],season:0,second:0,section:0,seem:0,select:0,semant:2,semi:[0,2],servic:0,set:[],share:[0,2],should:2,shpinx:[],sigec_parc_agri_anon__2020:0,similar:[1,2],sometim:0,sourc:[0,1,2],spanish:0,speci:0,specif:0,sphinx:[],spring:0,src:[0,2],start:0,step:1,stick:[0,2],store:[],string:2,studi:0,sucr:0,sum:2,surfac:0,syntax:[],tabl:[0,2],take:0,task:0,team:[],technic:[],temporair:0,temporari:0,tendr:0,terr:0,textual:[],than:0,thei:[0,2],them:0,thi:[0,2],threshold:[0,2],thu:[0,2],time:2,tool:[1,2],tournesol:0,tracker:1,translat:[0,2],type:0,under:0,understand:0,union:0,use:[0,1],used:[],user:1,uses:2,utilis:0,varieti:0,variou:0,vecteur:0,verger:0,veri:0,view:2,vign:0,walloni:0,wallonia:[1,2],want:0,web:[],well:0,wetland:0,what:0,wheat:0,when:[0,2],wherea:[],which:[0,2],why:0,wil:[],winter:0,without:0,word:2,work:2,workflow:1,would:0,write:[],written:[0,2],www:0,yahoo:1,year:2,you:[0,1,2],your:[0,1]},titles:["<span class=\"section-number\">2. </span>Analysis and conception notes","Classificrops\u2019s documentation","<span class=\"section-number\">1. </span>User guide"],titleterms:{analysi:0,choos:2,classif:0,classificrop:1,code:[],comput:0,concept:0,contribut:1,data:2,descript:2,document:1,download:2,european:0,franc:0,guid:2,how:2,input:2,instal:2,issu:2,languag:0,licens:1,main:2,note:0,prepar:2,project:[],side:0,similar:0,spoken:[],step:2,support:1,tool:0,use:2,user:2,wallonia:0,workflow:2,your:2}})[m
\ No newline at end of file[m
[32m+[m[32mSearch.setIndex({docnames:["analysis and conception notes","index","user guide"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":3,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":2,"sphinx.domains.rst":2,"sphinx.domains.std":1,sphinx:56},filenames:["analysis and conception notes.rst","index.rst","user guide.rst"],objects:{},objnames:{},objtypes:{},terms:{"100":2,"143":0,"328":0,"352":0,"378":0,"800":[],"assimil\u00e9":0,"bl\u00e9":0,"c\u00e9r\u00e9ale":0,"case":0,"class":[0,2],"final":[],"fourrag\u00e8r":0,"function":2,"gel\u00e9":0,"l\u00e9gume":0,"l\u00e9gumineus":0,"ma\u00ef":0,"mara\u00eech\u00e8r":0,"ol\u00e9agineux":0,"prot\u00e9agineux":0,"public":1,"true":[],But:0,For:2,The:[0,2],Then:0,There:0,Use:0,a0135:0,a0135e10:0,abil:[],abl:2,account:0,adapt:[],add:[],admit:[],against:0,agricultur:0,all:0,allow:[],alreadi:2,altern:0,among:[],analysi:1,anoth:0,app3:0,approach:0,arcgi:0,argu:[],austria:0,autom:[0,2],autr:0,avail:[0,2],base:2,basic:2,bean:0,belgium:0,bertillet:[1,2],bertilletempl:1,better:[],between:[0,2],botan:0,both:0,bring:0,browser:2,can:2,cann:0,capit:2,central:0,characterist:0,check:[],choos:[0,1],chosen:2,classif:[1,2],classificrop:[0,2],clone:2,code:[1,2],column:2,colza:0,com:[0,1,2],come:[0,2],compar:0,comparison:0,complex:0,comput:[1,2],con:0,concept:1,consequ:2,consid:0,contain:[0,2],convers:2,convert:[0,2],coqu:0,correct:0,could:0,countri:[0,2],cover:0,creat:0,crop:[0,2],cropland:0,crops_fr:2,crossov:0,csv:2,cultiv:0,cultur:0,cycl:0,data:[0,1],deal:0,decid:0,dedic:0,deepl:0,deeplcom:0,defin:0,delta:0,descript:1,differ:0,dioxygen:[],direct:[],distanc:0,distinct:0,diver:0,document:0,doe:0,domain:2,dominiqu:0,done:2,donne:0,download:1,draw:0,dri:0,dryland:0,dutsh:0,dw2_screen:[],dwl2_screen:[],each:0,eagl:0,easi:2,english:2,ensilag:0,eppo:0,equat:[],error:0,estiv:0,europ:0,european:[1,2],even:0,evolut:0,exampl:[0,2],exist:0,expect:2,extend:[],fao:[0,2],fibr:0,first:0,fit:0,flandr:0,flavor:[],fleur:0,focu:0,fodder:0,folder:2,follow:[0,2],food:0,format:2,fourrag:0,fr_2020:2,franc:1,french:0,fresh:0,from:[0,2],fruit:0,fulli:2,further:0,fuzzi:0,gel:0,gener:1,geoservic:0,german:0,germani:0,get:[],git:2,github:[0,1,2],glanc:0,gnu:1,goal:0,googl:0,grain:0,graphic:2,group:0,group_fr:[0,2],group_wl:0,grow:0,grown:0,guid:1,happen:0,has:[],have:[0,1],help:2,horticol:0,how:[0,1],htm:0,http:[0,2],hybrid:0,icc:[0,2],id_:2,id_crops_fr:2,id_group_fr:2,idea:0,ign:0,imag:[],imagin:0,increas:0,inde:0,index:0,indic:[0,2],industri:0,industriel:0,inferior:0,inform:0,input:1,instal:1,instead:0,interest:0,interfac:2,interpret:2,issu:[0,1],italian:0,its:0,know:1,land:0,languag:[1,2],larg:0,least:[0,2],legend:0,let:[0,1],letter:2,level:0,levenhestein:0,librari:0,limit:[0,2],list:0,lose:[],lowercas:2,luca:0,made:2,main:1,maiz:0,make:2,manag:0,mapserv:0,markdown:[],match:[0,2],math:[],mathemat:[],matric:[],method:0,more:0,moreov:[],much:0,must:2,name:2,need:[0,2],neg:0,netherland:0,never:0,niva:0,note:1,now:0,number:[0,2],numpi:2,object:0,offer:[],offici:0,olivi:0,onc:2,one:[0,2],oneself:[],onli:0,open:[],ordinari:0,org:0,organ:0,orient:0,output:[],panda:2,paramet:2,pass:[],path:2,perman:0,permanent:0,pip:2,place:2,plant:0,pleas:[0,1],png:[],polish:0,pomm:0,portuges:0,posit:0,possibl:[],prairi:0,pre:2,precis:0,prepar:1,present:[],pro:0,process:0,product:0,project:0,protect:0,provid:[],pumpkin:0,pure:[],put:2,python3:2,python:0,qualifi:0,question:0,quick:[],realiti:0,realli:0,recap:0,refer:0,regard:0,region:[0,2],repres:0,research:0,rest:0,restructuredtext:[],result:0,rice:0,riz:0,role:[],rpg:0,rst:[],run:[0,1],same:[],san:0,save:2,scratch:0,script:[0,2],season:0,second:0,section:0,seem:0,select:0,semant:2,semi:[0,2],servic:0,set:[],share:[0,2],should:2,shpinx:[],sigec_parc_agri_anon__2020:0,similar:[1,2],sometim:0,soon:2,sourc:[0,1,2],spanish:0,speci:0,specif:0,sphinx:[],spring:0,src:[0,2],start:0,step:1,stick:[0,2],store:[],string:2,studi:0,sucr:0,sum:2,surfac:0,syntax:[],tabl:[0,2],tablenam:2,take:0,task:0,team:[],technic:[],temporair:0,temporari:0,tendr:0,termin:2,terr:0,textual:[],than:0,thei:[0,2],them:0,thi:[0,2],third:2,threshold:[0,2],thu:[0,2],time:2,tool:[1,2],tournesol:0,tracker:1,translat:[0,2],type:0,under:0,understand:0,union:0,updat:2,use:[0,1],used:[],user:1,uses:2,utilis:0,varieti:0,variou:0,vecteur:0,verger:0,veri:0,view:2,vign:0,walloni:0,wallonia:[1,2],want:0,web:[],well:[0,2],wetland:0,what:0,wheat:0,when:[0,2],wherea:[],which:[0,2],why:0,width:[],wil:[],winter:0,without:0,word:2,work:2,workflow:1,would:0,write:[],written:[0,2],www:0,yahoo:1,year:2,you:[0,1,2],your:[0,1]},titles:["<span class=\"section-number\">2. </span>Analysis and conception notes","Classificrops\u2019s documentation","<span class=\"section-number\">1. </span>User guide"],titleterms:{analysi:0,choos:2,classif:0,classificrop:1,code:[],comput:0,concept:0,contribut:1,data:2,descript:2,document:1,download:2,european:0,franc:0,guid:2,how:2,input:2,instal:2,issu:2,languag:0,licens:1,main:2,note:0,prepar:2,project:[],run:2,side:0,similar:0,spoken:[],step:2,support:1,tool:0,use:2,user:2,wallonia:0,workflow:2,your:2}})[m
\ No newline at end of file[m
[1mdiff --git a/docs/build/html/user guide.html b/docs/build/html/user guide.html[m
[1mindex 6326478..9d1810d 100644[m
[1m--- a/docs/build/html/user guide.html[m	
[1m+++ b/docs/build/html/user guide.html[m	
[36m@@ -43,16 +43,19 @@[m [mTo match 2 classes, the tool uses a function that compute similarity between 2 w[m
 Thus, this tool is limited when it comes to match strings that need semantic interpretation.[m
 As a consequence, this tool is not able to automate fully the conversion from a classification to the ICC one, but at least to semi-automate it.[m
 To sum up, Classificrops must be viewed as a helping tool to pre-work the conversion and save the user time by making the easy and basic matching.</p>[m
[32m+[m[32m<blockquote>[m
[32m+[m[32m<div><a class="reference internal image-reference" href="_images/goal.png"><img alt="_images/goal.png" src="_images/goal.png" style="width: 800px;" /></a>[m
[32m+[m[32m</div></blockquote>[m
 </section>[m
 <section id="how-to-use-it-the-workflow">[m
 <h2><span class="section-number">1.2. </span>How to use it : the workflow<a class="headerlink" href="#how-to-use-it-the-workflow" title="Permalink to this headline">¬∂</a></h2>[m
 <ol class="arabic simple">[m
 <li><p><a class="reference internal" href="#prepare-the-data"><span class="std std-ref">Prepare the data</span></a>.</p></li>[m
 <li><p>If not already installed, <a class="reference internal" href="#install"><span class="std std-ref">Install</span></a> python3, numpy, and pandas.</p></li>[m
[31m-<li><p><a class="reference internal" href="#download"><span class="std std-ref">Download</span></a> the source code from Github and add the source classification you are working with in the folder data/country. For example you could download a classification of Wallonia into data/WL.</p></li>[m
[31m-<li><p>Go to the folder src/scripts/classificrops/</p></li>[m
[32m+[m[32m<li><p><a class="reference internal" href="#download"><span class="std std-ref">Download</span></a> the source code from Github.</p></li>[m
[32m+[m[32m<li><p><a class="reference internal" href="#go-to"><span class="std std-ref">Go to</span></a> the folder src/scripts/classificrops/</p></li>[m
 <li><p><a class="reference internal" href="#choose-your-inputs"><span class="std std-ref">Choose your inputs</span></a>.</p></li>[m
[31m-<li><p>Run the script converter.py with the source classification path and the inputs chosen in parameters.</p></li>[m
[32m+[m[32m<li><p><a class="reference internal" href="#run"><span class="std std-ref">Run</span></a> the script converter.py with the source classification path and the inputs chosen in parameters.</p></li>[m
 </ol>[m
 </section>[m
 <section id="step-by-step">[m
[36m@@ -63,29 +66,46 @@[m [mTo sum up, Classificrops must be viewed as a helping tool to pre-work the conver[m
 <dt>The source classification table should stick to the the following expectations :</dt><dd><ul class="simple">[m
 <li><p>format : csv</p></li>[m
 <li><p>table name : place+‚Äô_‚Äô+year+‚Äô.csv‚Äô ‚Äì&gt; example : FR_2020.csv</p></li>[m
[31m-<li><p>column name : class+‚Äô_‚Äô+language        or        ‚Äò<a href="#id5"><span class="problematic" id="id6">ID_</span></a>‚Äô+class+‚Äô_‚Äô+language ‚Äì&gt; example : GROUP_fr, CROPS_fr or ID_GROUP_FR, ID_CROPS_fr</p></li>[m
[31m-<li><p>column name should be written in english.</p></li>[m
[32m+[m[32m<li><p>column name : class+‚Äô_‚Äô+language        or        ‚Äò<a href="#id7"><span class="problematic" id="id8">ID_</span></a>‚Äô+class+‚Äô_‚Äô+language ‚Äì&gt; example : GROUP_fr, CROPS_fr or ID_GROUP_fr, ID_CROPS_fr</p></li>[m
[32m+[m[32m<li><p>column name should be written in english (this will be updated soon)</p></li>[m
[32m+[m[32m<li><p>Once the third step done (download classificrops code available on Github), the source classification well formatted should be put into the folder data/country. For example, if you are working with a crops classification of Wallonia, you can put it into data/WL.</p></li>[m
 </ul>[m
 </dd>[m
 </dl>[m
 </section>[m
 <section id="install">[m
 <span id="id2"></span><h3><span class="section-number">1.3.2. </span>Install<a class="headerlink" href="#install" title="Permalink to this headline">¬∂</a></h3>[m
[31m-<p>pip install python3[m
[31m-pip install numpy[m
[31m-pip install pandas</p>[m
[32m+[m[32m<p>From your terminal :[m
[32m+[m[32m<code class="docutils literal notranslate"><span class="pre">pip</span> <span class="pre">install</span> <span class="pre">python3</span></code>[m
[32m+[m[32m<code class="docutils literal notranslate"><span class="pre">pip</span> <span class="pre">install</span> <span class="pre">numpy</span></code>[m
[32m+[m[32m<code class="docutils literal notranslate"><span class="pre">pip</span> <span class="pre">install</span> <span class="pre">pandas</span></code></p>[m
 </section>[m
 <section id="download">[m
 <span id="id3"></span><h3><span class="section-number">1.3.3. </span>Download<a class="headerlink" href="#download" title="Permalink to this headline">¬∂</a></h3>[m
[31m-<p>git clone <a class="reference external" href="https://github.com/BertilleT/Classificrops">https://github.com/BertilleT/Classificrops</a></p>[m
[32m+[m[32m<blockquote>[m
[32m+[m[32m<div><ul class="simple">[m
[32m+[m[32m<li><p>From your terminal : <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span> <span class="pre">https://github.com/BertilleT/Classificrops</span></code></p></li>[m
[32m+[m[32m<li><p>Or from your browser :</p></li>[m
[32m+[m[32m</ul>[m
[32m+[m[32m<a class="reference internal image-reference" href="_images/dwl2_screen.png"><img alt="_images/dwl2_screen.png" src="_images/dwl2_screen.png" style="width: 800px;" /></a>[m
[32m+[m[32m</div></blockquote>[m
[32m+[m[32m</section>[m
[32m+[m[32m<section id="go-to">[m
[32m+[m[32m<span id="id4"></span><h3><span class="section-number">1.3.4. </span>Go to<a class="headerlink" href="#go-to" title="Permalink to this headline">¬∂</a></h3>[m
[32m+[m[32m<blockquote>[m
[32m+[m[32m<div><ul class="simple">[m
[32m+[m[32m<li><p>From your terminal : <code class="docutils literal notranslate"><span class="pre">cd</span> <span class="pre">src/scripts/classificrops/</span></code></p></li>[m
[32m+[m[32m<li><p>Or : from your graphic interface.</p></li>[m
[32m+[m[32m</ul>[m
[32m+[m[32m</div></blockquote>[m
 </section>[m
 <section id="choose-your-inputs">[m
[31m-<span id="id4"></span><h3><span class="section-number">1.3.4. </span>Choose your inputs<a class="headerlink" href="#choose-your-inputs" title="Permalink to this headline">¬∂</a></h3>[m
[32m+[m[32m<span id="id5"></span><h3><span class="section-number">1.3.5. </span>Choose your inputs<a class="headerlink" href="#choose-your-inputs" title="Permalink to this headline">¬∂</a></h3>[m
 <table class="docutils align-default">[m
 <colgroup>[m
[31m-<col style="width: 37%" />[m
[31m-<col style="width: 37%" />[m
[31m-<col style="width: 26%" />[m
[32m+[m[32m<col style="width: 31%" />[m
[32m+[m[32m<col style="width: 47%" />[m
[32m+[m[32m<col style="width: 22%" />[m
 </colgroup>[m
 <thead>[m
 <tr class="row-odd"><th class="head"><p>name input</p></th>[m
[36m@@ -94,21 +114,29 @@[m [mpip install pandas</p>[m
 </tr>[m
 </thead>[m
 <tbody>[m
[31m-<tr class="row-even"><td><p>language</p></td>[m
[32m+[m[32m<tr class="row-even"><td><p>path</p></td>[m
[32m+[m[32m<td><p>‚Äòdata/‚Äô + place + ‚Äò/‚Äô + tablename</p></td>[m
[32m+[m[32m<td></td>[m
[32m+[m[32m</tr>[m
[32m+[m[32m<tr class="row-odd"><td><p>language</p></td>[m
 <td><p>2 lowercase letters</p></td>[m
 <td><p>[en,fr,it,‚Ä¶]</p></td>[m
 </tr>[m
[31m-<tr class="row-odd"><td><p>place</p></td>[m
[32m+[m[32m<tr class="row-even"><td><p>place</p></td>[m
 <td><p>2 capitalized letters</p></td>[m
 <td><p>[WL,CT,FR,IT]</p></td>[m
 </tr>[m
[31m-<tr class="row-even"><td><p>threshold</p></td>[m
[32m+[m[32m<tr class="row-odd"><td><p>threshold</p></td>[m
 <td><p>a number</p></td>[m
 <td><p>[0,100]</p></td>[m
 </tr>[m
 </tbody>[m
 </table>[m
 </section>[m
[32m+[m[32m<section id="run">[m
[32m+[m[32m<span id="id6"></span><h3><span class="section-number">1.3.6. </span>Run<a class="headerlink" href="#run" title="Permalink to this headline">¬∂</a></h3>[m
[32m+[m[32m<p><code class="docutils literal notranslate"><span class="pre">python3</span> <span class="pre">converter.py</span> <span class="pre">path</span> <span class="pre">language</span> <span class="pre">place</span> <span class="pre">threshold</span></code></p>[m
[32m+[m[32m</section>[m
 </section>[m
 <section id="main-issues">[m
 <h2><span class="section-number">1.4. </span>Main issues<a class="headerlink" href="#main-issues" title="Permalink to this headline">¬∂</a></h2>[m
[36m@@ -147,7 +175,9 @@[m [mpip install pandas</p>[m
 <li class="toctree-l3"><a class="reference internal" href="#prepare-the-data">1.3.1. Prepare the data</a></li>[m
 <li class="toctree-l3"><a class="reference internal" href="#install">1.3.2. Install</a></li>[m
 <li class="toctree-l3"><a class="reference internal" href="#download">1.3.3. Download</a></li>[m
[31m-<li class="toctree-l3"><a class="reference internal" href="#choose-your-inputs">1.3.4. Choose your inputs</a></li>[m
[32m+[m[32m<li class="toctree-l3"><a class="reference internal" href="#go-to">1.3.4. Go to</a></li>[m
[32m+[m[32m<li class="toctree-l3"><a class="reference internal" href="#choose-your-inputs">1.3.5. Choose your inputs</a></li>[m
[32m+[m[32m<li class="toctree-l3"><a class="reference internal" href="#run">1.3.6. Run</a></li>[m
 </ul>[m
 </li>[m
 <li class="toctree-l2"><a class="reference internal" href="#main-issues">1.4. Main issues</a></li>[m
[1mdiff --git a/docs/images/.~lock.goal.png.odg# b/docs/images/.~lock.goal.png.odg#[m
[1mdeleted file mode 100644[m
[1mindex fb836c4..0000000[m
[1m--- a/docs/images/.~lock.goal.png.odg#[m
[1m+++ /dev/null[m
[36m@@ -1 +0,0 @@[m
[31m-,BTemple-Boyer-Dury,DEL1711P013,05.05.2022 09:52,file:///home/BTemple-Boyer-Dury/.config/libreoffice/4;[m
\ No newline at end of file[m
[1mdiff --git a/docs/images/dwl2_screen.pdf b/docs/images/dwl2_screen.pdf[m
[1mnew file mode 100644[m
[1mindex 0000000..a5f7cd2[m
Binary files /dev/null and b/docs/images/dwl2_screen.pdf differ
[1mdiff --git a/docs/images/dwl2_screen.png b/docs/images/dwl2_screen.png[m
[1mnew file mode 100644[m
[1mindex 0000000..be4fb3b[m
Binary files /dev/null and b/docs/images/dwl2_screen.png differ
[1mdiff --git a/docs/images/github2_screen.png b/docs/images/github2_screen.png[m
[1mdeleted file mode 100644[m
[1mindex fb4290c..0000000[m
Binary files a/docs/images/github2_screen.png and /dev/null differ
[1mdiff --git a/docs/images/goal (copie).odg b/docs/images/goal (copie).odg[m
[1mnew file mode 100644[m
[1mindex 0000000..5aedf07[m
Binary files /dev/null and b/docs/images/goal (copie).odg differ
[1mdiff --git a/docs/images/goal.odg b/docs/images/goal.odg[m
[1mindex d214be7..5aedf07 100644[m
Binary files a/docs/images/goal.odg and b/docs/images/goal.odg differ
[1mdiff --git a/docs/images/goal.png.pdf b/docs/images/goal.pdf[m
[1msimilarity index 100%[m
[1mrename from docs/images/goal.png.pdf[m
[1mrename to docs/images/goal.pdf[m
[1mdiff --git a/docs/images/goal.png b/docs/images/goal.png[m
[1mnew file mode 100644[m
[1mindex 0000000..61e704f[m
Binary files /dev/null and b/docs/images/goal.png differ
[1mdiff --git a/docs/source/index.rst b/docs/source/index.rst[m
[1mindex a0b5182..f26c7de 100644[m
[1m--- a/docs/source/index.rst[m
[1m+++ b/docs/source/index.rst[m
[36m@@ -27,4 +27,4 @@[m [mIf you are having issues, please let me know at bertilletemple@yahoo.fr[m
 License[m
 -------[m
 [m
[31m-Open source. [m
\ No newline at end of file[m
[32m+[m[32mGNU General Public License v3.0[m
\ No newline at end of file[m
[1mdiff --git a/docs/source/user guide.rst b/docs/source/user guide.rst[m
[1mindex 6cdc4f1..30e1363 100644[m
[1m--- a/docs/source/user guide.rst[m	
[1m+++ b/docs/source/user guide.rst[m	
[36m@@ -7,15 +7,17 @@[m [mTo match 2 classes, the tool uses a function that compute similarity between 2 w[m
 Thus, this tool is limited when it comes to match strings that need semantic interpretation. [m
 As a consequence, this tool is not able to automate fully the conversion from a classification to the ICC one, but at least to semi-automate it. [m
 To sum up, Classificrops must be viewed as a helping tool to pre-work the conversion and save the user time by making the easy and basic matching. [m
[32m+[m[32m    .. image:: ../images/goal.png[m
[32m+[m[32m      :width: 800[m
 [m
 How to use it : the workflow[m
 -----------------------------[m
 #. :ref:`Prepare the data`.[m
 #. If not already installed, :ref:`install` python3, numpy, and pandas.  [m
[31m-#. :ref:`Download` the source code from Github and add the source classification you are working with in the folder data/country. For example you could download a classification of Wallonia into data/WL. [m
[31m-#. Go to the folder src/scripts/classificrops/ [m
[32m+[m[32m#. :ref:`Download` the source code from Github.[m
[32m+[m[32m#. :ref:`Go to` the folder src/scripts/classificrops/[m[41m [m
 #. :ref:`Choose your inputs`. [m
[31m-#. Run the script converter.py with the source classification path and the inputs chosen in parameters. [m
[32m+[m[32m#. :ref:`Run` the script converter.py with the source classification path and the inputs chosen in parameters.[m[41m [m
 [m
 Step by step[m
 -------------[m
[36m@@ -26,36 +28,56 @@[m [mPrepare the data[m
 The source classification table should stick to the the following expectations : [m
     - format : csv[m
     - table name : place+'_'+year+'.csv' --> example : FR_2020.csv[m
[31m-    - column name : class+'_'+language        or        'ID_'+class+'_'+language --> example : GROUP_fr, CROPS_fr or ID_GROUP_FR, ID_CROPS_fr[m
[31m-    - column name should be written in english. [m
[32m+[m[32m    - column name : class+'_'+language        or        'ID_'+class+'_'+language --> example : GROUP_fr, CROPS_fr or ID_GROUP_fr, ID_CROPS_fr[m
[32m+[m[32m    - column name should be written in english (this will be updated soon)[m
[32m+[m[32m    - Once the third step done (download classificrops code available on Github), the source classification well formatted should be put into the folder data/country. For example, if you are working with a crops classification of Wallonia, you can put it into data/WL.[m[41m [m
 [m
 .. _install:[m
 [m
 Install[m
 ~~~~~~~~~[m
[31m-pip install python3[m
[31m-pip install numpy[m
[31m-pip install pandas[m
[32m+[m[32mFrom your terminal :[m[41m [m
[32m+[m[32m``pip install python3``[m[41m  [m
[32m+[m[32m``pip install numpy``[m[41m  [m
[32m+[m[32m``pip install pandas``[m[41m  [m
 [m
 .. _Download:[m
 [m
 Download[m
 ~~~~~~~~~[m
[31m-git clone https://github.com/BertilleT/Classificrops[m
[32m+[m[32m    - From your terminal : ``git clone https://github.com/BertilleT/Classificrops``[m
[32m+[m[32m    - Or from your browser :[m[41m [m
[32m+[m[32m    .. image:: ../images/dwl2_screen.png[m
[32m+[m[32m      :width: 800[m
[32m+[m
[32m+[m[32m.. _Go to:[m
[32m+[m
[32m+[m[32mGo to[m[41m [m
[32m+[m[32m~~~~~~[m
[32m+[m[32m    - From your terminal : ``cd src/scripts/classificrops/``[m
[32m+[m[32m    - Or : from your graphic interface.[m
 [m
 .. _Choose your inputs:[m
 [m
 Choose your inputs[m
 ~~~~~~~~~~~~~~~~~~[m
[31m-+-----------------------+-----------------------+----------------+[m
[31m-| name input            | format                | domain         |[m
[31m-+=======================+=======================+================+[m
[31m-| language              | 2 lowercase letters   | [en,fr,it,...] |[m
[31m-+-----------------------+-----------------------+----------------+[m
[31m-| place                 | 2 capitalized letters | [WL,CT,FR,IT]  |[m
[31m-+-----------------------+-----------------------+----------------+[m
[31m-| threshold             | a number              | [0,100]        |[m
[31m-+-----------------------+-----------------------+----------------+[m
[32m+[m[32m+-----------------------+-----------------------------------+----------------+[m
[32m+[m[32m| name input            | format                            | domain         |[m
[32m+[m[32m+=======================+===================================+================+[m
[32m+[m[32m| path                  | 'data/' + place + '/' + tablename |                |[m
[32m+[m[32m+-----------------------+-----------------------------------+----------------+[m
[32m+[m[32m| language              | 2 lowercase letters               | [en,fr,it,...] |[m
[32m+[m[32m+-----------------------+-----------------------------------+----------------+[m
[32m+[m[32m| place                 | 2 capitalized letters             | [WL,CT,FR,IT]  |[m
[32m+[m[32m+-----------------------+-----------------------------------+----------------+[m
[32m+[m[32m| threshold             | a number                          | [0,100]        |[m
[32m+[m[32m+-----------------------+-----------------------------------+----------------+[m
[32m+[m
[32m+[m[32m.. _Run:[m
[32m+[m
[32m+[m[32mRun[m[41m [m
[32m+[m[32m~~~[m
[32m+[m[32m``python3 converter.py path language place threshold``[m
 [m
 Main issues[m
 ------------[m
