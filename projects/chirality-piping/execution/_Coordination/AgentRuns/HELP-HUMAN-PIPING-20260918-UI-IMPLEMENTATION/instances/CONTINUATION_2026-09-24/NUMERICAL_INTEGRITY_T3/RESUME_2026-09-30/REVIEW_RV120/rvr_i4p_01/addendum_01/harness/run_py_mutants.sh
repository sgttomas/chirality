#!/bin/bash
# RV120: PY's mutant copy (RV113's P01-P40 schema plus my Q01-Q05, all on RV113_MUT), one t3_slot pytest job per
# mutant on the two retained test files (--maxfail=10), as RV113 ran them. Usage: run_py_mutants.sh <ids...>
WT=WT
S=$WT/scratch/rv120_rvr
B=$WT/targets/rv120-pybins/release
P=$S/copies/py-mut/projects/chirality-piping
for id in "$@"; do
  out=$S/mutants/py_runs/$id; mkdir -p "$out" "$S/tmp/pymut_$id"
  mut=$([ "$id" = NONE ] || echo "$id")
  cd "$P" || exit 90
  echo "# $id tests queued $(date -u '+%FT%TZ')" > "$out/run.log"
  "$WT/tools/t3_slot.sh" /usr/bin/env RV113_MUT="$mut" TMPDIR="$S/tmp/pymut_$id" PYTHONDONTWRITEBYTECODE=1 OPENPIPESTRESS_CHECKED_JSON_BIN=$B/openpipestress_jcs_ijson OPENPIPESTRESS_BINARY64_JSON_BIN=$B/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$B/openpipestress_units /bin/bash -c '
    echo "# start $(date -u "+%FT%TZ") RV113_MUT=${RV113_MUT:-unset}"
    "$1" -m pytest -p no:cacheprovider --basetemp="$TMPDIR/basetemp" -q -rf --junitxml="$2/pytest.xml" --maxfail=10 tests/test_retained_precision_contract.py tests/test_retained_precision_carriers.py > "$2/pytest.log" 2>&1; echo "pytest rc=$?"
    echo "# end $(date -u "+%FT%TZ")"' _ "$WT/venv/bin/python" "$out" >> "$out/run.log" 2>&1
done
echo py-mutants-done
