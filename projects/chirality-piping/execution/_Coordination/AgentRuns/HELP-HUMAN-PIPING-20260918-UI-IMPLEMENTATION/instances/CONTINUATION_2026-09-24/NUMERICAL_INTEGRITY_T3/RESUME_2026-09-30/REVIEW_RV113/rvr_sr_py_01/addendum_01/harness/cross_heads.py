"""RV113 (RV-R): side-by-side tables for the three readers' present heads (SR-TS repair 01, SR-PY repair 02).

probes <probes.json> <out.json> <label=jsonl> ...
    One row per probe (the probe file's order): id, set (the id's prefix, or v5), item, and each label's short verdict
    (bound, unbound, transport) or null when that run did not carry the probe.
census <out.json> <label=jsonl> ...
    07m entry by entry (matched by set, position and id; the harnesses hash inputs differently): every pair of labels'
    differences on bound, unbound and transport, with the short verdicts.
want <probes.json> <jsonl>
    Each stated (non-observe) per-verdict expectation of the probe file against one run: stated count and misses.
The short verdict: {"admitted": numerical_eligible} for an admission, {"gate", "code"} for a refusal.
"""
import itertools
import json
import sys

E = ("bound", "unbound", "transport")


def short(v):
    if v is None:
        return None
    if "ok" in v:
        return {"admitted": v["ok"]["numerical_eligible"]}
    if "err" in v:
        return {"gate": v["err"]["gate"], "code": v["err"]["code"]}
    return {"escape": str(v)[:200]}


def runs(pairs):
    out = {}
    for p in pairs:
        label, path = p.split("=", 1)
        out[label] = [json.loads(l) for l in open(path) if l.strip()]
    return out


def probes(pp, out, *pairs):
    P = json.load(open(pp))
    R = {k: {r["id"]: r for r in v} for k, v in runs(pairs).items()}
    rows = []
    for p in P:
        pid = p["id"]
        row = {"id": pid, "set": pid.split(":", 1)[0] if ":" in pid else "v5", "item": p.get("item")}
        for k, v in R.items():
            r = v.get(pid)
            row[k] = None if r is None else {e: short(r[e]) for e in E}
        rows.append(row)
    json.dump(rows, open(out, "w"), indent=1)
    print(len(rows), "rows")


def census(out, *pairs):
    R = runs(pairs)
    n = {len(v) for v in R.values()}
    assert len(n) == 1, n
    keys = {k: [(r["set"], r["i"], r["id"]) for r in v] for k, v in R.items()}
    first = next(iter(keys.values()))
    assert all(v == first for v in keys.values()), "entries differ in order or id"
    res = {"entries": len(first), "pairs": {}}
    for a, b in itertools.combinations(R, 2):
        d = []
        for ra, rb in zip(R[a], R[b]):
            for e in E:
                sa, sb = short(ra[e]), short(rb[e])
                if sa != sb:
                    d.append({"set": ra["set"], "i": ra["i"], "id": ra["id"], "verdict": e, a: sa, b: sb})
        res["pairs"][f"{a}~{b}"] = {"differences": len(d), "by_verdict": {e: sum(1 for x in d if x["verdict"] == e) for e in E}, "rows": d}
        print(f"{a}~{b}", res["pairs"][f"{a}~{b}"]["by_verdict"])
    json.dump(res, open(out, "w"), indent=1)


def want(pp, path):
    P = {p["id"]: p for p in json.load(open(pp))}
    stated = 0
    misses = []
    for l in open(path):
        if not l.strip():
            continue
        r = json.loads(l)
        w = P[r["id"]].get("want") or {}
        for e in E:
            we = w.get(e)
            if not we or we.get("observe"):
                continue
            stated += 1
            got = short(r[e])
            ok = got == we if "gate" in we else ("gate" not in got and (we.get("admitted") is None or got.get("admitted") == we["admitted"]))
            if not ok:
                misses.append({"id": r["id"], "verdict": e, "want": we, "got": got})
    print(json.dumps({"run": path.rsplit("/", 1)[-1], "stated": stated, "misses": misses}, indent=1))


if __name__ == "__main__":
    {"probes": probes, "census": census, "want": want}[sys.argv[1]](*sys.argv[2:])
