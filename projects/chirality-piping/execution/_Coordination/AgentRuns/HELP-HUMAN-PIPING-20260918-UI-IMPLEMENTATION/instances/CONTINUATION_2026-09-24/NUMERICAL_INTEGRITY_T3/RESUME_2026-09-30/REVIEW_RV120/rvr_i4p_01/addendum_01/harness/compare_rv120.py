"""RV120 (RV-R) comparisons for the round toward I4'.

census <corpus> <reader rust|typescript|python> <i4.jsonl> <head.jsonl> <out.json>
    One reader at I4 against its head, entry by entry: every verdict (bound, unbound, transport; standing where the
    harness records it), in full (gate, code and detail; or the admission); and each side's bound verdict against the
    corpus's own expectation for that reader (expected_by_reader.<reader>, else expected; must-pass eligibilities and
    standings; bases).
probes <probes.json> <i4.jsonl> <head.jsonl> <out.json>
    One reader at I4 against its head, probe by probe, every verdict in full; and the head against each probe's stated
    transport/bound/unbound `want` (non-observe).
cross <out.json> <label=jsonl> ...
    Pairwise differences of the short verdicts ({admitted} or {gate, code}) by probe or census id.
The short verdict: {"admitted": numerical_eligible} for an admission, {"gate", "code"} for a refusal.
"""
import itertools
import json
import sys

E = ("bound", "unbound", "transport")


def load(path):
    return [json.loads(l) for l in open(path) if l.strip()]


def short(v):
    if v is None:
        return None
    if "ok" in v:
        return {"admitted": v["ok"]["numerical_eligible"]}
    if "err" in v:
        return {"gate": v["err"]["gate"], "code": v["err"]["code"]}
    return {"escape": str(v)[:200]}


def standing_of(line):
    if "standing" in line:
        return line["standing"]
    ok = line["bound"].get("ok") if isinstance(line.get("bound"), dict) else None
    return ok.get("standing") if ok else None


def census(corpus, reader, ip, hp, out):
    d = json.load(open(corpus))
    a, b = load(ip), load(hp)
    n = len(d["cases"]) + len(d["mutations"]) + len(d["must_pass"])
    assert len(a) == len(b) == n, (len(a), len(b), n)
    changes, details, inputs, misses = [], [], [], {"i4": [], "head": []}
    norm = {"numerically_eligible": "eligible"}
    for x, y in zip(a, b):
        assert (x["set"], x["i"], x["id"]) == (y["set"], y["i"], y["id"])
        if x.get("input_sha256") != y.get("input_sha256"):
            inputs.append(x["id"])
        for k in E + ("standing",):
            if k not in x and k not in y:
                continue
            if x.get(k) != y.get(k):
                if k in E and short(x[k]) == short(y[k]):
                    details.append({"set": x["set"], "id": x["id"], "verdict": k, "i4": x[k], "head": y[k]})
                else:
                    changes.append({"set": x["set"], "id": x["id"], "verdict": k, "i4": x.get(k), "head": y.get(k)})
        for lab, line in (("i4", x), ("head", y)):
            if line["set"] == "mutation":
                m = d["mutations"][line["i"]]
                want = m.get("expected_by_reader", {}).get(reader, m["expected"])
                if short(line["bound"]) != {"gate": want["gate"], "code": want["code"]}:
                    misses[lab].append({"id": line["id"], "want": want, "got": short(line["bound"])})
            elif line["set"] == "must_pass":
                el = d["must_pass"][line["i"]]["expected_eligibility"]
                ok = line["bound"].get("ok")
                st = standing_of(line)
                if not (ok and ok["invocation_bound"] == el["invocation_bound"] and ok["numerical_eligible"] == el["numerical_eligible"]
                        and norm.get(st, st) == el["standing"]):
                    misses[lab].append({"id": line["id"], "want": el, "got": [line["bound"], st]})
            else:
                c = d["cases"][line["i"]]
                ok = line["bound"].get("ok")
                if not ok or ok["numerical_eligible"] != c["expected"]["numerical_eligible"]:
                    misses[lab].append({"id": line["id"], "want": c["expected"], "got": line["bound"]})
    res = {"entries": n, "inputs_differ": inputs, "verdict_changes": changes, "detail_only_changes": details,
           "expectation_misses": misses}
    json.dump(res, open(out, "w"), indent=1)
    print(json.dumps({"entries": n, "inputs_differ": len(inputs), "verdict_changes": len(changes), "detail_only_changes": len(details),
                      "misses_i4": len(misses["i4"]), "misses_head": len(misses["head"])}))


def probes(pp, ip, hp, out):
    P = json.load(open(pp))
    A = {r["id"]: r for r in load(ip)}
    B = {r["id"]: r for r in load(hp)}
    assert len(A) == len(B) == len(P), (len(A), len(B), len(P))
    changes, details, stated, misses = [], [], 0, []
    for p in P:
        x, y = A[p["id"]], B[p["id"]]
        if "materialize_error" in x or "materialize_error" in y:
            changes.append({"id": p["id"], "materialize_error": [x.get("materialize_error"), y.get("materialize_error")]})
            continue
        for k in E:
            if x[k] != y[k]:
                rec = {"id": p["id"], "verdict": k, "i4": x[k], "head": y[k]}
                (details if short(x[k]) == short(y[k]) else changes).append(rec)
        for k in E:
            w = (p.get("want") or {}).get(k)
            if not w or w.get("observe"):
                continue
            stated += 1
            got = short(y[k])
            ok = got == w if "gate" in w else ("gate" not in got and (w.get("admitted") is None or got.get("admitted") == w["admitted"]))
            if not ok:
                misses.append({"id": p["id"], "verdict": k, "want": w, "got": got})
    res = {"probes": len(P), "verdict_changes": changes, "detail_only_changes": details, "stated": stated, "misses_head": misses}
    json.dump(res, open(out, "w"), indent=1)
    print(json.dumps({"probes": len(P), "verdict_changes": len(changes), "detail_only_changes": len(details), "stated": stated,
                      "misses_head": len(misses)}))


def cross(out, *pairs):
    R = {}
    for pr in pairs:
        label, path = pr.split("=", 1)
        R[label] = {r["id"] if r.get("set") == "probe" else f'{r["set"]}:{r["i"]}:{r["id"]}': r for r in load(path)}
    res = {}
    for a, b in itertools.combinations(R, 2):
        ids = [i for i in R[a] if i in R[b]]
        rows = []
        for i in ids:
            for e in E:
                sa, sb = short(R[a][i].get(e)), short(R[b][i].get(e))
                if sa != sb:
                    rows.append({"id": i, "verdict": e, a: sa, b: sb})
        res[f"{a}~{b}"] = {"common": len(ids), "differences": len(rows), "by_verdict": {e: sum(1 for r in rows if r["verdict"] == e) for e in E},
                           "rows": rows}
        print(f"{a}~{b}", len(ids), res[f"{a}~{b}"]["by_verdict"])
    json.dump(res, open(out, "w"), indent=1)


if __name__ == "__main__":
    {"census": census, "probes": probes, "cross": cross}[sys.argv[1]](*sys.argv[2:])
