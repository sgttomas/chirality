"""I104 SQ G5: per-function TEXT requested bytes (branch W) at c = 1, 2, 3 on B1's real code, and the second
difference d2 = T(3) - 2 T(2) + T(1); a positive d2 is a site group growing faster than linearly in c (STUDY §3.3's
c² sites). Usage: second_diff.py <tb W c1> <tb W c2> <tb W c3>"""
import json, sys, collections
def agg(p):
    t = json.load(open(p)); d = collections.Counter()
    for r in t["rows"]:
        if r["mult"]:
            k = r["fn"] or ""; d[k.rsplit(":", 2)[0].replace("core/", "", 1).replace("/src/", "/") + ":" + k.rsplit(":", 1)[-1]] += r["req"]
    return t["total_text_requested_bytes"], d
(t1, a), (t2, b), (t3, c) = (agg(p) for p in sys.argv[1:4])
print(json.dumps({"TAV_W": [t1, t2, t3], "first_differences": [t2 - t1, t3 - t2], "second_difference": t3 - 2 * t2 + t1}))
rows = sorted(((k, c[k] - 2 * b[k] + a[k], a[k], b[k], c[k]) for k in set(a) | set(b) | set(c)), key=lambda x: -x[1])
pos = [r for r in rows if r[1] > 0]
print(f"positive d2: {len(pos)} functions, sum {sum(r[1] for r in pos):,}; negative d2 sum {sum(r[1] for r in rows if r[1] < 0):,}")
print(f"{'d2':>14} {'c=1':>14} {'c=2':>14} {'c=3':>14}  fn")
for k, d2, x, y, z in pos[:25]:
    print(f"{d2:>14,} {x:>14,} {y:>14,} {z:>14,}  {k}")
