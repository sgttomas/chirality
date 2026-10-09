"""I107 SB round 3 (U3): after g7_linemap_crates_rows3.py, drop each rule whose key names a line the commit deleted with
nothing in its place (the code it priced is gone). Only a dict entry keyed by such a key is dropped (context ".../key");
any other unmapped key (a replaced line, a value, an ambiguity) leaves the run stopped. Edits <rules dir>/*.json in place
and the line map's own summary; prints what it dropped. Exit 0 if every unmapped key was a deleted key and is dropped.
Usage: python3 prune_deleted.py <rules dir>"""
import json, os, sys
D = sys.argv[1]; out_p = os.path.join(D, "g7_linemap.out.json"); out = json.load(open(out_p)); s = out["summary"]
dropped, kept = [], []
for u in s["unmapped"]:
    ctx, key = u[0], u[1]; kind = u[3] if len(u) > 3 else None
    parts = ctx.split("/")
    if kind == "deleted" and len(parts) == 3 and parts[2] == "key":
        p = os.path.join(D, parts[0]); data = json.load(open(p))
        if parts[1] in data and key in data[parts[1]]:
            dropped.append({"file": parts[0], "family": parts[1], "key": key, "rule": data[parts[1]].pop(key)})
            json.dump(data, open(p, "w"), indent=1); continue
    kept.append(u)
s["unmapped_before_prune"] = s["unmapped"]; s["unmapped"] = kept; s["pruned_deleted"] = dropped
json.dump(out, open(out_p, "w"), indent=1)
print(json.dumps({"dropped": len(dropped), "still_unmapped": kept, "keys": [d["key"] for d in dropped]}))
sys.exit(0 if not kept else 4)
