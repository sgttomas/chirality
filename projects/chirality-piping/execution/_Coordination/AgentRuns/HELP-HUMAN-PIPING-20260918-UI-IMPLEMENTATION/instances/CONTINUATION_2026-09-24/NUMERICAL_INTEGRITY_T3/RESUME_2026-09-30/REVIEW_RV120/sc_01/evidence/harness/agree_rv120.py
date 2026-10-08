"""RV120: reader agreement on the probes (or the census), with the declared raw class set aside.
Usage: python3 agree_rv120.py <out.json> <label=jsonl> ...
For each pair of labels and each probe/entry and verdict: equal short verdicts; or a raw (bound/unbound) difference
where both refuse at G7 with different codes (the declared per-reader raw G7 class: B1_SC item 13 as ruling 3 states
it); or any other difference, listed in full. Transport differences are always listed."""
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


def key(r):
    return r["id"] if r.get("set") in (None, "probe") else f'{r["set"]}:{r["i"]}:{r["id"]}'


out, *pairs = sys.argv[1:]
R = {}
for p in pairs:
    lab, path = p.split("=", 1)
    R[lab] = {key(json.loads(l)): json.loads(l) for l in open(path) if l.strip()}
res = {}
for a, b in itertools.combinations(R, 2):
    ids = [i for i in R[a] if i in R[b]]
    declared, other, equal = [], [], 0
    for i in ids:
        for e in E:
            sa, sb = short(R[a][i].get(e)), short(R[b][i].get(e))
            if sa == sb:
                equal += 1
            elif e != "transport" and sa and sb and sa.get("gate") == "G7" and sb.get("gate") == "G7":
                declared.append({"id": i, "verdict": e, a: sa["code"], b: sb["code"]})
            else:
                other.append({"id": i, "verdict": e, a: sa, b: sb})
    res[f"{a}~{b}"] = {"common": len(ids), "equal_verdicts": equal, "raw_g7_code_class": len(declared),
                       "raw_g7_code_class_probes": sorted({d["id"] for d in declared}), "other_differences": other}
    print(f"{a}~{b}: common {len(ids)}, equal {equal}, raw G7 code class {len(declared)} verdicts on {len({d['id'] for d in declared})}, other {len(other)}")
    for o in other:
        print("   ", json.dumps(o))
json.dump(res, open(out, "w"), indent=1)
