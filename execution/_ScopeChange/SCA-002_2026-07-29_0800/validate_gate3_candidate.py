#!/usr/bin/env python3
"""Deterministic SCA-002 Gate 3 candidate validation.

Read-only. Compares the Gate_3_Candidate/ surfaces against the frozen-basis
authoritative surfaces under execution/_Decomposition/ and writes
Gate_3_Validation.json. Never mutates an input.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DECOMP = ROOT / "execution" / "_Decomposition"
SNAPSHOT = Path(__file__).resolve().parent
CANDIDATE = SNAPSHOT / "Gate_3_Candidate"
REPORT = SNAPSHOT / "Gate_3_Validation.json"

LEDGER = "chirality_root_scope_ledger_v1_0.csv"
REGISTER = "chirality_root_deliverable_register_v1_0.csv"
MAIN = "Chirality_Root_SOFTWARE_DECOMP_v1_0.md"

EXPECTED_BASIS_SHA256 = {
    MAIN: "2dd37e20d8175eec3a7a926dcf454fbee5065d076fc59eac6ead82e911192c18",
    LEDGER: "0d48abe08aa336ac5e495650451f286b4b717606f047adff931c45dacc8531a4",
    REGISTER: "ec32b36fdc078e44a7ca094e9c854a3be6b7d5917360fe5ef5f22ff3702a13b8",
}
EXPECTED_PRD_SHA256 = (
    "15fba9c36a197b36b281297af123115bcd3f282fe6c6f2fae05cd703b3743748"
)

REQUIRED_SOW042_TOKENS = [
    "every registered loop",
    "shared change-management role",
    "human-gated pull requests as the standing default",
    "bounded owner grant",
    "recorded before or at exercise",
    "merge-gate policy in PRD annex §5.3.1",
    "K-MERGE-1",
    "four closeout identities",
    "semantic approval, approved source SHA, merge authorization, effective merge SHA",
    "stricter local merge discipline remains controlling",
]
REQUIRED_DEL0406_DESC_TOKENS = [
    "shared change-management role",
    "human-gated pull requests as the standing default",
    "K-MERGE-1",
    "four closeout identities",
    "bounded owner grant recorded per PRD annex §5.3.1",
    "within its recorded scope and term",
]
REQUIRED_DEL0406_ART_TOKENS = [
    "Closeout checklist",
    "four-identity closeout evidence",
    "bounded-owner-grant records when a grant is exercised",
    "PR gate notes",
]
FORBIDDEN_OLD_TEXT = ["self-merge", "self merge", "selfmerge"]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_rows(raw: str) -> list[list[str]]:
    return list(csv.reader(io.StringIO(raw)))


def main() -> None:
    results: list[dict[str, str]] = []

    def check(condition: bool, name: str, details: str) -> None:
        results.append(
            {"check": name, "status": "PASS" if condition else "FAIL", "details": details}
        )

    # Basis integrity: the authoritative surfaces are the untouched v1.1 bytes.
    for name, expected in EXPECTED_BASIS_SHA256.items():
        observed = sha256(DECOMP / name)
        check(
            observed == expected,
            f"basis_untouched::{name}",
            f"observed={observed} expected={expected}",
        )

    # The live PRD at basis is the adopted D-GOV-31 Rev 7 subject.
    prd_sha = sha256(ROOT / "docs" / "PRD_ROOT.md")
    check(
        prd_sha == EXPECTED_PRD_SHA256,
        "prd_rev7_subject_parity",
        f"observed={prd_sha} expected={EXPECTED_PRD_SHA256}",
    )

    # Candidate folder contains exactly the three touched surfaces.
    names = sorted(p.name for p in CANDIDATE.iterdir())
    check(
        names == sorted([LEDGER, REGISTER, MAIN]),
        "candidate_file_set",
        f"observed={names}",
    )

    # ---- Scope ledger ----
    basis_raw = (DECOMP / LEDGER).read_bytes().decode("utf-8")
    cand_raw = (CANDIDATE / LEDGER).read_bytes().decode("utf-8")
    basis_lines = basis_raw.split("\r\n")
    cand_lines = cand_raw.split("\r\n")
    check(
        len(basis_lines) == len(cand_lines) == 106,
        "ledger_line_count",
        f"basis={len(basis_lines)} candidate={len(cand_lines)} (105 records + terminal empty)",
    )
    check(
        cand_raw.count("\r\n") == 105 and cand_raw.count("\n") == 105,
        "ledger_crlf_preserved",
        f"crlf={cand_raw.count(chr(13)+chr(10))} lf_total={cand_raw.count(chr(10))}",
    )
    diff_idx = [i for i, (a, b) in enumerate(zip(basis_lines, cand_lines)) if a != b]
    check(
        diff_idx == [42],
        "ledger_only_sow042_record_changed",
        f"changed_record_indexes={diff_idx} (0-based; 42 == file line 43)",
    )
    ledger_rows = read_rows(cand_raw)
    check(
        all(len(r) == 12 for r in ledger_rows),
        "ledger_column_count",
        f"rows={len(ledger_rows)} colcounts={sorted(set(len(r) for r in ledger_rows))}",
    )
    check(len(ledger_rows) == 105, "ledger_row_count", f"observed={len(ledger_rows)} expected=105 (header + 104)")
    ids = [r[0] for r in ledger_rows[1:]]
    check(len(ids) == len(set(ids)) == 104, "ledger_unique_scope_ids", f"scope_items={len(set(ids))}")
    statuses = [r[1] for r in ledger_rows[1:]]
    check(
        statuses.count("IN") == 95 and statuses.count("OUT") == 9 and statuses.count("TBD") == 0,
        "ledger_status_counts",
        f"IN={statuses.count('IN')} OUT={statuses.count('OUT')} TBD={statuses.count('TBD')}",
    )
    basis_sow042 = next(r for r in read_rows(basis_raw) if r and r[0] == "SOW-042")
    cand_sow042 = next(r for r in ledger_rows if r and r[0] == "SOW-042")
    preserved = [i for i in range(12) if i != 2]
    check(
        all(basis_sow042[i] == cand_sow042[i] for i in preserved),
        "sow042_only_statement_cell_changed",
        "columns 1,2,4..12 byte-equal to basis (SourceRef, mappings, D-8, flags preserved)",
    )
    statement = cand_sow042[2]
    missing = [t for t in REQUIRED_SOW042_TOKENS if t not in statement]
    check(not missing, "sow042_successor_policy_tokens", f"missing={missing}")
    check(
        not any(t in cand_raw.lower() for t in FORBIDDEN_OLD_TEXT),
        "ledger_old_text_absent",
        "no self-merge variant remains in the candidate ledger",
    )

    # ---- Deliverable register ----
    basis_reg_raw = (DECOMP / REGISTER).read_bytes().decode("utf-8")
    cand_reg_raw = (CANDIDATE / REGISTER).read_bytes().decode("utf-8")
    check("\r" not in cand_reg_raw, "register_lf_preserved", "no CR bytes in candidate register")
    basis_reg_lines = basis_reg_raw.split("\n")
    cand_reg_lines = cand_reg_raw.split("\n")
    check(
        len(basis_reg_lines) == len(cand_reg_lines) == 48,
        "register_line_count",
        f"basis={len(basis_reg_lines)} candidate={len(cand_reg_lines)} (47 records + terminal empty)",
    )
    reg_diff = [i for i, (a, b) in enumerate(zip(basis_reg_lines, cand_reg_lines)) if a != b]
    check(
        reg_diff == [26],
        "register_only_del0406_record_changed",
        f"changed_record_indexes={reg_diff} (0-based; 26 == file line 27)",
    )
    reg_rows = read_rows(cand_reg_raw)
    check(
        all(len(r) == 12 for r in reg_rows),
        "register_column_count",
        f"rows={len(reg_rows)} colcounts={sorted(set(len(r) for r in reg_rows))}",
    )
    check(len(reg_rows) == 47, "register_row_count", f"observed={len(reg_rows)} expected=47 (header + 46)")
    del_ids = [r[0] for r in reg_rows[1:]]
    check(len(del_ids) == len(set(del_ids)) == 46, "register_unique_deliverable_ids", f"deliverables={len(set(del_ids))}")
    basis_del = next(r for r in read_rows(basis_reg_raw) if r and r[0].startswith("DEL-04-06"))
    cand_del = next(r for r in reg_rows if r and r[0].startswith("DEL-04-06"))
    preserved_reg = [i for i in range(12) if i not in (5, 6)]
    check(
        all(basis_del[i] == cand_del[i] for i in preserved_reg),
        "del0406_only_description_and_artifacts_changed",
        "columns 1..5,8..12 byte-equal to basis (ID, package, owner, type, SOW/OBJ mapping, envelope preserved)",
    )
    desc_missing = [t for t in REQUIRED_DEL0406_DESC_TOKENS if t not in cand_del[5]]
    art_missing = [t for t in REQUIRED_DEL0406_ART_TOKENS if t not in cand_del[6]]
    check(not desc_missing, "del0406_description_tokens", f"missing={desc_missing}")
    check(not art_missing, "del0406_artifacts_tokens", f"missing={art_missing}")
    check(
        not any(t in cand_reg_raw.lower() for t in FORBIDDEN_OLD_TEXT),
        "register_old_text_absent",
        "no self-merge variant remains in the candidate register",
    )

    # ---- Cross-register lineage (unchanged by design) ----
    check(
        cand_sow042[4] == cand_del[2] == "PKG-04_Developmental_Machinery_and_Change_Control"
        and cand_sow042[5] == cand_del[0]
        and cand_del[7] == "SOW-042"
        and cand_sow042[6] == "OBJ-002"
        and "OBJ-002" in cand_del[8]
        and cand_sow042[7] == "D-8",
        "lineage_sow042_pkg04_del0406_obj002_d8",
        "SOW-042 -> PKG-04 -> DEL-04-06 -> OBJ-002 with D-8 linkage intact",
    )

    # ---- Working surface ----
    cand_md = (CANDIDATE / MAIN).read_bytes().decode("utf-8")
    basis_md = (DECOMP / MAIN).read_bytes().decode("utf-8")
    for token, name in [
        ("| DEC-023 | 2026-07-29 |", "md_dec023_present"),
        ("**SCA-002 revision 1.2 candidate.**", "md_changelog_entry_present"),
        ("`15fba9c36a197b36b281297af123115bcd3f282fe6c6f2fae05cd703b3743748` | `ea3db3607fbcbb7ce5f65bab31268a7eca431adb`", "md_ref001_rev7_pin"),
        ("**Revision:** v1.2 (SCA-002 candidate — not accepted)", "md_revision_marker"),
        ("| DEC-022 | 2026-07-26 |", "md_dec022_retained"),
        ("revision 1.1 remains the accepted basis", "md_predecessor_current_claim"),
    ]:
        check(token in cand_md, name, "token present" if token in cand_md else f"missing token: {token}")
    check(
        "self-merge" not in cand_md and "self-merge" not in basis_md,
        "md_no_literal_old_text",
        "neither basis nor candidate working surface carries the literal superseded phrase",
    )
    basis_md_lines = basis_md.split("\n")
    cand_md_lines = cand_md.split("\n")
    check(
        len(cand_md_lines) - len(basis_md_lines) == 18,
        "md_line_delta",
        f"basis={len(basis_md_lines)} candidate={len(cand_md_lines)} delta={len(cand_md_lines)-len(basis_md_lines)}",
    )
    for identifier in ("PKG-04_Developmental_Machinery_and_Change_Control", "DEL-04-06_Change_Management_and_Human_Gated_Closeout", "OBJ-002"):
        check(identifier in cand_md, f"md_identifier_retained::{identifier.split('_')[0]}", identifier)

    # ---- Verdict ----
    failures = [r for r in results if r["status"] == "FAIL"]
    report = {
        "amendment": "SCA-002",
        "gate": 3,
        "posture": "CANDIDATE_ONLY_OWNER_GATES_PENDING",
        "candidate_directory": str(CANDIDATE.relative_to(ROOT)),
        "frozen_basis": "main@ea3db3607fbcbb7ce5f65bab31268a7eca431adb",
        "result": "PASS" if not failures else "FAIL",
        "check_count": len(results),
        "failure_count": len(failures),
        "candidate_sha256": {name: sha256(CANDIDATE / name) for name in sorted([LEDGER, REGISTER, MAIN])},
        "basis_sha256": {name: sha256(DECOMP / name) for name in sorted([LEDGER, REGISTER, MAIN])},
        "checks": results,
    }
    REPORT.write_text(json.dumps(report, indent=1) + "\n", encoding="utf-8")
    print(f"{report['result']}: {len(results)} checks, {len(failures)} failures -> {REPORT.name}")
    if failures:
        for f in failures:
            print(f"  FAIL {f['check']}: {f['details']}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
