#!/usr/bin/env python3
import csv, hashlib, json, subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[8]
own = Path(__file__).resolve().parent
run = root / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
pref = run / "snapshots/W_P4/preflight"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

candidate = list(csv.DictReader((own / "CANDIDATE_HASHES_POST.tsv").open(), delimiter="\t"))
with (own / "CANDIDATE_MANIFEST_REPRODUCED.tsv").open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["sha256", "bytes", "path"], delimiter="\t", lineterminator="\n")
    w.writeheader()
    for row in candidate:
        w.writerow({"sha256": row["sha256"], "bytes": row["bytes"], "path": row["path"]})

live_rows = []
for row in csv.DictReader((pref / "EXPECTED_LIVE_BINDINGS.tsv").open(), delimiter="\t"):
    if row["package"] != "PKG-15":
        continue
    path = root / row["live_path"] / row["binding"]
    actual = sha(path) if path.is_file() else "MISSING"
    live_rows.append({**row, "actual_sha256": actual, "verdict": "PASS" if actual == row["sha256"] else "FAIL"})
with (own / "LIVE_BINDINGS_REPRODUCED.tsv").open("w", newline="") as f:
    fields = ["package", "deliverable_id", "live_path", "binding", "state", "sha256", "actual_sha256", "verdict"]
    w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
    w.writeheader(); w.writerows(live_rows)

methods = []
for row in csv.DictReader((pref / "METHOD_BINDINGS.tsv").open(), delimiter="\t"):
    path = root / row["surface"]
    actual = sha(path) if path.is_file() else "MISSING"
    methods.append({**row, "actual_sha256": actual, "verdict": "PASS" if actual == row["sha256"] else "FAIL"})
p4 = [r for r in csv.DictReader((pref / "P4_MANIFEST.tsv").open(), delimiter="\t") if r["package"] == "PKG-15"]
head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
audit = {
    "expected_head": "e8f59a63372f38d9e788ac39b39995558f5aba73",
    "head": head,
    "refs_head_match": head == "e8f59a63372f38d9e788ac39b39995558f5aba73",
    "live_bindings": len(live_rows),
    "live_bindings_passed": sum(r["verdict"] == "PASS" for r in live_rows),
    "method_bindings": len(methods),
    "method_bindings_passed": sum(r["verdict"] == "PASS" for r in methods),
    "method_rows": methods,
    "p4_manifest_members": len(p4),
    "p4_manifest_source_lines": sum(int(r["source_lines"]) for r in p4),
    "verdict": "PASS",
}
if not (audit["refs_head_match"] and audit["live_bindings_passed"] == 36 and audit["method_bindings_passed"] == 29 and audit["p4_manifest_members"] == 4 and audit["p4_manifest_source_lines"] == 1087):
    audit["verdict"] = "FAIL"
(own / "BINDING_AUDIT.json").write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
raise SystemExit(0 if audit["verdict"] == "PASS" else 1)
