#!/usr/bin/env python3
"""Validate an SCC Resolution Case folder in either case home.

The default home is `{EXECUTION_ROOT}/_DAG/cases/<CASE-ID>/` (D-GOV-49;
docs/SPEC.md §1.2, §5.4), where the folder name is the case's stable
`SCC-CASE-NNN` ID. A project whose cases are already held in a legacy PKG-00
control deliverable (`.../scc-cases/<case>/`) keeps that home; a case outside
`_DAG/` is validated exactly as before.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "Case_Contract.md",
    "Case_Datasheet.md",
    "Task_Findings.csv",
    "Evidence_Register.csv",
    "Candidate_Remedies.csv",
    "Ruling_Register.csv",
    "Open_Questions.md",
    "Owner_Workflow_Handoff.md",
    "Case_QA.md",
]

TASK_FINDINGS_COLUMNS = [
    "FindingID",
    "SourceTaskRun",
    "AffectedDeliverables",
    "FindingType",
    "Summary",
    "EvidenceRefs",
    "Status",
]

EVIDENCE_COLUMNS = [
    "EvidenceID",
    "SourcePath",
    "SourceRef",
    "EvidenceType",
    "Supports",
    "Notes",
]

CANDIDATE_REMEDY_COLUMNS = [
    "RemedyID",
    "IssueOrEdge",
    "RemedyType",
    "OwnerWorkflow",
    "AffectedDeliverables",
    "EvidenceRefs",
    "HumanRuling",
    "Status",
    "TBDReason",
]

RULING_COLUMNS = [
    "RulingID",
    "QuestionID",
    "Ruling",
    "RulingBy",
    "Date",
    "EvidenceRefs",
    "Status",
]

HANDOFF_COLUMNS = [
    "HandoffID",
    "OwnerWorkflow",
    "TriggerCondition",
    "PayloadPath",
    "ExpectedOutput",
    "Status",
]

CASE_STATES = {
    "OPEN_FOR_TASK_WORK",
    "EVIDENCE_ACCUMULATING",
    "HUMAN_RULINGS_PENDING",
    "REMEDY_CLASSIFIED",
    "READY_FOR_OWNER_WORKFLOWS",
    "DEP_CLOSURE_PENDING",
    "CLOSED_BY_DEPCLOSURE",
    "BLOCKED_TBD",
}

OWNER_WORKFLOWS = {
    "WORKING_ITEMS",
    "TASK",
    "DEPENDENCY_WORKFLOW",
    "SCOPE_CHANGE",
    "RECONCILIATION",
    "DEPCLOSURE",
    "PROJECT_SETUP",
    # legacy value retained because immutable historical SCC artifacts carry it; new cases use PROJECT_SETUP (D-GOV-18)
    "ORCHESTRATOR",
    "CHANGE",
    "TBD",
}

LEGACY_CONTROL_DELIVERABLE = "PKG-00_DAG_Closure_and_Project_Control"

# D-GOV-49 case identity: the next unused three-digit number, never reused.
DAG_CASE_ID = re.compile(r"^SCC-CASE-(\d{3})$")
DAG_CASE_NUMBER = re.compile(r"^SCC-CASE-(\d{3})(?!\d)", re.IGNORECASE)

FORBIDDEN_CLAIMS = [
    "SCC closure achieved",
    "strict graph is acyclic",
    "project-wide BLOCKED/UNBLOCKED is reportable",
    "dependency rows updated",
    "dependency rows changed",
    "Dependencies.csv updated",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def split_refs(value: str) -> list[str]:
    refs: list[str] = []
    for chunk in value.replace(",", ";").split(";"):
        token = chunk.strip()
        if token and token != "TBD":
            refs.append(token)
    return refs


def find_execution_root(case_path: Path) -> Path | None:
    for parent in [case_path, *case_path.parents]:
        if parent.name == "execution":
            return parent
    return None


def dag_cases_root(case_path: Path) -> Path | None:
    """The `_DAG/cases/` folder containing (or equal to) `case_path`, or None."""
    for parent in [case_path, *case_path.parents]:
        if parent.name == "cases" and parent.parent.name == "_DAG":
            return parent
    return None


def dag_home_errors(case_path: Path, cases_root: Path) -> list[str]:
    """Location, identity and single-home checks for a case under `_DAG/cases/`."""
    if case_path == cases_root:
        return ["path is the _DAG/cases/ home, not a case folder; pass _DAG/cases/<CASE-ID>/"]
    errors: list[str] = []
    if case_path.parent != cases_root:
        errors.append(
            "a case under _DAG/ must be a folder directly under _DAG/cases/: "
            f"{case_path.relative_to(cases_root).as_posix()}"
        )
    else:
        match = DAG_CASE_ID.match(case_path.name)
        if not match:
            errors.append(f"folder name {case_path.name!r} is not a case ID of the form SCC-CASE-NNN (D-GOV-49)")
        else:
            for sibling in sorted(cases_root.iterdir()):
                other = DAG_CASE_NUMBER.match(sibling.name)
                if sibling.is_dir() and sibling != case_path and other and other.group(1) == match.group(1):
                    errors.append(f"another folder in _DAG/cases/ uses case number {match.group(1)}: {sibling.name}")
    if any(cases_root.rglob("Dependencies.csv")):
        errors.append("_DAG/cases/ contains Dependencies.csv; SCC cases must not add dependency registers")
    if (cases_root / "_run_records").exists():
        errors.append("_DAG/cases/_run_records/ exists; run records belong under <CASE_PATH>/_run_records/")
    execution_root = cases_root.parent.parent
    legacy = sorted(
        folder.relative_to(execution_root).as_posix()
        for folder in execution_root.glob("PKG-00*/**/scc-cases")
        if folder.is_dir() and any(child.is_dir() for child in folder.iterdir())
    )
    if legacy:
        errors.append(
            f"project also holds SCC cases in a legacy PKG-00 home ({'; '.join(legacy)}); each project uses one case home"
        )
    return errors


def require_columns(
    errors: list[str], path: Path, expected: list[str]
) -> tuple[list[str], list[dict[str, str]]]:
    fields, rows = read_csv(path)
    missing = [col for col in expected if col not in fields]
    if missing:
        errors.append(f"{path.name} missing columns: {', '.join(missing)}")
    return fields, rows


def validate_case(case_path: Path) -> list[str]:
    errors: list[str] = []
    case_path = case_path.resolve()
    if not case_path.is_dir():
        return [f"case path is not a directory: {case_path}"]

    cases_root = dag_cases_root(case_path)
    if cases_root is not None:
        errors.extend(dag_home_errors(case_path, cases_root))
        if case_path == cases_root:
            return errors

    missing = [f"missing required file: {name}" for name in REQUIRED_FILES if not (case_path / name).is_file()]
    if missing:
        return errors + missing

    _, findings = require_columns(errors, case_path / "Task_Findings.csv", TASK_FINDINGS_COLUMNS)
    _, evidence = require_columns(errors, case_path / "Evidence_Register.csv", EVIDENCE_COLUMNS)
    _, remedies = require_columns(errors, case_path / "Candidate_Remedies.csv", CANDIDATE_REMEDY_COLUMNS)
    _, rulings = require_columns(errors, case_path / "Ruling_Register.csv", RULING_COLUMNS)
    _, handoffs = require_columns(errors, case_path / "Owner_Workflow_Handoff.md", HANDOFF_COLUMNS)

    evidence_ids = {row.get("EvidenceID", "").strip() for row in evidence}
    evidence_ids.discard("")
    if not evidence_ids:
        errors.append("Evidence_Register.csv has no evidence rows")

    for idx, row in enumerate(findings, start=2):
        for ref in split_refs(row.get("EvidenceRefs", "")):
            if ref not in evidence_ids:
                errors.append(f"Task_Findings.csv row {idx} unknown EvidenceRef={ref}")

    for idx, row in enumerate(remedies, start=2):
        refs = split_refs(row.get("EvidenceRefs", ""))
        tbd_reason = row.get("TBDReason", "").strip()
        if not refs and not tbd_reason:
            errors.append(f"Candidate_Remedies.csv row {idx} needs EvidenceRefs or TBDReason")
        for ref in refs:
            if ref not in evidence_ids:
                errors.append(f"Candidate_Remedies.csv row {idx} unknown EvidenceRef={ref}")
        owner = row.get("OwnerWorkflow", "").strip()
        if owner not in OWNER_WORKFLOWS:
            errors.append(f"Candidate_Remedies.csv row {idx} invalid OwnerWorkflow={owner!r}")

    for idx, row in enumerate(rulings, start=2):
        for ref in split_refs(row.get("EvidenceRefs", "")):
            if ref not in evidence_ids:
                errors.append(f"Ruling_Register.csv row {idx} unknown EvidenceRef={ref}")

    for idx, row in enumerate(handoffs, start=2):
        owner = row.get("OwnerWorkflow", "").strip()
        if owner not in OWNER_WORKFLOWS:
            errors.append(f"Owner_Workflow_Handoff.md row {idx} invalid OwnerWorkflow={owner!r}")

    datasheet = read_text(case_path / "Case_Datasheet.md")
    qa = read_text(case_path / "Case_QA.md")
    states_seen = [state for state in CASE_STATES if state in datasheet or state in qa]
    if not states_seen:
        errors.append("case state not found in Case_Datasheet.md or Case_QA.md")
    if "CLOSED_BY_DEPCLOSURE" in states_seen and "DepClosure" not in qa:
        errors.append("CLOSED_BY_DEPCLOSURE requires cited DepClosure evidence in Case_QA.md")

    combined_text = "\n".join(read_text(case_path / filename) for filename in REQUIRED_FILES if filename.endswith(".md"))
    for phrase in FORBIDDEN_CLAIMS:
        if phrase in combined_text:
            errors.append(f"forbidden positive closure/mutation claim found: {phrase}")
    if (case_path / "case-seeds").exists():
        seed_text = combined_text.lower()
        if "seed evidence" not in seed_text:
            errors.append("case-seeds present but case text does not label seeds as evidence")

    if cases_root is not None:
        if case_path.parent == cases_root and case_path.name not in datasheet:
            errors.append(f"Case_Datasheet.md does not record the case ID {case_path.name}")
        return errors

    execution_root = find_execution_root(case_path)
    if execution_root:
        pkg00 = execution_root / LEGACY_CONTROL_DELIVERABLE
        if pkg00.exists() and any(pkg00.rglob("Dependencies.csv")):
            errors.append("PKG-00 contains Dependencies.csv; SCC cases must not add dependency registers")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case_path", help="SCC resolution case folder: _DAG/cases/<CASE-ID>/ or a legacy PKG-00 scc-cases/<case>/")
    args = parser.parse_args()

    errors = validate_case(Path(args.case_path))
    if errors:
        print("FAIL: SCC resolution case validation")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: SCC resolution case validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
