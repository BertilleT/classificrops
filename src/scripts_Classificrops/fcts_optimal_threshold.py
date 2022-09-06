import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from converter import * 


def compare(handmade,computed,threshold, place):
    per = round((match*100)/tot)
    err = round((error*100)/tot)
    print('The conversion table computed with the threshold = ' + str(threshold) + ', fits to the expected output at ' + str(per) + '%.')
    print('The conversion script made '+str(err)+'%'+' of errors.')
    return (threshold, per, err)

def optimal_threshold(src_path_input, place, lg,sim_method, handmade_path): 
    compare_list = []
    thresholds =[]
    num = 1
    for t in thresholds:
        computed = converter(src_path_input, place, lg, t, sim_method, src_formatted, icc_formatted, 'test')[2]
        compare_list.append(compare(handmade,computed,t, place))

    plt.show()