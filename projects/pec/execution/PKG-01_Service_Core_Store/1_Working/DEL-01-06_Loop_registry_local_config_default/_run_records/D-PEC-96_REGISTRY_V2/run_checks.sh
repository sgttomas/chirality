#!/bin/bash
# usage: run_checks.sh <phase: pre|post> <checks dir> <repo root>
# Runs the proposal's registered checks and every-PR checks, logging each
# command, cwd (relative to the repo root) and exit code to COMMANDS.txt.
set -u
PH=$1; C=$2; R=$3
export PYTHONDONTWRITEBYTECODE=1
PY=/Library/Frameworks/Python.framework/Versions/3.13/bin/python3
echo "# phase $PH; PY=$PY ($($PY --version 2>&1)); PYTHONDONTWRITEBYTECODE=1; $(date)" >> "$C/COMMANDS.txt"
run(){ local cwd=$1 out=$2; shift 2; (cd "$cwd" && "$@" > "$C/$out" 2>&1); local e=$?; printf '%s\tcwd=.%s\t%s\t> checks/%s\n' "$e" "${cwd#$R}" "$*" "$out" >> "$C/COMMANDS.txt"; echo "$e $out"; }
for id in v2-loop-registry v2-store-guard v2-api-contract v2-core-posture harness-self-check; do
  run "$R" "${PH}_$id.stdout" "$PY" tools/software_workflow/run_registered_checks.py projects/pec/software-workflow.json --check "$id" --output "$C/${PH}_$id.json"
done
run "$R/projects/pec" "${PH}_loop_registry_verbose.out" "$PY" -m unittest discover -s v2/tests/config -p 'test_*.py' -v
run "$R/projects/pec" "${PH}_enforcement.out" "$PY" -m unittest discover -s v2/tests/enforcement -p 'test_*.py'
run "$R" "${PH}_harness.out" "$PY" tools/practitioner_harness/harness.py self-check
run "$R" "${PH}_receipts.out" "$PY" tools/validation/validate_pec_loop_receipts.py --repo-root .
run "$R" "${PH}_strict.out" "$PY" tools/validation/validate_decomposition_registers.py --strict projects/pec/execution
