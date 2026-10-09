"""T4-RV3 independent library: strong-form transfer-matrix solution of a chain of straight and
circular-arc Euler-Bernoulli members (axial, torsion and bending; bending scaled by k on arcs; no shear).

Method (independent of T4-I7's unit-load engine): the linear beam equations are written in the
co-rotating member frame (t, n inward, b), where a circular arc has constant coefficients,

    F' = -w x F - q            (j-side action; q distributed load per unit length)
    M' = -w x M - t x F
    u' = -w x u + theta x t + t (N/EA + eps0)
    theta' = -w x theta + (T/GJ) t + k (M - T t)/EI
    g' = -w x g                (a constant global vector seen in the rotating frame)

with w = (0, 0, 1/R) on arcs and 0 on straights.  The state [F, M, u, theta, g, 1] is propagated by the
matrix exponential of the constant 16x16 system matrix (Taylor series in Python decimal at 50 digits).
The line is solved by shooting from the anchored node A (unknown section action just past A); the
conditions at D are zero action beyond D (free) or zero motion (anchored).  No flexibility integral,
no Gauss quadrature, no stiffness matrix and no K*u_free are used.

pi by the Gauss-Legendre AGM; sin/cos by halving, Taylor and doubling; atan2 by Newton on sin/cos.
"""
from decimal import Decimal as D, getcontext, localcontext
import math

getcontext().prec = 50
ZERO, ONE = D(0), D(1)


# ---------------------------------------------------------------- scalar functions
def _agm_pi():
    with localcontext() as c:
        c.prec = getcontext().prec + 20
        a, b, t, p = D(1), D(1) / D(2).sqrt(), D(1) / 4, D(1)
        for _ in range(12):
            an = (a + b) / 2
            b = (a * b).sqrt()
            t -= p * (a - an) * (a - an)
            a = an
            p *= 2
        r = (a + b) * (a + b) / (4 * t)
    return +r


PI = _agm_pi()


def sincos(x):
    x = D(x)
    with localcontext() as c:
        c.prec = getcontext().prec + 15
        twopi = 2 * PI
        n = (x / twopi).to_integral_value()
        x = x - n * twopi
        k = 0
        while abs(x) > D("0.001"):
            x = x / 2
            k += 1
        x2 = x * x
        s, co = x, D(1)
        ts, tc = x, D(1)
        i = 1
        eps = D(10) ** (-(c.prec + 3))
        while True:
            ts = -ts * x2 / ((2 * i) * (2 * i + 1))
            tc = -tc * x2 / ((2 * i - 1) * (2 * i))
            s += ts
            co += tc
            if abs(ts) < eps and abs(tc) < eps:
                break
            i += 1
        for _ in range(k):
            s, co = 2 * s * co, co * co - s * s
    return +s, +co


def atan2(y, x):
    y, x = D(y), D(x)
    a = D(repr(math.atan2(float(y), float(x))))
    for _ in range(60):
        s, c = sincos(a)
        f = x * s - y * c
        fp = x * c + y * s
        da = f / fp
        a -= da
        if abs(da) < D(10) ** (-(getcontext().prec + 2)):
            break
    return a


# ---------------------------------------------------------------- vectors
def vec(a):
    return tuple(D(x) for x in a)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def mul(s, a):
    return (s * a[0], s * a[1], s * a[2])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def norm(a):
    return dot(a, a).sqrt()


def unit(a):
    return mul(ONE / norm(a), a)


V0 = (ZERO, ZERO, ZERO)


def to_global(frame, comps):
    t, n, b = frame
    return add(add(mul(comps[0], t), mul(comps[1], n)), mul(comps[2], b))


def to_local(frame, v):
    return tuple(dot(v, e) for e in frame)


# ---------------------------------------------------------------- matrices
def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    out = [[ZERO] * p for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        oi = out[i]
        for k in range(m):
            a = Ai[k]
            if a == 0:
                continue
            Bk = B[k]
            for j in range(p):
                if Bk[j] != 0:
                    oi[j] += a * Bk[j]
    return out


def matvec(A, x):
    return [sum((A[i][k] * x[k] for k in range(len(x)) if A[i][k] != 0 and x[k] != 0), ZERO) for i in range(len(A))]


def expm(A, h, terms=90):
    n = len(A)
    Ah = [[a * h for a in row] for row in A]
    E = [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]
    T = [row[:] for row in E]
    for k in range(1, terms + 1):
        T = matmul(T, Ah)
        T = [[x / k for x in row] for row in T]
        zero = True
        for i in range(n):
            for j in range(n):
                if T[i][j] != 0:
                    E[i][j] += T[i][j]
                    zero = False
        if zero:
            break
    return E


def solve(A, b):
    n = len(b)
    M = [list(A[i]) + [b[i]] for i in range(n)]
    for c in range(n):
        piv = max(range(c, n), key=lambda r: abs(M[r][c]))
        M[c], M[piv] = M[piv], M[c]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c] / M[c][c]
                M[r] = [M[r][k] - f * M[c][k] for k in range(n + 1)]
    return [M[i][n] / M[i][i] for i in range(n)]


# ---------------------------------------------------------------- section and material
class Section:
    def __init__(self, od, wall, mill):
        self.od, self.wall, self.mill = D(od), D(wall), D(mill)
        t = self.wall - self.mill
        self.ro = self.od / 2
        self.ri = self.ro - t
        self.As = PI * (self.ro * self.ro - self.ri * self.ri)
        self.Ai = PI * self.ri * self.ri
        self.I = PI * (self.ro ** 4 - self.ri ** 4) / 4
        self.J = 2 * self.I
        self.Z = self.I / self.ro


class Material:
    def __init__(self, E, nu, alpha):
        self.E, self.nu, self.alpha = D(E), D(nu), D(alpha)
        self.G = self.E / (2 * (1 + self.nu))


# ---------------------------------------------------------------- members
class Member:
    def __init__(self, pid, kind, a_from, a_to, xi, xj, yref, R=None, k=None):
        self.pid, self.kind, self.a_from, self.a_to = pid, kind, a_from, a_to
        self.xi, self.xj = xi, xj
        d = sub(xj, xi)
        self.chord_len = norm(d)
        cx = mul(ONE / self.chord_len, d)
        yp = sub(yref, mul(dot(yref, cx), cx))
        cy = unit(yp)
        cz = cross(cx, cy)
        self.chord_frame = (cx, cy, cz)
        self.k = ONE if kind == "straight" else D(k)
        if kind == "straight":
            self.L = self.chord_len
            self.kappa = ZERO
        else:
            self.R = D(R)
            h = self.chord_len / 2
            sag = (self.R * self.R - h * h).sqrt()
            self.c = sub(mul(D(1) / 2, add(xi, xj)), mul(sag, cy))
            ei = mul(ONE / self.R, sub(xi, self.c))
            ej = mul(ONE / self.R, sub(xj, self.c))
            nz = cross(ei, ej)
            self.zhat = unit(nz)
            self.Phi = atan2(norm(nz), dot(ei, ej))
            self.L = self.R * self.Phi
            self.kappa = ONE / self.R
            self.ei = ei
            self.yhat = cross(self.zhat, ei)

    def set_traversal(self, forward):
        self.forward = forward
        if self.kind == "straight":
            cx, cy, cz = self.chord_frame
            t0 = cx if forward else mul(-ONE, cx)
            n0 = cy
            self.frame0 = (t0, n0, cross(t0, n0))
        else:
            p0, p1 = (self.xi, self.xj) if forward else (self.xj, self.xi)
            b = unit(cross(sub(p0, self.c), sub(p1, self.c)))
            n0 = mul(ONE / self.R, sub(self.c, p0))
            t0 = cross(n0, b)
            self.frame0 = (t0, n0, b)

    def frame_at(self, s):
        """co-rotating traversal frame (t, n, b) at traversal arc length s."""
        if self.kind == "straight":
            return self.frame0
        t0, n0, b = self.frame0
        sn, cs = sincos(s * self.kappa)
        return (add(mul(cs, t0), mul(sn, n0)), add(mul(-sn, t0), mul(cs, n0)), b)

    def authored_frame(self, f):
        """reporting frame at authored fraction f: straight element-local; arc tangent frame."""
        if self.kind == "straight":
            return self.chord_frame
        sn, cs = sincos(D(f) * self.Phi)
        t = add(mul(-sn, self.ei), mul(cs, self.yhat))
        inward = mul(-ONE, add(mul(cs, self.ei), mul(sn, self.yhat)))
        return (t, inward, self.zhat)

    def system_matrix(self, sec, mat, w, P, eps0, wall=True):
        A = [[ZERO] * 16 for _ in range(16)]
        kap = self.kappa
        EA, GJ, EI = mat.E * sec.As, mat.G * sec.J, mat.E * sec.I
        k = self.k
        for base in (0, 3, 6, 9, 12):  # -w x v rows
            A[base + 0][base + 1] += kap
            A[base + 1][base + 0] -= kap
        # F' = ... - q ; q = w*g + wall (outward = -n, magnitude P/R)
        for i in range(3):
            A[i][12 + i] -= w
        if self.kind == "arc" and wall:
            A[1][15] += P / self.R
        # M' = ... - t x F = (0, F2, -F1)
        A[4][2] += ONE
        A[5][1] -= ONE
        # u' = ... + theta x t + t (N/EA + eps0) ; theta x t = (0, th2, -th1)
        A[6][0] += ONE / EA
        A[6][15] += eps0
        A[7][11] += ONE
        A[8][10] -= ONE
        # theta' = ... + (T/GJ, k My/EI, k Mz/EI)
        A[9][3] += ONE / GJ
        A[10][4] += k / EI
        A[11][5] += k / EI
        return A


def gdir_global():
    return (ZERO, ZERO, -ONE)
