"""T4-I9: emulation probe of T4-U1b's arc load-vector certificate (design only).

Standard library only (fractions, decimal, math). Run with `python -I`.
It is an emulation, not a product run: no Rust code is built or executed.

What it does, per case (an L line: straight 3 m, a realized bend, straight 4 m,
both ends anchored, a uniform global load on every member):
1. The certificate (DESIGN.md section 3): the arc's consistent uniform-load
   vector of T4-U1's objective element, evaluated in midpoint-radius ("ball")
   arithmetic. Midpoints are rounded to 128 significant bits, to nearest, ties
   to even (the Wide<2> p = 128 model); radii are exact rationals rounded up to
   binary64 after each operation. The flexibility inverse is verified by the
   residual test (rho = ||I - F X||_inf < 1/2). The arctangent midpoint is an
   accurate value rounded to 128 bits, and its radius uses K3a's proved
   atan_positive contract (21.54 u relative) plus the input radius.
2. An independent 70-digit Decimal reference (series sin/cos/atan of phi,
   not the half-angle identities) checks that every reference component lies
   inside its ball (the enclosure check).
3. Binary64 emulations of CB's `consistent_uniform_nodal_loads`:
   - "today": PP's absolute centre and CB's geometry (atan2, libm sin/cos,
     formula chord), as at ed012c7ccf;
   - "objective": T4-U1's sketch (d, R, plane normal; sin/cos from the half
     angle, phi = 2 atan2(s_h, c_h); H from the actual chord).
   The Gaussian elimination is a stand-in for FK `solve_dense`, so values are
   emulated, not bit-identical to the product.
4. The S11-G load-row statistic at the two free (junction) nodes: the bend's
   exact defect (binary64 value minus ball midpoint) plus the ball radius
   (DESIGN.md section 3.2), against RD(1e-9) * max(|n|, S*) with S11-G's free-row S*
   coupling. The straight members' terms are taken as exact (their S11-G
   records are unchanged by T4-U1b). Ratio >= 1 means the row fires.
   A bend-dominated variant uses 0.3 m straights.
5. Perturbed-vector controls at the free row where the bend's component is
   largest: the binary64 component moved by +2 T0 must fire, and by +T0/2
   must stay silent (T0 that row's threshold).
6. Extremes: phi = 0.1 deg, and k = 1e40 (the residual test fails: the
   certificate is refused and the terms stay CannotBound).
"""
from decimal import Decimal, getcontext
from fractions import Fraction as Q
import math
import sys

P = 128
U = Q(1, 2**P)            # unit roundoff of the 128-bit midpoints
ATAN_REL = Q(2154, 100)   # K3a atan_positive: (1.54 + 4k) u <= 21.54 u
INFLATE = Q(1)   # the radius enters B as it is (DESIGN.md section 3.2)
CRITERION = math.nextafter(1e-9, 0.0)   # RD(1e-9), as formation_guard.rs

# ------------------------------------------------------------ 128-bit model

def rnd(x):
    """x rounded to P significant bits, to nearest, ties to even."""
    if x == 0:
        return Q(0)
    sign = -1 if x < 0 else 1
    a = abs(x)
    n, d = a.numerator, a.denominator
    e = n.bit_length() - d.bit_length()
    if Q(n, d) < Q(2) ** e:
        e -= 1
    shift = P - 1 - e          # scale so that 2^(P-1) <= m < 2^P
    if shift >= 0:
        num, den = n << shift, d
    else:
        num, den = n, d << (-shift)
    m, r = divmod(num, den)
    twice = 2 * r
    if twice > den or (twice == den and (m & 1)):
        m += 1
    return sign * Q(m) / (Q(2) ** shift)


def up(x):
    """The smallest binary64 value >= x (x >= 0)."""
    x = Q(x)
    f = float(x)
    if Q(f) < x:
        f = math.nextafter(f, math.inf)
    return f


class Ball:
    __slots__ = ("m", "r")

    def __init__(self, m, r=0.0):
        self.m = Q(m)
        self.r = float(r)

    @staticmethod
    def lift(x):
        return Ball(Q(x), 0.0)

    def __neg__(self):
        return Ball(-self.m, self.r)


def b_add(a, b):
    m = rnd(a.m + b.m)
    return Ball(m, up(Q(a.r) + Q(b.r) + U * abs(m)))


def b_sub(a, b):
    return b_add(a, -b)


def b_mul(a, b):
    m = rnd(a.m * b.m)
    r = abs(a.m) * Q(b.r) + abs(b.m) * Q(a.r) + Q(a.r) * Q(b.r) + U * abs(m)
    return Ball(m, up(r))


def b_div(a, b):
    if abs(b.m) <= Q(b.r):
        raise ArithmeticError("divisor ball contains zero")
    m = rnd(a.m / b.m)
    r = (Q(a.r) + abs(a.m / b.m) * Q(b.r)) / (abs(b.m) - Q(b.r)) + U * abs(m)
    return Ball(m, up(r))


def isqrt_rounded(x):
    """sqrt(x) for x > 0 rounded to P bits, to nearest (exact decision)."""
    n, d = x.numerator, x.denominator
    e = (n.bit_length() - d.bit_length()) // 2
    k = P + 8 - e                       # result scaled by 2^k has ~P+8 bits
    if k >= 0:
        num, den = n << (2 * k), d
    else:
        num, den = n, d << (-2 * k)
    target = Q(num, den)
    s = math.isqrt(num // den)
    sticky = Q(s * s) != target
    # s <= sqrt(target) < s + 1; round s/2^k (with sticky) to P bits.
    bits = s.bit_length()
    drop = bits - P
    if drop <= 0:
        return Q(s, 1) / (Q(2) ** k) if not sticky else rnd(Q(2 * s + 1, 2) / (Q(2) ** k))
    m, rem = s >> drop, s & ((1 << drop) - 1)
    half = 1 << (drop - 1)
    if rem > half or (rem == half and (sticky or (m & 1))):
        m += 1
    return Q(m) * (Q(2) ** drop) / (Q(2) ** k)


def b_sqrt(a):
    if a.m - Q(a.r) <= 0:
        raise ArithmeticError("sqrt argument ball reaches zero")
    m = isqrt_rounded(a.m)
    r = Q(a.r) * (1 + U) / m + U * m
    return Ball(m, up(r))


def atan_decimal(x):
    """atan(x) for Decimal x > 0, by halving reductions and the series."""
    getcontext().prec = 90
    k = 0
    while x > Decimal("0.05"):
        x = x / (1 + (1 + x * x).sqrt())
        k += 1
    x2 = x * x
    term, total, n = x, x, 1
    eps = Decimal(10) ** -85
    while abs(term) > eps:
        term = -term * x2
        total += term / (2 * n + 1)
        n += 1
    return total * (2 ** k)


def q_to_dec(x):
    getcontext().prec = 90
    return Decimal(x.numerator) / Decimal(x.denominator)


def dec_to_q(x):
    return Q(x)


def b_atan(t):
    if t.m - Q(t.r) <= 0:
        raise ArithmeticError("atan argument ball not positive")
    m = rnd(dec_to_q(atan_decimal(q_to_dec(t.m))))
    r = Q(t.r) + ATAN_REL * U * m / (1 - ATAN_REL * U)
    return Ball(m, up(r))


def b_pow2(a, k):
    return Ball(a.m * (Q(2) ** k), float(Q(a.r) * (Q(2) ** k)) if a.r else 0.0)

# --------------------------------------------------- arithmetic "contexts"

class BallCtx:
    name = "ball"
    def lift(self, x): return Ball.lift(x)
    def add(self, a, b): return b_add(a, b)
    def sub(self, a, b): return b_sub(a, b)
    def mul(self, a, b): return b_mul(a, b)
    def div(self, a, b): return b_div(a, b)
    def sqrt(self, a): return b_sqrt(a)
    def neg(self, a): return -a
    def half(self, a): return b_pow2(a, -1)
    def zero(self): return Ball(Q(0))
    def one(self): return Ball(Q(1))

    def trig(self, s_h):
        """phi, sin, cos, sin 2phi, cos 2phi from the half-angle sine."""
        one = self.one()
        c_h = self.sqrt(self.sub(one, self.mul(s_h, s_h)))
        phi = b_pow2(b_atan(self.div(s_h, c_h)), 1)
        sin = b_pow2(self.mul(s_h, c_h), 1)
        cos = self.sub(one, b_pow2(self.mul(s_h, s_h), 1))
        sin2 = b_pow2(self.mul(sin, cos), 1)
        cos2 = self.sub(one, b_pow2(self.mul(sin, sin), 1))
        return c_h, phi, sin, cos, sin2, cos2


class DecCtx:
    name = "decimal"
    def __init__(self):
        getcontext().prec = 70
    def lift(self, x): return Decimal(x)
    def add(self, a, b): return a + b
    def sub(self, a, b): return a - b
    def mul(self, a, b): return a * b
    def div(self, a, b): return a / b
    def sqrt(self, a): return a.sqrt()
    def neg(self, a): return -a
    def half(self, a): return a / 2
    def zero(self): return Decimal(0)
    def one(self): return Decimal(1)

    @staticmethod
    def sin_cos(x):
        getcontext().prec = 80
        s, c = Decimal(0), Decimal(0)
        term = x
        n = 1
        while abs(term) > Decimal(10) ** -78:
            s += term
            term = -term * x * x / ((n + 1) * (n + 2))
            n += 2
        term = Decimal(1)
        n = 0
        while abs(term) > Decimal(10) ** -78:
            c += term
            term = -term * x * x / ((n + 1) * (n + 2))
            n += 2
        getcontext().prec = 70
        return +s, +c

    def trig(self, s_h):
        c_h = (1 - s_h * s_h).sqrt()
        getcontext().prec = 90
        phi = 2 * atan_decimal(s_h / c_h)
        getcontext().prec = 70
        phi = +phi
        sin, cos = self.sin_cos(phi)
        sin2, cos2 = self.sin_cos(2 * phi)
        return c_h, phi, sin, cos, sin2, cos2

# ------------------------------------------------ the formula (T4-U1/U1b)

def formula(ctx, xi, xj, radius, yref, em, gm, area, inertia, torsion, kin, kout, w):
    """Consistent uniform-load vector (global, [node i; node j]) of the
    objective arc, written once for any arithmetic context."""
    L = ctx.lift
    d = [ctx.sub(L(xj[k]), L(xi[k])) for k in range(3)]
    dd = ctx.add(ctx.add(ctx.mul(d[0], d[0]), ctx.mul(d[1], d[1])), ctx.mul(d[2], d[2]))
    length = ctx.sqrt(dd)
    R = L(radius)
    s_h = ctx.div(ctx.half(length), R)
    c_h, phi, s, c, s2, c2 = ctx.trig(s_h)
    dh = [ctx.div(d[k], length) for k in range(3)]
    y = [L(v) for v in yref]
    proj = ctx.add(ctx.add(ctx.mul(y[0], dh[0]), ctx.mul(y[1], dh[1])), ctx.mul(y[2], dh[2]))
    nr = [ctx.sub(y[k], ctx.mul(proj, dh[k])) for k in range(3)]
    nn = ctx.sqrt(ctx.add(ctx.add(ctx.mul(nr[0], nr[0]), ctx.mul(nr[1], nr[1])), ctx.mul(nr[2], nr[2])))
    nh = [ctx.div(nr[k], nn) for k in range(3)]
    ex = [ctx.add(ctx.neg(ctx.mul(s_h, dh[k])), ctx.mul(c_h, nh[k])) for k in range(3)]

    def cross(a, b):
        return [ctx.sub(ctx.mul(a[1], b[2]), ctx.mul(a[2], b[1])),
                ctx.sub(ctx.mul(a[2], b[0]), ctx.mul(a[0], b[2])),
                ctx.sub(ctx.mul(a[0], b[1]), ctx.mul(a[1], b[0]))]

    def dot(a, b):
        return ctx.add(ctx.add(ctx.mul(a[0], b[0]), ctx.mul(a[1], b[1])), ctx.mul(a[2], b[2]))

    ez = cross(nh, dh)
    ey = cross(ez, ex)
    axes = [ex, ey, ez]
    wl = [dot(axes[a], [L(v) for v in w]) for a in range(3)]
    chord = [dot(axes[a], d) for a in range(3)]          # actual chord, local

    one, zero = ctx.one(), ctx.zero()
    Rs, Rc = ctx.mul(R, s), ctx.mul(R, c)
    z3 = [zero, zero, zero]
    cases = [
        ([ctx.neg(Rs), zero, R], z3, z3, [zero, zero, ctx.neg(one)]),
        ([Rc, ctx.neg(R), zero], z3, z3, [zero, one, zero]),
        (z3, [zero, Rs, ctx.neg(Rc)], [R, ctx.neg(Rc), ctx.neg(Rs)], z3),
        (z3, [zero, one, zero], [zero, zero, ctx.neg(one)], z3),
        (z3, [zero, zero, one], [zero, one, zero], z3),
        ([one, zero, zero], z3, z3, z3),
    ]
    one_c = ctx.sub(one, c)
    half_phi = ctx.half(phi)
    q_s2 = ctx.half(ctx.half(s2))
    half_ss = ctx.half(ctx.mul(s, s))
    gram = [[phi, s, one_c],
            [s, ctx.add(half_phi, q_s2), half_ss],
            [one_c, half_ss, ctx.sub(half_phi, q_s2)]]
    phi_s = ctx.mul(phi, s)
    phi_c = ctx.mul(phi, c)
    i_tc = ctx.sub(ctx.add(phi_s, c), one)
    i_ts = ctx.sub(s, phi_c)
    phi2_4 = ctx.half(ctx.half(ctx.mul(phi, phi)))
    phi_s2_4 = ctx.half(ctx.half(ctx.mul(phi, s2)))
    c2m1_8 = ctx.half(ctx.half(ctx.half(ctx.sub(c2, one))))
    i_tcc = ctx.add(ctx.add(phi2_4, phi_s2_4), c2m1_8)
    i_tss = ctx.sub(ctx.sub(phi2_4, phi_s2_4), c2m1_8)
    i_tsc = ctx.sub(ctx.half(ctx.half(ctx.half(s2))), ctx.half(ctx.half(ctx.mul(phi, c2))))
    egram = [[phi, s, one_c, ctx.half(ctx.mul(phi, phi)), i_tc, i_ts],
             [s, ctx.add(half_phi, q_s2), half_ss, i_tc, i_tcc, i_tsc],
             [one_c, half_ss, ctx.sub(half_phi, q_s2), i_ts, i_tsc, i_tss]]
    R2 = ctx.mul(R, R)
    wx, wy, wz = wl
    a_x = [s, ctx.neg(phi), ctx.neg(one), zero, one, zero]
    a_y = [ctx.neg(c), one, ctx.neg(phi), zero, zero, one]
    ld_ip = [ctx.mul(R2, ctx.sub(ctx.mul(wy, a_x[k]), ctx.mul(wx, a_y[k]))) for k in range(6)]
    R2wz = ctx.mul(R2, wz)
    ld_op = [R2wz, ctx.neg(ctx.mul(R2wz, c)), ctx.neg(ctx.mul(R2wz, s)), zero, zero, zero]
    ld_t = [ctx.mul(R2wz, phi), ctx.neg(ctx.mul(R2wz, s)), ctx.mul(R2wz, c), ctx.neg(R2wz), zero, zero]
    Rwy, Rwx = ctx.mul(R, wy), ctx.mul(R, wx)
    ld_ax = [zero, ctx.mul(Rwy, phi), ctx.neg(ctx.mul(Rwx, phi)), zero, ctx.neg(Rwy), Rwx]

    def quad(g, left, right, ncol):
        total = zero
        for r in range(3):
            for k in range(ncol):
                total = ctx.add(total, ctx.mul(ctx.mul(left[r], g[r][k]), right[k]))
        return total

    EI = ctx.mul(L(em), L(inertia))
    GJ = ctx.mul(L(gm), L(torsion))
    EA = ctx.mul(L(em), L(area))
    fin, fout = L(kin), L(kout)

    def energy(qi, qo, qt, qa):
        t = ctx.add(ctx.div(ctx.mul(fin, qi), EI), ctx.div(ctx.mul(fout, qo), EI))
        t = ctx.add(ctx.add(t, ctx.div(qt, GJ)), ctx.div(qa, EA))
        return ctx.mul(R, t)

    F = [[None] * 6 for _ in range(6)]
    for r in range(6):
        for k in range(r, 6):
            v = energy(*(quad(gram, cases[r][j], cases[k][j], 3) for j in range(4)))
            F[r][k] = v
            F[k][r] = v
    delta = [energy(quad(egram, cases[r][0], ld_ip, 6), quad(egram, cases[r][1], ld_op, 6),
                    quad(egram, cases[r][2], ld_t, 6), quad(egram, cases[r][3], ld_ax, 6))
             for r in range(6)]
    K = invert(ctx, F)
    X = [zero] * 6
    for r in range(6):
        for k in range(6):
            X[r] = ctx.sub(X[r], ctx.mul(K[r][k], delta[k]))
    arm = [ctx.mul(R2, ctx.sub(s, phi)), ctx.mul(R2, one_c), zero]
    mom = cross(arm, wl)
    Rphi = ctx.mul(R, phi)
    W = [ctx.mul(Rphi, wl[a]) for a in range(3)] + mom
    H = [[one if r == k else zero for k in range(6)] for r in range(6)]
    H[3][1], H[3][2] = ctx.neg(chord[2]), chord[1]
    H[4][0], H[4][2] = chord[2], ctx.neg(chord[0])
    H[5][0], H[5][1] = ctx.neg(chord[1]), chord[0]
    local = [zero] * 12
    for r in range(6):
        t = zero
        for k in range(6):
            t = ctx.add(t, ctx.mul(H[r][k], X[k]))
        local[r] = ctx.add(t, W[r])
        local[6 + r] = ctx.neg(X[r])
    out = []
    for blk in range(4):
        loc = local[3 * blk:3 * blk + 3]
        for comp in range(3):
            g = zero
            for a in range(3):
                g = ctx.add(g, ctx.mul(axes[a][comp], loc[a]))
            out.append(g)
    return out, F


def invert(ctx, F):
    if ctx.name == "decimal":
        return gauss_jordan(F, lambda a, b: a + b, lambda a, b: a - b,
                            lambda a, b: a * b, lambda a, b: a / b, Decimal(0), Decimal(1))
    # Ball: approximate inverse of the midpoints at 128 bits, then the residual test.
    mid = [[F[r][k].m for k in range(6)] for r in range(6)]
    Xt = gauss_jordan(mid, lambda a, b: rnd(a + b), lambda a, b: rnd(a - b),
                      lambda a, b: rnd(a * b), lambda a, b: rnd(a / b), Q(0), Q(1))
    rho = Q(0)
    for r in range(6):
        row = Q(0)
        for k in range(6):
            acc = Ball(Q(1) if r == k else Q(0))
            for j in range(6):
                acc = b_sub(acc, b_mul(F[r][j], Ball(Xt[j][k])))
            row += abs(acc.m) + Q(acc.r)
        rho = max(rho, row)
    rho_up = up(rho)
    if rho_up >= 0.5:
        raise ArithmeticError("flexibility inverse not certified: rho=%g" % rho_up)
    norm_x = up(max(sum(abs(Xt[r][k]) for k in range(6)) for r in range(6)))
    rad = up(Q(norm_x) * Q(rho_up) / (1 - Q(rho_up)))
    invert.last_rho = rho_up
    return [[Ball(Xt[r][k], rad) for k in range(6)] for r in range(6)]


def gauss_jordan(Fm, add, sub, mul, div, zero, one):
    n = 6
    m = [row[:] for row in Fm]
    inv = [[one if r == k else zero for k in range(n)] for r in range(n)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(m[r][col]))
        m[col], m[piv] = m[piv], m[col]
        inv[col], inv[piv] = inv[piv], inv[col]
        p = m[col][col]
        m[col] = [div(v, p) for v in m[col]]
        inv[col] = [div(v, p) for v in inv[col]]
        for r in range(n):
            if r == col or m[r][col] == 0:
                continue
            f = m[r][col]
            m[r] = [sub(m[r][k], mul(f, m[col][k])) for k in range(n)]
            inv[r] = [sub(inv[r][k], mul(f, inv[col][k])) for k in range(n)]
    return inv

# --------------------------------------------- binary64 emulations of CB

def solve6(Fm, rhs):
    n = 6
    a = [Fm[r][:] + [rhs[r]] for r in range(n)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(a[r][col]))
        a[col], a[piv] = a[piv], a[col]
        for r in range(col + 1, n):
            f = a[r][col] / a[col][col]
            for k in range(col, n + 1):
                a[r][k] -= f * a[col][k]
    x = [0.0] * n
    for r in reversed(range(n)):
        s = a[r][n]
        for k in range(r + 1, n):
            s -= a[r][k] * x[k]
        x[r] = s / a[r][r]
    return x


def cb_vector(axes, radius, phi, s, c, s2, c2, chord, em, gm, area, inertia, torsion, kin, kout, w):
    """CB's consistent_uniform_nodal_loads in binary64 (operation order as
    CB, Gaussian elimination standing in for FK solve_dense)."""
    dot = lambda a, b: a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
    wl = [dot(axes[0], w), dot(axes[1], w), dot(axes[2], w)]
    R = radius
    cases = [
        ([-R * s, 0.0, R], [0.0] * 3, [0.0] * 3, [0.0, 0.0, -1.0]),
        ([R * c, -R, 0.0], [0.0] * 3, [0.0] * 3, [0.0, 1.0, 0.0]),
        ([0.0] * 3, [0.0, R * s, -R * c], [R, -R * c, -R * s], [0.0] * 3),
        ([0.0] * 3, [0.0, 1.0, 0.0], [0.0, 0.0, -1.0], [0.0] * 3),
        ([0.0] * 3, [0.0, 0.0, 1.0], [0.0, 1.0, 0.0], [0.0] * 3),
        ([1.0, 0.0, 0.0], [0.0] * 3, [0.0] * 3, [0.0] * 3),
    ]
    gram = [[phi, s, 1.0 - c], [s, 0.5 * phi + 0.25 * s2, 0.5 * s * s], [1.0 - c, 0.5 * s * s, 0.5 * phi - 0.25 * s2]]
    itc = phi * s + c - 1.0
    its = s - phi * c
    itcc = 0.25 * phi * phi + 0.25 * phi * s2 + 0.125 * (c2 - 1.0)
    itss = 0.25 * phi * phi - 0.25 * phi * s2 - 0.125 * (c2 - 1.0)
    itsc = 0.125 * s2 - 0.25 * phi * c2
    eg = [[phi, s, 1.0 - c, 0.5 * phi * phi, itc, its],
          [s, 0.5 * phi + 0.25 * s2, 0.5 * s * s, itc, itcc, itsc],
          [1.0 - c, 0.5 * s * s, 0.5 * phi - 0.25 * s2, its, itsc, itss]]
    wx, wy, wz = wl
    R2 = R * R
    ax_ = [s, -phi, -1.0, 0.0, 1.0, 0.0]
    ay_ = [-c, 1.0, -phi, 0.0, 0.0, 1.0]
    ld = ([R2 * (wy * ax_[k] - wx * ay_[k]) for k in range(6)],
          [R2 * wz, -R2 * wz * c, -R2 * wz * s, 0.0, 0.0, 0.0],
          [R2 * wz * phi, -R2 * wz * s, R2 * wz * c, -R2 * wz, 0.0, 0.0],
          [0.0, R * wy * phi, -R * wx * phi, 0.0, -R * wy, R * wx])

    def quad(g, l, r, n):
        t = 0.0
        for i in range(3):
            for k in range(n):
                t += l[i] * g[i][k] * r[k]
        return t

    EI, GJ, EA = em * inertia, gm * torsion, em * area

    def energy(qi, qo, qt, qa):
        return R * (kin * qi / EI + kout * qo / EI + qt / GJ + qa / EA)

    F = [[0.0] * 6 for _ in range(6)]
    for r in range(6):
        for k in range(r, 6):
            v = energy(*(quad(gram, cases[r][j], cases[k][j], 3) for j in range(4)))
            F[r][k] = F[k][r] = v
    delta = [energy(*(quad(eg, cases[r][j], ld[j], 6) for j in range(4))) for r in range(6)]
    K = [[0.0] * 6 for _ in range(6)]
    for col in range(6):
        e = [0.0] * 6
        e[col] = 1.0
        x = solve6(F, e)
        for r in range(6):
            K[r][col] = x[r]
    for r in range(6):
        for k in range(r + 1, 6):
            a = 0.5 * (K[r][k] + K[k][r])
            K[r][k] = K[k][r] = a
    X = [0.0] * 6
    for r in range(6):
        for k in range(6):
            X[r] -= K[r][k] * delta[k]
    arm = [R2 * (s - phi), R2 * (1.0 - c), 0.0]
    mom = [arm[1] * wl[2] - arm[2] * wl[1], arm[2] * wl[0] - arm[0] * wl[2], arm[0] * wl[1] - arm[1] * wl[0]]
    W = [R * phi * wl[0], R * phi * wl[1], R * phi * wl[2]] + mom
    H = [[1.0 if r == k else 0.0 for k in range(6)] for r in range(6)]
    H[3][1], H[3][2] = -chord[2], chord[1]
    H[4][0], H[4][2] = chord[2], -chord[0]
    H[5][0], H[5][1] = -chord[1], chord[0]
    local = [0.0] * 12
    for r in range(6):
        t = 0.0
        for k in range(6):
            t += H[r][k] * X[k]
        local[r] = t + W[r]
        local[6 + r] = -X[r]
    out = []
    for blk in range(4):
        loc = local[3 * blk:3 * blk + 3]
        g = [0.0, 0.0, 0.0]
        for a in range(3):
            for comp in range(3):
                g[comp] += axes[a][comp] * loc[a]
        out.extend(g)
    return out


def norm(v):
    return math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])


def sub3(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]


def cross3(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def objective_binary64(xi, xj, R, yref, mat, w, libm_trig):
    d = sub3(xj, xi)
    L = norm(d)
    s_h = (0.5 * L) / R
    c_h = math.sqrt(1.0 - s_h * s_h)
    phi = 2.0 * math.atan2(s_h, c_h)
    if libm_trig:
        s, c, s2, c2 = math.sin(phi), math.cos(phi), math.sin(2 * phi), math.cos(2 * phi)
    else:
        s, c = 2.0 * s_h * c_h, 1.0 - 2.0 * s_h * s_h
        s2, c2 = 2.0 * s * c, 1.0 - 2.0 * s * s
    dh = [v / L for v in d]
    pr = yref[0] * dh[0] + yref[1] * dh[1] + yref[2] * dh[2]
    nr = [yref[k] - pr * dh[k] for k in range(3)]
    nm = norm(nr)
    nh = [v / nm for v in nr]
    ex = [-s_h * dh[k] + c_h * nh[k] for k in range(3)]
    ez = cross3(nh, dh)
    ey = cross3(ez, ex)
    axes = [ex, ey, ez]
    chord = [sum(axes[a][k] * d[k] for k in range(3)) for a in range(3)]
    return cb_vector(axes, R, phi, s, c, s2, c2, chord, *mat, w)


def today_binary64(xi, xj, R, yref, mat, w):
    d = sub3(xj, xi)
    L = math.sqrt(d[0] * d[0] + d[1] * d[1] + d[2] * d[2])
    half = 0.5 * L
    du = [d[0] / L, d[1] / L, d[2] / L]
    ax = yref[0] * du[0] + yref[1] * du[1] + yref[2] * du[2]
    pn = [yref[k] - ax * du[k] for k in range(3)]
    pm = math.sqrt(pn[0] * pn[0] + pn[1] * pn[1] + pn[2] * pn[2])
    sag = math.sqrt(R * R - half * half)
    centre = [0.5 * (xi[k] + xj[k]) - sag * pn[k] / pm for k in range(3)]
    ri, rj = sub3(xi, centre), sub3(xj, centre)
    nri, nrj = norm(ri), norm(rj)
    if abs(nri - nrj) > 1e-9 * max(nri, nrj):
        return None
    radius = 0.5 * (nri + nrj)
    pl = cross3(ri, rj)
    phi = math.atan2(norm(pl), ri[0] * rj[0] + ri[1] * rj[1] + ri[2] * rj[2])
    ex = [v / nri for v in ri]
    ez = [v / norm(pl) for v in pl]
    ey = cross3(ez, ex)
    s, c = math.sin(phi), math.cos(phi)
    chord = [radius * (c - 1.0), radius * s, 0.0]
    return cb_vector([ex, ey, ez], radius, phi, s, c, math.sin(2 * phi), math.cos(2 * phi), chord, *mat, w)

# ------------------------------------------------------ the L line forecast

def straight_terms(p, q, w):
    """Exact consistent loads of a straight member (global): f = wL/2 at each
    end; m_i = (L^2/12) x x w, m_j = -m_i (x from i to j)."""
    d = sub3(q, p)
    L = norm(d)
    x = [v / L for v in d]
    f = [Q(wk) * Q(L) / 2 for wk in w]
    mx = cross3(x, w)
    m = [Q(mk) * Q(L) * Q(L) / 12 for mk in mx]
    return f + m, f + [-v for v in m]


def section(od, wall):
    ro, ri = od / 2, od / 2 - wall
    area = math.pi * (ro * ro - ri * ri)
    inertia = math.pi * (ro ** 4 - ri ** 4) / 4
    return area, inertia, 2 * inertia


def run_case(phi_deg, offset, w, k, label, l1=3.0, l2=4.0):
    R = 0.2286
    phi = math.radians(phi_deg)
    loc = {
        "A": [0.0, 0.0, 0.0],
        "B": [l1, 0.0, 0.0],
        "C": [l1 + R * math.sin(phi), R * (1.0 - math.cos(phi)), 0.0],
    }
    tj = [math.cos(phi), math.sin(phi), 0.0]
    loc["D"] = [loc["C"][i] + l2 * tj[i] for i in range(3)]
    X = {n: [loc[n][i] + offset[i] for i in range(3)] for n in loc}
    yref = [0.0, -1.0, 0.0]
    em = 2.03e11
    gm = em / (2.0 * 1.3)
    area, inertia, torsion = section(0.1683, 0.00711)
    mat = (em, gm, area, inertia, torsion, k, k)
    xi, xj = X["B"], X["C"]
    # Certificate (ball) and reference.
    try:
        ball, Fb = formula(BallCtx(), xi, xj, R, yref, em, gm, area, inertia, torsion, k, k, w)
        rho = invert.last_rho
    except ArithmeticError as error:
        return {"label": label, "certificate": "CannotBound (%s)" % error}
    ref, _ = formula(DecCtx(), xi, xj, R, yref, em, gm, area, inertia, torsion, k, k, w)
    enclosed = all(abs(Q(ref[i]) - ball[i].m) <= Q(ball[i].r) for i in range(12))
    scale = max(abs(float(b.m)) for b in ball)
    rad_rel = max(b.r for b in ball) / scale
    # Binary64 vectors.
    vecs = {
        "objective": objective_binary64(xi, xj, R, yref, mat, w, libm_trig=False),
        "objective_libm": objective_binary64(xi, xj, R, yref, mat, w, libm_trig=True),
        "today": today_binary64(xi, xj, R, yref, mat, w),
    }
    # Straight members A-B and C-D (exact terms).
    ab_i, ab_j = straight_terms(X["A"], X["B"], w)
    cd_i, cd_j = straight_terms(X["C"], X["D"], w)
    straight_B = ab_j          # node B: end j of A-B
    straight_C = cd_i          # node C: end i of C-D
    body_extent = math.sqrt(sum((max(X[n][a] for n in X) - min(X[n][a] for n in X)) ** 2 for a in range(3)))
    out = {"label": label, "rho": rho, "enclosed": enclosed, "radius_rel": rad_rel}
    for name, v in vecs.items():
        if v is None:
            out[name] = "refused (radius mismatch > 1e-9)"
            continue
        defect_rel = max(abs(Q(v[i]) - ball[i].m) for i in range(12)) / Q(scale)
        out[name + "_defect_rel"] = float(defect_rel)
        out[name] = guard_ratio(v, ball, straight_B, straight_C, body_extent)
    v = vecs["objective"]
    i_max = max(range(12), key=lambda i: abs(ball[i].m))
    t0 = row_threshold(ball, straight_B, straight_C, body_extent, i_max)
    fired = []
    for factor in (Q(2), Q(1, 2)):
        vp = list(v)
        vp[i_max] = float(Q(v[i_max]) + factor * t0)
        fired.append(guard_ratio(vp, ball, straight_B, straight_C, body_extent) >= 1.0)
    out["perturbed"] = "+2T0 fires=%s, +T0/2 fires=%s" % tuple(fired)
    return out


def row_threshold(ball, sB, sC, extent, index):
    """T0 of free row `index` (0..11), as `guard_ratio` forms it."""
    return guard_rows(None, ball, sB, sC, extent)[index]


def guard_rows(v, ball, sB, sC, extent):
    rows = []
    for node, (sterms, offs) in enumerate([(sB, 0), (sC, 6)]):
        for dof in range(6):
            i = offs + dof
            rows.append((dof, sterms[dof] + ball[i].m))
    F = max(abs(r[1]) for r in rows if r[0] < 3)
    M = max(abs(r[1]) for r in rows if r[0] >= 3)
    fo, mo = max(F, M / Q(extent)), max(M, Q(extent) * F)
    return [Q(CRITERION) * max(abs(n), mo if dof >= 3 else fo) for dof, n in rows]


def guard_ratio(v, ball, sB, sC, extent):
    """Max S11-G load-row statistic over the 12 free rows (nodes B, C)."""
    rows = []
    for node, (sterms, offs) in enumerate([(sB, 0), (sC, 6)]):
        for dof in range(6):
            i = offs + dof
            intended = sterms[dof] + ball[i].m
            defect = Q(v[i]) - ball[i].m
            bound = Q(up(Q(ball[i].r) * INFLATE))
            rows.append((dof, intended, defect, bound))
    F = max(abs(r[1]) for r in rows if r[0] < 3)
    M = max(abs(r[1]) for r in rows if r[0] >= 3)
    fo, mo = max(F, M / Q(extent)), max(M, Q(extent) * F)
    worst = 0.0
    for dof, intended, defect, bound in rows:
        s_star = mo if dof >= 3 else fo
        t0 = Q(CRITERION) * max(abs(intended), s_star)
        worst = max(worst, float((abs(defect) + bound) / t0))
    return worst


def main():
    getcontext().prec = 70
    print("T4-I9 arc certificate probe (emulation; python %s)" % sys.version.split()[0])
    print("L line: straight 3 m, bend R = 0.2286 m, straight 4 m; OD 168.3 mm, t 7.11 mm;")
    print("E = 2.03e11 Pa, nu = 0.3; both ends anchored; uniform load on every member.")
    print("Columns: rho = ||I - F X||_inf (certified < 1/2); enclosed = reference inside every ball;")
    print("rad = max ball radius / max |component|; defect = max |v - mid| / max |component|;")
    print("guard = max S11-G load-row statistic / threshold over the 12 free rows (>= 1 fires).")
    print()
    loads = {"self-weight -z": [0.0, 0.0, -450.0], "in-plane -y": [0.0, -450.0, 0.0]}
    offsets = {"origin": [0.0, 0.0, 0.0], "UTM 5e6/3.5e6": [5.0e6, 3.5e6, 0.0], "UTM 7.3e6": [7.3e6, 0.0, 0.0]}
    for lname, w in loads.items():
        for oname, off in offsets.items():
            for phi_deg in (90.0, 45.0, 15.0, 5.0, 1.0, 0.1):
                for k in (1.0, 2.0):
                    label = "%s | %s | phi=%g deg | k=%g" % (lname, oname, phi_deg, k)
                    r = run_case(phi_deg, off, w, k, label)
                    if "certificate" in r:
                        print(label, "|", r["certificate"])
                        continue
                    parts = [label,
                             "rho=%.2e" % r["rho"],
                             "enclosed=%s" % r["enclosed"],
                             "rad=%.1e" % r["radius_rel"]]
                    for name in ("objective", "objective_libm", "today"):
                        if isinstance(r[name], str):
                            parts.append("%s: %s" % (name, r[name]))
                        else:
                            parts.append("%s: defect=%.1e guard=%.1e" % (name, r[name + "_defect_rel"], r[name]))
                    parts.append("perturbed: %s" % r["perturbed"])
                    print(" | ".join(parts))
    print()
    print("Bend-dominated body: straights 0.3 m and 0.3 m (self-weight -z, k = 1)")
    for oname, off in offsets.items():
        for phi_deg in (45.0, 15.0, 5.0, 1.0):
            label = "short | %s | phi=%g deg" % (oname, phi_deg)
            r = run_case(phi_deg, off, loads["self-weight -z"], 1.0, label, 0.3, 0.3)
            print(" | ".join([label, "enclosed=%s" % r["enclosed"],
                              "objective: defect=%.1e guard=%.1e" % (r["objective_defect_rel"], r["objective"]),
                              "perturbed: %s" % r["perturbed"]]))
    print()
    print("Extreme: k = 1e40 (cond(F) beyond the residual test)")
    for oname, off in offsets.items():
        label = "self-weight -z | %s | phi=90 deg | k=1e40" % oname
        r = run_case(90.0, off, loads["self-weight -z"], 1e40, label)
        print(label, "|", r.get("certificate", "certified (unexpected)"))
    print()
    print("done")


if __name__ == "__main__":
    main()
