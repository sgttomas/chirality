#!/bin/sh
# Finite-verification checks that must be identical before and after the D-PEC-99 act.
# Usage (from the repository root): sh <run root>/run_checks.sh <phase: pre|post>
export PYTHONDONTWRITEBYTECODE=1
R=projects/pec/execution/_Coordination/REMAINING_RETIREMENT_D-PEC-99_2026-09-26
C=$R/checks; p="$1"
run() { name="$1"; shift; "$@" > "$C/${p}_$name.out" 2>&1; rc=$?; echo "exit=$rc" >> "$C/${p}_$name.out"; echo "$p $name exit=$rc"; }
: > "$C/${p}_sow.out"; n=0; ok=0
while IFS= read -r s; do
  out=$(python3 tools/scope_of_work/validate_scope_of_work.py "$s" 2>&1); rc=$?
  printf '%s\texit=%s\t%s\n' "$s" "$rc" "$(printf '%s' "$out" | tr '\n' ' ')" >> "$C/${p}_sow.out"
  n=$((n+1)); [ "$rc" -eq 0 ] && ok=$((ok+1))
done < "$C/sow_targets.txt"
echo "sow $ok/$n exit0" | tee -a "$C/${p}_sow.out"
run strict python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution
run harness python3 tools/practitioner_harness/harness.py self-check
run receipts python3 tools/validation/validate_pec_loop_receipts.py --repo-root .
run tm_REGISTER python3 tools/taskmgmt/taskmgmt.py validate --register projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv
run tm_REGISTER_CLOSED python3 tools/taskmgmt/taskmgmt.py validate --register projects/pec/execution/_Coordination/_TaskManagement/REGISTER_CLOSED.csv
run entrypoints python3 tools/validation/validate_instruction_entrypoints.py .
