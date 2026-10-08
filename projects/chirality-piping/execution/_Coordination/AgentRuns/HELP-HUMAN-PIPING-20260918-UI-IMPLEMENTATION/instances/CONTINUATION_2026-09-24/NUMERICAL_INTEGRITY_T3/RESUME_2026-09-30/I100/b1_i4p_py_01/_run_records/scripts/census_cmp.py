"""I100: the 07m census, entry by entry (matched by set, position and id).

Usage: census_cmp.py <corpus.json> <out.json> <A=py.jsonl> <B=py.jsonl> [<label=other.jsonl> ...]
- A against B (two PY runs, RV113's harness): every verdict (bound, unbound, transport) compared in full, detail
  included, and the materialized inputs' sha256;
- each PY run against the corpus's own expectation (as RV113's compare_py: the bound verdict; a mutation's
  expected_by_reader.python, else expected; a must-pass entry's expected_eligibility; a base's numerical_eligible);
- each PY run against every other label (RS, TS) on the short verdict ({gate, code} or {admitted}), all three verdicts.
Escapes from the reader are counted.
"""
import gzip
import json
import sys

E = ("bound", "unbound", "transport")


def load(path):
    f = gzip.open(path, "rt") if path.endswith(".gz") else open(path)
    return [json.loads(l) for l in f if l.strip()]


def short(v):
    if v is None:
        return None
    if "ok" in v:
        return {"admitted": v["ok"]["numerical_eligible"]}
    if "err" in v:
        return {"gate": v["err"]["gate"], "code": v["err"]["code"]}
    return {"escape": str(v)[:200]}


def misses(d, run):
    out = []
    for line in run:
        if line["set"] == "mutation":
            m = d["mutations"][line["i"]]
            want = m.get("expected_by_reader", {}).get("python", m["expected"])
            if short(line["bound"]) != {"gate": want["gate"], "code": want["code"]}:
                out.append({"id": line["id"], "want": want, "got": short(line["bound"])})
        elif line["set"] == "must_pass":
            el = d["must_pass"][line["i"]]["expected_eligibility"]
            ok = line["bound"].get("ok")
            if not (ok and ok["invocation_bound"] == el["invocation_bound"] and ok["numerical_eligible"] == el["numerical_eligible"] and ok["standing"] == el["standing"]):
                out.append({"id": line["id"], "want": el, "got": line["bound"]})
        else:
            c = d["cases"][line["i"]]
            ok = line["bound"].get("ok")
            if ok is None or ok["numerical_eligible"] != c["expected"]["numerical_eligible"]:
                out.append({"id": line["id"], "want": c["expected"], "got": line["bound"]})
    return out


def main():
    corpus, out, *pairs = sys.argv[1:]
    d = json.load(open(corpus))
    runs = {}
    for p in pairs:
        k, v = p.split("=", 1)
        runs[k] = load(v)
    labels = list(runs)
    a, b = labels[0], labels[1]
    n = len(d["cases"]) + len(d["mutations"]) + len(d["must_pass"])
    keys = {k: [(r["set"], r["i"], r["id"]) for r in v] for k, v in runs.items()}
    for k, v in keys.items():
        assert len(v) == n and v == keys[a], (k, len(v), n)
    res = {"entries": n, "labels": labels, "full_changes": [], "inputs_differ": [], "misses": {}, "escapes": {}, "short_vs": {}}
    for ra, rb in zip(runs[a], runs[b]):
        if ra.get("input_sha256") != rb.get("input_sha256"):
            res["inputs_differ"].append(ra["id"])
        for e in E:
            if ra[e] != rb[e]:
                res["full_changes"].append({"set": ra["set"], "i": ra["i"], "id": ra["id"], "verdict": e, a: ra[e], b: rb[e]})
    for k in (a, b):
        res["misses"][k] = misses(d, runs[k])
        res["escapes"][k] = [{"id": r["id"], "verdict": e} for r in runs[k] for e in E if "escape" in r[e]]
        for o in labels[2:]:
            rows = []
            for rk, ro in zip(runs[k], runs[o]):
                for e in E:
                    if short(rk[e]) != short(ro[e]):
                        rows.append({"set": rk["set"], "i": rk["i"], "id": rk["id"], "verdict": e, k: short(rk[e]), o: short(ro[e])})
            res["short_vs"][f"{k}~{o}"] = {"differences": len(rows), "by_verdict": {e: sum(1 for x in rows if x["verdict"] == e) for e in E}, "rows": rows}
    json.dump(res, open(out, "w"), indent=1, sort_keys=True)
    summary = {"entries": n, f"{a}->{b} full changes": len(res["full_changes"]), "inputs_differ": len(res["inputs_differ"]),
               "misses": {k: len(v) for k, v in res["misses"].items()}, "escapes": {k: len(v) for k, v in res["escapes"].items()},
               "short_vs": {k: v["by_verdict"] for k, v in res["short_vs"].items()}}
    print(json.dumps(summary, indent=1))


main()
