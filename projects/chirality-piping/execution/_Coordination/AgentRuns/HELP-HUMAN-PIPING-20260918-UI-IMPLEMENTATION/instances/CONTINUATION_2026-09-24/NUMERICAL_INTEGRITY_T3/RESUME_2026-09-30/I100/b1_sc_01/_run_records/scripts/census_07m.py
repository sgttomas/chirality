"""I100 B1 SC: the 07m census at the SC head against I4', reader by reader.

Usage: census_07m.py <out.json> <reader>=<i4p.jsonl>,<sc.jsonl> ...
07m's 339 entries keep their positions in 07n (cases 0-16, mutations 0-293, must-pass 0-27). For each reader, every
07m line at the SC head is compared with its line at I4' (07m in place): all three verdicts in full (detail
included; the classification counts and hashes too) and the materialized input's sha256.
"""
import json
import sys

out = sys.argv[1]
res = {}
for arg in sys.argv[2:]:
    reader, paths = arg.split("=", 1)
    a, b = paths.split(",")
    base = {(r["set"], r["i"]): r for r in (json.loads(l) for l in open(a) if l.strip())}
    head = {(r["set"], r["i"]): r for r in (json.loads(l) for l in open(b) if l.strip())}
    assert len(base) == 339
    changes = []
    for k, r in base.items():
        h = head[k]
        assert h["id"] == r["id"], k
        for x in ("input_sha256", "bound", "unbound", "transport"):
            hv, rv = h.get(x), r.get(x)
            if isinstance(hv, dict) and "ok" in hv:
                hv = {"ok": {kk: vv for kk, vv in hv["ok"].items() if kk != "classifications_full"}}
            if hv != rv:
                changes.append({"key": list(k), "id": r["id"], "field": x, "i4p": rv, "sc": hv})
    res[reader] = {"entries": len(base), "changes": changes}
json.dump(res, open(out, "w"), indent=1)
print(json.dumps({k: {"entries": v["entries"], "changes": len(v["changes"])} for k, v in res.items()}))
