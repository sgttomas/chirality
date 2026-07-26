#!/usr/bin/env python3
"""Validate and freeze the completed tandem-review package."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path


REPO = Path("/Users/ryan/.codex/worktrees/d9d0/chirality")
PRIMARY = Path("/Users/ryan/dev/chirality")
REL = Path("execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_TANDEM_2026-07-26_DA31C19")
ROOT = REPO / REL
FREEZE = "da31c19b5656dd74615e308c4215688971d33dc9"
PRODUCT = "aeadf5304435e1a4d8b4a26306da9ad4d4519eb6"
BASELINE_PRIMARY_STATUS_SHA256 = "3938a86b7c1d503839eb0dd5ad80b8c700faf57769592792cb92023e727f7e23"


def run(cwd: Path, *args: str) -> bytes:
    return subprocess.run(
        args,
        cwd=cwd,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


checks: list[dict[str, object]] = []


def check(name: str, passed: bool, detail: object) -> None:
    checks.append({"name": name, "verdict": "PASS" if passed else "FAIL", "detail": detail})


json_files = [
    "FROZEN_BASIS_MANIFEST.json",
    "DISPATCH_MANIFEST.json",
    "PASS1_FREEZE.json",
    "CHALLENGE_DISPATCH_MANIFEST.json",
    "CHALLENGE_FREEZE.json",
]
for relative in json_files:
    path = ROOT / relative
    try:
        json.loads(path.read_text(encoding="utf-8"))
        check(f"json:{relative}", True, "valid")
    except Exception as exc:
        check(f"json:{relative}", False, str(exc))

frozen_manifest = json.loads((ROOT / "FROZEN_BASIS_MANIFEST.json").read_text())
check(
    "frozen-manifest-sha256",
    digest(ROOT / "FROZEN_BASIS_MANIFEST.json")
    == "f569d994156f9585fd100286e43b325116ae473616b1d1bd4f169bd88d632386",
    digest(ROOT / "FROZEN_BASIS_MANIFEST.json"),
)
check("frozen-manifest-entry-count", frozen_manifest["entry_count"] == 776, frozen_manifest["entry_count"])
check(
    "product-basis-to-freeze-diff",
    frozen_manifest["product_basis_to_freeze_diff"]
    == ["plans/chirality_program_architecture_and_tandem_review_2026-07-25.html"],
    frozen_manifest["product_basis_to_freeze_diff"],
)

pass1_freeze = json.loads((ROOT / "PASS1_FREEZE.json").read_text())
pass1_hash_checks = {}
for reviewer_key in ("reviewer_a", "reviewer_b"):
    for artifact_key in ("report", "findings", "trace_matrix", "boundary_matrix", "return_manifest"):
        item = pass1_freeze[reviewer_key][artifact_key]
        actual = digest(ROOT / item["path"])
        pass1_hash_checks[f"{reviewer_key}.{artifact_key}"] = {
            "expected": item["sha256"],
            "actual": actual,
            "match": actual == item["sha256"],
        }
check(
    "pass1-freeze-hashes",
    all(item["match"] for item in pass1_hash_checks.values()),
    pass1_hash_checks,
)

challenge_freeze = json.loads((ROOT / "CHALLENGE_FREEZE.json").read_text())
challenge_hash_checks = {}
for challenge_key in ("a_on_b", "b_on_a"):
    for artifact_key in ("report", "challenge", "return_manifest"):
        item = challenge_freeze[challenge_key][artifact_key]
        actual = digest(ROOT / item["path"])
        challenge_hash_checks[f"{challenge_key}.{artifact_key}"] = {
            "expected": item["sha256"],
            "actual": actual,
            "match": actual == item["sha256"],
        }
check(
    "challenge-freeze-hashes",
    all(item["match"] for item in challenge_hash_checks.values()),
    challenge_hash_checks,
)

findings_path = ROOT / "FINDINGS.csv"
with findings_path.open(newline="", encoding="utf-8") as handle:
    reader = csv.DictReader(handle)
    findings_header = reader.fieldnames
    findings = list(reader)
expected_header = [
    "FindingID",
    "Concern",
    "Classification",
    "Severity",
    "Scope",
    "Claim",
    "EvidenceRefs",
    "Status",
    "RecommendedOwner",
    "RerunRequirement",
]
check("findings-header", findings_header == expected_header, findings_header)
check("findings-count", len(findings) == 19, len(findings))
check(
    "findings-unique-ids",
    len({row["FindingID"] for row in findings}) == len(findings)
    and all(row["FindingID"].startswith("FAN-") for row in findings),
    [row["FindingID"] for row in findings],
)
check(
    "findings-complete",
    all(all(row.get(field, "").strip() for field in expected_header) for row in findings),
    "all cells non-empty",
)
status_counts = Counter(row["Status"] for row in findings)
expected_status_counts = Counter(
    {
        "AGREED": 9,
        "RESOLVED_BY_EVIDENCE": 6,
        "STANDING_DIVERGENCE": 2,
        "SHARED_BLIND_SPOT_RISK": 1,
        "STALE_INPUT": 1,
    }
)
check("fan-in-status-counts", status_counts == expected_status_counts, dict(status_counts))

report_text = (ROOT / "EVALUATION_REPORT.md").read_text(encoding="utf-8")
report_sections = [
    "## Basis",
    "## Method",
    "## Coverage",
    "## Validated-return inventory",
    "## Findings",
    "## Conflicts and unknowns",
    "## Optional scorecard",
    "## Recommendations",
    "## Decision queue",
    "## Handoff summary",
]
check(
    "evaluation-report-contract",
    all(section in report_text for section in report_sections),
    report_sections,
)
check("evaluation-report-no-score", "No scorecard was produced" in report_text, "explicit")

handoff_text = (ROOT / "HANDOFF.md").read_text(encoding="utf-8")
handoff_sections = [
    "## State",
    "## Accepted upstream snapshots",
    "## Derivative-package status",
    "## Closure verdict",
    "## Human decision queue",
    "## Genuine blockers",
    "## Rerun requirements",
    "## Remaining unknowns",
    "## Next owner",
]
check("handoff-contract", all(section in handoff_text for section in handoff_sections), handoff_sections)

worktree_status = run(REPO, "git", "status", "--porcelain", "--untracked-files=all").decode()
status_paths = []
for line in worktree_status.splitlines():
    if len(line) >= 4:
        status_paths.append(line[3:])
allowed_prefix = str(REL) + "/"
check(
    "write-scope-containment",
    bool(status_paths) and all(path.startswith(allowed_prefix) for path in status_paths),
    status_paths,
)

primary_status = run(PRIMARY, "git", "status", "--short", "--untracked-files=all")
primary_status_sha = hashlib.sha256(primary_status).hexdigest()
check(
    "primary-checkout-status-unchanged",
    primary_status_sha == BASELINE_PRIMARY_STATUS_SHA256,
    {
        "baseline_sha256": BASELINE_PRIMARY_STATUS_SHA256,
        "final_sha256": primary_status_sha,
        "status": primary_status.decode().splitlines(),
    },
)

git_diff = run(REPO, "git", "diff", "--name-only", PRODUCT, FREEZE, "--").decode().splitlines()
check(
    "git-freeze-diff-recheck",
    git_diff == ["plans/chirality_program_architecture_and_tandem_review_2026-07-25.html"],
    git_diff,
)

required_outputs = [
    "EVALUATION_PROTOCOL.md",
    "FROZEN_BASIS_MANIFEST.json",
    "DISPATCH_MANIFEST.json",
    "PASS1_FREEZE.json",
    "CHALLENGE_DISPATCH_MANIFEST.json",
    "CHALLENGE_FREEZE.json",
    "returns/A_PASS1/REPORT.md",
    "returns/B_PASS1/REPORT.md",
    "challenges/A_ON_B/REPORT.md",
    "challenges/B_ON_A/REPORT.md",
    "FINDINGS.csv",
    "EVALUATION_REPORT.md",
    "HANDOFF.md",
]
output_hashes = {}
for relative in required_outputs:
    path = ROOT / relative
    output_hashes[relative] = {
        "sha256": digest(path),
        "bytes": path.stat().st_size,
    }
check("required-output-inventory", len(output_hashes) == len(required_outputs), sorted(output_hashes))

failures = [item for item in checks if item["verdict"] == "FAIL"]
result = {
    "schema": "chirality.tandem-review.final-validation.v1",
    "review_id": "CHIRALITY-PROGRAM-ARCH-TANDEM-2026-07-26-DA31C19",
    "review_freeze": FREEZE,
    "verdict": "PASS" if not failures else "FAIL",
    "failure_count": len(failures),
    "checks": checks,
    "fan_in_status_counts": dict(sorted(status_counts.items())),
    "output_hashes": output_hashes,
}
output = ROOT / "VALIDATION_RESULT.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"output": str(output), "verdict": result["verdict"], "failure_count": len(failures)}, indent=2))
raise SystemExit(0 if not failures else 1)
