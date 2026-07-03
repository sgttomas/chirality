#!/usr/bin/env python3
"""coord-check fixture tests."""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

import cmd_coord_check
import harness
from harness_common import GENERATED_ROOT_NAME, Severity
from test_brief_adoption import _git
from test_self_check_fixtures import _write

requires_git = pytest.mark.skipif(shutil.which("git") is None,
                                  reason="git not available")


def _repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    _write(repo / ".gitignore", GENERATED_ROOT_NAME + "/\n")
    _write(repo / "_DomainEngines" / "bridge" / "existing.md",
           "# Existing bridge artifact\n")
    _write(repo / "projects" / "chirality-piping" / "execution"
           / "_Coordination" / "_DECISIONS" / "_REGISTER.md",
           "# Register\n\n| ID | Decision | State |\n|---|---|---|\n"
           "| D-31 | Fixture packet | RULED |\n")
    _git(repo, "init", "-q")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", "initial")
    return repo


def _codes(report):
    return {f.code for f in report.findings}


@requires_git
def test_coord_check_clean_packet_with_register_precedent_and_resolved_ref(tmp_path):
    repo = _repo(tmp_path)
    base = _git(repo, "rev-parse", "HEAD")
    _write(repo / "projects" / "chirality-piping" / "execution"
           / "_Coordination" / "_DECISIONS" / "D-31_fixture_packet.md",
           "# D-31 fixture packet\n\n"
           "Precedent: D-28 packet skeleton.\n\n"
           "Source: `_DomainEngines/bridge/existing.md`\n")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", "packet")

    report = cmd_coord_check.run_coord_check(repo, f"{base}..HEAD")

    assert report.findings == []
    assert report.summary["coordination_paths"] == 1
    assert report.extras["coord_check"]["coordination_paths"][0]["path"].endswith(
        "D-31_fixture_packet.md")


@requires_git
def test_coord_check_flags_missing_ref_register_row_and_precedent(tmp_path):
    repo = _repo(tmp_path)
    base = _git(repo, "rev-parse", "HEAD")
    _write(repo / "projects" / "chirality-piping" / "execution"
           / "_Coordination" / "_DECISIONS" / "D-32_missing_packet.md",
           "# D-32 missing packet\n\n"
           "Source: `_DomainEngines/bridge/missing.md`\n")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", "bad packet")

    report = cmd_coord_check.run_coord_check(repo, f"{base}..HEAD")

    assert _codes(report) == {
        "COORD_UNRESOLVED_REF",
        "COORD_REGISTER_ROW_MISSING",
        "COORD_PRECEDENT_NOT_NAMED",
    }
    assert all(f.severity is Severity.REVIEW for f in report.findings)


@requires_git
def test_coord_check_generated_root_ref_is_info_and_cli_wired(tmp_path, capsys):
    repo = _repo(tmp_path)
    base = _git(repo, "rev-parse", "HEAD")
    _write(repo / "_DomainEngines" / "bridge" / "CHANGE_PREP_fixture.md",
           "# CHANGE prep fixture\n\n"
           "Precedent: framework-maintenance pattern.\n\n"
           "Evidence: `_harness_generated/evidence/fixture.json`\n")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", "change prep")

    report = cmd_coord_check.run_coord_check(repo, f"{base}..HEAD")

    hits = [f for f in report.findings if f.code == "COORD_GENERATED_REF_ABSENT"]
    assert len(hits) == 1
    assert hits[0].severity is Severity.INFO
    rc = harness.main([
        "--repo-root", str(repo), "coord-check", "--diff", f"{base}..HEAD"])
    assert rc == 0
    assert "COORD_GENERATED_REF_ABSENT" in capsys.readouterr().out
