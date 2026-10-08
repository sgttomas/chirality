#!/bin/bash
# RV113: the further C2 probe (probes_py2x.json) through the PY harness on the mutant copy, for the control
# (RV113_MUT unset) and P18; one t3_slot job each (a first version also ran P31, with a malformed probe).
WT=WT
S=$WT/scratch/rv113_rvr_01; T=$S/pyr2
VENV=VENV
B=$WT/targets/rv113-pybins2/release
P=$WT/rv113/py2-mut/projects/chirality-piping
cd "$P" || exit 90
for id in NONE P18; do
  out=$T/mutants/runs/$id; mkdir -p "$out" "$T/tmp/mut_$id"; mut=$([ "$id" = NONE ] || echo "$id")
  echo "# $id probes_py2x queued $(date -u '+%FT%TZ')" >> "$out/run.log"
  "$WT/tools/t3_slot.sh" /usr/bin/env RV113_MUT="$mut" TMPDIR="$T/tmp/mut_$id" OPENPIPESTRESS_CHECKED_JSON_BIN=$B/openpipestress_jcs_ijson OPENPIPESTRESS_BINARY64_JSON_BIN=$B/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$B/openpipestress_units /bin/bash -c '
    echo "# probes_py2x start $(date -u "+%FT%TZ")"; "$1" "$2" "$PWD" probes "$3" "$4/probes_py2x.jsonl" > "$4/probes_py2x.log" 2>&1; echo "probes_py2x rc=$?"; echo "# probes_py2x end $(date -u "+%FT%TZ")"' _ "$VENV/bin/python" "$S/tools/rv113_py_harness.py" "$T/probes/probes_py2x.json" "$out" >> "$out/run.log" 2>&1
done
echo py2x-done
