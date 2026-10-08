#!/bin/bash
# RV113: SR-PY repair 02's mutant schema, one t3_slot job per mutant (RV113_MUT=<id>; NONE = the control).
# Usage: run_py_mutants_r2.sh <tests|probes> <ids...>
#   tests:  pytest on the two retained test files in full (--maxfail=10), junit per mutant
#   probes: the reviewer's 392 probes through the PY harness
WT=WT
S=$WT/scratch/rv113_rvr_01
T=$S/pyr2
VENV=VENV
B=$WT/targets/rv113-pybins2/release
P=$WT/rv113/py2-mut/projects/chirality-piping
mode=$1; shift
for id in "$@"; do
  out=$T/mutants/runs/$id; mkdir -p "$out" "$T/tmp/mut_$id"
  mut=$([ "$id" = NONE ] || echo "$id")
  cd "$P" || exit 90
  if [ "$mode" = tests ]; then
    echo "# $id tests queued $(date -u '+%FT%TZ')" > "$out/run.log"
    "$WT/tools/t3_slot.sh" /usr/bin/env RV113_MUT="$mut" TMPDIR="$T/tmp/mut_$id" OPENPIPESTRESS_CHECKED_JSON_BIN=$B/openpipestress_jcs_ijson OPENPIPESTRESS_BINARY64_JSON_BIN=$B/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$B/openpipestress_units /bin/bash -c '
      echo "# start $(date -u "+%FT%TZ") RV113_MUT=${RV113_MUT:-unset}"
      "$1" -m pytest -p no:cacheprovider --basetemp="$TMPDIR/basetemp" -q -rf --junitxml="$2/pytest.xml" --maxfail=10 tests/test_retained_precision_contract.py tests/test_retained_precision_carriers.py > "$2/pytest.log" 2>&1; echo "pytest rc=$?"
      echo "# end $(date -u "+%FT%TZ")"' _ "$VENV/bin/python" "$out" >> "$out/run.log" 2>&1
  else
    echo "# $id probes queued $(date -u '+%FT%TZ')" >> "$out/run.log"
    "$WT/tools/t3_slot.sh" /usr/bin/env RV113_MUT="$mut" TMPDIR="$T/tmp/mut_$id" OPENPIPESTRESS_CHECKED_JSON_BIN=$B/openpipestress_jcs_ijson OPENPIPESTRESS_BINARY64_JSON_BIN=$B/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$B/openpipestress_units /bin/bash -c '
      echo "# probes start $(date -u "+%FT%TZ")"; "$1" "$2" "$PWD" probes "$3" "$4/probes.jsonl" > "$4/probes.log" 2>&1; echo "probes rc=$?"; echo "# probes end $(date -u "+%FT%TZ")"' _ "$VENV/bin/python" "$S/tools/rv113_py_harness.py" "$S/tsr1/probes/probes_ts1.json" "$out" >> "$out/run.log" 2>&1
  fi
done
