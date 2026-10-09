"""RV131: binary p-bit arithmetic emulation (round to nearest, ties to even) with Fractions,
for K-D5's Wide<2> (p = 128) re-formation of the B1 element and for M31b0's chord comparison.

This is an emulation of the arithmetic class, not a port of any Rust code. Square roots
are rounded from a 64-bit-extended integer square root (double-rounding probability about
2^-64, immaterial here). The arctangent is evaluated in Decimal at 80 digits and rounded
once (K-D5's K3a included angle is accurate to about an ulp).
"""
from fractions import Fraction as Fr
from decimal import Decimal as D, localcontext
import math


class P:
    def __init__(self, p):
        self.p = p

    def r(self, x):
        x = Fr(x)
        if x == 0:
            return x
        sign = -1 if x < 0 else 1
        a = -x if x < 0 else x
        n, d = a.numerator, a.denominator
        e = n.bit_length() - d.bit_length()
        # 2^e <= a < 2^(e+1)
        if (n << max(0, -e)) < (d << max(0, e)):
            e -= 1
        sh = self.p - 1 - e
        num = n << sh if sh >= 0 else n
        den = d if sh >= 0 else d << (-sh)
        q, rem = divmod(num, den)
        twice = 2 * rem
        if twice > den or (twice == den and q & 1):
            q += 1
        return sign * Fr(q, 1) * (Fr(2) ** (-sh) if sh >= 0 else Fr(2) ** (-sh))

    def add(self, a, b):
        return self.r(a + b)

    def sub(self, a, b):
        return self.r(a - b)

    def mul(self, a, b):
        return self.r(a * b)

    def div(self, a, b):
        return self.r(Fr(a) / Fr(b))

    def sqrt(self, a):
        a = Fr(a)
        if a == 0:
            return a
        k = self.p + 64
        n, d = a.numerator, a.denominator
        # floor(sqrt(a) * 2^K) for K chosen so that the result has >= p+64 bits
        e = (n.bit_length() - d.bit_length()) // 2
        K = k - e
        s = math.isqrt((n << (2 * K)) // d) if K >= 0 else math.isqrt(n // (d << (-2 * K)))
        return self.r(Fr(s, 1) / (Fr(2) ** K))

    def atan2_q1(self, y, x):
        with localcontext() as c:
            c.prec = 80
            yd = D(y.numerator) / D(y.denominator)
            xd = D(x.numerator) / D(x.denominator)
            v = _atan2_dec(yd, xd)
        return self.r(Fr(v))

    def dot3(self, a, b):
        p0 = self.mul(a[0], b[0])
        p1 = self.mul(a[1], b[1])
        p2 = self.mul(a[2], b[2])
        return self.add(self.add(p0, p1), p2)

    def cross3(self, a, b):
        def c(p, q):
            return self.sub(self.mul(a[p], b[q]), self.mul(a[q], b[p]))
        return [c(1, 2), c(2, 0), c(0, 1)]


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


def _pi():
    with localcontext() as c:
        c.prec += 10
        v = 16 * _atan_small(D(1) / 5) - 4 * _atan_small(D(1) / 239)
    return +v


def _atan_dec(x):
    with localcontext() as c:
        c.prec += 12
        if x > 1:
            return +(_pi() / 2 - _atan_dec(1 / x))
        k, y = 0, x
        while y > D("1e-4"):
            y = y / (1 + (1 + y * y).sqrt())
            k += 1
        r = _atan_small(y) * (2 ** k)
    return +r


def _atan2_dec(y, x):
    assert y >= 0 and x >= 0
    if x == 0:
        return _pi() / 2
    return _atan_dec(y / x)


def kd5_curved_at_p(ar, xi, xj, R, y, E, G, A, I, J, kin, kout, variant="closed", chord_mode="actual"):
    """B1's element re-formed at precision ar.p in K-D5's operation order (formation_check.rs
    curved_matrix steps 2-6, with B1's objective inputs (R, y) in place of the centre).
    variant: 'closed'  -> cos = 1 - 2 s^2 rounded, one_minus_cos = 1 - cos (K-D5's form);
             'stable'  -> one_minus_cos = 2 s^2 rounded once, cos = 1 - one_minus_cos.
    chord_mode: 'actual' -> H from A.d at p (the definition);
                'formula_p' -> H from (R(cos-1), R sin, 0) at p (M31b0).
    Returns (12x12 global K as Fractions, dict of intermediates)."""
    r = ar
    xi = [Fr(v) for v in xi]
    xj = [Fr(v) for v in xj]
    y = [Fr(v) for v in y]
    R = Fr(R)
    d = [r.sub(xj[k], xi[k]) for k in range(3)]
    L = r.sqrt(r.dot3(d, d))
    twoR = 2 * R  # exact
    s = r.div(L, twoR)
    c = r.div(r.sqrt(r.mul(r.sub(twoR, L), r.add(twoR, L))), twoR)
    half = r.atan2_q1(s, c)
    phi = 2 * half  # exact scaling
    if variant == "closed":
        cos = r.sub(1, 2 * r.mul(s, s))
        omc = r.sub(1, cos)
    elif variant == "stable":
        omc = 2 * r.mul(s, s)
        cos = r.sub(1, omc)
    else:
        raise ValueError(variant)
    sin = 2 * r.mul(s, c)
    sc = r.mul(sin, cos)
    sin2 = 2 * sc
    ss = r.mul(sin, sin)
    half_ss = ss / 2
    half_phi = phi / 2
    quarter_sin2 = sin2 / 4
    gram = [[phi, sin, omc],
            [sin, r.add(half_phi, quarter_sin2), half_ss],
            [omc, half_ss, r.sub(half_phi, quarter_sin2)]]
    rs = r.mul(R, sin)
    rc = r.mul(R, cos)
    z = Fr(0)
    z3 = [z, z, z]
    one = Fr(1)
    cases = [
        [[-rs, z, R], z3, z3, [z, z, -one]],
        [[rc, -R, z], z3, z3, [z, one, z]],
        [z3, [z, rs, -rc], [R, -rc, -rs], z3],
        [z3, [z, one, z], [z, z, -one], z3],
        [z3, [z, z, one], [z, one, z], z3],
        [[one, z, z], z3, z3, z3],
    ]

    def quad(left, right):
        acc = Fr(0)
        for i in range(3):
            if left[i] == 0:
                continue
            for j in range(3):
                if right[j] == 0 or gram[i][j] == 0:
                    continue
                t = r.mul(r.mul(left[i], gram[i][j]), right[j])
                acc = r.add(acc, t)
        return acc

    E, G, A, I, J, kin, kout = (Fr(v) for v in (E, G, A, I, J, kin, kout))
    bending = r.mul(E, I)
    torsion = r.mul(G, J)
    axial = r.mul(E, A)
    F = [[Fr(0)] * 6 for _ in range(6)]
    for a in range(6):
        for b in range(a, 6):
            t_in = r.div(r.mul(kin, quad(cases[a][0], cases[b][0])), bending)
            t_out = r.div(r.mul(kout, quad(cases[a][1], cases[b][1])), bending)
            t_t = r.div(quad(cases[a][2], cases[b][2]), torsion)
            t_a = r.div(quad(cases[a][3], cases[b][3]), axial)
            v = r.mul(R, r.add(r.add(r.add(t_in, t_out), t_t), t_a))
            F[a][b] = v
            F[b][a] = v
    tip = invert6(r, F)
    # axes (B1): dhat, n from y, e_x = -s dhat + c n, e_y = c dhat + s n, e_z = n x dhat
    dh = [r.div(d[k], L) for k in range(3)]
    proj = r.dot3(y, dh)
    yc = [r.sub(y[k], r.mul(proj, dh[k])) for k in range(3)]
    ym = r.sqrt(r.dot3(yc, yc))
    n = [r.div(yc[k], ym) for k in range(3)]
    ex = [r.add(-r.mul(s, dh[k]), r.mul(c, n[k])) for k in range(3)]
    ey = [r.add(r.mul(c, dh[k]), r.mul(s, n[k])) for k in range(3)]
    ez = r.cross3(n, dh)
    axes = [ex, ey, ez]
    if chord_mode == "actual":
        chord = [r.dot3(axes[k], d) for k in range(3)]
    elif chord_mode == "formula_p":
        chord = [r.mul(R, r.sub(cos, 1)), r.mul(R, sin), Fr(0)]
    else:
        raise ValueError(chord_mode)
    h = [[Fr(int(i == j)) for j in range(6)] for i in range(6)]
    h[3][1] = -chord[2]
    h[3][2] = chord[1]
    h[4][0] = chord[2]
    h[4][2] = -chord[0]
    h[5][0] = -chord[1]
    h[5][1] = chord[0]
    coupled = mul6(r, h, tip, False)
    anchored = mul6(r, coupled, h, True)
    k = [[Fr(0)] * 12 for _ in range(12)]
    for i in range(6):
        for j in range(6):
            k[i][j] = anchored[i][j]
            k[i][j + 6] = -coupled[i][j]
            k[i + 6][j] = -coupled[j][i]
            k[i + 6][j + 6] = tip[i][j]
    Kg = rotate(r, k, axes)
    return Kg, dict(d=d, L=L, s=s, c=c, phi=phi, cos=cos, sin=sin, omc=omc, axes=axes, chord=chord, F=F)


def mul6(r, x, y, transpose_right):
    out = [[Fr(0)] * 6 for _ in range(6)]
    for i in range(6):
        for j in range(6):
            acc = Fr(0)
            for k in range(6):
                yv = y[j][k] if transpose_right else y[k][j]
                if x[i][k] == 0 or yv == 0:
                    continue
                acc = r.add(acc, r.mul(x[i][k], yv))
            out[i][j] = acc
    return out


def invert6(r, f):
    m = [row[:] for row in f]
    inv = [[Fr(int(i == j)) for j in range(6)] for i in range(6)]
    for col in range(6):
        piv = col
        for rr in range(col + 1, 6):
            if abs(m[rr][col]) > abs(m[piv][col]):
                piv = rr
        m[col], m[piv] = m[piv], m[col]
        inv[col], inv[piv] = inv[piv], inv[col]
        dd = m[col][col]
        m[col] = [r.div(v, dd) for v in m[col]]
        inv[col] = [r.div(v, dd) for v in inv[col]]
        for rr in range(6):
            if rr == col or m[rr][col] == 0:
                continue
            fac = m[rr][col]
            m[rr] = [r.sub(m[rr][cc], r.mul(fac, m[col][cc])) for cc in range(6)]
            inv[rr] = [r.sub(inv[rr][cc], r.mul(fac, inv[col][cc])) for cc in range(6)]
    out = [row[:] for row in inv]
    for i in range(6):
        for j in range(i + 1, 6):
            v = r.add(inv[i][j], inv[j][i]) / 2
            out[i][j] = v
            out[j][i] = v
    return out


def rotate(r, k, axes):
    out = [[Fr(0)] * 12 for _ in range(12)]
    for bi in range(4):
        for bj in range(4):
            if all(k[3 * bi + p][3 * bj + q] == 0 for p in range(3) for q in range(3)):
                continue
            temp = [[Fr(0)] * 3 for _ in range(3)]
            for p in range(3):
                for cc in range(3):
                    acc = Fr(0)
                    for q in range(3):
                        kv = k[3 * bi + p][3 * bj + q]
                        if kv == 0 or axes[q][cc] == 0:
                            continue
                        acc = r.add(acc, r.mul(kv, axes[q][cc]))
                    temp[p][cc] = acc
            for rr in range(3):
                for cc in range(3):
                    acc = Fr(0)
                    for p in range(3):
                        if axes[p][rr] == 0 or temp[p][cc] == 0:
                            continue
                        acc = r.add(acc, r.mul(axes[p][rr], temp[p][cc]))
                    out[3 * bi + rr][3 * bj + cc] = acc
    return out
