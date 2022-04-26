import pandas as pd
import numpy as np
#to avoid too many global variables, this script is dedicated to write the script with an object oriented approach. 
#The code will be more easily "adaptable/modulable" and understable. 
#pseudo-code.

filtersDict = {EN:['other','crops',' and ',' or ','n.e.c.', 'spp','n.e.c'],FR:['autres','autre',' et ',' ou '],IT:[]}

#---------------------------------------------------------------------------------
class Classification:
    def __init__(self,pathCsv,lg):
        self.path = pathCsv
        self.language = lg
        self.df = pd.read_csv(self.pathCsv)
        self.fromOrTo()
        self.filters = filtersDict[lg]
    
    def fromOrTo(self):
        if 'ICC' in self.path:
            self.side = 'target'
        else
            self.side = 'source'

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
    def __init__():
        super(SrcClassification,self).__init__(pathCsv,lg))
        src_classes(self)

    def src_classes(self):
        classes=[]
        columns = list(self.df)
        for c in columns:
            if 'ID' not in c: 
                classes.append(c)
        self.classes = classes

#---------------------------------------------------------------------------------
class ICCClassification(Classification):
    def __init__():
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
class Match():
    pass
    '''code_src
    code_trg
    level_src
    level_trg
    similarity'''

def converter(path,lg):
    src = SrcClassification(path,lg)
    icc = ICCClassification('../../../../data/ICC/ICC.csv',lg)
    ##Initializing
    resultDf = src.df[['ID_CROPS_FR', 'ID_GROUP_FR']]
    ##Matching all
    matchingDf = matchDf(src.df,icc.df,threshold)
    ##Spreading
    rows = matchingDf.loc[matchingDf['class_level_src'] == 'GROUP_FR']
    rows.apply(lambda x: spreadMatch(x.id_src, x.id_trg), axis=1)
    ##Incrementing depth   
    resultDf['similarity'] = resultDf.apply(lambda x : spreadSim(x.ID_CROPS_FR),axis = 1)
    resultDf['ID_GROUP_ICC'] = resultDf.apply(lambda x: incDepth(x), axis=1)
    #Writting result
    resultDf.to_csv('../../../data/FR/conversionTable_FR_scriptMade.csv', index=False)
    matchingDf.to_csv('../../../data/FR/matchingDf_FR_scriptMade.csv', index=False)
    resultDf['ID_GROUP_ICC'] = resultDf.loc[:, ['ID_GROUP_ICC']].astype(float)
    compareList.append(compare('../../../data/FR/conversionTable_FR_handMade.csv',resultDf,threshold))

converter('../../../../data/FR/FR_2020.csv', 'FR')

''' class Classification:   
    attributes: 
        df:
        classes:
        language:
    constructor:
        downloading()
        listing()
    methods:
        selectingLevel() --> call the constructor of cropClass

class CropClass: 
    attributes:
        origin:src/trg
        level:
        dictionnary: {crop_id:crop_name}
        matchingList:
    constructor:
        filtering()
        translating()
    methods:
        formating() #do it for ICC crop_id
        matching()
    
class Match:
    attributes:
        code_src
        code_trg
        level_src
        level_trg
        sim #similarity'''