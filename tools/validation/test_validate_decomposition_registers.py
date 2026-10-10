"""Fixture tests for validate_decomposition_registers.py.

Fixtures are built in tmp_path so the tests never read a live project corpus.
Coverage targets, per the OI-013 closure contract:
  * both named evidence sub-classes, reported distinctly;
  * ANCHOR-row cleanliness under the same rules;
  * a clean synthetic register that produces zero findings;
  * cross-register (XRG) and dependency-binding (DRB) families;
  * report-only posture and the three exit codes.
"""

from __future__ import annotations

import csv
import os
import subprocess
import sys
from pathlib import Path

import pytest

VALIDATION_DIR = Path(__file__).resolve().parent

import validate_decomposition_registers as vdr  # noqa: E402
from validate_dependencies_schema import REQUIRED_COLUMNS  # noqa: E402

TOOL = VALIDATION_DIR / "validate_decomposition_registers.py"
INSTRUCTION_ROOT_ENV = "CHIRALITY_INSTRUCTION_ROOT"  # SPEC §0.2.1

DELIVERABLE_COLUMNS = [
    "DeliverableID", "PackageID", "Name", "Description", "Type", "ResponsibleParty",
    "AnticipatedArtifacts", "CoversScopeItems", "SupportsObjectives",
    "ContextEnvelope", "ContextEnvelopeNotes", "PhaseHint",
]
LEDGER_COLUMNS = [
    "ScopeItemID", "InOutStatus", "ScopeItemStatement", "SourceRef", "PackageID",
    "DeliverableIDs", "ObjectiveIDs", "DecisionRef", "OpenIssue", "Notes",
]
CONTEXT_QA_COLUMNS = [
    "DeliverableID", "PackageID", "ContextEnvelope", "Risk", "RecommendedAction", "Notes",
]


# --------------------------------------------------------------------------
# Fixture construction
# --------------------------------------------------------------------------

def write_csv(path: Path, columns: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def anchor_row(seq: str = "001", **overrides: str) -> dict[str, str]:
    """A well-formed ANCHOR row: SourceRef is a locus, EvidenceQuote is source text."""
    row = {column: "" for column in REQUIRED_COLUMNS}
    row.update(
        {
            "RegisterSchemaVersion": "v3.1",
            "DependencyID": f"DEP-01-01-{seq}",
            "FromPackageID": "PKG-01",
            "FromDeliverableID": "DEL-01-01",
            "FromDeliverableName": "Record tier schema",
            "DependencyClass": "ANCHOR",
            "AnchorType": "TRACES_TO_REQUIREMENT",
            "Direction": "UPSTREAM",
            "DependencyType": "OTHER",
            "TargetType": "REQUIREMENT",
            "TargetPackageID": "",
            "TargetDeliverableID": "",
            "TargetRefID": "SOW-001",
            "TargetName": "Record tier entity model",
            "TargetLocation": "execution/_Decomposition/ScopeLedger.csv",
            "Statement": "DEL-01-01 covers scope item SOW-001.",
            "EvidenceFile": "execution/_Decomposition/ScopeLedger.csv",
            "SourceRef": "ScopeLedger.csv row SOW-001",
            "EvidenceQuote": "DeliverableIDs include DEL-01-01",
            "Explicitness": "EXPLICIT",
            "RequiredMaturity": "SEMANTIC_READY",
            "ProposedMaturity": "SEMANTIC_READY",
            "SatisfactionStatus": "TBD",
            "Confidence": "HIGH",
            "Origin": "DECLARED",
            "FirstSeen": "2026-07-25",
            "LastSeen": "2026-07-25",
            "Status": "ACTIVE",
            "Notes": "",
        }
    )
    row.update(overrides)
    return row


def execution_row(seq: str = "003", **overrides: str) -> dict[str, str]:
    """A well-formed EXECUTION row."""
    row = anchor_row(seq)
    row.update(
        {
            "DependencyClass": "EXECUTION",
            "AnchorType": "NOT_APPLICABLE",
            "DependencyType": "PREREQUISITE",
            "TargetType": "DELIVERABLE",
            "TargetPackageID": "PKG-02",
            "TargetDeliverableID": "DEL-02-01",
            "TargetRefID": "DEL-02-01",
            "TargetName": "Status parser",
            "Statement": "DEL-01-01 must precede DEL-02-01.",
            "EvidenceFile": "execution/_Decomposition/ScopeLedger.csv",
            "SourceRef": "PLAN dag gate exhibit, row E-A01",
            "EvidenceQuote": "the record tier underlies the parser items",
            "Origin": "EXTRACTED",
        }
    )
    row.update(overrides)
    return row


def build_workspace(
    root: Path,
    registers: dict[str, list[dict[str, str]]] | None = None,
    deliverables: list[dict[str, str]] | None = None,
    ledger: list[dict[str, str]] | None = None,
    context_qa: list[dict[str, str]] | None = None,
) -> Path:
    """Build a minimal, internally consistent two-deliverable execution root."""
    execution_root = root / "execution"
    decomposition = execution_root / "_Decomposition"

    deliverables = deliverables if deliverables is not None else [
        {
            "DeliverableID": "DEL-01-01", "PackageID": "PKG-01",
            "Name": "Record tier schema", "Description": "d", "Type": "CODE",
            "ResponsibleParty": "TBD", "AnticipatedArtifacts": "a",
            "CoversScopeItems": "SOW-001", "SupportsObjectives": "OBJ-001",
            "ContextEnvelope": "S", "ContextEnvelopeNotes": "", "PhaseHint": "P1",
        },
        {
            "DeliverableID": "DEL-02-01", "PackageID": "PKG-02",
            "Name": "Status parser", "Description": "d", "Type": "CODE",
            "ResponsibleParty": "TBD", "AnticipatedArtifacts": "a",
            "CoversScopeItems": "SOW-002", "SupportsObjectives": "OBJ-001",
            "ContextEnvelope": "M", "ContextEnvelopeNotes": "", "PhaseHint": "P1",
        },
    ]
    ledger = ledger if ledger is not None else [
        {
            "ScopeItemID": "SOW-001", "InOutStatus": "IN", "ScopeItemStatement": "s",
            "SourceRef": "§7.1", "PackageID": "PKG-01", "DeliverableIDs": "DEL-01-01",
            "ObjectiveIDs": "OBJ-001", "DecisionRef": "", "OpenIssue": "FALSE", "Notes": "",
        },
        {
            "ScopeItemID": "SOW-002", "InOutStatus": "IN", "ScopeItemStatement": "s",
            "SourceRef": "§7.2", "PackageID": "PKG-02", "DeliverableIDs": "DEL-02-01",
            "ObjectiveIDs": "OBJ-001", "DecisionRef": "", "OpenIssue": "FALSE", "Notes": "",
        },
    ]
    context_qa = context_qa if context_qa is not None else [
        {"DeliverableID": "DEL-01-01", "PackageID": "PKG-01", "ContextEnvelope": "S",
         "Risk": "LOW", "RecommendedAction": "None", "Notes": ""},
        {"DeliverableID": "DEL-02-01", "PackageID": "PKG-02", "ContextEnvelope": "M",
         "Risk": "LOW", "RecommendedAction": "None", "Notes": ""},
    ]

    write_csv(decomposition / "Deliverables.csv", DELIVERABLE_COLUMNS, deliverables)
    write_csv(decomposition / "ScopeLedger.csv", LEDGER_COLUMNS, ledger)
    write_csv(decomposition / "ContextBudgetQA.csv", CONTEXT_QA_COLUMNS, context_qa)

    if registers is None:
        registers = {
            "PKG-01_Core/1_Working/DEL-01-01_Record_tier": [anchor_row(), execution_row()],
            "PKG-02_Parsers/1_Working/DEL-02-01_Status_parser": [
                anchor_row(
                    "001", DependencyID="DEP-02-01-001", FromPackageID="PKG-02",
                    FromDeliverableID="DEL-02-01", FromDeliverableName="Status parser",
                    TargetRefID="SOW-002", Statement="DEL-02-01 covers SOW-002.",
                )
            ],
        }
    for relative, rows in registers.items():
        write_csv(execution_root / relative / "Dependencies.csv", REQUIRED_COLUMNS, rows)
    return execution_root


@pytest.fixture(autouse=True)
def _no_instruction_root_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """Keep a caller's CHIRALITY_INSTRUCTION_ROOT out of every test."""
    monkeypatch.delenv(INSTRUCTION_ROOT_ENV, raising=False)


def empty_instruction_root(tmp_path: Path) -> Path:
    """An instruction root with no surface, so EVQ tests never read the checkout."""
    root = tmp_path / "empty_checkout"
    root.mkdir(exist_ok=True)
    return root


def codes(report: dict) -> dict[str, int]:
    return report["findings_by_code"]


def ids_for(report: dict, code: str) -> list[str]:
    return [f["row_id"] for f in report["findings"] if f["code"] == code]


# --------------------------------------------------------------------------
# Clean baseline
# --------------------------------------------------------------------------

def test_clean_synthetic_workspace_is_finding_free(tmp_path: Path) -> None:
    execution_root = build_workspace(tmp_path)
    report = vdr.run(execution_root)

    assert report["findings"] == []
    assert report["registers_scanned"] == 2
    assert report["dependency_rows"] == 3
    assert report["deliverables_declared"] == 2
    assert report["error_count"] == 0
    assert report["warning_count"] == 0
    metrics = report["row_class_metrics"]
    assert metrics["ANCHOR"]["rows"] == 2
    assert metrics["ANCHOR"]["well_formed_evidence"] == 2
    assert metrics["EXECUTION"]["well_formed_evidence"] == 1


# --------------------------------------------------------------------------
# OI-013 sub-class (a): locus/quote confusion
# --------------------------------------------------------------------------

def test_locus_quote_duplication_is_detected_as_its_own_subclass(tmp_path: Path) -> None:
    pasted = 'OI-012 basis: "driving edges: PKG-07/08/09"'
    execution_root = build_workspace(
        tmp_path,
        registers={
            "PKG-01_Core/1_Working/DEL-01-01_Record_tier": [
                anchor_row(),
                execution_row(SourceRef=pasted, EvidenceQuote=pasted),
            ]
        },
    )
    report = vdr.run(execution_root, families=("EVQ",))

    assert codes(report)["EVQ-001"] == 1
    assert ids_for(report, "EVQ-001") == ["DEP-01-01-003"]
    # Reported distinctly: duplication is not also counted as empty-evidence.
    assert "EVQ-003" not in codes(report)
    assert "EVQ-004" not in codes(report)
    metrics = report["row_class_metrics"]
    assert metrics["EXECUTION"]["locus_quote_duplication"] == 1
    assert metrics["EXECUTION"]["well_formed_evidence"] == 0
    assert metrics["ANCHOR"]["well_formed_evidence"] == 1


def test_quote_shaped_locus_is_a_separate_warning(tmp_path: Path) -> None:
    execution_root = build_workspace(
        tmp_path,
        registers={
            "PKG-01_Core/1_Working/DEL-01-01_Record_tier": [
                anchor_row(),
                execution_row(
                    SourceRef='§3 mapping notes: "parser items underlie OBJ-001"',
                    EvidenceQuote="parser items underlie OBJ-001",
                ),
            ]
        },
    )
    report = vdr.run(execution_root, families=("EVQ",))

    assert codes(report) == {"EVQ-002": 1}
    assert report["error_count"] == 0
    assert report["warning_count"] == 1
    assert report["row_class_metrics"]["EXECUTION"]["quote_shaped_locus"] == 1


# --------------------------------------------------------------------------
# OI-013 sub-class (b): empty-evidence rows
# --------------------------------------------------------------------------

def test_empty_evidence_row_reports_both_cells_distinctly(tmp_path: Path) -> None:
    execution_root = build_workspace(
        tmp_path,
        registers={
            "PKG-01_Core/1_Working/DEL-01-01_Record_tier": [
                anchor_row(),
                execution_row(SourceRef="location TBD", EvidenceQuote=""),
            ]
        },
    )
    report = vdr.run(execution_root, families=("EVQ",))

    assert codes(report) == {"EVQ-003": 1, "EVQ-004": 1}
    assert ids_for(report, "EVQ-003") == ["DEP-01-01-003"]
    assert ids_for(report, "EVQ-004") == ["DEP-01-01-003"]
    # The empty-evidence class must NOT be reported as locus/quote duplication,
    # even though both cells are "equal" when both are blank.
    assert "EVQ-001" not in codes(report)
    metrics = report["row_class_metrics"]["EXECUTION"]
    assert metrics["empty_evidence_quote"] == 1
    assert metrics["placeholder_locus"] == 1
    assert metrics["locus_quote_duplication"] == 0


def test_blank_source_ref_and_quote_is_empty_evidence_not_duplication(tmp_path: Path) -> None:
    execution_root = build_workspace(
        tmp_path,
        registers={
            "PKG-01_Core/1_Working/DEL-01-01_Record_tier": [
                execution_row(SourceRef="", EvidenceQuote=""),
            ]
        },
    )
    report = vdr.run(execution_root, families=("EVQ",))

    assert "EVQ-001" not in codes(report)
    assert codes(report)["EVQ-003"] == 1
    assert codes(report)["EVQ-004"] == 1


def test_placeholder_locus_vocabulary(tmp_path: Path) -> None:
    placeholders = ["location TBD", "TBD", "n/a", "N/A", "none", "?", "--", "  tbd  "]
    citable = ["ScopeLedger.csv row SOW-001", "§7.1", "PLAN §4.2 exhibit row E-A01",
               "Deliverables.csv row DEL-01-01"]
    for value in placeholders:
        assert vdr.PLACEHOLDER_LOCUS.match(value), f"{value!r} should read as a placeholder"
    for value in citable:
        assert not vdr.PLACEHOLDER_LOCUS.match(value), f"{value!r} is a real locus"


# --------------------------------------------------------------------------
# Row-class awareness
# --------------------------------------------------------------------------

def test_anchor_rows_are_checked_and_reported_separately(tmp_path: Path) -> None:
    """ANCHOR rows are subject to the same rules; the summary keeps classes apart."""
    execution_root = build_workspace(
        tmp_path,
        registers={
            "PKG-01_Core/1_Working/DEL-01-01_Record_tier": [
                anchor_row("001", SourceRef="dup text", EvidenceQuote="dup text"),
                anchor_row("002"),
                execution_row(),
            ]
        },
    )
    report = vdr.run(execution_root, families=("EVQ",))

    assert ids_for(report, "EVQ-001") == ["DEP-01-01-001"]
    assert [f["row_class"] for f in report["findings"]] == ["ANCHOR"]
    metrics = report["row_class_metrics"]
    assert metrics["ANCHOR"]["rows"] == 2
    assert metrics["ANCHOR"]["locus_quote_duplication"] == 1
    assert metrics["ANCHOR"]["well_formed_evidence"] == 1
    assert metrics["EXECUTION"]["well_formed_evidence"] == 1


def test_evidence_file_coverage_and_resolution_are_distinct_metrics(tmp_path: Path) -> None:
    """The analyze_dep_closure.py lesson: populated != resolves != quote quality."""
    execution_root = build_workspace(
        tmp_path,
        registers={
            "PKG-01_Core/1_Working/DEL-01-01_Record_tier": [
                anchor_row("001", EvidenceFile=""),
                anchor_row("002", EvidenceFile="execution/_Decomposition/NoSuchFile.csv"),
                anchor_row("003"),
            ]
        },
    )
    report = vdr.run(execution_root, families=("EVQ",),
                     instruction_root=empty_instruction_root(tmp_path))

    assert codes(report) == {"EVQ-005": 1, "EVQ-006": 1}
    metrics = report["row_class_metrics"]["ANCHOR"]
    assert metrics["rows"] == 3
    assert metrics["evidence_file_populated"] == 2   # coverage
    assert metrics["evidence_file_resolved"] == 1    # resolution
    assert metrics["well_formed_evidence"] == 1


# --------------------------------------------------------------------------
# Cross-register consistency (XRG)
# --------------------------------------------------------------------------

def test_non_reciprocal_scope_coverage_is_reported_from_both_sides(tmp_path: Path) -> None:
    execution_root = build_workspace(tmp_path)
    ledger_path = execution_root / "_Decomposition" / "ScopeLedger.csv"
    rows = list(csv.DictReader(ledger_path.open(encoding="utf-8-sig")))
    rows[0]["DeliverableIDs"] = "DEL-02-01"  # SOW-001 now points at the wrong deliverable
    write_csv(ledger_path, LEDGER_COLUMNS, rows)

    report = vdr.run(execution_root, families=("XRG",))

    assert codes(report)["XRG-003"] == 2  # once from the ledger, once from Deliverables
    assert codes(report)["XRG-004"] == 1  # home PKG-01 holds none of SOW-001's deliverables


def test_unknown_ids_objectives_and_context_budget_drift(tmp_path: Path) -> None:
    execution_root = build_workspace(tmp_path)
    decomposition = execution_root / "_Decomposition"

    ledger = list(csv.DictReader((decomposition / "ScopeLedger.csv").open(encoding="utf-8-sig")))
    ledger[0]["DeliverableIDs"] = "DEL-09-09"       # XRG-001
    ledger[1]["ObjectiveIDs"] = "OBJ-001;OBJ-007"   # XRG-005
    ledger.append({
        "ScopeItemID": "SOW-003", "InOutStatus": "IN", "ScopeItemStatement": "s",
        "SourceRef": "§7.3", "PackageID": "PKG-01", "DeliverableIDs": "",
        "ObjectiveIDs": "OBJ-001", "DecisionRef": "", "OpenIssue": "FALSE", "Notes": "",
    })                                              # XRG-006
    ledger.append({
        "ScopeItemID": "SOW-004", "InOutStatus": "OUT", "ScopeItemStatement": "s",
        "SourceRef": "§7.4", "PackageID": "PKG-01", "DeliverableIDs": "DEL-01-01",
        "ObjectiveIDs": "", "DecisionRef": "", "OpenIssue": "FALSE", "Notes": "",
    })                                              # XRG-007
    write_csv(decomposition / "ScopeLedger.csv", LEDGER_COLUMNS, ledger)

    deliverables = list(csv.DictReader((decomposition / "Deliverables.csv").open(encoding="utf-8-sig")))
    deliverables[0]["CoversScopeItems"] = "SOW-001;SOW-999"  # XRG-002
    deliverables[1]["PhaseHint"] = ""                        # XRG-008
    write_csv(decomposition / "Deliverables.csv", DELIVERABLE_COLUMNS, deliverables)

    context_qa = list(csv.DictReader((decomposition / "ContextBudgetQA.csv").open(encoding="utf-8-sig")))
    context_qa[0]["ContextEnvelope"] = "XL"                  # XRG-010
    context_qa.pop(1)                                        # XRG-009
    write_csv(decomposition / "ContextBudgetQA.csv", CONTEXT_QA_COLUMNS, context_qa)

    report = vdr.run(execution_root, families=("XRG",))
    found = codes(report)

    assert found["XRG-001"] == 1
    assert found["XRG-002"] == 1
    assert found["XRG-005"] == 1
    assert found["XRG-006"] == 1
    assert found["XRG-007"] == 1
    assert found["XRG-008"] == 1
    assert found["XRG-009"] == 1
    assert found["XRG-010"] == 1


def test_every_scope_item_has_a_package_home(tmp_path: Path) -> None:
    """D-GOV-48: every IN, OUT and TBD item has one Package; only IN items map to Deliverables.

    A missing home is XRG-011 (ERROR) on an IN item and XRG-013 (WARNING) on an
    OUT or TBD item. XRG-012 (D-GOV-47) is retired: an OUT or TBD item with a
    PackageID conforms.
    """
    execution_root = build_workspace(tmp_path)
    ledger_path = execution_root / "_Decomposition" / "ScopeLedger.csv"
    ledger = list(csv.DictReader(ledger_path.open(encoding="utf-8-sig")))
    blank = {"ScopeItemStatement": "s", "DeliverableIDs": "", "ObjectiveIDs": "",
             "DecisionRef": "", "OpenIssue": "FALSE", "Notes": ""}
    ledger.append({"ScopeItemID": "SOW-003", "InOutStatus": "OUT", "SourceRef": "§7.3",
                   "PackageID": "PKG-01", **blank})
    ledger.append({"ScopeItemID": "SOW-004", "InOutStatus": "TBD", "SourceRef": "§7.4",
                   "PackageID": "PKG-02", **blank})
    write_csv(ledger_path, LEDGER_COLUMNS, ledger)

    # OUT and TBD items with a Package home and no Deliverable mapping conform.
    assert vdr.run(execution_root, families=("XRG",))["findings"] == []

    ledger[0]["PackageID"] = ""  # IN item without a Package  -> XRG-011
    ledger[2]["PackageID"] = ""  # OUT item without a Package -> XRG-013
    ledger[3]["PackageID"] = ""  # TBD item without a Package -> XRG-013
    write_csv(ledger_path, LEDGER_COLUMNS, ledger)
    report = vdr.run(execution_root, families=("XRG",))

    assert codes(report) == {"XRG-011": 1, "XRG-013": 2}
    assert ids_for(report, "XRG-011") == ["SOW-001"]
    assert ids_for(report, "XRG-013") == ["SOW-003", "SOW-004"]
    assert report["error_count"] == 1  # XRG-013 is a WARNING
    assert "XRG-012" not in vdr.CHECKS  # retired by D-GOV-48, not reused


def test_package_home_is_exactly_one_known_package(tmp_path: Path) -> None:
    """D-GOV-48: a ledger item names exactly one Package, and that Package exists."""
    execution_root = build_workspace(tmp_path)
    ledger_path = execution_root / "_Decomposition" / "ScopeLedger.csv"
    ledger = list(csv.DictReader(ledger_path.open(encoding="utf-8-sig")))
    blank = {"ScopeItemStatement": "s", "DeliverableIDs": "", "ObjectiveIDs": "",
             "DecisionRef": "", "OpenIssue": "FALSE", "Notes": ""}
    ledger.append({"ScopeItemID": "SOW-003", "InOutStatus": "OUT", "SourceRef": "§7.3",
                   "PackageID": "PKG-99", **blank})
    ledger.append({"ScopeItemID": "SOW-004", "InOutStatus": "TBD", "SourceRef": "§7.4",
                   "PackageID": "PKG-01;PKG-02", **blank})
    write_csv(ledger_path, LEDGER_COLUMNS, ledger)
    report = vdr.run(execution_root, families=("XRG",))

    assert codes(report) == {"XRG-014": 1, "XRG-015": 1}
    assert ids_for(report, "XRG-014") == ["SOW-004"]
    assert ids_for(report, "XRG-015") == ["SOW-003"]


def test_single_home_is_compared_after_parsing(tmp_path: Path) -> None:
    """XRG-004 compares the parsed home, so a stray separator is not a mismatch."""
    execution_root = build_workspace(tmp_path)
    ledger_path = execution_root / "_Decomposition" / "ScopeLedger.csv"
    ledger = list(csv.DictReader(ledger_path.open(encoding="utf-8-sig")))
    ledger[0]["PackageID"] = "PKG-01; "
    write_csv(ledger_path, LEDGER_COLUMNS, ledger)
    assert "XRG-004" not in codes(vdr.run(execution_root, families=("XRG",)))

    ledger[0]["PackageID"] = "PKG-02;"
    write_csv(ledger_path, LEDGER_COLUMNS, ledger)
    assert codes(vdr.run(execution_root, families=("XRG",))).get("XRG-004") == 1


def test_supporting_deliverable_in_another_package_is_not_a_finding(tmp_path: Path) -> None:
    """XRG-004: a linked deliverable in another Package is a supporting contribution.

    Management manual v7: "Several Deliverables may contribute to an included
    obligation, including supporting contributions from another Package." No
    finding while the home Package holds at least one linked deliverable.
    """
    execution_root = build_workspace(tmp_path)
    decomposition = execution_root / "_Decomposition"
    ledger = list(csv.DictReader((decomposition / "ScopeLedger.csv").open(encoding="utf-8-sig")))
    ledger[0]["DeliverableIDs"] = "DEL-01-01;DEL-02-01"  # home PKG-01, support from PKG-02
    write_csv(decomposition / "ScopeLedger.csv", LEDGER_COLUMNS, ledger)
    deliverables = list(csv.DictReader((decomposition / "Deliverables.csv").open(encoding="utf-8-sig")))
    deliverables[1]["CoversScopeItems"] = "SOW-002;SOW-001"
    write_csv(decomposition / "Deliverables.csv", DELIVERABLE_COLUMNS, deliverables)

    report = vdr.run(execution_root, families=("XRG",))

    assert report["findings"] == []


def test_home_package_holding_no_linked_deliverable_is_a_warning(tmp_path: Path) -> None:
    """XRG-004 warns once per item when the home Package holds none of its deliverables."""
    execution_root = build_workspace(tmp_path)
    decomposition = execution_root / "_Decomposition"
    deliverables = list(csv.DictReader((decomposition / "Deliverables.csv").open(encoding="utf-8-sig")))
    deliverables.append({
        "DeliverableID": "DEL-02-02", "PackageID": "PKG-02",
        "Name": "Second parser", "Description": "d", "Type": "CODE",
        "ResponsibleParty": "TBD", "AnticipatedArtifacts": "a",
        "CoversScopeItems": "SOW-001", "SupportsObjectives": "OBJ-001",
        "ContextEnvelope": "S", "ContextEnvelopeNotes": "", "PhaseHint": "P1",
    })
    deliverables[1]["CoversScopeItems"] = "SOW-002;SOW-001"
    deliverables[0]["CoversScopeItems"] = ""
    write_csv(decomposition / "Deliverables.csv", DELIVERABLE_COLUMNS, deliverables)
    ledger = list(csv.DictReader((decomposition / "ScopeLedger.csv").open(encoding="utf-8-sig")))
    ledger[0]["DeliverableIDs"] = "DEL-02-01;DEL-02-02"  # home PKG-01 holds neither
    write_csv(decomposition / "ScopeLedger.csv", LEDGER_COLUMNS, ledger)
    context_qa = list(csv.DictReader((decomposition / "ContextBudgetQA.csv").open(encoding="utf-8-sig")))
    context_qa.append({"DeliverableID": "DEL-02-02", "PackageID": "PKG-02", "ContextEnvelope": "S",
                       "Risk": "LOW", "RecommendedAction": "None", "Notes": ""})
    write_csv(decomposition / "ContextBudgetQA.csv", CONTEXT_QA_COLUMNS, context_qa)

    report = vdr.run(execution_root, families=("XRG",))

    assert codes(report) == {"XRG-004": 1}  # one finding per item, not per link
    assert ids_for(report, "XRG-004") == ["SOW-001"]
    assert report["error_count"] == 0
    assert report["warning_count"] == 1
    assert vdr.CHECKS["XRG-004"][1] == vdr.WARNING


def test_xrg004_is_not_repeated_for_an_item_with_several_homes(tmp_path: Path) -> None:
    """With two homes, XRG-014 reports the item and XRG-004 stays silent."""
    execution_root = build_workspace(tmp_path)
    ledger_path = execution_root / "_Decomposition" / "ScopeLedger.csv"
    ledger = list(csv.DictReader(ledger_path.open(encoding="utf-8-sig")))
    ledger[0]["PackageID"] = "PKG-02;PKG-03"
    write_csv(ledger_path, LEDGER_COLUMNS, ledger)

    report = vdr.run(execution_root, families=("XRG",))

    assert "XRG-004" not in codes(report)
    assert codes(report)["XRG-014"] == 1


def test_registers_dir_reads_companion_registers_outside_decomposition(tmp_path: Path) -> None:
    """--registers-dir finds registers a project keeps outside _Decomposition/."""
    execution_root = build_workspace(tmp_path)
    registers = tmp_path / "docs" / "_Registers"
    registers.mkdir(parents=True)
    for name in ("Deliverables.csv", "ScopeLedger.csv", "ContextBudgetQA.csv"):
        (execution_root / "_Decomposition" / name).rename(registers / name)
    ledger = list(csv.DictReader((registers / "ScopeLedger.csv").open(encoding="utf-8-sig")))
    ledger[0]["PackageID"] = "PKG-01;PKG-02"  # XRG-014, visible only through the option
    write_csv(registers / "ScopeLedger.csv", LEDGER_COLUMNS, ledger)

    default = vdr.run(execution_root, families=("XRG",))
    assert default["skipped"] == ["XRG family (Deliverables.csv and/or ScopeLedger.csv absent)"]

    report = vdr.run(execution_root, families=("XRG",), registers_dir=registers)
    assert report["skipped"] == []
    assert codes(report) == {"XRG-014": 1}
    assert report["registers_dir"] == str(registers)

    cli = subprocess.run(
        [sys.executable, str(TOOL), str(execution_root), "--families", "XRG",
         "--registers-dir", str(registers)],
        capture_output=True, text=True,
    )
    assert cli.returncode == 1, cli.stdout + cli.stderr
    assert "XRG-014" in cli.stdout

    missing = subprocess.run(
        [sys.executable, str(TOOL), str(execution_root), "--registers-dir",
         str(tmp_path / "nope")],
        capture_output=True, text=True,
    )
    assert missing.returncode == 2


def test_unknown_package_check_needs_a_deliverable_package_column(tmp_path: Path) -> None:
    """XRG-015 is suppressed when Deliverables.csv carries no PackageID column."""
    execution_root = build_workspace(tmp_path)
    decomposition = execution_root / "_Decomposition"
    rows = list(csv.DictReader((decomposition / "Deliverables.csv").open(encoding="utf-8-sig")))
    columns = [c for c in DELIVERABLE_COLUMNS if c != "PackageID"]
    write_csv(decomposition / "Deliverables.csv", columns,
              [{k: v for k, v in row.items() if k != "PackageID"} for row in rows])

    assert "XRG-015" not in codes(vdr.run(execution_root, families=("XRG",)))


def test_package_home_checks_skip_a_ledger_without_a_package_column(tmp_path: Path) -> None:
    columns = [c for c in LEDGER_COLUMNS if c != "PackageID"]
    ledger = [
        {"ScopeItemID": "SOW-001", "InOutStatus": "IN", "ScopeItemStatement": "s",
         "SourceRef": "§7.1", "DeliverableIDs": "DEL-01-01", "ObjectiveIDs": "OBJ-001",
         "DecisionRef": "", "OpenIssue": "FALSE", "Notes": ""},
        {"ScopeItemID": "SOW-002", "InOutStatus": "IN", "ScopeItemStatement": "s",
         "SourceRef": "§7.2", "DeliverableIDs": "DEL-02-01", "ObjectiveIDs": "OBJ-001",
         "DecisionRef": "", "OpenIssue": "FALSE", "Notes": ""},
        {"ScopeItemID": "SOW-003", "InOutStatus": "OUT", "ScopeItemStatement": "s",
         "SourceRef": "§7.3", "DeliverableIDs": "", "ObjectiveIDs": "",
         "DecisionRef": "", "OpenIssue": "FALSE", "Notes": ""},
        {"ScopeItemID": "SOW-004", "InOutStatus": "TBD", "ScopeItemStatement": "s",
         "SourceRef": "§7.4", "DeliverableIDs": "", "ObjectiveIDs": "",
         "DecisionRef": "", "OpenIssue": "FALSE", "Notes": ""},
    ]
    execution_root = build_workspace(tmp_path)
    write_csv(execution_root / "_Decomposition" / "ScopeLedger.csv", columns, ledger)

    assert vdr.run(execution_root, families=("XRG",))["findings"] == []


def test_missing_companion_registers_are_skipped_not_errors(tmp_path: Path) -> None:
    execution_root = build_workspace(tmp_path)
    (execution_root / "_Decomposition" / "ScopeLedger.csv").unlink()

    report = vdr.run(execution_root, families=("XRG",))

    assert report["findings"] == []
    assert report["skipped"] == ["XRG family (Deliverables.csv and/or ScopeLedger.csv absent)"]


# --------------------------------------------------------------------------
# Dependency-register binding (DRB)
# --------------------------------------------------------------------------

def test_dependency_binding_defects(tmp_path: Path) -> None:
    execution_root = build_workspace(
        tmp_path,
        registers={
            "PKG-01_Core/1_Working/DEL-01-01_Record_tier": [
                anchor_row("001"),
                anchor_row("002", FromPackageID="PKG-09"),                  # DRB-003
                anchor_row("003", FromDeliverableName="Stale old name"),    # DRB-004
                execution_row("004", TargetDeliverableID="DEL-09-09"),      # DRB-005
                execution_row("001"),                                       # DRB-007 duplicate
            ],
            "PKG-02_Parsers/1_Working/DEL-02-01_Status_parser": [
                anchor_row("005"),  # FromDeliverableID DEL-01-01 in a DEL-02-01 folder
            ],
        },
    )
    report = vdr.run(execution_root, families=("DRB",))
    found = codes(report)

    assert found["DRB-001"] == 1
    assert found["DRB-003"] == 1
    assert found["DRB-004"] == 1
    assert found["DRB-005"] == 1
    assert found["DRB-007"] == 1


def test_unknown_from_deliverable_and_id_prefix(tmp_path: Path) -> None:
    execution_root = build_workspace(
        tmp_path,
        registers={
            "PKG-01_Core/1_Working/DEL-01-01_Record_tier": [
                anchor_row("001", DependencyID="DEP-07-07-001"),  # DRB-006
            ],
            "PKG-09_Ghost/1_Working/DEL-09-09_Ghost": [
                anchor_row("001", DependencyID="DEP-09-09-001", FromDeliverableID="DEL-09-09",
                           FromPackageID="PKG-09", FromDeliverableName="Ghost"),  # DRB-002
            ],
        },
    )
    report = vdr.run(execution_root, families=("DRB",))
    found = codes(report)

    assert found["DRB-006"] == 1
    assert found["DRB-002"] == 1
    assert found["DRB-008"] == 1  # DEL-02-01 declared but has no register


# --------------------------------------------------------------------------
# Schema delegation, posture, and CLI contract
# --------------------------------------------------------------------------

def test_schema_family_delegates_to_validate_dependencies_schema(tmp_path: Path) -> None:
    execution_root = build_workspace(
        tmp_path,
        registers={
            "PKG-01_Core/1_Working/DEL-01-01_Record_tier": [
                anchor_row("001", DependencyType="ARCHITECTURE_BASIS"),
            ]
        },
    )
    report = vdr.run(execution_root, families=("SCH",))

    assert codes(report)["SCH-001"] >= 1
    assert any("invalid DependencyType" in f["detail"] for f in report["findings"])


def test_validator_never_mutates_inputs(tmp_path: Path) -> None:
    execution_root = build_workspace(
        tmp_path,
        registers={
            "PKG-01_Core/1_Working/DEL-01-01_Record_tier": [
                execution_row(SourceRef="location TBD", EvidenceQuote=""),
            ]
        },
    )
    before = {
        path: path.read_bytes()
        for path in sorted(execution_root.rglob("*.csv"))
    }

    vdr.run(execution_root)

    after = {path: path.read_bytes() for path in sorted(execution_root.rglob("*.csv"))}
    assert before == after


def test_run_is_deterministic(tmp_path: Path) -> None:
    execution_root = build_workspace(
        tmp_path,
        registers={
            "PKG-01_Core/1_Working/DEL-01-01_Record_tier": [
                anchor_row("001", SourceRef="dup", EvidenceQuote="dup"),
                execution_row(SourceRef="location TBD", EvidenceQuote=""),
            ]
        },
    )
    first = vdr.run(execution_root)
    second = vdr.run(execution_root)
    assert first == second


def test_cli_exit_codes_and_json_report(tmp_path: Path) -> None:
    execution_root = build_workspace(tmp_path)
    json_out = tmp_path / "report.json"

    clean = subprocess.run(
        [sys.executable, str(TOOL), str(execution_root), "--json", str(json_out)],
        capture_output=True, text=True,
    )
    assert clean.returncode == 0, clean.stdout + clean.stderr
    assert json_out.is_file()
    assert "Evidence-cell metrics by row class" in clean.stdout

    # Findings -> exit 1.
    register = execution_root / "PKG-01_Core/1_Working/DEL-01-01_Record_tier/Dependencies.csv"
    rows = list(csv.DictReader(register.open(encoding="utf-8-sig")))
    rows[1]["EvidenceQuote"] = ""
    write_csv(register, REQUIRED_COLUMNS, rows)
    findings = subprocess.run(
        [sys.executable, str(TOOL), str(execution_root)], capture_output=True, text=True
    )
    assert findings.returncode == 1
    assert "EVQ-003" in findings.stdout

    # Operational error -> exit 2.
    missing = subprocess.run(
        [sys.executable, str(TOOL), str(tmp_path / "nope")], capture_output=True, text=True
    )
    assert missing.returncode == 2

    unknown_family = subprocess.run(
        [sys.executable, str(TOOL), str(execution_root), "--families", "NOPE"],
        capture_output=True, text=True,
    )
    assert unknown_family.returncode == 2

    listing = subprocess.run(
        [sys.executable, str(TOOL), "--list-checks"], capture_output=True, text=True
    )
    assert listing.returncode == 0
    assert "EVQ-001" in listing.stdout


def test_os_level_read_failures_are_operational_not_findings(tmp_path: Path) -> None:
    """R-05: PermissionError/IsADirectoryError must exit 2, not 1."""
    execution_root = build_workspace(tmp_path)
    register = execution_root / "PKG-01_Core/1_Working/DEL-01-01_Record_tier/Dependencies.csv"

    # IsADirectoryError: replace the register with a directory of the same name.
    register.unlink()
    register.mkdir()
    try:
        vdr.read_register(register)
    except vdr.OperationalError as exc:
        assert "unreadable" in str(exc)
    else:
        raise AssertionError("a directory in place of a register must raise OperationalError")
    register.rmdir()

    # PermissionError via an unreadable file.
    write_csv(register, REQUIRED_COLUMNS, [anchor_row()])
    register.chmod(0o000)
    try:
        vdr.read_register(register)
    except vdr.OperationalError as exc:
        assert "unreadable" in str(exc)
    except PermissionError:  # pragma: no cover - only if run as root
        pass
    else:
        if not os.access(register, os.R_OK):  # pragma: no cover
            raise AssertionError("an unreadable register must raise OperationalError")
    finally:
        register.chmod(0o644)


def test_registers_in_later_lifecycle_folders_are_scanned(tmp_path: Path) -> None:
    """R-10a: a promoted deliverable's register must not drop out of the corpus."""
    execution_root = build_workspace(
        tmp_path,
        registers={
            "PKG-01_Core/2_Checking/DEL-01-01_Record_tier": [anchor_row(), execution_row()],
            "PKG-02_Parsers/3_Issued/DEL-02-01_Status_parser": [
                anchor_row("001", DependencyID="DEP-02-01-001", FromPackageID="PKG-02",
                           FromDeliverableID="DEL-02-01", FromDeliverableName="Status parser"),
            ],
        },
    )
    report = vdr.run(execution_root)

    assert report["registers_scanned"] == 2
    assert report["dependency_rows"] == 3
    assert report["findings"] == []  # in particular, no DRB-008


def test_reference_folder_registers_are_not_scanned(tmp_path: Path) -> None:
    execution_root = build_workspace(
        tmp_path,
        registers={"PKG-01_Core/0_References/DEL-01-01_Record_tier": [anchor_row()]},
    )
    report = vdr.run(execution_root, families=("EVQ",))

    assert report["registers_scanned"] == 0


def test_evidence_file_must_be_a_relative_regular_file(tmp_path: Path) -> None:
    """R-10b: a directory is not evidence, and an absolute path escapes the root."""
    absolute = str(tmp_path / "execution" / "_Decomposition" / "ScopeLedger.csv")
    execution_root = build_workspace(
        tmp_path,
        registers={
            "PKG-01_Core/1_Working/DEL-01-01_Record_tier": [
                anchor_row("001", EvidenceFile="execution/_Decomposition"),  # a directory
                anchor_row("002", EvidenceFile=absolute),                    # absolute
                anchor_row("003"),                                           # good
            ]
        },
    )
    report = vdr.run(execution_root, families=("EVQ",),
                     instruction_root=empty_instruction_root(tmp_path))

    assert codes(report) == {"EVQ-006": 2}
    details = " ".join(f["detail"] for f in report["findings"])
    assert "is a directory, not a file" in details
    assert "absolute path" in details
    assert report["row_class_metrics"]["ANCHOR"]["evidence_file_resolved"] == 1


def _evidence_fixture(tmp_path: Path, rows: list[dict[str, str]]) -> tuple[Path, Path]:
    """A workspace plus a separate instruction root, so no live corpus is read."""
    execution_root = build_workspace(
        tmp_path / "project",
        registers={"PKG-01_Core/1_Working/DEL-01-01_Record_tier": rows},
    )
    deliverable = execution_root / "PKG-01_Core/1_Working/DEL-01-01_Record_tier"
    (deliverable / "ScopeOfWork.md").write_text("scope\n", encoding="utf-8")
    (deliverable / "_run_records").mkdir()
    (deliverable / "_run_records" / "RUN.md").write_text("run\n", encoding="utf-8")
    instruction_root = tmp_path / "checkout"
    (instruction_root / "workflows" / "dependency-extract").mkdir(parents=True)
    (instruction_root / "workflows" / "dependency-extract" / "WORKFLOW.md").write_text(
        "workflow\n", encoding="utf-8"
    )
    # Checkout-relative material that is not on the instruction surface.
    (instruction_root / "projects" / "demo" / "docs").mkdir(parents=True)
    (instruction_root / "projects" / "demo" / "docs" / "SPEC.md").write_text(
        "spec\n", encoding="utf-8"
    )
    (instruction_root / "execution" / "_ScopeChange").mkdir(parents=True)
    (instruction_root / "execution" / "_ScopeChange" / "PLAN.csv").write_text(
        "plan\n", encoding="utf-8"
    )
    return execution_root, instruction_root


def test_evidence_file_resolves_in_each_allowed_form(tmp_path: Path) -> None:
    """SPEC §6.5 filename, §0.2.4 working-root and instruction-root references."""
    execution_root, instruction_root = _evidence_fixture(
        tmp_path,
        [
            anchor_row("001", EvidenceFile="ScopeOfWork.md"),            # deliverable
            anchor_row("002", EvidenceFile="_run_records/RUN.md"),       # deliverable
            anchor_row("003"),                                           # working root
            anchor_row("004", EvidenceFile="workflows/dependency-extract/WORKFLOW.md"),
            anchor_row("005", EvidenceFile="../../../_Decomposition/Deliverables.csv"),
        ],
    )
    report = vdr.run(execution_root, families=("EVQ",), instruction_root=instruction_root)

    assert codes(report) == {}
    assert report["row_class_metrics"]["ANCHOR"]["evidence_file_resolved"] == 5
    assert report["evidence_file_resolution_forms"] == {
        "deliverable": 3, "working_root": 1, "instruction_root": 1,
    }
    assert report["instruction_root"] == str(instruction_root)


def test_evidence_file_missing_in_every_form_is_reported(tmp_path: Path) -> None:
    """A truly missing file is still EVQ-006, naming every base it was tried in."""
    execution_root, instruction_root = _evidence_fixture(
        tmp_path,
        [
            anchor_row("001", EvidenceFile="Procedure.md"),
            anchor_row("002", EvidenceFile="execution/_Decomposition/NoSuchFile.csv"),
            anchor_row("003", EvidenceFile="workflows/no-such-workflow/WORKFLOW.md"),
            anchor_row("004", EvidenceFile="ScopeOfWork.md"),
        ],
    )
    report = vdr.run(execution_root, families=("EVQ",), instruction_root=instruction_root)

    assert codes(report) == {"EVQ-006": 3}
    assert ids_for(report, "EVQ-006") == ["DEP-01-01-001", "DEP-01-01-002", "DEP-01-01-003"]
    detail = report["findings"][0]["detail"]
    assert "does not resolve under any allowed base" in detail
    for form in ("deliverable ", "working_root ", "instruction_root "):
        assert form in detail
    assert report["evidence_file_resolution_forms"]["deliverable"] == 1


def test_evidence_file_cannot_escape_through_any_base(tmp_path: Path) -> None:
    """`..` that leaves both anchors is not followed, even if the file exists."""
    (tmp_path / "outside.md").write_text("outside\n", encoding="utf-8")
    execution_root, instruction_root = _evidence_fixture(
        tmp_path,
        [
            anchor_row("001", EvidenceFile="../outside.md"),
            anchor_row("002", EvidenceFile="../../../../../../outside.md"),
            anchor_row("003"),
        ],
    )
    report = vdr.run(execution_root, families=("EVQ",), instruction_root=instruction_root)

    assert codes(report) == {"EVQ-006": 2}
    details = [f["detail"] for f in report["findings"]]
    assert any("leaves the working root and is not on the instruction surface" in d
               for d in details)


def test_instruction_root_form_is_limited_to_the_instruction_surface(tmp_path: Path) -> None:
    """SPEC §0.2.4: only agents/, workflows/, tools/, root docs/ and AGENTS.md.

    Checkout-relative paths to project material, or to Root execution records,
    must not resolve through the instruction root; they belong to a working root.
    """
    execution_root, instruction_root = _evidence_fixture(
        tmp_path,
        [
            anchor_row("001", EvidenceFile="projects/demo/docs/SPEC.md"),
            anchor_row("002", EvidenceFile="execution/_ScopeChange/PLAN.csv"),
            anchor_row("003", EvidenceFile="workflows/../projects/demo/docs/SPEC.md"),
            anchor_row("004", EvidenceFile="AGENTS.md"),
            anchor_row("005", EvidenceFile="docs/SPEC.md"),
            anchor_row("006", EvidenceFile="agents/AGENT_TASK.md"),
            anchor_row("007", EvidenceFile="tools/REGISTRY.md"),
            anchor_row("008", EvidenceFile="workflows/dependency-extract/WORKFLOW.md"),
        ],
    )
    for relative in ("AGENTS.md", "docs/SPEC.md", "agents/AGENT_TASK.md", "tools/REGISTRY.md"):
        target = instruction_root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("surface\n", encoding="utf-8")
    report = vdr.run(execution_root, families=("EVQ",), instruction_root=instruction_root)

    assert ids_for(report, "EVQ-006") == ["DEP-01-01-001", "DEP-01-01-002", "DEP-01-01-003"]
    assert report["evidence_file_resolution_forms"]["instruction_root"] == 5


def test_directory_is_not_evidence_in_any_form(tmp_path: Path) -> None:
    execution_root, instruction_root = _evidence_fixture(
        tmp_path,
        [
            anchor_row("001", EvidenceFile="_run_records"),                 # form 1
            anchor_row("002", EvidenceFile="workflows/dependency-extract"),  # form 3
        ],
    )
    report = vdr.run(execution_root, families=("EVQ",), instruction_root=instruction_root)

    assert codes(report) == {"EVQ-006": 2}
    assert all("is a directory, not a file" in f["detail"] for f in report["findings"])


def test_resolution_order_is_deliverable_then_working_root_then_instruction_root(
    tmp_path: Path,
) -> None:
    """Pins the order, including the documented fall-through of a bare name."""
    execution_root, instruction_root = _evidence_fixture(
        tmp_path,
        [
            anchor_row("001", EvidenceFile="README.md"),     # deliverable and project
            anchor_row("002", EvidenceFile="NOTES.md"),      # project only
            anchor_row("003", EvidenceFile="docs/SPEC.md"),  # project and checkout
        ],
    )
    project = execution_root.parent
    deliverable = execution_root / "PKG-01_Core/1_Working/DEL-01-01_Record_tier"
    (deliverable / "README.md").write_text("deliverable\n", encoding="utf-8")
    (project / "README.md").write_text("project\n", encoding="utf-8")
    (project / "NOTES.md").write_text("project\n", encoding="utf-8")
    (project / "docs").mkdir()
    (project / "docs" / "SPEC.md").write_text("project\n", encoding="utf-8")
    (instruction_root / "docs").mkdir()
    (instruction_root / "docs" / "SPEC.md").write_text("root\n", encoding="utf-8")

    report = vdr.run(execution_root, families=("EVQ",), instruction_root=instruction_root)

    assert codes(report) == {}
    assert report["evidence_file_resolution_forms"] == {
        "deliverable": 1, "working_root": 2, "instruction_root": 0,
    }
    assert report["evidence_file_multi_form"] == 2
    assert vdr.resolve_evidence_file(
        "README.md", deliverable, project, instruction_root
    )[0] == "deliverable"
    assert vdr.resolve_evidence_file(
        "NOTES.md", deliverable, project, instruction_root
    )[0] == "working_root"
    assert vdr.resolve_evidence_file(
        "docs/SPEC.md", deliverable, project, instruction_root
    )[2] == ["working_root", "instruction_root"]


def test_instruction_root_environment_variable(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """SPEC §0.2.1: CHIRALITY_INSTRUCTION_ROOT before the tool's own checkout."""
    execution_root, instruction_root = _evidence_fixture(
        tmp_path,
        [anchor_row("001", EvidenceFile="workflows/dependency-extract/WORKFLOW.md")],
    )
    monkeypatch.setenv(INSTRUCTION_ROOT_ENV, str(instruction_root))
    report = vdr.run(execution_root, families=("EVQ",))
    assert report["instruction_root"] == str(instruction_root)
    assert report["instruction_root_source"] == INSTRUCTION_ROOT_ENV
    assert codes(report) == {}

    other = empty_instruction_root(tmp_path)
    overridden = vdr.run(execution_root, families=("EVQ",), instruction_root=other)
    assert overridden["instruction_root_source"] == "argument"
    assert codes(overridden) == {"EVQ-006": 1}

    monkeypatch.setenv(INSTRUCTION_ROOT_ENV, str(tmp_path / "missing"))
    with pytest.raises(vdr.OperationalError):
        vdr.run(execution_root, families=("EVQ",))


def test_default_instruction_root_is_the_checkout_holding_the_tool(tmp_path: Path) -> None:
    execution_root = build_workspace(tmp_path)
    report = vdr.run(execution_root, families=("EVQ",))
    assert report["instruction_root"] == str(VALIDATION_DIR.parent.parent)
    assert report["instruction_root_source"] == "tool checkout"


def test_cli_instruction_root_option(tmp_path: Path) -> None:
    execution_root, instruction_root = _evidence_fixture(
        tmp_path,
        [anchor_row("001", EvidenceFile="workflows/dependency-extract/WORKFLOW.md")],
    )
    resolved = subprocess.run(
        [sys.executable, str(TOOL), str(execution_root), "--families", "EVQ",
         "--instruction-root", str(instruction_root)],
        capture_output=True, text=True,
    )
    assert resolved.returncode == 0, resolved.stdout + resolved.stderr
    assert "instruction-root-relative 1" in resolved.stdout

    bad = subprocess.run(
        [sys.executable, str(TOOL), str(execution_root),
         "--instruction-root", str(tmp_path / "nope")],
        capture_output=True, text=True,
    )
    assert bad.returncode == 2


def test_locus_quote_duplication_detail_is_direction_neutral(tmp_path: Path) -> None:
    """R-09: live hits run both ways; the message must not assert one direction."""
    execution_root = build_workspace(
        tmp_path,
        registers={
            "PKG-01_Core/1_Working/DEL-01-01_Record_tier": [
                # A locus duplicated into the quote column (the reverse of the
                # 'quote pasted into the locus column' case).
                execution_row(SourceRef="PEC-RCN-002 feed list (DL-4)",
                              EvidenceQuote="PEC-RCN-002 feed list (DL-4)"),
            ]
        },
    )
    report = vdr.run(execution_root, families=("EVQ",))

    detail = report["findings"][0]["detail"]
    assert "byte-identical" in detail
    assert "one column is carrying the other's content" in detail
    # Must not name a single causal direction.
    assert "locus column is carrying quote text" not in detail


WAIVER_COLUMNS = list(vdr.WAIVER_COLUMNS)

GOOD_RATIONALE = (
    "Relation derived from register truth; the dag-gate exhibit records no "
    "prose statement of it, so there is no source text to quote."
)


def write_waivers(execution_root: Path, relative: str, rows: list[dict[str, str]],
                  columns: list[str] | None = None) -> None:
    write_csv(execution_root / relative / vdr.WAIVER_FILENAME,
              columns or WAIVER_COLUMNS, rows)


def waiver(dep_id: str = "DEP-01-01-003", check: str = "EVQ-003",
           rationale: str = GOOD_RATIONALE, **overrides: str) -> dict[str, str]:
    row = {
        "DependencyID": dep_id, "WaivedCheck": check, "Rationale": rationale,
        "DeclaredBy": "PEC PROJECT_SETUP", "DeclaredOn": "2026-07-25",
    }
    row.update(overrides)
    return row


def test_valid_waiver_downgrades_to_warning_and_permits_exit_zero(tmp_path: Path) -> None:
    """R-04: an honest-empty row must be declarable without inventing a quote."""
    relative = "PKG-01_Core/1_Working/DEL-01-01_Record_tier"
    execution_root = build_workspace(
        tmp_path,
        registers={relative: [execution_row(SourceRef="location TBD", EvidenceQuote="")]},
    )
    write_waivers(execution_root, relative, [
        waiver(check="EVQ-003"),
        waiver(check="EVQ-004"),
    ])

    report = vdr.run(execution_root, families=("EVQ",))

    assert report["error_count"] == 0
    assert report["warning_count"] == 2
    assert codes(report) == {"EVQ-003": 1, "EVQ-004": 1}
    # The row is downgraded, never hidden.
    assert all(f["severity"] == "WARNING" for f in report["findings"])
    assert all("WAIVED:" in f["detail"] for f in report["findings"])
    assert report["row_class_metrics"]["EXECUTION"]["waived_rows"] == 1
    assert report["row_class_metrics"]["EXECUTION"]["empty_evidence_quote"] == 1

    result = subprocess.run(
        [sys.executable, str(TOOL), str(execution_root), "--families", "EVQ"],
        capture_output=True, text=True,
    )
    assert result.returncode == 0
    assert "waived" in result.stdout
    # --strict still surfaces them.
    strict = subprocess.run(
        [sys.executable, str(TOOL), str(execution_root), "--families", "EVQ", "--strict"],
        capture_output=True, text=True,
    )
    assert strict.returncode == 1


def test_thin_or_placeholder_rationale_is_rejected(tmp_path: Path) -> None:
    relative = "PKG-01_Core/1_Working/DEL-01-01_Record_tier"
    execution_root = build_workspace(
        tmp_path,
        registers={relative: [execution_row(SourceRef="location TBD", EvidenceQuote="")]},
    )
    write_waivers(execution_root, relative, [
        waiver(check="EVQ-003", rationale="n/a"),
        waiver(check="EVQ-004", rationale="no source"),
    ])

    report = vdr.run(execution_root, families=("EVQ",))

    assert codes(report)["EVQ-008"] == 2
    # The underlying findings stay ERROR — a bad waiver softens nothing.
    assert codes(report)["EVQ-003"] == 1
    assert codes(report)["EVQ-004"] == 1
    assert report["error_count"] == 4
    assert report["row_class_metrics"]["EXECUTION"]["waived_rows"] == 0


def test_stale_waiver_is_an_error(tmp_path: Path) -> None:
    relative = "PKG-01_Core/1_Working/DEL-01-01_Record_tier"
    execution_root = build_workspace(
        tmp_path,
        registers={relative: [execution_row()]},  # well-formed row
    )
    write_waivers(execution_root, relative, [waiver(check="EVQ-003")])

    report = vdr.run(execution_root, families=("EVQ",))

    assert codes(report) == {"EVQ-007": 1}
    assert report["error_count"] == 1


def test_malformed_waivers_are_rejected(tmp_path: Path) -> None:
    relative = "PKG-01_Core/1_Working/DEL-01-01_Record_tier"
    execution_root = build_workspace(
        tmp_path,
        registers={relative: [execution_row(SourceRef="location TBD", EvidenceQuote="")]},
    )
    write_waivers(execution_root, relative, [
        waiver(dep_id="DEP-99-99-999"),                 # unknown DependencyID
        waiver(check="EVQ-001"),                        # unwaivable check
        waiver(check="EVQ-004", DeclaredBy=""),         # unattributed
    ])

    report = vdr.run(execution_root, families=("EVQ",))

    assert codes(report)["EVQ-009"] == 3
    assert codes(report)["EVQ-003"] == 1
    assert codes(report)["EVQ-004"] == 1
    assert report["row_class_metrics"]["EXECUTION"]["waived_rows"] == 0


def test_waiver_sidecar_missing_columns_is_rejected(tmp_path: Path) -> None:
    relative = "PKG-01_Core/1_Working/DEL-01-01_Record_tier"
    execution_root = build_workspace(
        tmp_path,
        registers={relative: [execution_row(SourceRef="location TBD", EvidenceQuote="")]},
    )
    write_waivers(
        execution_root, relative,
        [{"DependencyID": "DEP-01-01-003", "WaivedCheck": "EVQ-003"}],
        columns=["DependencyID", "WaivedCheck"],
    )

    report = vdr.run(execution_root, families=("EVQ",))

    assert codes(report)["EVQ-009"] == 1
    assert any("missing required column" in f["detail"] for f in report["findings"])


def test_waiver_cannot_soften_locus_quote_duplication(tmp_path: Path) -> None:
    """EVQ-001 is never waivable: duplication is a defect, not a missing source."""
    relative = "PKG-01_Core/1_Working/DEL-01-01_Record_tier"
    execution_root = build_workspace(
        tmp_path,
        registers={relative: [execution_row(SourceRef="same text", EvidenceQuote="same text")]},
    )
    write_waivers(execution_root, relative, [waiver(check="EVQ-001")])

    report = vdr.run(execution_root, families=("EVQ",))

    assert codes(report)["EVQ-001"] == 1
    assert next(f for f in report["findings"] if f["code"] == "EVQ-001")["severity"] == "ERROR"
    assert codes(report)["EVQ-009"] == 1


def test_strict_promotes_warnings_to_a_failing_exit(tmp_path: Path) -> None:
    execution_root = build_workspace(
        tmp_path,
        registers={
            "PKG-01_Core/1_Working/DEL-01-01_Record_tier": [
                execution_row(SourceRef='§3 notes: "quoted span here"'),
            ],
            "PKG-02_Parsers/1_Working/DEL-02-01_Status_parser": [
                anchor_row("001", DependencyID="DEP-02-01-001", FromPackageID="PKG-02",
                           FromDeliverableID="DEL-02-01", FromDeliverableName="Status parser"),
            ],
        },
    )
    lenient = subprocess.run(
        [sys.executable, str(TOOL), str(execution_root)], capture_output=True, text=True
    )
    assert lenient.returncode == 0
    assert "WARNING EVQ-002" in lenient.stdout

    strict = subprocess.run(
        [sys.executable, str(TOOL), str(execution_root), "--strict"],
        capture_output=True, text=True,
    )
    assert strict.returncode == 1


def test_yaml_project_directs_to_deliverable_cli(tmp_path):
    source = tmp_path / 'PKG-01/DEL-01-01/deliverable.yaml'
    source.parent.mkdir(parents=True)
    source.write_text('id: DEL-01-01\nneeds: []\n')
    with pytest.raises(vdr.OperationalError, match='tools/deliverables/'):
        vdr.run(tmp_path)
