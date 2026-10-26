"""Run the CAEPIPE correlation pilot (DEL-17-05 Design §3-§7) for every case, one case at a time.

From the project root:

    python3 -m tools.caepipe_correlation.run_pilot [--case ID ...] [--offline] [--runner PATH]

Per case: the independent hand calculation, the SWBPIPE solve (headless runner),
the SI MBF (with the case's deliberate fault injection, if any), the live
CAEPIPE round trip through the configured virtual machine (skipped with
--offline, which reuses the CSV already stored in caepipe_out/), the parsed
CAEPIPE results, the three-way comparison record and the case manifest, all
under the private exchange folder named by SWBPIPE_CAEPIPE_EXCHANGE.

Standard output names each case's route and its counts by outcome and cause
only; it never prints a CAEPIPE value. Exit status 0 when every selected case
produced a comparison record, or when the harness is not configured (the reason
is printed and nothing is written); 1 otherwise; 2 for a usage error.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any, Callable, Mapping


PROJECT = Path(__file__).resolve().parents[2]
if str(PROJECT) not in sys.path:
    sys.path.insert(0, str(PROJECT))

from core.handoff.caepipe_external import (  # noqa: E402
    HarnessConfig,
    HarnessSkip,
    build_comparison_record,
    canonical_model_hash,
    case_paths,
    read_caepipe_print_csv,
    resolve_harness_config,
    run_caepipe_round_trip,
)
from core.handoff.caepipe_external.harness import BOUNDARY_NOTE, CASE_ID_PATTERN  # noqa: E402
from core.handoff.caepipe_mbf import render_caepipe_mbf_si  # noqa: E402


CASES_DIR = PROJECT / "validation" / "caepipe_correlation" / "cases"
HAND_CALCS = PROJECT / "validation" / "caepipe_correlation" / "hand_calcs.py"
RUNNER_ENV = "OPENPIPESTRESS_RUNNER_BIN"
MANIFEST_KIND = "openpipestress.caepipe_correlation.case_manifest"
LAYER_PRIVACY = {
    "swbpipe": "SWBPIPE request and result from the invented public case; kept with the private run",
    "caepipe_in": "SWBPIPE-derived MBF and writer maps; no CAEPIPE output",
    "caepipe_out": "PRIVATE: CAEPIPE output (CSV, .res, .mod) and the guest run log",
    "parsed": "PRIVATE: derived from CAEPIPE output",
    "comparison": "PRIVATE: derived from CAEPIPE output",
}


def load_cases(selected: list[str] | None = None) -> list[dict[str, Any]]:
    cases = {}
    for path in sorted(CASES_DIR.glob("*.json")):
        case = json.loads(path.read_text(encoding="utf-8"))
        if case.get("case_id") != path.stem or not CASE_ID_PATTERN.match(path.stem):
            raise ValueError(f"{path.name}: case_id must equal the file stem and match {CASE_ID_PATTERN.pattern}")
        cases[path.stem] = case
    if selected:
        unknown = sorted(set(selected) - set(cases))
        if unknown:
            raise KeyError(f"unknown case id(s): {', '.join(unknown)}")
        return [cases[case_id] for case_id in sorted(set(selected))]
    return [cases[case_id] for case_id in sorted(cases)]


def load_hand_calcs() -> Any:
    spec = importlib.util.spec_from_file_location("caepipe_correlation_hand_calcs", HAND_CALCS)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def runner_request(case_id: str) -> dict[str, Any]:
    """The headless runner request wrapper (shape of tests/test_headless_runner_contract.py final_runner_request)."""
    return {
        "request_id": f"caepipe-pilot-{case_id}",
        "operation": "solve",
        "operation_ref": {"ref_type": "api_operation", "ref_id": "solve"},
        "project_ref": {"ref_type": "project", "ref_id": case_id},
        "model_ref": {"ref_type": "model", "ref_id": case_id},
        "unit_system_ref": {"ref_type": "unit_system", "ref_id": "invented-si"},
        "load_basis_refs": [{"ref_type": "load_case", "ref_id": "LC1"}],
        "input_manifest_ref": {"ref_type": "audit_manifest", "ref_id": f"caepipe-pilot-{case_id}"},
        "requested_outputs": ["result_envelope", "audit_manifest", "diagnostics"],
        "privacy": {
            "local_only": True,
            "telemetry_allowed": False,
            "private_payload_redacted": True,
            "classification": "public_metadata",
        },
        "provenance": {
            "source_name": "invented CAEPIPE correlation pilot case",
            "source_location": f"validation/caepipe_correlation/cases/{case_id}.json",
            "source_license": "project invented",
            "contributor": "OpenPipeStress",
            "contributor_certification": "invented non-engineering example",
            "redistribution_status": "invented_non_engineering_example",
            "review_status": "pending",
        },
        "professional_boundary": {
            "human_review_required": True,
            "software_makes_compliance_claim": False,
            "software_makes_certification_claim": False,
            "software_makes_sealing_claim": False,
            "software_makes_approval_claim": False,
            "software_makes_authentication_claim": False,
        },
        "tbd_decisions": {
            "final_cli_command_syntax": "SETTLED_DEC_065",
            "package_scripts": "SETTLED_DEC_065",
            "process_invocation": "SETTLED_DEC_065",
            "network_access": "SETTLED_DEC_065",
            "filesystem_mutation_policy": "SETTLED_DEC_065",
            "ci_provider": "TBD",
            "release_matrix": "TBD",
            "public_transport_protocol": "TBD",
            "external_adapter_formats": "TBD",
            "physical_project_container": "TBD",
        },
    }


def solve_swbpipe(runner: str, case: Mapping[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None, str]:
    """Run `<runner> solve --explicit-local-private-intent --input -`; return (request body, output, error)."""
    body = {"request": runner_request(case["case_id"]),
            "solve": {"preview_model": {"model": case["model"], "materials": []}}}
    completed = subprocess.run([runner, "solve", "--explicit-local-private-intent", "--input", "-"],
                               input=json.dumps(body), capture_output=True, text=True, check=False)
    try:
        output = json.loads(completed.stdout)
    except json.JSONDecodeError:
        return body, None, f"runner exit {completed.returncode}; stdout is not JSON"
    mechanics = (((output.get("payload") or {}).get("mechanics_envelope") or {}).get("status") or {}).get("mechanics")
    if mechanics != "MECHANICS_SOLVED":
        return body, output, f"SWBPIPE mechanics status {mechanics!r} (runner exit {completed.returncode})"
    return body, output, ""


def apply_fault_injection(mbf_text: str, fault: Mapping[str, Any]) -> str:
    """Multiply the elastic modulus of every MATERIAL temperature row by the case's factor (deliberate fault)."""
    if fault.get("target") != "mbf" or "material_modulus_factor" not in fault:
        raise ValueError(f"unsupported fault injection {dict(fault)!r}")
    factor = float(fault["material_modulus_factor"])
    lines = mbf_text.split("\r\n")
    inside, changed = False, 0
    for index, line in enumerate(lines):
        if line == "MATERIAL":
            inside = True
        elif line.isupper() and line.isalpha():
            inside = False
        elif inside:
            fields = line.split(",")
            if len(fields) == 4:  # name, temperature, E, expansion coefficient
                fields[2] = format(float(fields[2]) * factor, ".10g")
                lines[index] = ",".join(fields)
                changed += 1
    if not changed:
        raise ValueError("fault injection found no MATERIAL temperature rows")
    return "\r\n".join(lines)


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _counts(summary: Mapping[str, Any]) -> str:
    parts = []
    for check, counts in summary["by_outcome"].items():
        parts.append(check + "{" + ", ".join(f"{key}={value}" for key, value in counts.items()) + "}")
    causes = ", ".join(f"{key}={value}" for key, value in summary["by_cause"].items())
    return "; ".join(parts) + "; causes{" + causes + "}"


def stored_csv(out_dir: Path) -> tuple[Path | None, dict[str, Any] | None]:
    record_path = out_dir / "run_record.json"
    record = json.loads(record_path.read_text(encoding="utf-8")) if record_path.is_file() else None
    host = ((record or {}).get("observed_csv_path") or {}).get("host")
    if host:
        candidate = out_dir.parent / host
        return (candidate if candidate.is_file() else None), record
    found = sorted(out_dir.glob("model*.csv"))
    return (found[0] if len(found) == 1 else None), record


def run_case(case: Mapping[str, Any], config: HarnessConfig, *, runner: str, offline: bool, hand_calcs: Any,
             emit: Callable[[str], None] = print,
             round_trip: Callable[..., dict[str, Any]] = run_caepipe_round_trip) -> bool:
    case_id = case["case_id"]
    paths = case_paths(config, case_id)
    analytic = hand_calcs.analytic_values(case_id)

    body, output, error = solve_swbpipe(runner, case)
    _write_json(paths["swbpipe"] / "request.json", body)
    if output is not None:
        _write_json(paths["swbpipe"] / "result.json", output)
    if error:
        emit(f"{case_id}: route=not_run; SWBPIPE not solved ({error})")
        return False
    payload = output["payload"]

    mbf = render_caepipe_mbf_si(case["model"], title=case.get("title", case_id),
                                reference_temperature_c=case.get("reference_temperature_c", 20.0))
    if mbf.status != "written":
        codes = sorted({item["code"] for item in mbf.diagnostics if item["severity"] == "error"})
        emit(f"{case_id}: route=not_run; MBF refused ({', '.join(codes)})")
        return False
    writer_text = mbf.text
    fault = case.get("fault_injection")
    mbf_text = apply_fault_injection(writer_text, fault) if fault else writer_text

    csv_path, run_record = None, None
    if offline:
        csv_path, run_record = stored_csv(paths["caepipe_out"])
        stored_hash = ((run_record or {}).get("mbf") or {}).get("sha256")
        if stored_hash and stored_hash != _sha256(mbf_text):
            emit(f"{case_id}: route=stale; the stored CAEPIPE output was produced from a different MBF")
            return False
    in_dir = paths["caepipe_in"]
    (in_dir / "model.mbf").write_bytes(mbf_text.encode("utf-8"))
    _write_json(in_dir / "id_map.json", {key: value for key, value in mbf.to_dict().items()
                                          if key.endswith("_map")})
    _write_json(in_dir / "mbf_render.json", {
        "profile_id": mbf.to_dict()["profile_id"], "status": mbf.status, "layout_row_count": mbf.layout_row_count,
        "diagnostics": mbf.diagnostics, "loss_report": mbf.loss_report, "assumptions": mbf.assumptions,
        "writer_text_sha256": _sha256(writer_text), "mbf_sha256": _sha256(mbf_text),
        "fault_injection": dict(fault) if fault else None,
    })

    if offline:
        route = (run_record or {}).get("route", "stored_csv_without_run_record") if csv_path else "no_stored_csv"
    else:
        run_record = round_trip(config, case_id, mbf_text)
        route = run_record["route"]
        host = (run_record.get("observed_csv_path") or {}).get("host")
        csv_path = paths["root"] / host if host else None
    if csv_path is None or not csv_path.is_file():
        emit(f"{case_id}: route={route}; no CAEPIPE CSV" + (" stored in caepipe_out/" if offline else "")
             + "; no comparison record")
        return False

    parsed = read_caepipe_print_csv(csv_path)
    _write_json(paths["parsed"] / "caepipe_results.json", parsed)
    _write_json(paths["parsed"] / "parser_diagnostics.json", {
        key: parsed[key] for key in ("parser_version", "diagnostics", "sections_parsed", "sections_skipped")})
    record = build_comparison_record(case, swbpipe_model=case["model"], swbpipe_result_payload=payload,
                                     mbf_result=mbf, mbf_text=mbf_text, parsed_caepipe=parsed, analytic=analytic)
    _write_json(paths["comparison"] / "comparison.json", record)
    _write_json(paths["manifest"], {
        "document_kind": MANIFEST_KIND,
        "case_id": case_id,
        "created": _now(),
        "mode": "offline" if offline else "live",
        "internal_model_hash": canonical_model_hash(case["model"]),
        "writer_text_sha256": _sha256(writer_text),
        "exported_model_hash": _sha256(mbf_text),
        "target_tool": record["target_tool"],
        "target_version": record["target_version"],
        "product_label": record["product_label"],
        "trial_first_launch_date": config.trial_first_launch_date,
        "route": route,
        "csv": str(csv_path.relative_to(paths["root"])),
        "layer_privacy": LAYER_PRIVACY,
        "boundary_note": BOUNDARY_NOTE,
    })
    emit(f"{case_id}: route={route}; {_counts(record['summary'])}")
    return True


def main(argv: list[str] | None = None, environ: Mapping[str, str] = os.environ) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--case", action="append", dest="cases", metavar="ID", help="run only this case (repeatable)")
    parser.add_argument("--offline", action="store_true", help="reuse the CAEPIPE CSV stored in caepipe_out/")
    parser.add_argument("--runner", help=f"openpipestress-runner executable (default: ${RUNNER_ENV})")
    args = parser.parse_args(argv)
    try:
        cases = load_cases(args.cases)
    except (KeyError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    config = resolve_harness_config(environ, require_vm_tools=not args.offline)
    if isinstance(config, HarnessSkip):
        print(f"CAEPIPE harness skipped: {config.reason}")
        return 0
    runner = args.runner or environ.get(RUNNER_ENV)
    if not runner or not Path(runner).is_file():
        print(f"error: no runner executable (--runner or ${RUNNER_ENV})", file=sys.stderr)
        return 2
    for warning in config.warnings:
        print(f"warning: {warning}")
    hand_calcs = load_hand_calcs()
    results = [run_case(case, config, runner=runner, offline=args.offline, hand_calcs=hand_calcs) for case in cases]
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
