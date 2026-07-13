#!/usr/bin/env python3
"""Reproduce deterministic candidate checklists for all ten D-GOV-15 pilots."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
TOOL = ROOT / "tools/scope_of_work/derive_review_checklist.py"
INSTANCE = Path(__file__).resolve().parent
OUTPUT_ROOT = INSTANCE / "evidence/checklists"
SUMMARY = INSTANCE / "evidence/TEN_PILOT_CHECKLIST_REPRODUCTION.json"
VARIANCE = "D-GOV-15@58aa81d62f4a32e3c2d687e4356a1e4be8141674"
PILOT_ROOTS = (
    Path("/Users/ryan/ai-env/projects/chirality-sow-app-pilot/projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working"),
    Path("/Users/ryan/ai-env/projects/chirality-sow-piping-pilot/projects/chirality-piping/execution/PKG-13_Physical Design Knowledge and Constraint Engine/1_Working"),
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    candidates = sorted(path for root in PILOT_ROOTS for path in root.glob("DEL-*/ScopeOfWork.md"))
    if len(candidates) != 10:
        print(f"ERROR: expected 10 pilot candidates, found {len(candidates)}", file=sys.stderr)
        return 1
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    results: list[dict[str, object]] = []
    with tempfile.TemporaryDirectory() as temporary:
        temp_root = Path(temporary)
        for candidate in candidates:
            first = temp_root / (candidate.parent.name + "-1.json")
            second = temp_root / (candidate.parent.name + "-2.json")
            command = [
                sys.executable,
                str(TOOL),
                str(candidate),
                "--pilot-variance",
                "--variance-ref",
                VARIANCE,
            ]
            for output in (first, second):
                completed = subprocess.run([*command, "--output", str(output)], text=True, capture_output=True)
                if completed.returncode:
                    print(completed.stderr, file=sys.stderr, end="")
                    return completed.returncode
            first_bytes = first.read_bytes()
            if first_bytes != second.read_bytes():
                print(f"ERROR: nondeterministic checklist for {candidate}", file=sys.stderr)
                return 1
            report = json.loads(first_bytes)
            deliverable_id = report["source"]["deliverable_id"]
            if report["source"]["sha256"] != sha256(candidate.read_bytes()):
                print(f"ERROR: source hash mismatch for {candidate}", file=sys.stderr)
                return 1
            if report["item_count"] != len(report["items"]) or not report["items"]:
                print(f"ERROR: missing checklist items for {candidate}", file=sys.stderr)
                return 1
            output = OUTPUT_ROOT / f"{deliverable_id}.json"
            output.write_bytes(first_bytes)
            results.append(
                {
                    "deliverable_id": deliverable_id,
                    "source_sha256": report["source"]["sha256"],
                    "checklist_sha256": sha256(first_bytes),
                    "item_count": report["item_count"],
                    "criterion_ids": [item["id"] for item in report["items"]],
                    "deterministic_repeat": True,
                    "variance_ref": report["source"]["variance_ref"],
                }
            )
    summary = {
        "schema": "chirality-stage1-checklist-reproduction/v1",
        "tool": "tools/scope_of_work/derive_review_checklist.py",
        "variance_ref": VARIANCE,
        "pilot_count": len(results),
        "all_deterministic": all(item["deterministic_repeat"] for item in results),
        "pilots": results,
    }
    SUMMARY.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"PASS pilots={len(results)} deterministic={summary['all_deterministic']} summary={SUMMARY}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
