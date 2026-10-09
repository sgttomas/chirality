"""T4-RV2: is there a conditioning-driven K-D5 true positive for a curved model once the
element is objective and stably formed? CSKEW-type cantilever (R5_4 / KM CSKEW_8_5:
nodes (0,0,0)-(0.3,0,0.3), R 0.3, y (1/3,-4/3,-1/3), N0 translations rigid, springs
(k_X, 1e6, 1e6), tip rx load k_X*1e-6), k_X swept across the Passed band.
Labelled emulation (emu64's GL element, LU and Cholesky); K-D5 with the exact K_int.
usage: python -I cond_tp.py"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decimal import Decimal as D, getcontext
import rv2_lib as L
import emu64 as M

getcontext().prec = 60
E, G, A, I, J = 2e11, 8e10, 0.005969026041820614, 2.700984283923829e-05, 5.401968567847658e-05
xi, xj = [0.0, 0.0, 0.0], [0.3, 0.0, 0.3]
y = [0.3333333333333333, -1.3333333333333333, -0.3333333333333333]
d = [0.3, 0.0, 0.3]
Kex = L.curved_K(xi, xj, 0.3, y, E, G, A, I, J, 1, 1, n=40)["K"]
free = [3, 4, 5, 6, 7, 8, 9, 10, 11]
elems = {}
for Fm in ("GL", "CR"):
    elems[Fm] = M.element_b64(d, 0.3, y, E, G, A, I, J, 1.0, 1.0, F_mode=Fm, chord="actual")[0]


def cond1(Kf, equilibrate):
    n = len(Kf)
    if equilibrate:
        s = [abs(Kf[i][i]).sqrt() for i in range(n)]
        Kf = [[Kf[i][j] / (s[i] * s[j]) for j in range(n)] for i in range(n)]
    Ki = L.gauss_jordan_inverse(Kf)
    n1 = max(sum(abs(Kf[i][j]) for i in range(n)) for j in range(n))
    n2 = max(sum(abs(Ki[i][j]) for i in range(n)) for j in range(n))
    return float(n1 * n2)


print("k_X   cond1(raw)  cond1(equil)   | element/solver: actual, trigger(exact K_int)")
for kx in (10.0, 9.0, 8.5, 8.0, 7.0, 6.0, 5.0):
    springs = [(3, kx), (4, 1e6), (5, 1e6)]
    f = [0.0] * 12
    f[9] = kx * 1e-6
    Kr = [[Kex[a][b] for b in range(12)] for a in range(12)]
    for dd, v in springs:
        Kr[dd][dd] += D(v)
    Kf = [[Kr[a][b] for b in free] for a in free]
    uref = dict(zip(free, L.lu_solve_dec(Kf, [D(f[a]) for a in free])))
    line = "%-5g %10.2e  %10.2e   |" % (kx, cond1(Kf, False), cond1(Kf, True))
    for Fm in ("GL", "CR"):
        Kg = M.assemble(2, [(0, 1, elems[Fm])], springs)
        for solver in ("LU", "LLT"):
            ub, fac = M.solve_model(Kg, f, free, solver)
            act, _ = M.actual_ratio(uref, ub, [xi, xj])
            t, _ = M.kd5_trigger(Kex, springs, f, ub, free, fac, [xi, xj])
            line += "  %s/%s %.2f,%.2f" % (Fm, solver, act, t)
    print(line)
