"""T4-RV3: at UTM-skew coordinates the binary64 inputs leave representation kinks (~1e-10 rad) at the
bend ends; their remainders pAi(t_in - t_out) are load-bearing at the 1e-9 floors.  This drops them
(a product that treats sub-tolerance kinks as exact tangency) and reports the largest distance.

    python -I rv3_utm_remainder.py <u2_reference_cases.json>
"""
import json
import os
import sys
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv3_solve as S  # noqa: E402
import rv3_check as C  # noqa: E402

data = json.load(open(sys.argv[1]))
for cid, case in data["cases"].items():
    if not (case.get("transform") or "").startswith("SKEW"):
        continue
    n_int = len(case["inputs"]["geometry"]["traversal_order"]) - 2
    c = S.Case(case["inputs"], mutation={"remove_kink_at": list(range(1, n_int + 1))}).solve()
    leaves = []
    C.walk(case["expected"], c.results(), [], leaves)
    zs = {g: D(v["zero_scale"]) for g, v in case["zero_scale"].items()}
    best = (D(0), None)
    for path, ref, mine, _ in leaves:
        if ref in ("MISSING", "EXTRA"):
            continue
        g = C.group_of(path)
        if not g:
            continue
        d = abs(mine - ref) / (D("1e-9") * max(abs(ref), zs[g]))
        if d > best[0]:
            best = (d, "/".join(path))
    print("%-50s remainders dropped: max distance %.3e tolerances at %s" % (cid, best[0], best[1]))
