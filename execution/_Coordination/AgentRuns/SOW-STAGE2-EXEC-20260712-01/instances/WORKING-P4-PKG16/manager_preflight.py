#!/usr/bin/env python3
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
PREFLIGHT = RUN / "snapshots/W_P4/preflight"
INSTANCE = RUN / "instances/WORKING-P4-PKG16"

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

checks = []
def record(name, ok, detail):
    checks.append({"check": name, "pass": bool(ok), "detail": detail})

manifest_rows = list(csv.DictReader((PREFLIGHT / "MANIFEST.tsv").open(), delimiter="\t"))
for row in manifest_rows:
    p = PREFLIGHT / row["artifact"]
    record("snapshot_binding", p.is_file() and sha(p) == row["sha256"], row["artifact"])
record("snapshot_manifest_sha256", sha(PREFLIGHT / "MANIFEST.tsv") == "e3c0ba738b4109fe8ab3eccaaab1e76e82e213b5e6b27f9dd6632c7716682faf", sha(PREFLIGHT / "MANIFEST.tsv"))

p4_rows = [r for r in csv.DictReader((PREFLIGHT / "P4_MANIFEST.tsv").open(), delimiter="\t") if r["package"] == "PKG-16"]
record("package_population", [r["deliverable_id"] for r in p4_rows] == [f"DEL-16-0{i}" for i in range(1, 5)], [r["deliverable_id"] for r in p4_rows])
record("source_line_total", sum(int(r["source_lines"]) for r in p4_rows) == 1097, sum(int(r["source_lines"]) for r in p4_rows))

bindings = [r for r in csv.DictReader((PREFLIGHT / "EXPECTED_LIVE_BINDINGS.tsv").open(), delimiter="\t") if r["package"] == "PKG-16"]
for row in bindings:
    p = ROOT / row["live_path"] / row["binding"]
    record("live_binding", row["state"] == "PRESENT" and p.is_file() and sha(p) == row["sha256"], f'{row["deliverable_id"]}:{row["binding"]}')

for row in p4_rows:
    live = ROOT / row["live_path"]
    legacy = [live / n for n in ("Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md")]
    status = (live / "_STATUS.md").read_text()
    record("legacy_four_doc", all(p.is_file() for p in legacy) and not (live / "ScopeOfWork.md").exists(), row["deliverable_id"])
    record("lifecycle", "IN_PROGRESS" in status and row["lifecycle"] == "IN_PROGRESS", row["deliverable_id"])

predecessor = RUN / "instances/WORKING-P4-PKG15/RETURN.md"
record("predecessor_release", predecessor.is_file() and "RUN_STATUS: `PASS`" in predecessor.read_text(), str(predecessor.relative_to(RUN)))
launch = INSTANCE / "LAUNCH_BRIEF.md"
record("manager_release", launch.is_file() and "RELEASED AFTER PKG-15 PASS" in launch.read_text(), str(launch.relative_to(RUN)))
for name in ("PREDECESSOR_RESULTS.tsv", "PKG00_DIRECTION_VALIDATION.tsv", "METHOD_BINDINGS.tsv", "APPLICABLE_CHECKS.tsv", "REFS.tsv"):
    p = PREFLIGHT / name
    text = p.read_text()
    record("frozen_surface", p.is_file() and "FAIL" not in text and "BLOCKED" not in text, name)

result = {
    "status": "PASS" if all(c["pass"] for c in checks) else "BLOCKED",
    "package": "PKG-16",
    "members": len(p4_rows),
    "source_lines": sum(int(r["source_lines"]) for r in p4_rows),
    "live_bindings": len(bindings),
    "checks": checks,
}
(INSTANCE / "PREFLIGHT_REPRODUCTION.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({k: v for k, v in result.items() if k != "checks"}, indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
