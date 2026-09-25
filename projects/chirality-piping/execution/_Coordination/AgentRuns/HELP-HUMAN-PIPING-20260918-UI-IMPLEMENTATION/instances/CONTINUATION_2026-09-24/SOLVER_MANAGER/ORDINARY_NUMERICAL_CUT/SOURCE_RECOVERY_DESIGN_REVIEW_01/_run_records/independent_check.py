#!/usr/bin/env python3
"""Independent bounded design checks. Standard library; no production imports.

Rational oracle: general elimination. Design path: per-block Cramer numerator
composition. Beam source: integrate cubic Hermite curvature energy and virtual
work independently of the production coefficient table. This does not execute
Rust expansion, bounded projection, adapter, product, or consumer paths.
"""
from fractions import Fraction as Q
import json
import random

records = []

def dot(x, y): return sum((a*b for a,b in zip(x,y)), Q(0))
def mv(a, x): return [dot(row,x) for row in a]
def mat(n): return [[Q(0) for _ in range(n)] for _ in range(n)]

def elimination(k, f, prescribed):
    free = [i for i in range(len(f)) if i not in prescribed]
    m = [[Q(k[i][j]) for j in free] +
         [Q(f[i])-sum(k[i][j]*v for j,v in prescribed.items())] for i in free]
    for col in range(len(free)):
        pivot = next(r for r in range(col,len(free)) if m[r][col])
        m[col],m[pivot] = m[pivot],m[col]
        p=m[col][col]; m[col]=[x/p for x in m[col]]
        for r in range(col+1,len(free)):
            p=m[r][col]; m[r]=[x-p*y for x,y in zip(m[r],m[col])]
    u=[Q(prescribed.get(i,0)) for i in range(len(f))]
    for col in reversed(range(len(free))):
        u[free[col]]=m[col][-1]-sum(m[col][j]*u[free[j]] for j in range(col+1,len(free)))
    return u

def blocks(k, prescribed):
    unseen=set(range(len(k)))-set(prescribed); out=[]
    while unseen:
        group=[min(unseen)]; unseen.remove(group[0])
        for i in group:
            neighbors=sorted(j for j in unseen if k[i][j])
            group.extend(neighbors); unseen.difference_update(neighbors)
        out.append(group)
    return out

def functional(k, f, prescribed, ell, beta=Q(0)):
    """Compose numerator/denominator block contributions, then combine ratios."""
    numerator=Q(beta)+sum(ell[i]*v for i,v in prescribed.items()); denominator=Q(1)
    for group in blocks(k,prescribed):
        if len(group)>2: raise ValueError('unsupported block')
        i=group[0]; a=k[i][i]
        if a<=0: raise ValueError('nonpositive first minor')
        h=[f[r]-sum(k[r][c]*v for c,v in prescribed.items()) for r in group]
        if len(group)==1: bn,bd=ell[i]*h[0],a
        else:
            j=group[1]; b=k[i][j]; c=k[j][j]; bd=a*c-b*b
            if bd<=0: raise ValueError('nonpositive determinant')
            bn=ell[i]*(c*h[0]-b*h[1])+ell[j]*(a*h[1]-b*h[0])
        numerator,denominator=numerator*bd+bn*denominator,denominator*bd
    return numerator/denominator

def verified_functional(k,f,p,ell,beta=Q(0)):
    u=elimination(k,f,p); q=functional(k,f,p,ell,beta)
    assert q==Q(beta)+dot(ell,u)
    for i in set(range(len(f)))-set(p): assert dot(k[i],u)==f[i]
    return q

# Generic multiple-block matrices with arbitrary constrained couplings and offsets.
rng=random.Random(9242026)
for case in range(120):
    sizes=[1+rng.randrange(2) for _ in range(1+rng.randrange(4))]
    nf=sum(sizes); n=nf+2; k=mat(n); cursor=0
    for size in sizes:
        a=Q(1+rng.randrange(7)); k[cursor][cursor]=a
        if size==2:
            b=Q(rng.choice([-3,-2,-1,1,2,3]),4)
            k[cursor][cursor+1]=k[cursor+1][cursor]=b
            k[cursor+1][cursor+1]=b*b/a+Q(1+rng.randrange(5))
        cursor+=size
    for i in range(n):
        for j in range(max(i,nf),n):
            k[i][j]=k[j][i]=Q(rng.randrange(-4,5),8)
    p={nf:Q(rng.randrange(-3,4),8),nf+1:Q(rng.randrange(-3,4),16)}
    f=[Q(rng.randrange(-8,9),16) for _ in range(n)]
    for _ in range(5):
        ell=[Q(rng.randrange(-5,6),8) for _ in range(n)]
        verified_functional(k,f,p,ell,Q(rng.randrange(-5,6),8))
records.append({'group':'generic partitions, prescribed couplings, offsets and cross-block ratios',
                'systems':120,'functional_comparisons':600})

def derivative(p): return [Q(i)*p[i] for i in range(1,len(p))]
def integral(p,L): return sum((v*L**(i+1)/Q(i+1) for i,v in enumerate(p)),Q(0))
def product(p,q):
    out=[Q(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): out[i+j]+=a*b
    return out

# Build the full local frame matrix from strain-energy and consistent load work.
L=Q(2); EA=Q(37); GJ=Q(7); EIY=Q(11); EIZ=Q(13)
kl=mat(12); feq=[Q(0)]*12; qx,qy,qz=Q(3,8),Q(-5,16),Q(7,32)
for ids,rigidity in [([0,6],EA),([3,9],GJ)]:
    for i,si in zip(ids,[-1,1]):
        for j,sj in zip(ids,[-1,1]): kl[i][j]+=rigidity*si*sj/L
hermite=[[Q(1),Q(0),-3/L**2,2/L**3],
         [Q(0),Q(1),-2/L,1/L**2],
         [Q(0),Q(0),3/L**2,-2/L**3],
         [Q(0),Q(0),-1/L,1/L**2]]
for ids,signs,ei,q in [([1,5,7,11],[1,1,1,1],EIZ,qy),
                       ([2,4,8,10],[1,-1,1,-1],EIY,qz)]:
    shapes=[[s*v for v in p] for p,s in zip(hermite,signs)]
    curvature=[derivative(derivative(p)) for p in shapes]
    for ii,i in enumerate(ids):
        feq[i]+=q*integral(shapes[ii],L)
        for jj,j in enumerate(ids): kl[i][j]+=ei*integral(product(curvature[ii],curvature[jj]),L)
feq[0]+=qx*L/2; feq[6]+=qx*L/2
thermal=Q(9,32); feq[0]-=thermal; feq[6]+=thermal
# Two distinct root rotational springs and a spring on a prescribed translation.
devices=[(3,Q(1,64),Q(1,128)),(3,Q(1,128),Q(-1,256)),(0,Q(5),Q(1,64))]
k=[row[:] for row in kl]
nodal=[Q((-1)**i*(i+1),128) for i in range(12)]
f=[a+b for a,b in zip(nodal,feq)]
for i,s,g in devices: k[i][i]+=s; f[i]+=s*g
p={i:Q(i+1,1024) for i in [0,1,2,4,5]}
u=elimination(k,f,p)
ends=[verified_functional(k,f,p,row,-offset) for row,offset in zip(kl,feq)]
assert all(ends), 'full component coverage witness must be nonzero'
reaction=[dot(row,u)-fi for row,fi in zip(k,f)]
actions=[]
for i,s,g in devices:
    ell=[Q(0)]*12; ell[i]=-s
    actions.append(verified_functional(k,f,p,ell,s*g))
for i in range(12):
    device=sum(action for action,device in zip(actions,devices) if device[0]==i)
    assert ends[i]-nodal[i]-device==reaction[i]
assert reaction[3]==0 and actions[0] and actions[1] and actions[0]!=actions[1]
assert reaction[0]!=0 and actions[2]!=0

# Derive a section from each side independently. Left and right segment moment
# balance must meet at every station after expressing both in the j-side convention.
for x in [Q(0),L/4,L/2,3*L/4,L]:
    left=[-ends[0]-qx*x,-ends[1]-qy*x,-ends[2]-qz*x,-ends[3],
          -ends[4]-ends[2]*x-qz*x*x/2,-ends[5]+ends[1]*x+qy*x*x/2]
    y=L-x
    right=[ends[6]+qx*y,ends[7]+qy*y,ends[8]+qz*y,ends[9],
           ends[10]-ends[8]*y-qz*y*y/2,ends[11]+ends[7]*y+qy*y*y/2]
    assert left==right
    # Build each complete station affine functional from the primitive rows.
    station=[(0,-1,None,0,-qx*x),(1,-1,None,0,-qy*x),(2,-1,None,0,-qz*x),
             (3,-1,None,0,Q(0)),(4,-1,2,-x,-qz*x*x/2),(5,-1,1,x,qy*x*x/2)]
    for row,(a,sa,b,sb,offset) in enumerate(station):
        ell=[sa*kl[a][j]+(sb*kl[b][j] if b is not None else 0) for j in range(12)]
        beta=offset-sa*feq[a]-(sb*feq[b] if b is not None else 0)
        assert verified_functional(k,f,p,ell,beta)==left[row]
records.append({'group':'12-DOF energy-derived beam with uniform/thermal affine source',
 'free_block_orders':list(map(len,blocks(k,p))),'nonzero_end_components':12,
 'section_comparisons':30,'spring_device_actions':list(map(str,actions)),
 'root_rx_equilibrium_reaction':str(reaction[3]),
 'prescribed_ux_ideal_reaction':str(reaction[0]),
 'scope':'algebraic full-load witness; minimum product adapter may explicitly decline non-nodal families'})

# Proper signed rotations (same 3x3 map on translations and rotations) plus
# arbitrary global indexing. Local forces must be invariant on the same frame.
for axisperm,signs in [([1,2,0],[1,-1,-1]),([2,1,0],[-1,1,1])]:
    inversion=sum(axisperm[i]>axisperm[j] for i in range(3) for j in range(i+1,3))
    assert (-1)**inversion*signs[0]*signs[1]*signs[2]==1
    order=[group*3+axisperm[i] for group in range(4) for i in range(3)]
    sense=signs*4
    kg=[[sense[i]*sense[j]*k[order[i]][order[j]] for j in range(12)] for i in range(12)]
    fg=[sense[i]*f[order[i]] for i in range(12)]
    pg={i:sense[i]*p[old] for i,old in enumerate(order) if old in p}
    ug=elimination(kg,fg,pg)
    assert ug==[sense[i]*u[order[i]] for i in range(12)]
    for r in range(12):
        ell=[kl[r][order[i]]*sense[i] for i in range(12)]
        assert verified_functional(kg,fg,pg,ell,-feq[r])==ends[r]
records.append({'group':'proper signed rotations and index permutation source closure',
                'orientations':2,'end_functionals_checked':24})

# N05/N06 declared-source examples, separately frozen from NP-A.
a=Q(float.fromhex('0x1.07c49b6ac7e26p+21'))
for name,ks,torque in [('N05',1e-4,1e-8),('N06-scale illustration',1e-12,1e-16)]:
    s,t=Q(ks),Q(torque); a2=[[a+s,-a],[-a,a]]
    uv=elimination(a2,[Q(0),t],{})
    end=verified_functional(a2,[Q(0),t],{},[-a,a])
    spring=verified_functional(a2,[Q(0),t],{},[-s,Q(0)])
    reconstructed=Q(float(a)*(float(uv[1])-float(uv[0])))
    assert end==t and spring==-t
    assert abs((reconstructed-t)/t)>Q(1,10**9)
    stored=[[Q(float(a)+ks),-a],[-a,a]]
    det_stored=stored[0][0]*a-a*a
    if name.startswith('N06'): assert det_stored==0 and float(uv[0])==float(uv[1])
    records.append({'group':name,'a_hex':float(a).hex(), 'source_determinant_positive':s*a>0,
       'stored_determinant_zero':det_stored==0, 'direct_member_torque':float(end),
       'direct_spring_action':float(spring),'projected_u_torque':float(reconstructed),
       'relative_error_after_projecting_u':float((reconstructed-t)/t),
       'product_execution':False,'N06_actual_coefficient_capture':False})

# Fully prescribed and conservative graph/positivity rejections.
verified_functional([[Q(2),Q(1)],[Q(1),Q(2)]],[Q(3),Q(5)],{0:Q(1,8),1:Q(-3,16)},[Q(7),Q(-2)],Q(9,4))
e=Q(1,2**80)
bad=[([[Q(2),Q(-1),0],[Q(-1),Q(2),e],[0,e,Q(2)]],'unsupported block'),
     ([[Q(1),Q(1)],[Q(1),Q(1)]],'nonpositive determinant'),
     ([[Q(-1)]],'nonpositive first minor')]
for matrix,message in bad:
    try: functional(matrix,[Q(0)]*len(matrix),{},[Q(1)]*len(matrix))
    except ValueError as error: assert str(error)==message
    else: raise AssertionError('inadmissible source accepted')
records.append({'group':'fully prescribed, tiny connected 3-block, zero/negative minors',
                'conservative_rejections':3})
print(json.dumps({'scope':'independent rational design verification; no implementation or physical qualification',
                  'groups_passed':len(records),'records':records},indent=2))
