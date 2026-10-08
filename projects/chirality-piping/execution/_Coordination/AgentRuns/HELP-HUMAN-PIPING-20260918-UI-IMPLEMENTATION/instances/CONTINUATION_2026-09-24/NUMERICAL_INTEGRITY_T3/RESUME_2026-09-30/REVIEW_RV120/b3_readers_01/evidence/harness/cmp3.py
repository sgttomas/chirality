"""RV120 (B3): compare the three readers' raw readings (bound, unbound, transport) on one input set, and each bound
reading with the probe's stated want ('?' = no want). Equal means gate and code (or ok/eligible); at G7 each reader's own
base code is listed, not compared (C1's G7 settlement). Usage: cmp3.py <inputs.jsonl> <rs> <ts> <py> [out.json]"""
import json, sys, collections
ins = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]
R, T, P = ([json.loads(l) for l in open(p) if l.strip()] for p in sys.argv[2:5])
assert len(ins) == len(R) == len(T) == len(P)
def v(x):
    if "ok" in x: return "eligible" if x["ok"]["eligible"] else "ok"
    if "gate" in x: return f"{x['gate']} {x['code'].removeprefix('RETAINED_PRECISION_')}"
    return "ESCAPE " + json.dumps(x)
diffs, want_miss, g7, tally = [], [], collections.Counter(), collections.Counter()
for i, (d, r, t, p) in enumerate(zip(ins, R, T, P)):
    assert r["name"] == t["name"] == p["name"] == d["name"]
    for m in ("bound", "unbound", "transport"):
        a, b, c = v(r[m]), v(t[m]), v(p[m])
        if a.startswith("G7 ") and b.startswith("G7 ") and c.startswith("G7 "): g7[(m, a, b, c)] += 1; tally[(m, "G7")] += 1
        elif a == b == c: tally[(m, a)] += 1
        else: diffs.append({"i": i, "name": d["name"], "reading": m, "rs": a, "ts": b, "py": c,
                            "details": {"rs": r[m].get("detail"), "ts": t[m].get("detail"), "py": p[m].get("detail")}})
    w = d.get("want")
    if w and w != "?":
        w2 = w.replace("RETAINED_PRECISION_", "")
        for name, x in (("rs", r), ("ts", t), ("py", p)):
            if v(x["bound"]) != w2: want_miss.append({"i": i, "name": d["name"], "reader": name, "want": w2, "got": v(x["bound"])})
res = {"inputs": len(ins), "differences_outside_g7": diffs, "want_misses": want_miss,
       "g7": [{"reading": m, "rs": a, "ts": b, "py": c, "n": n} for (m, a, b, c), n in sorted(g7.items())],
       "tally": [{"reading": m, "verdict": x, "n": n} for (m, x), n in sorted(tally.items())],
       "unwanted_bound": [{"i": i, "name": d["name"], "rs": v(r["bound"]), "ts": v(t["bound"]), "py": v(p["bound"])} for i, (d, r, t, p) in enumerate(zip(ins, R, T, P)) if d.get("want") == "?"]}
if len(sys.argv) > 5: json.dump(res, open(sys.argv[5], "w"), indent=1)
print(json.dumps({"inputs": len(ins), "differences_outside_g7": len(diffs), "want_misses": len(want_miss), "g7_triples": len(g7)}))
for x in diffs: print("DIFF", x["i"], x["name"], x["reading"], "rs:", x["rs"], "| ts:", x["ts"], "| py:", x["py"])
for x in want_miss: print("WANT", x["i"], x["name"], x["reader"], "want", x["want"], "got", x["got"])
for x in res["unwanted_bound"]: print("OPEN", x["i"], x["name"], "rs:", x["rs"], "| ts:", x["ts"], "| py:", x["py"])
for x in res["g7"]: print("G7", x)
