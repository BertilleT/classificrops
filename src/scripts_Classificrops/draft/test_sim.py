#test sim_method == 'split+ratio+symetric':
from fuzzywuzzy import fuzz
import pandas as pd
from difflib import SequenceMatcher

'''def lcs_len3(Seq1 , Seq2):
    #Compute the LCS len 2 sequences
    
    #Do not calculate the matrix and try to be as efficient as possible 
    #in storing only the minimal ammount of elelment in memory, mainly the previous
    #matrix row + 1 element.
    LL1 = len(Seq1)+1
    LL2 = len(Seq2)+1

    ## we will do the big loop over the longest sequence (L1)
    ## and store the previous row of the matrix (L2+1)
    if LL2 > LL1 : 
        Seq2, Seq1 = Seq1, Seq2
        LL2, LL1 = LL1, LL2

    
    previousrow = [0]*(LL2)
    cindex = 0

    for Seq1ii in Seq1:
        for jj in range(1,LL2):
            cindex = (cindex+1) % LL2

            if Seq1ii == Seq2[jj-1]:
                if jj == 1:
                    previousrow[cindex] = 1
                else :
                    previousrow[cindex]+=1
            if Seq1ii != Seq2[jj-1] :
                up = previousrow[(cindex+1) % LL2]
                
                if jj != 1 :
                    left = previousrow[(cindex-1) % LL2]
                    if left > up :
                        previousrow[cindex] = left
                        continue    
                previousrow[cindex] = up


    return previousrow[cindex]'''



src='fourrage'
trg='graminés et autres cultures fourragères'

#difflib
'''s = SequenceMatcher(None,
                     src,
                     trg, autojunk=False)

print(round(s.ratio(), 2))
print(fuzz.token_set_ratio(src,trg))


s = SequenceMatcher(None,
                     trg,
                     src, autojunk=False)

print(round(s.ratio(), 2))
print(fuzz.ratio(trg,src))'''
#for block in s.get_matching_blocks():
#    print("a[%d] and b[%d] match for %d elements" % block)

#print(2*lcs_len3(src, trg)/(len(src)+len(trg)))







#src = input("what is the first word you want to match ? ")
#trg = input("what is the second word you want to match ? ")

#trg='céréales et graminés'
#src='graminé'

#similarities = ['ratio', 'partial_ratio', 'token_sort_ratio', 'token_set_ratio']
similarities = {}
similarities['ratio'] = fuzz.ratio(src,trg)
similarities['partial_ratio'] = fuzz.partial_ratio(src, trg)
similarities['token_sort_ratio'] = fuzz.token_sort_ratio(src, trg)
similarities['token_set_ratio'] = fuzz.token_set_ratio(src, trg)

for k,v in similarities.items() : 
    print("Similarity score computed with : "+k+" similarity method = "+str(v))




'''nb = 0
src_l = src.split()
len_src = len(src_l)
trg_l = trg.split()
myList=[]
for w in src_l:
    for x in trg_l:
        myList.append([src_l.index(w),fuzz.ratio(w,x)])
cols = ['index', 'sim']
print(myList)
myDf = pd.DataFrame(myList, columns=cols)
r = myDf.groupby('index')['sim'].max().reset_index()
print(r.head())

##if len(trg_l) == 1 :
    #ranger r par ordre de similarité décroissante 
    sorted_r = r.sort_values(["sim"], ascending=False)
    #selectionner premier element de r
    nb = sorted_r.iloc[0,1]
else : ##
total = r['sim'].sum()
nb = total / len_src

print(nb)'''