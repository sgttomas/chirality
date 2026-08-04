#!/usr/bin/env python3
"""Validate the exact S3 decomposition application and preserved boundaries."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SNAPSHOT = Path(__file__).resolve().parent
RUN = ROOT / "execution/_Coordination/AgentRuns/ROOT_FOUR_LANES_2026-08-02"

PATHS = {
    "owner_ruling": RUN / "OWNER_RULING_2026-08-03_S2_APPLY_PI_G1B.md",
    "h3_return": RUN / "instances/H3-M2-APPLY/RETURN.md",
    "live_prd": ROOT / "docs/PRD_ROOT.md",
    "candidate_prd": SNAPSHOT / "Basis_Reconciliation_Candidate/docs/PRD_ROOT.md",
    "preapply_decomposition_evidence": SNAPSHOT.parent
    / "SCA-002_2026-07-29_0800/Gate_3_Candidate/Chirality_Root_SOFTWARE_DECOMP_v1_0.md",
    "live_decomposition": ROOT
    / "execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md",
    "candidate_decomposition": SNAPSHOT
    / "Basis_Reconciliation_Candidate/execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md",
    "scope_ledger": ROOT / "execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv",
    "deliverable_register": ROOT
    / "execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv",
    "latest_pointer": ROOT / "execution/_ScopeChange/_LATEST.md",
}

EXPECTED = {
    "owner_ruling": "12f7c46e86ca19c1e065e96b05e09814b9806cd5b0742f74d8cce405ef389129",
    "h3_return": "169cfa5e354aff0df9517c62b7093b73cf967598f5f263cb9f137663c4bac3a8",
    "live_prd": "d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4",
    "candidate_prd": "d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4",
    "preapply_decomposition_evidence": "6f43f3fbc25e0663697464a7a20f3b1bac4b731b01efbe473642e238b93a4d49",
    "live_decomposition": "69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c",
    "candidate_decomposition": "69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c",
    "scope_ledger": "3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2",
    "deliverable_register": "a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395",
    "latest_pointer": "b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def section(value: str, start: str, end: str) -> str:
    return value[value.index(start) : value.index(end)]


def stable_commitment_rows(value: str) -> list[str]:
    return [line for line in value.splitlines() if re.match(r"^\| \*\*[NODE]-[0-9]+", line)]


def identifiers(value: str) -> set[str]:
    return set(
        re.findall(
            r"\b(?:PKG-[0-9]{2}|DEL-[0-9]{2}-[0-9]{2}|SOW-[0-9]{3}|OBJ-[0-9]{3})\b",
            value,
        )
    )


actual = {name: sha256(path) for name, path in PATHS.items()}
checks: list[dict[str, str]] = []


def check(name: str, passed: bool, evidence: str) -> None:
    checks.append({"name": name, "result": "PASS" if passed else "FAIL", "evidence": evidence})


check("authority:owner_ruling", actual["owner_ruling"] == EXPECTED["owner_ruling"], actual["owner_ruling"])
check("dependency:h3_return", actual["h3_return"] == EXPECTED["h3_return"], actual["h3_return"])
check("prd:live_exact", actual["live_prd"] == EXPECTED["live_prd"], actual["live_prd"])
check("prd:candidate_exact", actual["candidate_prd"] == EXPECTED["candidate_prd"], actual["candidate_prd"])
check(
    "decomposition:preapply_evidence_exact",
    actual["preapply_decomposition_evidence"] == EXPECTED["preapply_decomposition_evidence"],
    actual["preapply_decomposition_evidence"],
)
check(
    "decomposition:live_exact_applied",
    actual["live_decomposition"] == EXPECTED["live_decomposition"],
    actual["live_decomposition"],
)
check(
    "decomposition:candidate_exact",
    actual["candidate_decomposition"] == EXPECTED["candidate_decomposition"],
    actual["candidate_decomposition"],
)
check(
    "decomposition:live_candidate_byte_parity",
    PATHS["live_decomposition"].read_bytes() == PATHS["candidate_decomposition"].read_bytes(),
    "live decomposition is byte-identical to frozen candidate",
)
check("companions:scope_ledger_unchanged", actual["scope_ledger"] == EXPECTED["scope_ledger"], actual["scope_ledger"])
check(
    "companions:deliverable_register_unchanged",
    actual["deliverable_register"] == EXPECTED["deliverable_register"],
    actual["deliverable_register"],
)
check("scope_change:latest_pointer_unchanged", actual["latest_pointer"] == EXPECTED["latest_pointer"], actual["latest_pointer"])

prd = text(PATHS["live_prd"])
candidate_prd = text(PATHS["candidate_prd"])
decomp = text(PATHS["live_decomposition"])
candidate_decomp = text(PATHS["candidate_decomposition"])
preapply_decomp = text(PATHS["preapply_decomposition_evidence"])

check(
    "pair:ref001_pins_applied_prd",
    f"| `{actual['live_prd']}` | Exact SCA-003 basis-reconciliation PRD candidate" in decomp,
    f"REF-001 pin={actual['live_prd']}",
)
check(
    "prd:stable_commitment_rows_preserved",
    stable_commitment_rows(prd) == stable_commitment_rows(candidate_prd)
    and len(stable_commitment_rows(prd)) == 43,
    "43 stable-commitment rows equal frozen candidate",
)
check(
    "prd:d8_annex_preserved",
    section(prd, "#### 5.3.1 Merge-gate policy", "### 5.4 Evidence")
    == section(candidate_prd, "#### 5.3.1 Merge-gate policy", "### 5.4 Evidence"),
    "§5.3.1 equals frozen candidate",
)
check(
    "decomposition:identifier_set_preserved",
    identifiers(decomp) == identifiers(candidate_decomp) and len(identifiers(decomp)) == 89,
    "89 decomposition identifiers equal frozen candidate",
)
check(
    "decomposition:historical_dec023_preserved",
    next(line for line in preapply_decomp.splitlines() if "| DEC-023 |" in line)
    == next(line for line in decomp.splitlines() if "| DEC-023 |" in line),
    "DEC-023 equals pre-application evidence",
)
check(
    "decomposition:current_status_and_dec024_present",
    "v1.2 — ACCEPTED CURRENT BASIS" in decomp
    and "ACCEPT SCA-002 271d456a" in decomp
    and "| DEC-024 | 2026-08-02 |" in decomp,
    "accepted status, acceptance token, and additive DEC-024 present",
)

failures = [entry for entry in checks if entry["result"] != "PASS"]
report = {
    "schema_version": "1.0",
    "run_id": "ROOT_FOUR_LANES_2026-08-02",
    "node": "S3",
    "amendment_id": "SCA-003",
    "status": "PASS" if not failures else "FAIL",
    "checks_total": len(checks),
    "checks_passed": len(checks) - len(failures),
    "checks_failed": len(failures),
    "hashes": actual,
    "checks": checks,
}
(SNAPSHOT / "S3_Applied_Validation.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

applied = {
    "schema_version": "1.0",
    "run_id": "ROOT_FOUR_LANES_2026-08-02",
    "node": "S3",
    "amendment_id": "SCA-003",
    "application_state": "APPLIED_PENDING_HUMAN_POST_CHANGE_CONFIRMATION",
    "authority": {
        "owner_ruling_sha256": actual["owner_ruling"],
        "h3_dependency_return_sha256": actual["h3_return"],
    },
    "files": [
        {
            "path": "execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md",
            "before_sha256": actual["preapply_decomposition_evidence"],
            "approved_candidate_sha256": actual["candidate_decomposition"],
            "applied_sha256": actual["live_decomposition"],
            "exact_candidate_match": PATHS["live_decomposition"].read_bytes()
            == PATHS["candidate_decomposition"].read_bytes(),
        }
    ],
    "preserved": {
        "docs/PRD_ROOT.md": actual["live_prd"],
        "execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv": actual["scope_ledger"],
        "execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv": actual["deliverable_register"],
        "execution/_ScopeChange/_LATEST.md": actual["latest_pointer"],
    },
}
(SNAPSHOT / "S3_Applied_File_Hashes.json").write_text(json.dumps(applied, indent=2) + "\n", encoding="utf-8")

print(json.dumps({"status": report["status"], "checks": len(checks), "failures": len(failures)}))
raise SystemExit(1 if failures else 0)
