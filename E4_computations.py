import regina
import json
from SigToSeq import Des_seq, Cusp_info, Mfd_cusp_index
from TestForCovers import CuspSeqs, Covers, CuspCovers 
# Both SigToSeq.py and TestForCovers.py can be accessed from the
# url "https://github.com/Adhibrittik/orb_triangulation_tetrahedral"


with open("E4_snappy_triangulations.json", "r+") as E4decomp:
    E4_decomp=json.load(E4decomp)
# import all the snappy triangulations data from "E4_snappy_triangulations.json" file
# of all the tetrahedral deomcpositions of all manifolds corresponding to \mathcal{E}_4


Snappy_triangulations_otet20_00049=E4_decomp['Snappy_triangulations_otet20_00049']

Snappy_triangulations_otet20_00063=E4_decomp['Snappy_triangulations_otet20_00063']

Snappy_triangulations_otet20_00462=E4_decomp['Snappy_triangulations_otet20_00462']

Snappy_triangulations_otet20_00474=E4_decomp['Snappy_triangulations_otet20_00474']

Snappy_triangulations_otet20_00577=E4_decomp['Snappy_triangulations_otet20_00577']

dseqdown=[0,0,0,1,2,3,4,0,1,5,6,2,6,4,1,4,5,1,3,3,4,6,2,7,3,2,5,8,8,8,9,5,7,9,7,6,9,7,8,9]
# destination sequence of O_{(2,3,6),(2,2,2,2)}


print('Computations for otet20_00049:')
print(' ')

for decomp in Snappy_triangulations_otet20_00049:
    t=Triangulation3(decomp)
    print('Isomorphism Signature',t.isoSig())
    print(' ')
    dsequp=Des_seq(t)
    print('Destination sequence', dsequp)
    print(' ')
    Cover_list=Covers(dsequp, dseqdown)
    print('All covers', Cover_list)
    print(' ')
    for j in range(len(Cover_list)):
        print(j,'th cover')
        print(' ')
        Cusp_cover=CuspCovers(Cover_list[j], CuspSeqs(dsequp), CuspSeqs(dseqdown))
        print('Cusp Cover', Cusp_cover)
        print(' ')
        rigid_pre_image=[]
        for l in Cusp_cover:
            if l[1]==[0,1,3,4]:
                rigid_pre_image.append(l[0])
        if len(rigid_pre_image)==1: 
            Mfd_cusp=Mfd_cusp_index(t,rigid_pre_image[0][0])
            print(Mfd_cusp, ' is the only cusp of Snappy Triangulation that covers the rigid cusp')
            print(' ')
            print("(ideal tetrahedra, ideal vertex) pairs and index of the first Glued_bary_simplex_pair from rigid_pre_image:")
            print(Cusp_info(t)[rigid_pre_image[0][0]])
            print(' ')
            print('Printing regina cusp data:')
            print(t.boundaryComponents())
            print(' ')

            
#The above checks whether there are triangulation preserving covers from
#the orbifold destination sequence corresponding to the tetrahedral decompsitions
# of otet20_00049 to O_{(2,3,6),(2,2,2,2)} so that the rigid cusp of  O_{(2,3,6),(2,2,2,2)}
# has only one pre-image. If it is so, it prints out which cusp is the only cusp that
# maps to the rigid cusp. 


print('Computations for otet20_00063:')
print(' ')

for decomp in Snappy_triangulations_otet20_00063:
    t=Triangulation3(decomp)
    print('Isomorphism Signature',t.isoSig())
    print(' ')
    dsequp=Des_seq(t)
    print('Destination sequence', dsequp)
    print(' ')
    Cover_list=Covers(dsequp, dseqdown)
    print('All covers', Cover_list)
    print(' ')
    for j in range(len(Cover_list)):
        print(j,'th cover')
        print(' ')
        Cusp_cover=CuspCovers(Cover_list[j], CuspSeqs(dsequp), CuspSeqs(dseqdown))
        print('Cusp Cover', Cusp_cover)
        print(' ')
        rigid_pre_image=[]
        for l in Cusp_cover:
            if l[1]==[0,1,3,4]:
                rigid_pre_image.append(l[0])
        if len(rigid_pre_image)==1: 
            Mfd_cusp=Mfd_cusp_index(t,rigid_pre_image[0][0])
            print(Mfd_cusp, ' is the only cusp of Snappy Triangulation that covers the rigid cusp')
            print(' ')
            print("(ideal tetrahedra, ideal vertex) pairs and index of the first Glued_bary_simplex_pair from rigid_pre_image:")
            print(Cusp_info(t)[rigid_pre_image[0][0]])
            print(' ')
            print('Printing regina cusp data:')
            print(t.boundaryComponents())
            print(' ')
#The above checks whether there are triangulation preserving covers from
#the orbifold destination sequence corresponding to the tetrahedral decompsitions
# of otet20_00063 to O_{(2,3,6),(2,2,2,2)} so that the rigid cusp of  O_{(2,3,6),(2,2,2,2)}
# has only one pre-image. If it is so, it prints out which cusp is the only cusp that
# maps to the rigid cusp. 


print('Computations for otet20_00462:')
print(' ')

for decomp in Snappy_triangulations_otet20_00462:
    t=Triangulation3(decomp)
    print('Isomorphism Signature',t.isoSig())
    print(' ')
    dsequp=Des_seq(t)
    print('Destination sequence', dsequp)
    print(' ')
    Cover_list=Covers(dsequp, dseqdown)
    print('All covers', Cover_list)
    print(' ')
    for j in range(len(Cover_list)):
        print(j,'th cover')
        print(' ')
        Cusp_cover=CuspCovers(Cover_list[j], CuspSeqs(dsequp), CuspSeqs(dseqdown))
        print('Cusp Cover', Cusp_cover)
        print(' ')
        rigid_pre_image=[]
        for l in Cusp_cover:
            if l[1]==[0,1,3,4]:
                rigid_pre_image.append(l[0])
        if len(rigid_pre_image)==1: 
            Mfd_cusp=Mfd_cusp_index(t,rigid_pre_image[0][0])
            print(Mfd_cusp, ' is the only cusp of Snappy Triangulation that covers the rigid cusp')
            print(' ')
            print("(ideal tetrahedra, ideal vertex) pairs and index of the first Glued_bary_simplex_pair from rigid_pre_image:")
            print(Cusp_info(t)[rigid_pre_image[0][0]])
            print(' ')
            print('Printing regina cusp data:')
            print(t.boundaryComponents())
            print(' ')            
#The above checks whether there are triangulation preserving covers from
#the orbifold destination sequence corresponding to the tetrahedral decompsitions
# of otet20_00462 to O_{(2,3,6),(2,2,2,2)} so that the rigid cusp of  O_{(2,3,6),(2,2,2,2)}
# has only one pre-image. If it is so, it prints out which cusp is the only cusp that
# maps to the rigid cusp.





print('Computations for otet20_00474:')
print(' ')

for decomp in Snappy_triangulations_otet20_00474:
    t=Triangulation3(decomp)
    print('Isomorphism Signature',t.isoSig())
    print(' ')
    dsequp=Des_seq(t)
    print('Destination sequence', dsequp)
    print(' ')
    Cover_list=Covers(dsequp, dseqdown)
    print('All covers', Cover_list)
    print(' ')
    for j in range(len(Cover_list)):
        print(j,'th cover')
        print(' ')
        Cusp_cover=CuspCovers(Cover_list[j], CuspSeqs(dsequp), CuspSeqs(dseqdown))
        print('Cusp Cover', Cusp_cover)
        print(' ')
        rigid_pre_image=[]
        for l in Cusp_cover:
            if l[1]==[0,1,3,4]:
                rigid_pre_image.append(l[0])
        if len(rigid_pre_image)==1: 
            Mfd_cusp=Mfd_cusp_index(t,rigid_pre_image[0][0])
            print(Mfd_cusp, ' is the only cusp of Snappy Triangulation that covers the rigid cusp')
            print(' ')
            print("(ideal tetrahedra, ideal vertex) pairs and index of the first Glued_bary_simplex_pair from rigid_pre_image:")
            print(Cusp_info(t)[rigid_pre_image[0][0]])
            print(' ')
            print('Printing regina cusp data:')
            print(t.boundaryComponents())
            print(' ')
#The above checks whether there are triangulation preserving covers from
#the orbifold destination sequence corresponding to the tetrahedral decompsitions
# of otet20_00474 to O_{(2,3,6),(2,2,2,2)} so that the rigid cusp of  O_{(2,3,6),(2,2,2,2)}
# has only one pre-image. If it is so, it prints out which cusp is the only cusp that
# maps to the rigid cusp.



print('Computations for otet20_00577:')
print(' ')

for decomp in Snappy_triangulations_otet20_00577:
    t=Triangulation3(decomp)
    print('Isomorphism Signature',t.isoSig())
    print(' ')
    dsequp=Des_seq(t)
    print('Destination sequence', dsequp)
    print(' ')
    Cover_list=Covers(dsequp, dseqdown)
    print('All covers', Cover_list)
    print(' ')
    for j in range(len(Cover_list)):
        print(j,'th cover')
        print(' ')
        Cusp_cover=CuspCovers(Cover_list[j], CuspSeqs(dsequp), CuspSeqs(dseqdown))
        print('Cusp Cover', Cusp_cover)
        print(' ')
        rigid_pre_image=[]
        for l in Cusp_cover:
            if l[1]==[0,1,3,4]:
                rigid_pre_image.append(l[0])
        if len(rigid_pre_image)==1: 
            Mfd_cusp=Mfd_cusp_index(t,rigid_pre_image[0][0])
            print(Mfd_cusp, ' is the only cusp of Snappy Triangulation that covers the rigid cusp')
            print(' ')
            print("(ideal tetrahedra, ideal vertex) pairs and index of the first Glued_bary_simplex_pair from rigid_pre_image:")
            print(Cusp_info(t)[rigid_pre_image[0][0]])
            print(' ')
            print('Printing regina cusp data:')
            print(t.boundaryComponents())
            print(' ')
#The above checks whether there are triangulation preserving covers from
#the orbifold destination sequence corresponding to the tetrahedral decompsitions
# of otet20_00577 to O_{(2,3,6),(2,2,2,2)} so that the rigid cusp of  O_{(2,3,6),(2,2,2,2)}
# has only one pre-image. If it is so, it prints out which cusp is the only cusp that
# maps to the rigid cusp.  
