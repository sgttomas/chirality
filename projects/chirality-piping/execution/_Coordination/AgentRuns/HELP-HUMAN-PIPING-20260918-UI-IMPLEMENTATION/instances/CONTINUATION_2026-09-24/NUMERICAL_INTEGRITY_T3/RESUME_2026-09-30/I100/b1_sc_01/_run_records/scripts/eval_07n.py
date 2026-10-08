"""I100 B1 SC: each reader's pass/fail on a corpus, from its census lines (RV113's harnesses).

Usage: eval_07n.py <corpus.json> <out.json> python=<py.jsonl> rust=<rs.jsonl> typescript=<ts.jsonl>

Per reader, every check the corpus states:
- a base: bound admitted with its `expected` eligibility and as many classifications as `expected_classifications`;
  unbound admitted, not eligible; transport admitted;
- a mutation: bound refused with `expected_by_reader[reader]`, else `expected` (gate and code);
- a must-pass entry: bound admitted with `expected_eligibility`;
- where stated, `expected_unbound` and `expected_transport` ("pass": admitted, not eligible; else gate and code).
Misses are listed, split into 07m's entries (the census) and 07n's.
"""
import json
import sys

corpus = json.load(open(sys.argv[1]))
out = sys.argv[2]
runs = {}
for a in sys.argv[3:]:
    k, p = a.split("=", 1)
    runs[k] = {(r["set"], r["i"]): r for r in (json.loads(l) for l in open(p) if l.strip())}


def admitted(v, eligible=False, bound=False, classes=None):
    if not v or "ok" not in v:
        return False
    ok = v["ok"]
    return ok["numerical_eligible"] == eligible and ok["invocation_bound"] == bound and (classes is None or ok["classifications"] == classes)


def refused(v, want):
    return bool(v) and "err" in v and v["err"]["gate"] == want["gate"] and v["err"]["code"] == want["code"]


def stated(v, want):
    return admitted(v) if want == "pass" else refused(v, want)


res = {}
for reader, lines in runs.items():
    checks, misses = 0, []

    def check(ok, where, kind, what, got):
        global_checks[0] += 1
        if not ok:
            misses.append({"where": where, "kind": kind, "check": what, "got": got})
    global_checks = [0]
    for i, c in enumerate(corpus["cases"]):
        r = lines[("base", i)]
        assert r["id"] == c["id"]
        where = "07m" if i < 17 else "07n"
        check(admitted(r["bound"], c["expected"]["numerical_eligible"], True, len(c["expected_classifications"])), where, "base", (c["id"], "bound"), r["bound"])
        full = (r["bound"].get("ok") or {}).get("classifications_full")
        if full is not None:
            check(full == c["expected_classifications"], where, "base", (c["id"], "classifications"), len(full))
        check(admitted(r["unbound"]), where, "base", (c["id"], "unbound"), r["unbound"])
        check(admitted(r["transport"]), where, "base", (c["id"], "transport"), r["transport"])
    for kind, n0 in (("mutations", 294), ("must_pass", 28)):
        for i, e in enumerate(corpus[kind]):
            r = lines[("mutation" if kind == "mutations" else "must_pass", i)]
            assert r["id"] == e["id"], (reader, kind, i)
            where = "07m" if i < n0 else "07n"
            if kind == "mutations":
                want = e.get("expected_by_reader", {}).get(reader, e["expected"])
                check(refused(r["bound"], want), where, kind, (e["id"], "bound"), r["bound"])
            else:
                el = e["expected_eligibility"]
                check(admitted(r["bound"], el["numerical_eligible"], el["invocation_bound"]), where, kind, (e["id"], "bound"), r["bound"])
                full = (r["bound"].get("ok") or {}).get("classifications_full")
                want = e.get("expected_classifications") or next(c for c in corpus["cases"] if c["id"] == e["base"])["expected_classifications"]
                if full is not None:
                    check(full == want, where, kind, (e["id"], "classifications"), len(full))
            for x in ("unbound", "transport"):
                if f"expected_{x}" in e:
                    check(stated(r[x], e[f"expected_{x}"]), where, kind, (e["id"], x), r[x])
            if "expected_unbound_by_reader" in e:
                check(refused(r["unbound"], e["expected_unbound_by_reader"][reader]), where, kind, (e["id"], "unbound by reader"), r["unbound"])
    res[reader] = {"checks": global_checks[0], "misses": len(misses), "misses_07m": sum(m["where"] == "07m" for m in misses),
                   "misses_07n": sum(m["where"] == "07n" for m in misses), "rows": misses}
json.dump(res, open(out, "w"), indent=1, default=str)
print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk != "rows"} for k, v in res.items()}))
