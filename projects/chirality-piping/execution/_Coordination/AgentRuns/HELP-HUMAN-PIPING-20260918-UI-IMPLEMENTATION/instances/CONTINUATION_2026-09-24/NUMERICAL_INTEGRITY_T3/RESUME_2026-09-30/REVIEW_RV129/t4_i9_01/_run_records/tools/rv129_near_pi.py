"""RV129: radius growth of T4-I9's certificate toward phi = pi, with the
design's L5 (Lipschitz constant 1) and with a sharpened L5 that uses the
derivative bound 1/(1 + (m_t - r_t)^2) of atan on the ball. Arcs are built
with skew chords so that 1 - s reaches ~1e-19 (phi ~ pi - 1e-9).
Run: python -I rv129_near_pi.py <probe path> <rv129_ref.py path>
"""
import importlib.util
import math
import random
import sys
from fractions import Fraction as Q


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


probe = load(sys.argv[1], "t4i9_probe")
ref = load(sys.argv[2], "rv129_ref")
design_atan = probe.b_atan


def sharpened_atan(t):
    if t.m - Q(t.r) <= 0:
        raise ArithmeticError("atan argument ball not positive")
    m = probe.rnd(probe.dec_to_q(probe.atan_decimal(probe.q_to_dec(t.m))))
    low = t.m - Q(t.r)
    r = Q(t.r) / (1 + low * low) + probe.ATAN_REL * probe.U * m / (1 - probe.ATAN_REL * probe.U)
    return probe.Ball(m, probe.up(r))


def near_pi_case(rng, target):
    """Skew chord with |d| = L in binary64 components, R the binary64 value
    just above L/2, retried until 1 - s is near `target`."""
    best = None
    for _ in range(200000):
        a = rng.uniform(0.2, 1.3)
        d = [0.4572 * math.cos(a), 0.4572 * math.sin(a), 0.0]
        L = Q(d[0]) ** 2 + Q(d[1]) ** 2
        half = math.sqrt(float(L)) / 2
        R = half
        for _ in range(4):
            R = math.nextafter(R, 0.0)
        while Q(R) ** 2 * 4 <= L:     # the smallest binary64 R with 2R > L
            R = math.nextafter(R, math.inf)
        one_minus_s2 = 1 - L / (4 * Q(R) ** 2)
        if best is None or abs(math.log10(float(one_minus_s2)) - math.log10(target)) < best[0]:
            best = (abs(math.log10(float(one_minus_s2)) - math.log10(target)), d, R, one_minus_s2)
            if best[0] < 0.3:
                break
    _, d, R, oms2 = best
    xi = [0.0, 0.0, 0.0]          # at the origin so that x_j - x_i = d exactly
    xj = [d[0], d[1], 0.0]
    return xi, xj, R, oms2


def main():
    rng = random.Random(1291)
    area, inertia, torsion = ref.section(0.1683, 0.00711)
    em = 2.03e11
    gm = em / 2.6
    print("phi target | 1-s^2 (exact) | phi | design L5: rad/max|f| | sharpened L5: rad/max|f| | enclosed (both)")
    for target in (1e-12, 1e-15, 1e-17, 1e-19):
        xi, xj, R, oms2 = near_pi_case(rng, target)
        # the y_reference points away from the chord, in the xy plane
        d = [xj[k] - xi[k] for k in range(3)]
        yref = [-d[1], d[0], 0.0]
        args = (xi, xj, R, yref, em, gm, area, inertia, torsion, 1.0, 1.0, [0.0, 0.0, -450.0])
        f, phi, _ = ref.reference(*args)
        scale = max(abs(v) for v in f)
        out = []
        for atan in (design_atan, sharpened_atan):
            probe.b_atan = atan
            try:
                ball, _ = probe.formula(probe.BallCtx(), *args)
            except ArithmeticError as error:
                out.append(("refused: %s" % error, False))
                continue
            enclosed = all(abs(Q(f[k]) - ball[k].m) <= Q(ball[k].r) for k in range(12))
            out.append(("%.2e" % (max(b.r for b in ball) / float(scale)), enclosed))
        probe.b_atan = design_atan
        print("%.0e | %.2e | pi - %.3e | %s | %s | %s"
              % (target, float(oms2), float(ref.pi_dec() - phi), out[0][0], out[1][0],
                 out[0][1] and out[1][1]))


if __name__ == "__main__":
    main()
