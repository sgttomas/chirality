#!/usr/bin/env python3
"""Validate and render the three-passage COV-POST-001 correction candidate."""

from __future__ import annotations

import difflib
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SNAPSHOT = Path(__file__).resolve().parent
RUN = ROOT / "execution/_Coordination/AgentRuns/ROOT_FOUR_LANES_2026-08-02"
SOURCE = ROOT / "execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md"
CANDIDATE = SNAPSHOT / "COV_POST_001_Candidate/execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md"
DIFF = SNAPSHOT / "COV_POST_001_Exact_Amendment.diff"
REPORT = SNAPSHOT / "COV_POST_001_Validation.json"

OWNER_SHA = "12f7c46e86ca19c1e065e96b05e09814b9806cd5b0742f74d8cce405ef389129"
APPLIED_SHA = "f2781dd2c33f01cbaf014b2bb97fbff0bcdf1db3c46a8969f195a7d320501cc8"
DECISION_PATH = "execution/_ScopeChange/SCA-003_2026-08-02_2212/Decision_Log.md"

PATHS = {
    "launch_brief": RUN / "instances/S4-SCOPE-CORRECTION/LAUNCH_BRIEF.md",
    "route_ruling": RUN / "OWNER_RULING_2026-08-03_COV_POST_001_ROUTE.md",
    "source_decomposition": SOURCE,
    "candidate_decomposition": CANDIDATE,
    "prd": ROOT / "docs/PRD_ROOT.md",
    "s3_applied_files": SNAPSHOT / "S3_Applied_File_Hashes.json",
    "s3_validation": SNAPSHOT / "S3_Applied_Validation.json",
    "s3_return": RUN / "instances/S3-SCOPE-APPLY/RETURN.md",
    "post_apply_audit": SNAPSHOT / "Evidence/AUDIT_DECOMP_POST_APPLY/RETURN.md",
    "latest": ROOT / "execution/_ScopeChange/_LATEST.md",
    "scope_ledger": ROOT / "execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv",
    "deliverable_register": ROOT / "execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv",
}

EXPECTED = {
    "launch_brief": "12af64a7f58676bf2831e04d439f62680420b4ee111e4adf67cfa913b3188e25",
    "route_ruling": "0349897a313f1a41973d3134be3dd1addffc4e9d20ed73bb60b337143de6022b",
    "source_decomposition": "69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c",
    "candidate_decomposition": "23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d",
    "prd": "d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4",
    "s3_applied_files": APPLIED_SHA,
    "s3_validation": "18e00b070e7eb889043688531ed4dfcdeca2f168b4e031ba2dfe86761fd08c61",
    "s3_return": "38478cd78435e771897378a241fe6b8f0a386e3d16fd3f36c18eaa61f7b1eb57",
    "post_apply_audit": "0c49c5e18e1d02bc9abec1b01adcf1adf5cc895b79e159259d76a470aa4630a5",
    "latest": "b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1",
    "scope_ledger": "3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2",
    "deliverable_register": "a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395",
}

OLD_NEW = [
    (
        "**Amendment:** `SCA-002` accepted and applied on 2026-07-29; this SCA-003 basis-reconciliation candidate changes current-facing acceptance/status metadata only and remains pending exact owner acceptance and application",
        f"**Amendment:** `SCA-002` accepted and applied on 2026-07-29; the exact SCA-003 basis-reconciliation candidate was accepted and applied under owner ruling SHA-256 `{OWNER_SHA}`, with applied-file evidence SHA-256 `{APPLIED_SHA}`; human confirmation status is recorded only in `{DECISION_PATH}`",
    ),
    (
        "| DEC-024 | 2026-08-02 | **SCA-003 basis-reconciliation candidate aligns current-facing acceptance and source-control metadata without changing decomposition truth.** The title, header, status block, REF-001 pin, and downstream acceptance notes are reconciled to the already-recorded facts that SCA-002 revision 1.2 was accepted/applied and that Receipt 64 produced Root PRD Revision 8. DEC-023 and the original SCA-002 candidate Change Log entry remain unchanged as time-scoped proposal history. | SCA-002 `Decision_Log.md`, `Handoff_State.md`, `Applied_File_Hashes.json`, `_ScopeChange/_LATEST.md`, Receipt 63, Receipt 64, and the Root loop handoff agree on the current state. This is metadata-only: no scope item, package, deliverable, objective, ID, mapping, status row, count, topology, or substantive requirement changes. Candidate effect remains pending exact human acceptance and application. |",
        f"| DEC-024 | 2026-08-02 | **SCA-003 basis reconciliation aligns current-facing acceptance and source-control metadata without changing decomposition truth.** The title, header, status block, REF-001 pin, and downstream acceptance notes are reconciled to the already-recorded facts that SCA-002 revision 1.2 was accepted/applied and that Receipt 64 produced Root PRD Revision 8. DEC-023 and the original SCA-002 candidate Change Log entry remain unchanged as time-scoped proposal history. | SCA-002 `Decision_Log.md`, `Handoff_State.md`, `Applied_File_Hashes.json`, `_ScopeChange/_LATEST.md`, Receipt 63, Receipt 64, and the Root loop handoff agree on the current state. This is metadata-only: no scope item, package, deliverable, objective, ID, mapping, status row, count, topology, or substantive requirement changes. The exact SCA-003 candidate was accepted and applied under owner ruling SHA-256 `{OWNER_SHA}`, with applied-file evidence SHA-256 `{APPLIED_SHA}`; human confirmation status is recorded only in `{DECISION_PATH}`. |",
    ),
    (
        "  substantive requirement changes. These metadata bytes remain pending\n  exact human acceptance and application.",
        f"  substantive requirement changes. Exact SCA-003 candidate acceptance and\n  application are recorded by owner ruling SHA-256\n  `{OWNER_SHA}`\n  and applied-file evidence SHA-256\n  `{APPLIED_SHA}`;\n  human confirmation status is recorded only in\n  `{DECISION_PATH}`.",
    ),
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def identifiers(value: str) -> set[str]:
    return set(re.findall(r"\b(?:PKG-[0-9]{2}|DEL-[0-9]{2}-[0-9]{2}|SOW-[0-9]{3}|OBJ-[0-9]{3})\b", value))


actual = {name: sha256(path) for name, path in PATHS.items()}
checks: list[dict[str, str]] = []


def check(name: str, passed: bool, evidence: str) -> None:
    checks.append({"name": name, "result": "PASS" if passed else "FAIL", "evidence": evidence})


for name in (
    "launch_brief", "route_ruling", "source_decomposition", "candidate_decomposition",
    "prd", "s3_applied_files", "s3_validation", "s3_return", "post_apply_audit",
    "latest", "scope_ledger", "deliverable_register",
):
    check(f"sha256:{name}", actual[name] == EXPECTED[name], f"expected={EXPECTED[name]}; actual={actual[name]}")

source = SOURCE.read_text(encoding="utf-8")
candidate = CANDIDATE.read_text(encoding="utf-8")
constructed = source
for old, new in OLD_NEW:
    check(f"passage:{len(checks)-11}:source_unique", constructed.count(old) == 1, f"source occurrences={constructed.count(old)}")
    constructed = constructed.replace(old, new, 1)

check("containment:exact_three_passages", candidate == constructed, "candidate equals source after exactly three authorized replacements")
new_passages = [new for _, new in OLD_NEW]
check(
    "future_truth:no_pending_or_confirmed",
    all(not re.search(r"\b(?:pending|confirmed)\b", value, re.IGNORECASE) for value in new_passages),
    "corrected passages contain neither pending nor confirmed",
)
check(
    "future_truth:completed_acts_and_pointers",
    all(OWNER_SHA in value and APPLIED_SHA in value and DECISION_PATH in value for value in new_passages),
    "each corrected passage cites completed acts, exact evidence hashes, and Decision_Log confirmation pointer",
)
check(
    "semantic_inventory:identifiers_unchanged",
    identifiers(source) == identifiers(candidate) and len(identifiers(source)) == 89,
    "89 identifiers preserved",
)
source_dec023 = next(line for line in source.splitlines() if "| DEC-023 |" in line)
candidate_dec023 = next(line for line in candidate.splitlines() if "| DEC-023 |" in line)
check(
    "history_and_shape:protected",
    source_dec023 == candidate_dec023 and source.count("| DEC-") == candidate.count("| DEC-"),
    "DEC-023 byte-preserved and decision-row count unchanged",
)

diff_text = "".join(
    difflib.unified_diff(
        source.splitlines(keepends=True),
        candidate.splitlines(keepends=True),
        fromfile="a/execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md",
        tofile="b/execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md",
        n=0,
        lineterm="\n",
    )
)
DIFF.write_text(diff_text, encoding="utf-8")

failures = [entry for entry in checks if entry["result"] != "PASS"]
report = {
    "schema_version": "1.0",
    "run_id": "ROOT_FOUR_LANES_2026-08-02",
    "node": "S4",
    "finding": "COV-POST-001",
    "status": "PASS" if not failures else "FAIL",
    "checks_total": len(checks),
    "checks_passed": len(checks) - len(failures),
    "checks_failed": len(failures),
    "hashes": actual,
    "authorized_passages": 3,
    "checks": checks,
}
REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": report["status"], "checks": len(checks), "failures": len(failures)}))
raise SystemExit(1 if failures else 0)
