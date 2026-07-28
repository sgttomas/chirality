#!/usr/bin/env python3
"""Compare accepted and Gate-3 candidate Section 8/9 traceability."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path


SCA = Path(__file__).resolve().parent
BASIS = "c487b7dd57a378e2f74417118e78e7f61a161629"
DECOMP = Path(
    "projects/chirality-app-dev/execution/_Decomposition/"
    "Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
)
CANDIDATE = SCA / "Candidate_Tree" / DECOMP

TERMINAL = {
    "SOW-002": {"DEL-02-03", "DEL-07-01"},
    "SOW-023": {"DEL-02-05", "DEL-09-06"},
    "SOW-064": {"DEL-06-02", "DEL-06-03"},
    "SOW-075": {"DEL-01-01", "DEL-07-01"},
    "SOW-076": {"DEL-01-04", "DEL-04-02"},
    "SOW-077": {"DEL-01-04", "DEL-07-06"},
    "SOW-078": {"DEL-01-04", "DEL-09-04"},
}


def repo_root() -> Path:
    for parent in [SCA, *SCA.parents]:
        if (parent / ".git").exists():
            return parent
    raise RuntimeError("repository root not found")


def cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def parse(text: str) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    reverse: dict[str, set[str]] = defaultdict(set)
    ledger: dict[str, set[str]] = {}
    section = ""
    for line in text.splitlines():
        if line == "## 8. Deliverables":
            section = "deliverables"
            continue
        if line == "## 9. Scope Ledger":
            section = "ledger"
            continue
        if line.startswith("## 10."):
            section = ""
        row = cells(line) if line.startswith("|") else []
        if section == "deliverables" and len(row) == 10 and re.fullmatch(r"DEL-\d{2}-\d{2}", row[0]):
            for sow_id in re.findall(r"\bSOW-\d{3}\b", row[6]):
                reverse[sow_id].add(row[0])
        elif section == "ledger" and len(row) == 10 and re.fullmatch(r"SOW-\d{3}", row[0]):
            ledger[row[0]] = set(re.findall(r"\bDEL-\d{2}-\d{2}\b", row[5]))
    return dict(reverse), ledger


def mismatches(reverse: dict[str, set[str]], ledger: dict[str, set[str]]) -> dict[str, object]:
    return {
        sow_id: {
            "section_8": sorted(reverse.get(sow_id, set())),
            "section_9": sorted(ledger.get(sow_id, set())),
        }
        for sow_id in sorted(set(reverse) | set(ledger))
        if reverse.get(sow_id, set()) != ledger.get(sow_id, set())
    }


def edges(mapping: dict[str, set[str]]) -> set[tuple[str, str]]:
    return {(sow_id, del_id) for sow_id, values in mapping.items() for del_id in values}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    root = repo_root()
    accepted = subprocess.check_output(
        ["git", "show", f"{BASIS}:{DECOMP.as_posix()}"],
        cwd=root,
        text=True,
    )
    candidate = CANDIDATE.read_text(encoding="utf-8")
    before_reverse, before_ledger = parse(accepted)
    after_reverse, after_ledger = parse(candidate)

    before_mismatches = mismatches(before_reverse, before_ledger)
    after_mismatches = mismatches(after_reverse, after_ledger)
    added_reverse = edges(after_reverse) - edges(before_reverse)
    deleted_reverse = edges(before_reverse) - edges(after_reverse)
    added_ledger = edges(after_ledger) - edges(before_ledger)
    deleted_ledger = edges(before_ledger) - edges(after_ledger)

    errors: list[str] = []
    if set(before_mismatches) != set(TERMINAL):
        errors.append("accepted-basis mismatch set is not the expected seven scope IDs")
    if after_mismatches:
        errors.append("candidate has Section 8/9 mismatches")
    if deleted_reverse or deleted_ledger:
        errors.append("candidate deletes supported relations")
    for sow_id, expected in TERMINAL.items():
        if after_reverse.get(sow_id) != expected or after_ledger.get(sow_id) != expected:
            errors.append(f"{sow_id} does not match the terminal relation")

    result = {
        "status": "PASS" if not errors else "FAIL",
        "basis_commit": BASIS,
        "accepted_mismatch_scope_ids": sorted(before_mismatches),
        "accepted_mismatch_count": len(before_mismatches),
        "candidate_mismatch_count": len(after_mismatches),
        "candidate_mismatches": after_mismatches,
        "added_section_8_relations": sorted([list(edge) for edge in added_reverse]),
        "added_section_9_relations": sorted([list(edge) for edge in added_ledger]),
        "deleted_section_8_relations": sorted([list(edge) for edge in deleted_reverse]),
        "deleted_section_9_relations": sorted([list(edge) for edge in deleted_ledger]),
        "terminal_relations": {key: sorted(value) for key, value in TERMINAL.items()},
        "errors": errors,
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.write_report:
        (SCA / "Gate_3_Traceability_Comparison.json").write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
