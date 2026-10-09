"""T4-RV2: does K-D5's closed-form re-formation at p ~ 128 bits (emulated by Decimal at
38 and 39 digits; B1's Gram and action table) move the trigger on K1 (statically
determinate in its element) or on an indeterminate small-angle model? Labelled emulation.
usage: python -I o4_check.py"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decimal import Decimal as D, getcontext, localcontext
import rv2_lib as L
import emu64 as M

getcontext().prec = 80
E, G, A, I, J = 2e11, 8e10, 0.005969026041820614, 2.700984283923829e-05, 5.401968567847658e-05
G30 = 2.0 ** -30


def closed_form_K(xi, xj, R, y, prec):
    """B1's closed form (Gram + action table) at `prec` digits, H from A.d, global by A."""
    with localcontext() as c:
        c.prec = prec
        xi = [D(v) for v in xi]; xj = [D(v) for v in xj]; y = [D(v) for v in y]; R = D(R)
        d = [xj[k] - xi[k] for k in range(3)]
        Lc = (d[0] * d[0] + d[1] * d[1] + d[2] * d[2]).sqrt()
        s = Lc / (2 * R)
        ch = ((2 * R - Lc) * (2 * R + Lc)).sqrt() / (2 * R)
        half = L.angle_newton(s, ch)
        half = +half
        phi = 2 * half
        sp, cp = 2 * s * ch, 1 - 2 * s * s
        s2 = 2 * sp * cp
        Gm = [[phi, sp, 1 - cp], [sp, phi / 2 + s2 / 4, sp * sp / 2], [1 - cp, sp * sp / 2, phi / 2 - s2 / 4]]
        z3 = (D(0), D(0), D(0))
        acts = [((0, 0, -1), (-R * sp, 0, R), z3, z3), ((0, 1, 0), (R * cp, -R, 0), z3, z3),
                (z3, z3, (0, R * sp, -R * cp), (R, -R * cp, -R * sp)), (z3, z3, (0, 1, 0), (0, 0, -1)),
                (z3, z3, (0, 0, 1), (0, 1, 0)), (z3, (1, 0, 0), z3, z3)]  # (N, Mip, Mop, T)
        EI, GJ, EA = D(E) * D(I), D(G) * D(J), D(E) * D(A)

        def q(u, v):
            return sum((D(u[i]) * Gm[i][j] * D(v[j]) for i in range(3) for j in range(3)), D(0))
        F = [[R * (q(acts[a][1], acts[b][1]) / EI + q(acts[a][2], acts[b][2]) / EI + q(acts[a][3], acts[b][3]) / GJ + q(acts[a][0], acts[b][0]) / EA) for b in range(6)] for a in range(6)]
        Kt = L.gauss_jordan_inverse(F)
        dh = [v / Lc for v in d]
        yd = sum(y[k] * dh[k] for k in range(3))
        nr = [y[k] - yd * dh[k] for k in range(3)]
        nn = (nr[0] ** 2 + nr[1] ** 2 + nr[2] ** 2).sqrt()
        n = [v / nn for v in nr]
        ex = [-s * dh[k] + ch * n[k] for k in range(3)]
        ey = [ch * dh[k] + s * n[k] for k in range(3)]
        ez = [n[1] * dh[2] - n[2] * dh[1], n[2] * dh[0] - n[0] * dh[2], n[0] * dh[1] - n[1] * dh[0]]
        Ax = [ex, ey, ez]
        cl = [sum(Ax[a][k] * d[k] for k in range(3)) for a in range(3)]
        H = [[D(1) if i == j else D(0) for j in range(6)] for i in range(6)]
        H[3][1], H[3][2], H[4][0], H[4][2], H[5][0], H[5][1] = -cl[2], cl[1], cl[2], -cl[0], -cl[1], cl[0]
        HK = [[sum((H[i][k] * Kt[k][j] for k in range(6)), D(0)) for j in range(6)] for i in range(6)]
        HKHt = [[sum((HK[i][k] * H[j][k] for k in range(6)), D(0)) for j in range(6)] for i in range(6)]
        Kl = [[D(0)] * 12 for _ in range(12)]
        for i in range(6):
            for j in range(6):
                Kl[i][j] = HKHt[i][j]; Kl[i][j + 6] = -HK[i][j]; Kl[i + 6][j] = -HK[j][i]; Kl[i + 6][j + 6] = Kt[i][j]
        T = [[D(0)] * 12 for _ in range(12)]
        for b in range(4):
            for i in range(3):
                for j in range(3):
                    T[3 * b + i][3 * b + j] = Ax[i][j]
        TK = [[sum((T[k][i] * Kl[k][j] for k in range(12)), D(0)) for j in range(12)] for i in range(12)]
        return [[sum((TK[i][k] * T[k][j] for k in range(12)), D(0)) for j in range(12)] for i in range(12)]


def run(label, d, R, y, rigid, springs, loads):
    xi = [0.0, 0.0, 0.0]
    xj = list(d)
    nodes = [xi, xj]
    free = [i for i in range(12) if i not in rigid]
    f = [0.0] * 12
    for k, v in loads:
        f[k] = v
    Kex = L.curved_K(xi, xj, R, y, E, G, A, I, J, 1, 1, n=40)["K"]
    Kref = [[Kex[a][b] for b in range(12)] for a in range(12)]
    for dd, v in springs:
        Kref[dd][dd] += D(v)
    uref = dict(zip(free, L.lu_solve_dec([[Kref[a][b] for b in free] for a in free], [D(f[a]) for a in free])))
    Kb, gb, _ = M.element_b64(d, R, y, E, G, A, I, J, 1.0, 1.0, F_mode="GL", chord="actual")
    Kg = M.assemble(2, [(0, 1, Kb)], springs)
    ub, fac = M.solve_model(Kg, f, free, "LU")
    act, _ = M.actual_ratio(uref, ub, nodes)
    out = ["%-34s phi %.1e  actual %.2e" % (label, gb["phi"], act)]
    t_ex, _ = M.kd5_trigger(Kex, springs, f, ub, free, fac, nodes)
    out.append("trigger exact K_int %.2e" % t_ex)
    for p in (38, 39):
        Kp = closed_form_K(xi, xj, R, y, p)
        rel = max(abs(Kp[a][b] - Kex[a][b]) for a in range(12) for b in range(12)) / L.maxabs(Kex)
        t_p, _ = M.kd5_trigger(Kp, springs, f, ub, free, fac, nodes)
        out.append("p%d: max|dK|/max|K| %.1e trigger %.2e" % (p, float(rel), t_p))
    print("  ".join(out))


def grid(v):
    return round(v / G30) * G30


def radius_for(d, phi):
    with localcontext() as c:
        c.prec = 60
        Ld = L.vnorm([D(v) for v in d])
        s, _ = L.sincos(D(phi) / 2)
        return float(Ld / (2 * s))


dh, y = [math.cos(math.pi / 6), math.sin(math.pi / 6), 0.0], [0.0, 1.0, 0.0]
d = [grid(0.3 * v) for v in dh]
k1 = dict(rigid=[0, 1, 2], springs=[(3, 1e6), (4, 1e6), (5, 1e6)], loads=[(9, 1.0), (10, 1.0), (11, 1.0)])
ind = dict(rigid=[0, 1, 2, 3, 4, 5], springs=[(6, 2.4e9), (7, 2.4e9), (8, 2.4e9), (9, 1e7), (10, 1e7), (11, 1e7)],
           loads=[(6, 1.0), (7, 1.0), (8, 1.0), (9, 1.0), (10, 1.0), (11, 1.0)])
for phi in (1e-9, 3e-9, 1e-8, 1e-6, 1e-4):
    R = radius_for(d, phi)
    run("K1 (determinate) phi_nom %.0e" % phi, d, R, y, **k1)
    run("indeterminate (tip springs) %.0e" % phi, d, R, y, **ind)
