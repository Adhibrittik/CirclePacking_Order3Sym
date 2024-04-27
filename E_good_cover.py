import json
from SigToSeq import Des_seq
from TestForCovers import CuspSeqs, Covers, CuspCovers
# Both SigToSeq.py and TestForCovers.py can be accessed from the
# url "https://github.com/Adhibrittik/orb_triangulation_tetrahedral"

with open("Excep_tuple.json", "r+") as excep:
    E=json.load(excep)# import "Excep_tuple.json" as list E


with open("Iso_sigs.json", "r+") as sigfile:
    Isom=json.load(sigfile)# import "Iso_sigs.json" as list Isom

dseqdown=[0,0,0,1,2,3,4,0,1,5,6,2,6,4,1,4,5,1,3,3,4,6,2,7,3,2,5,8,8,8,9,5,7,9,7,6,9,7,8,9]
# destination sequence of O_{(2,3,6),(2,2,2,2)}

E_good_cover=[]

for j in range(86):
    for sig in Isom[j]:
        dsequp=Des_seq(Triangulation3.fromIsoSig(sig))# destination sequence corresponding to sig
        Cover_list=Covers(dsequp,dseqdown) # the list of all covers from dsequp to dseqdown
        if len(Cover_list)!=0:
            for c in Cover_list:
                Rigid_preimage=[l[0] for l in CuspCovers(c, CuspSeqs(dsequp), CuspSeqs(dseqdown)) if l[1]==[0,1,3,4]]
                #Rigid_preimage is the list of all cusps of dsequp mapping to rigid cusp [0,1,3,4] of O_{(2,3,6),(2,2,2,2)}
                if len(Rigid_preimage)==1:
                    E_good_cover.append(E[j])#if only one cusp covers [0,1,3,4], j-th element of \mathcal{E} is in \mathcal{E}_{good cover}


        

with open("E_good_cover.json", "w+") as Egoodcover:
    json.dump(E_good_cover, Egoodcover)
# export the list E_good_cover as the "E_good_cover.json" file
