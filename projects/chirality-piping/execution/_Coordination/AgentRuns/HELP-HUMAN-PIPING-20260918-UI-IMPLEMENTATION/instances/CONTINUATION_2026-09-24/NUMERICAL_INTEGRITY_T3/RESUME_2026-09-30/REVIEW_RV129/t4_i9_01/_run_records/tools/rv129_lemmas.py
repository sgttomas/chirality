"""RV129: adversarial exact-rational checks of the ball lemmas L1-L4 and L7 as
the design's probe implements them (b_add, b_mul, b_div, b_sqrt, invert).
For random balls with 128-bit midpoints and binary64 radii, every operand
is taken at a ball endpoint or interior point, the exact result is formed
in Fractions, and enclosure in the result ball is checked exactly.
Run: python -I rv129_lemmas.py <probe path>
"""
import importlib.util
import math
import random
import sys
from fractions import Fraction as Q

spec = importlib.util.spec_from_file_location("t4i9_probe", sys.argv[1])
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)
Ball, rnd, U = probe.Ball, probe.rnd, probe.U

rng = random.Random(1290)


def rand_ball(rel_lo=-40, rel_hi=-2, positive=False):
    mag = 10 ** rng.uniform(-6, 6)
    m = rnd(Q(rng.uniform(0.5, 1.0) * mag) * (1 if positive or rng.random() < 0.5 else -1)
            + Q(rng.getrandbits(100), 2 ** 140) * Q(mag))
    r = abs(float(m)) * 10 ** rng.uniform(rel_lo, rel_hi) if rng.random() < 0.9 else 0.0
    return Ball(m, r)


def points(b):
    r = Q(b.r)
    return [b.m - r, b.m + r, b.m, b.m + r * Q(rng.randrange(-1000, 1001), 1000)]


def inside(value, b):
    return abs(value - b.m) <= Q(b.r)


def exact_sqrt_bracket(x):
    """Fractions lo <= sqrt(x) <= hi with hi - lo tiny (x > 0)."""
    scale = 2 ** 400
    n = (x * scale * scale)
    s = math.isqrt(n.numerator // n.denominator)
    return Q(s, scale), Q(s + 1, scale)


def main():
    fails = {"add": 0, "mul": 0, "div": 0, "sqrt": 0, "inv": 0}
    counts = dict.fromkeys(fails, 0)
    for _ in range(3000):
        a, b = rand_ball(), rand_ball()
        for op, f, g in (("add", probe.b_add, lambda x, y: x + y), ("mul", probe.b_mul, lambda x, y: x * y)):
            res = f(a, b)
            for x in points(a):
                for y in points(b):
                    counts[op] += 1
                    fails[op] += not inside(g(x, y), res)
        try:
            res = probe.b_div(a, b)
            for x in points(a):
                for y in points(b):
                    counts["div"] += 1
                    fails["div"] += not inside(x / y, res)
        except ArithmeticError:
            pass
        p = rand_ball(positive=True)
        try:
            res = probe.b_sqrt(p)
            for x in points(p):
                lo, hi = exact_sqrt_bracket(x)
                counts["sqrt"] += 1
                fails["sqrt"] += not (inside(lo, res) and inside(hi, res))
        except ArithmeticError:
            pass
    # L7: ball matrices around a random SPD matrix; random members of the ball.
    for trial in range(40):
        n = 6
        A = [[Q(rng.uniform(-1, 1)) for _ in range(n)] for _ in range(n)]
        cond_scale = [10 ** rng.uniform(-3, 3) for _ in range(n)]
        F = [[sum(A[k][r] * A[k][c] for k in range(n)) * Q(cond_scale[r] * cond_scale[c]) +
              (Q(1) if r == c else Q(0)) * Q(cond_scale[r] ** 2) for c in range(n)] for r in range(n)]
        balls = [[Ball(rnd(F[r][c]), abs(float(F[r][c])) * 10 ** rng.uniform(-30, -12)) for c in range(n)]
                 for r in range(n)]
        try:
            K = probe.invert(probe.BallCtx(), balls)
        except ArithmeticError:
            continue
        for _ in range(3):
            G = [[balls[r][c].m + Q(balls[r][c].r) * Q(rng.randrange(-1000, 1001), 1000) for c in range(n)]
                 for r in range(n)]
            inv = probe.gauss_jordan(G, lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y,
                                     lambda x, y: x / y, Q(0), Q(1))
            for r in range(n):
                for c in range(n):
                    counts["inv"] += 1
                    fails["inv"] += not inside(inv[r][c], K[r][c])
    for op in fails:
        print("%s: %d exact checks, %d outside the ball" % (op, counts[op], fails[op]))


if __name__ == "__main__":
    main()
