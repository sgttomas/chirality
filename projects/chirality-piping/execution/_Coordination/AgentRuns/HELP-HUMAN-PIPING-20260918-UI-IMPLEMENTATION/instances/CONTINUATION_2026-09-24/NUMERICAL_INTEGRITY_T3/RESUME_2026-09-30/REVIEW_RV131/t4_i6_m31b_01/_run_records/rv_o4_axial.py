"""RV131 O4 attack: K-D5's closed-form error at p = 128 on a rigidly rooted, axially loaded,
nearly straight bend (the load direction where the F_xy coupling error is not masked by S*).
N0 fully fixed; N1 free; unit force at N1 along the chord. Ideal product (u exact, rounded to binary64).
usage: python -I rv_o4_axial.py"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from decimal import Decimal as D, getcontext, localcontext
import rv_element as RV
import rv_wide as W
getcontext().prec = 70
S = RV.SECTION
g30 = 2.0 ** -30
def gr(v): return round(v / g30) * g30
FREE = [6, 7, 8, 9, 10, 11]

def run(Lnom, phi, load_kind, variant, p=128):
    dh = [math.cos(math.pi / 6), math.sin(math.pi / 6), 0.0]
    y = [0.0, 1.0, 0.0]
    d = [gr(Lnom * c) for c in dh]
    with localcontext() as c:
        c.prec = 60
        L = RV.v_norm([D(v) for v in d]); s_, _ = RV.d_sincos(D(phi) / 2)
        R = float(L / (2 * s_))
    Kex, geo, _ = RV.element_global(d, R, y, S["E"], S["G"], S["A"], S["I"], S["J"], 1.0, 1.0)
    Kf = [[Kex[a][b] for b in FREE] for a in FREE]
    Lf = float(geo["L"])
    if load_kind == "axial":
        f = {6: d[0] / Lf, 7: d[1] / Lf, 8: d[2] / Lf}
    elif load_kind == "transverse":
        n = [float(v) for v in geo["n"]]
        f = {6: n[0], 7: n[1], 8: n[2]}
    elif load_kind == "moment111":
        f = {9: 1.0, 10: 1.0, 11: 1.0}
    u = RV.m_solve(Kf, [D(f.get(a, 0.0)) for a in FREE])
    ub = [0.0] * 12
    for a, v in zip(FREE, u):
        ub[a] = float(v)
    Kp, _ = W.kd5_curved_at_p(W.P(p), [0.0] * 3, d, R, y, S["E"], S["G"], S["A"], S["I"], S["J"], 1.0, 1.0, variant, "actual")
    rho = []
    for a in FREE:
        acc = Fr(f.get(a, 0.0))
        for b in FREE:
            acc -= Kp[a][b] * Fr(ub[b])
        rho.append(D(acc.numerator) / D(acc.denominator))
    w = RV.m_solve(Kf, rho)
    st = max(abs(ub[a]) for a in FREE if a % 6 < 3)
    sr = max(abs(ub[a]) for a in FREE if a % 6 >= 3)
    tr, ro = max(st, Lf * sr), max(sr, st / Lf)
    worst = (0.0, None)
    for i, a in enumerate(FREE):
        sc = max(abs(ub[a]), ro if a % 6 >= 3 else tr)
        t = float(2 * abs(w[i]) / (D("1e-9") * D(sc)))
        if t > worst[0]:
            worst = (t, a)
    return R, worst

for Lnom in (0.3, 3.0, 30.0):
    for phi in (1e-9, 2e-9, 5e-9, 1e-8, 1e-7):
        for load in ("axial", "transverse", "moment111"):
            line = []
            for variant, p in (("closed", 128), ("stable", 128), ("closed", 192)):
                R, (t, at) = run(Lnom, phi, load, variant, p)
                line.append("%s p%d trig %.3e%s" % (variant, p, t, " DEMOTES" if t > 1 else ""))
            print("L %-5g phi %-6g R %.3e %-10s | %s" % (Lnom, phi, R, load, " | ".join(line)))
