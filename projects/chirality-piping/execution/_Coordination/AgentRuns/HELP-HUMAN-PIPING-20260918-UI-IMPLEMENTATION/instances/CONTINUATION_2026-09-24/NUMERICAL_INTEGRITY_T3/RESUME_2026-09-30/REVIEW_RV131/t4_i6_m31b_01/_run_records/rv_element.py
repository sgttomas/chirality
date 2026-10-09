"""RV131: an independent reference for the B1 curved element (T4-I6 U1_REFERENCE.md B1).

Written from the definition only; it does not import or transcribe curved_ref.py.
Method (deliberately different from T4-I6's local closed form):
  - geometry in GLOBAL coordinates from d = x_j - x_i, R and y (arc bows toward +n, n the
    unit projection of y normal to d); the arc is parametrized about its exact centre,
    expressed relative to x_i;
  - the 6x6 tip flexibility (node i clamped) is integrated by Gauss-Legendre quadrature of
    the complementary energy, the section actions formed directly from global vectors
    (moment arm x_j - P(theta) crossed with the unit force); no Gram matrix, no local frame;
  - the 12x12 follows from global equilibrium with the actual chord d:
    K = [[G Kt G^T, -G Kt], [-Kt G^T, Kt]], G = [[I, 0], [skew(d), I]], Kt = F^-1 (global).
Standard library only (decimal).
"""
from decimal import Decimal as D, getcontext, localcontext
import math

getcontext().prec = 90


def dec(v):
    return v if isinstance(v, D) else D(v)


# ------------------------------------------------------------------ scalar functions (own series)
def d_pi():
    with localcontext() as c:
        c.prec += 10
        # Machin: pi = 16 atan(1/5) - 4 atan(1/239)
        v = 16 * _atan_small(D(1) / 5) - 4 * _atan_small(D(1) / 239)
    return +v


def _atan_small(x):
    with localcontext() as c:
        c.prec += 10
        eps = D(10) ** (-(c.prec + 2))
        s, t, k, x2 = D(0), x, 0, x * x
        while abs(t) > eps:
            s += t / (2 * k + 1) if k % 2 == 0 else -t / (2 * k + 1)
            t *= x2
            k += 1
    return +s


def d_atan(x):
    """atan(x), any real x, by halving the argument until it is small."""
    with localcontext() as c:
        c.prec += 12
        if x < 0:
            return -d_atan(-x)
        if x > 1:
            r = d_pi() / 2 - d_atan(1 / x)
        else:
            k, y = 0, x
            while y > D("1e-4"):
                y = y / (1 + (1 + y * y).sqrt())
                k += 1
            r = _atan_small(y) * (2 ** k)
    return +r


def d_atan2(y, x):
    if x > 0:
        return d_atan(y / x)
    if x == 0:
        return d_pi() / 2 if y > 0 else -d_pi() / 2
    return d_atan(y / x) + (d_pi() if y >= 0 else -d_pi())


def d_sincos(x):
    with localcontext() as c:
        c.prec += 15
        eps = D(10) ** (-(c.prec + 2))
        s, t, n = D(0), x, 1
        x2 = x * x
        while abs(t) > eps:
            s += t
            t = -t * x2 / ((n + 1) * (n + 2))
            n += 2
        co, t, n = D(0), D(1), 0
        while abs(t) > eps:
            co += t
            t = -t * x2 / ((n + 1) * (n + 2))
            n += 2
    return +s, +co


# ------------------------------------------------------------------ vectors and matrices
def v_add(a, b):
    return [a[k] + b[k] for k in range(3)]


def v_sub(a, b):
    return [a[k] - b[k] for k in range(3)]


def v_mul(s, a):
    return [s * a[k] for k in range(3)]


def v_dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def v_cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def v_norm(a):
    return v_dot(a, a).sqrt()


def m_mul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), D(0)) for j in range(len(B[0]))] for i in range(len(A))]


def m_T(A):
    return [list(r) for r in zip(*A)]


def m_inv(M):
    n = len(M)
    A = [list(M[i]) + [D(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(A[r][col]))
        A[col], A[piv] = A[piv], A[col]
        p = A[col][col]
        A[col] = [v / p for v in A[col]]
        for r in range(n):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [A[r][k] - f * A[col][k] for k in range(2 * n)]
    return [row[n:] for row in A]


def m_solve(M, b):
    n = len(M)
    A = [list(M[i]) + [b[i]] for i in range(n)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(A[r][col]))
        A[col], A[piv] = A[piv], A[col]
        for r in range(col + 1, n):
            if A[r][col] != 0:
                f = A[r][col] / A[col][col]
                A[r] = [A[r][k] - f * A[col][k] for k in range(n + 1)]
    x = [D(0)] * n
    for i in range(n - 1, -1, -1):
        x[i] = (A[i][n] - sum((A[i][k] * x[k] for k in range(i + 1, n)), D(0))) / A[i][i]
    return x


# ------------------------------------------------------------------ Gauss-Legendre (own)
_GL = {}


def gauss_legendre(n):
    key = (n, getcontext().prec)
    if key in _GL:
        return _GL[key]
    xs, ws = [], []
    with localcontext() as c:
        c.prec += 10
        tol = D(10) ** (-(c.prec - 4))
        for i in range(1, n + 1):
            x = D(math.cos(math.pi * (i - 0.25) / (n + 0.5)))
            for _ in range(200):
                p0, p1 = D(1), x
                for k in range(2, n + 1):
                    p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
                dp = n * (x * p1 - p0) / (x * x - 1)
                dx = p1 / dp
                x -= dx
                if abs(dx) < tol:
                    break
            p0, p1 = D(1), x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (x * p1 - p0) / (x * x - 1)
            xs.append(+x)
            ws.append(+(2 / ((1 - x * x) * dp * dp)))
    _GL[key] = (xs, ws)
    return xs, ws


# ------------------------------------------------------------------ the element
def arc_geometry(d, R, y):
    d = [dec(v) for v in d]
    R = dec(R)
    y = [dec(v) for v in y]
    L = v_norm(d)
    assert 2 * R > L, "R must exceed L/2"
    dh = v_mul(1 / L, d)
    yp = v_sub(y, v_mul(v_dot(y, dh), dh))
    n = v_mul(1 / v_norm(yp), yp)
    h = (R * R - L * L / 4).sqrt()          # centre-to-chord distance (exact real)
    C = v_sub(v_mul(D(1) / 2, d), v_mul(h, n))  # centre relative to x_i
    u1 = v_mul(-1 / R, C)                    # radial unit at x_i (outward)
    w = v_sub(d, v_mul(v_dot(d, u1), u1))
    u2 = v_mul(1 / v_norm(w), w)             # in-plane, toward x_j
    rj = v_sub(d, C)
    phi = d_atan2(v_dot(rj, u2), v_dot(rj, u1))
    return dict(d=d, L=L, R=R, n=n, C=C, u1=u1, u2=u2, phi=phi, ez=v_cross(u1, u2))


def tip_flexibility_global(geo, E, G, A, I, J, kin, kout, npts=48):
    R, phi, C, u1, u2, ez, d = geo["R"], geo["phi"], geo["C"], geo["u1"], geo["u2"], geo["ez"], geo["d"]
    E, G, A, I, J, kin, kout = (dec(v) for v in (E, G, A, I, J, kin, kout))
    xs, ws = gauss_legendre(npts)
    F = [[D(0)] * 6 for _ in range(6)]
    units = [[D(int(k == j)) for k in range(3)] for j in range(3)]
    for x, wq in zip(xs, ws):
        th = phi * (x + 1) / 2
        s, c = d_sincos(th)
        er = v_add(v_mul(c, u1), v_mul(s, u2))          # radial at the section
        t = v_add(v_mul(-s, u1), v_mul(c, u2))          # tangent (direction i -> j)
        P = v_add(C, v_mul(R, er))                      # section point relative to x_i
        arm = v_sub(d, P)                               # x_j - P
        acts = []
        for a in range(6):
            Fv = units[a] if a < 3 else [D(0)] * 3
            Mv = [D(0)] * 3 if a < 3 else units[a - 3]
            M = v_add(Mv, v_cross(arm, Fv))
            acts.append((v_dot(Fv, t), v_dot(M, t), v_dot(M, ez), v_dot(M, er)))
        wt = wq * phi / 2 * R
        for a in range(6):
            Na, Ta, Ia, Oa = acts[a]
            for b in range(a, 6):
                Nb, Tb, Ib, Ob = acts[b]
                F[a][b] += wt * (kin * Ia * Ib / (E * I) + kout * Oa * Ob / (E * I) + Ta * Tb / (G * J) + Na * Nb / (E * A))
    for a in range(6):
        for b in range(a):
            F[a][b] = F[b][a]
    return F


def element_global(d, R, y, E, G, A, I, J, kin, kout, chord_global=None, npts=48):
    """12x12 global stiffness. chord_global=None: the actual chord d (the definition);
    otherwise the transfer uses the supplied global chord (a mutant)."""
    geo = arc_geometry(d, R, y)
    F = tip_flexibility_global(geo, E, G, A, I, J, kin, kout, npts)
    Kt = m_inv(F)
    c = geo["d"] if chord_global is None else [dec(v) for v in chord_global]
    Gm = [[D(0)] * 6 for _ in range(6)]
    for i in range(6):
        Gm[i][i] = D(1)
    S = [[D(0), -c[2], c[1]], [c[2], D(0), -c[0]], [-c[1], c[0], D(0)]]
    for i in range(3):
        for j in range(3):
            Gm[3 + i][j] = S[i][j]
    GK = m_mul(Gm, Kt)
    GKGt = m_mul(GK, m_T(Gm))
    K = [[D(0)] * 12 for _ in range(12)]
    for i in range(6):
        for j in range(6):
            K[i][j] = GKGt[i][j]
            K[i][j + 6] = -GK[i][j]
            K[i + 6][j] = -GK[j][i]
            K[i + 6][j + 6] = Kt[i][j]
    return K, geo, F


def b1_axes(geo):
    """B1's local axes (rows): e_x radial at i, e_y tangent at i, e_z = n x dhat."""
    return [geo["u1"], geo["u2"], geo["ez"]]


# ------------------------------------------------------------------ the K1-type cantilever
SECTION = dict(E=2.0e11, G=8.0e10, A=0.005969026041820614, I=2.700984283923829e-05, J=5.401968567847658e-05)


def cantilever_free_K(Ke, springs=1.0e6):
    """N0 translations rigid, N0 rotations on springs, N1 free. Free DOFs 3,4,5,6..11."""
    free = [3, 4, 5, 6, 7, 8, 9, 10, 11]
    K = [[Ke[a][b] for b in free] for a in free]
    for k in range(3):
        K[k][k] += dec(springs)
    return K, free


def cantilever_solve(Ke, load=(0, 0, 0, 0, 0, 0, 0, 0, 0, 1.0, 1.0, 1.0)):
    K, free = cantilever_free_K(Ke)
    f = [dec(load[dof]) for dof in free]
    u = m_solve(K, f)
    return dict(zip(free, u)), K, free


def actual_ratio(u_ref, u, L_b):
    """kd5_tests.rs:204 measure, one body, L_b the extent diagonal."""
    st = max(abs(v) for k, v in u_ref.items() if k % 6 < 3)
    sr = max(abs(v) for k, v in u_ref.items() if k % 6 >= 3)
    tr, ro = max(st, L_b * sr), max(sr, st / L_b)
    worst = D(0)
    for k, v in u_ref.items():
        sc = max(abs(v), tr if k % 6 < 3 else ro)
        worst = max(worst, abs(dec(u[k]) - v) / (D("1e-9") * sc))
    return worst
