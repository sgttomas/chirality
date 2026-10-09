"""RV131 M31b0 attack, ill-conditioned y: PP's plane tolerance is absolute (|y_perp| > 1e-9 on the
unnormalized y), so |y|/|y_perp| is unbounded. Chord difference at p = 128 versus that ratio.
usage: python -I rv_m31b0_yscale.py"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rv_m31b0_attack import chords, radius
d = [0.25980762112885714, 0.15000000037252903, 0.0]
L = math.sqrt(sum(v * v for v in d))
dh = [v / L for v in d]
for ratio in (1e9, 1e15, 1e20, 1e25, 1e28, 1e30):
    big = ratio * 2e-9
    y = [big * dh[0] - 2e-9 * dh[1], big * dh[1] + 2e-9 * dh[0], 0.0]
    for phi in (math.pi / 2, 1e-8):
        R = radius(L, phi)
        ph, e1, e2, ym = chords([0.0, 0.0, 0.0], d, R, y)
        print("|y|/|y_perp| %.0e  phi %.3e  |y_perp|_p %.2e  |dc|/L (i) %.2e (ii) %.2e  -> EF <= %.1e crit" % (ratio, ph, ym, e1, e2, 1.3e9 * max(e1, e2)))
