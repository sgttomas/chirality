#!/usr/bin/env python3
"""Build the SCA-001 Gate 3 candidate without touching decomposition truth."""

from __future__ import annotations

import csv
import difflib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DECOMP = ROOT / "execution" / "_Decomposition"
SNAPSHOT = Path(__file__).resolve().parent
CANDIDATE = SNAPSHOT / "Gate_3_Candidate"

MAIN = "Chirality_Root_SOFTWARE_DECOMP_v1_0.md"
SCOPE = "chirality_root_scope_ledger_v1_0.csv"
DELIVERABLES = "chirality_root_deliverable_register_v1_0.csv"
OBJECTIVES = "chirality_root_objective_register_v1_0.csv"
FORWARD = "chirality_root_prd_coverage_forward_v1_0.csv"
REVERSE = "chirality_root_trace_reverse_v1_0.csv"
TELEMETRY = "chirality_root_coverage_telemetry_v1_0.md"
FILES = [MAIN, SCOPE, DELIVERABLES, OBJECTIVES, FORWARD, REVERSE, TELEMETRY]

PKG = "PKG-02_Operative_Instruction_Surface_and_Runtime_Layers"
DEL = "DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance"
SOW = "SOW-104"
OBJECTIVE_IDS = ["OBJ-001", "OBJ-002", "OBJ-004", "OBJ-007"]


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"expected one occurrence, found {count}: {old[:100]!r}")
    return text.replace(old, new, 1)


def replace_line(text: str, prefix: str, new_line: str) -> str:
    lines = text.splitlines()
    matches = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    if len(matches) != 1:
        raise RuntimeError(f"expected one line with prefix {prefix!r}, found {len(matches)}")
    lines[matches[0]] = new_line
    return "\n".join(lines) + "\n"


def append_semicolon(value: str, addition: str) -> str:
    parts = value.split(";") if value else []
    if addition not in parts:
        parts.append(addition)
    return ";".join(parts)


def add_sorted_semicolon(value: str, addition: str) -> str:
    parts = {part for part in value.split(";") if part} if value else set()
    parts.add(addition)
    return ";".join(sorted(parts))


def read_csv(name: str) -> tuple[list[str], list[dict[str, str]], str]:
    raw = (DECOMP / name).read_bytes()
    line_ending = "\r\n" if b"\r\n" in raw else "\n"
    with (DECOMP / name).open(newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader), line_ending


def write_csv(name: str, fields: list[str], rows: list[dict[str, str]], line_ending: str) -> None:
    with (CANDIDATE / name).open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator=line_ending)
        writer.writeheader()
        writer.writerows(rows)


def build_scope() -> None:
    fields, rows, line_ending = read_csv(SCOPE)
    rows.append(
        {
            "ScopeItemID": SOW,
            "InOutStatus": "IN",
            "ScopeItemStatement": (
                "Consequential work on generic runtime semantics uses a Root-owned standing "
                "scope carrier and declared runtime write locus; preserves the authority, "
                "security, residency, exclusion, and implementation-gate boundaries ruled "
                "by D-GOV-20; produces versioned-contract, affected-client conformance or "
                "migration, and proportionate regression evidence; returns release "
                "disposition to an accountable human; and does not transfer generic runtime "
                "ownership to App, PEC, or another client."
            ),
            "SourceRef": "PRD §5.2 O-11 [PROPOSED-origin; adopted D-GOV-28]",
            "PackageID": PKG,
            "DeliverableIDs": DEL,
            "ObjectiveIDs": ";".join(OBJECTIVE_IDS),
            "PRDItem": "O-11",
            "Categories": "OperativeProduct;Evidence",
            "DecisionRef": "DEC-022",
            "OpenIssue": "FALSE",
            "Notes": (
                "Standing carrier activated one bounded runtime-change tranche at a time. "
                "D-GOV-20 remains the ruled architectural basis; D-T0-23 is a coordinating "
                "Tier-0 counterpart, not a Root scope source. O-11 is in effect through "
                "D-GOV-28."
            ),
        }
    )
    write_csv(SCOPE, fields, rows, line_ending)


def build_deliverables() -> None:
    fields, rows, line_ending = read_csv(DELIVERABLES)
    new_row = {
        "DeliverableID": DEL,
        "Name": "Generic Runtime Stewardship and Release Assurance",
        "ParentPackageID": PKG,
        "ResponsibleParty": "Ryan Tufts",
        "Type": "REQ_SLICE",
        "Description": (
            "Provide the standing Root carrier for consequential generic runtime semantic "
            "changes: preserve the D-GOV-20 boundary, produce versioned-contract and "
            "affected-client conformance or migration plus proportionate regression "
            "evidence, and return release disposition to an accountable human without "
            "transferring generic runtime ownership to a client."
        ),
        "AnticipatedArtifacts": (
            "Runtime change brief and declared write-locus record; versioned-contract delta "
            "or no-change record; affected-client conformance or migration matrix; "
            "proportionate regression evidence bundle; accountable-human release disposition"
        ),
        "CoversScopeItems": SOW,
        "SupportsObjectives": ";".join(OBJECTIVE_IDS),
        "ContextEnvelope": "M",
        "ContextEnvelopeNotes": (
            "One bounded runtime semantic-change tranche and its affected-client evidence; "
            "split the activation if implementation or client breadth would exceed M."
        ),
        "AnticipatedWriteLocus": (
            "runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/**; "
            "client implementation only through separately authorized client-owned tranches"
        ),
    }
    index = next(i for i, row in enumerate(rows) if row["DeliverableID"].startswith("DEL-02-05_"))
    rows.insert(index + 1, new_row)
    write_csv(DELIVERABLES, fields, rows, line_ending)


def build_objectives() -> None:
    fields, rows, line_ending = read_csv(OBJECTIVES)
    for row in rows:
        if row["ObjectiveID"] in OBJECTIVE_IDS:
            row["MappedDeliverables"] = add_sorted_semicolon(row["MappedDeliverables"], DEL)
            row["MappedScopeItems"] = add_sorted_semicolon(row["MappedScopeItems"], SOW)
    write_csv(OBJECTIVES, fields, rows, line_ending)


def build_forward() -> None:
    fields, rows, line_ending = read_csv(FORWARD)
    for row in rows:
        if row["ObjectiveID"] in OBJECTIVE_IDS:
            row["ScopeItemIDs"] = add_sorted_semicolon(row["ScopeItemIDs"], SOW)
            row["PackageIDs"] = add_sorted_semicolon(row["PackageIDs"], PKG)
            row["DeliverableIDs"] = add_sorted_semicolon(row["DeliverableIDs"], DEL)
    new_row = {
        "PRDItem": "O-11",
        "ItemKind": "commitment",
        "PRDSection": "§5.2",
        "ObjectiveID": "",
        "ScopeItemIDs": SOW,
        "PackageIDs": PKG,
        "DeliverableIDs": DEL,
        "CoverageStatus": "COVERED",
        "DeferralReason": "",
    }
    index = next(i for i, row in enumerate(rows) if row["PRDItem"] == "O-10")
    rows.insert(index + 1, new_row)
    write_csv(FORWARD, fields, rows, line_ending)


def build_reverse() -> None:
    fields, rows, line_ending = read_csv(REVERSE)
    for row in rows:
        if row["UnitID"] == PKG:
            row["PRDItems"] = add_sorted_semicolon(row["PRDItems"], "O-11")
            row["ScopeItemIDs"] = add_sorted_semicolon(row["ScopeItemIDs"], SOW)
    new_row = {
        "UnitID": DEL,
        "UnitKind": "deliverable",
        "ParentPackageID": PKG,
        "PRDItems": "O-11;OBJ-1;OBJ-2;OBJ-4;OBJ-7",
        "ScopeItemIDs": SOW,
        "TraceStatus": "TRACED",
    }
    index = next(i for i, row in enumerate(rows) if row["UnitID"].startswith("DEL-02-05_"))
    rows.insert(index + 1, new_row)
    write_csv(REVERSE, fields, rows, line_ending)


def build_main() -> None:
    text = (DECOMP / MAIN).read_text()
    text = replace_once(
        text,
        "# Chirality Root — Software Decomposition (ACCEPTED v1.0)",
        "# Chirality Root — Software Decomposition (SCA-001 SUCCESSOR v1.1)",
    )
    text = replace_once(text, "**Revision:** v1.0 · **Date:** 2026-07-25", "**Revision:** v1.1 · **Date:** 2026-07-26")
    text = replace_once(
        text,
        "**Basis commit:** `24726a73c64a849909e3615c32ef1a888b3dfd36`",
        "**Source-basis commit:** `fb0b3d247d32e643a7fbb994d2f61b9b673ad0fb` (D-GOV-28 EffectiveSHA)",
    )
    text = replace_once(text, "**AcceptedCandidateSHA:**", "**Predecessor AcceptedCandidateSHA:**")
    text = replace_once(text, "**EffectiveSHA:**", "**Predecessor EffectiveSHA:**")
    text = replace_once(text, "**Accepting instrument:**", "**Predecessor accepting instrument:**")
    text = replace_once(
        text,
        "**Run:** `ROOT-STEP8-DECOMP-20260725`, node N1",
        "**Run:** `ROOT-STEP8-DECOMP-20260725`, node N1\n"
        "**Amendment:** `SCA-001`; Gate 3 exact text approved and Gate 5 current-basis "
        "confirmation required before successor effect",
    )
    status_start = text.index("> **Status: ACCEPTED")
    status_end = text.index("\n---", status_start)
    text = (
        text[:status_start]
        + "> **Status: SCA-001 SUCCESSOR — conditional current basis.** The v1.0\n"
        + "> predecessor remains the accepted basis until the owner confirms the SCA-001\n"
        + "> Gate 5 post-change state. Upon that confirmation, these exact v1.1 bytes are\n"
        + "> the current accepted decomposition basis. The confirmation and all five\n"
        + "> SCOPE_CHANGE gates are recorded in\n"
        + "> `execution/_ScopeChange/SCA-001_2026-07-26_1454/Decision_Log.md`.\n"
        + ">\n"
        + "> **What the amendment does not do.** It authorizes no `runtime/` edit,\n"
        + "> implementation, client change, package dispatch, or release. It adds one\n"
        + "> Root-owned standing scope carrier and planning locus. Materialization and\n"
        + "> guard-state refresh remain downstream PROJECT_SETUP work.\n"
        + ">\n"
        + "> **Predecessor acceptance.** D-GOV-25 continues to identify and govern the\n"
        + "> accepted v1.0 predecessor at its exact candidate and effective SHAs. SCA-001\n"
        + "> changes no historical ruling and reuses no stable ID.\n"
        + text[status_end:]
    )
    text = replace_once(
        text,
        "| REF-001 | `docs/PRD_ROOT.md` | **Sole scope source.** Objectives (§3), categories (§4), stable commitments (§5), self-application direction (§6), variant and promotion direction (§7), non-goals and falsifiers (§8), ruled owner decisions (§9), source-concordance obligations (§10). | `e98031c14b4c6c9b2602545e6f80abd5019ead0af1ff460b3e4ea26135bb63eb` | `24726a73c64a849909e3615c32ef1a888b3dfd36` |",
        "| REF-001 | `docs/PRD_ROOT.md` | **Sole scope source.** Objectives (§3), categories (§4), stable commitments (§5), including O-11 continuing Root stewardship of generic runtime, self-application direction (§6), variant and promotion direction (§7), non-goals and falsifiers (§8), ruled owner decisions (§9), source-concordance obligations (§10). | `0e36a03abc16b86f99024aa2a17c467ae7f4303f9740be3a6ba2e9dd1dfb2f2d` | `fb0b3d247d32e643a7fbb994d2f61b9b673ad0fb` (D-GOV-28 EffectiveSHA) |",
    )
    text = replace_once(
        text,
        "The PRD carries **7 objectives**, **42 stable commitments** (9 normative-basis\n`N-*`, 10 operative `O-*`, 15 developmental `D-*` with `D-3` retired and never",
        "The PRD carries **7 objectives**, **43 stable commitments** (9 normative-basis\n`N-*`, 11 operative `O-*`, 15 developmental `D-*` with `D-3` retired and never",
    )
    text = replace_once(
        text,
        "- **Nothing is accepted here.** All seven gates are human-gated (I1); this run\n  rules on none of them.",
        "- **The original seven decomposition gates are accepted under D-GOV-25.** This\n  amendment uses SCOPE_CHANGE's five separately human-gated decisions; no stage\n  self-accepts.",
    )
    text = replace_once(
        text,
        "- **This candidate creates no `PKG-*` or `DEL-*` directory**, writes nothing to",
        "- **This decomposition amendment creates no `PKG-*` or `DEL-*` directory**, writes nothing to",
    )
    text = replace_once(text, "**Declared but unused in v1.0**", "**Declared but unused in v1.1**")
    text = replace_once(
        text,
        "The SSOW is **103 atomic scope items** (`SOW-001`..`SOW-103`), normalized from",
        "The SSOW is **104 atomic scope items** (`SOW-001`..`SOW-104`), normalized from",
    )
    text = replace_once(text, "| `IN` | 94 |", "| `IN` | 95 |")
    text = replace_once(
        text,
        "§5.3 (16), §5.4 (8), §6 (7), §7 (7), §8 (14), §9 (10), §10 (7) — total 103.",
        "§5.3 (16), §5.4 (8), §6 (7), §7 (7), §8 (14), §9 (10), §10 (7) — total 104.",
    )
    text = replace_once(text, "§5.1 (12), §5.2 (10),", "§5.1 (12), §5.2 (11),")
    objective_rows = {
        "| OBJ-001 |": "| OBJ-001 | OBJ-1 | Coherent and discoverable normative authority — a reader can determine what governs, from the repository alone. | DEL-01-01, DEL-01-02, DEL-01-03, DEL-01-07, DEL-01-08, DEL-02-01, DEL-02-05, DEL-02-06, DEL-04-07, DEL-04-09 |",
        "| OBJ-002 |": "| OBJ-002 | OBJ-2 | Governed production of professional knowledge work — the product carries work to an issuance decision that an accountable human makes. | DEL-01-04, DEL-01-06, DEL-02-02, DEL-02-03, DEL-02-06, DEL-03-02, DEL-03-06, DEL-04-02, DEL-04-06 |",
        "| OBJ-004 |": "| OBJ-004 | OBJ-4 | Safe self-application without self-authorization — F1–F3 unobserved, capabilities accepted before consumption, guards registered and passing. | DEL-02-04, DEL-02-06, DEL-03-01, DEL-03-04, DEL-03-05, DEL-03-06, DEL-05-06, DEL-06-01, DEL-06-04, DEL-06-07 |",
        "| OBJ-007 |": "| OBJ-007 | OBJ-7 | File-native continuity and recoverability — nothing load-bearing lives outside the checkout. | DEL-01-05, DEL-02-06, DEL-03-01 |",
    }
    for prefix, row in objective_rows.items():
        text = replace_line(text, prefix, row)
    text = replace_once(
        text,
        "declared write scope and capability-boundary controls, and live registry discipline.",
        "declared write scope and capability-boundary controls, live registry discipline, "
        "and continuing stewardship and release assurance for the Root-owned generic runtime.",
    )
    text = replace_once(
        text,
        "45 deliverables, each belonging to exactly one package, each sized for a\nbounded Agent 2 execution. `ResponsibleParty` is `TBD` for every deliverable —\nthis run holds no assignment authority (OI-011).",
        "46 deliverables, each belonging to exactly one package, each sized for a\n"
        "bounded Agent 2 execution. `ResponsibleParty` is `Ryan Tufts` for every\n"
        "deliverable under the D-GOV-27 assignment; SCA-001 applies that existing\n"
        "assignment to the new carrier and closes the stale OI-011 statement.",
    )
    new_deliverable_row = (
        "| DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance | Generic Runtime "
        "Stewardship and Release Assurance | REQ_SLICE | M | runtime/**; "
        "execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/**; client "
        "implementation only through separately authorized client-owned tranches | "
        "OBJ-001, OBJ-002, OBJ-004, OBJ-007 |"
    )
    text = replace_once(
        text,
        "| DEL-02-05_Live_Registry_Discipline_for_Skills_and_Tools | Live Registry Discipline for Skills and Tools | REGISTER | S | instruction-surface (M2); execution-tree for drift reports | OBJ-001 |",
        "| DEL-02-05_Live_Registry_Discipline_for_Skills_and_Tools | Live Registry Discipline for Skills and Tools | REGISTER | S | instruction-surface (M2); execution-tree for drift reports | OBJ-001 |\n"
        + new_deliverable_row,
    )
    text = replace_once(text, "(hard rule; 103/103).", "(hard rule; 104/104).")
    text = replace_once(text, "(94/94); mappings", "(95/95); mappings")
    text = replace_once(text, "| ScopeItemCount | 103 (IN 94 / OUT 9 / TBD 0) |", "| ScopeItemCount | 104 (IN 95 / OUT 9 / TBD 0) |")
    text = replace_once(text, "| DeliverableCount | 45 |", "| DeliverableCount | 46 |")
    text = replace_once(text, "| ContextEnvelopeCounts | S=14, M=30, L=1, XL=0 |", "| ContextEnvelopeCounts | S=14, M=31, L=1, XL=0 |")
    text = replace_once(
        text,
        "| Operative product | 26 | PKG-01, PKG-02, PKG-03, PKG-04, PKG-06 | 18 | COVERED |",
        "| Operative product | 27 | PKG-01, PKG-02, PKG-03, PKG-04, PKG-06 | 19 | COVERED |",
    )
    text = replace_once(
        text,
        "| Evidence | 18 | PKG-01, PKG-04, PKG-05, PKG-06 | 16 | COVERED |",
        "| Evidence | 19 | PKG-01, PKG-02, PKG-04, PKG-05, PKG-06 | 17 | COVERED |",
    )
    text = replace_once(
        text,
        "| PRD item → decomposition | `chirality_root_prd_coverage_forward_v1_0.csv` | 84 | 83 COVERED, 1 COVERED_WITH_RECORDED_DEFERRAL (OBJ-2), 0 UNCOVERED |",
        "| PRD item → decomposition | `chirality_root_prd_coverage_forward_v1_0.csv` | 85 | 84 COVERED, 1 COVERED_WITH_RECORDED_DEFERRAL (OBJ-2), 0 UNCOVERED |",
    )
    text = replace_once(
        text,
        "| decomposition unit → PRD | `chirality_root_trace_reverse_v1_0.csv` | 51 | 51 TRACED, 0 UNTRACED |",
        "| decomposition unit → PRD | `chirality_root_trace_reverse_v1_0.csv` | 52 | 52 TRACED, 0 UNTRACED |",
    )
    text = replace_once(text, "N-1..N-9; O-1..O-10;", "N-1..N-9; O-1..O-11;")
    text = replace_once(
        text,
        "RESPONSIBILITY_UNASSIGNED=1, OBJECTIVE_GRANULARITY=1 (total 13: 9 closed at the ruling, 4 carried open)",
        "RESPONSIBILITY_UNASSIGNED=1, OBJECTIVE_GRANULARITY=1 (total 13: 10 closed, 3 carried open)",
    )
    text = replace_once(
        text,
        "| Revision / Date | v1.0 candidate / 2026-07-25 |",
        "| Revision / Date | v1.1 SCA-001 successor / 2026-07-26 |",
    )
    text = replace_once(
        text,
        "`DEL-04-09_PRD_Source_Currency_Check_Capability` — is **proposed** as\n"
        "large-but-single-domain with envelope notes, for the owner to accept or split\n"
        "at Gate 5/6;",
        "`DEL-04-09_PRD_Source_Currency_Check_Capability` — was accepted as\n"
        "large-but-single-domain under D-GOV-25 and retains its envelope notes;",
    )
    text = replace_line(
        text,
        "| OI-011 |",
        "| OI-011 | `CLOSED_ASSIGNED_BY_D-GOV-27` | RESPONSIBILITY_UNASSIGNED | all 46 deliverables | `ResponsibleParty` is assigned to Ryan Tufts across the accepted register and the SCA-001 carrier. | D-GOV-27 assigned responsibility across the original 45 deliverables; SCA-001 carries that existing assignment to DEL-02-06 and closes the stale issue text. |",
    )
    decision = (
        "| DEC-022 | 2026-07-26 | **SCA-001 adds one standing Root runtime-stewardship "
        "carrier.** Add SOW-104 and DEL-02-06 under PKG-02; preserve DEL-02-02 unchanged; "
        "map the carrier to OBJ-001, OBJ-002, OBJ-004, and OBJ-007; classify the scope "
        "item as Operative Product and Evidence; use REQ_SLICE with Context Envelope M; "
        "and declare `runtime/**` plus the carrier's execution/evidence tree as its "
        "anticipated Root write locus. | O-11 requires a standing Root carrier and "
        "declared locus. A separate deliverable preserves the accepted distinction between "
        "three-layer boundary conformance and consequential runtime stewardship. The "
        "carrier is activated one bounded change tranche at a time and creates no "
        "implementation or release authority. Requested by Ryan Tufts and approved through "
        "SCA-001 Gates 2–3. |"
    )
    text = replace_once(text, "\n### Change Log\n", "\n" + decision + "\n\n### Change Log\n")
    change_log = (
        "- 2026-07-26 — **SCA-001 revision 1.1 successor.** D-GOV-28 advanced the sole\n"
        "  scope source to Root PRD Revision 6 and adopted O-11. The amendment adds\n"
        "  SOW-104 and DEL-02-06 under PKG-02, maps OBJ-001/2/4/7, adds the bounded\n"
        "  `runtime/**` planning locus, and reconciles both trace registers and telemetry.\n"
        "  DEL-02-02 and every existing stable ID remain unchanged. These bytes become\n"
        "  current basis only upon the SCA-001 Gate 5 owner confirmation.\n"
    )
    text = replace_once(text, "\n---\n\n## 14. Downstream Execution Notes", "\n" + change_log + "\n---\n\n## 14. Downstream Execution Notes")
    text = replace_once(
        text,
        "preserve `ResponsibleParty: TBD` until a human\n  assigns it,",
        "preserve the D-GOV-27 `ResponsibleParty` assignment unless a human\n  changes it,",
    )
    text = replace_once(
        text,
        "- **Materialization stays gated.** This candidate creates no `PKG-*` or",
        "- **Materialization stays gated.** This amendment creates no `PKG-*` or",
    )
    (CANDIDATE / MAIN).write_text(text)


def build_telemetry() -> None:
    text = (DECOMP / TELEMETRY).read_text()
    text = replace_once(text, "**Revision:** v1.0 · **Date:** 2026-07-25", "**Revision:** v1.1 · **Date:** 2026-07-26")
    status_start = text.index("**Status:** ACCEPTED")
    status_end = text.index("\n\nThis register", status_start)
    text = (
        text[:status_start]
        + "**Status:** SCA-001 successor; current-basis effect is conditional on the\n"
        + "Gate 5 owner confirmation recorded in\n"
        + "`execution/_ScopeChange/SCA-001_2026-07-26_1454/Decision_Log.md`.\n"
        + text[status_end:]
    )
    replacements = [
        ("| Revision | v1.0 (candidate) |", "| Revision | v1.1 (SCA-001 successor) |"),
        ("| Date | 2026-07-25 |", "| Date | 2026-07-26 |"),
        ("| ScopeItemCount | 103 |", "| ScopeItemCount | 104 |"),
        ("| ScopeItemsIN | 94 |", "| ScopeItemsIN | 95 |"),
        ("| DeliverableCount | 45 |", "| DeliverableCount | 46 |"),
        ("| ContextEnvelopeCounts | S=14, M=30, L=1, XL=0 |", "| ContextEnvelopeCounts | S=14, M=31, L=1, XL=0 |"),
        ("| PRDForwardItemCount | 84 |", "| PRDForwardItemCount | 85 |"),
        ("| PRDItemsCovered | 83 |", "| PRDItemsCovered | 84 |"),
        ("| UnitsUntracedInReverseRegister | 0 |", "| UnitsUntracedInReverseRegister | 0 |"),
        ("| OpenIssueCount | 13 (9 closed at the D-GOV-25 ruling, 4 carried open) |", "| OpenIssueCount | 13 (10 closed, 3 carried open) |"),
        ("| ScopeLedgerRowsCarryingLabelEffectAnnotation | 18 |", "| ScopeLedgerRowsCarryingLabelEffectAnnotation | 19 |"),
        ("| PKG-02_Operative_Instruction_Surface_and_Runtime_Layers | 5 |", "| PKG-02_Operative_Instruction_Surface_and_Runtime_Layers | 6 |"),
        ("| Operative product | 26 |", "| Operative product | 27 |"),
        ("| Evidence | 18 |", "| Evidence | 19 |"),
        ("| decomposition unit → PRD | `chirality_root_trace_reverse_v1_0.csv` | 51 (6 packages + 45 deliverables) | 51 TRACED, 0 UNTRACED |", "| decomposition unit → PRD | `chirality_root_trace_reverse_v1_0.csv` | 52 (6 packages + 46 deliverables) | 52 TRACED, 0 UNTRACED |"),
        ("Forward population (84 items):", "Forward population (85 items):"),
        ("O-1..O-10 (10);", "O-1..O-11 (11);"),
        ("**9\nclosed, 4 carried open.**", "**10\nclosed, 3 carried open.**"),
        ("| OI-011 | `OPEN` | Not ruled on; no responsibility assigned |", "| OI-011 | `CLOSED_ASSIGNED_BY_D-GOV-27` | Ryan Tufts assigned; carried to DEL-02-06 by SCA-001 |"),
    ]
    for old, new in replacements:
        text = replace_once(text, old, new)
    text = replace_once(
        text,
        "| PRD item → decomposition | `chirality_root_prd_coverage_forward_v1_0.csv` | 84 | 83 COVERED, 1 COVERED_WITH_RECORDED_DEFERRAL (OBJ-2), 0 UNCOVERED |",
        "| PRD item → decomposition | `chirality_root_prd_coverage_forward_v1_0.csv` | 85 | 84 COVERED, 1 COVERED_WITH_RECORDED_DEFERRAL (OBJ-2), 0 UNCOVERED |",
    )
    text = replace_once(
        text,
        "| Evidence | 19 | PKG-01, PKG-04, PKG-05, PKG-06 | 16 | COVERED |",
        "| Evidence | 19 | PKG-01, PKG-02, PKG-04, PKG-05, PKG-06 | 17 | COVERED |",
    )
    text = replace_once(
        text,
        "| Operative product | 27 | PKG-01, PKG-02, PKG-03, PKG-04, PKG-06 | 18 | COVERED |",
        "| Operative product | 27 | PKG-01, PKG-02, PKG-03, PKG-04, PKG-06 | 19 | COVERED |",
    )
    text = replace_once(
        text,
        "participation ranges from two categories (PKG-02: normative basis and\noperative product) to all four",
        "participation ranges from three categories (PKG-02: normative basis,\noperative product, and evidence) to all four",
    )
    text = replace_once(
        text,
        "DEL-06-02, DEL-06-04, DEL-06-05, DEL-06-08",
        "DEL-02-06, DEL-06-02, DEL-06-04, DEL-06-05, DEL-06-08",
    )
    text = replace_once(
        text,
        "DEL-05-08, DEL-06-02, DEL-06-06",
        "DEL-05-08, DEL-02-06, DEL-06-02, DEL-06-06",
    )
    text = replace_once(
        text,
        "**Label-effect annotations.** 18 ledger rows and all 7 objective-register rows\n"
        "carry PROPOSED source labels from the PRD; each now carries the additive\n"
        "annotation \"in effect per the D-GOV-22 adoption ruling; confirmed at the\n"
        "D-GOV-25 ruling\" (owner decision 2, DEC-017). **No source label was\n"
        "overwritten**",
        "**Label-effect annotations.** 18 predecessor ledger rows and all 7\n"
        "objective-register rows carry the additive D-GOV-22/D-GOV-25 effect\n"
        "annotation described by DEC-017. SOW-104 separately carries its\n"
        "PROPOSED-origin label and D-GOV-28 adoption effect. **No source label was\n"
        "overwritten**",
    )
    (CANDIDATE / TELEMETRY).write_text(text)


def build_diff() -> None:
    chunks: list[str] = []
    for name in FILES:
        old = (DECOMP / name).read_text().splitlines(keepends=True)
        new = (CANDIDATE / name).read_text().splitlines(keepends=True)
        chunks.extend(
            difflib.unified_diff(
                old,
                new,
                fromfile=f"accepted-v1.0/{name}",
                tofile=f"candidate-v1.1/{name}",
            )
        )
    (SNAPSHOT / "Gate_3_Exact_Amendment.diff").write_text("".join(chunks))


def main() -> None:
    CANDIDATE.mkdir(exist_ok=True)
    build_scope()
    build_deliverables()
    build_objectives()
    build_forward()
    build_reverse()
    build_main()
    build_telemetry()
    build_diff()


if __name__ == "__main__":
    main()
