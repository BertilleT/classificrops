#to avoid too many globa variables, this script is dedicated to write the script with n object oriented approach. 
#The code will be more easily "adaptable/modulable" and understable. 
#pseudo-code.

class classification:
    attributes: 
        classes:
        language:
    constructor:
        downloading()
        listing()
    methods:
        selectingLevel() --> call the constructor of cropClass

class cropClass: 
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
    
class match:
    attributes:
        code_src
        code_trg
        level_src
        level_trg
        sim #similarity