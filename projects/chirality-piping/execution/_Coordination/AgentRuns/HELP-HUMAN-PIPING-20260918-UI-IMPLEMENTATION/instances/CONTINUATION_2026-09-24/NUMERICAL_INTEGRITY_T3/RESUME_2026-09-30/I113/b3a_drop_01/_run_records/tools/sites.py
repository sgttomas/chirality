"""I113: I110's 34 `b3a` inventory sites, located at the start head and at the candidate by their recorded text (the
inventory's lines are at the pre-merge lane heads). Usage: sites.py <inventory.json> <base P root> <cand P root> <out.json>"""
import json, sys
inv, base, cand, out = sys.argv[1:5]
pre = {"PP/": "core/product_physics/", "RE/": "core/reporting/result_export/", "P/": ""}
def where(root, rel, text):
    try:
        lines = open(f"{root}/{rel}", encoding="utf-8").read().split("\n")
    except FileNotFoundError:
        return []
    return [i + 1 for i, l in enumerate(lines) if text in l]
rows = []
for s in json.load(open(inv))["sites"]:
    if s.get("kind") != "b3a":
        continue
    path, line = s["site"].rsplit(":", 1)
    rel = next(v + path[len(k):] for k, v in pre.items() if path.startswith(k))
    text = s["symbol"].strip()
    rows.append({"site": s["site"], "branch": s["branch"], "symbol": s["symbol"], "base_lines": where(base, rel, text), "candidate_lines": where(cand, rel, text)})
json.dump(rows, open(out, "w"), indent=1, ensure_ascii=False)
for r in rows:
    print(r["site"], "base", r["base_lines"], "cand", r["candidate_lines"])
