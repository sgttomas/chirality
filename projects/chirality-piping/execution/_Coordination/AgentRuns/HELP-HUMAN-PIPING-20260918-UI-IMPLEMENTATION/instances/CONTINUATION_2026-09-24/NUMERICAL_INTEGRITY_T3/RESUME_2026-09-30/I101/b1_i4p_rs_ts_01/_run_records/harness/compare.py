"""I101 (B1 I4' RS/TS): comparisons of RV113-harness outputs (JSON lines; .gz accepted).

census <corpus> <reader rust|typescript> <before.jsonl> <after.jsonl> <out.json>
    Entry by entry (bases, mutations, must-pass): the input digest and every verdict in full (bound, unbound,
    transport; and standing for Rust), before against after. Each side against the corpus's own expectation for
    the reader (mutations: expected_by_reader.<reader>, else expected, on the bound gate and code; must-pass:
    expected_eligibility with its standing; bases: expected numerical_eligible).
probes <probes.json> <before.jsonl> <after.jsonl> <out.json>
    Probe by probe: every verdict in full, before against after; each change listed (short form and detail).
cross <probes.json> <out.json> <label=jsonl> ...
    Readers side by side on the same probes, short verdicts per entry point, with the transport details.
"""
import gzip
import json
import sys

STANDING = {"numerically_eligible": "eligible"}


def loadl(path):
    op = gzip.open if path.endswith(".gz") else open
    return [json.loads(l) for l in op(path, "rt") if l.strip()]


def short(v):
    if v is None:
        return None
    if "ok" in v:
        return {"admitted": v["ok"]["numerical_eligible"]}
    if "err" in v:
        return {"gate": v["err"]["gate"], "code": v["err"]["code"]}
    return {"escape": str(v)[:200]}


def detail(v):
    return v.get("err", {}).get("detail") if isinstance(v, dict) else None


def misses_of(d, reader, y):
    if "materialize_error" in y:
        return {"id": y["id"], "materialize_error": y["materialize_error"]}
    if y["set"] == "mutation":
        m = d["mutations"][y["i"]]
        want = m.get("expected_by_reader", {}).get(reader, m["expected"])
        if short(y["bound"]) != {"gate": want["gate"], "code": want["code"]}:
            return {"id": y["id"], "want": want, "got": short(y["bound"])}
    elif y["set"] == "must_pass":
        el = d["must_pass"][y["i"]]["expected_eligibility"]
        ok = y["bound"].get("ok")
        standing = y.get("standing") if reader == "rust" else (ok or {}).get("standing")
        if not (ok and ok["invocation_bound"] == el["invocation_bound"] and ok["numerical_eligible"] == el["numerical_eligible"]
                and STANDING.get(standing, standing) == el["standing"]):
            return {"id": y["id"], "want": el, "got": [y["bound"], standing]}
    else:
        c = d["cases"][y["i"]]
        ok = y["bound"].get("ok")
        if ok is None or ok["numerical_eligible"] != c["expected"]["numerical_eligible"]:
            return {"id": y["id"], "want": c["expected"], "got": y["bound"]}
    return None


def census(corpus, reader, bp, ap, out):
    d = json.load(open(corpus))
    b, a = loadl(bp), loadl(ap)
    n = len(d["cases"]) + len(d["mutations"]) + len(d["must_pass"])
    assert len(a) == len(b) == n, (len(a), len(b), n)
    keys = ("bound", "unbound", "transport") + (("standing",) if reader == "rust" else ())
    changes, inputs, misses = [], [], {"before": [], "after": []}
    for x, y in zip(b, a):
        assert (x["set"], x["i"], x["id"]) == (y["set"], y["i"], y["id"])
        if x.get("input_sha256") != y.get("input_sha256"):
            inputs.append(x["id"])
        for k in keys:
            if x.get(k) != y.get(k):
                changes.append({"set": x["set"], "i": x["i"], "id": x["id"], "verdict": k, "before": x.get(k), "after": y.get(k)})
        for lab, line in (("before", x), ("after", y)):
            m = misses_of(d, reader, line)
            if m:
                misses[lab].append(m)
    res = {"reader": reader, "entries": n, "inputs_differ": inputs, "verdict_changes": changes, "expectation_misses": misses}
    json.dump(res, open(out, "w"), indent=1)
    print(json.dumps({"reader": reader, "entries": n, "inputs_differ": len(inputs), "verdict_changes": len(changes),
                      "misses_before": len(misses["before"]), "misses_after": len(misses["after"])}))
    for c in changes:
        print("  CHANGED", c["id"], c["verdict"], json.dumps(c["before"])[:160], "->", json.dumps(c["after"])[:160])


def probes(pp, bp, ap, out):
    ps = json.load(open(pp))
    b, a = loadl(bp), loadl(ap)
    assert len(a) == len(b) == len(ps)
    changes, full = [], 0
    for p, x, y in zip(ps, b, a):
        assert x["id"] == y["id"] == p["id"]
        for k in ("bound", "unbound", "transport"):
            if x.get(k) != y.get(k):
                full += 1
                changes.append({"id": p["id"], "verdict": k, "before": short(x.get(k)), "after": short(y.get(k)),
                                "before_detail": detail(x.get(k)), "after_detail": detail(y.get(k)),
                                "short_equal": short(x.get(k)) == short(y.get(k))})
    json.dump({"probes": len(ps), "verdict_changes": changes}, open(out, "w"), indent=1)
    print(json.dumps({"probes": len(ps), "verdict_changes": len(changes),
                      "short_changes": sum(1 for c in changes if not c["short_equal"])}))
    for c in changes:
        print("  CHANGED", c["id"], c["verdict"], c["before"], c["before_detail"], "->", c["after"], c["after_detail"])


def cross(pp, out, *pairs):
    ps = json.load(open(pp))
    runs = {}
    for pair in pairs:
        lab, path = pair.split("=", 1)
        runs[lab] = {l["id"]: l for l in loadl(path)}
    rows = []
    for p in ps:
        r = {"id": p["id"], "set": p.get("set_name"), "item": p.get("item")}
        for lab, data in runs.items():
            y = data.get(p["id"])
            if y is None or "materialize_error" in y:
                r[lab] = None if y is None else {"materialize_error": y["materialize_error"]}
            else:
                r[lab] = {k: short(y.get(k)) for k in ("bound", "unbound", "transport")}
                r[lab]["transport_detail"] = detail(y.get("transport"))
                r[lab]["bound_detail"] = detail(y.get("bound"))
        rows.append(r)
    json.dump(rows, open(out, "w"), indent=1)
    print(len(rows), "rows")


if __name__ == "__main__":
    {"census": census, "probes": probes, "cross": cross}[sys.argv[1]](*sys.argv[2:])
