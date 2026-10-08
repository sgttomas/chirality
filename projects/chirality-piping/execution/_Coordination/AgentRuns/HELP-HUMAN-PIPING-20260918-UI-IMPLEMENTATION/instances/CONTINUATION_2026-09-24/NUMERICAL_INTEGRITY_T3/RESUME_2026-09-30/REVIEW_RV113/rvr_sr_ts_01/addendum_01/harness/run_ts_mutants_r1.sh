#!/bin/bash
# RV113: SR-TS repair 01's TS mutant schema, one t3_slot vitest job per mutant (RV113_MUT=<id>; NONE = the control).
# Usage: run_ts_mutants_r1.sh <tests|probes> <ids...>
#   tests:  the seven test files that import the TS reader (vitest JSON report per mutant)
#   probes: the reviewer's probe harness (probes_ts1.json)
WT=WT
S=$WT/scratch/rv113_rvr_01/tsr1
NMS=NMS
D=$WT/rv113/ts1-mut/projects/chirality-piping/apps/desktop
FILES="src/features/results/retainedPrecision.test.ts src/features/results/retainedPrecisionIntegration.test.tsx src/features/results/retainedPrecisionOutputRefusal.test.tsx src/features/results/outputPolicy.test.ts src/features/result-export/retainedPrecisionResultExport.test.tsx src/features/stress-neutral/retainedPrecisionStressNeutral.test.tsx src/services/retainedPrecisionAnalysisRun.test.ts"
mode=$1; shift
for id in "$@"; do
  out=$S/mutants/runs/$id; mkdir -p "$out" "$S/tmp/mut_$id"
  mut=$([ "$id" = NONE ] || echo "$id")
  cd "$D" || exit 90
  if [ "$mode" = tests ]; then
    echo "# $id tests queued $(date -u '+%FT%TZ')" > "$out/run.log"
    "$WT/tools/t3_slot.sh" /usr/bin/env RV113_MUT="$mut" TMPDIR="$S/tmp/mut_$id" /bin/bash -c '
      echo "# start $(date -u "+%FT%TZ") RV113_MUT=${RV113_MUT:-unset}"
      "$1" run $2 --reporter=dot --reporter=json --outputFile.json="$3/vitest.json" > "$3/vitest.log" 2>&1; echo "vitest rc=$?"
      echo "# end $(date -u "+%FT%TZ")"' _ "$NMS/.bin/vitest" "$FILES" "$out" >> "$out/run.log" 2>&1
  else
    echo "# $id probes queued $(date -u '+%FT%TZ')" >> "$out/run.log"
    "$WT/tools/t3_slot.sh" /usr/bin/env RV113_MUT="$mut" TMPDIR="$S/tmp/mut_$id" RV113_PROBES="$S/probes/probes_ts1.json" RV113_PROBES_OUT="$out/probes.jsonl" /bin/bash -c '
      echo "# probes start $(date -u "+%FT%TZ")"; "$1" run src/features/results/rv113Census.test.ts > "$2/harness.log" 2>&1; echo "probes rc=$?"; echo "# probes end $(date -u "+%FT%TZ")"' _ "$NMS/.bin/vitest" "$out" >> "$out/run.log" 2>&1
  fi
  rm -rf "$D/node_modules/.vite"
done
