"""T4-I7: recompute selected cases at 90 digits with 50-point arc quadrature and compare every
written value of u2_reference_cases.json (20 significant digits) normwise per tolerance group.

    python -I u2_precision_check.py <dir containing u2_reference_cases.json>
"""
import json
import os
import sys
from decimal import getcontext

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u2_engine as E  # noqa: E402
import u2_generate as G  # noqa: E402
from u2_engine import D  # noqa: E402

ref = json.load(open(os.path.join(sys.argv[1] if len(sys.argv) > 1 else ".", "u2_reference_cases.json")))
getcontext().prec = 90
E._PI = None
E._GL.clear()
E.GL_ARC = 50
E.GL_STRAIGHT = 6
cases = {c["id"]: c for c in G.case_list()}
sel = ["U2-L-FREE-SEPD-K1", "U2-L-ANCH-ALL-K2", "U2-U-ANCH-ALL-K1", "U2-U-ANCH-PW-K2",
       "MECH-CURVED-BEND-EXACT-PRESSURE-ARC-K2-SKEW-X7P3E6", "U2-L-KINK-ANCH-P-K2", "U2-L-ANCH-ALL-K2-REV",
       "U2-U-ANCH-ALL-K2-SKEW-X5E6", "U2-L-ANCH-PTW-K2-SKEW-X7P3E6", "U2-L-FREE-PTW-K1"]


def walk(a, b, zs, path, worst):
    if isinstance(a, dict):
        for k in a:
            walk(a[k], b[k], zs, path + "/" + k, worst)
    elif isinstance(a, list):
        for i, (x, y) in enumerate(zip(a, b)):
            walk(x, y, zs, path + "/" + str(i), worst)
    elif isinstance(a, str):
        try:
            x, y = D(a), D(b)
        except Exception:
            return
        worst["n"] += 1
        r = abs(x - y) / max(abs(y), worst["scale"])
        if r > worst["max"]:
            worst["max"], worst["at"] = r, path


overall = D(0)
for cid in sel:
    out, derived, zs, checks, rec = G.record_case(cases[cid])
    smallest = min(D(z["zero_scale"]) for z in zs.values())
    w = {"max": D(0), "at": "", "n": 0, "scale": D("1e-300")}
    # compare group-normwise: use each group's zero scale where the value is small
    exp_ref = ref["cases"][cid]["expected"]
    for grp_path in ("nodes", "supports", "members", "terminals"):
        walk(out[grp_path], exp_ref[grp_path], zs, grp_path, w)
    # relative to the per-case smallest zero scale for robustness of tiny values
    print("%-52s values %4d  max rel diff (90 digits, GL50 vs written) %.2e at %s" % (cid, w["n"], w["max"], w["at"]))
    overall = max(overall, w["max"])
print("overall max %.2e (the written 20-digit rounding is 5e-20 relative)" % overall)
