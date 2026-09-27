#!/usr/bin/env python3
"""dependency-extract Function 5 local quality checks over the in-scope registers (read-only).

Run from the repository root. Writes FUNCTION5_CHECKS.json next to this script.
"""
import collections, csv, glob, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = json.load(open(os.path.join(HERE, "EXTRACTION_LOG.json")))
ENUMS = {"DependencyClass": "DEPENDENCY_CLASS", "AnchorType": "ANCHOR_TYPE", "Direction": "DIRECTION",
         "DependencyType": "DEPENDENCY_TYPE", "TargetType": "TARGET_TYPE", "Explicitness": "EXPLICITNESS",
         "Confidence": "CONFIDENCE", "Origin": "ORIGIN", "Status": "STATUS", "SatisfactionStatus": "SATISFACTION_STATUS"}


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip().replace(os.getcwd() + "/", "")


out = {"schema": {}, "enum_pairs": {}, "id_format": {}, "uniqueness": {}, "parent_anchor": {}, "index_counts": {}}
pairs = set()
for d, info in LOG["deliverables"].items():
    p = info["folder"] + "/Dependencies.csv"
    rc, msg = run([sys.executable, "-B", "tools/validation/validate_dependencies_schema.py", p])
    out["schema"][d] = {"rc": rc, "result": msg.splitlines()[-1] if msg else ""}
    rows = list(csv.DictReader(open(p, encoding="utf-8")))
    ids = [r["DependencyID"] for r in rows]
    out["uniqueness"][d] = len(ids) == len(set(ids))
    act = [r for r in rows if r["Status"] == "ACTIVE"]
    out["parent_anchor"][d] = sum(1 for r in act if r["AnchorType"] == "IMPLEMENTS_NODE")
    bad = []
    for kind, val in [("DEL", d), ("PKG", rows[0]["FromPackageID"])] + [("DEP", i) for i in ids]:
        rc, msg = run(["bash", "tools/validation/validate_id_format.sh", kind, val])
        if rc != 0:
            bad.append(f"{kind} {val}: {msg}")
        if kind == "DEP" and not val.startswith(f"DEP-{d[4:6]}-{d[7:9]}-"):
            bad.append(f"prefix {val}")
    out["id_format"][d] = {"checked": len(ids) + 2, "failures": bad}
    changed = {k for k, v in info["actions"].items() if not v.startswith("RESEEN")}
    for r in rows:
        if r["DependencyID"] in changed:
            for f, e in ENUMS.items():
                pairs.add((e, r[f]))
    md = open(info["folder"] + "/_DEPENDENCIES.md", encoding="utf-8").read()
    m = re.search(r"\| ACTIVE rows \| (\d+) \|", md.split("## Extracted Dependency Register", 1)[1])
    out["index_counts"][d] = {"index_active": int(m.group(1)), "csv_active": len(act), "match": int(m.group(1)) == len(act)}
for e, v in sorted(pairs):
    rc, msg = run([sys.executable, "-B", "tools/validation/validate_enum.py", e, v])
    out["enum_pairs"][f"{e}={v}"] = {"rc": rc, "result": msg.splitlines()[-1] if msg else ""}
rc, msg = run([sys.executable, "-B", "tools/validation/validate_decomposition_registers.py", "projects/chirality-app-dev/execution",
               "--families", "EVQ,DRB", "--max-per-code", "100000"])
scope_ids = {i for info in LOG["deliverables"].values() for i in info["actions"]}
lines = msg.splitlines()
out["evq_drb"] = {"rc": rc, "codes": dict(collections.Counter(m.group(1) for m in (re.search(r"^\s*(?:ERROR|WARNING) (\S+) ", l) for l in lines) if m)),
                  "in_scope_changed_rows": [l for l in lines if any(i in l for i in scope_ids
                                                                    if not LOG["deliverables"][f"DEL-{i[4:6]}-{i[7:9]}"]["actions"][i].startswith("RESEEN"))]}
json.dump(out, open(os.path.join(HERE, "FUNCTION5_CHECKS.json"), "w"), indent=1)
print("schema rc", collections.Counter(v["rc"] for v in out["schema"].values()),
      "unique", all(out["uniqueness"].values()),
      "parents", collections.Counter(out["parent_anchor"].values()),
      "id failures", sum(len(v["failures"]) for v in out["id_format"].values()),
      "enum rc", collections.Counter(v["rc"] for v in out["enum_pairs"].values()),
      "index match", all(v["match"] for v in out["index_counts"].values()),
      "evq_drb rc", rc, "changed-row findings", len(out["evq_drb"]["in_scope_changed_rows"]))
