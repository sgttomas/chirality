"""Tests for G4, the D-GOV-21 instruction-surface tranche manifest guard."""

import subprocess
from pathlib import Path

import yaml

import validate_instruction_tranche_manifest as g4


def _manifest(tranche_id: str = "T-DEMO", **overrides) -> dict:
    data = {
        "schema": "instruction-tranche-manifest/v1",
        "tranche_id": tranche_id,
        "title": "Demo tranche",
        "date": "2026-07-25",
        "instruction_surface_paths": ["tools/validation/demo.py"],
        "m2_gate": {
            "authorization": "owner direction of record, in-session 2026-07-25",
            "authorized_by": "Ryan Tufts",
            "authorization_date": "2026-07-25",
            "integration_owner": "HELP_HUMAN (Agent 0)",
            "merge_gate": "human-gated-pr",
            "self_merge": False,
        },
        "m6_notice": {
            "disposition": "none-required",
            "routed_to": [],
            "rationale": "No project loop pins the touched surfaces.",
        },
    }
    data.update(overrides)
    return data


def _write_manifest(root: Path, data: dict, stem: str | None = None) -> Path:
    stem = stem or str(data.get("tranche_id", "T-DEMO"))
    path = root / g4.MANIFEST_DIR_RELPATH / f"{stem}.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    return path


def _git(root: Path, *args: str) -> str:
    out = subprocess.run(
        [
            "git",
            "-C",
            str(root),
            "-c",
            "user.name=Test",
            "-c",
            "user.email=test@example.invalid",
            "-c",
            "commit.gpgsign=false",
            *args,
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    return out.stdout.strip()


def _init_repo(root: Path) -> None:
    _git(root, "init", "-q", "-b", "main")
    (root / "README.md").write_text("seed\n", encoding="utf-8")
    _git(root, "add", "-A")
    _git(root, "commit", "-q", "-m", "seed")


def test_block_when_manifest_directory_absent(tmp_path):
    code, lines = g4.check(tmp_path)
    assert code == 1
    assert any("does not exist" in line for line in lines)


def test_block_when_manifest_directory_empty(tmp_path):
    (tmp_path / g4.MANIFEST_DIR_RELPATH).mkdir(parents=True)
    code, lines = g4.check(tmp_path)
    assert code == 1
    assert any("silently emptied" in line for line in lines)


def test_pass_with_valid_manifest(tmp_path):
    _write_manifest(tmp_path, _manifest())
    code, lines = g4.check(tmp_path)
    assert code == 0, lines
    assert any("G4 PASS (CI mode)" in line for line in lines)


def test_block_on_unknown_schema(tmp_path):
    _write_manifest(tmp_path, _manifest(schema="tranche/v0"))
    code, lines = g4.check(tmp_path)
    assert code == 1
    assert any("this guard understands" in line for line in lines)


def test_block_on_missing_required_keys(tmp_path):
    data = _manifest()
    del data["m2_gate"]
    del data["date"]
    _write_manifest(tmp_path, data)
    code, lines = g4.check(tmp_path)
    assert code == 1
    assert any("missing required keys" in line for line in lines)


def test_block_when_tranche_id_does_not_match_filename(tmp_path):
    _write_manifest(tmp_path, _manifest("T-DEMO"), stem="T-OTHER")
    code, lines = g4.check(tmp_path)
    assert code == 1
    assert any("does not match the filename stem" in line for line in lines)


def test_block_on_bad_date(tmp_path):
    _write_manifest(tmp_path, _manifest(date="July 25 2026"))
    code, lines = g4.check(tmp_path)
    assert code == 1
    assert any("is not YYYY-MM-DD" in line for line in lines)


def test_pass_with_unquoted_yaml_dates(tmp_path):
    """Hand-authored manifests write `date: 2026-07-25`, which YAML parses as a
    date object; both that and the quoted string form are accepted."""
    path = tmp_path / g4.MANIFEST_DIR_RELPATH / "T-DATE.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "schema: instruction-tranche-manifest/v1\n"
        "tranche_id: T-DATE\n"
        "title: Unquoted dates\n"
        "date: 2026-07-25\n"
        "instruction_surface_paths:\n"
        "  - tools/validation/demo.py\n"
        "m2_gate:\n"
        "  authorization: owner direction of record\n"
        "  authorized_by: Ryan Tufts\n"
        "  authorization_date: 2026-07-25\n"
        "  integration_owner: HELP_HUMAN (Agent 0)\n"
        "  merge_gate: human-gated-pr\n"
        "  self_merge: false\n"
        "m6_notice:\n"
        "  disposition: none-required\n"
        "  routed_to: []\n"
        "  rationale: nothing pins these surfaces\n",
        encoding="utf-8",
    )
    code, lines = g4.check(tmp_path)
    assert code == 0, lines


def test_block_on_machine_absolute_declared_path(tmp_path):
    _write_manifest(tmp_path, _manifest(instruction_surface_paths=["/etc/passwd"]))
    code, lines = g4.check(tmp_path)
    assert code == 1
    assert any("not a repo-relative POSIX path" in line for line in lines)


def test_dot_github_workflows_is_instruction_surface():
    """Regression: naive `lstrip('./')` ate the leading dot of `.github/`, so CI
    wiring silently read as non-protected."""
    assert g4.intersects_instruction_surface(".github/workflows/governance-harness.yml")
    assert g4.intersects_instruction_surface("./.github/workflows/x.yml")
    assert g4.intersects_instruction_surface("AGENTS.md")
    assert not g4.intersects_instruction_surface("execution/_Coordination/x.md")
    assert not g4.intersects_instruction_surface("projects/demo/docs/x.md")


def test_claude_md_is_instruction_surface():
    """D-GOV-26 item 2: `CLAUDE.md` is the session-init instruction pointer that
    imports `AGENTS.md`, so a change to it is an instruction-surface change."""
    assert g4.intersects_instruction_surface("CLAUDE.md")
    assert g4.intersects_instruction_surface("./CLAUDE.md")
    assert not g4.intersects_instruction_surface("projects/demo/CLAUDE.md")


def test_diff_mode_blocks_uncovered_claude_md_change(tmp_path):
    _init_repo(tmp_path)
    _write_manifest(
        tmp_path, _manifest(instruction_surface_paths=["docs/governance_harness/"])
    )
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-q", "-m", "manifest")
    base = _git(tmp_path, "rev-parse", "HEAD")
    (tmp_path / "CLAUDE.md").write_text("@AGENTS.md\n", encoding="utf-8")
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-q", "-m", "pointer")
    head = _git(tmp_path, "rev-parse", "HEAD")
    code, lines = g4.check(tmp_path, base, head)
    assert code == 1
    assert any("CLAUDE.md" in line for line in lines)
    assert any("is not covered by any declared tranche manifest path" in line for line in lines)


def test_diff_mode_pass_when_claude_md_change_is_covered(tmp_path):
    _init_repo(tmp_path)
    _write_manifest(tmp_path, _manifest(instruction_surface_paths=["CLAUDE.md"]))
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-q", "-m", "manifest")
    base = _git(tmp_path, "rev-parse", "HEAD")
    (tmp_path / "CLAUDE.md").write_text("@AGENTS.md\n", encoding="utf-8")
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-q", "-m", "pointer")
    head = _git(tmp_path, "rev-parse", "HEAD")
    code, lines = g4.check(tmp_path, base, head)
    assert code == 0, lines


def test_note_on_over_declared_non_instruction_path(tmp_path):
    _write_manifest(
        tmp_path,
        _manifest(instruction_surface_paths=["tools/validation/demo.py", "execution/x.md"]),
    )
    code, lines = g4.check(tmp_path)
    assert code == 0, lines
    assert any("over-declaration" in line for line in lines)


def test_block_on_non_human_gated_merge(tmp_path):
    data = _manifest()
    data["m2_gate"]["merge_gate"] = "auto-merge"
    _write_manifest(tmp_path, data)
    code, lines = g4.check(tmp_path)
    assert code == 1
    assert any("requires 'human-gated-pr'" in line for line in lines)


def test_block_on_self_merge(tmp_path):
    data = _manifest()
    data["m2_gate"]["self_merge"] = True
    _write_manifest(tmp_path, data)
    code, lines = g4.check(tmp_path)
    assert code == 1
    assert any("forbids self-merge" in line for line in lines)


def test_block_on_empty_authorization(tmp_path):
    data = _manifest()
    data["m2_gate"]["authorization"] = "   "
    _write_manifest(tmp_path, data)
    code, lines = g4.check(tmp_path)
    assert code == 1
    assert any("m2_gate.authorization must be a non-empty string" in line for line in lines)


def test_block_on_unknown_m6_disposition(tmp_path):
    data = _manifest()
    data["m6_notice"]["disposition"] = "later"
    _write_manifest(tmp_path, data)
    code, lines = g4.check(tmp_path)
    assert code == 1
    assert any("m6_notice.disposition" in line for line in lines)


def test_block_when_routed_names_no_notice(tmp_path):
    data = _manifest()
    data["m6_notice"]["disposition"] = "routed"
    _write_manifest(tmp_path, data)
    code, lines = g4.check(tmp_path)
    assert code == 1
    assert any("names no notice" in line for line in lines)


def test_block_when_routed_notice_missing(tmp_path):
    data = _manifest()
    data["m6_notice"]["disposition"] = "routed"
    data["m6_notice"]["routed_to"] = ["projects/demo/NOTICE.md"]
    _write_manifest(tmp_path, data)
    code, lines = g4.check(tmp_path)
    assert code == 1
    assert any("does not exist" in line for line in lines)


def test_pass_when_routed_notice_exists(tmp_path):
    notice = tmp_path / "projects" / "demo" / "NOTICE.md"
    notice.parent.mkdir(parents=True, exist_ok=True)
    notice.write_text("# notice\n", encoding="utf-8")
    data = _manifest()
    data["m6_notice"]["disposition"] = "routed"
    data["m6_notice"]["routed_to"] = ["projects/demo/NOTICE.md"]
    _write_manifest(tmp_path, data)
    code, lines = g4.check(tmp_path)
    assert code == 0, lines


def test_pending_disposition_passes_with_note(tmp_path):
    data = _manifest()
    data["m6_notice"]["disposition"] = "pending"
    _write_manifest(tmp_path, data)
    code, lines = g4.check(tmp_path)
    assert code == 0, lines
    assert any("completed by the accepting agent at fan-in" in line for line in lines)


def test_block_on_unparseable_manifest(tmp_path):
    path = tmp_path / g4.MANIFEST_DIR_RELPATH / "T-BAD.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("schema: [unterminated\n", encoding="utf-8")
    code, lines = g4.check(tmp_path)
    assert code == 1
    assert any("unparseable" in line for line in lines)


def test_diff_mode_pass_when_change_is_covered(tmp_path):
    _init_repo(tmp_path)
    _write_manifest(
        tmp_path,
        _manifest(instruction_surface_paths=["tools/validation/", "docs/governance_harness/"]),
    )
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-q", "-m", "manifest")
    base = _git(tmp_path, "rev-parse", "HEAD")
    tool = tmp_path / "tools" / "validation" / "demo.py"
    tool.parent.mkdir(parents=True, exist_ok=True)
    tool.write_text("# demo\n", encoding="utf-8")
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-q", "-m", "tool")
    head = _git(tmp_path, "rev-parse", "HEAD")
    code, lines = g4.check(tmp_path, base, head)
    assert code == 0, lines
    assert any("G4 PASS (diff mode)" in line for line in lines)


def test_diff_mode_blocks_uncovered_instruction_surface_change(tmp_path):
    _init_repo(tmp_path)
    _write_manifest(
        tmp_path, _manifest(instruction_surface_paths=["docs/governance_harness/"])
    )
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-q", "-m", "manifest")
    base = _git(tmp_path, "rev-parse", "HEAD")
    agents = tmp_path / "AGENTS.md"
    agents.write_text("# changed doctrine\n", encoding="utf-8")
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-q", "-m", "doctrine")
    head = _git(tmp_path, "rev-parse", "HEAD")
    code, lines = g4.check(tmp_path, base, head)
    assert code == 1
    assert any("is not covered by any declared tranche manifest path" in line for line in lines)


def test_diff_mode_ignores_non_instruction_surface_change(tmp_path):
    _init_repo(tmp_path)
    _write_manifest(tmp_path, _manifest())
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-q", "-m", "manifest")
    base = _git(tmp_path, "rev-parse", "HEAD")
    record = tmp_path / "execution" / "_Coordination" / "RECORD.md"
    record.parent.mkdir(parents=True, exist_ok=True)
    record.write_text("# record\n", encoding="utf-8")
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-q", "-m", "record")
    head = _git(tmp_path, "rev-parse", "HEAD")
    code, lines = g4.check(tmp_path, base, head)
    assert code == 0, lines


def test_diff_mode_operational_on_unknown_tranche(tmp_path):
    _init_repo(tmp_path)
    _write_manifest(tmp_path, _manifest())
    code, lines = g4.check(tmp_path, "HEAD", "HEAD", tranche="T-NOT-DECLARED")
    assert code == 2
    assert any("no manifest declares tranche_id" in line for line in lines)


def test_diff_mode_operational_on_bad_refs(tmp_path):
    _init_repo(tmp_path)
    _write_manifest(tmp_path, _manifest())
    code, lines = g4.check(tmp_path, "no-such-ref", "HEAD")
    assert code == 2
    assert any("OPERATIONAL" in line for line in lines)


def test_cli_rejects_half_specified_diff_mode():
    assert g4.main(["--base", "HEAD~1"]) == 2


def test_live_repo_lane_b_manifest_exists_and_passes():
    """The G4 discipline applied to itself: this tranche's own manifest must be
    present and schema-valid in the live checkout (packet §5.3 G4)."""
    root = g4.repo_root()
    manifest = root / g4.MANIFEST_DIR_RELPATH / "ROOT-LANE-B-20260725.yaml"
    assert manifest.is_file()
    code, lines = g4.check(root)
    assert code == 0, lines
    assert any("ROOT-LANE-B-20260725" in line for line in lines)
