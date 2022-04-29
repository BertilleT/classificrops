import pandas as pd
import numpy as np
#this script is dedicated to write the converter script with an object oriented approach. 
#The code will be more easily adaptable,modulable and understable. 

filtersDict = {EN:['other','crops',' and ',' or ','n.e.c.', 'spp','n.e.c'],FR:['autres','autre',' et ',' ou '],IT:[]}
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
class Classification:
    def __init__(self,pathCsv,lg):
        self.path = pathCsv
        self.language = lg
        self.df = pd.read_csv(self.pathCsv)
        self.side = ''
        self.filters = filtersDict[lg]
        self.fromOrTo()
    
    def fromOrTo(self):
        if 'ICC' in self.path:
            self.side = 'target'
            ICCClassification(self) 
        else
            self.side = 'source'
            SrcClassification(self) 

    def filter(self,col):
        mydict = {f'(?i){word}':'' for word in self.filters} 
        self.df[col+'_filtered'] = self.df[col].replace(mydict, regex=True)
        self.df[col+'_filtered'] = self.df[col+'_filtered'].str.replace(r'[^\w\s]+', '', regex=True)
        self.df[col+'_filtered'] = self.df[col+'_filtered'].str.replace('   ', ' ')
        self.df[col+'_filtered'] = self.df[col+'_filtered'].str.replace('  ', ' ')
        self.df[col+'_filtered'] = self.df[col+'_filtered'].str.strip()
        self.df.replace('',np.nan,regex = True,inplace=True)

#---------------------------------------------------------------------------------
class SrcClassification(Classification):
    def __init__(pathCsv,lg):
        super(SrcClassification,self).__init__(pathCsv,lg))
        self.classes = []
        src_classes(self)
        for c in src_classes:
            self.filter(c)
            Class(self,c.index,c)
        
        match()

    def src_classes(self):
        columns = list(self.df)
        for c in columns:
            if 'ID' not in c: 
                self.classes.append(c)
    
    def scan(self):
        for c in self.src_classes:
            c = Class(SrcClassification)

#---------------------------------------------------------------------------------
class ICCClassification(Classification):
    def __init__(pathCsv,lg):
        super(ICCClassification,self).__init__(pathCsv,lg))
        self.filter('label_en')
        self.df.to_csv('../../../data/ICC/ICC.csv', index=False)        
        self.icc_translate()
        self.df.to_csv('../../../data/ICC/ICC.csv', index=False)  
        self.icc_code_format()      

    def icc_translate(self):
        if 'label_'+self.lg.lower()+'_filtered' not in list(self.df.columns):
            DEEPL_AUTH_KEY="47c6c989-9eaa-5b30-4ee6-b2e4f1ebd530:fx"
            translator = deepl.Translator(DEEPL_AUTH_KEY)
            self.df['label_'+lg.lower()+'_filtered'] = self.df['label_en_filtered'].apply(lambda crop: translator.translate_text(crop, target_lang=self.language) if (pd.notna(crop)) else crop)

    def icc_code_format(self):    
        self.df['code'] = self.df['code'].apply(lambda code: "".join(x.split('.')))
        self.df['code'] = self.df['code'].astype('int')
        self.df['group_code'] = self.df['code'].astype('str').str[:1].astype('int')

#---------------------------------------------------------------------------------
class Class(SrcClassification):
    def __init__(pathCsv,lg,level,class_level):
        super(Class,self).__init__(pathCsv,lg))
        self.level = level
        self.class_level = class_level
        self.class_distinct = pd.Dataframe()
        drop_duplicates(class_level)

    def drop_duplicates(self,c):
        self.class_distinct = self.df.drop_duplicates(subset = ['ID_' + c + '_filtered'])
    
    def match(self):
        self.class_distinct.apply(matching)
        

class MatchData():
    def __init__():
        self.class_level = 
        self.id_src =
        self.words_src = 
        self.words_trg = 
        self.id_trg = 
        self.similarity = 

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
def converter(path,lg):
    src = SrcClassification(path,lg)
    icc = ICCClassification('../../../../data/ICC/ICC.csv',lg)
    ##Initializing
    resultDf = src.df[['ID_CROPS_FR', 'ID_GROUP_FR']]
    ##Matching all
    matchingDf = matchDf(src.df,icc.df,threshold)
    for c in classes:
        result = merge matchDf + select max
    spreadResult
    incDepth
    spreadResult
    incDepth 
    etc ... 

converter('../../../../data/FR/FR_2020.csv', 'FR')

