"""RV131 K2 emulation (U1_REFERENCE.md B5.1 'Kernel-level kill K2'): the system matrix is K1's element with the
binary64 formula chord in H (exact tip stiffness, rounded once to binary64 -- i.e. built independently of any binary64
small-angle evaluation); u is the exact solution of that binary64 system rounded to binary64 (an ideal solve).
K-D5 variants at p = 128: correct (actual chord), M31b (binary64 formula chord), M31b0 (formula at p), M31a (K_int = the
system's own element matrix).
usage: python -I rv_k2_emulation.py"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from decimal import Decimal as D, getcontext
import rv_element as RV
import rv_wide as W
from rv_o4_kd5_emulation import kd5_with_chord, FREE, LOAD, scales
getcontext().prec = 70
S = RV.SECTION

def trig(Kint_el, u_b64, Kfree_ref, L_b):
    rho = []
    for a in FREE:
        acc = Fr(LOAD.get(a, 0.0))
        for b in range(12):
            if u_b64[b] != 0.0:
                acc -= Kint_el[a][b] * Fr(u_b64[b])
        if a in (3, 4, 5):
            acc -= Fr(1.0e6) * Fr(u_b64[a])
        rho.append(D(acc.numerator) / D(acc.denominator))
    w = RV.m_solve(Kfree_ref, rho)
    tr, ro = scales(u_b64, L_b)
    return max(float(2 * abs(w[i]) / (D("1e-9") * D(max(abs(u_b64[a]), ro if a % 6 >= 3 else tr)))) for i, a in enumerate(FREE))

for plane, d, R, y in (("IP", [0.25980762112885714, 0.15000000037252903, 0.0], 30000000.018065747, [0.0, 1.0, 0.0]),
                       ("SK", [0.09999999962747097, 0.20000000018626451, 0.20000000018626451], 30000000.012417633, [1.0, -1.0, 0.5])):
    L64 = math.sqrt(sum(v * v for v in d)); phib = 2.0 * math.asin(L64 / (2.0 * R))
    cl = [R * (math.cos(phib) - 1.0), R * math.sin(phib), 0.0]
    Kex, geo, _ = RV.element_global(d, R, y, S["E"], S["G"], S["A"], S["I"], S["J"], 1.0, 1.0)
    ax = RV.b1_axes(geo)
    cg = [sum(D(cl[a]) * ax[a][q] for a in range(3)) for q in range(3)]
    Kmut, _, _ = RV.element_global(d, R, y, S["E"], S["G"], S["A"], S["I"], S["J"], 1.0, 1.0, chord_global=cg)
    Ksys = [[float(v) for v in row] for row in Kmut]           # the K2 system element, rounded once
    Kf = [[D(Ksys[a][b]) for b in FREE] for a in FREE]
    for k in range(3):
        Kf[k][k] += D(1.0e6)
    usol = RV.m_solve(Kf, [D(LOAD.get(a, 0.0)) for a in FREE])
    u_b64 = [0.0] * 12
    for a, v in zip(FREE, usol):
        u_b64[a] = float(v)
    L_b = float(geo["L"])
    ar = W.P(128)
    Kc, _ = W.kd5_curved_at_p(ar, [0.0] * 3, d, R, y, S["E"], S["G"], S["A"], S["I"], S["J"], 1.0, 1.0, "closed", "actual")
    K0, _ = W.kd5_curved_at_p(ar, [0.0] * 3, d, R, y, S["E"], S["G"], S["A"], S["I"], S["J"], 1.0, 1.0, "closed", "formula_p")
    Kb, _ = kd5_with_chord(ar, [0.0] * 3, d, R, y, "closed", cl)
    Ka = [[Fr(v) for v in row] for row in Ksys]
    print("%s K2: correct %.3f | M31b %.3e | M31b0 %.3f | M31a (K_int = system element) %.3e" % (
        plane, trig(Kc, u_b64, Kf, L_b), trig(Kb, u_b64, Kf, L_b), trig(K0, u_b64, Kf, L_b), trig(Ka, u_b64, Kf, L_b)))
