"""I101 addendum 01: RS, TS and PY (I100's committed verdicts at b7721d27e9) on I100's 52 shapes, per reading, normalized to
gate:code or pass:eligible / pass:not_eligible. Counts the shapes where the readers differ, on the 44 preview probes and the 8
exact shapes, and checks RS and TS against I100's SHAPES.tsv expectation (bound, unbound, transport).
Usage: add1_compare.py <rs.jsonl> <ts.jsonl> <py.jsonl> <SHAPES.tsv> <out.json>"""
import csv, json, sys
def load(p): return [json.loads(l) for l in open(p) if l.strip()]
def mine(v): return f"{v['gate']}:{v['code']}" if "gate" in v else ("pass:eligible" if v["ok"]["eligible"] else "pass:not_eligible")
def py(v): return f"{v['err']['gate']}:{v['err']['code']}" if "err" in v else ("pass:eligible" if v["ok"]["numerical_eligible"] else "pass:not_eligible")
def tsv(v):
    k, _, s = v.partition(":")
    return v if k != "pass" else ("pass:eligible" if s == "eligible" else "pass:not_eligible")
R, T, P = load(sys.argv[1]), load(sys.argv[2]), {d["id"]: d for d in load(sys.argv[3])}
E = {r["id"]: r for r in csv.DictReader(open(sys.argv[4]), delimiter="\t")}
rows, differ, unexpected = [], {"preview": 0, "exact": 0}, []
for r, t in zip(R, T):
    assert r["name"] == t["name"]
    name = r["name"]; p = P[name]; e = E[name]; part = "exact" if " exact " in name else "preview"
    row = {"name": name, "base": r["base"]}
    any_diff = False
    for m in ("bound", "unbound", "transport"):
        a, b, c, x = mine(r[m]), mine(t[m]), py(p[m]), tsv(e[m])
        row[m] = {"rs": a, "ts": b, "py": c, "expected": x}
        if not (a == b == c): any_diff = True
        if a != x or b != x: unexpected.append((name, m, a, b, x))
    differ[part] += any_diff
    rows.append(row)
res = {"shapes": len(rows), "preview": sum(1 for r in rows if " exact " not in r["name"]), "exact": sum(1 for r in rows if " exact " in r["name"]),
       "shapes_where_readers_differ": differ, "rs_or_ts_unlike_expected": unexpected, "rows": rows}
json.dump(res, open(sys.argv[5], "w"), indent=1)
print(json.dumps({k: v for k, v in res.items() if k != "rows"})[:1500])
