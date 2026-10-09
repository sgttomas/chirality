"""T4-RV2: labelled binary64 emulations (NOT product code) of
  * a stable T4-U1 element ('GL'): half-angle geometry, local frame from d, R, y;
    F by 16-point Gauss-Legendre in binary64 with cancellation-free arm differences
    (P(phi) - P(theta) = 2R sin((phi-theta)/2) (-sin((phi+theta)/2), cos((phi+theta)/2)));
  * an ideal stable element ('CR'): the exact local F correctly rounded, then the same
    binary64 inversion, H and transform;
  * chord variants: 'actual' (-sL, cL, 0); 'formula' R(fl(cos phi_b) - 1), R fl(sin phi_b)
    with cos rounded to nearest ('formula_cr') or one ulp low ('formula_lo');
  * binary64 solves: LU with partial pivoting ('LU') and natural-order Cholesky ('LLT');
  * K-D5's estimate: rho = f - K_int u exactly (Decimal), w = K_b^-1 rho with the
    product factor, trigger 2|w_i| / (1e-9 max(|u_i|, S*_kind)), S* per FK body_scales.
"""
import math
from decimal import Decimal as D, getcontext, localcontext
import rv2_lib as L

_GL = None


def gl_b64(n=16):
    global _GL
    if _GL is None or len(_GL[0]) != n:
        with localcontext() as c:
            c.prec = 60
            xs, ws = L.gauss_legendre(n)
            _GL = ([float(x) for x in xs], [float(w) for w in ws])
    return _GL


def norm3(v):
    return math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])


def geometry_b64(d, R, y):
    Lc = norm3(d)
    s = Lc / (2.0 * R)
    c = math.sqrt((2.0 * R - Lc) * (2.0 * R + Lc)) / (2.0 * R)
    phi = 2.0 * math.atan2(s, c)
    dh = [v / Lc for v in d]
    yd = y[0] * dh[0] + y[1] * dh[1] + y[2] * dh[2]
    nr = [y[k] - yd * dh[k] for k in range(3)]
    nn = norm3(nr)
    n = [v / nn for v in nr]
    ex = [-s * dh[k] + c * n[k] for k in range(3)]
    ey = [c * dh[k] + s * n[k] for k in range(3)]
    ez = [n[1] * dh[2] - n[2] * dh[1], n[2] * dh[0] - n[0] * dh[2], n[0] * dh[1] - n[1] * dh[0]]
    return dict(L=Lc, s=s, c=c, phi=phi, axes=[ex, ey, ez])


def local_F_gl(R, phi, E, G, A, I, J, kin, kout, n=16):
    xs, ws = gl_b64(n)
    EI, GJ, EA = E * I, G * J, E * A
    F = [[0.0] * 6 for _ in range(6)]
    for x, w in zip(xs, ws):
        th = phi * (x + 1.0) * 0.5
        st, ct = math.sin(th), math.cos(th)
        hm = math.sin((phi - th) * 0.5)
        sp, cp = math.sin((phi + th) * 0.5), math.cos((phi + th) * 0.5)
        arm = (-2.0 * R * hm * sp, 2.0 * R * hm * cp)  # P(phi) - P(theta), z = 0
        acts = []
        for a in range(6):
            Fv = [0.0, 0.0, 0.0]
            Mv = [0.0, 0.0, 0.0]
            if a < 3:
                Fv[a] = 1.0
                # arm x F with arm = (ax, ay, 0)
                Mv = [arm[1] * Fv[2], -arm[0] * Fv[2], arm[0] * Fv[1] - arm[1] * Fv[0]]
            else:
                Mv[a - 3] = 1.0
            N = -st * Fv[0] + ct * Fv[1]
            T = -st * Mv[0] + ct * Mv[1]
            Mi = Mv[2]
            Mo = ct * Mv[0] + st * Mv[1]
            acts.append((N, T, Mi, Mo))
        wt = w * phi * 0.5 * R
        for a in range(6):
            Na, Ta, Ia, Oa = acts[a]
            for b in range(a, 6):
                Nb, Tb, Ib, Ob = acts[b]
                F[a][b] += wt * (kin * Ia * Ib / EI + kout * Oa * Ob / EI + Ta * Tb / GJ + Na * Nb / EA)
    for a in range(6):
        for b in range(a):
            F[a][b] = F[b][a]
    return F


def local_F_cr(d, R, y, E, G, A, I, J, kin, kout):
    """Exact local F (rv2_lib, global then rotated by the exact local axes), rounded once."""
    with localcontext() as c:
        c.prec = 80
        g = L.arc_geometry([0.0, 0.0, 0.0], d, R, y)
        Fg = L.tip_flexibility_global(g, E, G, A, I, J, kin, kout, n=40)
        Ax = [g["u0"], g["v0"], g["z"]]
        T6 = [[D(0)] * 6 for _ in range(6)]
        for b in range(2):
            for i in range(3):
                for j in range(3):
                    T6[3 * b + i][3 * b + j] = Ax[i][j]
        TF = [[sum((T6[i][k] * Fg[k][j] for k in range(6)), D(0)) for j in range(6)] for i in range(6)]
        Fl = [[sum((TF[i][k] * T6[j][k] for k in range(6)), D(0)) for j in range(6)] for i in range(6)]
        return [[float(v) for v in row] for row in Fl]


def inv6(F):
    n = 6
    M = [F[i][:] + [1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for col in range(n):
        p = max(range(col, n), key=lambda r: abs(M[r][col]))
        M[col], M[p] = M[p], M[col]
        pv = M[col][col]
        M[col] = [v / pv for v in M[col]]
        for r in range(n):
            if r != col:
                f = M[r][col]
                if f != 0.0:
                    M[r] = [M[r][k] - f * M[col][k] for k in range(2 * n)]
    K = [row[n:] for row in M]
    for i in range(6):
        for j in range(i + 1, 6):
            m = (K[i][j] + K[j][i]) * 0.5
            K[i][j] = K[j][i] = m
    return K


def mm(P, Q):
    return [[sum(P[i][t] * Q[t][j] for t in range(len(Q))) for j in range(len(Q[0]))] for i in range(len(P))]


def element_b64(d, R, y, E, G, A, I, J, kin, kout, F_mode="GL", chord="actual"):
    g = geometry_b64(d, R, y)
    if F_mode == "GL":
        F = local_F_gl(R, g["phi"], E, G, A, I, J, kin, kout)
    else:
        F = local_F_cr(d, R, y, E, G, A, I, J, kin, kout)
    Kt = inv6(F)
    if chord == "actual":
        c = [-g["s"] * g["L"], g["c"] * g["L"], 0.0]
    else:
        cosb = math.cos(g["phi"])
        if chord == "formula_lo" and cosb == 1.0:
            cosb = 1.0 - 2.0 ** -53
        c = [R * (cosb - 1.0), R * math.sin(g["phi"]), 0.0]
    H = [[0.0] * 6 for _ in range(6)]
    for i in range(6):
        H[i][i] = 1.0
    H[3][1], H[3][2], H[4][0], H[4][2], H[5][0], H[5][1] = -c[2], c[1], c[2], -c[0], -c[1], c[0]
    HK = mm(H, Kt)
    HKHt = mm(HK, [list(r) for r in zip(*H)])
    Kl = [[0.0] * 12 for _ in range(12)]
    for i in range(6):
        for j in range(6):
            Kl[i][j] = HKHt[i][j]
            Kl[i][j + 6] = -HK[i][j]
            Kl[i + 6][j] = -HK[j][i]
            Kl[i + 6][j + 6] = Kt[i][j]
    Ax = g["axes"]
    K = [[0.0] * 12 for _ in range(12)]
    for bi in range(4):
        for bj in range(4):
            blk = [[Kl[3 * bi + p][3 * bj + q] for q in range(3)] for p in range(3)]
            tmp = [[sum(blk[p][q] * Ax[q][cc] for q in range(3)) for cc in range(3)] for p in range(3)]
            for r in range(3):
                for cc in range(3):
                    K[3 * bi + r][3 * bj + cc] = sum(Ax[p][r] * tmp[p][cc] for p in range(3))
    return K, g, c


# ------------------------------------------------------------------ models and solves (binary64)
def assemble(n_nodes, elems, springs):
    n = 6 * n_nodes
    K = [[0.0] * n for _ in range(n)]
    for (i, j, Ke) in elems:
        dof = [6 * i + r for r in range(6)] + [6 * j + r for r in range(6)]
        for a in range(12):
            for b in range(12):
                K[dof[a]][dof[b]] += Ke[a][b]
    for dd, v in springs:
        K[dd][dd] += v
    return K


class LU:
    def __init__(self, A):
        n = len(A)
        self.n = n
        M = [r[:] for r in A]
        self.perm = list(range(n))
        for col in range(n):
            p = max(range(col, n), key=lambda r: abs(M[r][col]))
            M[col], M[p] = M[p], M[col]
            self.perm[col], self.perm[p] = self.perm[p], self.perm[col]
            for r in range(col + 1, n):
                f = M[r][col] / M[col][col]
                M[r][col] = f
                for k in range(col + 1, n):
                    M[r][k] -= f * M[col][k]
        self.M = M

    def solve(self, b):
        n, M = self.n, self.M
        y = [b[self.perm[i]] for i in range(n)]
        for i in range(n):
            for k in range(i):
                y[i] -= M[i][k] * y[k]
        for i in reversed(range(n)):
            for k in range(i + 1, n):
                y[i] -= M[i][k] * y[k]
            y[i] /= M[i][i]
        return y


class LLT:
    def __init__(self, A):
        n = len(A)
        self.n = n
        Lm = [[0.0] * n for _ in range(n)]
        for j in range(n):
            s = A[j][j] - sum(Lm[j][k] * Lm[j][k] for k in range(j))
            Lm[j][j] = math.sqrt(s)
            for i in range(j + 1, n):
                Lm[i][j] = (A[i][j] - sum(Lm[i][k] * Lm[j][k] for k in range(j))) / Lm[j][j]
        self.Lm = Lm

    def solve(self, b):
        n, Lm = self.n, self.Lm
        y = b[:]
        for i in range(n):
            for k in range(i):
                y[i] -= Lm[i][k] * y[k]
            y[i] /= Lm[i][i]
        for i in reversed(range(n)):
            for k in range(i + 1, n):
                y[i] -= Lm[k][i] * y[k]
            y[i] /= Lm[i][i]
        return y


def solve_model(K, f, free, solver="LU", refine=0):
    Kf = [[K[a][b] for b in free] for a in free]
    fac = LU(Kf) if solver == "LU" else LLT(Kf)
    x = fac.solve([f[a] for a in free])
    for _ in range(refine):
        r = [f[a] - sum(K[a][b] * x[jb] for jb, b in enumerate(free)) for a in free]
        dx = fac.solve(r)
        x = [x[i] + dx[i] for i in range(len(x))]
    return dict(zip(free, x)), fac


def body_scales_one(u, free, nodes):
    st = max((abs(u[i]) for i in free if i % 6 < 3), default=0.0)
    sr = max((abs(u[i]) for i in free if i % 6 >= 3), default=0.0)
    ext = [max(p[k] for p in nodes) - min(p[k] for p in nodes) for k in range(3)]
    lb = math.sqrt((ext[0] * ext[0] + ext[1] * ext[1]) + ext[2] * ext[2])
    return max(st, lb * sr), max(sr, st / lb)


def kd5_trigger(Kint_dec, springs, f, u_b, free, fac, nodes):
    """Kint_dec: exact (Decimal) global matrix of the intended elements (assembled, n x n)."""
    n = len(f)
    uvec = [0.0] * n
    for i in free:
        uvec[i] = u_b[i]
    with localcontext() as c:
        c.prec = 90
        rho = []
        for a in free:
            s = D(f[a])
            for b in range(n):
                if uvec[b] != 0.0 and Kint_dec[a][b] != 0:
                    s -= Kint_dec[a][b] * D(uvec[b])
            for dd, v in springs:
                if dd == a:
                    s -= D(v) * D(uvec[a])
            rho.append(float(s))
    w = fac.solve(rho)
    tr, ro = body_scales_one(uvec, free, nodes)
    worst, at = 0.0, None
    for r, i in enumerate(free):
        scale = max(abs(uvec[i]), ro if i % 6 >= 3 else tr)
        t = 2.0 * abs(w[r]) / (1e-9 * scale)
        if t > worst:
            worst, at = t, i
    return worst, at


def actual_ratio(u_ref, u, nodes):
    st = max(abs(v) for k, v in u_ref.items() if k % 6 < 3)
    sr = max(abs(v) for k, v in u_ref.items() if k % 6 >= 3)
    ext = [max(D(p[k]) for p in nodes) - min(D(p[k]) for p in nodes) for k in range(3)]
    lb = L.vnorm(ext)
    tr, ro = max(st, lb * sr), max(sr, st / lb)
    worst, at = D(0), None
    for k, v in u_ref.items():
        r = abs(D(u[k]) - v) / (D("1e-9") * max(abs(v), tr if k % 6 < 3 else ro))
        if r > worst:
            worst, at = r, k
    return float(worst), at
