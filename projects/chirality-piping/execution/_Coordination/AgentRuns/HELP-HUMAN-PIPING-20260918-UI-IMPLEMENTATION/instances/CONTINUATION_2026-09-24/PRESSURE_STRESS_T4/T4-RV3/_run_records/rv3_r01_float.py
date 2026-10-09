"""T4-RV3 addendum 01: indicative binary64 noise against the floors of T4-I7's round-01 file, now
including the chord_frame_elastic rows (elastic K(d - u_free) - p_w in the chord frame) and the new PTW cases.
(Copy of rv3_float_noise.py with those additions.)

Original description:

A naive binary64 direct-stiffness emulation of the H-2 product path (straights: EB frame stiffness and
Poisson pairs; arcs: tip flexibility rounded to binary64, inverted in binary64, assembled by rigid
transfer; bend term K_b u_free(eps_p) - c_b; caps at transferring terminals; Gaussian elimination with
partial pivoting in binary64; elastic recovery N_w = N_el + pAi on arcs).  It is not the product: the
product's exact sums and scaled formation should be at least as accurate.  It reports, per case, the
largest |emulated - reference| / absolute_floor over the groups the floors protect, so a ratio well
below 1 says the floor is not tight against plain binary64 rounding.

    python -I -B rv3_r01_float.py <round-01 u2_reference_cases.json>
"""
import json
import os
import sys
from decimal import Decimal as D

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv3_lib as L  # noqa: E402
import rv3_solve as S  # noqa: E402
from rv3_lib import ZERO, ONE  # noqa: E402


def fl(x):
    return float(x)


def cross_mat(d):
    return [[0.0, -d[2], d[1]], [d[2], 0.0, -d[0]], [-d[1], d[0], 0.0]]


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def tr(A):
    return [list(r) for r in zip(*A)]


def inv(A):
    n = len(A)
    M = [list(A[i]) + [1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c]))
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0.0:
                f = M[r][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return [row[n:] for row in M]


def gsolve(A, b):
    n = len(b)
    M = [list(A[i]) + [b[i]] for i in range(n)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c]))
        M[c], M[p] = M[p], M[c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            if f != 0.0:
                M[r] = [a - f * bb for a, bb in zip(M[r], M[c])]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        x[r] = (M[r][n] - sum(M[r][k] * x[k] for k in range(r + 1, n))) / M[r][r]
    return x


def arc_tip_flexibility_global(case, mem):
    """6x6 global flexibility of node j (authored) with authored i clamped, from the exact transfer
    matrix of rv3_lib (Decimal), returned in binary64."""
    sec, mat = case.sec, case.mat
    A = mem.system_matrix(sec, mat, ZERO, ZERO, ZERO, wall=False)
    save = mem.forward
    mem.set_traversal(True)
    E = L.expm(A, mem.L)
    fr0, fr1 = mem.frame0, mem.frame_at(mem.L)
    mem.set_traversal(save)
    # columns: unit global tip action (f, m) at j -> start action (F0, M0) local -> tip motion global
    EFF = [[E[r][c] for c in range(6)] for r in range(6)]
    EuF = [[E[6 + r][c] for c in range(6)] for r in range(6)]
    EFFi = [L.solve(EFF, [ONE if i == j else ZERO for i in range(6)]) for j in range(6)]
    EFFi = [[EFFi[j][i] for j in range(6)] for i in range(6)]  # inverse
    Fl = L.matmul(EuF, EFFi)  # local(end) tip action -> local(end) tip motion ... frames below
    # tip action given in end frame comps; motion out in end frame comps (u, theta blocks)
    R1 = [list(e) for e in fr1]  # rows: t, n, b in global

    def blk(Rrows):
        out = [[ZERO] * 6 for _ in range(6)]
        for b in range(2):
            for i in range(3):
                for j in range(3):
                    out[3 * b + i][3 * b + j] = Rrows[i][j]
        return out
    G = blk(R1)  # global -> local comps
    Gt = [list(r) for r in zip(*G)]
    Fg = L.matmul(Gt, L.matmul(Fl, G))
    return [[fl(x) for x in row] for row in Fg]


def straight_K_global(case, mem):
    sec, mat = case.sec, case.mat
    Lm = fl(mem.L)
    EA, GJ, EI = fl(mat.E * sec.As), fl(mat.G * sec.J), fl(mat.E * sec.I)
    k = [[0.0] * 12 for _ in range(12)]

    def s(i, j, v):
        k[i][j] += v
    a = EA / Lm
    t = GJ / Lm
    b12, b6, b4, b2 = 12 * EI / Lm ** 3, 6 * EI / Lm ** 2, 4 * EI / Lm, 2 * EI / Lm
    for (i, j, v) in [(0, 0, a), (0, 6, -a), (6, 6, a), (3, 3, t), (3, 9, -t), (9, 9, t),
                      (1, 1, b12), (1, 5, b6), (1, 7, -b12), (1, 11, b6), (5, 5, b4), (5, 7, -b6), (5, 11, b2),
                      (7, 7, b12), (7, 11, -b6), (11, 11, b4),
                      (2, 2, b12), (2, 4, -b6), (2, 8, -b12), (2, 10, -b6), (4, 4, b4), (4, 8, b6), (4, 10, b2),
                      (8, 8, b12), (8, 10, b6), (10, 10, b4)]:
        s(i, j, v)
        if i != j:
            s(j, i, v)
    R = [[fl(x) for x in e] for e in mem.chord_frame]  # rows local axes in global
    T = [[0.0] * 12 for _ in range(12)]
    for b in range(4):
        for i in range(3):
            for j in range(3):
                T[3 * b + i][3 * b + j] = R[i][j]
    return mm(tr(T), mm(k, T)), T, k


def arc_K_global(Fg, xi, xj):
    Kjj = inv(Fg)
    d = [xj[i] - xi[i] for i in range(3)]
    dx = cross_mat(d)
    G = [[1.0 if i == j else 0.0 for j in range(6)] for i in range(6)]
    for i in range(3):
        for j in range(3):
            G[i][3 + j] = -dx[i][j]
    Gt = tr(G)
    KiI = mm(Gt, mm(Kjj, G))
    Kij = [[-x for x in r] for r in mm(Gt, Kjj)]
    Kji = [[-x for x in r] for r in mm(Kjj, G)]
    K = [[0.0] * 12 for _ in range(12)]
    for i in range(6):
        for j in range(6):
            K[i][j], K[i][6 + j], K[6 + i][j], K[6 + i][6 + j] = KiI[i][j], Kij[i][j], Kji[i][j], Kjj[i][j]
    return K


def straight_weight_peq(case, mem):
    """binary64 consistent nodal loads of the uniform self-weight on a straight (global)."""
    w = fl(case.w)
    if w == 0.0:
        return [0.0] * 12
    R = [[fl(x) for x in e] for e in mem.chord_frame]
    q = [w * R[a][2] * -1.0 for a in range(3)]  # local comps of w*(0,0,-1)
    Lm = fl(mem.L)
    loc = [q[0] * Lm / 2, q[1] * Lm / 2, q[2] * Lm / 2, 0.0, -q[2] * Lm * Lm / 12, q[1] * Lm * Lm / 12,
           q[0] * Lm / 2, q[1] * Lm / 2, q[2] * Lm / 2, 0.0, q[2] * Lm * Lm / 12, -q[1] * Lm * Lm / 12]
    out = []
    for b in range(4):
        blk = loc[3 * b:3 * b + 3]
        out += [sum(R[a][i] * blk[a] for a in range(3)) for i in range(3)]
    return out


_ARCW = {}


def arc_weight_peq(case, mem):
    """consistent nodal loads of the self-weight on an arc, clamped-clamped by the exact transfer matrix
    (Decimal), rounded to binary64; order [authored i; authored j], global."""
    key = id(mem)
    if key in _ARCW:
        return _ARCW[key]
    if case.w == 0:
        _ARCW[key] = [0.0] * 12
        return _ARCW[key]
    save = mem.forward
    mem.set_traversal(True)
    A = mem.system_matrix(case.sec, case.mat, case.w, ZERO, ZERO, wall=False)
    E = L.expm(A, mem.L)
    fr0, fr1 = mem.frame0, mem.frame_at(mem.L)
    g0 = L.to_local(fr0, L.gdir_global())
    yp = [ZERO] * 12 + list(g0) + [ONE]
    ypL = L.matvec(E, yp)
    Amat = [[E[6 + r][k] for k in range(6)] for r in range(6)]
    cvec = L.solve(Amat, [-ypL[6 + r] for r in range(6)])
    y0 = yp[:]
    for k in range(6):
        y0[k] += cvec[k]
    yL = L.matvec(E, y0)
    F0, M0 = L.to_global(fr0, y0[0:3]), L.to_global(fr0, y0[3:6])
    FL, ML = L.to_global(fr1, yL[0:3]), L.to_global(fr1, yL[3:6])
    mem.set_traversal(save)
    out = [fl(x) for x in list(F0) + list(M0)] + [-fl(x) for x in list(FL) + list(ML)]
    _ARCW[key] = out
    return out


def emulate(case_json):
    _ARCW.clear()
    c = S.Case(case_json["inputs"]).solve()
    ref = case_json["expected"]
    floors = {g: float(v["absolute_floor"]) for g, v in case_json["zero_scale"].items()}
    nodes = c.order
    idx = {n: i for i, n in enumerate(nodes)}
    ndof = 6 * len(nodes)
    K = [[0.0] * ndof for _ in range(ndof)]
    f = [0.0] * ndof
    P = fl(c.P)
    xs = {n: [fl(x) for x in c.coords[n]] for n in nodes}
    eps_p = fl((1 - 2 * c.mat.nu) * c.P / (c.mat.E * c.sec.As))
    eps_nu = fl(c.eps_nu)
    eps_th = fl(c.eps_th)
    elem = []
    for m in c.mems:
        i, j = idx[m.a_from], idx[m.a_to]
        xi, xj = xs[m.a_from], xs[m.a_to]
        if m.kind == "straight":
            Kg, T, kl = straight_K_global(c, m)
            ex = [fl(x) for x in m.chord_frame[0]]
            EA = fl(c.mat.E * c.sec.As)
            e0 = eps_nu + eps_th
            pe = [-EA * e0 * e for e in ex] + [0.0] * 3 + [EA * e0 * e for e in ex] + [0.0] * 3
            pw = straight_weight_peq(c, m)
            pe = [pe[r] + pw[r] for r in range(12)]
            uf = None
        else:
            Kg = arc_K_global(arc_tip_flexibility_global(c, m), xi, xj)
            d = [xj[q] - xi[q] for q in range(3)]
            uf = [0.0] * 6 + [(eps_p + eps_th) * x for x in d] + [0.0] * 3
            Kuf = [sum(Kg[r][q] * uf[q] for q in range(12)) for r in range(12)]
            ti = [fl(x) for x in m.authored_frame(D(0))[0]]
            tj = [fl(x) for x in m.authored_frame(D(1))[0]]
            cb = [-P * x for x in ti] + [0.0] * 3 + [P * x for x in tj] + [0.0] * 3
            pw = arc_weight_peq(c, m)
            pe = [Kuf[r] - cb[r] + pw[r] for r in range(12)]
        dofs = list(range(6 * i, 6 * i + 6)) + list(range(6 * j, 6 * j + 6))
        for r in range(12):
            f[dofs[r]] += pe[r]
            for q in range(12):
                K[dofs[r]][dofs[q]] += Kg[r][q]
        elem.append((m, Kg, pe, uf, dofs))
    # caps and remainders
    for i, loads in c.pts.items():
        for v in loads:
            for q in range(3):
                f[6 * i + q] += fl(v[q])
    fixed = set(range(6))
    if c.anchorD:
        fixed |= set(range(ndof - 6, ndof))
    free = [q for q in range(ndof) if q not in fixed]
    Kr = [[K[a][b] for b in free] for a in free]
    fr = [f[a] for a in free]
    ur = gsolve(Kr, fr)
    u = [0.0] * ndof
    for a, val in zip(free, ur):
        u[a] = val
    worst = {}

    def note(group, val, refv):
        fl_ = floors[group]
        r = abs(val - float(refv)) / fl_
        if r > worst.get(group, (0.0,))[0]:
            worst[group] = (r, val, refv)
    for n in nodes:
        for q, key in enumerate(["ux", "uy", "uz", "rx", "ry", "rz"]):
            note("displacement" if q < 3 else "rotation", u[6 * idx[n] + q], ref["nodes"][n][key])
    # reactions at A (and D): support-on-pipe = K u - f restricted, sign: R = K u - f_applied
    for sid, base in (("support:A", 0), ("support:D", ndof - 6)):
        if sid == "support:D" and not c.anchorD:
            continue
        for q, key in enumerate(["Fx", "Fy", "Fz", "Mx", "My", "Mz"]):
            val = sum(K[base + q][b] * u[b] for b in range(ndof)) - f[base + q]
            note(("support_force" if q < 3 else "support_moment") + "@" + sid, val, ref["supports"][sid][key])
    # member end forces and end-row shear / moment / axial (tangent frame at the ends)
    for m, Kg, pe, uf, dofs in elem:
        ue = [u[d] for d in dofs]
        if uf is None:
            fe = [sum(Kg[r][q] * ue[q] for q in range(12)) - pe[r] for r in range(12)]  # physical
            add_axial = 0.0
        else:
            pw = arc_weight_peq(c, m)
            fe = [sum(Kg[r][q] * (ue[q] - uf[q]) for q in range(12)) - pw[r] for r in range(12)]  # elastic
            add_axial = P
        for end, sl, f_ in (("end_i", slice(0, 6), D(0)), ("end_j", slice(6, 12), D(1))):
            fr_ = [[fl(x) for x in e] for e in m.authored_frame(f_)]
            fv, mv = fe[sl][:3], fe[sl][3:]
            sign = -1.0 if end == "end_i" else 1.0
            loc = [sum(fr_[a][q] * fv[q] for q in range(3)) for a in range(3)]
            locm = [sum(fr_[a][q] * mv[q] for q in range(3)) for a in range(3)]
            rowname = "element_local" if m.kind == "straight" else "tangent_frame"
            er = ref["members"][m.pid]["end_rows"][end][rowname]
            Nw = loc[0] + sign * add_axial
            note("wall_axial_force", Nw, er["F_x"])
            note("shear_force", loc[1], er["F_y"])
            note("shear_force", loc[2], er["F_z"])
            for a, key in enumerate(["M_x", "M_y", "M_z"]):
                note("section_moment", locm[a], er[key])
            if m.kind == "arc":
                cf = [[fl(x) for x in e] for e in m.chord_frame]
                ce = ref["members"][m.pid]["end_rows"][end]["chord_frame_elastic"]
                for a, key in enumerate(["F_x", "F_y", "F_z"]):
                    note("elastic_end_force_chord_frame", sum(cf[a][q] * fv[q] for q in range(3)), ce[key])
                for a, key in enumerate(["M_x", "M_y", "M_z"]):
                    note("section_moment", sum(cf[a][q] * mv[q] for q in range(3)), ce[key])
    return worst


def main(path):
    data = json.load(open(path))
    targets = ["U2-L-FREE-P-K2", "MECH-CURVED-BEND-EXACT-PRESSURE-ARC-K2", "U2-L-KINK-FREE-P-K2", "U2-L-KINK-ANCH-P-K2",
               "U2-L-FREE-PTW-K2", "U2-L-ANCH-PTW-K2", "U2-U-ANCH-PTW-K2", "U2-L-ANCH-PTW-K2-SKEW-X7P3E6",
               "U2-L-ANCH-ALL-K2", "U2-L-FREE-SEPD-K2"]
    for cid in targets:
        w = emulate(data["cases"][cid])
        zg = [g for g, v in data["cases"][cid]["zero_scale"].items() if v["basis"].startswith("group expected")]
        print(cid, " identically-zero groups:", zg)
        for g, (r, val, refv) in sorted(w.items(), key=lambda kv: -kv[1][0]):
            print("    %-32s max |emulated - ref| / floor = %.3e   (emulated %.6e, ref %s)" % (g, r, val, refv))


if __name__ == "__main__":
    main(sys.argv[1])
