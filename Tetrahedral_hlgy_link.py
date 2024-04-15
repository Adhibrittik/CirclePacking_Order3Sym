import snappy

def Hlgy_tor(M):
    '''returns False iff there are no torsion elements in
    the homology group of M'''
    r=False
    G=M.homology()
    L=G.elementary_divisors()
    if L[0]!=0:
            r=True
    return r
def Link_HS(M):
    '''returns true iff homology group of M is Z^n'''
    r=False
    G=M.homology()
    if Hlgy_tor(M)==False:
        if G.rank()==M.num_cusps():
            r=True
    return r

K_hlgy_lk=[]
for i in range(1,26):
    for M in snappy.TetrahedralOrientableCuspedCensus(solids=i):
        if Link_HS(M)==True:
            if M.num_cusps()>1:
                K_hlgy_lk.append(M)
'''The list K_hlgy_lk above collects the homology links with more than one cusp from
the orientable tetrahedral census of Fominykh, Garoufalidis, Goerner, Tarkaev and Vesnin 
which have 25 or fewer tetrahedra in their tetrahedral decompositions'''

def Cusp_list(M):
    '''returns a maximal list of cusps of M such that no two cusps in the list
    are exchanged by a symmetry of M'''
    G=M.symmetry_group()
    IG=G.isometries()
    L=range(M.num_cusps())
    K=[]
    for g in IG:
        for i in L:
            if g.cusp_images()[i]>i and g.cusp_images()[g.cusp_images()[i]]==i:
                K.append(g.cusp_images()[i])
    return list(set(L)-set(K))
