import TwoCentroids
import Tetrahedral_hlgy_link
import json



All=[]

for M in Tetrahedral_hlgy_link.K_hlgy_lk:
    for i in Tetrahedral_hlgy_link.Cusp_list(M):
        All.append((M,i))# All contains all (M,i) such that
# M is in K_hlgy_lk and i in Cusp_list(M) 

print('The total numbr of cases that we check: ')
print(len(All))
print(' ')
Nice_link=[]
Excep_link=[]

for M in Tetrahedral_hlgy_link.K_hlgy_lk:
    for i in Tetrahedral_hlgy_link.Cusp_list(M):
        if TwoCentroids.Free_rot_strng(M,i)==True:
            Excep_link.append((Tetrahedral_hlgy_link.K_hlgy_lk.index(M),M.name(),i,M.triangulation_isosig(decorated=False)))
        else:
            Nice_link.append((Tetrahedral_hlgy_link.K_hlgy_lk.index(M),M.name(),i,M.triangulation_isosig(decorated=False)))
# Excep_link contains (index, manifold, cusp number, default isomorphism signature) where (manifold, cusp) belongs to \mathcal{E}
# Nice_link contains (index, manifold, cusp number, default isomorphism signature) where (manifold, cusp) belongs to \mathcal{N}
            
print("Exceptional tuples (i.e. those corresponding to \mathcal{E} are: ")
print(Excep_link)
print(' ')
print("Nice tuples (i.e. those corresponding to \mathcal{N} are: ")
print(Nice_link)
print(' ')

with open("Excep_tuple.json", "w+") as exceptuple:
    json.dump(Excep_link, exceptuple) # export list Excep_link as "Excep_tuple.json" file
