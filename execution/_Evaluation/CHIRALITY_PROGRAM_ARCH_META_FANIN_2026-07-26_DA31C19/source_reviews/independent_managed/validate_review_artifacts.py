#!/usr/bin/env python3
"""Deterministic schema and evidence validation for tandem-review returns."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path


REPO = Path("/Users/ryan/.codex/worktrees/d9d0/chirality")
EVAL = REPO / "execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_TANDEM_2026-07-26_DA31C19"
FREEZE = "da31c19b5656dd74615e308c4215688971d33dc9"
MANIFEST_PATH = EVAL / "FROZEN_BASIS_MANIFEST.json"
EXPECTED_MANIFEST_SHA256 = "f569d994156f9585fd100286e43b325116ae473616b1d1bd4f169bd88d632386"

FINDINGS_HEADER = [
    "FindingID",
    "ProductSurface",
    "Assertion",
    "EvidenceRefs",
    "Class",
    "Severity",
    "Consequence",
    "SmallestAction",
    "Owner",
    "Confidence",
]
TRACE_HEADER = [
    "TraceRowID",
    "Product",
    "SourceLayer",
    "SourceID",
    "SourceAssertion",
    "DownstreamRefs",
    "Disposition",
    "Notes",
]
BOUNDARY_HEADER = [
    "BoundaryRowID",
    "Function",
    "SemanticOwner",
    "Producers",
    "Consumers",
    "AuthoritativeRecord",
    "CompatibilityObligation",
    "FallbackBehavior",
    "ChangeRoute",
    "Disposition",
    "EvidenceRefs",
]
CHALLENGE_HEADER = [
    "ChallengeID",
    "TargetFindingID",
    "Disposition",
    "Assertion",
    "EvidenceRefs",
    "Consequence",
    "Confidence",
]

FINDING_CLASSES = {
    "AUTHORITY_CONFLICT",
    "TRACE_GAP",
    "OWNERSHIP_GAP",
    "SEMANTIC_CONFLICT",
    "OMISSION",
    "OVERREACH",
    "OBSERVATION",
    "UNKNOWN",
    "ASSUMPTION",
}
SEVERITIES = {"BLOCK", "REVIEW", "WARN", "INFO"}
CONFIDENCES = {"HIGH", "MEDIUM", "LOW", "UNKNOWN"}
TRACE_DISPOSITIONS = {
    "TRACED",
    "PARTIAL",
    "GAP",
    "AMBIGUOUS",
    "DEFERRED",
    "SUPERSEDED",
    "NOT_APPLICABLE",
    "UNKNOWN",
}
BOUNDARY_DISPOSITIONS = {
    "EXPLICIT",
    "PARTIAL",
    "CONFLICT",
    "GAP",
    "CANDIDATE_ONLY",
    "NOT_APPLICABLE",
    "UNKNOWN",
}
CHALLENGE_DISPOSITIONS = {
    "CONFIRM",
    "REFUTE",
    "NARROW",
    "ADD-MISSING-EVIDENCE",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_csv(path: Path, expected_header: list[str], checks: list[str]) -> list[dict[str, str]]:
    try:
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != expected_header:
                checks.append(
                    f"FAIL {path.name}: header {reader.fieldnames!r} != {expected_header!r}"
                )
                return []
            rows = list(reader)
    except Exception as exc:
        checks.append(f"FAIL {path.name}: CSV parse error: {exc}")
        return []
    if not rows:
        checks.append(f"FAIL {path.name}: no data rows")
    else:
        checks.append(f"PASS {path.name}: {len(rows)} data rows")
    for number, row in enumerate(rows, start=2):
        if None in row:
            checks.append(f"FAIL {path.name}:{number}: non-rectangular row")
        for field in expected_header:
            if row.get(field) is None:
                checks.append(f"FAIL {path.name}:{number}: missing field {field}")
    return rows


def unique_nonempty(rows: list[dict[str, str]], field: str, label: str, checks: list[str]) -> None:
    values = [row.get(field, "").strip() for row in rows]
    if any(not value for value in values):
        checks.append(f"FAIL {label}: empty {field}")
    elif len(values) != len(set(values)):
        checks.append(f"FAIL {label}: duplicate {field}")
    else:
        checks.append(f"PASS {label}: unique non-empty {field}")


def evidence_valid(
    evidence: str,
    manifest_paths: set[str],
    tree_paths: set[str],
) -> bool:
    if not evidence.strip():
        return False
    if evidence.strip().upper() in {"UNKNOWN", "ASSUMPTION"}:
        return True
    if "da31c19" not in evidence:
        return False
    candidates = re.findall(r"da31c19(?:b5656dd74615e308c4215688971d33dc9)?\:([^#;|,\"]+)", evidence)
    if not candidates:
        return False
    for candidate in candidates:
        path = candidate.strip()
        if path not in manifest_paths and path not in tree_paths:
            return False
    return True


def git_tree_paths() -> set[str]:
    result = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", FREEZE],
        cwd=REPO,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    )
    return set(result.stdout.splitlines())


def validate_pass1(reviewer: str, target: Path) -> dict:
    checks: list[str] = []
    required = [
        target / "REPORT.md",
        target / "FINDINGS.csv",
        target / "TRACE_MATRIX.csv",
        target / "BOUNDARY_MATRIX.csv",
        target / "RETURN_MANIFEST.json",
    ]
    for path in required:
        checks.append(f"{'PASS' if path.is_file() else 'FAIL'} required file: {path.name}")
    if not all(path.is_file() for path in required):
        return finish("PASS1", reviewer, target, checks, {})

    findings = load_csv(target / "FINDINGS.csv", FINDINGS_HEADER, checks)
    traces = load_csv(target / "TRACE_MATRIX.csv", TRACE_HEADER, checks)
    boundaries = load_csv(target / "BOUNDARY_MATRIX.csv", BOUNDARY_HEADER, checks)
    unique_nonempty(findings, "FindingID", "FINDINGS", checks)
    unique_nonempty(traces, "TraceRowID", "TRACE_MATRIX", checks)
    unique_nonempty(boundaries, "BoundaryRowID", "BOUNDARY_MATRIX", checks)

    finding_prefix = f"{reviewer}-F-"
    if findings and all(row["FindingID"].startswith(finding_prefix) for row in findings):
        checks.append(f"PASS FINDINGS: reviewer prefix {finding_prefix}")
    else:
        checks.append(f"FAIL FINDINGS: reviewer prefix {finding_prefix}")

    enum_checks = [
        ("FINDINGS Class", findings, "Class", FINDING_CLASSES),
        ("FINDINGS Severity", findings, "Severity", SEVERITIES),
        ("FINDINGS Confidence", findings, "Confidence", CONFIDENCES),
        ("TRACE Disposition", traces, "Disposition", TRACE_DISPOSITIONS),
        ("BOUNDARY Disposition", boundaries, "Disposition", BOUNDARY_DISPOSITIONS),
    ]
    for label, rows, field, allowed in enum_checks:
        invalid = sorted({row[field] for row in rows if row[field] not in allowed})
        checks.append(
            f"{'PASS' if not invalid else 'FAIL'} {label}: "
            + ("valid" if not invalid else f"invalid={invalid}")
        )

    manifest = json.loads(MANIFEST_PATH.read_text())
    manifest_paths = {entry["path"] for entry in manifest["entries"]}
    tree_paths = git_tree_paths()
    invalid_finding_evidence = [
        row["FindingID"]
        for row in findings
        if not evidence_valid(row["EvidenceRefs"], manifest_paths, tree_paths)
    ]
    checks.append(
        f"{'PASS' if not invalid_finding_evidence else 'FAIL'} finding evidence anchors: "
        + ("all valid" if not invalid_finding_evidence else ",".join(invalid_finding_evidence))
    )
    invalid_boundary_evidence = [
        row["BoundaryRowID"]
        for row in boundaries
        if not evidence_valid(row["EvidenceRefs"], manifest_paths, tree_paths)
    ]
    checks.append(
        f"{'PASS' if not invalid_boundary_evidence else 'FAIL'} boundary evidence anchors: "
        + ("all valid" if not invalid_boundary_evidence else ",".join(invalid_boundary_evidence))
    )

    products = {row["Product"].strip().upper() for row in traces}
    for product in ("ROOT", "APP", "PEC"):
        checks.append(
            f"{'PASS' if product in products else 'FAIL'} trace product coverage: {product}"
        )

    report = (target / "REPORT.md").read_text(encoding="utf-8")
    report_lower = report.lower()
    required_report_phrases = {
        "basis attestation": ["basis attestation"],
        "independent orientation": ["independent orientation"],
        "root coverage": ["root"],
        "app coverage": ["app"],
        "pec coverage": ["pec"],
        "cross-product": ["cross-product", "cross product"],
        "disclosed conditions": ["disclosed-condition", "disclosed condition"],
        "unknowns": ["unknown"],
        "recommendations": ["recommendation"],
        "no score": ["no score", "not scored"],
    }
    for label, alternatives in required_report_phrases.items():
        present = any(phrase in report_lower for phrase in alternatives)
        checks.append(f"{'PASS' if present else 'FAIL'} report section/content: {label}")

    for population in ("45", "53", "64", "32"):
        checks.append(
            f"{'PASS' if population in report else 'FAIL'} report population attestation: {population}"
        )

    boundary_text = " ".join(
        " ".join(row.values()).lower() for row in boundaries
    )
    boundary_concepts = {
        "root": "root",
        "app": "app",
        "pec": "pec",
        "human": "human",
        "domain truth": "domain",
        "runtime": "runtime",
        "fallback": "fallback",
        "notice/drift": "drift",
    }
    for label, token in boundary_concepts.items():
        checks.append(
            f"{'PASS' if token in boundary_text else 'FAIL'} boundary concept: {label}"
        )
    checks.append(
        f"{'PASS' if len(boundaries) >= 16 else 'FAIL'} boundary row minimum: {len(boundaries)} >= 16"
    )

    high_rows = [row for row in findings if row["Severity"] in {"BLOCK", "REVIEW"}]
    incomplete_high = [
        row["FindingID"]
        for row in high_rows
        if not all(
            row[field].strip()
            for field in ("Consequence", "SmallestAction", "Owner", "Confidence")
        )
    ]
    checks.append(
        f"{'PASS' if not incomplete_high else 'FAIL'} high-severity completeness: "
        + ("complete" if not incomplete_high else ",".join(incomplete_high))
    )

    try:
        return_manifest = json.loads((target / "RETURN_MANIFEST.json").read_text())
        checks.append("PASS RETURN_MANIFEST.json: valid JSON")
    except Exception as exc:
        checks.append(f"FAIL RETURN_MANIFEST.json: {exc}")
        return_manifest = {}
    if return_manifest.get("reviewer_id") == reviewer:
        checks.append("PASS RETURN_MANIFEST reviewer identity")
    else:
        checks.append("FAIL RETURN_MANIFEST reviewer identity")
    if return_manifest.get("review_freeze") == FREEZE:
        checks.append("PASS RETURN_MANIFEST review freeze")
    else:
        checks.append("FAIL RETURN_MANIFEST review freeze")
    if return_manifest.get("input_manifest_sha256") == EXPECTED_MANIFEST_SHA256:
        checks.append("PASS RETURN_MANIFEST input manifest")
    else:
        checks.append("FAIL RETURN_MANIFEST input manifest")

    declared_outputs = return_manifest.get("outputs", {})
    for filename in ("REPORT.md", "FINDINGS.csv", "TRACE_MATRIX.csv", "BOUNDARY_MATRIX.csv"):
        actual_path = target / filename
        declaration = declared_outputs.get(filename, {})
        good = (
            declaration.get("sha256") == sha256(actual_path)
            and declaration.get("bytes") == actual_path.stat().st_size
        )
        checks.append(
            f"{'PASS' if good else 'FAIL'} RETURN_MANIFEST hash/bytes: {filename}"
        )
    if return_manifest.get("other_reviewer_consulted") is False:
        checks.append("PASS independence attestation")
    else:
        checks.append("FAIL independence attestation")

    details = {
        "finding_count": len(findings),
        "high_severity_count": len(high_rows),
        "trace_row_count": len(traces),
        "boundary_row_count": len(boundaries),
        "output_hashes": {path.name: sha256(path) for path in required},
    }
    return finish("PASS1", reviewer, target, checks, details)


def validate_challenge(
    reviewer: str,
    target: Path,
    other_findings_path: Path,
) -> dict:
    checks: list[str] = []
    required = [
        target / "REPORT.md",
        target / "CHALLENGE.csv",
        target / "RETURN_MANIFEST.json",
    ]
    for path in required:
        checks.append(f"{'PASS' if path.is_file() else 'FAIL'} required file: {path.name}")
    if not all(path.is_file() for path in required):
        return finish("CHALLENGE", reviewer, target, checks, {})

    challenges = load_csv(target / "CHALLENGE.csv", CHALLENGE_HEADER, checks)
    unique_nonempty(challenges, "ChallengeID", "CHALLENGE", checks)
    invalid_dispositions = sorted(
        {row["Disposition"] for row in challenges if row["Disposition"] not in CHALLENGE_DISPOSITIONS}
    )
    checks.append(
        f"{'PASS' if not invalid_dispositions else 'FAIL'} challenge dispositions: "
        + ("valid" if not invalid_dispositions else f"invalid={invalid_dispositions}")
    )
    invalid_confidence = sorted(
        {row["Confidence"] for row in challenges if row["Confidence"] not in CONFIDENCES}
    )
    checks.append(
        f"{'PASS' if not invalid_confidence else 'FAIL'} challenge confidence: "
        + ("valid" if not invalid_confidence else f"invalid={invalid_confidence}")
    )

    other_checks: list[str] = []
    other_findings = load_csv(other_findings_path, FINDINGS_HEADER, other_checks)
    if any(item.startswith("FAIL") for item in other_checks):
        checks.extend(other_checks)
    target_by_id = {row["FindingID"]: row for row in other_findings}
    challenged_ids = [row["TargetFindingID"] for row in challenges]
    unknown_ids = sorted(set(challenged_ids) - set(target_by_id))
    duplicate_ids = sorted(
        finding_id for finding_id in set(challenged_ids) if challenged_ids.count(finding_id) > 1
    )
    checks.append(
        f"{'PASS' if not unknown_ids else 'FAIL'} challenge target IDs: "
        + ("valid" if not unknown_ids else ",".join(unknown_ids))
    )
    checks.append(
        f"{'PASS' if not duplicate_ids else 'FAIL'} one challenge per target: "
        + ("unique" if not duplicate_ids else ",".join(duplicate_ids))
    )

    high_ids = sorted(
        row["FindingID"] for row in other_findings if row["Severity"] in {"BLOCK", "REVIEW"}
    )
    lower_ids = sorted(
        row["FindingID"] for row in other_findings if row["Severity"] in {"WARN", "INFO"}
    )
    lower_sample_size = max(1, (len(lower_ids) + 3) // 4) if lower_ids else 0
    required_ids = set(high_ids + lower_ids[:lower_sample_size])
    missing_required = sorted(required_ids - set(challenged_ids))
    checks.append(
        f"{'PASS' if not missing_required else 'FAIL'} required challenge coverage: "
        + ("complete" if not missing_required else ",".join(missing_required))
    )

    manifest = json.loads(MANIFEST_PATH.read_text())
    manifest_paths = {entry["path"] for entry in manifest["entries"]}
    tree_paths = git_tree_paths()
    invalid_evidence = [
        row["ChallengeID"]
        for row in challenges
        if not evidence_valid(row["EvidenceRefs"], manifest_paths, tree_paths)
    ]
    checks.append(
        f"{'PASS' if not invalid_evidence else 'FAIL'} challenge evidence anchors: "
        + ("all valid" if not invalid_evidence else ",".join(invalid_evidence))
    )

    report = (target / "REPORT.md").read_text(encoding="utf-8").lower()
    for label, token in {
        "basis": "basis",
        "method": "method",
        "coverage": "coverage",
        "blind spots": "blind spot",
        "divergence": "diverg",
        "no consensus": "consensus",
    }.items():
        checks.append(
            f"{'PASS' if token in report else 'FAIL'} challenge report content: {label}"
        )

    try:
        return_manifest = json.loads((target / "RETURN_MANIFEST.json").read_text())
        checks.append("PASS RETURN_MANIFEST.json: valid JSON")
    except Exception as exc:
        checks.append(f"FAIL RETURN_MANIFEST.json: {exc}")
        return_manifest = {}
    if return_manifest.get("reviewer_id") == reviewer:
        checks.append("PASS challenge reviewer identity")
    else:
        checks.append("FAIL challenge reviewer identity")
    if return_manifest.get("review_freeze") == FREEZE:
        checks.append("PASS challenge review freeze")
    else:
        checks.append("FAIL challenge review freeze")
    declared_outputs = return_manifest.get("outputs", {})
    for filename in ("REPORT.md", "CHALLENGE.csv"):
        actual_path = target / filename
        declaration = declared_outputs.get(filename, {})
        good = (
            declaration.get("sha256") == sha256(actual_path)
            and declaration.get("bytes") == actual_path.stat().st_size
        )
        checks.append(
            f"{'PASS' if good else 'FAIL'} challenge manifest hash/bytes: {filename}"
        )

    details = {
        "challenge_count": len(challenges),
        "required_target_ids": sorted(required_ids),
        "output_hashes": {path.name: sha256(path) for path in required},
    }
    return finish("CHALLENGE", reviewer, target, checks, details)


def finish(stage: str, reviewer: str, target: Path, checks: list[str], details: dict) -> dict:
    failures = [check for check in checks if check.startswith("FAIL")]
    return {
        "schema": "chirality.tandem-review.validation.v1",
        "stage": stage,
        "reviewer": reviewer,
        "target": str(target),
        "verdict": "PASS" if not failures else "FAIL",
        "failure_count": len(failures),
        "checks": checks,
        "details": details,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="stage", required=True)
    pass1_parser = subparsers.add_parser("pass1")
    pass1_parser.add_argument("reviewer", choices=["A", "B"])
    pass1_parser.add_argument("target", type=Path)
    challenge_parser = subparsers.add_parser("challenge")
    challenge_parser.add_argument("reviewer", choices=["A", "B"])
    challenge_parser.add_argument("target", type=Path)
    challenge_parser.add_argument("other_findings", type=Path)
    args = parser.parse_args()

    if sha256(MANIFEST_PATH) != EXPECTED_MANIFEST_SHA256:
        raise SystemExit("Frozen basis manifest hash mismatch")
    if args.stage == "pass1":
        result = validate_pass1(args.reviewer, args.target)
    else:
        result = validate_challenge(args.reviewer, args.target, args.other_findings)
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["verdict"] == "PASS" else 1)


if __name__ == "__main__":
    main()
