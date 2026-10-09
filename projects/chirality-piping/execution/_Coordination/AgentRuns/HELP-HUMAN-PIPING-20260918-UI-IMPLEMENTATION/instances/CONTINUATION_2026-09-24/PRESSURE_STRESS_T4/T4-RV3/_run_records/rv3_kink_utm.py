"""T4-RV3: the kink controls against alpha_tan = 1e-3 rad, and the UTM coordinate transport.

    python -I rv3_kink_utm.py <u2_reference_cases.json> <u2_document_sketches.json>
"""
import json
import math
import os
import sys
from decimal import Decimal as D

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv3_lib as L  # noqa: E402
import rv3_solve as S  # noqa: E402
import rv3_check as C  # noqa: E402

ALPHA = D("1e-3")


def kink_part(data):
    print("== kink controls against alpha_tan = 1e-3 rad (theta <= alpha_tan admitted) ==")
    for cid in ("U2-L-KINK-FREE-P-K2", "U2-L-KINK-ANCH-P-K2"):
        inp = data["cases"][cid]["inputs"]
        c = S.Case(inp)
        (node, th), = [k for k in c.kinks() if k[1] > D("1e-12")]
        tin, tout = c.t_end(1), c.t_start(2)
        cr = L.norm(L.cross(tin, tout))
        dt = L.dot(tin, tout)
        print(cid, "node", node)
        print("   D.x as binary64        = %s" % D(float(inp["geometry"]["node_coordinates_binary64_exact"]["node:D"][0])))
        print("   theta (exact, from the binary64 inputs) = %.15e rad" % th)
        print("   alpha_tan - theta      = %.6e rad (relative %.3e)" % (ALPHA - th, (ALPHA - th) / ALPHA))
        print("   tan(theta) - alpha_tan = %.6e   (a 'tan theta <= alpha_tan' test refuses)" % (cr / dt - ALPHA))
        print("   sin(theta) - alpha_tan = %.6e" % (cr - ALPHA))
        s1, c1 = L.sincos(ALPHA)
        print("   (1-cos theta) - (1-cos alpha) = %.6e" % ((1 - dt) - (1 - c1)))
        print("   tan(theta) - tan(alpha) = %.6e" % (cr / dt - s1 / c1))
        # binary64 emulation of the shared kink function: atan2(|a x b|, a.b)
        a = [float(x) for x in tin]
        b = [float(x) for x in tout]
        crf = [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
        thf = math.atan2(math.sqrt(sum(x * x for x in crf)), sum(x * y for x, y in zip(a, b)))
        print("   binary64 atan2 kink    = %.17e ; minus exact %.3e ; admitted at 1e-3: %s" % (
            thf, D(thf) - th, thf <= 1e-3))
        # the same from raw node differences (S2 direction) and the arc end tangent in binary64
        print("   remainder |pAi (t_in - t_out)| = %.6e N" % L.norm(L.mul(c.P, L.sub(tin, tout))))


def utm_part(data, sketches):
    print("== UTM transport ==")
    bad_rt = []
    for cid, case in data["cases"].items():
        g = case["inputs"]["geometry"]
        strs = [s for xyz in g["node_coordinates_binary64_exact"].values() for s in xyz]
        strs += [s for m in g["members"] for s in m["y_reference_binary64_exact"]]
        for s in strs:
            if repr(float(s)) != s:
                bad_rt.append((cid, s))
    print("coordinate / y_reference strings that are not round-trip binary64 reprs: %d" % len(bad_rt))
    # sketches: node positions equal float(reference strings)?
    mism = 0
    for cid, case in data["cases"].items():
        g = case["inputs"]["geometry"]
        scale = 1000.0 if case["inputs"]["units_of_document"] == "mm" else 1.0
        for ver in ("0.3.0", "0.4.0"):
            doc = sketches["sketches"][cid][ver]["document"]["model"]
            for n in doc["nodes"]:
                ref = [float(s) for s in g["node_coordinates_binary64_exact"][n["id"]]]
                got = [n["position"][k] / scale for k in "xyz"] if scale != 1.0 else [n["position"][k] for k in "xyz"]
                if scale == 1.0 and got != ref:
                    mism += 1
                if scale != 1.0 and any(abs(x - y) > 1e-15 * max(1.0, abs(y)) for x, y in zip(got, ref)):
                    mism += 1
    print("sketch node positions differing from the reference binary64 coordinates: %d" % mism)
    print("-- sensitivity: the same cases computed from the short decimal strings taken as exact decimals --")
    for cid, case in data["cases"].items():
        if case.get("transform") not in ("X5E6", "X7P3E6", "SKEW", "SKEW-X5E6", "SKEW-X7P3E6"):
            continue
        c = S.Case(case["inputs"], exact_decimal_coords=True).solve()
        n, worst, missing = C.compare(case, c.results())
        print("   %-50s max normalized diff vs reference %.2e at %s" % (cid, worst[0], worst[1]))


if __name__ == "__main__":
    data = json.load(open(sys.argv[1]))
    sk = json.load(open(sys.argv[2]))
    kink_part(data)
    utm_part(data, sk)
