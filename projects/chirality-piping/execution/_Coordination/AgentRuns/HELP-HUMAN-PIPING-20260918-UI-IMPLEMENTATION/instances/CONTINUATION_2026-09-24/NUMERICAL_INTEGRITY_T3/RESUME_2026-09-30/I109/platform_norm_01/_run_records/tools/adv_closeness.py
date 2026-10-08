#!/usr/bin/env python3
"""I109: how close the oracle's adversarial triples (the last N of the input file) are to a
rounding midpoint of the exact norm3, in ulps (exact Fractions), on every k-th triple.
Usage: adv_closeness.py <oracle_in.bin> <adversarial count> <step>"""
import json, math, os, struct, sys
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import norm_oracle as o
path, n, step = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
size = os.path.getsize(path) // 24
hist = {}
with open(path, "rb") as f:
    for i in range(size - n, size, step):
        f.seek(24 * i); t = struct.unpack("<3d", f.read(24))
        if any(math.isinf(x) or math.isnan(x) for x in t): k = "special"
        else:
            r = o.ref_norm(list(t))
            if r == 0 or math.isinf(r): k = "zero_or_overflow"
            else:
                S = sum(Fraction(x) ** 2 for x in t); g = Fraction(r)
                up = Fraction(math.nextafter(r, math.inf)) if r < sys.float_info.max else Fraction(2) ** 1024
                dn = Fraction(math.nextafter(r, 0.0))
                u = up - g
                d = min(abs(S - ((g + up) / 2) ** 2), abs(S - ((g + dn) / 2) ** 2)) / (2 * g) / u
                k = "exact_midpoint" if d == 0 else "<2^-40 ulp" if d < Fraction(1, 2 ** 40) else "<2^-20 ulp" if d < Fraction(1, 2 ** 20) else ">=2^-20 ulp"
        hist[k] = hist.get(k, 0) + 1
print(json.dumps({"sampled": sum(hist.values()), "of_adversarial": n, "closeness": hist}))
