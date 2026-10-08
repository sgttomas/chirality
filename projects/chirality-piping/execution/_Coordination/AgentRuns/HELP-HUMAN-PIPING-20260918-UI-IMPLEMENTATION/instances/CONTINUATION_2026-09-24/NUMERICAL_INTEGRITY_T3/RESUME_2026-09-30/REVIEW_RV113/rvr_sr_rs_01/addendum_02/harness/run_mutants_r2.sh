#!/bin/bash
# RV113: SR-RS repair 02's mutant schema, already built (no cargo). One t3_slot job per mutant.
# Usage: run_mutants_r2.sh <tests|probes> <ids...>   ("NONE" = the control: RV113_MUT unset)
#   tests:  RE's lib unit tests and the contract test binary
#   probes: the reviewer's probes (probes_all.json) through the census harness binary
WT=WT
S=$WT/scratch/rv113_rvr_01/rsr2
D=$WT/targets/rv113-rs2mut/debug/deps
RE=$WT/rv113/rs2-mut/projects/chirality-piping/core/reporting/result_export
bin() { echo "$D/$(ls "$D" | grep -E "^$1-[0-9a-f]+\$" | head -1)"; }
LIB=$(bin open_pipe_stress_result_export); CONTRACT=$(bin retained_precision_contract); CENSUS=$(bin rv113_census)
mode=$1; shift
for id in "$@"; do
  out=$S/mutants/runs/$id; mkdir -p "$out" "$S/tmp/mut_$id"
  mut=$([ "$id" = NONE ] || echo "$id")
  cd "$RE" || exit 90
  if [ "$mode" = tests ]; then
    echo "# $id tests queued $(date -u '+%FT%TZ')" > "$out/run.log"
    "$WT/tools/t3_slot.sh" /usr/bin/env RV113_MUT="$mut" TMPDIR="$S/tmp/mut_$id" RUST_TEST_THREADS=2 /bin/bash -c '
      echo "# start $(date -u "+%FT%TZ") RV113_MUT=${RV113_MUT:-unset}"
      "$1" > "$3/lib.log" 2>&1; echo "lib rc=$?"
      "$2" > "$3/contract.log" 2>&1; echo "contract rc=$?"
      echo "# end $(date -u "+%FT%TZ")"' _ "$LIB" "$CONTRACT" "$out" >> "$out/run.log" 2>&1
  else
    echo "# $id probes queued $(date -u '+%FT%TZ')" >> "$out/run.log"
    "$WT/tools/t3_slot.sh" /usr/bin/env RV113_MUT="$mut" TMPDIR="$S/tmp/mut_$id" RV113_PROBES="$S/probes/probes_all.json" RV113_PROBES_OUT="$out/probes.jsonl" RUST_TEST_THREADS=2 /bin/bash -c '
      echo "# probes start $(date -u "+%FT%TZ")"; "$1" rv113_probes --exact > "$2/harness.log" 2>&1; echo "probes rc=$?"; echo "# probes end $(date -u "+%FT%TZ")"' _ "$CENSUS" "$out" >> "$out/run.log" 2>&1
  fi
done
