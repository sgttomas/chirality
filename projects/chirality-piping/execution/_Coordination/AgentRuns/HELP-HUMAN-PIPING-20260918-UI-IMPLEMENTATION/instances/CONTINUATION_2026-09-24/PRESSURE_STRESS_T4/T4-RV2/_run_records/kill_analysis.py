"""T4-RV2: K1 and K2 under a stable binary64 element (labelled emulations, emu64.py),
with K-D5's estimate emulated for the correct check, M31b (cos rounded to nearest and
one ulp low) and M31a. Reference u_int from rv2_lib (independent of T4-I6).
usage: python -I kill_analysis.py"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decimal import Decimal as D, getcontext, localcontext
from fractions import Fraction as Fr
import rv2_lib as L
import emu64 as M

getcontext().prec = 80
E, G, A, I, J = 2e11, 8e10, 0.005969026041820614, 2.700984283923829e-05, 5.401968567847658e-05
G30 = 2.0 ** -30


def grid(v):
    return round(v / G30) * G30


def radius_for(d, phi):
    with localcontext() as c:
        c.prec = 60
        Ld = L.vnorm([D(v) for v in d])
        s, _ = L.sincos(D(phi) / 2)
        return float(Ld / (2 * s))


def kint_exact(xi, xj, R, y, chord_local=None):
    """exact 12x12 of the intended element; chord_local (binary64 local chord) gives M31b's H."""
    r = L.curved_K(xi, xj, R, y, E, G, A, I, J, 1, 1, n=40)
    if chord_local is None:
        return r["K"]
    g = r["geo"]
    cg = [D(chord_local[0]) * g["u0"][k] + D(chord_local[1]) * g["v0"][k] + D(chord_local[2]) * g["z"][k] for k in range(3)]
    return L.curved_K(xi, xj, R, y, E, G, A, I, J, 1, 1, n=40, chord_override=cg)["K"]


def embed(K12):
    n = 12
    return [[K12[a][b] for b in range(n)] for a in range(n)]


springs = [(3, 1e6), (4, 1e6), (5, 1e6)]
free = [3, 4, 5, 6, 7, 8, 9, 10, 11]
f = [0.0] * 12
f[9] = f[10] = f[11] = 1.0

print("K1 family: N0 translations rigid, rotational springs 1e6, tip moment (1,1,1); k = 1; E 2e11, G 8e10, OD 0.2 t 0.01")
print("columns: product element / solver | actual (criterion units) | K-D5 trigger with: correct, M31b(cos RN), M31b(cos 1ulp low), M31a   [demotes iff trigger > 1]")
planes = {"IP": ([math.cos(math.pi / 6), math.sin(math.pi / 6), 0.0], [0.0, 1.0, 0.0]),
          "SK": ([1.0 / 3.0, 2.0 / 3.0, 2.0 / 3.0], [1.0, -1.0, 0.5])}
for plane, (dh, y) in planes.items():
    d = [grid(0.3 * v) for v in dh]
    for phi_nom in (1e-8, 1.5e-8, 2e-8, 3e-8, 5e-8, 1e-6, 1e-4, math.pi / 36):
        R = radius_for(d, phi_nom)
        for X in ((0.0, 5e6) if (plane == "IP" and phi_nom == 1e-8) else (0.0,)):
            xi = [X, 0.7 * X, 0.0]
            xj = [xi[k] + d[k] for k in range(3)]
            assert all(xj[k] - xi[k] == d[k] for k in range(3))
            nodes = [xi, xj]
            Kc = kint_exact(xi, xj, R, y)
            # reference solve
            Kref = [[Kc[a][b] for b in range(12)] for a in range(12)]
            for dd, v in springs:
                Kref[dd][dd] += D(v)
            uref = dict(zip(free, L.lu_solve_dec([[Kref[a][b] for b in free] for a in free], [D(f[a]) for a in free])))
            gb = M.geometry_b64(d, R, y)
            cos_b = math.cos(gb["phi"])
            ch_rn = [R * (cos_b - 1.0), R * math.sin(gb["phi"]), 0.0]
            ch_lo = [R * ((1.0 - 2.0 ** -53 if cos_b == 1.0 else cos_b) - 1.0), R * math.sin(gb["phi"]), 0.0]
            K31b_rn = kint_exact(xi, xj, R, y, ch_rn)
            K31b_lo = kint_exact(xi, xj, R, y, ch_lo)
            print("-- K1-%s phi_nom %.3g  X %.0f  R %.17g  phi_b %.17g  fl(cos phi_b) = %r" % (plane, phi_nom, X, R, gb["phi"], cos_b))
            for pname, Fm, chord in (("correct/GL", "GL", "actual"), ("correct/CR", "CR", "actual"),
                                     ("mutant RN/GL (K2 system)", "GL", "formula_cr"), ("mutant lo/GL", "GL", "formula_lo")):
                Kb, _, _ = M.element_b64(d, R, y, E, G, A, I, J, 1.0, 1.0, F_mode=Fm, chord=chord)
                Kg = M.assemble(2, [(0, 1, Kb)], springs)
                K31a = [[D(v) for v in row] for row in Kb]
                for solver in ("LU", "LLT"):
                    ub, fac = M.solve_model(Kg, f, free, solver)
                    act, at = M.actual_ratio(uref, ub, nodes)
                    trig = []
                    for Ki in (Kc, K31b_rn, K31b_lo, K31a):
                        t, _ = M.kd5_trigger(Ki, springs, f, ub, free, fac, nodes)
                        trig.append(t)
                    print("   %-26s %-3s actual %9.3e   triggers: correct %9.3e  M31b-RN %9.3e  M31b-lo %9.3e  M31a %9.3e" % (pname, solver, act, *trig))
