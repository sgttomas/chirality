#!/usr/bin/env python3
"""I109: every committed JSON document with magnitude rows: are the published magnitudes the
correctly rounded 3-norms of their component rows? Documents are searched recursively for result
lists (envelopes, successors, corpus case sources). Usage: committed_magnitudes.py <P root> <list>"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import analyze_magnitudes as am
root, lst = sys.argv[1], sys.argv[2]
def docs(x, path=""):
    if isinstance(x, dict):
        if isinstance(x.get("results"), list) and x["results"] and isinstance(x["results"][0], dict) and "kind" in x["results"][0]:
            yield path, x
        for k, v in x.items():
            yield from docs(v, f"{path}/{k}")
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from docs(v, f"{path}[{i}]")
tot = {"files": 0, "documents": 0, "magnitudes": 0, "not_norm3": 0}
rows = []
for rel in open(lst).read().split():
    try:
        d = json.load(open(os.path.join(root, rel)))
    except Exception:
        continue
    tot["files"] += 1
    for path, doc in docs(d):
        r = am.analyse(doc)
        if not r["magnitudes"]:
            continue
        tot["documents"] += 1; tot["magnitudes"] += r["magnitudes"]
        nn = r["magnitudes"] - r["eq_norm3"]
        tot["not_norm3"] += nn
        if nn:
            rows.append({"file": rel, "path": path or "/", "magnitudes": r["magnitudes"], "not_norm3": nn,
                         "examples": [{"id": n["id"], "published": n["value"], "norm3": n["norm3"], "chain": n["chain"]} for n in r["neither"]][:5],
                         "eq_chain_not_norm3": r["eq_chain"] - r["eq_both"]})
print(json.dumps({"totals": tot, "documents_with_non_cr_magnitudes": rows}, indent=1))
