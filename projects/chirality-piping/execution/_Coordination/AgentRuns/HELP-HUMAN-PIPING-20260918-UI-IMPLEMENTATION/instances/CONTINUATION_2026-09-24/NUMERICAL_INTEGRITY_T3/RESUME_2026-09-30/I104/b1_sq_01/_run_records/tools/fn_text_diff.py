"""I104 SQ G5: TEXT requested bytes by function (fn name and file), between two text_budget outputs (e.g. I82's
emulated c = 3 run and B1's real one, or the base and B1 at c = 1), with each function's multiplicity.
Usage: fn_text_diff.py <first text_budget json> <second> [top]"""
import json, sys, collections
a, b = (json.load(open(p)) for p in sys.argv[1:3]); top = int(sys.argv[3]) if len(sys.argv) > 3 else 40
def key(k):
    """crate-relative file and fn name, without the line (lines move between bases)"""
    f = k.rsplit(":", 2)[0].replace("core/", "", 1).replace("/src/", "/")
    return f + ":" + k.rsplit(":", 1)[-1]
def agg(t):
    d, m = collections.Counter(), {}
    for r in t["rows"]:
        if r["mult"]:
            d[key(r["fn"] or "")] += r["req"]
    for k, v in t["function_multiplicity"].items():
        m[key(k)] = v
    return d, m
(A, MA), (B, MB) = agg(a), agg(b)
rows = sorted(((k, B[k] - A[k], A[k], B[k], MA.get(k, 0), MB.get(k, 0)) for k in set(A) | set(B) if B[k] != A[k]), key=lambda x: -abs(x[1]))
print(json.dumps({"tav": [a["total_text_requested_bytes"], b["total_text_requested_bytes"]], "delta": b["total_text_requested_bytes"] - a["total_text_requested_bytes"],
                  "D": [a["D_diagnostics"], b["D_diagnostics"]]}))
print(f"{'delta':>14} {'first':>14} {'second':>14} {'M first':>9} {'M second':>9}  fn")
for k, d, x, y, mx, my in rows[:top]:
    print(f"{d:>14,} {x:>14,} {y:>14,} {mx:>9,} {my:>9,}  {k}")
print("rows:", len(rows), "sum of all deltas:", sum(r[1] for r in rows))
