#!/usr/bin/env python3
"""Validate and render the SCA-003 metadata-only basis-reconciliation candidate."""

from __future__ import annotations

import difflib
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SNAPSHOT = Path(__file__).resolve().parent

PRD_LIVE = ROOT / "docs/PRD_ROOT.md"
PRD_CANDIDATE = SNAPSHOT / "Basis_Reconciliation_Candidate/docs/PRD_ROOT.md"
DECOMP_LIVE = ROOT / "execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md"
DECOMP_CANDIDATE = (
    SNAPSHOT
    / "Basis_Reconciliation_Candidate/execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md"
)
SCOPE_LEDGER = ROOT / "execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv"
DELIVERABLE_REGISTER = (
    ROOT / "execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv"
)

DIFF_PATH = SNAPSHOT / "Basis_Reconciliation_Exact_Amendment.diff"
REPORT_PATH = SNAPSHOT / "Basis_Reconciliation_Validation.json"

EXPECTED = {
    "live_prd": "278f31ae99607f970e39c6535f809c93a7c5bf09b139ffa2cbbdbe3f08c3746c",
    "candidate_prd": "d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4",
    "live_decomposition": "6f43f3fbc25e0663697464a7a20f3b1bac4b731b01efbe473642e238b93a4d49",
    "candidate_decomposition": "69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c",
    "scope_ledger": "3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2",
    "deliverable_register": "a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def section(value: str, start: str, end: str) -> str:
    return value[value.index(start) : value.index(end)]


def stable_commitment_rows(value: str) -> list[str]:
    return [
        line
        for line in value.splitlines()
        if re.match(r"^\| \*\*[NODE]-[0-9]+", line)
    ]


def identifiers(value: str) -> set[str]:
    return set(re.findall(r"\b(?:PKG-[0-9]{2}|DEL-[0-9]{2}-[0-9]{2}|SOW-[0-9]{3}|OBJ-[0-9]{3})\b", value))


def exact_diff(before: Path, after: Path, logical_path: str) -> str:
    before_lines = text(before).splitlines(keepends=True)
    after_lines = text(after).splitlines(keepends=True)
    return "".join(
        difflib.unified_diff(
            before_lines,
            after_lines,
            fromfile=f"a/{logical_path}",
            tofile=f"b/{logical_path}",
            n=0,
            lineterm="\n",
        )
    )


checks: list[dict[str, object]] = []


def check(name: str, passed: bool, evidence: str) -> None:
    checks.append({"name": name, "result": "PASS" if passed else "FAIL", "evidence": evidence})


prd_live_text = text(PRD_LIVE)
prd_candidate_text = text(PRD_CANDIDATE)
decomp_live_text = text(DECOMP_LIVE)
decomp_candidate_text = text(DECOMP_CANDIDATE)

actual = {
    "live_prd": sha256(PRD_LIVE),
    "candidate_prd": sha256(PRD_CANDIDATE),
    "live_decomposition": sha256(DECOMP_LIVE),
    "candidate_decomposition": sha256(DECOMP_CANDIDATE),
    "scope_ledger": sha256(SCOPE_LEDGER),
    "deliverable_register": sha256(DELIVERABLE_REGISTER),
}

for key, expected in EXPECTED.items():
    check(f"sha256:{key}", actual[key] == expected, f"expected={expected}; actual={actual[key]}")

check(
    "prd:stable_commitment_rows_unchanged",
    stable_commitment_rows(prd_live_text) == stable_commitment_rows(prd_candidate_text),
    f"row_count={len(stable_commitment_rows(prd_live_text))}",
)
check(
    "prd:d8_annex_unchanged",
    section(prd_live_text, "#### 5.3.1 Merge-gate policy", "### 5.4 Evidence")
    == section(prd_candidate_text, "#### 5.3.1 Merge-gate policy", "### 5.4 Evidence"),
    "§5.3.1 bytes match live Revision 8",
)
check(
    "prd:current_status_present",
    "Current status: ACCEPTED — Revision 8" in prd_candidate_text
    and "### 10.5 Current document control — Revision 8" in prd_candidate_text,
    "top current-status layer and §10.5 present",
)
check(
    "prd:historical_candidate_control_preserved",
    "Status: `ADOPTION-READY — adopted only by the instrument named below`" in prd_candidate_text
    and "### 10.4 Historical Revision 7 candidate document control" in prd_candidate_text,
    "Revision 7 candidate header/table retained and explicitly time-scoped",
)
check(
    "decomposition:identifier_set_unchanged",
    identifiers(decomp_live_text) == identifiers(decomp_candidate_text),
    f"identifier_count={len(identifiers(decomp_live_text))}",
)
check(
    "decomposition:accepted_status_present",
    "v1.2 — ACCEPTED CURRENT BASIS" in decomp_candidate_text
    and "ACCEPT SCA-002 271d456a" in decomp_candidate_text,
    "current status cites exact SCA-002 acceptance token",
)
check(
    "decomposition:prd_candidate_pin_exact",
    EXPECTED["candidate_prd"] in decomp_candidate_text,
    f"REF-001 pins candidate PRD SHA-256 {EXPECTED['candidate_prd']}",
)
check(
    "decomposition:historical_decision_preserved",
    next(line for line in decomp_live_text.splitlines() if "| DEC-023 |" in line)
    == next(line for line in decomp_candidate_text.splitlines() if "| DEC-023 |" in line),
    "DEC-023 line byte-preserved",
)
check(
    "decomposition:new_disposition_present",
    "| DEC-024 | 2026-08-02 |" in decomp_candidate_text,
    "additive current-state reconciliation record present",
)
check(
    "decomposition:companion_registers_untouched",
    actual["scope_ledger"] == EXPECTED["scope_ledger"]
    and actual["deliverable_register"] == EXPECTED["deliverable_register"],
    "scope ledger and deliverable register remain at pre-candidate hashes",
)
check(
    "candidate:only_two_authoritative_target_copies",
    sorted(
        str(path.relative_to(SNAPSHOT / "Basis_Reconciliation_Candidate"))
        for path in (SNAPSHOT / "Basis_Reconciliation_Candidate").rglob("*")
        if path.is_file()
    )
    == [
        "docs/PRD_ROOT.md",
        "execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md",
    ],
    "candidate tree contains exactly the PRD and decomposition target copies",
)

diff_text = exact_diff(PRD_LIVE, PRD_CANDIDATE, "docs/PRD_ROOT.md")
diff_text += exact_diff(
    DECOMP_LIVE,
    DECOMP_CANDIDATE,
    "execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md",
)
DIFF_PATH.write_text(diff_text, encoding="utf-8")

failures = [entry for entry in checks if entry["result"] != "PASS"]
report = {
    "schema_version": "1.0",
    "amendment_id": "SCA-003",
    "candidate_kind": "metadata_only_basis_reconciliation",
    "status": "PASS" if not failures else "FAIL",
    "checks_total": len(checks),
    "checks_passed": len(checks) - len(failures),
    "checks_failed": len(failures),
    "hashes": actual,
    "application_order": ["docs/PRD_ROOT.md", "execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md"],
    "checks": checks,
}
REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": report["status"], "checks": len(checks), "failures": len(failures)}))
raise SystemExit(1 if failures else 0)
