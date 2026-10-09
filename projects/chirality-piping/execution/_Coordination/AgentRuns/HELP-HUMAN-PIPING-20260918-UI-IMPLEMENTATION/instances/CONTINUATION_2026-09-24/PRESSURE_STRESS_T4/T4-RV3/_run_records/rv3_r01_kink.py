"""T4-RV3 addendum 01: the repaired kink controls (D.x = 3.248) and the new refusal control (D.x = 3.242)
against alpha_tan = 1e-3 rad, under several measures of the junction angle, exact and in binary64.

    python -I -B rv3_r01_kink.py <round-01 u2_reference_cases.json>
"""
import json
import math
import os
import sys
from decimal import Decimal as D

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv3_lib as L  # noqa: E402
import rv3_solve as S  # noqa: E402

ALPHA = D("1e-3")
data = json.load(open(sys.argv[1]))
s1, c1 = L.sincos(ALPHA)
for cid in ("U2-L-KINK-FREE-P-K2", "U2-L-KINK-ANCH-P-K2", "U2-L-MITRE-REFUSED-P-K2"):
    inp = data["cases"][cid]["inputs"]
    c = S.Case(inp)
    (node, th), = [k for k in c.kinks() if k[1] > D("1e-12")]
    tin, tout = c.t_end(1), c.t_start(2)
    cr, dt = L.norm(L.cross(tin, tout)), L.dot(tin, tout)
    a = [float(x) for x in tin]
    b = [float(x) for x in tout]
    crf = [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
    thf = math.atan2(math.sqrt(sum(x * x for x in crf)), sum(x * y for x, y in zip(a, b)))
    print("%s node %s: D.x binary64 %s" % (cid, node, D(float(inp["geometry"]["node_coordinates_binary64_exact"]["node:D"][0]))))
    print("   theta %.16e rad; theta - alpha_tan %.6e; tan(theta) - alpha_tan %.6e; sin(theta) - alpha_tan %.6e;"
          " (1-cos theta) - (1-cos alpha) %.6e; tan(theta) - tan(alpha) %.6e" % (
              th, th - ALPHA, cr / dt - ALPHA, cr - ALPHA, (1 - dt) - (1 - c1), cr / dt - s1 / c1))
    print("   binary64 atan2 kink %.17e (minus exact %.2e); admitted (theta <= 1e-3): %s" % (thf, D(thf) - th, thf <= 1e-3))
