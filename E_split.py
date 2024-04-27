import json


with open("Excep_tuple.json", "r+") as Etuple:
    E=json.load(Etuple)
# Imports the list E_tuple whose elements are
# (index in K_hlgy_lk, manifold name, cusp number, default isomorphism signature) so that
# (manifold, cusp number) is in \mathcal{E}. 


with open("E_good_cover.json", "r+") as Egoodcover:
    E_good_cover=json.load(Egoodcover)
# Imports the list E_good_cover whose elements are
# (index in K_hlgy_lk, manifold name, cusp number, default isomorphism signature) so that
# (manifold, cusp number) is in \mathcal{E}_{good cover}. 



with open("E_single.json", "r+") as Esingle:
    E_single=json.load(Esingle)
# Imports the list E_single whose elements are
# (index, cusp number) so that
# (K_hlgy_lk[index], cusp number) is in \mathcal{E}_{single}



E1=[]
E4=[]
E2E3=[]


for x in E_good_cover:
    for y in E_single:
        if x[0]==y[0]:
            E1.append(x[:4])
            # E1 contains all (index, manifold name, cusp number) so that (manifold, cusp number) is in \mathcal{E}_1
            # index here is index in K_hlgy_lk. 
        else:
            E4.append(x[:4])
            # E4 contains all (index, manifold name, cusp number) so that (manifold, cusp number) is in \mathcal{E}_4
            # index here is index in K_hlgy_lk.

for x in E:
    if x not in E_good_cover:
        E2E3.append(x[:4])
        # E2E3 contains all (index, manifold name, cusp number) so that (manifold, cusp number) is in union of
        #\mathcal{E}_2 and \mathcal{E}_3. Index here is index in K_hlgy_lk.

print('The members of E_1 are: ', E1)
print(' ')


print('The members of E_4 are: ', E4)
print(' ')


print('The members of E_2 and E_3 are" ', E2E3)
print(' ')


