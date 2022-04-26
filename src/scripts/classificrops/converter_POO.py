#to avoid too many global variables, this script is dedicated to write the script with an object oriented approach. 
#The code will be more easily "adaptable/modulable" and understable. 
#pseudo-code.

class Classification:
    #constructor
    def __init__(self,pathCsv,lg):
        self.path = pathCsv
        self.language = lg
        self.df = downloading(self)
        self.classes = listing(self)

    def downloading(self):
        return pd.read_csv(self.path)
        
#listing works for src file french. But not for ICC target file.
    def listing(self):
        classes = []
        columns = list(self.df)
        for col in columns:
            if 'ID' not in col: 
                classes.append(col)
        return classes

    def selectingLevel(self,level,origin):
        return = CropClass(self,level,origin)
    
''' class Classification:   
    attributes: 
        df:
        classes:
        language:
    constructor:
        downloading()
        listing()
    methods:
        selectingLevel() --> call the constructor of cropClass'''

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
        sim #similarity