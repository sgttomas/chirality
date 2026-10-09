"""T4-RV2: an independent derivation of T4-U1's objective curved element.

Standard library only (decimal, fractions). Written without reading T4-I6's
formulas into it. Method (deliberately different from T4-I6's):
  * geometry: the arc centre C is formed exactly (high precision) from
    d = x_j - x_i, R and the bow direction b = unit(y - (y.d)d/|d|^2):
    C = x_i + d/2 - h b, h = sqrt(R^2 - |d|^2/4); the arc is the circle
    through x_i and x_j about C in the plane (d, b), bowing toward +b;
  * flexibility: the complementary-energy (unit-load) integral in GLOBAL
    coordinates, the section actions formed from global vectors
    M(theta) = M + (x_j - P(theta)) x F, integrated by Gauss-Legendre
    quadrature (no closed forms, no local action table, no Gram matrix);
  * stiffness: K_jj = F^-1 (global), and the 12x12 by the global
    compatibility matrix B = [[-I, skew(d)], [0, -I] | I_6], K = B^T K_jj B
    (no local frame, no H, no rotation T).
Trigonometry: own Taylor sin/cos with argument halving and double-angle
recovery; pi by the Gauss-Legendre AGM; angles by Newton iteration.
"""
from decimal import Decimal as D, getcontext, localcontext
from fractions import Fraction as Fr
import math

# ------------------------------------------------------------------ scalars
_pi_cache = {}


def pi_agm():
    p = getcontext().prec
    if p in _pi_cache:
        return _pi_cache[p]
    with localcontext() as c:
        c.prec = p + 15
        a, b, t, q = D(1), D(1) / D(2).sqrt(), D(1) / 4, D(1)
        for _ in range(60):
            an = (a + b) / 2
            b = (a * b).sqrt()
            t -= q * (a - an) ** 2
            q *= 2
            a = an
            if abs(a - b) < D(10) ** (-(c.prec - 2)):
                break
        v = (a + b) ** 2 / (4 * t)
    _pi_cache[p] = +v
    return _pi_cache[p]


def sincos(x):
    """(sin x, cos x) for |x| <= 4 by halving k times, Taylor, then k double-angle steps."""
    with localcontext() as c:
        c.prec += 30
        k = 0
        y = x
        while abs(y) > D("1e-3"):
            y /= 2
            k += 1
        eps = D(10) ** (-(c.prec + 3))
        y2 = y * y
        s, term, n = D(0), y, 1
        while abs(term) > eps:
            s += term
            term = -term * y2 / ((n + 1) * (n + 2))
            n += 2
        # cos - 1 by series (keeps relative accuracy of 1 - cos)
        cm1, term, n = D(0), -y2 / 2, 2
        while abs(term) > eps:
            cm1 += term
            term = -term * y2 / ((n + 1) * (n + 2))
            n += 2
        for _ in range(k):
            # sin 2a = 2 s (1 + cm1);  cos 2a - 1 = 2 cm1 (2 + cm1)... = 2(c^2) - 2 = 2 cm1 (cm1 + 2)
            s, cm1 = 2 * s * (1 + cm1), 2 * cm1 * (cm1 + 2)
        return +s, +(1 + cm1)


def angle_newton(s, c):
    """theta in (0, pi/2] with sin theta : cos theta = s : c (s, c > 0), by Newton on
    g(t) = sin t * c - cos t * s, started from binary64 atan2."""
    t = D(math.atan2(float(s), float(c)))
    with localcontext() as ctx:
        ctx.prec += 20
        for _ in range(200):
            st, ct = sincos(t)
            g = st * c - ct * s
            dg = ct * c + st * s
            dt = g / dg
            t -= dt
            if dt == 0 or abs(dt) < abs(t) * D(10) ** (-(ctx.prec - 3)):
                break
    return +t


# ------------------------------------------------------------------ vectors
def vdot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def vcross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def vsub(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]


def vadd(a, b):
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]


def vmul(s, a):
    return [s * a[0], s * a[1], s * a[2]]


def vnorm(a):
    return vdot(a, a).sqrt()


def gauss_jordan_inverse(M):
    n = len(M)
    A = [[M[i][j] for j in range(n)] + [D(1) if i == j else D(0) for j in range(n)] for i in range(n)]
    for col in range(n):
        p = max(range(col, n), key=lambda r: abs(A[r][col]))
        A[col], A[p] = A[p], A[col]
        piv = A[col][col]
        A[col] = [v / piv for v in A[col]]
        for r in range(n):
            if r != col:
                f = A[r][col]
                if f != 0:
                    A[r] = [A[r][k] - f * A[col][k] for k in range(2 * n)]
    return [row[n:] for row in A]


def lu_solve_dec(M, b):
    n = len(M)
    A = [list(M[i]) + [b[i]] for i in range(n)]
    for col in range(n):
        p = max(range(col, n), key=lambda r: abs(A[r][col]))
        A[col], A[p] = A[p], A[col]
        for r in range(col + 1, n):
            f = A[r][col] / A[col][col]
            if f != 0:
                for k in range(col, n + 1):
                    A[r][k] -= f * A[col][k]
    x = [D(0)] * n
    for i in reversed(range(n)):
        x[i] = (A[i][n] - sum((A[i][k] * x[k] for k in range(i + 1, n)), D(0))) / A[i][i]
    return x


# ------------------------------------------------------------------ quadrature
_gl_cache = {}


def gauss_legendre(n):
    key = (n, getcontext().prec)
    if key in _gl_cache:
        return _gl_cache[key]
    xs, ws = [], []
    with localcontext() as c:
        c.prec += 10
        tol = D(10) ** (-(c.prec - 4))
        for i in range(1, n + 1):
            # Tricomi initial guess
            x = D(math.cos(math.pi * (4 * i - 1) / (4 * n + 2)))
            for _ in range(60):
                p0, p1 = D(1), x
                for k in range(2, n + 1):
                    p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
                dp = n * (p0 - x * p1) / (1 - x * x)
                dx = p1 / dp
                x -= dx
                if abs(dx) < tol:
                    break
            p0, p1 = D(1), x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (p0 - x * p1) / (1 - x * x)
            xs.append(+x)
            ws.append(+(2 / ((1 - x * x) * dp * dp)))
    _gl_cache[key] = (xs, ws)
    return xs, ws


# ------------------------------------------------------------------ the element
def arc_geometry(xi, xj, R, y):
    xi = [D(v) for v in xi]
    xj = [D(v) for v in xj]
    y = [D(v) for v in y]
    R = D(R)
    d = vsub(xj, xi)
    L2 = vdot(d, d)
    L = L2.sqrt()
    b = vsub(y, vmul(vdot(y, d) / L2, d))
    b = vmul(1 / vnorm(b), b)
    h = (R * R - L2 / 4).sqrt()
    C = vsub(vadd(xi, vmul(D(1) / 2, d)), vmul(h, b))
    ri = vsub(xi, C)
    rj = vsub(xj, C)
    u0 = vmul(1 / R, ri)
    z = vcross(ri, rj)
    z = vmul(1 / vnorm(z), z)
    v0 = vcross(z, u0)
    # half angle: sin(phi/2) = L/(2R), cos(phi/2) = h/R
    half = angle_newton(L / (2 * R), h / R)
    phi = 2 * half
    return dict(xi=xi, xj=xj, d=d, L=L, R=R, b=b, h=h, C=C, u0=u0, v0=v0, z=z, phi=phi)


def tip_flexibility_global(g, E, G, A, I, J, kin, kout, n=48):
    E, G, A, I, J, kin, kout = (D(v) for v in (E, G, A, I, J, kin, kout))
    R, phi, C, u0, v0, z, xj = g["R"], g["phi"], g["C"], g["u0"], g["v0"], g["z"], g["xj"]
    xs, ws = gauss_legendre(n)
    F = [[D(0)] * 6 for _ in range(6)]
    EI, GJ, EA = E * I, G * J, E * A
    for x, w in zip(xs, ws):
        th = phi * (x + 1) / 2
        st, ct = sincos(th)
        er = vadd(vmul(ct, u0), vmul(st, v0))
        t = vadd(vmul(-st, u0), vmul(ct, v0))
        P = vadd(C, vmul(R, er))
        arm = vsub(xj, P)
        acts = []
        for a in range(6):
            Fv = [D(0)] * 3
            Mv = [D(0)] * 3
            if a < 3:
                Fv[a] = D(1)
                Mt = vcross(arm, Fv)
            else:
                Mv[a - 3] = D(1)
                Mt = Mv
            acts.append((vdot(Fv, t), vdot(Mt, t), vdot(Mt, z), vdot(Mt, er)))
        wt = w * phi / 2 * R
        for a in range(6):
            Na, Ta, Ia, Oa = acts[a]
            for b in range(a, 6):
                Nb, Tb, Ib, Ob = acts[b]
                F[a][b] += wt * (kin * Ia * Ib / EI + kout * Oa * Ob / EI + Ta * Tb / GJ + Na * Nb / EA)
    for a in range(6):
        for b in range(a):
            F[a][b] = F[b][a]
    return F


def compat_B(d):
    """6x12: e = (u_j - u_i - w_i x d, w_j - w_i)."""
    B = [[D(0)] * 12 for _ in range(6)]
    for k in range(3):
        B[k][k] = D(-1)
        B[3 + k][3 + k] = D(-1)
        B[k][6 + k] = D(1)
        B[3 + k][9 + k] = D(1)
    # skew(d) w = d x w  ->  -w x d
    S = [[D(0), -d[2], d[1]], [d[2], D(0), -d[0]], [-d[1], d[0], D(0)]]
    for r in range(3):
        for c in range(3):
            B[r][3 + c] = S[r][c]
    return B


def curved_K(xi, xj, R, y, E, G, A, I, J, kin, kout, n=48, chord_override=None):
    """Global 12x12. chord_override: a global vector replacing d in B (a mutant H)."""
    g = arc_geometry(xi, xj, R, y)
    F = tip_flexibility_global(g, E, G, A, I, J, kin, kout, n)
    Kjj = gauss_jordan_inverse(F)
    for a in range(6):
        for b in range(a):
            m = (Kjj[a][b] + Kjj[b][a]) / 2
            Kjj[a][b] = Kjj[b][a] = m
    dd = g["d"] if chord_override is None else chord_override
    B = compat_B(dd)
    KB = [[sum((Kjj[r][k] * B[k][c] for k in range(6)), D(0)) for c in range(12)] for r in range(6)]
    K = [[sum((B[k][r] * KB[k][c] for k in range(6)), D(0)) for c in range(12)] for r in range(12)]
    return dict(geo=g, F=F, Kjj=Kjj, K=K)


def frame_K(xi, xj, E, G, A, I, J):
    """Straight Euler-Bernoulli frame, Iy = Iz = I (pipe), so independent of y_reference.
    Formed by the same compatibility route: K_jj = F^-1 of a straight cantilever."""
    xi = [D(v) for v in xi]
    xj = [D(v) for v in xj]
    E, G, A, I, J = (D(v) for v in (E, G, A, I, J))
    d = vsub(xj, xi)
    L = vnorm(d)
    e = vmul(1 / L, d)
    # tip flexibility of a straight cantilever, global: translation-force
    # F_tt = L/(EA) e e^T + L^3/(3EI) (I - e e^T); F_tr = L^2/(2EI) skew-type; F_rr = L/(GJ) e e^T + L/(EI)(I - e e^T)
    P = [[e[r] * e[c] for c in range(3)] for r in range(3)]
    Q = [[(D(1) if r == c else D(0)) - P[r][c] for c in range(3)] for r in range(3)]
    F = [[D(0)] * 6 for _ in range(6)]
    for r in range(3):
        for c in range(3):
            F[r][c] = L / (E * A) * P[r][c] + L ** 3 / (3 * E * I) * Q[r][c]
            F[3 + r][3 + c] = L / (G * J) * P[r][c] + L / (E * I) * Q[r][c]
    # tip rotation under tip force F: theta = (L^2/(2EI)) e x F ; tip translation under tip moment M: u = (L^2/(2EI)) M x e ... (reciprocity)
    S = [[D(0), -e[2], e[1]], [e[2], D(0), -e[0]], [-e[1], e[0], D(0)]]  # S v = e x v
    k = L ** 2 / (2 * E * I)
    for r in range(3):
        for c in range(3):
            F[3 + r][c] = k * S[r][c]
            F[c][3 + r] = k * S[r][c]
    Kjj = gauss_jordan_inverse(F)
    B = compat_B(d)
    KB = [[sum((Kjj[r][kk] * B[kk][c] for kk in range(6)), D(0)) for c in range(12)] for r in range(6)]
    return [[sum((B[kk][r] * KB[kk][c] for kk in range(6)), D(0)) for c in range(12)] for r in range(12)]


def rigid_modes(d):
    out = []
    for k in range(3):
        m = [D(0)] * 12
        m[k] = m[6 + k] = D(1)
        out.append(m)
    for k in range(3):
        w = [D(0)] * 3
        w[k] = D(1)
        s = vcross(w, [D(v) for v in d])
        m = [D(0)] * 12
        for c in range(3):
            m[3 + c] = m[9 + c] = w[c]
            m[6 + c] = s[c]
        out.append(m)
    return out


def maxabs(M):
    return max(abs(v) for row in M for v in row)
