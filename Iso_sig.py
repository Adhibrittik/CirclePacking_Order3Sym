import regina
import json


from example import children_iterator # example.py can be downloaded from
# the url "https://unhyperbolic.org/tetrahedralCensus/tetrahedralCensus/regina/". 
# One should modify the Regina command "getFirstTreeChild" to "firstChild"
# and "getNextTreeSibling" to "nextSibling" inside the "children_iterator" function
# of example.py as these changes were made in the newer versions of Regina. See the url
# "https://github.com/regina-normal/regina/blob/master/CHANGES.txt"
# The rest of the code in examle.py apart from children_iterator function should be commented out.  




def Signatures (manifold):
    '''For manifold in the Regina packet census below
    the function Signatures collects and returns the list of the
    isomorphism signatures of all the tetrahedral decompositions of
    manifold from census'''
    L_sig=[]
    
    All_triangulations=list(children_iterator(manifold))
    for triangulation in All_triangulations[:-1]:# the last entry of All_triangulation is excluded as it is the canonical decomposition which might not be tetrahedral
        L_sig.append(triangulation.isoSig())
    return L_sig

def Contain(check_list, test_element):
    '''Contain functions returns True if test_element is the list check_list '''
    r=False
    for i in check_list:
        if test_element==i:
            r=True
            break
    return r
    

    
    
census = regina.open('tetrahedralOrientableCuspedCensus.rga')# download tetrahedralOrientableCuspedCensus.rga 
# from "https://unhyperbolic.org/tetrahedralCensus/tetrahedralCensus/regina/"

All_census_sigs=[]
for tetrahedra_number in children_iterator(census):
    for manifold in children_iterator(tetrahedra_number): 
        All_census_sigs.append(Signatures(manifold)) # All_census_sigs is the list whose elements are
# lists each containing the isomorphism signatures of all the tetrahedral decompositions of all manifolds
# in the regina packet


with open("Excep_tuple.json", "r+") as exceptuple:
    E=json.load(exceptuple)# import "Excep_tuple.json" as list E
    


All_excep_sigs=[]

for x in E:
    for i in range(len(All_census_sigs)):
        if Contain(All_census_sigs[i], x[3])==True:
           All_excep_sigs.append(All_census_sigs[i])
           break #All_excep_sigs is the list whose elements are
# lists each containing the isomorphism signatures of all the tetrahedral decompositions of manifolds
# M such that (M,c) is in \mathcal{E}. We check whether the default triangulation (i.e. x[3])
# of this M is in some element of All_census_sigs and if yes, we add that element (which contains
# the isomorphism signatures of all the tetrahedral decompositions of M) to All_excep_sigs


with open("Iso_sigs.json", "w+") as allexcepsigs:
    json.dump(All_excep_sigs, allexcepsigs) # export list All_excep_sigs as the "Iso_sigs.json" file 



            



    
