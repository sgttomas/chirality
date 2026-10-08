"""RV113 (RV-R): comparisons for SR-RS repair 02.

census <corpus> <before.jsonl> <after.jsonl> <out.json>
    RS before (cc81e78801/b5cb7faaeb: identical src) against RS after (6e3e4fe219), entry by entry, every verdict
    (bound, unbound, transport, standing); and each entry's bound verdict against the corpus's Rust expectation.
probes <probes_all.json> <rs_after.jsonl> <rs_before_v5.jsonl> <rs_before_fg.jsonl> <rs_before_rp.jsonl> <out.json>
    r2 probes: RS after against this reviewer's per-verdict expectation (`want`).
    v5/fg/rp probes: RS after against RS before, every verdict; each change listed.
cross <probes_all.json> <out.json> <label=jsonl> ...
    Any readers' outputs on the same probes, side by side (r2's T and C sections, and the fg/rp sets).
"""
import json
import sys

STANDING = {"numerically_eligible": "eligible"}


def load(path):
    return {json.loads(l)["id"]: json.loads(l) for l in open(path) if l.strip()}


def loadl(path):
    return [json.loads(l) for l in open(path) if l.strip()]


def short(v):
    if v is None:
        return None
    if "ok" in v:
        return {"admitted": v["ok"]["numerical_eligible"]}
    if "err" in v:
        return {"gate": v["err"]["gate"], "code": v["err"]["code"]}
    return {"escape": str(v)[:200]}


def census(corpus, bp, ap, out):
    d = json.load(open(corpus))
    b, a = loadl(bp), loadl(ap)
    assert len(a) == len(b) == len(d["cases"]) + len(d["mutations"]) + len(d["must_pass"])
    changes, misses = [], []
    for x, y in zip(b, a):
        assert (x["set"], x["i"], x["id"]) == (y["set"], y["i"], y["id"])
        if x["input_sha256"] != y["input_sha256"]:
            changes.append({"id": x["id"], "input": "differs"})
        for k in ("bound", "unbound", "transport", "standing"):
            if x.get(k) != y.get(k):
                changes.append({"id": x["id"], "verdict": k, "before": x.get(k), "after": y.get(k)})
        if y["set"] == "mutation":
            m = d["mutations"][y["i"]]
            want = m.get("expected_by_reader", {}).get("rust", m["expected"])
            if short(y["bound"]) != {"gate": want["gate"], "code": want["code"]}:
                misses.append({"id": y["id"], "want": want, "got": short(y["bound"])})
        elif y["set"] == "must_pass":
            el = d["must_pass"][y["i"]]["expected_eligibility"]
            ok = y["bound"].get("ok")
            if not (ok and ok["invocation_bound"] == el["invocation_bound"] and ok["numerical_eligible"] == el["numerical_eligible"]
                    and STANDING.get(y["standing"], y["standing"]) == el["standing"]):
                misses.append({"id": y["id"], "want": el, "got": [y["bound"], y["standing"]]})
        else:
            c = d["cases"][y["i"]]
            ok = y["bound"].get("ok")
            if ok is None or ok["numerical_eligible"] != c["expected"]["numerical_eligible"]:
                misses.append({"id": y["id"], "want": c["expected"], "got": y["bound"]})
    res = {"entries": len(a), "changes": changes, "rust_expectation_misses": misses}
    json.dump(res, open(out, "w"), indent=1)
    print(json.dumps({"entries": len(a), "changes": len(changes), "misses": len(misses)}))


def probes(pp, ap, b5, bfg, brp, out):
    ps = json.load(open(pp))
    after = load(ap)
    before = {"v5": load(b5), "fg": {"fg:" + k: v for k, v in load(bfg).items()}, "rp": {"rp:" + k: v for k, v in load(brp).items()}}
    rows, bad, changed = [], 0, []
    for p in ps:
        y = after[p["id"]]
        if "materialize_error" in y:
            rows.append({"id": p["id"], "materialize_error": y["materialize_error"]}); bad += 1; continue
        if p["set_name"] == "r2":
            r = {"id": p["id"], "item": p["item"], "note": p.get("note", "")}
            for k in ("bound", "unbound", "transport"):
                want = p["want"][k]
                got = short(y[k])
                ok = "observe" in want or got == want
                r[k] = {"want": want, "got": got, "ok": ok}
                bad += not ok
            rows.append(r)
        else:
            x = before[p["set_name"]][p["id"]]
            for k in ("bound", "unbound", "transport"):
                if short(x.get(k)) != short(y.get(k)):
                    changed.append({"id": p["id"], "verdict": k, "before": short(x.get(k)), "after": short(y.get(k))})
    res = {"r2_rows": rows, "r2_mismatches": bad, "earlier_sets_changed": changed}
    json.dump(res, open(out, "w"), indent=1)
    for r in rows:
        for k in ("bound", "unbound", "transport"):
            if k in r and not r[k]["ok"]:
                print("MISMATCH", r["id"], k, "want", r[k]["want"], "got", r[k]["got"])
    for c in changed:
        print("CHANGED", c["id"], c["verdict"], c["before"], "->", c["after"])
    print(json.dumps({"r2": len(rows), "r2_mismatches": bad, "earlier_changed": len(changed)}))


def cross(pp, out, *pairs):
    ps = json.load(open(pp))
    runs = {}
    for pair in pairs:
        lab, path = pair.split("=", 1)
        runs[lab] = load(path)
    rows = []
    for p in ps:
        r = {"id": p["id"], "set": p["set_name"], "item": p["item"]}
        for lab, data in runs.items():
            y = data.get(p["id"])
            r[lab] = None if y is None else ({"materialize_error": y["materialize_error"]} if "materialize_error" in y else
                                             {k: short(y.get(k)) for k in ("bound", "unbound", "transport")})
        rows.append(r)
    json.dump(rows, open(out, "w"), indent=1)
    print(len(rows), "rows")


if __name__ == "__main__":
    {"census": census, "probes": probes, "cross": cross}[sys.argv[1]](*sys.argv[2:])
