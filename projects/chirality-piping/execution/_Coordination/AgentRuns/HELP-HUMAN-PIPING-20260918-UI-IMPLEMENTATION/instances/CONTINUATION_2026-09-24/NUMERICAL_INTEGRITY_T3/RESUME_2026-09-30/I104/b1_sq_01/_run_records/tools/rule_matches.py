"""I104 SQ G5: for every I104 loop rule (new, first, rebound, kept), the loop headers it bounds in a run's loop
log (the TEXT multiplicity contexts), so that a reviewer can see each rule reaches only its intended loops.
Usage: rule_matches.py <chain loop_bounds json> <looplog json> > out.json"""
import json, re, sys, collections
LB = json.load(open(sys.argv[1])); log = json.load(open(sys.argv[2]))
rules = [(i, re.compile(r["re"]), r) for i, r in enumerate(LB["loops"]) if r["why"].startswith("I104 SQ")]
first = {}
for ctx, h, expr, val in log:
    if h in first: first[h]["contexts"].add(ctx); continue
    for i, rx, r in [(j, re.compile(x["re"]), x) for j, x in enumerate(LB["loops"])]:
        if rx.search(h):
            first[h] = {"rule": i, "contexts": {ctx}}; break
    else:
        first[h] = {"rule": None, "contexts": {ctx}}
out = []
for i, rx, r in rules:
    hs = {h: sorted(v["contexts"])[:8] for h, v in first.items() if v["rule"] == i}
    out.append({"rule": i, "bound": r["bound"], "re": r["re"][:200], "why": r["why"][:160], "headers": hs,
                "files": sorted({c.split(" ")[1].split(":")[0] for v in hs.values() for c in v})})
json.dump(out, sys.stdout, indent=1)
