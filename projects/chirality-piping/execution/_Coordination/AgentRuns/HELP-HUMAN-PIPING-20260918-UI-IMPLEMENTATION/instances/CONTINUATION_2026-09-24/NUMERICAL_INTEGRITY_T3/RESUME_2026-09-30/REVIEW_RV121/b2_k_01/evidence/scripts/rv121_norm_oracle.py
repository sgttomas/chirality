"""RV121's own exact RN64 3-norm oracle and adversarial triples (standard library only).
Method (independent of the kernel, I97's rn64_norm3 and the B2-K generator's isqrt):
bisection over positive binary64 bit patterns for the largest b with v(b)^2 <= S, then one
exact comparison of S with the square of the midpoint of v(b) and v(b+1) (ties to even).
Writes the triples as JSON (argv[1]); if argv[2] is given, it is the kernel's printed
RV121_NORM lines, which are compared bit for bit."""
import sys, json, struct, random, math
from fractions import Fraction as F
INF_BITS = 0x7ff0000000000000
def val(b):
    if b == INF_BITS: return F(2) ** 1024
    return F(struct.unpack('>d', struct.pack('>Q', b))[0])
def fbits(x): return struct.unpack('>Q', struct.pack('>d', x))[0]
def oracle(bx, by, bz):
    S = sum(val(b & 0x7fffffffffffffff) ** 2 for b in (bx, by, bz))
    if S == 0: return 0
    lo, hi = 0, INF_BITS          # v(lo)^2 <= S always; find max b with v(b)^2 <= S
    if val(hi) ** 2 <= S: return None
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if val(mid) ** 2 <= S: lo = mid
        else: hi = mid
    b = lo
    m = (val(b) + val(b + 1)) / 2
    d = S - m * m
    r = b if d < 0 else (b + 1 if d > 0 else (b if b % 2 == 0 else b + 1))
    return None if r >= INF_BITS else r
# ---- exact ties by Cornacchia: x^2 + y^2 + z^2 = (d * 2^s)^2 with d odd (54 bits)
def is_probable_prime(n):
    if n < 2: return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0: return n == p
    d, s = n - 1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41):
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True
def two_squares_prime(p):
    """p prime, p % 4 == 1: (a, b) with a^2 + b^2 = p (Hermite-Serret / Cornacchia)."""
    rng = random.Random(p)
    while True:
        c = rng.randrange(2, p - 1)
        if pow(c, (p - 1) // 2, p) == p - 1: break
    t = pow(c, (p - 1) // 4, p)
    a, b = p, t
    lim = math.isqrt(p)
    while b > lim: a, b = b, a % b
    rest = p - b * b
    c2 = math.isqrt(rest)
    assert c2 * c2 == rest
    return b, c2
def tie_triple(d, s, rng):
    """d odd: d^2 = X^2 + (2u)^2 + (2v)^2 with X = q2 - q1 odd (< 2^53), q1 = 2 r1, q2 = d - q1,
    r1 and q2 primes = 1 mod 4, so u^2 + v^2 = q1 q2 (Brahmagupta-Fibonacci, then 2 = 1 + 1).
    Components X 2^s, 2u 2^s, 2v 2^s must be binary64."""
    for _ in range(400000):
        r1 = rng.randrange(max(3, (d - 2 ** 53) // 4 + 1), (d + 2 ** 53) // 4) | 1
        if r1 % 4 != 1 or not is_probable_prime(r1): continue
        q1 = 2 * r1; q2 = d - q1
        if q2 <= 0 or q2 % 4 != 1 or not is_probable_prime(q2): continue
        X = abs(q2 - q1)
        if X >= 2 ** 53: continue
        s1, t1 = two_squares_prime(r1); s2, t2 = two_squares_prime(q2)
        A, B = s1 * s2 - t1 * t2, s1 * t2 + t1 * s2
        u, v = abs(A + B), abs(A - B)
        assert u * u + v * v == q1 * q2 and X * X + 4 * (u * u + v * v) == d * d
        if u >= 2 ** 53 or v >= 2 ** 53: continue
        xs = [F(X) * F(2) ** s, F(2 * u) * F(2) ** s, F(2 * v) * F(2) ** s]
        bits_ = []
        for x in xs:
            f = float(x)
            if F(f) != x: break
            bits_.append(fbits(f))
        else:
            assert sum(val(b) ** 2 for b in bits_) == (F(d) * F(2) ** s) ** 2
            return tuple(bits_)
    return None
def triples():
    rng = random.Random(121)
    out = []
    MAXB = 0x7fefffffffffffff
    # SA4-1 (the brief's three added vectors), each expected at MIN_POSITIVE.
    out += [('rv115_counterexample', (0x000fffffffffffff, 0x0000000004000001, 0)),
            ('rv118_witness', (0x000fffffffffffff, fbits(2.0 ** -1048), 0)),
            ('near_threshold', (0x000fffffffffffff, 0x0000000003ffffff, 0x0000000000002d42))]
    # Exact ties at binade edges: d = 2^54 - 1 (rounds up across the binade), d = 2^53 + 1
    # (between the binade's first value and its successor), and interior d, at several scales,
    # with one-ulp perturbations of the last component either way.
    for d in (2 ** 54 - 1, 2 ** 54 - 3, 2 ** 53 + 1, 2 ** 53 + 3, 3 * 2 ** 52 + 1, 3 * 2 ** 52 - 1):
        for s in (-1100, -1075, -1060, -600, -54, 0, 400, 900, 916):
            t = tie_triple(d, s, rng)
            if t is None: continue
            out.append((f'tie d={d:#x} s={s}', t))
            out.append((f'tie+ d={d:#x} s={s}', (t[0], t[1], t[2] + 1)))
            if t[2] & 0x7fffffffffffffff: out.append((f'tie- d={d:#x} s={s}', (t[0], t[1], t[2] - 1)))
    # The overflow edge: S = (MAX + 2^970)^2 exactly (a tie that rounds to 2^1024: refused),
    # and the same with the last component one ulp lower (MAX).
    # x = 2^970 (2^54 - 2 - 2k): S - x^2 = 2^1940 (1 + 2k)(2^55 - 3 - 2k) = y^2 + z^2.
    def rep2(n):
        """n = y^2 + z^2 for n = q * p (q in {1} or a prime = 1 mod 4, p prime = 1 mod 4)."""
        return None
    for k in range(0, 4000):
        f1, f2 = 1 + 2 * k, 2 ** 55 - 3 - 2 * k
        ok1 = f1 == 1 or (f1 % 4 == 1 and is_probable_prime(f1))
        ok2 = f2 % 4 == 1 and is_probable_prime(f2)
        if not (ok1 and ok2): continue
        a1, b1 = (1, 0) if f1 == 1 else two_squares_prime(f1)
        a2, b2 = two_squares_prime(f2)
        y, z = a1 * a2 + b1 * b2, abs(a1 * b2 - b1 * a2)
        assert y * y + z * z == f1 * f2
        x = F(2) ** 970 * (2 ** 54 - 2 - 2 * k)
        t = (fbits(float(x)), fbits(float(F(y) * F(2) ** 970)), fbits(float(F(z) * F(2) ** 970)))
        if any(F(float(F(v) * F(2) ** 970)) != F(v) * F(2) ** 970 for v in (y, z)): continue
        assert sum(val(b) ** 2 for b in t) == (val(MAXB) + F(2) ** 970) ** 2
        out.append((f'overflow_tie k={k}', t))
        out.append((f'overflow_tie- k={k}', (t[0], t[1], t[2] - 1)))
        out.append((f'overflow_tie+ k={k}', (t[0], t[1], t[2] + 1)))
        if sum(1 for l, _ in out if l.startswith('overflow_tie k')) >= 3: break
    # Subnormal and MIN_POSITIVE neighbourhoods, signed components, and random patterns.
    for b in (1, 2, 3, 0x000fffffffffffff, 0x0010000000000000, 0x0010000000000001, 0x001fffffffffffff):
        out.append((f'single {b:#x}', (b | 0x8000000000000000, 0, 0)))
        out.append((f'pair {b:#x}', (b, b, 0)))
        out.append((f'triple {b:#x}', (b, b, b)))
    for _ in range(400):
        e = rng.choice([rng.randrange(1, 60), rng.randrange(900, 1100), rng.randrange(1900, 2046)])
        out.append(('random', tuple((rng.getrandbits(52) | (e << 52) | (rng.getrandbits(1) << 63)) & 0xffffffffffffffff
                                    if rng.random() < 0.9 else rng.getrandbits(52) for _ in range(3))))
    for _ in range(200):
        out.append(('spread', (rng.getrandbits(63) % INF_BITS, rng.getrandbits(63) % INF_BITS, rng.randrange(0, 2 ** 52))))
    out = [(l, t) for l, t in out if all((b & 0x7fffffffffffffff) < INF_BITS for b in t)]
    return out
if __name__ == '__main__':
    T = triples()
    rows = []
    for label, t in T:
        r = oracle(*t)
        rows.append({'label': label, 'x': f'{t[0]:016x}', 'y': f'{t[1]:016x}', 'z': f'{t[2]:016x}',
                     'p': 'refused' if r is None else f'{r:016x}'})
    json.dump({'method': 'bit-pattern bisection plus one exact midpoint comparison', 'vectors': rows},
              open(sys.argv[1], 'w'), indent=1)
    ties = sum(1 for r in rows if r['label'].startswith('tie '))
    print(json.dumps({'vectors': len(rows), 'ties': ties,
                      'sa4_1': [r['p'] for r in rows[:3]],
                      'overflow': [r['p'] for r in rows if r['label'].startswith('overflow')]}))
    if len(sys.argv) > 2:
        got = {}
        for line in open(sys.argv[2]):
            if 'RV121_NORM ' in line:
                x, y, z, p = line.split('RV121_NORM ', 1)[1].split()
                got[(x, y, z)] = p
        bad = [r for r in rows if got.get((r['x'], r['y'], r['z'])) != r['p']]
        print(json.dumps({'compared': len(got), 'disagree': len(bad), 'first': bad[:5]}))
        sys.exit(1 if bad or len(got) < len(rows) else 0)
