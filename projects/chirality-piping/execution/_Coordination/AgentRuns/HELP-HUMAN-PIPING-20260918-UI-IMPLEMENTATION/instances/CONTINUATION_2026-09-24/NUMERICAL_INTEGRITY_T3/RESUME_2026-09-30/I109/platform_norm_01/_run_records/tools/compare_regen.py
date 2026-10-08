#!/usr/bin/env python3
"""I109: compare regen_all.sh outputs, base against candidate, envelope by envelope.

For every (fixture, mode): identical bytes, or the number of changed numbers with their ulp
histogram and the changed rows (by result id and kind when the path is a result row). Also
compares each candidate envelope with a committed raw fixture of the same name when one exists.
Usage: compare_regen.py <base dir> <cand dir> <P root of a tree> <out.json>
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import json_ulps  # noqa: E402

base, cand, proot, out = sys.argv[1:5]
runs = [l.split(maxsplit=2) for l in open(os.path.join(cand, "runs.txt")).read().splitlines()]
report = {"runs": 0, "identical": 0, "differ": [], "errors": [], "committed": []}
for rc, mode, path in runs:
    name = path.replace("/", "_") + "." + mode + ".json"
    a, b = os.path.join(base, name), os.path.join(cand, name)
    report["runs"] += 1
    if rc != "0":
        ea = open(a.replace(".json", ".err")).read().strip() if os.path.exists(a.replace(".json", ".err")) else ""
        eb = open(b.replace(".json", ".err")).read().strip()
        report["errors"].append({"fixture": path, "mode": mode, "rc": rc, "base_err": ea[:200], "cand_err": eb[:200]})
        continue
    if open(a, "rb").read() == open(b, "rb").read():
        report["identical"] += 1
        continue
    r = json_ulps.compare(a, b)
    doc = json.load(open(b))
    rows = {}
    for p, x, y, u in r["number_paths"]:
        if p.startswith("/results["):
            i = int(p[len("/results["):p.index("]")])
            row = doc["results"][i]
            rows.setdefault(row.get("kind"), []).append({"id": row.get("id"), "field": p.split("]", 1)[1], "base": x, "cand": y, "ulps": u})
        else:
            rows.setdefault("(not a result row) " + p, []).append({"base": x, "cand": y, "ulps": u})
    report["differ"].append({"fixture": path, "mode": mode, "numbers_changed": r["numbers_changed"], "ulps": r["ulps_histogram"],
                             "strings_changed": r["strings_changed"], "string_paths": r["string_paths"][:10], "rows": rows})
# committed raw fixtures named after a request: <stem>-<mode>.raw.json beside it
for rc, mode, path in runs:
    if rc != "0" or not path.endswith(".request.json"):
        continue
    raw = os.path.join(proot, path[: -len(".request.json")] + f"-{mode}.raw.json")
    if os.path.exists(raw):
        b = os.path.join(cand, path.replace("/", "_") + "." + mode + ".json")
        a_b = open(os.path.join(base, path.replace("/", "_") + "." + mode + ".json"), "rb").read()
        report["committed"].append({"fixture": os.path.relpath(raw, proot), "cand_equal": open(raw, "rb").read() == open(b, "rb").read(),
                                    "base_equal": open(raw, "rb").read() == a_b})
json.dump(report, open(out, "w"), indent=1)
print(json.dumps({"runs": report["runs"], "identical": report["identical"], "differ": len(report["differ"]), "errors": len(report["errors"]),
                  "committed": report["committed"]}, indent=1))
