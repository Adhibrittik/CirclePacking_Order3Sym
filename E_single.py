import json


with open("Excep_tuple.json", "r+") as excep:
    E=json.load(excep)# import the file "Excep_tuple.json" as list E

def All_excep_cusp(j):
    '''returns the list of all cusps c such that
    (K_hlgy_lk[j],c) is in \mathcal{E}'''

    Exceptional_cusp=[]
    for x in E:
        if j==x[0]:
            Exceptional_cusp.append(x[2])

    return Exceptional_cusp


            
E_indices=set()

for x in E:
    E_indices.add(x[0])
# E_indices contains indices in K_hlgy_lk of all M such that (M,c)
# is in \mathcal{E} 



E_single=[]
for j in E_indices:
    if len(All_excep_cusp(j))==1:
        E_single.append((j,All_excep_cusp(j)[0]))
# (j,c) is in E_single iff c is the only cusp such that (K_hlgy_lk[j],c) is in \mathcal{E} 



with open("E_single.json", "w+") as Esingle:
    json.dump(E_single, Esingle) # export list E_single as the "E_single.json" file 
    
