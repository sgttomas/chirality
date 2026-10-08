"""RV126: an independent input generator for the correctly rounded norm (PR-N review).

Writes little-endian binary64 triples (a, b, c) to OUT and one category byte per triple to OUT.cat.
Written by RV126 without reference to I109's generator. Seed 126 unless given.

Categories (id: name):
  0 special      every ordered triple of 22 special values (zeros, infinities, NaN, subnormal,
                 MIN_POSITIVE, MAX, the 2^-60 and 2^-120 scaled thresholds, ...)
  1 rbits        uniformly random 64-bit patterns
  2 compar       comparable magnitudes over the whole exponent range
  3 thresh       dynamic ranges around the 2^-60 (largest-only) and 2^-120 (sticky) thresholds
  4 tie2d        exact 2-D midpoints from Euclid's formula, h odd in [2^53, 2^54), scaled; with a
                 sticky, kept or absent third component and 0-3 ulp perturbations
  5 tie3d        exact 3-D midpoints from the quaternion form of Pythagorean quadruples
  6 near2d       2-D near-midpoints with a small second component, b^2 ~ 2a(k+1/2)ulp(a)
  7 near3d       3-D near-midpoints: a, b arbitrary, c solved exactly toward a midpoint (incl. the
                 midpoints beside powers of two)
  8 subnorm      subnormal results, near-ties on the subnormal grid, and the MIN_POSITIVE boundary
  9 overflow     the overflow threshold 2^1024 - 2^970 and near-MAX comparable triples
 10 smallint     small integers, scaled by random powers of two
"""
import math
import random
import struct
import sys

MANT = (1 << 52) - 1
MAXF = struct.unpack('<d', struct.pack('<Q', 0x7FEFFFFFFFFFFFFF))[0]


def f(bits):
    return struct.unpack('<d', struct.pack('<Q', bits & 0xFFFFFFFFFFFFFFFF))[0]


def b(x):
    return struct.unpack('<Q', struct.pack('<d', x))[0]


def nxt(x, k=1):
    """Move x by k ulps toward +inf (k may be negative) on the positive axis; x >= 0."""
    bits = b(x) + k
    if bits < 0:
        return 0.0
    return f(bits)


def exact(m, e):
    """m * 2^e as a double, or None when not exactly representable / out of range."""
    try:
        x = math.ldexp(float(m), e)
    except OverflowError:
        return None
    if m != 0 and (x == 0.0 or math.isinf(x)):
        return None
    if float(m) != m:
        return None
    # round trip check
    n, d = x.as_integer_ratio()
    if e >= 0:
        return x if n == m << e and d == 1 else None
    return x if n * (1 << -e) == m * d else None


def rsign(rng, x):
    return -x if rng.random() < 0.5 else x


def rperm(rng, t):
    t = list(t)
    rng.shuffle(t)
    return t


def rdouble_exp(rng, e):
    """A random double with exponent e (normal if e >= -1022, else a random subnormal)."""
    if e >= -1022:
        return math.ldexp(1.0 + rng.getrandbits(52) / 2.0 ** 52, e)
    return f(rng.getrandbits(52) | 1)


def isqrt_rn_double(num, den_exp):
    """RN(sqrt(num * 2^-(2*den_exp))) as a double (num >= 0 int): used only to build inputs."""
    if num == 0:
        return 0.0
    # sqrt(num) * 2^-den_exp; compute with 80 extra bits then round via float of a big int
    sh = 160
    r = math.isqrt(num << sh)  # sqrt(num) * 2^80
    return math.ldexp(float(r), -den_exp - 80) if r.bit_length() < 1000 else math.ldexp(float(r >> (r.bit_length() - 64)), r.bit_length() - 64 - den_exp - 80)


def to_int_exp(x):
    """|x| = M * 2^E for finite nonzero x."""
    bits = b(abs(x))
    ef = bits >> 52
    fr = bits & MANT
    if ef == 0:
        return fr, -1074
    return fr | (1 << 52), ef - 1075


def gen(n_scale, seed, out):
    rng = random.Random(seed)
    triples = []
    cats = []

    def add(cat, t):
        triples.append(tuple(float(v) for v in t))
        cats.append(cat)

    # 0 specials
    sp = [0.0, -0.0, math.inf, -math.inf, math.nan, f(1), -f(1), f(2), f(0x000FFFFFFFFFFFFF),
          2.2250738585072014e-308, -2.2250738585072014e-308, MAXF, -MAXF, 1.0, -1.0, 3.0,
          2.0 ** -60, nxt(2.0 ** -60, -1), 2.0 ** -120, nxt(2.0 ** -120, -1), 2.0 ** 1023, 1.5]
    for x in sp:
        for y in sp:
            for z in sp:
                add(0, (x, y, z))

    # 1 random bit patterns
    for _ in range(150 * n_scale):
        add(1, (f(rng.getrandbits(64)), f(rng.getrandbits(64)), f(rng.getrandbits(64))))

    # 2 comparable magnitudes
    for _ in range(250 * n_scale):
        e = rng.randint(-1076, 1023)
        t = [rsign(rng, rdouble_exp(rng, max(-1080, e - rng.randint(0, 4)))) for _ in range(3)]
        add(2, rperm(rng, t))

    # 3 thresholds: second component around 2^-60 relative, third around 2^-120 relative
    for _ in range(150 * n_scale):
        e = rng.randint(-1022 + 130, 1023) if rng.random() < 0.9 else rng.randint(-1074, 1023)
        a = rdouble_exp(rng, e)
        if rng.random() < 0.5:
            d1 = rng.choice([58, 59, 60, 61, 62])
        else:
            d1 = rng.randint(0, 70)
        mode = rng.random()
        if mode < 0.15:
            bb = 2.0 ** (e - 60) if e - 60 >= -1074 else 0.0
            bb = nxt(bb, rng.choice([-2, -1, 0, 1, 2]))
        else:
            bb = rdouble_exp(rng, e - d1) if e - d1 >= -1080 else 0.0
        d2 = rng.choice([118, 119, 120, 121, 122]) if rng.random() < 0.6 else rng.randint(d1, 200)
        if rng.random() < 0.2:
            cc = 2.0 ** (e - 120) if e - 120 >= -1074 else f(1)
            cc = nxt(cc, rng.choice([-1, 0, 1]))
        else:
            cc = rdouble_exp(rng, e - d2) if e - d2 >= -1074 else f(rng.getrandbits(10) | 1)
        add(3, rperm(rng, [rsign(rng, a), rsign(rng, bb), rsign(rng, cc)]))

    # 4 exact 2-D midpoints (Euclid): a = m^2 - n^2 (odd, < 2^53), b = 2mn, h = m^2 + n^2 odd in [2^53, 2^54)
    lo, hi = 1 << 53, 1 << 54
    made = 0
    while made < 200 * n_scale:
        m = rng.randint(1 << 26, (1 << 27) - 1)
        n = rng.randint(1, m - 1)
        if (m - n) % 2 == 0:
            continue
        a, bb, h = m * m - n * n, 2 * m * n, m * m + n * n
        if not (lo <= h < hi and a < lo and bb < hi):
            continue
        assert a * a + bb * bb == h * h and h & 1
        s = rng.randint(-1021, 970)  # all components stay exact normal doubles
        A, B = exact(a, s), exact(bb, s)
        if A is None or B is None:
            continue
        E = h.bit_length() - 1 + s  # exponent of the result
        variant = rng.random()
        if variant < 0.25:
            C = 0.0
        elif variant < 0.55:  # sticky third component (below 2^-120 relative to the largest)
            j = rng.choice([121, 122, 125, 150, 200, 400, 1000]) if rng.random() < 0.6 else rng.randint(121, 1100)
            C = rdouble_exp(rng, E - j) if E - j >= -1074 else f(rng.getrandbits(8) | 1)
            if rng.random() < 0.2 and E - 121 >= -1022:
                C = nxt(2.0 ** (E - 120), -rng.randint(1, 3))
        elif variant < 0.7:  # kept third component, near the sticky threshold
            j = rng.choice([118, 119, 120]) if rng.random() < 0.5 else rng.randint(60, 120)
            C = rdouble_exp(rng, E - j) if E - j >= -1022 else 0.0
            if rng.random() < 0.2 and E - 120 >= -1022:
                C = 2.0 ** (E - 120)
        else:  # perturb a or b by 1-3 ulps, sometimes with a sticky third component
            k = rng.choice([-3, -2, -1, 1, 2, 3])
            if rng.random() < 0.5:
                A = nxt(A, k)
            else:
                B = nxt(B, k)
            C = 0.0 if rng.random() < 0.5 else rdouble_exp(rng, E - rng.randint(121, 300)) if E - 300 >= -1074 else 0.0
        add(4, rperm(rng, [rsign(rng, A), rsign(rng, B), rsign(rng, C)]))
        made += 1

    # 5 exact 3-D midpoints (Pythagorean quadruples): a = m^2+n^2-p^2-q^2, b = 2(mq+np), c = 2(nq-mp), d = m^2+n^2+p^2+q^2
    made = 0
    while made < 100 * n_scale:
        m, n, p, q = (rng.randint(0, (1 << 26) + (1 << 25)) for _ in range(4))
        d = m * m + n * n + p * p + q * q
        if not (lo <= d < hi and d & 1):
            continue
        a = m * m + n * n - p * p - q * q
        bb = 2 * (m * q + n * p)
        cc = 2 * (n * q - m * p)
        assert a * a + bb * bb + cc * cc == d * d
        if abs(a) >= lo or abs(bb) >= hi or abs(cc) >= hi:
            continue
        s = rng.randint(-1021, 969)
        t = [exact(abs(a), s), exact(abs(bb), s), exact(abs(cc), s)]
        if any(v is None for v in t):
            continue
        if rng.random() < 0.3:  # perturb one component by an ulp
            i = rng.randint(0, 2)
            t[i] = nxt(t[i], rng.choice([-1, 1])) if t[i] > 0 else t[i]
        add(5, rperm(rng, [rsign(rng, v) for v in t]))
        made += 1

    # 6 2-D near-midpoints with a small second component: a in [1,2)*2^E, b^2 ~ (2a + (k+1/2)u)(k+1/2)u
    made = 0
    while made < 100 * n_scale:
        E = rng.randint(-960, 1000)
        Am = (1 << 52) | rng.getrandbits(52)  # a = Am * 2^(E-52)
        k = rng.choice([0, 0, 1, 2, 3, rng.randint(0, 1000), rng.randint(0, 1 << 20)])
        # in units u = 2^(E-52): a = Am u, target T = (Am + k + 1/2) u, b^2 = T^2 - a^2 = (2Am + k + 1/2)(k + 1/2) u^2
        num = (4 * Am + 2 * k + 1) * (2 * k + 1)  # = 4 * b^2 / u^2
        # b = sqrt(num)/2 * u ; RN to a double via integer sqrt with guard bits
        r = math.isqrt(num << 200)  # sqrt(num) * 2^100
        Bv = math.ldexp(float(r >> (r.bit_length() - 60)), r.bit_length() - 60 - 100 - 1 + E - 52)
        if Bv == 0.0 or math.isinf(Bv):
            continue
        A = math.ldexp(float(Am), E - 52)
        if A + 0.0 >= 2.0 ** 1023 * 1.999:
            continue
        for dk in ([0] if rng.random() < 0.7 else [rng.choice([-1, 1])]):
            Bk = nxt(Bv, dk)
            third = 0.0
            if rng.random() < 0.3:
                third = rdouble_exp(rng, E - rng.randint(121, 400)) if E - 400 >= -1074 else 0.0
            add(6, rperm(rng, [rsign(rng, A), rsign(rng, Bk), rsign(rng, third)]))
            made += 1

    # 7 3-D near-midpoints: a, b arbitrary; c solved exactly toward a midpoint m of the result grid
    made = 0
    while made < 200 * n_scale:
        E = rng.randint(-1000, 1000)
        A = rdouble_exp(rng, E)
        B = rdouble_exp(rng, E - rng.choice([0, 0, 0, 1, 2, 5, 20, 40, 59, 60, 61]))
        (Ma, Ea), (Mb, Eb) = to_int_exp(A), to_int_exp(B)
        E0 = min(Ea, Eb)
        S2 = (Ma << (Ea - E0)) ** 2 + (Mb << (Eb - E0)) ** 2  # a^2+b^2 = S2 * 4^E0
        # result grid: choose a midpoint mid >= sqrt(S2) * 2^E0, some half-ulps above
        root = math.isqrt(S2)  # ~ sqrt(S2)
        L = root.bit_length() - 1  # exponent of sqrt(S2) in units 2^E0
        pick = rng.random()
        if pick < 0.2:
            # midpoint just below the next power of two: 2^(L+1) - 2^(L+1-54)  (in units 2^E0)
            q = L + 1 - 54
            mid_num, mid_exp = (1 << 54) - 1, q  # mid = mid_num * 2^(mid_exp) units
        else:
            q = L - 52  # ulp of result, units 2^E0
            base = (root >> q) if q >= 0 else (root << -q)
            j = rng.choice([0, 1, 1, 2, 3, rng.randint(0, 50), rng.randint(0, 1 << 24)])
            mid_num, mid_exp = 2 * (base + j) + 1, q - 1
        # c^2 = mid^2 - S2 (units 4^E0); mid^2 = mid_num^2 * 4^mid_exp
        if mid_exp >= 0:
            C2 = (mid_num << mid_exp) ** 2 - S2
            sh = 0
        else:
            C2 = mid_num * mid_num - (S2 << (-2 * mid_exp))
            sh = -mid_exp  # C2 in units 4^(E0 - sh)
        if C2 <= 0:
            continue
        r = math.isqrt(C2 << 240)  # sqrt(C2) * 2^120
        c_exp = E0 - sh - 120
        top = r.bit_length() - 60
        try:
            Cv = math.ldexp(float(r >> top), top + c_exp) if top > 0 else math.ldexp(float(r), c_exp)
        except OverflowError:
            continue
        if Cv == 0.0 or math.isinf(Cv) or math.isinf(A) or math.isinf(B):
            continue
        Cv = nxt(Cv, rng.choice([0, 0, 0, 0, -1, 1]))
        add(7, rperm(rng, [rsign(rng, A), rsign(rng, B), rsign(rng, Cv)]))
        made += 1

    # 8 subnormal results and the MIN_POSITIVE boundary
    made = 0
    while made < 100 * n_scale:
        pick = rng.random()
        if pick < 0.35:  # random subnormal / tiny components
            t = [f(rng.getrandbits(rng.randint(1, 52))) for _ in range(3)]
        elif pick < 0.75:  # near-ties on the subnormal grid: A^2+B^2+C^2 ~ (K + 1/2)^2 (units 2^-1074)
            Am = rng.getrandbits(rng.randint(2, 51)) | 1
            Bm = rng.getrandbits(rng.randint(1, max(1, Am.bit_length()))) if rng.random() < 0.8 else 0
            S2 = Am * Am + Bm * Bm
            K = math.isqrt(S2) + rng.choice([0, 0, 1, 2, rng.randint(0, 100)])
            C2 = (2 * K + 1) ** 2 - 4 * S2  # = 4*c^2
            if C2 <= 0:
                continue
            Cm = (math.isqrt(C2) + 1) // 2 + rng.choice([-1, 0, 0, 1])
            if Cm < 0 or Cm >= (1 << 52):
                continue
            t = [f(Am), f(Bm), f(Cm)]
            if any(x >= 2.2250738585072014e-308 for x in t):
                continue
        else:  # straddle MIN_POSITIVE: components ~ 2^-1023
            t = [f(rng.getrandbits(52) | (1 << 51)) if rng.random() < 0.7 else rdouble_exp(rng, -1022 - rng.randint(0, 3)) for _ in range(3)]
            if rng.random() < 0.5:
                t[2] = 0.0
        add(8, rperm(rng, [rsign(rng, x) for x in t]))
        made += 1

    # 9 overflow threshold and near-MAX
    TH = (1 << 1024) - (1 << 970)
    made = 0
    while made < 50 * n_scale:
        pick = rng.random()
        if pick < 0.5:
            A = nxt(MAXF, -rng.choice([0, 0, 1, 2, rng.randint(0, 1 << 30), rng.randint(0, 1 << 50)]))
            Ma, Ea = to_int_exp(A)
            a_int = Ma << Ea  # A exactly (Ea >= 0 here)
            # b^2 = TH^2 - A^2 (exact ints); b = RN(sqrt)
            B2 = TH * TH - a_int * a_int
            if B2 <= 0:
                continue
            r = math.isqrt(B2)
            top = max(0, r.bit_length() - 60)
            Bv = math.ldexp(float(r >> top), top)
            Bv = nxt(Bv, rng.choice([0, 0, -1, 1, -2, 2]))
            third = 0.0 if rng.random() < 0.5 else rdouble_exp(rng, rng.randint(800, 1000))
            add(9, rperm(rng, [rsign(rng, A), rsign(rng, Bv), rsign(rng, third)]))
        else:
            e = rng.choice([1023, 1023, 1022, 1021])
            t = [rsign(rng, rdouble_exp(rng, e - rng.randint(0, 2))) for _ in range(3)]
            if rng.random() < 0.3:
                t[2] = 0.0
            add(9, rperm(rng, t))
        made += 1

    # 10 small integers, scaled
    for _ in range(50 * n_scale):
        s = rng.choice([0, 0, rng.randint(-1060, 1000)])
        t = []
        for _ in range(3):
            v = rng.randint(-100, 100)
            x = exact(abs(v), s) if v else 0.0
            t.append(rsign(rng, x if x is not None else 0.0))
        add(10, t)

    with open(out, 'wb') as fo:
        for t in triples:
            fo.write(struct.pack('<ddd', *t))
    with open(out + '.cat', 'wb') as fo:
        fo.write(bytes(cats))
    counts = {}
    for c in cats:
        counts[c] = counts.get(c, 0) + 1
    print('triples', len(triples), 'by category', dict(sorted(counts.items())))


if __name__ == '__main__':
    gen(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
