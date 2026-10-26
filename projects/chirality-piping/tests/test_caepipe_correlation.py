#!/usr/bin/env python3
"""Focused tests for the DEL-17-05 correlation pilot: comparison record, harness configuration and hand calculations.

Every number here is synthetic or invented; nothing is CAEPIPE output.
"""

from __future__ import annotations

import dataclasses
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.handoff.caepipe_external import (  # noqa: E402
    HarnessConfig,
    HarnessSkip,
    build_comparison_record,
    case_paths,
    resolve_harness_config,
    run_caepipe_round_trip,
)
from core.handoff.caepipe_external.harness import (  # noqa: E402
    ENV_VAR,
    ContainmentError,
    _quote,
    last_json_object,
)
from core.handoff.caepipe_mbf import render_caepipe_mbf_si  # noqa: E402
from tools.caepipe_correlation import run_pilot  # noqa: E402
from validation.caepipe_correlation import hand_calcs  # noqa: E402


CASES_DIR = ROOT / "validation" / "caepipe_correlation" / "cases"
PARSER_FIXTURE = ROOT / "fixtures" / "caepipe_external" / "invented" / "print_to_file_results.csv"
SUS = "Sustained (W+P)"
TOL = {
    "analytic_vs_swbpipe": {"rel": 1e-6, "abs": {"m": 1e-9, "rad": 1e-9, "N": 1e-6, "N*m": 1e-6}},
    "external": {"rel": 5e-3, "abs": {"m": 2e-6, "rad": 2e-6, "N": 1.0, "N*m": 1.0}},
}


# --------------------------------------------------------------------------
# comparison record (synthetic numbers)
# --------------------------------------------------------------------------
def swb_rows(*, uy_mm=-10.0, rz_rad=-0.01, fy=2000.0, restraint_fy=50.0):
    def row(kind, entity, value, unit, component=None):
        item = {"id": f"r:{kind}:{entity}:{component}", "kind": kind, "entity_ref": entity, "value": value,
                "unit": unit, "basis_ref": {"ref_type": "load_case", "ref_id": "LC1"}}
        if component:
            item["metadata"] = {"component": component}
        return item
    rows = [row("global_nodal_displacement_y", "N1", uy_mm, "mm"), row("global_nodal_rotation_z", "N1", rz_rad, "rad")]
    if fy is not None:
        rows.append(row("support_reaction_component_v2", "A0", fy, "N", "Fy"))
    rows.append(row("support_reaction_component_v2", "G1", restraint_fy, "N", "Fy"))
    return {"mechanics_envelope": {"results": rows}}


MBF = {
    "profile_id": "caepipe-mbf-si-pilot-1",
    "node_map": {"N0": "10", "N1": "20", "N2": "30"},
    "support_map": {"A0": {"node": "10", "caepipe_kind": "anchor"}, "G1": {"node": "30", "caepipe_kind": "restraint"}},
    "load_case_map": {"LC1": SUS},
    "assumptions": ["invented assumption"],
    "loss_report": [{"entity": "x", "code": "MBF-SI-X"}],
}


def parsed(*, uy_mm=-10.0, rz_deg=None, anchor_fy=-2000.0, restraint_fy=-50.0, drop_node=False):
    rz_deg = math.degrees(-0.01) if rz_deg is None else rz_deg
    displacements = {} if drop_node else {"20": {"ux": 0.0, "uy": uy_mm, "uz": 0.0, "rx": 0.0, "ry": 0.0, "rz": rz_deg}}
    return {
        "parser_version": "caepipe-print-csv-1",
        "header": {"product_label": "Invented Product", "version": "0.0-invented"},
        "units": {"length": "mm", "rotation": "deg", "force": "N", "moment": "N*m"},
        "load_cases": {SUS: {
            "displacements": displacements,
            "anchor_loads_global": {"10": {"fx": 0.0, "fy": anchor_fy, "fz": 0.0, "mx": 0.0, "my": 0.0, "mz": 0.0}},
            "restraint_loads_global": {"30": {"fx": 0.0, "fy": restraint_fy, "fz": 0.0}},
        }},
    }


def synthetic_case(**extra):
    case = {
        "case_id": "invented-case",
        "quantities": [
            {"id": "uy", "quantity": "displacement", "node": "N1", "component": "y", "load_case": "LC1"},
            {"id": "rz", "quantity": "rotation", "node": "N1", "component": "z", "load_case": "LC1"},
            {"id": "fy", "quantity": "reaction_force", "support": "A0", "component": "y", "load_case": "LC1"},
            {"id": "gy", "quantity": "reaction_force", "support": "G1", "component": "y", "load_case": "LC1"},
        ],
        "tolerances": json.loads(json.dumps(TOL)),
        "declared_differences": [],
    }
    case.update(extra)
    return case


ANALYTIC = {
    "uy": {"value": -0.010, "unit": "m", "formula": "invented", "basis": "Euler-Bernoulli"},
    "rz": {"value": -0.01, "unit": "rad", "formula": "invented", "basis": "Euler-Bernoulli"},
    "fy": {"value": 2000.0, "unit": "N", "formula": "invented", "basis": "Euler-Bernoulli"},
    "gy": {"value": 50.0, "unit": "N", "formula": "invented", "basis": "Euler-Bernoulli"},
}
MODEL = {"invented": True, "nodes": [{"id": "N1"}]}


def record(case=None, payload=None, caepipe=None, analytic=ANALYTIC, mbf_text="INVENTED\r\n"):
    return build_comparison_record(case or synthetic_case(), swbpipe_model=MODEL,
                                   swbpipe_result_payload=payload or swb_rows(), mbf_result=MBF,
                                   mbf_text=mbf_text, parsed_caepipe=caepipe if caepipe is not None else parsed(),
                                   analytic=analytic)


def quantity(result, qid):
    return next(row for row in result["quantities"] if row["id"] == qid)


def outcomes(row):
    return {name: check["outcome"] for name, check in row["checks"].items()}


def test_all_matched_with_unit_conversion_and_sign_flip():
    result = record()
    for qid in ("uy", "rz", "fy", "gy"):
        row = quantity(result, qid)
        assert set(outcomes(row).values()) == {"matched_within_tolerance"}, qid
        assert row["cause"] is None and row["disposition"] == "no_action"
    assert quantity(result, "uy")["values"]["caepipe"] == pytest.approx(-0.010, rel=1e-15)
    assert quantity(result, "rz")["values"]["caepipe"] == pytest.approx(-0.01, rel=1e-15)  # deg -> rad
    assert quantity(result, "fy")["values"]["caepipe"] == 2000.0  # pipe-on-anchor -2000 flipped
    assert quantity(result, "fy")["value_sources"]["caepipe"]["sign_flip"] is True
    assert quantity(result, "gy")["value_sources"]["caepipe"]["section"] == "restraint_loads_global"
    assert result["summary"]["by_cause"] == {"none": 4}


def test_unflipped_reaction_exceeds_tolerance():
    result = record(caepipe=parsed(anchor_fy=2000.0))
    row = quantity(result, "fy")
    assert outcomes(row) == {"analytic_vs_swbpipe": "matched_within_tolerance",
                             "swbpipe_vs_caepipe": "delta_exceeds_tolerance",
                             "analytic_vs_caepipe": "delta_exceeds_tolerance"}
    assert row["checks"]["swbpipe_vs_caepipe"]["difference"] == -4000.0


def test_triangle_rule_caepipe_side():
    row = quantity(record(caepipe=parsed(uy_mm=-11.0)), "uy")
    assert row["cause"]["label"] == "export_mapping_issue"
    assert row["cause"]["evidence"] == "triangle_rule"
    assert row["cause"]["basis"] == "ASSUMPTION"
    assert row["disposition"] == "requires_professional_review"


def test_triangle_rule_swbpipe_alone():
    row = quantity(record(payload=swb_rows(uy_mm=-11.0)), "uy")
    assert outcomes(row)["analytic_vs_caepipe"] == "matched_within_tolerance"
    assert row["cause"]["label"] == "solver_defect_candidate"
    assert row["disposition"] == "requires_professional_review"


def test_triangle_rule_analytic_alone():
    analytic = dict(ANALYTIC, uy={**ANALYTIC["uy"], "value": -0.011})
    row = quantity(record(analytic=analytic), "uy")
    assert outcomes(row) == {"analytic_vs_swbpipe": "delta_exceeds_tolerance",
                             "swbpipe_vs_caepipe": "matched_within_tolerance",
                             "analytic_vs_caepipe": "delta_exceeds_tolerance"}
    assert row["cause"]["label"] == "missing_model_parameter"


def test_row_unmatched_both_ways():
    row = quantity(record(caepipe=parsed(drop_node=True)), "uy")
    assert outcomes(row)["swbpipe_vs_caepipe"] == "row_unmatched_internal_only"
    assert outcomes(row)["analytic_vs_caepipe"] == "row_unmatched_internal_only"
    assert row["cause"]["label"] == "parser_mapping_issue"
    row = quantity(record(payload=swb_rows(fy=None)), "fy")
    # In each check the first-named source is the internal side of the pair.
    assert outcomes(row)["analytic_vs_swbpipe"] == "row_unmatched_internal_only"
    assert outcomes(row)["swbpipe_vs_caepipe"] == "row_unmatched_external_only"
    assert row["cause"]["label"] == "missing_model_parameter"
    assert row["disposition"] == "requires_professional_review"


def test_tolerance_tbd_and_missing_analytic():
    case = synthetic_case()
    del case["tolerances"]["external"]
    result = record(case=case)
    row = quantity(result, "uy")
    assert outcomes(row)["swbpipe_vs_caepipe"] == "tolerance_tbd"
    assert row["status"] == "no_verdict" and row["cause"] is None
    assert result["tolerance_basis"]["swbpipe_vs_caepipe"]["status"] == "tolerance_tbd"
    analytic = {key: value for key, value in ANALYTIC.items() if key != "rz"}
    row = quantity(record(analytic=analytic), "rz")
    assert outcomes(row) == {"analytic_vs_swbpipe": "not_applicable", "swbpipe_vs_caepipe": "matched_within_tolerance",
                             "analytic_vs_caepipe": "not_applicable"}
    assert row["disposition"] == "no_action"
    row = quantity(record(analytic=analytic, caepipe=parsed(rz_deg=1.0)), "rz")
    assert row["cause"]["label"] == "caepipe_profile_unknown"


def test_declared_difference_with_prediction_and_without():
    predicted = {"id": "dd", "applies_to": ["uy"], "cause": "documented_behavior_difference",
                 "description": "invented", "predicted_caepipe_minus_swbpipe": -0.001}
    within = quantity(record(case=synthetic_case(declared_differences=[predicted]), caepipe=parsed(uy_mm=-11.05)), "uy")
    assert within["cause"]["label"] == "documented_behavior_difference"
    assert within["cause"]["evidence"] == "predicted"
    assert within["cause"]["declared_difference"] == "dd"
    assert within["disposition"] == "assumption_recorded"
    outside = quantity(record(case=synthetic_case(declared_differences=[predicted]), caepipe=parsed(uy_mm=-11.2)), "uy")
    assert outside["cause"]["label"] == "export_mapping_issue"
    declared_only = dict(predicted, predicted_caepipe_minus_swbpipe=None)
    row = quantity(record(case=synthetic_case(declared_differences=[declared_only]), caepipe=parsed(uy_mm=-12.0)), "uy")
    assert row["cause"]["evidence"] == "declared_only"


def test_declared_difference_never_masks_a_swbpipe_departure_from_the_analytic_witness():
    # All three disagree (analytic -10 mm, SWBPIPE -12 mm, CAEPIPE -13.05 mm) and the residual CAEPIPE - SWBPIPE
    # (-1.05 mm) lies within 10 % of the declared prediction (-1 mm): the triangle rule still names the cause.
    predicted = {"id": "dd", "applies_to": ["uy"], "cause": "documented_behavior_difference",
                 "description": "invented", "predicted_caepipe_minus_swbpipe": -0.001}
    for declaration in (predicted, dict(predicted, predicted_caepipe_minus_swbpipe=None)):
        row = quantity(record(case=synthetic_case(declared_differences=[declaration]), payload=swb_rows(uy_mm=-12.0),
                              caepipe=parsed(uy_mm=-13.05)), "uy")
        assert set(outcomes(row).values()) == {"delta_exceeds_tolerance"}
        assert row["cause"]["label"] == "solver_defect_candidate"
        assert row["cause"]["evidence"] == "triangle_rule"
        assert row["cause"]["declared_difference_also_matched"] == "dd"
        assert row["disposition"] == "requires_professional_review"
    # Without an analytic witness a declaration is not enough either.
    analytic = {key: value for key, value in ANALYTIC.items() if key != "uy"}
    row = quantity(record(case=synthetic_case(declared_differences=[predicted]), analytic=analytic,
                          caepipe=parsed(uy_mm=-11.05)), "uy")
    assert row["cause"]["label"] == "caepipe_profile_unknown"
    assert row["cause"]["declared_difference_also_matched"] == "dd"


def test_fault_injection_is_classified_as_deliberate_export_issue():
    fault = {"target": "mbf", "description": "invented deliberate fault", "material_modulus_factor": 1.1}
    result = record(case=synthetic_case(fault_injection=fault), caepipe=parsed(uy_mm=-9.0))
    row = quantity(result, "uy")
    assert row["cause"]["label"] == "export_mapping_issue"
    assert row["cause"]["evidence"] == "deliberate_fault_injection"
    assert row["disposition"] == "bug_report"
    assert quantity(result, "fy")["disposition"] == "no_action"
    assert result["manual_changes"]["description"] == "invented deliberate fault"


def test_record_carries_prd_22_5_fields():
    result = record()
    for key in ("internal_model_hash", "exported_model_hash", "target_tool", "target_version", "product_label",
                "import_export_assumptions", "manual_changes", "load_case_mapping", "support_mapping",
                "comparison_basis", "tolerance_basis", "quantities", "summary", "discrepancy_disposition",
                "evidence_classification"):
        assert key in result, key
    canonical = json.dumps(MODEL, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    assert result["internal_model_hash"] == hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    assert result["exported_model_hash"] == hashlib.sha256(b"INVENTED\r\n").hexdigest()
    assert result["target_tool"] == "CAEPIPE" and result["target_version"] == "0.0-invented"
    assert result["manual_changes"] == "none"
    assert result["comparison_basis"]["caepipe_load_cases_compared"] == [SUS]
    assert "not validation" in result["evidence_classification"]
    assert all(entry["basis"] == "ASSUMPTION" for name, entry in result["tolerance_basis"].items()
               if isinstance(entry, dict))


# --------------------------------------------------------------------------
# harness configuration
# --------------------------------------------------------------------------
def git_only_path(tmp_path: Path) -> str:
    """A PATH holding only `git` (so prlctl is absent while the Git work-tree check still runs)."""
    directory = tmp_path / "bin-git-only"
    directory.mkdir()
    git = shutil.which("git")
    assert git, "git is required for this test"
    (directory / "git").symlink_to(git)
    return str(directory)


def exchange(tmp_path: Path, *, ignore="*\n", config=None) -> Path:
    root = tmp_path / "exchange"
    root.mkdir()
    if ignore is not None:
        (root / ".gitignore").write_text(ignore, encoding="utf-8")
    if config is not False:
        (root / "harness_config.json").write_text(json.dumps(config or {
            "vm_name": "invented-vm", "guest_executable": "C:\\Invented\\tool.exe",
            "guest_exchange_root": "Z:\\invented", "guest_work_root": "C:\\invented-work",
            "license_and_environment_responsibility_acknowledged": True,
        }), encoding="utf-8")
    return root


def skip_reason(environ) -> str:
    result = resolve_harness_config(environ)
    assert isinstance(result, HarnessSkip), result
    return result.reason


def test_harness_skips_when_unset_or_missing(tmp_path):
    assert "unset" in skip_reason({})
    assert "unset" in skip_reason({ENV_VAR: "  "})
    assert "does not exist" in skip_reason({ENV_VAR: str(tmp_path / "absent")})
    file_path = tmp_path / "file"
    file_path.write_text("x", encoding="utf-8")
    assert "directory" in skip_reason({ENV_VAR: str(file_path)})


def test_harness_skips_without_exact_gitignore(tmp_path):
    path = git_only_path(tmp_path)
    root = exchange(tmp_path, ignore=None)
    assert ".gitignore" in skip_reason({ENV_VAR: str(root), "PATH": path})
    (root / ".gitignore").write_text("*.csv\n", encoding="utf-8")
    assert ".gitignore" in skip_reason({ENV_VAR: str(root), "PATH": path})


def test_harness_refuses_folder_inside_git_work_tree(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init", "-q", str(repo)], check=True)
    root = repo / "exchange"
    root.mkdir()
    (root / ".gitignore").write_text("*", encoding="utf-8")
    reason = skip_reason({ENV_VAR: str(root), "PATH": git_only_path(tmp_path)})
    assert "inside a Git work tree" in reason


def test_harness_skips_without_config_or_acknowledgement(tmp_path):
    path = git_only_path(tmp_path)
    root = exchange(tmp_path, config=False)
    assert "harness_config.json" in skip_reason({ENV_VAR: str(root), "PATH": path})
    (root / "harness_config.json").write_text(json.dumps({"vm_name": "invented-vm"}), encoding="utf-8")
    assert "license_and_environment_responsibility_acknowledged" in skip_reason({ENV_VAR: str(root), "PATH": path})
    (root / "harness_config.json").write_text(json.dumps({
        "vm_name": "invented-vm", "license_and_environment_responsibility_acknowledged": True}), encoding="utf-8")
    assert "guest_executable" in skip_reason({ENV_VAR: str(root), "PATH": path})


@pytest.mark.parametrize("key,value", [
    ("guest_executable", 'C:\\Invented\\tool.exe" & calc & "'),
    ("guest_executable", "C:\\Invented\\%COMSPEC%\\tool.exe"),
    ("guest_executable", "C:\\Invented\\tool.exe\\"),
    ("guest_executable", "C:\\Invented\\a^b|c<d>e!f.exe"),
    ("guest_exchange_root", "\\\\invented-host\\share"),
    ("guest_exchange_root", "Z:\\invented\nnext"),
    ("guest_exchange_root", "invented\\relative"),
    ("guest_work_root", "C:\\invented-work\\..\\elsewhere"),
    ("guest_work_root", "C:/invented-work"),
])
def test_harness_refuses_guest_paths_outside_the_allow_list(tmp_path, key, value):
    config = {"vm_name": "invented-vm", "guest_executable": "C:\\Invented Tools (x86)\\tool_1.0-a.exe",
              "guest_exchange_root": "Z:\\invented", "guest_work_root": "C:\\invented-work\\",
              "license_and_environment_responsibility_acknowledged": True}
    root = exchange(tmp_path, config=config)
    environ = {ENV_VAR: str(root), "PATH": git_only_path(tmp_path)}
    assert isinstance(resolve_harness_config(environ, require_vm_tools=False), HarnessConfig)
    (root / "harness_config.json").write_text(json.dumps({**config, key: value}), encoding="utf-8")
    result = resolve_harness_config(environ, require_vm_tools=False)
    assert isinstance(result, HarnessSkip) and key in result.reason


def test_guest_command_quoting_refuses_shell_metacharacters():
    assert _quote("C:\\invented-work\\cpc-x\\model*.csv") == '"C:\\invented-work\\cpc-x\\model*.csv"'
    for bad in ('C:\\a" & calc', "C:\\%PATH%", "C:\\a\nb"):
        with pytest.raises(ValueError):
            _quote(bad)


def test_harness_skips_without_prlctl_and_resolves_with_it(tmp_path):
    path = git_only_path(tmp_path)
    root = exchange(tmp_path)
    result = resolve_harness_config({ENV_VAR: str(root), "PATH": path})
    assert isinstance(result, HarnessSkip) and "prlctl" in result.reason
    assert "prlctl on PATH" in result.checked
    offline = resolve_harness_config({ENV_VAR: str(root), "PATH": path}, require_vm_tools=False)
    assert isinstance(offline, HarnessConfig) and offline.prlctl is None
    fake = tmp_path / "bin-fake-prlctl"
    fake.mkdir()
    prlctl = fake / "prlctl"
    prlctl.write_text("#!/bin/sh\nexit 97\n", encoding="utf-8")
    prlctl.chmod(0o755)
    live = resolve_harness_config({ENV_VAR: str(root), "PATH": os.pathsep.join([path, str(fake)])})
    assert isinstance(live, HarnessConfig)
    assert live.prlctl == str(prlctl) and live.vm_name == "invented-vm"


def test_case_paths_layout_and_id_check(tmp_path):
    paths = case_paths(tmp_path, "cpc-99-invented")
    for layer in ("swbpipe", "caepipe_in", "caepipe_out", "parsed", "comparison"):
        assert paths[layer].is_dir()
    assert paths["manifest"] == tmp_path / "cases" / "cpc-99-invented" / "case_manifest.json"
    for bad in ("Upper", "-lead", "a/b", "x" * 64, "", "trailing-newline\n"):
        with pytest.raises(ValueError):
            case_paths(tmp_path, bad)


def test_last_json_object_takes_the_final_top_level_object():
    text = 'noise {not json\n{"a": {"b": 1}}\nmore\n{"status": "x", "gui": {"used": true}}\ntrailing'
    assert last_json_object(text) == {"status": "x", "gui": {"used": True}}
    assert last_json_object("no json here") is None


def fake_config(tmp_path: Path) -> HarnessConfig:
    root = exchange(tmp_path)
    return HarnessConfig(exchange_root=root, vm_name="invented-vm", guest_executable="C:\\Invented\\tool.exe",
                         guest_exchange_root="Z:\\invented", guest_work_root="C:\\invented-work",
                         prlctl="/invented/prlctl", acknowledged=True, trial_first_launch_date="2026-10-26",
                         checked=("invented",))


MBF_TEXT = "INVENTED\r\nMBF\r\n"
MBF_SHA = hashlib.sha256(MBF_TEXT.encode("utf-8")).hexdigest()


def test_round_trip_records_route_and_never_runs_a_real_prlctl(tmp_path):
    config = fake_config(tmp_path)
    calls = []

    def runner(argv, **kwargs):
        calls.append(argv)
        assert argv[:6] == ["/invented/prlctl", "exec", "invented-vm", "--current-user", "cmd", "/c"]
        assert kwargs["timeout"] == 600
        command = argv[6]
        stdout = ""
        if command.startswith("powershell"):
            stdout = 'WARNING: banner\n' + json.dumps({"status": "csv_from_gui_print", "gui": {"used": True},
                                                        "mbf_sha256": MBF_SHA.upper(),
                                                        "csv_path": "C:\\invented-work\\cpc-x\\model_results.csv"})
        if "copy /Y" in command and "caepipe_out" in command:
            (config.exchange_root / "cases" / "cpc-x" / "caepipe_out" / "model_results.csv").write_text("Invented\n")
        return subprocess.CompletedProcess(argv, 0, stdout, "")

    record_ = run_caepipe_round_trip(config, "cpc-x", MBF_TEXT, runner=runner)
    assert [call[6].split(" ")[0] for call in calls] == ["if", "powershell", "copy"]
    assert '"C:\\invented-work\\cpc-x\\model.mbf"' in calls[0][6].split(" & copy ")[0]  # old guest MBF deleted
    assert record_["guest_mbf_sha256"] == MBF_SHA and record_["input_hash_verified"] is True
    assert "-File \"Z:\\invented\\_harness\\Invoke-CaepipeRoundTrip.ps1\"" in calls[1][6]
    assert record_["route"] == "csv_from_gui_print"
    assert record_["command_shape"]["gui_print_fallback"] == {
        **record_["command_shape"]["gui_print_fallback"], "used": True, "label": "trial_build_workaround"}
    assert record_["mbf"]["sha256"] == MBF_SHA
    case_dir = config.exchange_root / "cases" / "cpc-x"
    assert (case_dir / "caepipe_in" / "model.mbf").read_bytes() == b"INVENTED\r\nMBF\r\n"
    assert (config.exchange_root / "_harness" / "Invoke-CaepipeRoundTrip.ps1").is_file()
    assert record_["observed_csv_path"]["host"] == "caepipe_out/model_results.csv"
    assert record_["expected_batch_csv_path"] == "C:\\invented-work\\cpc-x\\model.csv"
    assert record_["boundary_note"].startswith("regression/handoff evidence only")
    assert "invented-vm" not in json.dumps(record_)
    stored = json.loads((case_dir / "caepipe_out" / "run_record.json").read_text(encoding="utf-8"))
    assert stored["route"] == "csv_from_gui_print"
    assert not (config.exchange_root / "_harness" / "round_trip.lock").exists()


def test_round_trip_falls_back_to_a_guest_local_script_copy(tmp_path):
    config = fake_config(tmp_path)
    commands = []

    def runner(argv, **kwargs):
        commands.append(argv[6])
        stdout = ""
        if argv[6].startswith("powershell") and "invented-work" in argv[6].split(" -Exe ")[0]:
            stdout = json.dumps({"status": "no_results_after_batch", "gui": {"used": False},
                                 "mbf_sha256": hashlib.sha256(b"X\r\n").hexdigest()})
        return subprocess.CompletedProcess(argv, 0, stdout, "cannot run script" if not stdout else "")

    record_ = run_caepipe_round_trip(config, "cpc-y", "X\r\n", runner=runner)
    assert len(commands) == 5
    assert record_["guest_script"]["run_from"] == "guest_work_dir"
    assert record_["route"] == "no_results_after_batch"
    assert record_["observed_csv_path"]["host"] is None


def test_round_trip_stops_before_solving_when_preparation_fails(tmp_path):
    config = fake_config(tmp_path)
    commands = []

    def runner(argv, **kwargs):
        commands.append(argv[6])
        if argv[6].startswith("powershell"):
            raise AssertionError("solve must not run after a failed prepare step")
        return subprocess.CompletedProcess(argv, 1, "", "The system cannot find the file specified.")

    record_ = run_caepipe_round_trip(config, "cpc-p", MBF_TEXT, runner=runner)
    assert len(commands) == 1 and commands[0].startswith("if not exist")
    assert record_["route"] == "prepare_failed"
    assert record_["observed_csv_path"]["host"] is None and record_["guest_mbf_sha256"] is None


def test_round_trip_accepts_a_drive_root_exchange_share(tmp_path):
    # A shared folder mapped as a whole drive (`Z:\\`) is held as `Z:` after resolution and must still run.
    config = {"vm_name": "invented-vm", "guest_executable": "C:\\Invented\\tool.exe",
              "guest_exchange_root": "Z:\\", "guest_work_root": "C:\\invented-work",
              "license_and_environment_responsibility_acknowledged": True}
    root = exchange(tmp_path, config=config)
    resolved = resolve_harness_config({ENV_VAR: str(root), "PATH": git_only_path(tmp_path)}, require_vm_tools=False)
    assert isinstance(resolved, HarnessConfig) and resolved.guest_exchange_root == "Z:"
    commands = []

    def runner(argv, **kwargs):
        commands.append(argv[6])
        return subprocess.CompletedProcess(argv, 1, "", "invented failure")

    record_ = run_caepipe_round_trip(dataclasses.replace(resolved, prlctl="/invented/prlctl"), "cpc-z", MBF_TEXT,
                                     runner=runner)
    assert record_["route"] == "prepare_failed"
    assert "Z:\\cases\\cpc-z\\caepipe_in\\model.mbf" in commands[0]


def test_round_trip_refuses_outputs_of_a_different_guest_mbf(tmp_path):
    config = fake_config(tmp_path)
    commands = []
    out = config.exchange_root / "cases" / "cpc-h" / "caepipe_out"

    def runner(argv, **kwargs):
        commands.append(argv[6])
        stdout = ""
        if argv[6].startswith("powershell"):
            stdout = json.dumps({"status": "csv_from_batch", "mbf_sha256": "0" * 64,
                                 "csv_path": "C:\\invented-work\\cpc-h\\model.csv"})
        if "caepipe_out" in argv[6]:
            (out / "model.csv").write_text("Invented\n", encoding="utf-8")
        return subprocess.CompletedProcess(argv, 0, stdout, "")

    record_ = run_caepipe_round_trip(config, "cpc-h", MBF_TEXT, runner=runner)
    assert record_["route"] == "input_hash_mismatch"
    assert record_["guest_mbf_sha256"] == "0" * 64 and record_["input_hash_verified"] is False
    assert record_["observed_csv_path"]["host"] is None
    assert not any("caepipe_out" in command for command in commands)  # nothing is collected
    assert not (out / "model.csv").exists()


# --------------------------------------------------------------------------
# exchange containment and offline binding (no prlctl, no runner)
# --------------------------------------------------------------------------
def git_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "victim-repo"
    repo.mkdir()
    subprocess.run(["git", "init", "-q", str(repo)], check=True)
    return repo


def repo_entries(repo: Path) -> list[str]:
    return sorted(str(path.relative_to(repo)) for path in repo.rglob("*") if ".git" not in path.parts)


def test_symlinked_cases_dir_is_refused(tmp_path):
    config = fake_config(tmp_path)
    repo = git_repo(tmp_path)
    (config.exchange_root / "cases").symlink_to(repo, target_is_directory=True)
    with pytest.raises(ContainmentError):
        case_paths(config, "cpc-s")
    with pytest.raises(ContainmentError):
        run_caepipe_round_trip(config, "cpc-s", MBF_TEXT, runner=lambda *a, **k: pytest.fail("prlctl called"))
    lines = []
    assert run_pilot.run_case({"case_id": "cpc-s"}, config, runner="unused", offline=True, hand_calcs=None,
                              emit=lines.append) is False
    assert lines and "route=containment_violation" in lines[0]
    assert repo_entries(repo) == []


def test_symlinked_layer_dir_and_file_are_refused(tmp_path):
    config = fake_config(tmp_path)
    repo = git_repo(tmp_path)
    (repo / "tracked.txt").write_text("keep\n", encoding="utf-8")
    paths = case_paths(config, "cpc-l")
    paths["caepipe_out"].rmdir()
    paths["caepipe_out"].symlink_to(repo, target_is_directory=True)
    with pytest.raises(ContainmentError):
        case_paths(config, "cpc-l")
    with pytest.raises(ContainmentError):
        run_caepipe_round_trip(config, "cpc-l", MBF_TEXT, runner=lambda *a, **k: pytest.fail("prlctl called"))
    paths["caepipe_out"].unlink()
    paths["caepipe_out"].mkdir()
    (paths["caepipe_out"] / "run_record.json").symlink_to(repo / "tracked.txt")
    with pytest.raises(ContainmentError):
        run_caepipe_round_trip(config, "cpc-l", MBF_TEXT, runner=lambda *a, **k: pytest.fail("prlctl called"))
    assert repo_entries(repo) == ["tracked.txt"]
    assert (repo / "tracked.txt").read_text(encoding="utf-8") == "keep\n"
    assert not (config.exchange_root / "_harness" / "round_trip.lock").exists()


def test_case_variant_output_links_are_refused_before_collection(tmp_path):
    # On a case-insensitive file system a link named MODEL_RESULTS.CSV would receive the guest's copy of
    # model_results.csv; a link must be refused whatever its letter case, before the guest collects anything.
    victim = tmp_path / "outside" / "victim.txt"
    victim.parent.mkdir()
    victim.write_text("keep\n", encoding="utf-8")

    (tmp_path / "pre").mkdir()
    config = fake_config(tmp_path / "pre")
    paths = case_paths(config, "cpc-v")
    (paths["caepipe_out"] / "MODEL_RESULTS.CSV").symlink_to(victim)
    with pytest.raises(ContainmentError):
        run_caepipe_round_trip(config, "cpc-v", MBF_TEXT, runner=lambda *a, **k: pytest.fail("prlctl called"))

    (tmp_path / "during").mkdir()
    config = fake_config(tmp_path / "during")
    out = case_paths(config, "cpc-w")["caepipe_out"]
    commands = []

    def runner(argv, **kwargs):
        commands.append(argv[6])
        stdout = ""
        if argv[6].startswith("powershell"):
            (out / "Model_Results.csv").symlink_to(victim)  # planted while the guest solves
            stdout = json.dumps({"status": "csv_from_batch", "mbf_sha256": MBF_SHA,
                                 "csv_path": "C:\\invented-work\\cpc-w\\model_results.csv"})
        return subprocess.CompletedProcess(argv, 0, stdout, "")

    with pytest.raises(ContainmentError):
        run_caepipe_round_trip(config, "cpc-w", MBF_TEXT, runner=runner)
    assert not any("caepipe_out" in command and command.startswith("copy") for command in commands)
    assert victim.read_text(encoding="utf-8") == "keep\n"


def offline_case(tmp_path, monkeypatch, *, run_record=None, csv=True):
    """Prepare an offline run of the cantilever case with a stubbed SWBPIPE solve and an invented CSV."""
    case = next(item for item in run_pilot.load_cases() if item["case_id"] == "cpc-01-cantilever-force")
    monkeypatch.setattr(run_pilot, "solve_swbpipe", lambda runner, case_: (
        {"invented": True}, {"payload": {"mechanics_envelope": {"results": []}}}, ""))
    tmp_path.mkdir(exist_ok=True)
    config = fake_config(tmp_path)
    paths = case_paths(config, case["case_id"])
    if csv:
        shutil.copyfile(PARSER_FIXTURE, paths["caepipe_out"] / "model_results.csv")
    if run_record is not None:
        (paths["caepipe_out"] / "run_record.json").write_text(json.dumps(run_record), encoding="utf-8")
    lines = []
    ok = run_pilot.run_case(case, config, runner="unused", offline=True, hand_calcs=hand_calcs, emit=lines.append)
    return ok, lines, paths


def current_mbf_sha(case_id: str) -> str:
    case = next(item for item in run_pilot.load_cases() if item["case_id"] == case_id)
    text = render_caepipe_mbf_si(case["model"], title=case["title"],
                                 reference_temperature_c=case["reference_temperature_c"]).text
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def bound_record(sha: str, **extra):
    return {"document_kind": "openpipestress.caepipe_harness_run_record", "route": "csv_from_gui_print",
            "mbf": {"sha256": sha}, "guest_mbf_sha256": sha,
            "observed_csv_path": {"host": "caepipe_out/model_results.csv"}, **extra}


def test_offline_refuses_a_csv_without_a_run_record(tmp_path, monkeypatch):
    ok, lines, paths = offline_case(tmp_path, monkeypatch)
    assert ok is False and "route=unbound_output" in lines[0]
    assert not (paths["comparison"] / "comparison.json").exists() and not (paths["parsed"] / "caepipe_results.json").exists()


def test_offline_refuses_stale_and_guest_unverified_outputs(tmp_path, monkeypatch):
    sha = current_mbf_sha("cpc-01-cantilever-force")
    ok, lines, paths = offline_case(tmp_path / "stale", monkeypatch, run_record=bound_record("1" * 64))
    assert ok is False and "route=stale" in lines[0]
    assert not (paths["caepipe_in"] / "model.mbf").exists()  # the solved MBF is not overwritten
    ok, lines, _ = offline_case(tmp_path / "legacy", monkeypatch, run_record=bound_record(sha, guest_mbf_sha256=None))
    assert ok is False and "route=unbound_output" in lines[0]


def test_offline_bound_csv_is_compared_and_stdout_carries_status_only(tmp_path, monkeypatch):
    sha = current_mbf_sha("cpc-01-cantilever-force")
    ok, lines, paths = offline_case(tmp_path, monkeypatch, run_record=bound_record(sha))
    assert ok is True
    assert lines == ["cpc-01-cantilever-force: route=csv_from_gui_print; comparison record written: "
                     "cases/cpc-01-cantilever-force/comparison/comparison.json"]
    stored = json.loads((paths["comparison"] / "comparison.json").read_text(encoding="utf-8"))
    assert "by_outcome" in stored["summary"]


# --------------------------------------------------------------------------
# hand calculations and cases
# --------------------------------------------------------------------------
def test_cantilever_hand_calc_against_textbook_numbers():
    # Worked independently: D = 0.1683 m, Di = 0.1683 - 2 * 0.00711 = 0.15408 m.
    inertia = math.pi / 64.0 * (0.1683**4 - 0.15408**4)
    assert inertia == pytest.approx(1.1714e-5, rel=1e-3)
    tip = -2000.0 * 6.0**3 / (3.0 * 200.0e9 * inertia)
    values = hand_calcs.analytic_values("cpc-01-cantilever-force")
    assert values["n1_uy"]["value"] == pytest.approx(tip, rel=1e-12)
    assert values["n1_uy"]["value"] == pytest.approx(-0.06145, rel=1e-3)
    assert values["n1_rz"]["value"] == pytest.approx(-2000.0 * 36.0 / (2.0 * 200.0e9 * inertia), rel=1e-12)
    assert values["a0_fy"]["value"] == 2000.0 and values["a0_mz"]["value"] == 12000.0
    area = math.pi / 4.0 * (0.1683**2 - 0.15408**2)
    shear = hand_calcs.timoshenko_predictions("cpc-01-cantilever-force")["n1_uy"]
    assert shear == pytest.approx(-2000.0 * 6.0 / (0.5 * 200.0e9 / 2.6 * area), rel=1e-12)


def test_thermal_and_weight_hand_calcs():
    area = math.pi / 4.0 * (0.1683**2 - 0.15408**2)
    thermal = hand_calcs.analytic_values("cpc-02-anchored-thermal")
    assert thermal["a0_fx"]["value"] == pytest.approx(200.0e9 * area * 1.2e-5 * 100.0, rel=1e-12)
    assert thermal["a1_fx"]["value"] == -thermal["a0_fx"]["value"]
    weight = hand_calcs.analytic_values("cpc-03-anchored-weight")
    w = 7850.0 * area * 9.80665
    assert weight["a0_fy"]["value"] == pytest.approx(w * 3.0, rel=1e-12)
    assert weight["a0_mz"]["value"] == pytest.approx(w * 36.0 / 12.0, rel=1e-12)
    assert weight["a1_mz"]["value"] == -weight["a0_mz"]["value"]


def test_l_bend_and_branch_hand_calcs_satisfy_equilibrium():
    values = {key: item["value"] for key, item in hand_calcs.analytic_values("cpc-04-l-bend-thermal").items()}
    assert values["a_fx"] + values["b_fx"] == pytest.approx(0.0, abs=1e-9)
    assert values["a_fz"] + values["b_fz"] == pytest.approx(0.0, abs=1e-9)
    # Moments about A (origin): My_A + My_B + (zB Fx_B - xB Fz_B) = 0 with B = (4, 0, 3).
    assert values["a_my"] + values["b_my"] + 3.0 * values["b_fx"] - 4.0 * values["b_fz"] == pytest.approx(0.0, abs=1e-6)
    assert values["a_fx"] > 0 and values["a_fz"] > 0  # the expanding L pushes away from A; A pushes back
    branch = hand_calcs.branch_solution(shear=False)
    assert branch["a1_fy"] + branch["a2_fy"] + branch["a3_fy"] == pytest.approx(0.0, abs=1e-9)
    # Moments about X through J: Mx_A1 + Mx_A2 + Mx_A3 + (y Fz - z Fy)_A3 = 0, z_A3 = 4.
    assert branch["a1_mx"] + branch["a2_mx"] + branch["a3_mx"] - 4.0 * branch["a3_fy"] == pytest.approx(0.0, abs=1e-6)
    assert branch["j_uy"] > 0 and branch["j_rx"] < 0  # J follows the +Y motion; the Z-leg slope is +dv/dz


def test_case_files_render_within_the_evaluation_row_limit_and_match_hand_calcs():
    paths = sorted(CASES_DIR.glob("*.json"))
    assert [path.stem for path in paths] == sorted(hand_calcs.HAND_CALCS)
    for path in paths:
        case = json.loads(path.read_text(encoding="utf-8"))
        result = render_caepipe_mbf_si(case["model"], title=case["title"],
                                       reference_temperature_c=case["reference_temperature_c"])
        assert result.status == "written", (path.stem, result.diagnostics)
        assert result.layout_row_count <= 20, path.stem
        analytic = hand_calcs.analytic_values(case["case_id"])
        assert {item["id"] for item in case["quantities"]} == set(analytic), path.stem
        assert all(item["basis"] == "Euler-Bernoulli" for item in analytic.values())
        predictions = hand_calcs.timoshenko_predictions(case["case_id"])
        for declared in case["declared_differences"]:
            assert declared["cause"] == "documented_behavior_difference"
            if declared["predicted_caepipe_minus_swbpipe"] is not None:
                (qid,) = declared["applies_to"]
                assert declared["predicted_caepipe_minus_swbpipe"] == pytest.approx(predictions[qid], rel=1e-12)
        for name in ("analytic_vs_swbpipe", "external"):
            assert case["tolerances"][name]["basis"] == "ASSUMPTION"
        assert case["provenance"]["origin"] == "invented"
