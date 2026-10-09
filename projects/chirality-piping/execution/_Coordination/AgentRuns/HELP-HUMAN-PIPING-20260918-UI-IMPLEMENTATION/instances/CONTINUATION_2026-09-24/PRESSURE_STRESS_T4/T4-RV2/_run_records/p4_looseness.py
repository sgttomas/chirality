"""T4-RV2: how loose is P4's matrix-scale criterion? max|K| / min_i K_ii per frozen case
(the factor by which 1e-9*max|K| exceeds 1e-9 of the smallest diagonal stiffness).
usage: python -I p4_looseness.py U1_REFERENCE_CASES_JSON"""
import sys, json
from decimal import Decimal as D
doc = json.load(open(sys.argv[1]))
rows = []
for c in doc["cases"]:
    K = [[D(v) for v in r] for r in c["K_global"]]
    m = max(abs(v) for r in K for v in r)
    rows.append((float(m / min(K[i][i] for i in range(12))), c["id"]))
rows.sort()
for r, cid in rows:
    print("%-28s max|K|/min K_ii = %.3g" % (cid, r))
print("WORST %.3g (%s)" % rows[-1])
