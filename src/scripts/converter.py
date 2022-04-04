#we suppose that JECAM is already translated into e language. 
levels = [TYPE, GROUP, CROP, SUB-CROP, SUB-SUB-CROP]
#goal : to associate french crop into a JECAM group
def converter(table_path, country): 
    open table_path
    open JECAM_ue:
    g = 'GROUP_'+country
    c = 'CROP_'+country
    sc = 'SUB-CROP_'+country
    ssc = 'SUB-SUB-CROP_'+country

    for c in table_path.CROP:
        for word in c:
            i == 1
            if key_JECAM_group(country, i, w) != NULL
                return key_JECAM_group(country, i, w)
            else 
                return key_JECAM_group(country, i+1, w)



def key_JECAM_group(c, i, w): 
    t = levels[i]+'_'+c
    result = c.execute('select distinct GROUP_ID FROM JECAM_UE WHERE w in t', t)
    return result

result = select distinct group_id from jecam where crop in group_lg
if result is null
    result = select distinct group_id from jecam where crop in crop_lg