"""I100 B3: compare two PY census runs entry by entry (input sha256, bound, unbound, transport verdicts in full).
Usage: census_cmp.py <from.jsonl> <to.jsonl> <out.json>"""
import json, sys
def load(p):
    return {(r["set"], r["i"]): r for r in (json.loads(l) for l in open(p) if l.strip())}
a, b = load(sys.argv[1]), load(sys.argv[2])
changes = []
for k in sorted(set(a) | set(b)):
    ra, rb = a.get(k), b.get(k)
    if ra is None or rb is None:
        changes.append({"key": list(k), "missing": "from" if ra is None else "to"}); continue
    for f in ("id", "input_sha256", "bound", "unbound", "transport"):
        if ra.get(f) != rb.get(f):
            changes.append({"key": list(k), "id": ra.get("id"), "field": f, "from": ra.get(f), "to": rb.get(f)})
out = {"from_entries": len(a), "to_entries": len(b), "changes": changes}
json.dump(out, open(sys.argv[3], "w"), indent=1)
print(json.dumps({"from_entries": len(a), "to_entries": len(b), "changes": len(changes)}))
