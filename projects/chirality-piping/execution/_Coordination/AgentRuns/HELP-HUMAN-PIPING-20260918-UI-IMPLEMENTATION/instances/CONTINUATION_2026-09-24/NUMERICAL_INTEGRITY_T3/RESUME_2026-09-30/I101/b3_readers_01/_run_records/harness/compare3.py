"""I101: the three readers' B3b verdicts (bound, unbound, transport) on one shape set (the Rust reader's materialized
inputs; TS's materialized inputs are compared equal by compare_shapes.py, PY reads the Rust inputs). Equal at every gate and
code except G7, where each reader reports its own base code (C1 G7 settlement); G7 rows list the three codes.
Usage: compare3.py <rs readings> <ts readings> <py readings> <out.json>"""
import json, sys, collections
def load(p): return {(d["name"], d["base"]): d for d in map(json.loads, (l for l in open(p) if l.strip()))}
R, T, P = (load(p) for p in sys.argv[1:4])
assert set(R) == set(T) == set(P), "the same shapes"
diffs, g7, verdicts = [], collections.Counter(), collections.Counter()
for k in sorted(R):
    for m in ("bound", "unbound", "transport"):
        a, b, c = R[k][m], T[k][m], P[k][m]
        if a.get("gate") == b.get("gate") == c.get("gate") == "G7":
            g7[(m, a["code"], b["code"], c["code"])] += 1
            verdicts[(m, "G7")] += 1
        elif a == b == c:
            verdicts[(m, a.get("gate") or ("eligible" if a["ok"]["eligible"] else "ok, not eligible"))] += 1
        else:
            diffs.append({"name": k[0], "base": k[1], "reading": m, "rs": a, "ts": b, "py": c})
bases = collections.Counter(k[1] for k in R)
res = {"shapes": len(R), "bases": dict(bases), "differences_outside_g7": diffs,
       "g7_codes": [{"reading": m, "rs": a, "ts": b, "py": c, "shapes": n} for (m, a, b, c), n in sorted(g7.items())],
       "verdicts": [{"reading": m, "verdict": v, "shapes": n} for (m, v), n in sorted(verdicts.items())]}
json.dump(res, open(sys.argv[4], "w"), indent=1)
print(json.dumps({"shapes": len(R), "differences_outside_g7": len(diffs), "g7_code_triples": len(g7)}))
