"""I100: RV113's probes, probe by probe (matched by id).

Usage: probe_cmp.py <probes.json> <out.json> <A=py.jsonl> <B=py.jsonl> [<label=other.jsonl> ...]
- A against B (two PY runs): every verdict compared in full (detail included);
- B (the PY run under test) against each other label on the short verdict, all three verdicts, with the probe's
  item and RV113's stated expectation ("want", where stated and not "observe").
A label whose run lacks a probe reads null for it.
"""
import gzip
import json
import sys

E = ("bound", "unbound", "transport")


def load(path):
    f = gzip.open(path, "rt") if path.endswith(".gz") else open(path)
    return {r["id"]: r for r in (json.loads(l) for l in f if l.strip())}


def short(v):
    if v is None:
        return None
    if "ok" in v:
        return {"admitted": v["ok"]["numerical_eligible"]}
    if "err" in v:
        return {"gate": v["err"]["gate"], "code": v["err"]["code"]}
    return {"escape": str(v)[:200]}


def met(want, got):
    if not want or want.get("observe"):
        return None
    return got == want if "gate" in want else ("gate" not in (got or {}) and (want.get("admitted") is None or got.get("admitted") == want["admitted"]))


def main():
    pp, out, *pairs = sys.argv[1:]
    P = json.load(open(pp))
    runs = {}
    for p in pairs:
        k, v = p.split("=", 1)
        runs[k] = load(v)
    labels = list(runs)
    a, b = labels[0], labels[1]
    res = {"probes": len(P), "labels": labels, "full_changes": [], "rows": [], "want_misses": {a: [], b: []}}
    for p in P:
        pid = p["id"]
        ra, rb = runs[a].get(pid), runs[b].get(pid)
        for e in E:
            if (ra or {}).get(e) != (rb or {}).get(e):
                res["full_changes"].append({"id": pid, "verdict": e, a: (ra or {}).get(e), b: (rb or {}).get(e)})
        row = {"id": pid, "item": p.get("item")}
        for k in labels:
            r = runs[k].get(pid)
            row[k] = None if r is None else {e: short(r.get(e)) for e in E}
        for e in E:
            w = (p.get("want") or {}).get(e)
            for k, r in ((a, ra), (b, rb)):
                m = met(w, short((r or {}).get(e)))
                if m is False:
                    res["want_misses"][k].append({"id": pid, "verdict": e, "want": w, "got": short((r or {}).get(e))})
        row["diff"] = {o: [e for e in E if row[o] is not None and row[b][e] != row[o][e]] for o in labels[2:]}
        res["rows"].append(row)
    json.dump(res, open(out, "w"), indent=1, sort_keys=True)
    summary = {"probes": len(P), f"{a}->{b} full changes": len(res["full_changes"]),
               "changed probes": len({x["id"] for x in res["full_changes"]}),
               "want_misses": {k: len(v) for k, v in res["want_misses"].items()}}
    for o in labels[2:]:
        carried = [r for r in res["rows"] if r[o] is not None]
        summary[f"{b}~{o}"] = {"carried": len(carried), "probes differing": sum(1 for r in carried if r["diff"][o]),
                               "by_verdict": {e: sum(1 for r in carried if e in r["diff"][o]) for e in E}}
    print(json.dumps(summary, indent=1))


main()
