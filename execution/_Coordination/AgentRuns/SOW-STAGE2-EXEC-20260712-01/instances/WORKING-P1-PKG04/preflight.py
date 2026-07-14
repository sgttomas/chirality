#!/usr/bin/env python3
"""Reproduce the frozen PKG-04 live bindings and physical source-line totals."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
INSTANCE = Path(__file__).resolve().parent
PREFLIGHT = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/W_P1/preflight-r1"
EXPECTED = PREFLIGHT / "EXPECTED_LIVE_BINDINGS.tsv"
OUT = INSTANCE / "LIVE_BINDING_REPRODUCTION.tsv"
SUMMARY = INSTANCE / "PREFLIGHT_SUMMARY.md"
SOURCE_NAMES = {"Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


with EXPECTED.open(newline="") as handle:
    rows = [row for row in csv.DictReader(handle, delimiter="\t") if row["package"] == "PKG-04"]

result = []
line_totals: dict[str, int] = {}
for row in rows:
    path = ROOT / row["live_path"] / row["binding"]
    actual = sha(path) if path.is_file() else "MISSING"
    verdict = "PASS" if actual == row["sha256"] else "FAIL"
    result.append({**row, "actual_sha256": actual, "verdict": verdict})
    if row["binding"] in SOURCE_NAMES:
        line_totals[row["deliverable_id"]] = line_totals.get(row["deliverable_id"], 0) + len(path.read_bytes().splitlines())

fields = list(rows[0]) + ["actual_sha256", "verdict"]
with OUT.open("w", newline="") as handle:
    writer = csv.DictWriter(handle, fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(result)

failures = sum(row["verdict"] != "PASS" for row in result)
expected = {"DEL-04-01": 245, "DEL-04-02": 199, "DEL-04-03": 216, "DEL-04-04": 200, "DEL-04-05": 232, "DEL-04-06": 276}
lines_ok = line_totals == expected
text = [
    "# PKG-04 Preflight Reproduction",
    "",
    f"Binding rows: `{len(result)}`; mismatches: `{failures}`.",
    f"Physical legacy source lines: `{sum(line_totals.values())}`; expected `1,368`; verdict: `{'PASS' if lines_ok else 'FAIL'}`.",
    "",
    "| Member | Physical lines | Batch |",
    "|---|---:|---:|",
]
for did in sorted(line_totals):
    text.append(f"| {did} | {line_totals[did]} | {1 if did <= 'DEL-04-05' else 2} |")
text += [
    "",
    "Batch 1 is `DEL-04-01..05`, five members and 1,092 lines. Batch 2 is",
    "`DEL-04-06`, one member and 276 lines. This is the minimum consecutive",
    "numeric partition under the five-member/2,053-line limits.",
    "",
    "Every source, status, context, reference, dependency-summary, and",
    "dependency-register hash is reproduced row-for-row in",
    "`LIVE_BINDING_REPRODUCTION.tsv`.",
]
SUMMARY.write_text("\n".join(text) + "\n")

if failures or not lines_ok:
    raise SystemExit(1)
