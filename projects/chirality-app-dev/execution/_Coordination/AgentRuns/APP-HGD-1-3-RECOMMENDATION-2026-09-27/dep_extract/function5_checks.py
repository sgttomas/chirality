#!/usr/bin/env python3
"""dependency-extract Function 5 checks for the DEL-02-01 HGD/FC ruling application (read-only).

Run from the repository root after apply_hgd_ruling.py. Writes FUNCTION5_CHECKS.json next to this script.
"""
import collections, csv, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = json.load(open(os.path.join(HERE, "EXTRACTION_LOG.json"), encoding="utf-8"))
ENUMS = {"DependencyClass": "DEPENDENCY_CLASS", "AnchorType": "ANCHOR_TYPE", "Direction": "DIRECTION",
         "DependencyType": "DEPENDENCY_TYPE", "TargetType": "TARGET_TYPE", "Explicitness": "EXPLICITNESS",
         "Confidence": "CONFIDENCE", "Origin": "ORIGIN", "Status": "STATUS", "SatisfactionStatus": "SATISFACTION_STATUS"}


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip().replace(os.getcwd() + "/", "")


folder = LOG["folder"]
p = folder + "/Dependencies.csv"
out = {}
rc, msg = run([sys.executable, "-B", "tools/validation/validate_dependencies_schema.py", p])
out["schema"] = {"rc": rc, "result": msg}
rows = list(csv.DictReader(open(p, encoding="utf-8")))
ids = [r["DependencyID"] for r in rows]
out["uniqueness"] = len(ids) == len(set(ids))
act = [r for r in rows if r["Status"] == "ACTIVE"]
out["parent_anchor_active_implements_node"] = sum(1 for r in act if r["AnchorType"] == "IMPLEMENTS_NODE")
bad = []
for kind, val in [("DEL", "DEL-02-01"), ("PKG", rows[0]["FromPackageID"]), ("DEL", "DEL-05-03"), ("DEL", "DEL-08-02")] + [("DEP", i) for i in ids]:
    rc, m = run(["bash", "tools/validation/validate_id_format.sh", kind, val])
    if rc != 0:
        bad.append(f"{kind} {val}: {m}")
out["id_format"] = {"checked": len(ids) + 4, "failures": bad}
changed = set(LOG["row_diffs"])
out["enum_pairs"] = {}
for e, v in sorted({(ENUMS[f], r[f]) for r in rows if r["DependencyID"] in changed for f in ENUMS}):
    rc, m = run([sys.executable, "-B", "tools/validation/validate_enum.py", e, v])
    out["enum_pairs"][f"{e}={v}"] = {"rc": rc, "result": m.splitlines()[-1] if m else ""}
md = open(folder + "/_DEPENDENCIES.md", encoding="utf-8").read()
m = re.search(r"\| ACTIVE rows \| (\d+) \|", md)
out["index_counts"] = {"index_active": int(m.group(1)), "csv_active": len(act), "match": int(m.group(1)) == len(act)}
compact = {l.split("|")[1].strip(): [c.strip() for c in l.split("|")[2:8]] for l in md.splitlines() if l.startswith("| DEP-02-01-")}
out["compact_register_matches_csv"] = all(
    compact.get(r["DependencyID"]) == [r["DependencyClass"], r["Direction"], r["DependencyType"],
                                       r["TargetDeliverableID"] or r["TargetRefID"] or compact.get(r["DependencyID"], [""] * 4)[3],
                                       r["Status"], r["SatisfactionStatus"]] for r in rows)
out["row_diffs_fields"] = {k: sorted(v) for k, v in LOG["row_diffs"].items()}
json.dump(out, open(os.path.join(HERE, "FUNCTION5_CHECKS.json"), "w", encoding="utf-8"), indent=1, sort_keys=True)
print("schema rc", out["schema"]["rc"], "| unique", out["uniqueness"], "| parents", out["parent_anchor_active_implements_node"],
      "| id failures", len(bad), "| enum rc", dict(collections.Counter(v["rc"] for v in out["enum_pairs"].values())),
      "| index match", out["index_counts"]["match"], "| compact match", out["compact_register_matches_csv"])
