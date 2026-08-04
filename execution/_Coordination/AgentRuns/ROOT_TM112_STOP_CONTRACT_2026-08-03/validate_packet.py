#!/usr/bin/env python3
"""Deterministic structural/currentness checks for ROOT_TM112_STOP_CONTRACT."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
RUN = Path(__file__).resolve().parent

EXPECTED = {
    "execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/OWNER_RULING_TRANSCRIPT_2026-08-03.md": "66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06",
    "execution/_Coordination/AgentRuns/ROOT_TM112_DECISION_PREP_2026-08-03/instances/H1-TM112-INVESTIGATION/evidence/raw/CONTROLLED_RESULTS.json": "cc2d703a32899e905ee44455f32a75f0ac7c79ca912d7dd4e2e181201f903ea2",
    "runtime/packages/daemon/src/runtime-daemon.ts": "a6bb6b2388bbca084640611d15f4186b3c98379776001e2335b96831cebe2d46",
    "runtime/tests/daemon.test.ts": "bbcfcabb48dd7c4b5c5e0645b14601efd89404e34a5cdde322a0bef5b22a693e",
    "runtime/package.json": "499cb55afb26bdbaa36f85178c28d392bfa2527b60a002e4eb0ae0e076402071",
    "runtime/package-lock.json": "4105799bbdb8a1b5025a71a0098e460281f8e6db62b1a912d37aade2935a7c0f",
    "docs/DIRECTIVE.md": "83daac8c93022fb1c11430487c80d430f90b3f27b10a74d3aeb93dade3403ca6",
    "docs/CONTRACT.md": "6271cac33a7cd97d9d13143e17951ac63544763a0f1fd832cebdd2ca1d64d4e6",
    "docs/SPEC.md": "988c4b90287753d1249f53d01838819028ecb959a8fa1cbecf873e50c0fb62db",
    "docs/TYPES.md": "e37ee85a1e3ae044c07670a1285c29d4ca8fa83853acd89abea0b4afcb5b4fe2",
}

REQUIRED = [
    "ORCHESTRATION_PLAN.md",
    "WORK_GRAPH.json",
    "OWNER_SEMANTIC_DECISION_PACKET.md",
    "SEMANTIC_OPTIONS.json",
    "CANDIDATE_NORMATIVE_CLAUSES.md",
    "IMPLEMENTATION_TEST_SCOPE_MAP.md",
    "RISKS_AND_CAVEATS.md",
    "OWNER_RETURN_TEMPLATES.md",
    "REFUTATION_DISPOSITION.md",
    "VALIDATION.md",
    "MANAGER_RETURN.md",
    "HANDOFF_STATE.md",
    "instances/E1-NODE-BEHAVIOR/LAUNCH_BRIEF.md",
    "instances/E1-NODE-BEHAVIOR/RETURN.md",
    "instances/E1-NODE-BEHAVIOR/EVIDENCE.md",
    "instances/E2-CONTRACT-MAP/LAUNCH_BRIEF.md",
    "instances/E2-CONTRACT-MAP/RETURN.md",
    "instances/E2-CONTRACT-MAP/SOURCE_CONTRACT_MAP.md",
    "instances/E3-INDEPENDENT-REFUTER/LAUNCH_BRIEF.md",
    "instances/E3-INDEPENDENT-REFUTER/REFUTATION.md",
    "instances/E3-INDEPENDENT-REFUTER/RETURN.md",
    "instances/E4-REFUTATION-BACKCHECK/LAUNCH_BRIEF.md",
    "instances/E4-REFUTATION-BACKCHECK/DISPATCH_INPUT.md",
    "instances/E4-REFUTATION-BACKCHECK/BACKCHECK.md",
    "instances/E4-REFUTATION-BACKCHECK/RETURN.md",
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fail(message: str) -> None:
    print(f"BLOCK: {message}")
    raise SystemExit(1)


for relative in REQUIRED:
    if not (RUN / relative).is_file():
        fail(f"required output missing: {relative}")

for relative, expected in EXPECTED.items():
    actual = digest(ROOT / relative)
    if actual != expected:
        fail(f"basis drift: {relative}: {actual} != {expected}")

options = json.loads((RUN / "SEMANTIC_OPTIONS.json").read_text())
if options.get("signature") is not None or options.get("status") != "UNSIGNED_PROPOSAL":
    fail("selection form is signed or not an unsigned proposal")

all_ids: set[str] = set()
for dimension in options["dimensions"]:
    if dimension.get("cardinality") != "EXACTLY_ONE":
        fail(f"invalid cardinality: {dimension.get('id')}")
    ids = [option["id"] for option in dimension["options"]]
    if len(ids) < 2 or len(ids) != len(set(ids)):
        fail(f"incomplete/duplicate options: {dimension.get('id')}")
    if all_ids.intersection(ids):
        fail(f"option IDs overlap dimensions: {dimension.get('id')}")
    all_ids.update(ids)

recommended = options["recommendedSelection"]
if recommended != ["G2", "C1", "F1"] or not set(recommended).issubset(all_ids):
    fail("recommended selection is missing or incoherent")
fixed = options["fixedConsequences"]
if fixed.get("connectionGovernedTerminationMs") != "SELECTED_PRODUCTION_GRACE_MS_PLUS_500":
    fail("connection bound is not derived from selected grace")
if fixed.get("startDuringStart") != "REJECT" or fixed.get("startDuringStop") != "REJECT":
    fail("structured concurrent-start/stop parity missing")

clauses = (RUN / "CANDIDATE_NORMATIVE_CLAUSES.md").read_text()
packet = (RUN / "OWNER_SEMANTIC_DECISION_PACKET.md").read_text()
scope = (RUN / "IMPLEMENTATION_TEST_SCOPE_MAP.md").read_text()
for token in ["NON-AUTHORITATIVE", "2,000 milliseconds", "N-STOP-7"]:
    if token not in clauses:
        fail(f"candidate clause token missing: {token}")
for token in ["G2 + C1 + F1", "IMPLEMENTATION HELD", "semantic acceptance **and** an accepted repair"]:
    if token not in packet:
        fail(f"packet hold/recommendation token missing: {token}")
for case in [
    "Idle", "Completed keep-alive", "Incomplete ordinary request", "Live SSE",
    "Bounded termination", "Disconnect/interrupt", "Socket and owner cleanup", "Restart"
]:
    if f"| {case} |" not in scope:
        fail(f"approved test case absent: {case}")

head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
origin = subprocess.check_output(["git", "rev-parse", "origin/main"], cwd=ROOT, text=True).strip()
if head != "88e7590d3664d4f1daf91bed2a8899bda0748b92" or origin != head:
    fail(f"revision drift: HEAD={head}, origin/main={origin}")

node = subprocess.check_output(["node", "--version"], cwd=ROOT, text=True).strip()
if node != "v24.18.0":
    fail(f"installed Node drift: {node}")

print("PASS: required outputs present")
print("PASS: authority, evidence, source, tests, runtime manifests, and Root canon hashes current")
print("PASS: three exactly-one dimensions have unique option IDs; recommendation G2/C1/F1 is coherent")
print("PASS: candidate is visibly non-authoritative and implementation/App-notice holds are explicit")
print("PASS: all eight owner-approved regression cases are mapped")
print(f"PASS: HEAD/origin-main current at {head}; installed Node {node}")
