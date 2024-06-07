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



E1_prime=[]
E4_prime=[]
E2E3_prime=[]
E1_prime_4tuple=[]

for x in E_good_cover:
    for y in E_single:
        if x[0]==y[0]:
            E1_prime_4tuple.append(x)
            E1_prime.append(tuple(x[:4]))
            # E1_prime contains all (index, manifold name, cusp number) so that (manifold, cusp number) is in \mathcal{E}'_1
            # index here is index in K_hlgy_lk. 
for x in E_good_cover:
    r=True
    for y in E1_prime_4tuple:
        if x[0]==y[0]:
            r=False
            break
    if r==True:
        E4_prime.append(tuple(x[:4]))
            # E4_prime contains all (index, manifold name, cusp number) so that (manifold, cusp number) is in \mathcal{E}'_4
            # index here is index in K_hlgy_lk.

for x in E:
    if x not in E_good_cover:
        E2E3_prime.append(tuple(x[:4]))
        # E2E3_prime contains all (index, manifold name, cusp number) so that (manifold, cusp number) does not belong to
        #\mathcal{E}_{good cover} but belongs to \mathcal{E}. Index here is index in K_hlgy_lk.

'''print(' ')
print('The members of E_1_prime are: ')
print(' ')
for i in range(882):
    for x in set(E1_prime):
        if i==x[0]:
            print(x)
            print(' ')
    

print(' ')
print('Combined members of E_2_prime and E_3_prime are: ')
print(' ')
for i in range(882):
    for x in set(E2E3_prime):
        if i==x[0]:
            print(x)
            print(' ')

print(' ')
print('The members of E_4_prime are: ')
print(' ')
for i in range(882):
    for x in set(E4_prime):
        if i==x[0]:
            print(x)
            print(' ')'''

E4=set(E4_prime)
E1=set(E1_prime)
E2E3=set(E2E3_prime)
print(' ')
E4_remove=set()
for x in E4:
    if x[0]==333 or x[0]==336:
        E4_remove.add(x)
        if x[2]==3:
            E2E3.add(x)  # Sets up union of \mathcal{E}_2 and \mathcal{E}_3 from E2E3_prime
        else:
            E1.add(x) # Sets up \mathcal{E}_1 from \mathcal{E}'_1

E4=E4-E4_remove # Sets up \mathcal{E}_4 from \mathcal{E}'_4


print(' ')
print('The members of E_1 are: ')
print(' ')
for i in range(882):
    for x in E1:
        if i==x[0]:
            print(x)
            print(' ')
print('Total number of elements in E_1 are: ')
print(len(list(E1)))
print(' ')

      
print(' ')
print('Combined members of E_2 and E_3 are: ')
print(' ')
for i in range(882):
    for x in E2E3:
        if i==x[0]:
            print(x)
            print(' ')
print('Total number of combined elements in E_2 and E_3 are: ')
print(len(list(E2E3)))
print(' ')

      
print(' ')
print('The members of E_4 are: ')
print(' ')
for i in range(882):
    for x in E4:
        if i==x[0]:
            print(x)
            print(' ')
print('Total number of elements in E_4 are: ')
print(len(list(E4)))
print(' ')
