#!/bin/bash
# I101: the mutant runs, one heavy job at a time. RS: one cargo build of the mutant copy (t3_cargo.sh), then per
# mutant RE's lib unit-test binary and its contract-test binary as one t3_slot job (RV113_MUT=<id>; NONE = control).
# TS: per mutant the two test files as one t3_slot vitest job with a JSON report (I101_MUT=<id>; NONE = control).
WT=WT
S=$WT/scratch/i101_b1_i4p_rs_ts
J=$S/harness/job.sh
RE=$S/copies/rsm/projects/chirality-piping/core/reporting/result_export
DT=$S/copies/tsm/projects/chirality-piping/apps/desktop
T=$WT/targets/i101-b1-i4p-rs-ts/rsm
$J cargo mut_rs_build "$RE" "$T" test --locked --offline --no-run
echo "rs build rc=$?"
D=$T/debug/deps
bin() { echo "$D/$(ls "$D" | grep -E "^$1-[0-9a-f]+\$" | head -1)"; }
LIB=$(bin open_pipe_stress_result_export); CONTRACT=$(bin retained_precision_contract)
ids=(NONE $(python3 -I -c "import json;print(' '.join(m['id'] for m in json.load(open('$S/mutants/MUTANTS_RS.json'))))"))
for id in "${ids[@]}"; do
  out=$S/mutants/runs/$id; mkdir -p "$out" "$S/tmp/mut_$id"
  mut=$([ "$id" = NONE ] || echo "$id")
  cd "$RE" || exit 90
  echo "# $id tests queued $(date -u '+%FT%TZ')" > "$out/run.log"
  "$WT/tools/t3_slot.sh" /usr/bin/env RV113_MUT="$mut" TMPDIR="$S/tmp/mut_$id" RUST_TEST_THREADS=2 /bin/bash -c '
    echo "# start $(date -u "+%FT%TZ") RV113_MUT=${RV113_MUT:-unset}"
    "$1" > "$3/lib.log" 2>&1; echo "lib rc=$?"
    "$2" > "$3/contract.log" 2>&1; echo "contract rc=$?"
    echo "# end $(date -u "+%FT%TZ")"' _ "$LIB" "$CONTRACT" "$out" >> "$out/run.log" 2>&1
done
echo "rs mutants done"
FILES="src/features/results/previewPhysicsEvidence.test.ts src/features/results/retainedPrecision.test.ts"
for id in NONE Y01 Y02; do
  out=$S/mutants/runs/$id; mkdir -p "$out" "$S/tmp/mut_$id"
  mut=$([ "$id" = NONE ] || echo "$id")
  cd "$DT" || exit 90
  echo "# $id vitest queued $(date -u '+%FT%TZ')" >> "$out/run.log"
  "$WT/tools/t3_slot.sh" /usr/bin/env I101_MUT="$mut" TMPDIR="$S/tmp/mut_$id" /bin/bash -c '
    echo "# vitest start $(date -u "+%FT%TZ") I101_MUT=${I101_MUT:-unset}"
    "$1" run $2 --reporter=dot --reporter=json --outputFile.json="$3/vitest.json" > "$3/vitest.log" 2>&1; echo "vitest rc=$?"
    echo "# vitest end $(date -u "+%FT%TZ")"' _ "$DT/../../node_modules/.bin/vitest" "$FILES" "$out" >> "$out/run.log" 2>&1
done
echo "ts mutants done"
