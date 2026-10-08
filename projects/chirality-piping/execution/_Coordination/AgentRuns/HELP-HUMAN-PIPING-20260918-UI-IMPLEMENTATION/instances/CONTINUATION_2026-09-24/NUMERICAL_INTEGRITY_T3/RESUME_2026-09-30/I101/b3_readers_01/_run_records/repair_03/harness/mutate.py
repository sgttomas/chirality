"""I101: run mutants one at a time in an archive copy, through job.sh (one heavy job at a time).
Usage: mutate.py <rs|ts|py> <copy name> <spec.py> <out.jsonl> [ids...]
rs: cargo test --locked --offline [--lib] --test retained_precision_contract b3 (target WT/targets/i101-b3r-mut; --lib for
the control and the step-6 function's mutant); a spec may set RS_TESTS = {id: [cargo test selection...]} instead (repair 03)
ts: vitest run src/features/results/retainedPrecision.test.ts src/features/results/outputPolicy.test.ts
py (lane T's carrier schemas): pytest tests/test_retained_precision_schema.py tests/test_source_block_schema_contract.py
tests/test_results_dispatcher_v0_3.py with WT/venv (no install)
A mutant is killed when the run fails with an assertion (a test failure), not a build error."""
import json, os, re, runpy, subprocess, sys, pathlib
kind, copy, spec, out = sys.argv[1:5]
only = set(sys.argv[5:])
WT = pathlib.Path("WT"); S = WT / "scratch/i101_b3r"
P = S / "copies" / copy / "projects/chirality-piping"
spec_ns = runpy.run_path(spec); mutants = spec_ns["M"]; RS_TESTS = spec_ns.get("RS_TESTS", {})
LIB = {"control", "B06a"}  # the step-6 function's reader-local unit test lives in the lib target
def run(label, mid):
    if kind == "rs":
        cmd = [str(S / "harness/job.sh"), "cargo", label, str(P / "core/reporting/result_export"), str(WT / "targets/i101-b3r-mut"),
               "test", "--locked", "--offline"] + (RS_TESTS[mid] if mid in RS_TESTS else (["--lib"] if mid in LIB else []) + ["--test", "retained_precision_contract", "b3"])
    elif kind == "py":
        cmd = [str(S / "harness/job.sh"), "slot", label, str(P), str(WT / "venv/bin/python"), "-m", "pytest", "-p", "no:cacheprovider",
               f"--basetemp={S / 'tmp' / label / 'bt'}", "-q", "-rf", "tests/test_retained_precision_schema.py",
               "tests/test_source_block_schema_contract.py", "tests/test_results_dispatcher_v0_3.py"]
    else:
        cmd = [str(S / "harness/job.sh"), "slot", label, str(P / "apps/desktop"), str(P / "node_modules/.bin/vitest"), "run", "--reporter=verbose",
               "src/features/results/retainedPrecision.test.ts", "src/features/results/outputPolicy.test.ts"]
    # The caller's PATH (cargo and node); no B3B_* or RV113_* output variable reaches a mutant run.
    env = {"PATH": os.environ["PATH"], "HOME": str(pathlib.Path.home()), "RUST_TEST_THREADS": "4"}
    if kind == "py":  # the two helper binaries, built once through t3_cargo.sh (py_helpers.sh): no cargo inside the job
        env["OPENPIPESTRESS_CHECKED_JSON_BIN"] = str(WT / "targets/i101-b3r-pyh/cj/release/openpipestress_jcs_ijson")
        env["OPENPIPESTRESS_UNITS_BIN"] = str(WT / "targets/i101-b3r-pyh/units/release/openpipestress_units")
    rc = subprocess.run(cmd, env=env).returncode
    log = re.sub(r"\x1b\[[0-9;]*m", "", (S / "logs" / f"{label}.log").read_text(errors="replace"))  # vitest's colours
    if kind == "rs":
        failed = re.findall(r"^test (\S+) \.\.\. FAILED", log, re.M)
        build_error = bool(re.search(r"^error(\[E\d+\])?:", log, re.M)) and not failed
    elif kind == "py":
        failed = sorted(set(re.findall(r"^FAILED (\S+)", log, re.M)))
        build_error = ("ERROR collecting" in log) and not failed
    else:
        failed = sorted(set(re.findall(r"^\s+[×✗] (.+?)(?: \d+ms)?$", log, re.M)))
        build_error = ("Transform failed" in log or "SyntaxError" in log) and not failed
    return rc, failed, build_error
with open(out, "a") as f:
    if not only or "control" in only:
        rc, failed, be = run(f"{kind}_mut_control", "control")
        f.write(json.dumps({"id": "control", "rc": rc, "failed": failed, "build_error": be}) + "\n"); f.flush()
    for mid, desc, rel, old, new in mutants:
        if only and mid not in only: continue
        path = P / rel; pristine = path.read_text()
        n = pristine.count(old)
        if n != 1:
            f.write(json.dumps({"id": mid, "desc": desc, "error": f"occurrences {n}"}) + "\n"); f.flush(); continue
        path.write_text(pristine.replace(old, new))
        try:
            rc, failed, be = run(f"{kind}_mut_{mid}", mid)
        finally:
            path.write_text(pristine)
        f.write(json.dumps({"id": mid, "desc": desc, "file": rel, "rc": rc, "killed": rc != 0 and bool(failed), "failed": failed, "build_error": be}) + "\n"); f.flush()
