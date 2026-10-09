"""RV131 M31b0 attack: at p = 128, compare K-D5's actual chord A_p.d_p with the formula chord
R(cos phi - 1), R sin phi, 0 evaluated at p, over adversarial admissible inputs.
Spellings of the formula: (i) cos = 1 - 2 s^2 at p (B1's trigonometry), sin = 2 s c;
(ii) cos and sin of the rounded phi_p, each correctly rounded at p (a libm-at-p spelling).
usage: python -I rv_m31b0_attack.py"""
import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from decimal import Decimal as D, localcontext
import rv_wide as W
import rv_element as RV

ar = W.P(128)

def chords(xi, xj, R, y):
    r = ar
    xi = [Fr(v) for v in xi]; xj = [Fr(v) for v in xj]; y = [Fr(v) for v in y]; R = Fr(R)
    d = [r.sub(xj[k], xi[k]) for k in range(3)]
    L = r.sqrt(r.dot3(d, d))
    twoR = 2 * R
    s = r.div(L, twoR)
    c = r.div(r.sqrt(r.mul(r.sub(twoR, L), r.add(twoR, L))), twoR)
    phi = 2 * r.atan2_q1(s, c)
    dh = [r.div(d[k], L) for k in range(3)]
    proj = r.dot3(y, dh)
    yc = [r.sub(y[k], r.mul(proj, dh[k])) for k in range(3)]
    ym = r.sqrt(r.dot3(yc, yc))
    n = [r.div(yc[k], ym) for k in range(3)]
    ex = [r.add(-r.mul(s, dh[k]), r.mul(c, n[k])) for k in range(3)]
    ey = [r.add(r.mul(c, dh[k]), r.mul(s, n[k])) for k in range(3)]
    ez = r.cross3(n, dh)
    act = [r.dot3(ex, d), r.dot3(ey, d), r.dot3(ez, d)]
    cos1 = r.sub(1, 2 * r.mul(s, s)); sin1 = 2 * r.mul(s, c)
    f1 = [r.mul(R, r.sub(cos1, 1)), r.mul(R, sin1), Fr(0)]
    with localcontext() as cx:
        cx.prec = 90
        sp, cp = RV.d_sincos(D(phi.numerator) / D(phi.denominator))
    cos2, sin2 = ar.r(Fr(cp)), ar.r(Fr(sp))
    f2 = [r.mul(R, r.sub(cos2, 1)), r.mul(R, sin2), Fr(0)]
    Lf = float(L)
    def rel(f):
        return math.sqrt(sum(float(f[k] - act[k]) ** 2 for k in range(3))) / Lf
    return float(phi), rel(f1), rel(f2), float(ym)

def radius(L, phi):
    with localcontext() as c:
        c.prec = 60
        s, _ = RV.d_sincos(D(phi) / 2)
        return float(D(L) / (2 * s))

rng = random.Random(20261008)
rows = []


def case(tag, X, L, phi, ydir=None, near_parallel=None):
    u = [rng.gauss(0, 1) for _ in range(3)]; nu = math.sqrt(sum(v * v for v in u)); u = [v / nu for v in u]
    xi = [X + rng.uniform(0, 1000), 0.7 * X + rng.uniform(0, 1000), rng.uniform(-50, 50)]
    xj = [xi[k] + L * u[k] for k in range(3)]
    d = [xj[k] - xi[k] for k in range(3)]
    Lb = math.sqrt(sum(v * v for v in d))
    R = radius(Lb, phi)
    if R <= Lb / 2:
        return
    if near_parallel is not None:
        w = [rng.gauss(0, 1) for _ in range(3)]
        dh = [v / Lb for v in d]
        wd = sum(w[k] * dh[k] for k in range(3)); w = [w[k] - wd * dh[k] for k in range(3)]
        nw = math.sqrt(sum(v * v for v in w)); w = [v / nw for v in w]
        y = [dh[k] + near_parallel * w[k] for k in range(3)]
    else:
        y = ydir or [rng.gauss(0, 1) for _ in range(3)]
    ph, e1, e2, ym = chords(xi, xj, R, y)
    rows.append((tag, X, L, ph, ym, e1, e2))


if __name__ == "__main__":
    for _ in range(150):
        case("random", rng.choice([0.0, 5e5, 5e6, 7.3e6]), 10 ** rng.uniform(-3, 2), 10 ** rng.uniform(-9, 0.3))
    for _ in range(80):
        case("near-pi", rng.choice([0.0, 7.3e6]), 10 ** rng.uniform(-2, 1), math.pi - 10 ** rng.uniform(-9, -1))
    for _ in range(80):
        case("floor", rng.choice([0.0, 7.3e6]), 10 ** rng.uniform(-3, 2), 1e-9 * (1 + rng.uniform(0, 1)))
    for _ in range(60):
        case("y-near-parallel", rng.choice([0.0, 7.3e6]), 10 ** rng.uniform(-2, 1), 10 ** rng.uniform(-9, 0.3), near_parallel=10 ** rng.uniform(-9, -7))
    print("cases:", len(rows))
    for tag in ("random", "near-pi", "floor", "y-near-parallel"):
        sel = [r for r in rows if r[0] == tag]
        w1 = max(sel, key=lambda r: r[5]); w2 = max(sel, key=lambda r: r[6])
        s1 = max(r[5] * min(r[3], math.pi - r[3]) for r in sel); s2 = max(r[6] * min(r[3], math.pi - r[3]) for r in sel)
        print("%-16s n=%3d  max|dc|/L (i) %.2e at phi %.3e | (ii) %.2e at phi %.3e | max (|dc|/L)*min(phi,pi-phi): (i) %.2e (ii) %.2e  [2^-127 = %.2e]"
              % (tag, len(sel), w1[5], w1[3], w2[6], w2[3], s1, s2, 2.0 ** -127))
    allmax = max(max(r[5], r[6]) for r in rows)
    print("overall max |dc|/L = %.2e ; implied EF ratio <= 1.3e9 x that = %.1e of the criterion (trigger 2x)" % (allmax, 1.3e9 * allmax))
