#!/usr/bin/env python3
"""Deterministic SCA-002 Gate 5 applied-state validation.

Read-only over the LIVE authoritative surfaces under execution/_Decomposition/.
Re-runs the package's Gate 3 deterministic checks against the applied files,
adapted for exactly one owner-ruled application delta: the SOW-042 `SourceRef`
bracket, changed at application per the owner's 2026-07-29 bracket ruling
("BRACKET AS RECOMMENDED: at application, update SOW-042 SourceRef to cite
D-GOV-31 adoption") from `PRD §5.3 D-8 [TRANSCRIBED]` to
`PRD §5.3 D-8 [ADOPTED-D-GOV-31]`. Every other applied byte must equal the
owner-accepted Gate 3 candidate bytes. Writes Gate_5_Validation.json. Never
mutates an input.
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
REPORT = SNAPSHOT / "Gate_5_Validation.json"

LEDGER = "chirality_root_scope_ledger_v1_0.csv"
REGISTER = "chirality_root_deliverable_register_v1_0.csv"
MAIN = "Chirality_Root_SOFTWARE_DECOMP_v1_0.md"

# Owner-accepted Gate 3 candidate identities (Gate_3_Validation.json).
EXPECTED_CANDIDATE_SHA256 = {
    MAIN: "6f43f3fbc25e0663697464a7a20f3b1bac4b731b01efbe473642e238b93a4d49",
    LEDGER: "61992b3c43da62f4ecbb1f43bab4d1c62835be19102763645f2418abe6b478d7",
    REGISTER: "b18ebe6b9bc3cdac6bd0bd78f6470be328a81783c7c6ab5b55478b506c61e8da",
}
EXPECTED_PRD_SHA256 = (
    "15fba9c36a197b36b281297af123115bcd3f282fe6c6f2fae05cd703b3743748"
)

# The single owner-ruled application delta (owner bracket ruling, 2026-07-29).
CANDIDATE_SOURCEREF = "PRD §5.3 D-8 [TRANSCRIBED]"
APPLIED_SOURCEREF = "PRD §5.3 D-8 [ADOPTED-D-GOV-31]"

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

    # Frozen candidate integrity: the accepted Gate 3 bytes are unchanged.
    for name, expected in EXPECTED_CANDIDATE_SHA256.items():
        observed = sha256(CANDIDATE / name)
        check(
            observed == expected,
            f"candidate_frozen::{name}",
            f"observed={observed} expected={expected}",
        )

    # The live PRD remains the adopted D-GOV-31 Rev 7 subject.
    prd_sha = sha256(ROOT / "docs" / "PRD_ROOT.md")
    check(
        prd_sha == EXPECTED_PRD_SHA256,
        "prd_rev7_subject_parity",
        f"observed={prd_sha} expected={EXPECTED_PRD_SHA256}",
    )

    # Exact-byte application: working surface and deliverable register are
    # byte-identical to the accepted candidate.
    for name in (MAIN, REGISTER):
        live_sha = sha256(DECOMP / name)
        check(
            live_sha == EXPECTED_CANDIDATE_SHA256[name],
            f"applied_exact_candidate::{name}",
            f"live={live_sha} candidate={EXPECTED_CANDIDATE_SHA256[name]}",
        )

    # ---- Scope ledger: candidate bytes plus exactly the owner bracket delta ----
    live_raw = (DECOMP / LEDGER).read_bytes().decode("utf-8")
    cand_raw = (CANDIDATE / LEDGER).read_bytes().decode("utf-8")
    live_lines = live_raw.split("\r\n")
    cand_lines = cand_raw.split("\r\n")
    check(
        len(live_lines) == len(cand_lines) == 106,
        "ledger_line_count",
        f"live={len(live_lines)} candidate={len(cand_lines)} (105 records + terminal empty)",
    )
    check(
        live_raw.count("\r\n") == 105 and live_raw.count("\n") == 105,
        "ledger_crlf_preserved",
        f"crlf={live_raw.count(chr(13)+chr(10))} lf_total={live_raw.count(chr(10))}",
    )
    diff_idx = [i for i, (a, b) in enumerate(zip(cand_lines, live_lines)) if a != b]
    check(
        diff_idx == [42],
        "ledger_only_sow042_record_differs_from_candidate",
        f"differing_record_indexes={diff_idx} (0-based; 42 == file line 43)",
    )
    ledger_rows = read_rows(live_raw)
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
    cand_sow042 = next(r for r in read_rows(cand_raw) if r and r[0] == "SOW-042")
    live_sow042 = next(r for r in ledger_rows if r and r[0] == "SOW-042")
    preserved = [i for i in range(12) if i != 3]
    check(
        all(cand_sow042[i] == live_sow042[i] for i in preserved),
        "sow042_only_sourceref_cell_differs_from_candidate",
        "columns 1..3,5..12 byte-equal to the accepted candidate (statement, mappings, D-8, flags preserved)",
    )
    check(
        cand_sow042[3] == CANDIDATE_SOURCEREF,
        "sow042_candidate_sourceref_identity",
        f"candidate={cand_sow042[3]!r} expected={CANDIDATE_SOURCEREF!r}",
    )
    check(
        live_sow042[3] == APPLIED_SOURCEREF,
        "sow042_applied_sourceref_owner_bracket_ruling",
        f"live={live_sow042[3]!r} expected={APPLIED_SOURCEREF!r} (owner bracket ruling 2026-07-29)",
    )
    statement = live_sow042[2]
    missing = [t for t in REQUIRED_SOW042_TOKENS if t not in statement]
    check(not missing, "sow042_successor_policy_tokens", f"missing={missing}")
    check(
        not any(t in live_raw.lower() for t in FORBIDDEN_OLD_TEXT),
        "ledger_old_text_absent",
        "no self-merge variant remains in the applied ledger",
    )

    # ---- Deliverable register (byte-identical to candidate; content checks) ----
    live_reg_raw = (DECOMP / REGISTER).read_bytes().decode("utf-8")
    check("\r" not in live_reg_raw, "register_lf_preserved", "no CR bytes in applied register")
    reg_rows = read_rows(live_reg_raw)
    check(len(reg_rows) == 47, "register_row_count", f"observed={len(reg_rows)} expected=47 (header + 46)")
    del_ids = [r[0] for r in reg_rows[1:]]
    check(len(del_ids) == len(set(del_ids)) == 46, "register_unique_deliverable_ids", f"deliverables={len(set(del_ids))}")
    live_del = next(r for r in reg_rows if r and r[0].startswith("DEL-04-06"))
    desc_missing = [t for t in REQUIRED_DEL0406_DESC_TOKENS if t not in live_del[5]]
    art_missing = [t for t in REQUIRED_DEL0406_ART_TOKENS if t not in live_del[6]]
    check(not desc_missing, "del0406_description_tokens", f"missing={desc_missing}")
    check(not art_missing, "del0406_artifacts_tokens", f"missing={art_missing}")
    check(
        not any(t in live_reg_raw.lower() for t in FORBIDDEN_OLD_TEXT),
        "register_old_text_absent",
        "no self-merge variant remains in the applied register",
    )

    # ---- Cross-register lineage (unchanged by design) ----
    check(
        live_sow042[4] == live_del[2] == "PKG-04_Developmental_Machinery_and_Change_Control"
        and live_sow042[5] == live_del[0]
        and live_del[7] == "SOW-042"
        and live_sow042[6] == "OBJ-002"
        and "OBJ-002" in live_del[8]
        and live_sow042[7] == "D-8",
        "lineage_sow042_pkg04_del0406_obj002_d8",
        "SOW-042 -> PKG-04 -> DEL-04-06 -> OBJ-002 with D-8 linkage intact",
    )

    # ---- Working surface (byte-identical to candidate; token checks) ----
    live_md = (DECOMP / MAIN).read_bytes().decode("utf-8")
    for token, name in [
        ("| DEC-023 | 2026-07-29 |", "md_dec023_present"),
        ("**SCA-002 revision 1.2 candidate.**", "md_changelog_entry_present"),
        ("`15fba9c36a197b36b281297af123115bcd3f282fe6c6f2fae05cd703b3743748` | `ea3db3607fbcbb7ce5f65bab31268a7eca431adb`", "md_ref001_rev7_pin"),
        ("| DEC-022 | 2026-07-26 |", "md_dec022_retained"),
    ]:
        check(token in live_md, name, "token present" if token in live_md else f"missing token: {token}")
    check(
        "self-merge" not in live_md,
        "md_no_literal_old_text",
        "the applied working surface carries no literal superseded phrase",
    )
    for identifier in ("PKG-04_Developmental_Machinery_and_Change_Control", "DEL-04-06_Change_Management_and_Human_Gated_Closeout", "OBJ-002"):
        check(identifier in live_md, f"md_identifier_retained::{identifier.split('_')[0]}", identifier)

    # ---- Verdict ----
    failures = [r for r in results if r["status"] == "FAIL"]
    report = {
        "amendment": "SCA-002",
        "gate": 5,
        "posture": "APPLIED_WITH_OWNER_RULED_BRACKET_DELTA",
        "acceptance_act": "ACCEPT SCA-002 271d456a — Ryan Tufts 2026-07-29",
        "bracket_ruling_act": (
            "BRACKET AS RECOMMENDED: at application, update SOW-042 SourceRef "
            "to cite D-GOV-31 adoption — Ryan Tufts 2026-07-29"
        ),
        "application_basis": "main@204321467b567ede862636a36dd67bcac1ff326a",
        "result": "PASS" if not failures else "FAIL",
        "check_count": len(results),
        "failure_count": len(failures),
        "applied_sha256": {name: sha256(DECOMP / name) for name in sorted([LEDGER, REGISTER, MAIN])},
        "candidate_sha256": {name: sha256(CANDIDATE / name) for name in sorted([LEDGER, REGISTER, MAIN])},
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
