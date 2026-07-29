#!/usr/bin/env python3
"""Deterministically build the SCA-002 Gate 3 candidate from the frozen basis.

Reads the three touched authoritative decomposition surfaces at the frozen
basis (main@ea3db3607fbcbb7ce5f65bab31268a7eca431adb, the D-GOV-31 effective
merge) and writes candidate copies under Gate_3_Candidate/ with exactly the
SCA-002 amendment applied:

1. chirality_root_scope_ledger_v1_0.csv — the SOW-042 ScopeItemStatement is
   restated to the D-GOV-31 successor merge-gate policy. Every other cell,
   row, and the file's CRLF record terminators are byte-preserved.
2. chirality_root_deliverable_register_v1_0.csv — the DEL-04-06 Description
   and AnticipatedArtifacts cells are reconciled to the successor discipline.
   Every other cell, row, and the file's LF terminators are byte-preserved.
3. Chirality_Root_SOFTWARE_DECOMP_v1_0.md — header/revision metadata, the
   REF-001 sole-scope-source pin, the status banner, DEC-023, and one Change
   Log entry record the amendment; nothing else changes.

This script never writes to execution/_Decomposition/. The candidate is a
preview only; application is a later gated act after owner acceptance.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DECOMP = ROOT / "execution" / "_Decomposition"
SNAPSHOT = Path(__file__).resolve().parent
CANDIDATE = SNAPSHOT / "Gate_3_Candidate"

LEDGER = "chirality_root_scope_ledger_v1_0.csv"
REGISTER = "chirality_root_deliverable_register_v1_0.csv"
MAIN = "Chirality_Root_SOFTWARE_DECOMP_v1_0.md"

OLD_SOW042 = (
    "SOW-042,IN,Git closeout runs through the change-management role with "
    "human-gated pull requests and never self-merge.,"
    "PRD §5.3 D-8 [TRANSCRIBED],"
    "PKG-04_Developmental_Machinery_and_Change_Control,"
    "DEL-04-06_Change_Management_and_Human_Gated_Closeout,"
    "OBJ-002,D-8,DevelopmentalMachinery,,FALSE,\r\n"
)

NEW_SOW042 = (
    "SOW-042,IN,\"Git closeout in every registered loop runs through the "
    "shared change-management role with human-gated pull requests as the "
    "standing default; a bounded owner grant, recorded before or at exercise, "
    "may authorize merge execution under the merge-gate policy in PRD annex "
    "§5.3.1, which preserves K-MERGE-1 and the four closeout identities "
    "(semantic approval, approved source SHA, merge authorization, effective "
    "merge SHA). Each loop's stricter local merge discipline remains "
    "controlling until that loop adopts or acknowledges the policy under its "
    "own instruments.\","
    "PRD §5.3 D-8 [TRANSCRIBED],"
    "PKG-04_Developmental_Machinery_and_Change_Control,"
    "DEL-04-06_Change_Management_and_Human_Gated_Closeout,"
    "OBJ-002,D-8,DevelopmentalMachinery,,FALSE,\r\n"
)

OLD_DEL0406 = (
    "DEL-04-06_Change_Management_and_Human_Gated_Closeout,"
    "Change Management and Human-Gated Closeout,"
    "PKG-04_Developmental_Machinery_and_Change_Control,"
    "Ryan Tufts,CI_CD_CHANGE,"
    "Keep git closeout running through the change-management role with "
    "human-gated pull requests and no self-merge.,"
    "Closeout checklist; no-self-merge evidence; PR gate notes,"
    "SOW-042,OBJ-002,S,One narrow procedural control.,execution-tree\n"
)

NEW_DEL0406 = (
    "DEL-04-06_Change_Management_and_Human_Gated_Closeout,"
    "Change Management and Human-Gated Closeout,"
    "PKG-04_Developmental_Machinery_and_Change_Control,"
    "Ryan Tufts,CI_CD_CHANGE,"
    "\"Keep git closeout running through the shared change-management role "
    "with human-gated pull requests as the standing default; preserve "
    "K-MERGE-1 and the four closeout identities (semantic approval, approved "
    "source SHA, merge authorization, effective merge SHA) in every closeout; "
    "a bounded owner grant recorded per PRD annex §5.3.1 before or at "
    "exercise may authorize merge execution within its recorded scope and "
    "term.\","
    "\"Closeout checklist; four-identity closeout evidence (semantic "
    "approval, approved source SHA, merge authorization, effective merge "
    "SHA); bounded-owner-grant records when a grant is exercised; PR gate "
    "notes\","
    "SOW-042,OBJ-002,S,One narrow procedural control.,execution-tree\n"
)

MD_EDITS = [
    # 1. Title line.
    (
        "# Chirality Root — Software Decomposition (SCA-001 SUCCESSOR v1.1)\n",
        "# Chirality Root — Software Decomposition (SCA-002 CANDIDATE v1.2)\n",
    ),
    # 2. Header metadata block.
    (
        "**Revision:** v1.1 · **Date:** 2026-07-26\n"
        "**Source-basis commit:** `fb0b3d247d32e643a7fbb994d2f61b9b673ad0fb` (D-GOV-28 EffectiveSHA)\n"
        "**Predecessor AcceptedCandidateSHA:** `ec62af0700e530c1640698fa406398cb1cb45d29`\n"
        "**Predecessor EffectiveSHA:** `ea0ad7a566ddb51d89297bfcf491636f1fc5dd15` (merge of PR #347)\n"
        "**Predecessor accepting instrument:** `docs/governance_harness/_DECISIONS/D-GOV-25_root_decomposition_acceptance.md`\n"
        "**Run:** `ROOT-STEP8-DECOMP-20260725`, node N1\n"
        "**Amendment:** `SCA-001`; Gate 3 exact text approved and Gate 5 current-basis confirmation required before successor effect\n",
        "**Revision:** v1.2 (SCA-002 candidate — not accepted) · **Date:** 2026-07-29\n"
        "**Source-basis commit:** `ea3db3607fbcbb7ce5f65bab31268a7eca431adb` (D-GOV-31 effective merge; PRD Revision 7)\n"
        "**Predecessor (v1.1):** accepted by the SCA-001 Gate 5 owner confirmation, 2026-07-26; Git effect PR #366 merge `2db2c7128c32d32d197ae47660eb34ab2cef9660`\n"
        "**v1.0 acceptance:** AcceptedCandidateSHA `ec62af0700e530c1640698fa406398cb1cb45d29`; EffectiveSHA `ea0ad7a566ddb51d89297bfcf491636f1fc5dd15` (merge of PR #347); instrument `docs/governance_harness/_DECISIONS/D-GOV-25_root_decomposition_acceptance.md`\n"
        "**Run:** `GOV-STEP4-SCA-20260729` (SCA-002 drafting); origin run `ROOT-STEP8-DECOMP-20260725`, node N1\n"
        "**Amendment:** `SCA-002`; candidate only — all five SCOPE_CHANGE owner gates pending; revision 1.1 remains the accepted basis\n",
    ),
    # 3. Status banner.
    (
        "> **Status: SCA-001 SUCCESSOR — conditional current basis.** The v1.0\n"
        "> predecessor remains the accepted basis until the owner confirms the SCA-001\n"
        "> Gate 5 post-change state. Upon that confirmation, these exact v1.1 bytes are\n"
        "> the current accepted decomposition basis. The confirmation and all five\n"
        "> SCOPE_CHANGE gates are recorded in\n"
        "> `execution/_ScopeChange/SCA-001_2026-07-26_1454/Decision_Log.md`.\n"
        ">\n"
        "> **What the amendment does not do.** It authorizes no `runtime/` edit,\n"
        "> implementation, client change, package dispatch, or release. It adds one\n"
        "> Root-owned standing scope carrier and planning locus. Materialization and\n"
        "> guard-state refresh remain downstream PROJECT_SETUP work.\n"
        ">\n"
        "> **Predecessor acceptance.** D-GOV-25 continues to identify and govern the\n"
        "> accepted v1.0 predecessor at its exact candidate and effective SHAs. SCA-001\n"
        "> changes no historical ruling and reuses no stable ID.\n",
        "> **Status: SCA-002 CANDIDATE — not the accepted basis.** Revision 1.1\n"
        "> (SCA-001 successor, owner-confirmed 2026-07-26) remains the accepted\n"
        "> current basis. These v1.2 bytes exist only inside the SCA-002 snapshot\n"
        "> and become the current basis only upon the SCA-002 owner gate\n"
        "> confirmations recorded in\n"
        "> `execution/_ScopeChange/SCA-002_2026-07-29_0800/Decision_Log.md`,\n"
        "> followed by a separately gated application act. No owner acceptance of\n"
        "> SCA-002 has occurred at drafting time.\n"
        ">\n"
        "> **What the amendment does.** It restates the SOW-042 scope-ledger row\n"
        "> and the DEL-04-06 deliverable-register row from the superseded Rev 6\n"
        "> D-8 wording to the D-GOV-31 successor merge-gate policy (PRD Revision 7\n"
        "> row D-8 and annex §5.3.1), and advances the sole-scope-source pin to\n"
        "> Revision 7. No ID, status, mapping, package, deliverable, objective,\n"
        "> count, or topology changes; no grant is issued; no historical record is\n"
        "> rewritten.\n"
        ">\n"
        "> **Predecessor acceptance.** D-GOV-25 (v1.0) and the SCA-001 Gate 5\n"
        "> confirmation (v1.1) continue to identify and govern their accepted\n"
        "> states. SCA-002 changes no historical ruling and reuses no stable ID.\n",
    ),
    # 4. REF-001 sole-scope-source pin.
    (
        "| `0e36a03abc16b86f99024aa2a17c467ae7f4303f9740be3a6ba2e9dd1dfb2f2d` | `fb0b3d247d32e643a7fbb994d2f61b9b673ad0fb` (D-GOV-28 EffectiveSHA) |",
        "| `15fba9c36a197b36b281297af123115bcd3f282fe6c6f2fae05cd703b3743748` | `ea3db3607fbcbb7ce5f65bab31268a7eca431adb` (D-GOV-31 effective merge; PRD Revision 7) |",
    ),
    # 5. DEC-023 appended after the DEC-022 block.
    (
        "Requested by Ryan Tufts and approved through SCA-001 Gates 2–3. |\n"
        "\n"
        "### Change Log\n",
        "Requested by Ryan Tufts and approved through SCA-001 Gates 2–3. |\n"
        "\n"
        "| DEC-023 | 2026-07-29 | **SCA-002 restates SOW-042 and DEL-04-06 to the D-GOV-31 successor merge-gate policy.** The SOW-042 `ScopeItemStatement` and the DEL-04-06 `Description` and `AnticipatedArtifacts` cells are restated from the superseded Rev 6 D-8 wording to the adopted successor: the shared change-management role with human-gated PRs as the standing default; a bounded owner grant, recorded before or at exercise per PRD annex §5.3.1, may authorize merge execution; K-MERGE-1 and the four closeout identities (semantic approval, approved source SHA, merge authorization, effective merge SHA) are preserved; each loop's stricter local merge discipline remains controlling until adopted under its own instruments. The SOW-042 `SourceRef` bracket retains its historical `[TRANSCRIBED]` label per the drafting brief; the live D-8 row is labeled PROPOSED (Rev 7), and the label disposition is surfaced to the owner in the SCA-002 snapshot rather than changed here (F6 discipline). No ID, status, mapping, count, or other cell changes. | D-GOV-31 adopted PRD Revision 7 (subject SHA-256 `15fba9c36a197b36b281297af123115bcd3f282fe6c6f2fae05cd703b3743748`; effective merge `ea3db3607fbcbb7ce5f65bab31268a7eca431adb`); its POLICY_DELTA §4 row 1 obligates this restatement through SCOPE_CHANGE. Candidate only: these bytes take effect only upon the SCA-002 owner gate confirmations. Owner acceptance is pending and is a separate act. |\n"
        "\n"
        "### Change Log\n",
    ),
    # 6. Change Log entry appended after the SCA-001 entry.
    (
        "  current basis only upon the SCA-001 Gate 5 owner confirmation.\n"
        "\n"
        "---\n"
        "\n"
        "## 14. Downstream Execution Notes\n",
        "  current basis only upon the SCA-001 Gate 5 owner confirmation.\n"
        "\n"
        "- 2026-07-29 — **SCA-002 revision 1.2 candidate.** D-GOV-31 adopted PRD\n"
        "  Revision 7: the D-8 successor row and merge-gate policy annex §5.3.1\n"
        "  (shared change-management role; human-gated PRs as the standing default;\n"
        "  bounded owner grants recorded before or at exercise; K-MERGE-1 and the\n"
        "  four closeout identities preserved). This candidate restates SOW-042\n"
        "  (scope ledger) and DEL-04-06 (deliverable register) to the successor\n"
        "  policy and advances the sole-scope-source pin to Revision 7 at the\n"
        "  D-GOV-31 effective merge (DEC-023). No topology, ID, status, mapping,\n"
        "  or count changes; no grant is issued; frozen records are untouched.\n"
        "  These bytes become the current basis only upon the SCA-002 owner gate\n"
        "  confirmations; revision 1.1 remains the accepted basis until then.\n"
        "\n"
        "---\n"
        "\n"
        "## 14. Downstream Execution Notes\n",
    ),
]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"FATAL: expected exactly 1 occurrence for {label}, found {count}")
    return text.replace(old, new, 1)


def main() -> None:
    CANDIDATE.mkdir(parents=True, exist_ok=True)

    ledger = (DECOMP / LEDGER).read_bytes().decode("utf-8")
    ledger_new = replace_once(ledger, OLD_SOW042, NEW_SOW042, "SOW-042 row")
    (CANDIDATE / LEDGER).write_bytes(ledger_new.encode("utf-8"))

    register = (DECOMP / REGISTER).read_bytes().decode("utf-8")
    register_new = replace_once(register, OLD_DEL0406, NEW_DEL0406, "DEL-04-06 row")
    (CANDIDATE / REGISTER).write_bytes(register_new.encode("utf-8"))

    main_doc = (DECOMP / MAIN).read_bytes().decode("utf-8")
    for index, (old, new) in enumerate(MD_EDITS, start=1):
        main_doc = replace_once(main_doc, old, new, f"MD edit {index}")
    (CANDIDATE / MAIN).write_bytes(main_doc.encode("utf-8"))

    for name in (MAIN, LEDGER, REGISTER):
        basis = sha256((DECOMP / name).read_bytes())
        cand = sha256((CANDIDATE / name).read_bytes())
        print(f"{name}\n  basis     {basis}\n  candidate {cand}")


if __name__ == "__main__":
    main()
