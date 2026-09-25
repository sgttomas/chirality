#!/usr/bin/env python3
"""Design arithmetic checks only. No production imports, solver or fixture writes."""
from fractions import Fraction as Q
from decimal import Decimal, localcontext
import json


def gauss(k, f):
    a = [list(map(Q, row)) + [Q(v)] for row, v in zip(k, f)]
    n = len(a)
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j])
        a[j], a[pivot] = a[pivot], a[j]
        p = a[j][j]
        a[j] = [x / p for x in a[j]]
        for i in range(n):
            if i != j:
                q = a[i][j]
                a[i] = [x - q*y for x, y in zip(a[i], a[j])]
    return [row[-1] for row in a]


def blocks(k, free):
    unseen = set(free); result = []
    while unseen:
        block = [min(unseen)]; unseen.remove(block[0])
        for i in block:
            found = sorted(j for j in unseen if k[i][j] != 0)
            block.extend(found); unseen.difference_update(found)
        result.append(block)
    return result


def affine(k, f, prescribed, ell, beta):
    n = len(f); free = [i for i in range(n) if i not in prescribed]
    u = [Q(0)]*n
    for i, x in prescribed.items(): u[i] = Q(x)
    for block in blocks(k, free):
        assert len(block) <= 2
        h = [Q(f[i]) - sum(k[i][j]*u[j] for j in prescribed) for i in block]
        i = block[0]; a = k[i][i]
        assert a > 0
        if len(block) == 1:
            u[i] = h[0]/a
        else:
            j = block[1]; b = k[i][j]; c = k[j][j]; delta = a*c-b*b
            assert delta > 0
            u[i], u[j] = (c*h[0]-b*h[1])/delta, (a*h[1]-b*h[0])/delta
    q = Q(beta) + sum(Q(c)*x for c,x in zip(ell,u))
    reduced = [[k[i][j] for j in free] for i in free]
    rhs = [Q(f[i])-sum(k[i][j]*u[j] for j in prescribed) for i in free]
    independent = gauss(reduced, rhs) if free else []
    assert [u[i] for i in free] == independent
    for i in free: assert sum(k[i][j]*u[j] for j in range(n)) == f[i]
    return u,q


def decimal(q):
    with localcontext() as c:
        c.prec=70
        return str(Decimal(q.numerator)/Decimal(q.denominator))

records = []
a = Q(float.fromhex('0x1.07c49b6ac7e26p+21'))
for name, spring, torque in [('N05-source-arithmetic',1e-4,1e-8),('N06-source-arithmetic',1e-12,1e-16)]:
    k,t = Q(spring),Q(torque)
    matrix = [[a+k,-a],[-a,a]]
    u,endj = affine(matrix,[0,t],{},[-a,a],0)
    _, spring_action = affine(matrix,[0,t],{},[-k,0],0)
    assert u == [t/k,t/k+t/a] and endj == t and spring_action == -t
    projected = list(map(float,u))
    reconstructed = Q(float(a)*(projected[1]-projected[0]))
    direct = Q(float(endj))
    assert abs((direct-t)/t) <= Q(1,10**9)
    assert abs((reconstructed-t)/t) > Q(1,10**9)
    records.append({'case':name,'a_hex':float(a).hex(),'exact_root':decimal(u[0]),
      'exact_twist':decimal(t/a),'projected_root':projected[0],'projected_tip':projected[1],
      'direct_functional_torque':float(endj),'torque_reconstructed_from_projected_u':float(reconstructed),
      'reconstructed_torque_relative_error':decimal((reconstructed-t)/t),
      'spring_action':float(spring_action),'free_equilibrium_reaction':'exact zero',
      'source_basis':'N05 diagnosis inferred f64 a reused as declared illustrative coefficient; no full N06 source capture','not_a_product_execution':True})
# Nonzero prescribed movement + explicit loads on both constrained/free rows.
k1,k2,ks=Q(7),Q(11),Q(1,1024)
k=[[k1,-k1,0],[-k1,k1+k2,-k2],[0,-k2,k2+ks]]
f=[Q(3),Q(-2),Q(5)]; d=Q(1,8)
u, endj=affine(k,f,{0:d},[0,-k2,k2],0)
r0=sum(k[0][j]*u[j] for j in range(3))-f[0]
_, fixed_end=affine(k,f,{0:d},[0,-k2,k2],Q(-2,7))
assert fixed_end==endj-Q(2,7)
assert r0+f[0]+f[1]+f[2]-ks*u[2]==0
records.append({'case':'prescribed-load-subtraction','u':list(map(str,u)),'constraint_reaction':str(r0),'member_end_j':str(endj),'member_after_fixed_end_subtraction':str(fixed_end)})
# One functional crossing two separately solved blocks, and fully prescribed state.
k=[[Q(2),0,0],[0,Q(3),Q(-1)],[0,Q(-1),Q(2)]]
u,q=affine(k,[1,2,3],{},[Q(1),Q(-2),Q(4)],Q(-5,9))
assert q==Q(-5,9)+u[0]-2*u[1]+4*u[2]
_, qfixed=affine(k,[1,2,3],{0:Q(1,3),1:Q(-1,7),2:Q(1,11)},[2,3,-5],Q(4))
records.append({'case':'cross-block-and-all-fixed','q':str(q),'all_fixed_q':str(qfixed)})
# Genuine tiny nonzero coupling must not be thresholded out of graph.
e=Q(1,2**80); coupled=[[Q(2),Q(-1),0],[Q(-1),Q(2),e],[0,e,Q(2)]]
assert list(map(len,blocks(coupled,[0,1,2])))==[3]
try: affine(coupled,[1,0,0],{},[1,0,0],0)
except AssertionError: pass
else: raise AssertionError('unsupported 3-block admitted')
# Signed permutation is exact source coordinate transport, not fixture recognition.
perm=[2,0,1]; signs=[-1,1,-1]
kp=[[signs[i]*signs[j]*k[perm[i]][perm[j]] for j in range(3)] for i in range(3)]
fp=[signs[i]*Q([1,2,3][perm[i]]) for i in range(3)]
up,_=affine(kp,fp,{},[0,0,0],0)
assert up==[signs[i]*u[perm[i]] for i in range(3)]
records.append({'case':'eligibility','tiny_coupling_block_orders':[3],'signed_permutation_passed':True})
print(json.dumps({'scope':'independent elementary design arithmetic; no implementation qualification', 'checks_passed':len(records),'records':records},indent=2))
