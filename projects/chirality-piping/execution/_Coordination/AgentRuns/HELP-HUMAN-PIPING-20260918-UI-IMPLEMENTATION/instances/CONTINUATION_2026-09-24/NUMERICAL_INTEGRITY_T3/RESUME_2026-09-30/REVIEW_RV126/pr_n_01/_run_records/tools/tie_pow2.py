"""RV126: exact ties at the lower midpoint of a power of two, h = 2^54 - 1 (between 2^54 - 2 and 2^54),
scaled by 2^s for s across the range, including s = 970 where h * 2^970 is exactly the overflow
threshold 2^1024 - 2^970 (an exact tie that must round to +inf).

3-D: d = 2^54 - 1 = m^2+n^2+p^2+q^2 (d = 7 mod 8, so four squares are needed), via a prime
R = d - m^2 - n^2 = 1 mod 4 split as p^2 + q^2 (Cornacchia); then (a, b, c) from the quaternion form.
2-D: h = k * h1 with h1 = 262657 (prime, 1 mod 4) = m^2 + n^2; legs k(m^2 - n^2), 2kmn.
Also +-1 ulp perturbations and sticky third components.
Usage: tie_pow2.py OUT COUNT SEED
"""
import math
import random
import struct
import sys

D = (1 << 54) - 1


def is_probable_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def two_squares_prime(p, rng):
    """p prime = 1 mod 4 -> (x, y) with x^2 + y^2 = p (Hermite-Serret / Cornacchia)."""
    while True:
        a = rng.randrange(2, p - 1)
        t = pow(a, (p - 1) // 4, p)
        if t * t % p == p - 1:
            break
    r0, r1 = p, t
    lim = math.isqrt(p)
    while r1 > lim:
        r0, r1 = r1, r0 % r1
    x = r1
    y = math.isqrt(p - x * x)
    assert x * x + y * y == p
    return x, y


def exact(m, s):
    x = math.ldexp(float(m), s)
    n, d = x.as_integer_ratio()
    ok = (n == m << s and d == 1) if s >= 0 else (n * (1 << -s) == m * d)
    return x if ok and float(m) == m else None


def nxt(x, k):
    b = struct.unpack('<Q', struct.pack('<d', x))[0] + k
    return struct.unpack('<d', struct.pack('<Q', b))[0]


def main():
    out, count, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    rng = random.Random(seed)
    triples = []
    # 2-D family
    k = D // 262657
    assert k * 262657 == D
    m, n = two_squares_prime(262657, rng)
    legs = sorted([k * abs(m * m - n * n), 2 * k * m * n])
    assert legs[0] ** 2 + legs[1] ** 2 == D * D
    two_d = legs if (legs[0] % 2 == 0 or legs[0] < (1 << 53)) and (legs[1] % 2 == 0 or legs[1] < (1 << 53)) else None
    # 3-D family
    quads = []
    while len(quads) < max(1, count // 40):
        mm, nn = rng.randrange(1, 1 << 26), rng.randrange(1, 1 << 26)
        R = D - mm * mm - nn * nn
        if R <= 0 or R % 4 != 1 or not is_probable_prime(R):
            continue
        p, q = two_squares_prime(R, rng)
        a = mm * mm + nn * nn - p * p - q * q
        b = 2 * (mm * q + nn * p)
        c = 2 * (nn * q - mm * p)
        assert a * a + b * b + c * c == D * D
        if abs(a) < (1 << 53) and abs(b) < (1 << 54) and abs(c) < (1 << 54):
            quads.append((abs(a), abs(b), abs(c)))
    bases = ([tuple(two_d) + (0,)] if two_d else []) + quads
    while len(triples) < count:
        base = rng.choice(bases)
        s = rng.choice([970, 970, 969, 0, -1000, -1020] + [rng.randint(-1020, 970)])
        t = [exact(v, s) if v else 0.0 for v in base]
        if any(x is None for x in t):
            continue
        mode = rng.random()
        if mode < 0.15 and t[0] > 0:
            t[0] = nxt(t[0], rng.choice([-1, 1]))
        elif mode < 0.3 and t[2] == 0.0:
            e = 53 + s  # exponent of h * 2^s is 53 + s
            j = rng.randint(121, 400)
            if e - j >= -1074:
                t[2] = math.ldexp(1.0 + rng.random(), e - j)
        rng.shuffle(t)
        triples.append(tuple(-x if rng.random() < 0.5 else x for x in t))
    with open(out, 'wb') as fo:
        for t in triples:
            fo.write(struct.pack('<ddd', *t))
    with open(out + '.cat', 'wb') as fo:
        fo.write(bytes([5] * len(triples)))
    print({'triples': len(triples), 'two_d_base': bool(two_d), 'three_d_bases': len(quads)})


if __name__ == '__main__':
    main()
