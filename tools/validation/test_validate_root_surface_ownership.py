"""Tests for G2, the D-GOV-21 static root surface-ownership register guard."""

from pathlib import Path

import yaml

import validate_root_surface_ownership as g2


def _write_register(root: Path, data: dict) -> None:
    path = root / g2.REGISTER_RELPATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")


def _materialize(root: Path, name: str) -> None:
    (root / "execution" / name).mkdir(parents=True, exist_ok=True)


def _entry(entry_id: str = "PKG-01_Example", **overrides) -> dict:
    entry = {
        "id": entry_id,
        "kind": "package",
        "decomposition_ref": "TBD",
        "write_targets": [f"execution/{entry_id}/**"],
        "instruction_surface": False,
        "serialization": None,
    }
    entry.update(overrides)
    return entry


def _register(entries: list[dict] | None = None, **overrides) -> dict:
    data = {
        "schema": "root-surface-ownership/v1",
        "decomposition": "TBD",
        "entries": entries if entries is not None else [],
    }
    data.update(overrides)
    return data


def test_pass_idle_when_no_structure_and_no_register(tmp_path):
    code, lines = g2.check(tmp_path)
    assert code == 0
    assert any("guard idle" in line for line in lines)


def test_pass_idle_with_control_plane_only(tmp_path):
    (tmp_path / "execution" / "_Coordination").mkdir(parents=True)
    code, _ = g2.check(tmp_path)
    assert code == 0


def test_block_when_structure_exists_without_register(tmp_path):
    _materialize(tmp_path, "PKG-01_Example")
    code, lines = g2.check(tmp_path)
    assert code == 1
    assert any("is absent while PKG-*/DEL-* structure exists" in line for line in lines)


def test_pass_with_empty_register_and_no_structure(tmp_path):
    _write_register(tmp_path, _register([]))
    code, lines = g2.check(tmp_path)
    assert code == 0, lines
    assert any("G2 PASS" in line for line in lines)


def test_pass_with_registered_materialized_package(tmp_path):
    _materialize(tmp_path, "PKG-01_Example")
    _write_register(tmp_path, _register([_entry()]))
    code, lines = g2.check(tmp_path)
    assert code == 0, lines


def test_block_on_unregistered_materialized_package(tmp_path):
    _materialize(tmp_path, "PKG-01_Example")
    _materialize(tmp_path, "PKG-02_Unregistered")
    _write_register(tmp_path, _register([_entry()]))
    code, lines = g2.check(tmp_path)
    assert code == 1
    assert any("unregistered materialized package" in line for line in lines)


def test_block_on_undeclared_own_tree(tmp_path):
    _materialize(tmp_path, "PKG-01_Example")
    entry = _entry(write_targets=["execution/PKG-99_Other/**"])
    _write_register(tmp_path, _register([entry]))
    code, lines = g2.check(tmp_path)
    assert code == 1
    assert any("undeclared write target" in line for line in lines)


def test_block_on_absolute_write_target(tmp_path):
    entry = _entry(write_targets=["/var/tmp/anything", "execution/PKG-01_Example/**"])
    _write_register(tmp_path, _register([entry]))
    code, lines = g2.check(tmp_path)
    assert code == 1
    assert any("not a repo-relative POSIX path" in line for line in lines)


def test_block_on_unmarked_instruction_surface_target(tmp_path):
    entry = _entry(write_targets=["execution/PKG-01_Example/**", "tools/validation/**"])
    _write_register(tmp_path, _register([entry]))
    code, lines = g2.check(tmp_path)
    assert code == 1
    assert any("intersect the instruction surface" in line for line in lines)


def test_pass_on_marked_instruction_surface_target(tmp_path):
    entry = _entry(
        write_targets=["execution/PKG-01_Example/**", "docs/PRD_ROOT.md"],
        instruction_surface=True,
    )
    _write_register(tmp_path, _register([entry]))
    code, lines = g2.check(tmp_path)
    assert code == 0, lines


def test_dot_github_workflows_is_instruction_surface():
    """Regression: naive `lstrip('./')` ate the leading dot of `.github/`."""
    assert g2.intersects_instruction_surface(".github/workflows/governance-harness.yml")
    assert g2.intersects_instruction_surface("tools/validation/**")
    assert not g2.intersects_instruction_surface("execution/PKG-01_Example/**")


def test_block_on_duplicate_entry_ids(tmp_path):
    _write_register(tmp_path, _register([_entry(), _entry()]))
    code, lines = g2.check(tmp_path)
    assert code == 1
    assert any("duplicate register entry" in line for line in lines)


def test_block_on_bad_identifier_or_kind(tmp_path):
    entry = _entry()
    entry["id"] = "NotAPackage"
    entry["kind"] = "widget"
    _write_register(tmp_path, _register([entry]))
    code, lines = g2.check(tmp_path)
    assert code == 1
    assert any("is not a PKG-*/DEL-* identifier" in line for line in lines)
    assert any("kind" in line for line in lines)


def test_block_when_declared_decomposition_missing(tmp_path):
    _write_register(
        tmp_path,
        _register([_entry()], decomposition="execution/_Decomposition/ACCEPTED.md"),
    )
    code, lines = g2.check(tmp_path)
    assert code == 1
    assert any("does not exist" in line for line in lines)


def test_block_on_tbd_ref_when_decomposition_declared(tmp_path):
    decomposition = tmp_path / "execution" / "_Decomposition" / "ACCEPTED.md"
    decomposition.parent.mkdir(parents=True, exist_ok=True)
    decomposition.write_text("PKG-01_Example\n", encoding="utf-8")
    _write_register(
        tmp_path,
        _register([_entry()], decomposition="execution/_Decomposition/ACCEPTED.md"),
    )
    code, lines = g2.check(tmp_path)
    assert code == 1
    assert any("register/decomposition mismatch" in line for line in lines)


def test_block_on_ref_absent_from_declared_decomposition(tmp_path):
    decomposition = tmp_path / "execution" / "_Decomposition" / "ACCEPTED.md"
    decomposition.parent.mkdir(parents=True, exist_ok=True)
    decomposition.write_text("PKG-07_Something_Else\n", encoding="utf-8")
    _write_register(
        tmp_path,
        _register(
            [_entry(decomposition_ref="PKG-01_Example")],
            decomposition="execution/_Decomposition/ACCEPTED.md",
        ),
    )
    code, lines = g2.check(tmp_path)
    assert code == 1
    assert any("does not appear in" in line for line in lines)


def test_pass_when_ref_present_in_declared_decomposition(tmp_path):
    decomposition = tmp_path / "execution" / "_Decomposition" / "ACCEPTED.md"
    decomposition.parent.mkdir(parents=True, exist_ok=True)
    decomposition.write_text("PKG-01_Example is accepted.\n", encoding="utf-8")
    _write_register(
        tmp_path,
        _register(
            [_entry(decomposition_ref="PKG-01_Example")],
            decomposition="execution/_Decomposition/ACCEPTED.md",
        ),
    )
    code, lines = g2.check(tmp_path)
    assert code == 0, lines


def test_overlapping_targets_are_info_not_block(tmp_path):
    """Static facts only: G2 makes no concurrency claim about shared targets."""
    shared = "execution/PKG-01_Example/shared"
    entries = [
        _entry("PKG-01_Example", write_targets=["execution/PKG-01_Example/**", shared]),
        _entry("PKG-02_Other", write_targets=["execution/PKG-02_Other/**", shared]),
    ]
    _write_register(tmp_path, _register(entries))
    code, lines = g2.check(tmp_path)
    assert code == 0, lines
    assert any("no concurrency claim" in line for line in lines)


def test_block_on_unknown_schema(tmp_path):
    _write_register(tmp_path, _register([], schema="something-else/v1"))
    code, lines = g2.check(tmp_path)
    assert code == 1
    assert any("this guard understands" in line for line in lines)


def test_block_on_unparseable_register(tmp_path):
    path = tmp_path / g2.REGISTER_RELPATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("entries: [unterminated\n", encoding="utf-8")
    code, lines = g2.check(tmp_path)
    assert code == 1
    assert any("unparseable" in line for line in lines)


def test_live_repo_state_passes():
    """G2 must PASS on the actual checkout: no root PKG-*/DEL-* and no register
    is the lawful pre-instantiation condition (packet §5.3)."""
    code, _ = g2.check(g2.repo_root())
    assert code == 0
