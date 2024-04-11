
from math import sqrt, ceil
import snappy

k0=1/sqrt(sqrt(3))

def Cos_angle(u,v):
    '''returns absolute value of cosine of the angle between the vectors 
    given by complex numbers u and v'''
    
    return abs(u.real*v.real+u.imag*v.imag)/(abs(u)*abs(v)) 
    
    
def R_1(x,y):
    '''returns r_{x,3}(y) where r_{x,3} is the order 3 rotation around x'''
    
    re=x.real-(y-x).real/2-(y-x).imag*sqrt(3)/2
    im=(x.imag-(y-x).imag/2+(y-x).real*sqrt(3)/2)*(0+1J)
    return re+im

def R_2(x,y):
    '''returns r_{x,3}^2 (y) where r_{x,3} is the order 3 rotation around x'''

    re=x.real-(y-x).real/2+(y-x).imag*sqrt(3)/2
    im=(x.imag-(y-x).imag/2-(y-x).real*sqrt(3)/2)*(0+1J)
    return re+im
  

def Centroid_strng(h,S,G,v,d):
    '''returns a set E whose elements
    do not belong to G and 
    are centroids of triangles with h as a vertex and two other vertices from S such that
    (1) the sides incident to h make an angle of pi/3 or 2 pi/3 at h, 
    (2) have the same length bounded by k0*sqrt(v) and
    (3) the distance between its centroid and vertex h is bounded above by d/3'''
    L=list(S)
    E=set()
    for x in range(len(L)):
        if 0.005<abs(L[x]-h)<k0*sqrt(v)+0.005:
            for y in range(x+1,len(L)):
                if abs(abs(L[y]-h)-abs(L[x]-h))<0.005 and abs(Cos_angle(L[x]-h,L[y]-h)-0.5)<0.005 and abs(-2*h+L[x]+L[y])/3<(d/3)+0.005 and Include((h+L[x]+L[y])/3,G)==False: E.add((h+L[x]+L[y])/3)
    return E


def Include(x,H):
    '''checks whether x belong to list H'''

    r=False
    for y in H:
        if abs(x-y)<0.005:
            r=True
            break
    return r



def Free_rot_strng(M,i):
    '''For manifold M and cusp i, if this function returns False then there is no W_{(3,3,3)} wallpaper group
    of symmetries of the $i$-circle packing of the complex plane satisfying Theorem 5.2 of the paper.
    If it returns True, the $i$-circle packing might have such a  W_{(3,3,3)} wallpaper group of symmetries but it is not guranteed - in other words inconclusive.'''
    c=M.cusp_neighborhood()
    c.set_displacement(c.reach(i),i)#Put ith cusp at infinity and maximizes ith cusp
	
    vol,mer,lon=c.volume(i),c.translations(i)[0],c.translations(i)[1]#sets up the cusp volume and meridianal and longitudinal translations for i-th cusp
    d,hei=max(abs(mer), abs(lon), abs(mer+lon), abs(mer-lon)),abs(mer)*sqrt(1-pow(Cos_angle(mer,lon),2))#d=maximal length between 2 points in i-cusp parallelogram, hei=height of i-cusp parallelogram
	
    H_circ_cen={x['center'] for x in c.horoballs(cutoff=0.9, which_cusp=i, full_list=True, high_precision=False) if x['index']==i}#set of horocenters of full sized i-horoballs

    H_diff_cen={x['center'] for x in c.horoballs(cutoff=0.1,which_cusp=i,full_list=True, high_precision=False) if x['index']!=i}#set of horocenters of (large number of) non i-horoballs 

    h=list(H_circ_cen)[0]#choosing the center of a circle in the i-cicle packing: so h here is the c_0 of Proposition 7.4
    k_h_sm=ceil(((11/7)*d+1)/hei)#this is k'_h(x) from Section 7 where x=4/7 
    k_sm=ceil(k_h_sm*abs(mer)*abs(Cos_angle(mer,lon))/abs(lon))#this is k'(x) from Section 7 where x=4/7
    k_l_sm=ceil(((11/7)*d+1)/abs(lon))#this is k'_l(x) from Section 7 where x=4/7
    k_h_la=ceil((d*((8/3)+ k_h_sm+k_sm+k_l_sm)+1)/hei)#this is k'_h(x) from Section 7 where x=5/3+k'_h(4/7)+k'(4/7)+k'_l(4/7)
    k_la=ceil(k_h_la*abs(mer)*abs(Cos_angle(mer,lon))/abs(lon))#this is k'(x) from Section 7 where x=5/3+k'_h(4/7)+k'(4/7)+k'_l(4/7)
    k_l_la=ceil((d*((8/3)+k_h_sm+k_sm+k_l_sm)+1)/abs(lon))#this is k'_l(x) from Section 7 where x=5/3+k'_h(4/7)+k'(4/7)+k'_l(4/7)
	
    H_small={x+p*mer+q*lon for x in H_circ_cen for p in range(-k_h_sm, k_h_sm+1) for q in range(-k_sm-k_l_sm, k_sm+k_l_sm+1)}#this is C'_P(x) from Proposition 7.4 where x=4/7
    H_large={x+p*mer+q*lon for x in H_circ_cen for p in range(-k_h_la, k_h_la+1) for q in range(-k_la-k_l_la, k_la+k_l_la+1)}#this is C'_P(x) from Proposition 7.4 where x=5/3+k'_h(4/7)+k'(4/7)+k'_l(4/7)
    H_diff={x+p*mer+q*lon for x in H_diff_cen for p in range(-k_h_sm,k_h_sm+1) for q in range(-k_sm-k_l_sm, k_sm+k_l_sm+1) if abs(x+p*mer+q*lon-h)<(d/3)+0.005}
    #this is an extended collection of horocenters of non i-horoballs 
	
    exist_free_rot=False
    H_free_rot=set()
    E=Centroid_strng(h,H_small,H_diff,vol,d)#this contains elements of E_strong from Proposition 7.4 that are not in H_diff

    for x in E:
        r=True
        for y in H_small:
            if Include(R_1(x,y),H_large)==False or Include(R_2(x,y),H_large)==False:
                r=False
                break
        if r==True and Include(x, H_free_rot)==False: H_free_rot.add(x) 
        if len(H_free_rot)>1:
            exist_free_rot=True
            break
    '''this loop checks if whether order 3 rotations R_1 and R_2 through members of E send elements of H_small to H_larege. If yes, they are added to the set H_free_rot.
    The moment H_free_rot has 2 elements, we stop loop. Otherwise, we check it for all elements of E.
    When H_free_rot does not have two elements, Free_rot_strng returns False, otherwise it returns True'''

    return (exist_free_rot)
    









             
     






