"""Tests for validate_scc_resolution_case.py in the _DAG/cases/ and legacy PKG-00 homes."""

from __future__ import annotations

from pathlib import Path

import pytest

import validate_scc_resolution_case as vscc

LEGACY_DELIVERABLE = "DEL-00-01_SCC-002_Closure"


def write_case(case: Path, case_id: str) -> Path:
    """Write a minimal valid case recording `case_id` in its datasheet."""
    case.mkdir(parents=True)
    (case / "Case_Contract.md").write_text("# Case contract\n", encoding="utf-8")
    (case / "Case_Datasheet.md").write_text(
        f"# Case datasheet\n\nCASE_ID: {case_id}\nOrigin: CLOSURE-2026-09-26, SCC-001, members DEL-01-01;DEL-01-02\n"
        "CaseState: EVIDENCE_ACCUMULATING\n",
        encoding="utf-8",
    )
    (case / "Open_Questions.md").write_text("# Open questions\n\nTBD\n", encoding="utf-8")
    (case / "Case_QA.md").write_text("# Case QA\n\nCase state: EVIDENCE_ACCUMULATING\n", encoding="utf-8")
    (case / "Evidence_Register.csv").write_text(
        ",".join(vscc.EVIDENCE_COLUMNS) + "\nEVID-001,source.md,L1,DOC,FIND-001,\n", encoding="utf-8"
    )
    (case / "Task_Findings.csv").write_text(
        ",".join(vscc.TASK_FINDINGS_COLUMNS) + "\nFIND-001,TASK_RUN_1,DEL-01-01,EDGE,Summary,EVID-001,OPEN\n",
        encoding="utf-8",
    )
    (case / "Candidate_Remedies.csv").write_text(
        ",".join(vscc.CANDIDATE_REMEDY_COLUMNS) + "\nREM-001,DEP-1,ROW,WORKING_ITEMS,DEL-01-01,EVID-001,TBD,PROPOSED,\n",
        encoding="utf-8",
    )
    (case / "Ruling_Register.csv").write_text(",".join(vscc.RULING_COLUMNS) + "\n", encoding="utf-8")
    (case / "Owner_Workflow_Handoff.md").write_text(
        ",".join(vscc.HANDOFF_COLUMNS) + "\nHOFF-001,DEPCLOSURE,After rulings,Candidate_Remedies.csv,Closure run,PENDING\n",
        encoding="utf-8",
    )
    return case


def dag_case(root: Path, case_id: str = "SCC-CASE-001") -> Path:
    return write_case(root / "execution" / "_DAG" / "cases" / case_id, case_id)


def legacy_case(root: Path, name: str = "CASE-SCC-002_Policy") -> Path:
    deliverable = root / "execution" / vscc.LEGACY_CONTROL_DELIVERABLE / "1_Working" / LEGACY_DELIVERABLE
    return write_case(deliverable / "scc-cases" / name, name)


# Legacy PKG-00 home: behaviour unchanged.


def test_legacy_case_passes(tmp_path: Path) -> None:
    assert vscc.validate_case(legacy_case(tmp_path)) == []


def test_legacy_case_rejects_pkg00_dependency_register(tmp_path: Path) -> None:
    case = legacy_case(tmp_path)
    (case.parents[1] / "Dependencies.csv").write_text("DependencyID\n", encoding="utf-8")
    assert vscc.validate_case(case) == ["PKG-00 contains Dependencies.csv; SCC cases must not add dependency registers"]


def test_legacy_case_keeps_its_own_folder_names_and_ignores_dag_checks(tmp_path: Path) -> None:
    case = legacy_case(tmp_path, "CASE-SCC-001_Legacy_Name")
    (case / "Case_Datasheet.md").write_text("CaseState: OPEN_FOR_TASK_WORK\n", encoding="utf-8")
    assert vscc.validate_case(case) == []


def test_legacy_missing_files_reported_alone(tmp_path: Path) -> None:
    case = legacy_case(tmp_path)
    (case / "Case_QA.md").unlink()
    assert vscc.validate_case(case) == ["missing required file: Case_QA.md"]


def test_existing_app_legacy_cases_still_pass() -> None:
    repo = Path(__file__).resolve().parents[2]
    control = repo / "projects/chirality-app-dev/execution" / vscc.LEGACY_CONTROL_DELIVERABLE
    cases = sorted(path for path in control.glob("1_Working/*/scc-cases/*") if path.is_dir())
    if not cases:
        pytest.skip("App legacy SCC cases are not present in this checkout")
    for case in cases:
        assert vscc.validate_case(case) == [], case


# _DAG/cases/<CASE-ID>/ home (D-GOV-49).


def test_dag_case_passes(tmp_path: Path) -> None:
    assert vscc.validate_case(dag_case(tmp_path)) == []


def test_dag_case_shares_content_checks(tmp_path: Path) -> None:
    case = dag_case(tmp_path)
    (case / "Case_QA.md").write_text("Case state: EVIDENCE_ACCUMULATING\nSCC closure achieved\n", encoding="utf-8")
    assert vscc.validate_case(case) == ["forbidden positive closure/mutation claim found: SCC closure achieved"]


@pytest.mark.parametrize("name", ["SCC-001", "SCC-CASE-1", "SCC-CASE-0001", "scc-case-001", "CASE-SCC-001"])
def test_dag_case_folder_must_be_stable_case_id(tmp_path: Path, name: str) -> None:
    errors = vscc.validate_case(dag_case(tmp_path, name))
    assert errors == [f"folder name {name!r} is not a case ID of the form SCC-CASE-NNN (D-GOV-49)"]


def test_dag_case_datasheet_must_record_case_id(tmp_path: Path) -> None:
    case = dag_case(tmp_path)
    (case / "Case_Datasheet.md").write_text("CaseState: EVIDENCE_ACCUMULATING\n", encoding="utf-8")
    assert vscc.validate_case(case) == ["Case_Datasheet.md does not record the case ID SCC-CASE-001"]


def test_dag_case_number_not_reused(tmp_path: Path) -> None:
    case = dag_case(tmp_path)
    (case.parent / "SCC-CASE-001_withdrawn").mkdir()
    (case.parent / "SCC-CASE-002").mkdir()
    assert vscc.validate_case(case) == ["another folder in _DAG/cases/ uses case number 001: SCC-CASE-001_withdrawn"]


def test_dag_cases_reject_dependency_register_anywhere(tmp_path: Path) -> None:
    case = dag_case(tmp_path)
    other = case.parent / "SCC-CASE-002" / "notes"
    other.mkdir(parents=True)
    (other / "Dependencies.csv").write_text("DependencyID\n", encoding="utf-8")
    assert vscc.validate_case(case) == ["_DAG/cases/ contains Dependencies.csv; SCC cases must not add dependency registers"]


def test_dag_cases_reject_shared_run_records(tmp_path: Path) -> None:
    case = dag_case(tmp_path)
    (case / "_run_records").mkdir()
    assert vscc.validate_case(case) == []
    (case.parent / "_run_records").mkdir()
    assert vscc.validate_case(case) == [
        "_DAG/cases/_run_records/ exists; run records belong under <CASE_PATH>/_run_records/"
    ]


def test_dag_case_rejects_split_with_legacy_home(tmp_path: Path) -> None:
    case = dag_case(tmp_path)
    legacy_case(tmp_path)
    expected = (
        "project also holds SCC cases in a legacy PKG-00 home "
        f"({vscc.LEGACY_CONTROL_DELIVERABLE}/1_Working/{LEGACY_DELIVERABLE}/scc-cases); each project uses one case home"
    )
    assert vscc.validate_case(case) == [expected]


def misplaced(found: str) -> str:
    return (
        "a case under _DAG/ must be a folder directly under _DAG/cases/, named by its case ID: "
        f"_DAG/cases/SCC-CASE-NNN/ (D-GOV-49; docs/SPEC.md §1.2); found {found}"
    )


def test_dag_case_must_sit_directly_under_cases(tmp_path: Path) -> None:
    case = write_case(tmp_path / "execution/_DAG/cases/SCC-CASE-001/nested", "SCC-CASE-001")
    assert vscc.validate_case(case) == [misplaced("_DAG/cases/SCC-CASE-001/nested/")]


@pytest.mark.parametrize(
    "relative",
    [
        "SCC-CASE-001",  # directly under _DAG/
        "DAG-011/SCC-CASE-001",  # in a DAG version folder
        "DAG-011/cases/SCC-CASE-001",  # a cases/ folder that is not _DAG/cases/
        "_Candidates/DAG-012/SCC-CASE-001",  # nested deeper
        "scc-cases/CASE-SCC-001_Legacy_Name",  # a legacy-style case under _DAG/
    ],
)
def test_case_elsewhere_under_dag_is_refused(tmp_path: Path, relative: str) -> None:
    case = write_case(tmp_path / "execution" / "_DAG" / relative, Path(relative).name)
    assert vscc.validate_case(case) == [misplaced(f"_DAG/{relative}/")]


def test_case_elsewhere_under_dag_keeps_content_and_one_home_checks(tmp_path: Path) -> None:
    case = write_case(tmp_path / "execution/_DAG/SCC-CASE-001", "SCC-CASE-001")
    (case / "Case_QA.md").unlink()
    assert vscc.validate_case(case) == [misplaced("_DAG/SCC-CASE-001/"), "missing required file: Case_QA.md"]
    write_case(tmp_path / "execution/_DAG/SCC-CASE-002", "SCC-CASE-002")
    legacy_case(tmp_path)
    expected_legacy = (
        "project also holds SCC cases in a legacy PKG-00 home "
        f"({vscc.LEGACY_CONTROL_DELIVERABLE}/1_Working/{LEGACY_DELIVERABLE}/scc-cases); each project uses one case home"
    )
    assert vscc.validate_case(tmp_path / "execution/_DAG/SCC-CASE-002") == [
        misplaced("_DAG/SCC-CASE-002/"),
        expected_legacy,
    ]


def test_dag_tool_root_itself_is_not_a_case(tmp_path: Path) -> None:
    dag = tmp_path / "execution" / "_DAG"
    dag.mkdir(parents=True)
    assert vscc.validate_case(dag) == ["path is the _DAG/ tool root, not a case folder; pass _DAG/cases/<CASE-ID>/"]


def test_cli_fails_case_directly_under_dag(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    case = write_case(tmp_path / "execution/_DAG/SCC-CASE-001", "SCC-CASE-001")
    monkeypatch.setattr("sys.argv", ["validate_scc_resolution_case.py", str(case)])
    assert vscc.main() == 1
    assert capsys.readouterr().out == (
        f"FAIL: SCC resolution case validation\n- {misplaced('_DAG/SCC-CASE-001/')}\n"
    )


def test_legacy_case_rejects_split_with_dag_home(tmp_path: Path) -> None:
    case = legacy_case(tmp_path)
    dag_case(tmp_path, "SCC-CASE-001")
    dag_case(tmp_path, "SCC-CASE-002")
    assert vscc.validate_case(case) == [
        "project also holds SCC cases in the _DAG/cases/ home (SCC-CASE-001; SCC-CASE-002); each project uses one case home"
    ]


def test_legacy_case_ignores_empty_dag_cases_home_and_other_projects(tmp_path: Path) -> None:
    case = legacy_case(tmp_path / "app")
    (tmp_path / "app" / "execution" / "_DAG" / "cases").mkdir(parents=True)
    dag_case(tmp_path / "piping")
    assert vscc.validate_case(case) == []


def test_legacy_split_reported_under_any_execution_root_name(tmp_path: Path) -> None:
    deliverable = tmp_path / "project-exec" / vscc.LEGACY_CONTROL_DELIVERABLE / "1_Working" / LEGACY_DELIVERABLE
    case = write_case(deliverable / "scc-cases" / "CASE-SCC-002_Policy", "CASE-SCC-002_Policy")
    assert vscc.validate_case(case) == []
    write_case(tmp_path / "project-exec" / "_DAG" / "cases" / "SCC-CASE-001", "SCC-CASE-001")
    assert vscc.validate_case(case) == [
        "project also holds SCC cases in the _DAG/cases/ home (SCC-CASE-001); each project uses one case home"
    ]


def test_dag_cases_home_itself_is_not_a_case(tmp_path: Path) -> None:
    case = dag_case(tmp_path)
    errors = vscc.validate_case(case.parent)
    assert errors == ["path is the _DAG/cases/ home, not a case folder; pass _DAG/cases/<CASE-ID>/"]


def test_dag_case_missing_files_reported_with_location_errors(tmp_path: Path) -> None:
    case = dag_case(tmp_path, "SCC-001")
    (case / "Case_QA.md").unlink()
    assert vscc.validate_case(case) == [
        "folder name 'SCC-001' is not a case ID of the form SCC-CASE-NNN (D-GOV-49)",
        "missing required file: Case_QA.md",
    ]


def test_dag_home_under_any_execution_root_name(tmp_path: Path) -> None:
    case = write_case(tmp_path / "project-exec" / "_DAG" / "cases" / "SCC-CASE-007", "SCC-CASE-007")
    assert vscc.validate_case(case) == []


def test_cli_reports_dag_case(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    case = dag_case(tmp_path)
    monkeypatch.setattr("sys.argv", ["validate_scc_resolution_case.py", str(case)])
    assert vscc.main() == 0
    assert capsys.readouterr().out == "PASS: SCC resolution case validation\n"
    (case.parent / "_run_records").mkdir()
    assert vscc.main() == 1
    assert "FAIL: SCC resolution case validation" in capsys.readouterr().out


def test_symlinked_case_into_dag_refused(tmp_path):
    execution = tmp_path / "proj" / "execution"
    real = execution / "elsewhere" / "SCC-CASE-001"
    real.mkdir(parents=True)
    (execution / "_DAG").mkdir()
    (execution / "_DAG" / "SCC-CASE-001").symlink_to(real, target_is_directory=True)
    errors = vscc.validate_case(execution / "_DAG" / "SCC-CASE-001")
    assert any("through a symbolic link" in e for e in errors), errors


def test_symlinked_dag_folder_refused(tmp_path):
    execution = tmp_path / "proj" / "execution"
    real_dag = tmp_path / "outside" / "_DAGREAL"
    (real_dag / "cases" / "SCC-CASE-001").mkdir(parents=True)
    execution.mkdir(parents=True)
    (execution / "_DAG").symlink_to(real_dag, target_is_directory=True)
    errors = vscc.validate_case(execution / "_DAG" / "cases" / "SCC-CASE-001")
    assert any("through a symbolic link" in e for e in errors), errors


def test_differently_cased_dag_refused(tmp_path):
    case = tmp_path / "proj" / "execution" / "_dag" / "cases" / "SCC-CASE-001"
    case.mkdir(parents=True)
    errors = vscc.validate_case(case)
    assert any("named exactly _DAG/cases/" in e for e in errors), errors


def test_symlink_above_the_project_is_not_a_route(tmp_path):
    real_parent = tmp_path / "real"
    case = real_parent / "proj" / "execution" / "_DAG" / "cases" / "SCC-CASE-001"
    case.mkdir(parents=True)
    (tmp_path / "linked").symlink_to(real_parent, target_is_directory=True)
    errors = vscc.validate_case(tmp_path / "linked" / "proj" / "execution" / "_DAG" / "cases" / "SCC-CASE-001")
    assert not any("symbolic link" in e for e in errors), errors
