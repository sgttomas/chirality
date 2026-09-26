#!/usr/bin/env python3
"""Tests for tools/validation/check_amendment_reopen.py (D-GOV-50, D-GOV-51).

Fixture amendment folders are built under tmp_path; one test reads the
accepted PEC SCA-006 records when they are present in the checkout.
"""
from __future__ import annotations

import csv
import hashlib
import importlib.util
import io
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = REPO_ROOT / "tools" / "validation" / "check_amendment_reopen.py"

_spec = importlib.util.spec_from_file_location("check_amendment_reopen", SCRIPT)
assert _spec and _spec.loader
mod = importlib.util.module_from_spec(_spec)
sys.modules["check_amendment_reopen"] = mod
_spec.loader.exec_module(mod)

BASE_COLUMNS = [
    "AmendmentID",
    "ActionSeq",
    "ActionType",
    "EntityType",
    "EntityID",
    "Description",
    "AffectedFiles",
    "DownstreamReruns",
    "SupersessionBindingPresent",
]
DEL_REL = "projects/fixture/execution/PKG-01_Fixture/1_Working/DEL-01-01_Fixture"
SC_REL = "projects/fixture/execution/_ScopeChange"


def _csv(columns, rows) -> str:
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=columns, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow({c: row.get(c, "") for c in columns})
    return buffer.getvalue()


def row(action, entity="DEL-01-01", seq="1", entity_type="DELIVERABLE", scope=None, amendment="SCA-001"):
    data = {
        "AmendmentID": amendment,
        "ActionSeq": seq,
        "ActionType": action,
        "EntityType": entity_type,
        "EntityID": entity,
        "Description": "fixture",
        "SupersessionBindingPresent": "NO",
    }
    if scope is not None:
        data["ScopeChanging"] = scope
    return data


def build(
    project: Path,
    rows,
    *,
    amendment="SCA-001",
    scope_column=True,
    groups=("1", "2", "3"),
    group3_heading=None,
    register_name="Amendment_Actions.csv",
    bound_sha=None,
    extra_manifest_rows=(),
    manifest_path_override=None,
) -> dict:
    """Write a deliverable folder and one amendment's scope-change records."""
    deliverable = project / DEL_REL
    deliverable.mkdir(parents=True, exist_ok=True)
    (deliverable / "_STATUS.md").write_text("# Status: DEL-01-01\n\n**Current State:** ISSUED\n")
    root = project / SC_REL
    snapshot = root / f"{amendment}_2026-09-26_1200"
    snapshot.mkdir(parents=True, exist_ok=True)
    columns = BASE_COLUMNS + (["ScopeChanging"] if scope_column else [])
    register = snapshot / register_name
    register.write_text(_csv(columns, rows))
    sha = bound_sha or hashlib.sha256(register.read_bytes()).hexdigest()
    register_rel = manifest_path_override or register.relative_to(project).as_posix()
    snapshots = root / "checkpoint_snapshots"
    for group in groups:
        folder = snapshots / f"{amendment}_GROUP-{group}_2026-09-26"
        folder.mkdir(parents=True, exist_ok=True)
        heading = f"{amendment} checkpoint group {group} — accepted fixture"
        if group == "3" and group3_heading is not None:
            heading = group3_heading
        (folder / "DECISION.md").write_text(f"# {heading}\n\nFixture decision.\n")
        manifest_rows = [f"{snapshot.relative_to(project).as_posix()}/Propagation_Plan.md,{'0' * 64},plan,Accepted"]
        if group == "2":
            manifest_rows.append(f"{register_rel},{sha},exact final action register,Accepted")
            manifest_rows.extend(extra_manifest_rows)
        (folder / "ACCEPTED_MANIFEST.csv").write_text(
            "Path,SHA256,Role,AcceptanceBoundary\n" + "\n".join(manifest_rows) + "\n"
        )
    return {"deliverable": deliverable, "root": root, "snapshot": snapshot, "register": register}


def check(project: Path, deliverable, amendment="SCA-001", **kwargs):
    return mod.check_reopen(str(deliverable), amendment, project_root=project, cwd=project, **kwargs)


# ---------------------------------------------------------------------------
# Admitted paths
# ---------------------------------------------------------------------------


def test_modify_admitted(tmp_path):
    paths = build(tmp_path, [row("ADD", entity="DEL-01-02"), row("MODIFY", seq="2", scope="NO")])
    decision = check(tmp_path, paths["deliverable"])
    assert decision.admitted, decision
    assert decision.code == mod.ADMITTED
    assert decision.amendment_id == "SCA-001"
    assert decision.action_seq == "2"
    assert decision.action_type == "MODIFY"
    assert decision.scope_changing == "NO"
    assert decision.group3_decision == f"{SC_REL}/checkpoint_snapshots/SCA-001_GROUP-3_2026-09-26/DECISION.md"
    assert decision.register_sha256 == hashlib.sha256(paths["register"].read_bytes()).hexdigest()


def test_modify_admitted_in_legacy_register_without_scope_column(tmp_path):
    paths = build(tmp_path, [row("MODIFY")], scope_column=False)
    decision = check(tmp_path, paths["deliverable"])
    assert decision.admitted
    assert decision.scope_changing is None
    assert any("legacy register" in note for note in decision.notes)


def test_reclassify_scope_changing_yes_admitted(tmp_path):
    paths = build(tmp_path, [row("RECLASSIFY", scope="YES")])
    decision = check(tmp_path, paths["deliverable"])
    assert decision.admitted
    assert decision.action_type == "RECLASSIFY"
    assert decision.scope_changing == "YES"


def test_deliverable_id_and_labelled_entity_id(tmp_path):
    paths = build(tmp_path, [row("MODIFY", entity="DEL-01-01_Fixture", scope="YES")])
    assert check(tmp_path, "DEL-01-01", scope_change_root=paths["root"]).admitted
    assert check(tmp_path, paths["deliverable"]).admitted


def test_similar_deliverable_id_is_not_matched(tmp_path):
    paths = build(tmp_path, [row("MODIFY", entity="DEL-01-011", scope="NO")])
    decision = check(tmp_path, paths["deliverable"])
    assert decision.code == mod.NO_DELIVERABLE_ACTION


def test_group3_folder_and_decision_paths_admitted(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    folder = paths["root"] / "checkpoint_snapshots" / "SCA-001_GROUP-3_2026-09-26"
    assert check(tmp_path, paths["deliverable"], amendment=str(folder)).admitted
    assert check(tmp_path, paths["deliverable"], amendment=f"{SC_REL}/checkpoint_snapshots/SCA-001_GROUP-3_2026-09-26/DECISION.md").admitted
    assert check(tmp_path, paths["deliverable"], amendment=str(paths["snapshot"])).admitted


def test_project_qualified_amendment_id(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO", amendment="SCA-APP-003")], amendment="SCA-APP-003")
    decision = check(tmp_path, paths["deliverable"], amendment="SCA-APP-003")
    assert decision.admitted, decision


def test_cp2_register_name_bound_in_group2_manifest(tmp_path):
    # A run whose group-1 snapshot bound Amendment_Actions.csv as intake writes
    # its group-2 register under a distinct name; the manifest names it.
    paths = build(tmp_path, [row("MODIFY", scope="NO")], register_name="Amendment_Actions_CP2.csv")
    (paths["snapshot"] / "Amendment_Actions.csv").write_text(_csv(BASE_COLUMNS, [row("ADD")]))
    decision = check(tmp_path, paths["deliverable"])
    assert decision.admitted
    assert decision.register_path.endswith("Amendment_Actions_CP2.csv")


def test_manifest_path_relative_to_project_folder_admitted(tmp_path):
    paths = build(
        tmp_path,
        [row("MODIFY", scope="NO")],
        manifest_path_override="execution/_ScopeChange/SCA-001_2026-09-26_1200/Amendment_Actions.csv",
    )
    decision = check(tmp_path, paths["deliverable"])
    assert decision.admitted, decision
    assert decision.register_path == f"{SC_REL}/SCA-001_2026-09-26_1200/Amendment_Actions.csv"


def test_role_disambiguates_two_bound_register_files(tmp_path):
    intake = f"{SC_REL}/SCA-001_2026-09-26_1200/Amendment_Actions.csv"
    paths = build(
        tmp_path,
        [row("MODIFY", scope="NO")],
        register_name="Amendment_Actions_CP2.csv",
        extra_manifest_rows=[f"{intake},{'1' * 64},intake context,Context"],
    )
    (paths["snapshot"] / "Amendment_Actions.csv").write_text("x\n")
    decision = check(tmp_path, paths["deliverable"])
    assert decision.admitted
    assert decision.register_path.endswith("Amendment_Actions_CP2.csv")


# ---------------------------------------------------------------------------
# Refusals: acceptance stage
# ---------------------------------------------------------------------------


def test_group2_only_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")], groups=("1", "2"))
    decision = check(tmp_path, paths["deliverable"])
    assert not decision.admitted
    assert decision.code == mod.GROUP3_NOT_ACCEPTED
    assert "SCA-001_GROUP-2_2026-09-26" in decision.reason


def test_group1_only_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")], groups=("1",))
    decision = check(tmp_path, paths["deliverable"])
    assert decision.code == mod.GROUP3_NOT_ACCEPTED


def test_candidate_snapshot_without_group3_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")], groups=("1", "2"))
    decision = check(tmp_path, paths["deliverable"], amendment=str(paths["snapshot"]))
    assert decision.code == mod.GROUP3_NOT_ACCEPTED


def test_group2_decision_path_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    folder = paths["root"] / "checkpoint_snapshots" / "SCA-001_GROUP-2_2026-09-26"
    decision = check(tmp_path, paths["deliverable"], amendment=str(folder))
    assert decision.code == mod.GROUP3_NOT_ACCEPTED
    assert "group-2" in decision.reason


@pytest.mark.parametrize(
    "heading",
    [
        "SCA-001 checkpoint group 3 — returned to checkpoint 2",
        "SCA-001 checkpoint group 3 — not accepted",
        "SCA-002 checkpoint group 3 — accepted audited poststate",
        "Checkpoint group 3 notes",
    ],
)
def test_group3_heading_without_acceptance_refused(tmp_path, heading):
    paths = build(tmp_path, [row("MODIFY", scope="NO")], group3_heading=heading)
    decision = check(tmp_path, paths["deliverable"])
    assert decision.code == mod.GROUP3_NOT_ACCEPTED


def test_group3_without_manifest_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    (paths["root"] / "checkpoint_snapshots" / "SCA-001_GROUP-3_2026-09-26" / "ACCEPTED_MANIFEST.csv").unlink()
    assert check(tmp_path, paths["deliverable"]).code == mod.GROUP3_NOT_ACCEPTED


def test_missing_group2_manifest_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    (paths["root"] / "checkpoint_snapshots" / "SCA-001_GROUP-2_2026-09-26" / "ACCEPTED_MANIFEST.csv").unlink()
    assert check(tmp_path, paths["deliverable"]).code == mod.GROUP2_MANIFEST_MISSING


# ---------------------------------------------------------------------------
# Refusals: register binding
# ---------------------------------------------------------------------------


def test_register_hash_mismatch_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    with paths["register"].open("a") as handle:
        handle.write("SCA-001,9,MODIFY,DELIVERABLE,DEL-09-09,late edit,,,NO,NO\n")
    decision = check(tmp_path, paths["deliverable"])
    assert decision.code == mod.REGISTER_HASH_MISMATCH


def test_register_not_bound_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")], register_name="Actions_Final.csv")
    assert check(tmp_path, paths["deliverable"]).code == mod.REGISTER_NOT_BOUND


def test_register_ambiguous_refused(tmp_path):
    other = f"{SC_REL}/SCA-001_2026-09-26_1200/Amendment_Actions_B.csv"
    paths = build(
        tmp_path,
        [row("MODIFY", scope="NO")],
        extra_manifest_rows=[f"{other},{'1' * 64},exact final action register,Accepted"],
    )
    assert check(tmp_path, paths["deliverable"]).code == mod.REGISTER_AMBIGUOUS


def test_bound_register_missing_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    paths["register"].unlink()
    assert check(tmp_path, paths["deliverable"]).code == mod.REGISTER_MISSING


# ---------------------------------------------------------------------------
# Refusals: action rows
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("action", ["ADD", "REMOVE", "MERGE", "SPLIT"])
def test_other_actions_refused(tmp_path, action):
    paths = build(tmp_path, [row(action, scope="YES")])
    decision = check(tmp_path, paths["deliverable"])
    assert decision.code == mod.ACTION_NOT_AUTHORIZING
    assert action in decision.reason


def test_reclassify_scope_changing_no_refused(tmp_path):
    paths = build(tmp_path, [row("RECLASSIFY", scope="NO")])
    assert check(tmp_path, paths["deliverable"]).code == mod.RECLASSIFY_NOT_SCOPE_CHANGING


def test_reclassify_scope_changing_blank_refused(tmp_path):
    paths = build(tmp_path, [row("RECLASSIFY", scope="")])
    assert check(tmp_path, paths["deliverable"]).code == mod.RECLASSIFY_NOT_SCOPE_CHANGING


def test_reclassify_in_legacy_register_refused(tmp_path):
    paths = build(tmp_path, [row("RECLASSIFY")], scope_column=False)
    decision = check(tmp_path, paths["deliverable"])
    assert decision.code == mod.RECLASSIFY_LEGACY_REGISTER
    assert "directly" in decision.reason


def test_non_deliverable_entity_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", entity_type="OTHER", scope="NO")])
    assert check(tmp_path, paths["deliverable"]).code == mod.NO_DELIVERABLE_ACTION


def test_row_of_another_amendment_ignored(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO", amendment="SCA-009")])
    assert check(tmp_path, paths["deliverable"]).code == mod.NO_DELIVERABLE_ACTION


# ---------------------------------------------------------------------------
# Containment
# ---------------------------------------------------------------------------


def test_manifest_path_escape_refused(tmp_path):
    project = tmp_path / "project"
    outside = tmp_path / "outside"
    outside.mkdir()
    (outside / "Amendment_Actions.csv").write_text(_csv(BASE_COLUMNS, [row("MODIFY")]))
    paths = build(project, [row("MODIFY", scope="NO")], manifest_path_override="../outside/Amendment_Actions.csv")
    decision = check(project, paths["deliverable"])
    assert decision.code == mod.PATH_ESCAPE


def test_manifest_path_outside_scope_change_root_refused(tmp_path):
    other = tmp_path / "projects" / "other" / "Amendment_Actions.csv"
    other.parent.mkdir(parents=True)
    other.write_text(_csv(BASE_COLUMNS + ["ScopeChanging"], [row("MODIFY", scope="YES")]))
    paths = build(tmp_path, [row("MODIFY", scope="NO")], manifest_path_override="projects/other/Amendment_Actions.csv")
    assert check(tmp_path, paths["deliverable"]).code == mod.PATH_ESCAPE


def test_symlinked_register_escape_refused(tmp_path):
    project = tmp_path / "project"
    paths = build(project, [row("MODIFY", scope="NO")])
    outside = tmp_path / "outside.csv"
    outside.write_bytes(paths["register"].read_bytes())
    paths["register"].unlink()
    os.symlink(outside, paths["register"])
    assert check(project, paths["deliverable"]).code == mod.PATH_ESCAPE


def test_symlinked_checkpoint_snapshots_escape_refused(tmp_path):
    project = tmp_path / "project"
    paths = build(project, [row("MODIFY", scope="NO")])
    snapshots = paths["root"] / "checkpoint_snapshots"
    moved = tmp_path / "moved_snapshots"
    snapshots.rename(moved)
    os.symlink(moved, snapshots)
    assert check(project, paths["deliverable"]).code == mod.PATH_ESCAPE


def test_amendment_path_outside_project_refused(tmp_path):
    project = tmp_path / "project"
    paths = build(project, [row("MODIFY", scope="NO")])
    elsewhere = build(tmp_path / "elsewhere", [row("MODIFY", scope="NO")])
    decision = check(project, paths["deliverable"], amendment=str(elsewhere["snapshot"]))
    assert decision.code == mod.PATH_ESCAPE


def test_amendment_of_another_execution_root_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    other_root = tmp_path / "projects" / "other" / "execution" / "_ScopeChange"
    other_root.mkdir(parents=True)
    decision = check(tmp_path, paths["deliverable"], scope_change_root=other_root)
    assert decision.code == mod.AMENDMENT_OUTSIDE_DELIVERABLE_ROOT


def test_unresolvable_amendment_refused(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    assert check(tmp_path, paths["deliverable"], amendment="no/such/path").code == mod.AMENDMENT_UNRESOLVED


def test_deliverable_id_without_root_refused(tmp_path):
    build(tmp_path, [row("MODIFY", scope="NO")])
    assert check(tmp_path, "DEL-01-01").code == mod.SCOPE_CHANGE_ROOT_NOT_FOUND


def test_invalid_deliverable_is_usage_error(tmp_path):
    with pytest.raises(mod.UsageError):
        check(tmp_path, "not-a-deliverable")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def run_cli(cwd: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=cwd, capture_output=True, text=True)


def test_cli_exit_codes_and_json(tmp_path):
    paths = build(tmp_path, [row("MODIFY", scope="NO")])
    ok = run_cli(tmp_path, "--deliverable", DEL_REL, "--amendment", "SCA-001", "--project-root", str(tmp_path), "--json")
    assert ok.returncode == 0, ok.stderr
    assert json.loads(ok.stdout)["code"] == "ADMITTED"

    refused = run_cli(tmp_path, "--deliverable", DEL_REL, "--amendment", "SCA-002", "--project-root", str(tmp_path))
    assert refused.returncode == 1
    assert refused.stderr.startswith("REFUSE GROUP3_NOT_ACCEPTED:")

    usage = run_cli(tmp_path, "--deliverable", "bogus", "--amendment", "SCA-001", "--project-root", str(tmp_path))
    assert usage.returncode == 2
    assert paths["deliverable"].is_dir()


# ---------------------------------------------------------------------------
# Real accepted amendment records (read only; skipped when absent)
# ---------------------------------------------------------------------------


PEC_DEL = "projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access"
PEC_GROUP3 = "projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-3_2026-09-26"


@pytest.mark.skipif(not (REPO_ROOT / PEC_GROUP3).is_dir() or not (REPO_ROOT / PEC_DEL).is_dir(), reason="PEC records not in this checkout")
def test_real_pec_amendment_records():
    admitted = mod.check_reopen(PEC_DEL, "SCA-006", project_root=REPO_ROOT, cwd=REPO_ROOT)
    assert admitted.admitted, admitted
    assert admitted.register_path.endswith("SCA-006_2026-09-25_1912/Amendment_Actions_CP2.csv")
    assert admitted.action_type == "MODIFY"
    assert admitted.scope_changing is None  # accepted before the ScopeChanging column

    added = mod.check_reopen(
        "DEL-08-06", PEC_GROUP3, project_root=REPO_ROOT, cwd=REPO_ROOT
    )
    assert added.code == mod.ACTION_NOT_AUTHORIZING  # ADD, not MODIFY


PIPING_ROOT = "projects/chirality-piping/execution/_ScopeChange"


@pytest.mark.skipif(not (REPO_ROOT / PIPING_ROOT / "checkpoint_snapshots").is_dir(), reason="Piping records not in this checkout")
def test_real_piping_group2_only_amendment_refused():
    decision = mod.check_reopen(
        "DEL-04-07", "SCA-011", scope_change_root=REPO_ROOT / PIPING_ROOT, project_root=REPO_ROOT, cwd=REPO_ROOT
    )
    assert decision.code == mod.GROUP3_NOT_ACCEPTED
