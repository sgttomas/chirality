#!/usr/bin/env python3
"""Validate the complete SCA-APP-006 Gate-3 candidate without applying it."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import tempfile
from collections import Counter, defaultdict
from pathlib import Path


SCA = Path(__file__).resolve().parent
DECOMP_PATH = Path(
    "projects/chirality-app-dev/execution/_Decomposition/"
    "Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
)
CONTRACT_PATH = Path("projects/chirality-app-dev/docs/CONTRACT.md")
PRD_PATH = Path("projects/chirality-app-dev/docs/PRD.md")
OPEN_ITEMS_PATH = Path(
    "docs/governance_harness/_PROPOSALS/"
    "D-GOV-28_root_runtime_stewardship/OPEN_ITEMS.csv"
)
BASIS_COMMIT = "c487b7dd57a378e2f74417118e78e7f61a161629"
BASIS_DECOMP_SHA = (
    "69b3110c26cb0b435ced4144845282bf6905cde4c0474b21282b9a1806984946"
)
CONTRACT_SHA = (
    "6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7"
)
PRD_SHA = "ef638f43ccae1cd78b26b1ae078a33770cf64cc36c247c5d7da04b35196a4010"
CANDIDATE_DECOMP_SHA = (
    "dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83"
)
CANDIDATE_REGISTER_SHA = (
    "84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1"
)

CANDIDATE_DECOMP = SCA / "Candidate_Tree" / DECOMP_PATH
CANDIDATE_REGISTER = (
    SCA
    / "Candidate_Tree"
    / "projects"
    / "chirality-app-dev"
    / "execution"
    / "_Decomposition"
    / "contract_invariant_coverage_register.csv"
)
PATCH = SCA / "Gate_3_Exact_Decomposition.patch"
UNRESOLVED = (
    SCA
    / "Agent2_Returns"
    / "Register_Mapper"
    / "UNRESOLVED_MAPPINGS.csv"
)
ENUMS = SCA / "Register_Enums.json"

SCHEMA = [
    "InvariantID",
    "InvariantFamily",
    "SourcePath",
    "SourceAnchor",
    "ContractSourceSHA256",
    "SemanticOwnerProduct",
    "OwnerAuthorityRef",
    "OwnerAuthorityBasis",
    "AppObligationClass",
    "AppPackageIDs",
    "AppDeliverableIDs",
    "EnforcementSurfaces",
    "ValidationSurfaces",
    "OpenIssueIDs",
    "CoverageStatus",
    "ProvenanceStatus",
    "RationaleEvidenceAnchor",
    "AppDecompositionBasis",
]

EXPECTED_RELATIONS = {
    "SOW-002": {"DEL-02-03", "DEL-07-01"},
    "SOW-023": {"DEL-02-05", "DEL-09-06"},
    "SOW-064": {"DEL-06-02", "DEL-06-03"},
    "SOW-075": {"DEL-01-01", "DEL-07-01"},
    "SOW-076": {"DEL-01-04", "DEL-04-02"},
    "SOW-077": {"DEL-01-04", "DEL-07-06"},
    "SOW-078": {"DEL-01-04", "DEL-09-04"},
}
EXPECTED_UNKNOWNS = {
    "K-PERM-1",
    "K-PERM-2",
    "K-PERM-3",
    "K-PERM-4",
    "K-PERM-5",
    "K-HOOK-1",
    "K-BASH-1",
    "K-SUBAGENT-1",
    "K-SUBAGENT-2",
    "K-KEY-1",
    "K-DOMAIN-1",
    "K-DOMAIN-2",
    "K-DOMAIN-3",
    "K-DOMAIN-4",
}


def repo_root() -> Path:
    for parent in [SCA, *SCA.parents]:
        if (parent / ".git").exists():
            return parent
    raise RuntimeError("repository root not found")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def split_ids(value: str) -> set[str]:
    if value in {"", "NONE"}:
        return set()
    return {part.strip() for part in value.split(";") if part.strip()}


def table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def exact_ids(text: str, prefix: str) -> set[str]:
    pattern = {
        "PKG": r"\bPKG-\d{2}\b",
        "DEL": r"\bDEL-\d{2}-\d{2}\b",
        "SOW": r"\bSOW-\d{3}\b",
        "OBJ": r"\bOBJ-\d{3}\b",
    }[prefix]
    return set(re.findall(pattern, text))


def defined_ids(text: str, prefix: str) -> set[str]:
    pattern = {
        "PKG": r"^\|\s*(PKG-\d{2})\s*\|",
        "DEL": r"^\|\s*(DEL-\d{2}-\d{2})\s*\|",
        "SOW": r"^\|\s*(SOW-\d{3})\s*\|",
        "OBJ": r"^\|\s*(OBJ-\d{3})\s*\|",
    }[prefix]
    return set(re.findall(pattern, text, re.M))


def parse_relations(text: str) -> tuple[dict[str, set[str]], dict[str, set[str]], dict[str, str]]:
    reverse: dict[str, set[str]] = defaultdict(set)
    ledger: dict[str, set[str]] = {}
    statuses: dict[str, str] = {}
    in_deliverables = False
    in_ledger = False
    for line in text.splitlines():
        if line == "## 8. Deliverables":
            in_deliverables, in_ledger = True, False
            continue
        if line == "## 9. Scope Ledger":
            in_deliverables, in_ledger = False, True
            continue
        if line.startswith("## 10."):
            in_deliverables, in_ledger = False, False
        cells = table_cells(line) if line.startswith("|") else []
        if in_deliverables and len(cells) == 10 and re.fullmatch(r"DEL-\d{2}-\d{2}", cells[0]):
            for sow_id in re.findall(r"\bSOW-\d{3}\b", cells[6]):
                reverse[sow_id].add(cells[0])
        if in_ledger and len(cells) == 10 and re.fullmatch(r"SOW-\d{3}", cells[0]):
            ledger[cells[0]] = set(re.findall(r"\bDEL-\d{2}-\d{2}\b", cells[5]))
            statuses[cells[0]] = cells[1]
    return dict(reverse), ledger, statuses


def source_invariants(contract: str) -> tuple[dict[str, tuple[str, int]], set[str]]:
    rows: dict[str, tuple[str, int]] = {}
    for line_no, line in enumerate(contract.splitlines(), 1):
        match = re.match(r"^\|\s*\*\*(K-[A-Z0-9]+-\d+)\*\*\s*\|", line)
        if match:
            inv_id = match.group(1)
            rows[inv_id] = (re.sub(r"-\d+$", "", inv_id), line_no)
    return rows, {family for family, _ in rows.values()}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    root = repo_root()
    errors: list[str] = []
    warnings: list[str] = []
    checks: dict[str, object] = {}

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    basis_decomp = subprocess.check_output(
        ["git", "show", f"{BASIS_COMMIT}:{DECOMP_PATH.as_posix()}"],
        cwd=root,
    )
    contract_bytes = subprocess.check_output(
        ["git", "show", f"{BASIS_COMMIT}:{CONTRACT_PATH.as_posix()}"],
        cwd=root,
    )
    prd_bytes = subprocess.check_output(
        ["git", "show", f"{BASIS_COMMIT}:{PRD_PATH.as_posix()}"],
        cwd=root,
    )
    require(sha256_bytes(basis_decomp) == BASIS_DECOMP_SHA, "basis decomposition hash")
    require(sha256_bytes(contract_bytes) == CONTRACT_SHA, "CONTRACT hash")
    require(sha256_bytes(prd_bytes) == PRD_SHA, "PRD hash")
    require(sha256(CANDIDATE_DECOMP) == CANDIDATE_DECOMP_SHA, "candidate decomposition hash")
    require(sha256(CANDIDATE_REGISTER) == CANDIDATE_REGISTER_SHA, "candidate register hash")

    with tempfile.TemporaryDirectory(prefix="sca-app-006-gate3-") as tmp:
        temp = Path(tmp)
        target = temp / DECOMP_PATH
        target.parent.mkdir(parents=True)
        target.write_bytes(basis_decomp)
        applied = subprocess.run(
            ["patch", "-p1", "--batch", "--forward", "-i", str(PATCH)],
            cwd=temp,
            text=True,
            capture_output=True,
        )
        require(applied.returncode == 0, f"patch reproduction: {applied.stderr.strip()}")
        if target.exists():
            require(target.read_bytes() == CANDIDATE_DECOMP.read_bytes(), "patch/candidate identity")

    contract = contract_bytes.decode("utf-8")
    candidate_text = CANDIDATE_DECOMP.read_text(encoding="utf-8")
    source_rows, source_families = source_invariants(contract)
    require(len(source_rows) == 81, "source CONTRACT invariant count")
    require(len(source_families) == 48, "source CONTRACT family count")

    with CANDIDATE_REGISTER.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        require(reader.fieldnames == SCHEMA, "register schema")
        rows = list(reader)
    row_ids = [row["InvariantID"] for row in rows]
    require(len(rows) == 81, "register row count")
    require(len(set(row_ids)) == 81, "register ID uniqueness")
    require(set(row_ids) == set(source_rows), "register exact invariant population")
    require({row["InvariantFamily"] for row in rows} == source_families, "register family population")

    enum_values = json.loads(ENUMS.read_text(encoding="utf-8"))
    package_ids = defined_ids(candidate_text, "PKG")
    deliverable_ids = defined_ids(candidate_text, "DEL")
    issue_ids = set(re.findall(r"^\|\s*(OI-\d{3})\s*\|", candidate_text, re.M))
    open_item_text = subprocess.check_output(
        ["git", "show", f"{BASIS_COMMIT}:{OPEN_ITEMS_PATH.as_posix()}"],
        cwd=root,
        text=True,
    )
    issue_ids.update(re.findall(r"^(RUNTIME-OPEN-\d{3}),", open_item_text, re.M))
    candidate_basis = f"{DECOMP_PATH.as_posix()}#candidate-sha256={CANDIDATE_DECOMP_SHA}"

    unknown_rows: set[str] = set()
    for row in rows:
        inv_id = row["InvariantID"]
        family, line_no = source_rows[inv_id]
        require(row["InvariantFamily"] == family, f"{inv_id}: family")
        require(row["SourcePath"] == CONTRACT_PATH.as_posix(), f"{inv_id}: source path")
        require(row["ContractSourceSHA256"] == CONTRACT_SHA, f"{inv_id}: source hash")
        require(f":L{line_no}#{inv_id}" in row["SourceAnchor"], f"{inv_id}: source anchor")
        require(row["AppDecompositionBasis"] == candidate_basis, f"{inv_id}: candidate basis")
        for field, allowed in enum_values.items():
            require(row[field] in allowed, f"{inv_id}: {field} enum")
        require(split_ids(row["AppPackageIDs"]) <= package_ids, f"{inv_id}: package ref")
        require(split_ids(row["AppDeliverableIDs"]) <= deliverable_ids, f"{inv_id}: deliverable ref")
        require(split_ids(row["ValidationSurfaces"]) <= deliverable_ids, f"{inv_id}: validation ref")
        require(split_ids(row["OpenIssueIDs"]) <= issue_ids, f"{inv_id}: open-issue ref")
        if row["SemanticOwnerProduct"] == "APP":
            require(row["OwnerAuthorityBasis"] == "APP_CONTRACT_AND_DECOMPOSITION", f"{inv_id}: App owner basis")
            require(row["ProvenanceStatus"] == "DIRECT_APP_AUTHORITY", f"{inv_id}: App provenance")
        elif row["SemanticOwnerProduct"] == "ROOT":
            require(row["OwnerAuthorityBasis"] == "ROOT_RULED_CONTINUING_STEWARDSHIP", f"{inv_id}: Root owner basis")
            require(row["ProvenanceStatus"] == "EXTERNAL_ROOT_AUTHORITY", f"{inv_id}: Root provenance")
            require("D-GOV-20" in row["OwnerAuthorityRef"] and "D-GOV-28" in row["OwnerAuthorityRef"], f"{inv_id}: Root authority refs")
            require("D-GOV-28_root_runtime_stewardship.md#Effects" in row["OwnerAuthorityRef"], f"{inv_id}: Root authority anchor")
            require("#Outcome" not in row["OwnerAuthorityRef"], f"{inv_id}: stale Root authority anchor")
        else:
            unknown_rows.add(inv_id)
            require("UNRESOLVED" in row["OwnerAuthorityBasis"] or "FUTURE_BOUNDARY" in row["OwnerAuthorityBasis"], f"{inv_id}: unknown basis")
            require("UNRESOLVED" in row["CoverageStatus"] or "FUTURE_BOUNDARY" in row["CoverageStatus"], f"{inv_id}: unknown coverage")

    with UNRESOLVED.open(newline="", encoding="utf-8") as handle:
        unresolved_ids = {row["InvariantID"] for row in csv.DictReader(handle)}
    require(unknown_rows == EXPECTED_UNKNOWNS, "exact UNKNOWN semantic-owner set")
    require(unresolved_ids == EXPECTED_UNKNOWNS, "unresolved register exact set")
    warnings.append(f"{len(unknown_rows)} semantic owners remain explicit UNKNOWN")

    source_text = basis_decomp.decode("utf-8")
    for prefix, expected in (("PKG", 10), ("DEL", 51), ("SOW", 78), ("OBJ", 10)):
        before = defined_ids(source_text, prefix)
        after = defined_ids(candidate_text, prefix)
        require(before == after, f"{prefix} stable-ID population")
        require(len(after) == expected, f"{prefix} expected count")

    reverse, ledger, statuses = parse_relations(candidate_text)
    relation_diffs = {
        sow_id: {
            "section_8": sorted(reverse.get(sow_id, set())),
            "section_9": sorted(ledger.get(sow_id, set())),
        }
        for sow_id in sorted(set(reverse) | set(ledger))
        if reverse.get(sow_id, set()) != ledger.get(sow_id, set())
    }
    require(not relation_diffs, "Section 8 / Section 9 relation parity")
    for sow_id, expected in EXPECTED_RELATIONS.items():
        require(ledger.get(sow_id) == expected, f"{sow_id}: terminal relation")
    for sow_id in ("SOW-065", "SOW-076", "SOW-077", "SOW-078"):
        require(statuses.get(sow_id) == "OUT", f"{sow_id}: OUT preserved")

    require(candidate_text.count("| DEC-022 |") == 1, "DEC-022 exact row count")
    require(f"`{PRD_SHA}`" in candidate_text, "REF-006 refreshed")
    require("exactly 81 CONTRACT invariant IDs in 48 families" in candidate_text, "live register statement")
    require("Remote MCP, plugins, and marketplace scope remain excluded" in candidate_text, "SOW-064 exclusion")
    require("SOW-023" in candidate_text and "DEL-02-05" in candidate_text, "SOW-023 UI carrier")

    owner_counts = Counter(row["SemanticOwnerProduct"] for row in rows)
    coverage_counts = Counter(row["CoverageStatus"] for row in rows)
    checks.update(
        {
            "basis_commit": BASIS_COMMIT,
            "basis_decomposition_sha256": BASIS_DECOMP_SHA,
            "contract_sha256": CONTRACT_SHA,
            "prd_sha256": PRD_SHA,
            "candidate_decomposition_sha256": CANDIDATE_DECOMP_SHA,
            "candidate_register_sha256": CANDIDATE_REGISTER_SHA,
            "register_rows": len(rows),
            "invariant_families": len(source_families),
            "semantic_owner_counts": dict(sorted(owner_counts.items())),
            "coverage_counts": dict(sorted(coverage_counts.items())),
            "unknown_semantic_owner_ids": sorted(unknown_rows),
            "relation_differences": relation_diffs,
            "topology": {"packages": 10, "deliverables": 51, "scope_items": 78, "objectives": 10},
        }
    )
    report = {
        "status": "PASS_WITH_EXPLICIT_UNKNOWNS" if not errors else "FAIL",
        "checks": checks,
        "warnings": warnings,
        "errors": errors,
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.write_report:
        (SCA / "Gate_3_Validation.json").write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
