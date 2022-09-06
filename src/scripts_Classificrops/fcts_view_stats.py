def let_user_pick(options):
    return my_list

def autopct(pct): # only show the label when it's > 10%
    return ('%.2f' % pct) if pct > 5 else ''

def create_keys(my_array):
    return my_keys

def view_stats(path_regions_outline, path_dep_outline, path_prov_outline, path_Occ_crops, path_Cat_crops):
    ##download outlines
    #OCCITANIA
    #CATALONIA

    ##download crops
    #OCCITANIA
    #CATALONIA

    ##download the ICC classification, to be shared by the 2 areas under study
    ##define the areas that can selected and ask the user to choose
    for dep in deps:
        if dep in dep_Occ: 
            #convert to Icc, computes percentages
            list_resulting_per.append(percentages_icc)

        if dep in prov_Cat:
            #convert to Icc, computes percentages
            list_resulting_per.append(percentages_icc)
        
    return fig