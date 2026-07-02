#!/usr/bin/env python3
"""GEN-8 project-tree machine-absolute-path lint tests (SPEC §0.2.4).

Plan-of-record basis: plan v3 parked-findings row "Machine-absolute-path
lint — Now — Folded into self-check; detect, never rewrite"; audit basis:
`plans/consistency_audit_2026-07-01.md` §4 item 6 (~82 instruction/plan
files carry machine-absolute paths; worst: the app-dev pi-assessment
cluster) and §6 item 5 (relativization when files are next touched).

All machine-absolute fixture content is re-anchored to the synthetic
`/Users/fixture/...` prefix and lives as string constants INSIDE this
`test_`-prefixed module (never loose data files under `tools/`), the same
export-boundary idiom as `test_archive_fixture_corpus.py`.

Severity per TYPES.md §11 / D-GOV-02: REVIEW, one finding per FILE (the
worst live file carries 21 hit lines; per-line findings would flood human
triage). Evidence-marker and unclassified files are counted as facts, never
findings. SPEC §0.2.4 is a DRAFT-track basis, so BLOCK is never emitted.
"""

from __future__ import annotations

from harness_common import Severity, find_claim_language
from test_self_check_fixtures import _findings, _has, _write, build_mini_repo

import cmd_self_check

# --- Fixture material (synthetic /Users/fixture prefix) --------------------------

FIXTURE_ABS = "/Users/fixture/ai-env/projects/example"

PLAN_THREE_HITS_MD = f"""# Fixture assessment plan

Working notes anchored at {FIXTURE_ABS}/notes.md — machine-local anchor.

Repo-relative prose between the hits (must not count).

Second anchor: {FIXTURE_ABS}/plans/other_assessment.md
Third anchor: {FIXTURE_ABS}/execution/run_output.log
"""
PLAN_HIT_LINES = (3, 7, 8)  # ABS_PATH_RE hit lines in the constant above

DECISION_ONE_HIT_MD = f"""# D-99 — fixture ruling record

**Context:** session ran from {FIXTURE_ABS}/worktree — machine-local anchor.
"""

STATUS_ONE_HIT_MD = f"""# Status: DEL-09-01

**Current State:** OPEN
**Working copy:** {FIXTURE_ABS}/execution/DEL-09-01

## History
- 2026-06-30 - State set to OPEN (PREPARATION)
"""

RUN_RECORD_TWO_HITS_MD = f"""# Run record (fixture evidence)

Executed: {FIXTURE_ABS}/tools/run.sh
Output captured at {FIXTURE_ABS}/execution/_run_records/out.log
"""

WORKING_CONTENT_ONE_HIT_MD = f"""# Working content artifact (fixture)

Draft cites a local screenshot at {FIXTURE_ABS}/Desktop/capture.png for now.
"""

APP_DEV = ("projects", "chirality-app-dev")


def _fact(report, fact_id):
    for f in report.facts:
        if f.fact_id == fact_id:
            return f
    raise AssertionError(
        f"fact {fact_id} missing: {[f.fact_id for f in report.facts]}")


def _gen8(report):
    return _findings(report, "ABS_PATH_IN_PROJECT_SURFACE")


# --- (a) plans/ file: ONE per-file REVIEW finding, count + first line -------------

def test_plans_file_yields_one_finding_with_count_and_first_line(tmp_path):
    repo = build_mini_repo(tmp_path)
    _write(repo.joinpath(*APP_DEV, "plans", "fixture_assessment.md"),
           PLAN_THREE_HITS_MD)
    report, _ = cmd_self_check.run_self_check(repo)
    hits = _gen8(report)
    assert [(f.source_path, f.source_line) for f in hits] == [
        ("projects/chirality-app-dev/plans/fixture_assessment.md",
         PLAN_HIT_LINES[0])]  # ONE finding per FILE, anchored at the first hit
    f = hits[0]
    assert f.severity is Severity.REVIEW
    assert f.invariant == "SPEC-0.2.4"
    assert f.dimension == "path-anchoring"
    assert "path segment `plans/`" in f.message  # the classification reason
    assert f"{len(PLAN_HIT_LINES)} machine-absolute-path hit line(s)" in f.message
    assert f"first hit at line {PLAN_HIT_LINES[0]}" in f.message
    assert "repo-relative anchoring" in f.message
    assert "lawfully carry absolute paths" in f.message
    assert "never rewrite" in f.message
    assert "human review required" in f.message
    assert find_claim_language(f.message) == []


# --- (b) _Coordination/_DECISIONS record -> REVIEW --------------------------------

def test_coordination_decision_record_is_instruction_class(tmp_path):
    repo = build_mini_repo(tmp_path)
    _write(repo / "projects" / "chirality-piping" / "execution"
           / "_Coordination" / "_DECISIONS" / "D-99_fixture_ruling.md",
           DECISION_ONE_HIT_MD)
    report, _ = cmd_self_check.run_self_check(repo)
    f = _has(report, "ABS_PATH_IN_PROJECT_SURFACE",
             "_DECISIONS/D-99_fixture_ruling.md", line=3,
             severity=Severity.REVIEW)
    assert "path segment `_Coordination/`" in f.message


# --- (c) _STATUS.md filename pattern -> REVIEW -------------------------------------

def test_status_file_is_instruction_class_by_filename(tmp_path):
    repo = build_mini_repo(tmp_path)
    _write(repo.joinpath(*APP_DEV, "execution", "PKG-09_Fixture",
                         "1_Working", "DEL-09-01_Abs anchor", "_STATUS.md"),
           STATUS_ONE_HIT_MD)
    report, _ = cmd_self_check.run_self_check(repo)
    f = _has(report, "ABS_PATH_IN_PROJECT_SURFACE",
             "DEL-09-01_Abs anchor/_STATUS.md", line=4,
             severity=Severity.REVIEW)
    # No marked segment on this path: the FILENAME pattern is the reason.
    assert "filename pattern match on `_STATUS.md`" in f.message


# --- (d) evidence-marker file: NO finding; counted in the evidence fact -----------

def test_run_record_is_counted_as_evidence_not_finding(tmp_path):
    repo = build_mini_repo(tmp_path)
    _write(repo.joinpath(*APP_DEV, "execution", "_run_records",
                         "run_2026-07-01.md"), RUN_RECORD_TWO_HITS_MD)
    report, _ = cmd_self_check.run_self_check(repo)
    assert _gen8(report) == []
    fact = _fact(report, "abs_path_lint.chirality-app-dev.evidence")
    assert fact.value == "files=1; hit_lines=2"
    assert "permitted by SPEC §0.2.4" in fact.caveat
    assert find_claim_language(fact.caveat) == []


# --- (e) unclassified working surface: NO finding; counted in its fact -------------

def test_working_content_is_counted_as_unclassified_not_finding(tmp_path):
    repo = build_mini_repo(tmp_path)
    _write(repo.joinpath(*APP_DEV, "execution", "PKG-01_Fixture Pkg",
                         "1_Working", "DEL-02-01_Match one",
                         "content_notes.md"), WORKING_CONTENT_ONE_HIT_MD)
    report, _ = cmd_self_check.run_self_check(repo)
    assert _gen8(report) == []
    fact = _fact(report, "abs_path_lint.chirality-app-dev.unclassified")
    assert fact.value == "files=1; hit_lines=1"
    # The honest caveat: the v1 split and the human-triage posture.
    assert "instruction/coordination/plan" in fact.caveat
    assert "not mechanically classifiable in v1" in fact.caveat
    assert "labeled, never guessed" in fact.caveat
    assert "human triage" in fact.caveat
    assert find_claim_language(fact.caveat) == []


# --- (f) clean project: quiet, zero-count facts ------------------------------------

def test_clean_project_tree_yields_no_gen8_findings(tmp_path):
    repo = build_mini_repo(tmp_path)  # project fixtures carry no abs paths
    report, _ = cmd_self_check.run_self_check(repo)
    assert _gen8(report) == []
    for project in ("chirality-app-dev", "chirality-piping"):
        for cls in ("evidence", "unclassified"):
            fact = _fact(report, f"abs_path_lint.{project}.{cls}")
            assert fact.value == "files=0; hit_lines=0"


# --- (g) GEN-1 control-area behavior unchanged (per-line) --------------------------

def test_gen1_control_area_per_line_behavior_unchanged(tmp_path):
    repo = build_mini_repo(tmp_path)
    # Two hit lines in one control-area file -> TWO per-line GEN-1 findings
    # (GEN-8's per-file collapse never reaches the control roots).
    _write(repo / "_DomainEngines" / "TWO_ANCHORS.md",
           f"# two anchors (fixture)\n\nA: {FIXTURE_ABS}/a.md\n"
           f"B: {FIXTURE_ABS}/b.md\n")
    report, _ = cmd_self_check.run_self_check(repo)
    governed = [f for f in _findings(report, "ABS_PATH_IN_GOVERNED_SURFACE")
                if f.source_path.endswith("TWO_ANCHORS.md")]
    assert [f.source_line for f in governed] == [3, 4]
    assert all(f.severity is Severity.REVIEW for f in governed)
    # The mini repo's standing control-area shapes still fire as before.
    _has(report, "ABS_PATH_IN_GOVERNED_SURFACE", "CHANGE_HANDOFF.md", line=3,
         severity=Severity.REVIEW)
    _has(report, "ABS_PATH_IN_EVIDENCE", "open_pipe_stress.validation.json",
         line=5, severity=Severity.INFO)
    # Control-area files never fire the project-surface code, and no GEN-8
    # finding is ever BLOCK.
    assert all(not f.source_path.startswith("_DomainEngines")
               for f in _gen8(report))
    assert all(f.severity is not Severity.BLOCK for f in _gen8(report))
