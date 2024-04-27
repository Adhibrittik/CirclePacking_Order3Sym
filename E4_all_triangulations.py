import snappy
import json

sigs_otet20_00049=['uLLLLvzPPzLQQQccefemlkokqsqrtqsrtrstiitdipattiuapqlqpqphi']
sigs_otet20_00063=['uLLLLvzQMzPPQPccefemllkkkppqprsqstttiitdimpamtiaplttdhxeh', 'uLLPLvAALQMvPQcceefejijimnomnpsttstsiiatdpaxteqahiaehdqid']
sigs_otet20_00462=['uLLvvvLAMQQAPQcceppmlronlplnoqtststsiiuhxqpiaexqixiqaqllx','uvvLLMvvQAQQQPcfghfnrponsoprsqosqtttaaulaqxxluaulqahluluq']
sigs_otet20_00474=['uLLvvvLAPQQAPQccennmlllnrorqpqttssstiilxhhtxapaaqaipaqiaa', 'uvvLLPwLPMQAPQcgjilgmnmnpopqrptststsmataptdammaaatpupqqux']
sigs_otet20_00577=['uLLzvvvPQQwPQQcceenqllnpomotssrsrtrtiiamqamxaqxippaihhiia', 'uvvLLAwLMMQAPQchfgkhomnmqpooqrststtseeauauappptahqauaxqex']
# The above five lists contain the isomporphism signatures of all the tetrahedral decompositions of the manifolds that correspond to \mathcal{E}_4.
# One can see these signatures at the url "https://arxiv.org/src/1502.00383v2/anc/data/namedIsometricOrientableTetrahedralTessellations_up_to_25.txt"
# In the url above, in the names of the above manifolds, there is one less "0" (eg. 'otet20_00049' is 'otet20_0049' in the url).  

E4_snappy_triangulations={'Snappy_triangulations_otet20_00049':[snappy.Manifold(s)._to_string() for s in  sigs_otet20_00049],

'Snappy_triangulations_otet20_00063':[snappy.Manifold(s)._to_string() for s in  sigs_otet20_00063],

'Snappy_triangulations_otet20_00462':[snappy.Manifold(s)._to_string() for s in  sigs_otet20_00462],

'Snappy_triangulations_otet20_00474':[snappy.Manifold(s)._to_string() for s in  sigs_otet20_00474],

'Snappy_triangulations_otet20_00577':[snappy.Manifold(s)._to_string() for s in  sigs_otet20_00577]}
# In the above dictionary, the value of the each key is a list whose elements are strings each containing the SnapPy triangulation data for
# the isomorphism signatures of the tetrahedral decompositions of the correspondig manifold (associated to \mathcal{E}_4) given in the key
 

with open("E4_snappy_triangulations.json", "w+") as E4decomps:
    json.dump(E4_snappy_triangulations, E4decomps)# Export the dictionary E4_snappy_triangulations as the "E4_snappy_triangulations.json" file




