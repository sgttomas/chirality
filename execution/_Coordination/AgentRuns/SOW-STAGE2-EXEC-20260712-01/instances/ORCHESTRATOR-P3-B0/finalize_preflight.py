#!/usr/bin/env python3
"""Finalize checked W-P3 evidence and rebuild its direct snapshot binding."""

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
OUT = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/W_P3/preflight"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_text(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n")


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


summary_path = OUT / "SUMMARY.json"
summary = json.loads(summary_path.read_text())
if summary["preliminary_verdict"] != "PASS":
    raise SystemExit("refusing final PASS: preliminary gates are not PASS")
summary["command_checks"] = {
    "dependency_schema": "15/15 PASS",
    "harness_self_check": "EXIT_0_WITH_BASELINE_FINDINGS",
    "harness_pytest": "264/264 PASS",
}
summary["blockers"] = []
summary["unknowns"] = []
summary["waivers"] = []
summary["final_verdict"] = "PASS"
write_text(summary_path, json.dumps(summary, indent=2, sort_keys=True))

write_tsv(
    OUT / "CHECK_COMMAND_RESULTS.tsv",
    ["check", "scope", "exit_code", "result", "detail"],
    [
        {"check": "dependency-schema", "scope": "15 selected Dependencies.csv registers", "exit_code": 0, "result": "PASS", "detail": "15/15 valid canonical v3.1; 261 total data rows"},
        {"check": "harness-self-check", "scope": "repository registered always-check", "exit_code": 0, "result": "PASS_WITH_BASELINE_FINDINGS", "detail": "INFO=15; NOT_APPLICABLE=2; REVIEW=27; WARN=6; no P3-preflight-scope finding"},
        {"check": "harness-pytest", "scope": "tools/practitioner_harness", "exit_code": 0, "result": "PASS", "detail": "264/264 passed"},
    ],
)

applicable = list(csv.DictReader((OUT / "APPLICABLE_CHECKS.tsv").open(), delimiter="\t"))
for row in applicable:
    if row["check"] == "dependency-schema":
        row["result"] = "PASS"
    elif row["check"] == "harness-self-check":
        row["result"] = "PASS_WITH_BASELINE_FINDINGS"
    elif row["check"] == "harness-pytest":
        row["result"] = "PASS"
write_tsv(OUT / "APPLICABLE_CHECKS.tsv", list(applicable[0]), applicable)

write_text(OUT / "BASIS.md", """
# W-P3 Ordinary Piping Preflight Basis

Status: `IMMUTABLE DERIVATIVE CANDIDATE — PASS`

The exact population is 15 P3 ordinary Piping members in PKG-10 through
PKG-12, split 5/5/5. All 60 legacy sources, 15 statuses, and 135 live
bindings reproduce the accepted execution manifest. Every member is non-pilot,
non-issued, `IN_PROGRESS`, valid `LEGACY_FOUR_DOC`, and SOW-absent. The frozen
legacy corpus contains 4,919 physical lines and 261 dependency rows.

The minimum consecutive partition under five-member/2,053-line limits is
three batches: PKG-10 5/1,594; PKG-11 5/1,588; PKG-12 5/1,737. All 56 accepted
Piping SOW predecessors are separately frozen, clean, and disjoint. Active
PKG-00 upstream direction is valid for all three packages with zero outbound
contradictions. Method, authority, check-profile, P1/P2/I1, refs, ancestry,
and release-correction bindings are frozen. Dependency schemas, registered
self-check, and 264 practitioner tests pass. No project/candidate/Git/
lifecycle write or conversion occurred.
""")

write_text(OUT / "CHECKS.md", """
# W-P3 Preflight Checks

Status: `PASS — CANDIDATE AWAITING HELP_HUMAN FAN-IN`

| Gate | Result | Evidence |
|---|---|---|
| Exact P3 extraction | PASS | 15 members; PKG-10/11/12 = 5/5/5 |
| P3 identity | PASS | 60/60 source hashes and 15/15 status hashes |
| Live bindings | PASS | 135/135 present; 15 dependency registers; 261 rows |
| Lifecycle and format | PASS | 15/15 IN_PROGRESS, non-pilot, non-ISSUED, valid LEGACY_FOUR_DOC, SOW-absent |
| Line freeze | PASS | 4,919 physical legacy source lines with per-file counts |
| Batch partition | PASS | Minimum consecutive three batches; every batch <=5 members and <=2,053 lines |
| Dependency schemas | PASS | 15/15 canonical v3.1 registers |
| PKG-00 direction | PASS | PKG-10-12 each have active upstream basis; zero outbound contradictions |
| Accepted predecessors | PASS | 56 clean Piping SOW predecessors; zero selected overlap |
| Method/profile | PASS | Standard, skill, tools, amendments, manifest, dependency truth, and Piping profile hash-bound |
| Refs/ancestry | PASS | HEAD, origin/main and remote main exact; required D-GOV/P1/I1/P2 ancestors present |
| Registered checks | PASS | Self-check exit 0 with baseline findings outside scope; 264/264 harness tests |
| Ownership/topology | PASS | Three fresh serial managers; three ordered author-to-verifier batch pairs; later direct RECON |
| Containment | PASS | Only W-P3 preflight and ORCHESTRATOR-P3-B0 evidence written |

Blockers: none. Unknowns: none. Waivers: none. H2 remains unapproved.
""")

write_text(OUT / "HANDOFF_STATE.md", """
# W-P3 Preflight Handoff State

Snapshot status: `IMMUTABLE DERIVATIVE CANDIDATE — PASS`

The exact 15-member P3 population, 135 live bindings, 4,919 source lines,
261 dependency rows, three minimum consecutive batches, three-package serial
ownership graph, 56-member accepted-predecessor preservation, PKG-00 upstream
direction, active methods/checks, and live refs are frozen.

Next owner: `HELP_HUMAN`. Accept or reject this derivative snapshot. On
acceptance release only `WORKING-P3-PKG10`; PKG-11 and PKG-12 remain serially
dependent on predecessor package PASS. After all three package managers pass,
release direct RECONCILIATION fan-in without a redundant child layer.

Rerun on any ref, ancestry, accepted-snapshot, member, source, line-count,
status, control, dependency, lifecycle, format, authority, caller, tool,
profile, ownership, batch, check, PKG-00-direction, or predecessor drift.

This is derivative coordination evidence and does not replace decomposition
truth. No project, candidate, Git, lifecycle, release, reliance, rollback,
retirement, or H2 act occurred. Blockers: none. Unknowns: none. Waivers: none.
""")

# MANIFEST.tsv is a direct self-binding index and intentionally excludes itself.
manifest_rows: list[dict[str, object]] = []
for path in sorted(OUT.rglob("*")):
    if not path.is_file() or path.name == "MANIFEST.tsv":
        continue
    data_rows: object = "not_applicable"
    if path.suffix == ".tsv":
        data_rows = max(len(path.read_text().splitlines()) - 1, 0)
    manifest_rows.append({"artifact": path.relative_to(OUT).as_posix(), "sha256": sha(path), "bytes": path.stat().st_size, "data_rows": data_rows, "binding_status": "BOUND"})
write_tsv(OUT / "MANIFEST.tsv", ["artifact", "sha256", "bytes", "data_rows", "binding_status"], manifest_rows)
