#!/usr/bin/env python3
"""I109's exact-rational oracle for correctly rounded norm2/norm3.

The reference is exact integer arithmetic: every binary64 is n / 2^d, so
S = sum(x_i^2) = N / 4^D with integer N, and RN(sqrt(S)) is decided with
math.isqrt on N (scaled), with ties to even, subnormal results on the
2^-1074 grid and overflow to +inf at 2^1024 - 2^970 (IEEE 754 7.4).

Subcommands
  gen <out.bin> <seed> <random_count>   random + adversarial triples (LE f64 x3)
  check <in.bin> <out.bin> <report.json> verify norm3 (and norm2) bits exactly
  vectors <seed> <count> <out.txt>      committed test vectors (hex) with exact expectations
  selftest                               the reference against Fractions on a sample
"""
import json
import math
import random
import struct
import sys
from fractions import Fraction

MAXF = sys.float_info.max
INF = float("inf")


def as_ratio(x):
    """x = n / 2^d with integer n >= 0, d >= 0 (x finite, sign dropped)."""
    n, den = abs(x).as_integer_ratio()
    return n, den.bit_length() - 1


def cr_sqrt_ratio(N, D):
    """RN(sqrt(N / 4^D)) as a float, N >= 0 integer."""
    if N == 0:
        return 0.0
    es = math.isqrt(N).bit_length() - 1          # floor(log2 sqrt N)
    er = es - D                                 # floor(log2 r)
    q = max(er - 52, -1074)                     # quantum exponent of the destination
    t = D + q                                   # v = r / 2^q = sqrt(N / 4^t)
    j = t - 1                                   # 2v = sqrt(N / 4^j)
    if j <= 0:
        m = N << (-2 * j)
        f = math.isqrt(m)
        exact = f * f == m
    else:
        f = math.isqrt(N >> (2 * j))
        exact = (f * f) << (2 * j) == N
    # f = floor(2v)
    if f % 2 == 0:
        k = f // 2
    else:
        lo = (f - 1) // 2
        if exact:   # tie at lo + 1/2
            k = lo if lo % 2 == 0 else lo + 1
        else:
            k = lo + 1
    try:
        return math.ldexp(k, q)
    except OverflowError:
        return INF


def ref_norm(xs):
    if any(math.isinf(x) for x in xs):
        return INF
    if any(math.isnan(x) for x in xs):
        return float("nan")
    parts = [as_ratio(x) for x in xs]
    D = max(d for _, d in parts)
    N = sum((n * n) << (2 * (D - d)) for n, d in parts)
    return cr_sqrt_ratio(N, D)


def ref_chain(a, b, c):
    return ref_norm([ref_norm([a, b]), c])


def bits(x):
    return struct.unpack("<Q", struct.pack("<d", x))[0]


def from_bits(u):
    return struct.unpack("<d", struct.pack("<Q", u))[0]


def same(x, y):
    if math.isnan(x) and math.isnan(y):
        return True
    return bits(x) == bits(y)


# ---------------------------------------------------------------- generation
def rnd_finite(rng):
    while True:
        u = rng.getrandbits(64)
        if (u >> 52) & 0x7FF != 0x7FF:
            return from_bits(u)


def rnd_exp(rng, e, sign=True):
    """Random double with unbiased exponent e (subnormal patterns if e < -1022)."""
    m = rng.getrandbits(52)
    if e < -1022:
        x = from_bits(m) if m else from_bits(1)
    else:
        e = min(e, 1023)
        x = from_bits(((e + 1023) << 52) | m)
    return -x if sign and rng.getrandbits(1) else x


def rnd_signs(rng, xs):
    return [(-x if rng.getrandbits(1) else x) for x in xs]


def gen_random(rng, count):
    """Random triples across magnitude classes."""
    for i in range(count):
        cls = i % 10
        if cls == 0:            # arbitrary bit patterns (wide exponent spread)
            yield rnd_finite(rng), rnd_finite(rng), rnd_finite(rng)
        elif cls in (1, 2, 3):  # comparable magnitudes (main path), whole range
            e = rng.randint(-1074, 1023)
            yield tuple(rnd_exp(rng, e + rng.randint(-62, 2)) for _ in range(3))
        elif cls == 4:          # near-equal exponents
            e = rng.randint(-1020, 1020)
            yield tuple(rnd_exp(rng, e + rng.randint(-2, 0)) for _ in range(3))
        elif cls == 5:          # third component across the sticky boundary
            e = rng.randint(-900, 900)
            yield rnd_exp(rng, e), rnd_exp(rng, e - rng.randint(0, 60)), rnd_exp(rng, e - rng.randint(55, 200))
        elif cls == 6:          # subnormal and near-minimum results
            e = rng.randint(-1074, -1015)
            yield tuple(rnd_exp(rng, e + rng.randint(-60, 0)) for _ in range(3))
        elif cls == 7:          # overflow range
            e = rng.randint(1015, 1023)
            yield tuple(rnd_exp(rng, e - rng.randint(0, 60)) for _ in range(3))
        elif cls == 8:          # zeros, signed zeros, second-component boundary at 2^-60
            e = rng.randint(-1000, 1000)
            a = rnd_exp(rng, e)
            b = rnd_exp(rng, e - rng.choice([59, 60, 61, 62]))
            c = rng.choice([0.0, -0.0, rnd_exp(rng, e - rng.randint(0, 130))])
            if rng.getrandbits(1):
                b, c = c, b
            yield a, b, c
        else:                   # small integers (exact results) and mixed scales
            if rng.getrandbits(1):
                yield tuple(float(rng.randint(-2**26, 2**26)) for _ in range(3))
            else:
                k = rng.randint(-1100, 970)
                yield tuple(math.ldexp(rng.randint(-2**26, 2**26), k) if k > -1100 else 0.0 for _ in range(3))


def isqrt_round(n):
    r = math.isqrt(n)
    return r + 1 if n - r * r > r else r


def gen_adversarial(rng, count):
    """Exact and near midpoints, sticky ties, binade and range boundaries."""
    out = []
    # 1. exact 2-D midpoints from k(2n+1, 2n(n+1), 2n^2+2n+1), plus perturbations
    while len(out) < count // 4:
        k = rng.choice([1, 3, 5, 7, 9, 11, 13, 15])
        lo_n = math.isqrt((2**53) // (2 * k)) + 1
        hi_n = math.isqrt((2**54) // (2 * k)) - 2
        if lo_n >= hi_n:
            continue
        n = rng.randint(lo_n, hi_n)
        a, b, h = k * (2 * n + 1), k * 2 * n * (n + 1), k * (2 * n * n + 2 * n + 1)
        if not (h >> 53 == 1 and a < 2**53 and b < 2**54 and b % 2 == 0):
            continue
        s = rng.randint(-1074 + 60, 1023 - 56)
        af, bf = math.ldexp(a, s), math.ldexp(b, s)
        third = rng.choice([0.0, 0.0, math.ldexp(1, s - rng.randint(0, 400)), from_bits(1), math.ldexp(a, s - 70)])
        out.append(rnd_signs(rng, [af, bf, third]))
        out.append(rnd_signs(rng, [math.nextafter(af, INF), bf, 0.0]))
        out.append(rnd_signs(rng, [af, math.nextafter(bf, 0.0), 0.0]))
        out.append(rnd_signs(rng, [bf, 0.0, af]))
    # 2. near midpoint just above a: b^2 ~ a*ulp(a) + ulp^2/4 (2-D and 3-D)
    while len(out) < count // 2:
        e = rng.randint(-1000, 1000)
        a = abs(rnd_exp(rng, e))
        u = math.ulp(a)
        target = Fraction(a) * Fraction(u) + Fraction(u) ** 2 / 4
        if rng.getrandbits(1):
            n, d = target.numerator, target.denominator     # dyadic: d = 2^dd
            dd = d.bit_length() - 1
            b = cr_sqrt_ratio(n << (dd % 2), (dd + (dd % 2)) // 2)
            out.append(rnd_signs(rng, [a, b, 0.0]))
        else:
            c = abs(rnd_exp(rng, e - 26 - rng.randint(0, 8)))
            rest = target - Fraction(c) ** 2
            if rest <= 0:
                continue
            n, d = rest.numerator, rest.denominator
            dd = d.bit_length() - 1
            b = cr_sqrt_ratio(n << (dd % 2), (dd + (dd % 2)) // 2)
            out.append(rnd_signs(rng, [c, a, b]))
    # 3. near a random midpoint M: a random, b = RN(sqrt(M^2 - a^2))
    while len(out) < 3 * count // 4:
        e = rng.randint(-1000, 1000)
        mid = (2 * rng.getrandbits(52) + 1) | (1 << 53)       # 54-bit odd significand
        M = Fraction(mid) * Fraction(2) ** (e - 53)
        a = abs(rnd_exp(rng, e - rng.randint(0, 40)))
        rest = M * M - Fraction(a) ** 2
        if rest <= 0:
            continue
        n, d = rest.numerator, rest.denominator
        if d & (d - 1):
            continue
        dd = d.bit_length() - 1
        b = cr_sqrt_ratio(n << (dd % 2), (dd + (dd % 2)) // 2)
        if math.isinf(b):
            continue
        third = rng.choice([0.0, 0.0, math.ldexp(1.0, e - rng.randint(60, 300))])
        out.append(rnd_signs(rng, [a, b, third]))
    # 4. binade, subnormal, overflow boundaries
    while len(out) < count:
        kind = rng.randint(0, 3)
        if kind == 0:   # results just below/above a power of two
            e = rng.randint(-1020, 1022)
            p = math.ldexp(1.0, e)
            a = math.nextafter(p, 0.0) if rng.getrandbits(1) else p
            b = math.ldexp(rng.random(), e - rng.randint(20, 60))
            out.append(rnd_signs(rng, [a, b, rng.choice([0.0, math.ldexp(rng.random(), e - rng.randint(20, 60))])]))
        elif kind == 1:  # subnormal grid near midpoints: integer units of 2^-1074
            k = rng.randint(1, 2**52)
            a = rng.randint(0, k)
            target = 4 * k * k + 4 * k + 1     # (2k+1)^2 / 4 in quarter units
            rest = target - 4 * a * a
            b = isqrt_round(rest // 4) if rest > 0 else 0
            out.append(rnd_signs(rng, [math.ldexp(a, -1074), math.ldexp(b, -1074), rng.choice([0.0, 5e-324])]))
        elif kind == 2:  # overflow threshold 2^1024 - 2^970 and MAX
            top = Fraction(2) ** 1024 - Fraction(2) ** 970
            a = MAXF if rng.getrandbits(1) else math.nextafter(MAXF, 0.0)
            if rng.getrandbits(1):
                a = abs(rnd_exp(rng, 1023))
            rest = top * top - Fraction(a) ** 2
            if rest > 0:
                n, d = rest.numerator, rest.denominator
                b = cr_sqrt_ratio(n, 0) if d == 1 else 0.0
                b = math.nextafter(b, INF) if rng.getrandbits(1) else b
                if math.isinf(b):
                    b = MAXF
            else:
                b = 0.0
            out.append(rnd_signs(rng, [a, b, rng.choice([0.0, 1.0, math.ldexp(1.0, 900)])]))
        else:            # special values
            pool = [0.0, -0.0, INF, -INF, float("nan"), 1.0, 5e-324, MAXF, 2.2250738585072014e-308]
            out.append([rng.choice(pool), rng.choice(pool), rng.choice(pool)])
    return out


def write_triples(path, triples):
    n = 0
    with open(path, "wb") as f:
        for t in triples:
            f.write(struct.pack("<3d", *t))
            n += 1
    return n


def cmd_gen(out, seed, random_count):
    rng = random.Random(seed)
    adv = gen_adversarial(rng, max(1_000_000, random_count // 10))

    def all_triples():
        yield from gen_random(rng, random_count)
        yield from adv
    n = write_triples(out, all_triples())
    print(json.dumps({"written": n, "random": random_count, "adversarial": len(adv)}))


def cmd_check(inp, outp, report):
    total = bad3 = bad2 = 0
    first = []
    classes = {"norm3_main_path": 0, "norm3_largest_only": 0, "special": 0}
    with open(inp, "rb") as fi, open(outp, "rb") as fo:
        while True:
            rec = fi.read(24 * 4096)
            if not rec:
                break
            out = fo.read(16 * (len(rec) // 24))
            for i, (a, b, c) in enumerate(struct.iter_unpack("<3d", rec)):
                n3, n2 = struct.unpack_from("<2Q", out, 16 * i)
                e3, e2 = ref_norm([a, b, c]), ref_norm([a, b])
                total += 1
                if not same(from_bits(n3), e3):
                    bad3 += 1
                    if len(first) < 20:
                        first.append({"f": "norm3", "in": [a.hex(), b.hex(), c.hex()], "got": from_bits(n3).hex(), "want": e3.hex()})
                if not same(from_bits(n2), e2):
                    bad2 += 1
                    if len(first) < 20:
                        first.append({"f": "norm2", "in": [a.hex(), b.hex()], "got": from_bits(n2).hex(), "want": e2.hex()})
                if any(math.isinf(x) or math.isnan(x) for x in (a, b, c)):
                    classes["special"] += 1
                else:
                    xs = sorted((abs(a), abs(b), abs(c)), reverse=True)
                    ex = math.frexp(xs[0])[1] if xs[0] else 0
                    if xs[0] == 0 or math.ldexp(xs[1], 61 - ex) < 1.0:
                        classes["norm3_largest_only"] += 1
                    else:
                        classes["norm3_main_path"] += 1
        assert fo.read(1) == b"", "output longer than input"
    result = {"triples": total, "norm3_misrounded": bad3, "norm2_misrounded": bad2, "first_failures": first, "classes": classes}
    with open(report, "w") as f:
        json.dump(result, f, indent=1)
    print(json.dumps({k: v for k, v in result.items() if k != "first_failures"}))
    return bad3 + bad2


def cmd_vectors(seed, count, out):
    rng = random.Random(seed)
    adv = gen_adversarial(rng, count)
    rand = list(gen_random(rng, count // 2))
    rows = adv[: count // 2 + count // 4] + rand[: count // 4]
    with open(out, "w") as f:
        f.write("# I109 correct_norm vectors: a b c norm3(a,b,c) norm2(a,b), binary64 bits in hex.\n")
        f.write(f"# Expected bits from exact integer square roots (norm_oracle.py vectors {seed} {count}).\n")
        for a, b, c in rows:
            f.write("%016x %016x %016x %016x %016x\n" % (bits(a), bits(b), bits(c), bits(ref_norm([a, b, c])), bits(ref_norm([a, b]))))
    print(json.dumps({"vectors": len(rows)}))


def cmd_selftest():
    rng = random.Random(109)
    checked = 0
    for t in list(gen_random(rng, 20000)) + gen_adversarial(rng, 4000):
        if any(math.isinf(x) or math.isnan(x) for x in t):
            continue
        got = ref_norm(list(t))
        S = sum(Fraction(x) ** 2 for x in t)
        # independent check: got is the nearest double, ties to even, via Fractions
        if math.isinf(got):
            assert S >= (Fraction(2) ** 1024 - Fraction(2) ** 970) ** 2, t
        else:
            g = Fraction(got)
            up = Fraction(math.nextafter(got, INF)) if got < MAXF else Fraction(2) ** 1024
            dn = Fraction(math.nextafter(got, 0.0)) if got > 0 else Fraction(0)
            hi, lo = ((g + up) / 2) ** 2, ((g + dn) / 2) ** 2
            even = bits(got) % 2 == 0
            assert (S < hi or (S == hi and even)) and (S > lo or (S == lo and even) or got == 0), (t, got)
        checked += 1
    print(json.dumps({"selftest_checked": checked}))


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "gen":
        cmd_gen(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    elif cmd == "check":
        sys.exit(1 if cmd_check(sys.argv[2], sys.argv[3], sys.argv[4]) else 0)
    elif cmd == "vectors":
        cmd_vectors(int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
    elif cmd == "selftest":
        cmd_selftest()
