import regina
from SigToSeq import Des_seq
from TestForCovers import CuspSeqs, Covers, CuspCovers 
# Both SigToSeq.py and TestForCovers.py can be accessed from the
# url "https://github.com/Adhibrittik/orb_triangulation_tetrahedral"


des_seq_O4=[0,1,1,0,1,0,0,2,3,2,2,1,2,3,3,3]
print('des_seq_O4 is ')
print(des_seq_O4)
print()
print()

print('Calculation when M_0 is 6^2_2 complement ')
print()

Isom_622='eLMkbcddddedde' #Default tetrahedral isomorphism signature of otet04_00001 aka 6^2_2
print('Default tetrahedral isomorphism signature of otet04_00001 aka 6^2_2 complement is ')
print(Isom_622)
print()



des_seq_622=Des_seq(Triangulation3.fromIsoSig(Isom_622))
print('des_seq_622 is ')
print(des_seq_622)
print()

CoverList_622=Covers(des_seq_622,des_seq_O4)
print('Covers from des_seq_622 to des_seq_O4 are ')
print(CoverList_622)
print()
print()


print('Calculation when M_0 is L12n2208 complement')
print()

Isom_L12n2208='mvvLPQwQQfhgffijlklklkaaaaaaaaaaaaa'#Non-default tetrahedral isomorphism signature of otet12_00009 aka L12n2208 complement
print('Non-default tetrahedral isomorphism signature of otet12_00009 aka L12n2208 complement is ')
print(Isom_L12n2208)
print()

des_seq_L12n2208=Des_seq(Triangulation3.fromIsoSig(Isom_L12n2208))
print('des_seq_L12n2208 is ')
print(des_seq_L12n2208)
print()


CoverList_L12n2208=Covers(des_seq_L12n2208,des_seq_O4)
print('Covers from des_seq_L12n2208 to des_seq_O4 are ')
print(CoverList_L12n2208)
print()
print()


for i in range(len(CoverList_L12n2208)):
    print('For the ', i, '-th cover from des_seq_L12n2208 to des_seq_O4, Cusp covers look like ')
    print()
    print(CuspCovers(CoverList_L12n2208[i], CuspSeqs(des_seq_L12n2208), CuspSeqs(des_seq_O4)))
    print()
    print('Cusps of des_seq_O4 are ')
    print()
    print(CuspSeqs(des_seq_O4))
    print()
    

