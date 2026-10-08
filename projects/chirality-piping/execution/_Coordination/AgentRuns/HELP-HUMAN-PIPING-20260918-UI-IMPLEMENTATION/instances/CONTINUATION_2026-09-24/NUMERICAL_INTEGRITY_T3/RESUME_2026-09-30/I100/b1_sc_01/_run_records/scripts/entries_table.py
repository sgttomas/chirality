"""I100 B1 SC: every 07n base and entry with its kind, base, item, origin, and each reader's first failure.

Usage: entries_table.py <corpus.json> <plan.json> <py.jsonl> <rs.jsonl> <ts.jsonl> <out.json> <out.tsv>
A reader's verdict is its census line at the SC head: "pass[/eligible]" or "gate code", for bound, unbound and
transport.
"""
import json
import sys

corpus_p, plan_p, py_p, rs_p, ts_p, out_json, out_tsv = sys.argv[1:8]
c = json.load(open(corpus_p))
plan = {e["id"]: e for e in json.load(open(plan_p))["entries"]}
runs = {}
for r, p in (("python", py_p), ("rust", rs_p), ("typescript", ts_p)):
    runs[r] = {(x["set"], x["id"]): x for x in (json.loads(l) for l in open(p) if l.strip())}


def short(v):
    if "ok" in v:
        return "pass" + ("/eligible" if v["ok"]["numerical_eligible"] else "")
    if "err" in v:
        return f'{v["err"]["gate"]} {v["err"]["code"]}'
    return "escape"


rows = []
for b in c["cases"][17:]:
    rows.append({"kind": "base", "id": b["id"], "base": "", "item": "base", "origin": b["provenance"] if isinstance(b["provenance"], str) else b["provenance"]["kind"],
                 **{f"{r}_{x}": short(runs[r][("base", b["id"])][x]) for r in runs for x in ("bound", "unbound", "transport")}})
for kind, start, setname in (("mutation", 294, "mutation"), ("must_pass", 28, "must_pass")):
    for e in c["mutations" if kind == "mutation" else "must_pass"][start:]:
        p = plan[e["id"]]
        rows.append({"kind": kind, "id": e["id"], "base": e["base"], "item": p["item"], "origin": p["source"],
                     **{f"{r}_{x}": short(runs[r][(setname, e["id"])][x]) for r in runs for x in ("bound", "unbound", "transport")}})
json.dump(rows, open(out_json, "w"), indent=1)
cols = ["kind", "id", "base", "item", "origin"] + [f"{r}_{x}" for r in ("python", "rust", "typescript") for x in ("bound", "unbound", "transport")]
with open(out_tsv, "w") as f:
    f.write("\t".join(cols) + "\n")
    for r in rows:
        f.write("\t".join(str(r[k]) for k in cols) + "\n")
print(len(rows), "rows")
