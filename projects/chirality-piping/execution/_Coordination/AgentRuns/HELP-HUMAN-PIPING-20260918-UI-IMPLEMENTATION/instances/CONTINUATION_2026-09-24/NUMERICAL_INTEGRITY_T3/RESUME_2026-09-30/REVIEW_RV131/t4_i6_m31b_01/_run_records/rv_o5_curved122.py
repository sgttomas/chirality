"""RV131 O5 probe: the 122 mechanism with a realized bend. F122's supports and loads (kd5_models.rs F122:
nodes (0,0,0),(1,2,2); N0 translations rigid; springs (3,144),(4,1e6),(5,1e6); tip loads (9,.0048),(10,.0096),(11,.0096)),
its straight member replaced by a B1 bend (RV131 element) of radius R and plane reference y. Reports crK (correctly
rounded element entries, exact solve; the floor-type estimate T4-I6 uses) and the exact equilibrated 1-norm condition
of the reduced matrix, against F122's own (straight frame: crK 0.64, product actual 2.43 dense / 1.21 sparse).
Not a product run.
usage: python -I rv_o5_curved122.py"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decimal import Decimal as D, getcontext
import rv_element as RV
getcontext().prec = 60
S = dict(E=200000000000.0, G=80000000000.0, A=0.005969026041820614, I=2.700984283923829e-05, J=5.401968567847658e-05)
rigid = [0, 1, 2]; loads = [(9, 0.0048), (10, 0.0096), (11, 0.0096)]
def reduced(K, springs):
    free = [q for q in range(12) if q not in rigid]
    Kf = [[K[a][b] for b in free] for a in free]
    for dof, v in springs:
        Kf[free.index(dof)][free.index(dof)] += D(v)
    return Kf, free
def solve(K, springs):
    Kf, free = reduced(K, springs)
    f = [D(0)] * len(free)
    for dof, v in loads:
        f[free.index(dof)] += D(v)
    return dict(zip(free, RV.m_solve(Kf, f))), Kf
def cond1(Kf):
    dsc = [abs(Kf[i][i]).sqrt() for i in range(len(Kf))]
    Ks = [[Kf[i][j] / (dsc[i] * dsc[j]) for j in range(len(Kf))] for i in range(len(Kf))]
    Ki = RV.m_inv(Ks)
    n1 = max(sum(abs(Ks[i][j]) for i in range(len(Ks))) for j in range(len(Ks)))
    return n1 * max(sum(abs(Ki[i][j]) for i in range(len(Ki))) for j in range(len(Ki)))
d = [1.0, 2.0, 2.0]
for R in (1.6, 3.0, 10.0, 100.0):
    for y in ([1.0, 0.0, 0.0], [0.0, 1.0, -1.0]):
        for kx in (144.0,):
            K, geo, _ = RV.element_global(d, R, y, S["E"], S["G"], S["A"], S["I"], S["J"], 1.0, 1.0)
            springs = [(3, kx), (4, 1e6), (5, 1e6)]
            u, Kf = solve(K, springs)
            ucr, _ = solve([[D(float(v)) for v in row] for row in K], springs)
            print("R %-6g y %-16s k_X %-6g phi %.4f  cond1_eq %.2e  crK %.3e" % (R, y, kx, float(geo["phi"]), float(cond1(Kf)), float(RV.actual_ratio(u, ucr, geo["L"]))))

if len(sys.argv) > 1:
    sys.path.insert(1, sys.argv[1])
    import curved_ref as C
    Kf122 = C.frame_element([0.0, 0, 0], d, [1.0, 0.0, 0.0], S["E"], S["G"], S["A"], S["I"], S["I"], S["J"])
    u, Kf = solve(Kf122, [(3, 144.0), (4, 1e6), (5, 1e6)])
    ucr, _ = solve([[D(float(v)) for v in row] for row in Kf122], [(3, 144.0), (4, 1e6), (5, 1e6)])
    print("F122 straight (T4-I6 curved_ref.frame_element, labelled cross-check): cond1_eq %.2e  crK %.3e" % (float(cond1(Kf)), float(RV.actual_ratio(u, ucr, D(3)))))
