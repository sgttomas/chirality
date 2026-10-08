"""I113: RV113's census at two heads, entry by entry. For each reader (rs, ts, py) and corpus (07m, 07n), the two runs
must list the same entries in the same order, and every record field must be equal (input digest; bound, unbound and
transport verdicts in full; RS's standing; anything else the harness writes). 0 changes is required.
Usage: census_cmp.py <base run dir> <candidate run dir> <out.json>"""
import json, sys
A, B, OUT = sys.argv[1:4]
load = lambda p: [json.loads(l) for l in open(p) if l.strip()]
res = {}
for corpus in ("07m", "07n"):
    for r in ("rs", "ts", "py"):
        a, b = load(f"{A}/c{corpus}_{r}.jsonl"), load(f"{B}/c{corpus}_{r}.jsonl")
        same_roster = [(x.get("set"), x.get("i"), x.get("id")) for x in a] == [(x.get("set"), x.get("i"), x.get("id")) for x in b]
        changes = [{"set": x.get("set"), "i": x.get("i"), "id": x.get("id"), "field": k, "base": x.get(k), "candidate": y.get(k)}
                   for x, y in zip(a, b) for k in sorted(set(x) | set(y)) if x.get(k) != y.get(k)]
        sets = {}
        for x in b:
            sets[x.get("set")] = sets.get(x.get("set"), 0) + 1
        res[f"{corpus}_{r}"] = {"base_entries": len(a), "candidate_entries": len(b), "same_roster": same_roster, "sets": sets,
                                "fields": sorted(b[0]) if b else [], "changes": changes}
        print(corpus, r, {"entries": (len(a), len(b)), "same_roster": same_roster, "sets": sets, "changes": len(changes)})
json.dump(res, open(OUT, "w"), indent=1)
