#!/bin/bash
# RV120: TS's heavy jobs, one at a time, each through WT/tools/t3_slot.sh: the reviewer harness (07m census and the
# 437 probes) at I4 and the head; the whole vitest suite (JSON) at I4 and the head; tsc at the head; then the mutant
# copy's control and my mutants (whole suite each), and the control's probe run.
WT=WT
S=$WT/scratch/rv120_rvr
J=$S/tools/rv120_job.sh
D() { echo $S/copies/$1/projects/chirality-piping/apps/desktop; }
VT() { echo $S/copies/$1/projects/chirality-piping/node_modules/.bin/vitest; }
for c in i4 head; do
  $J slot ts_${c}_harness $(D ts-$c) /usr/bin/env RV113_OUT=$S/census/ts_${c}.jsonl RV113_PROBES=$S/probes/probes_rv120_all.json RV113_PROBES_OUT=$S/probes/ts_${c}.jsonl $(VT ts-$c) run src/features/results/rv113Census.test.ts; echo "ts_${c}_harness rc=$?"
  rm -rf $(D ts-$c)/node_modules/.vite
done
for c in i4 head; do
  $J slot ts_${c}_vitest $(D ts-$c) $(VT ts-$c) run --reporter=dot --reporter=json --outputFile.json=$S/suites/vitest_ts_${c}.json; echo "ts_${c}_vitest rc=$?"
  rm -rf $(D ts-$c)/node_modules/.vite
done
$J slot ts_head_tsc $(D ts-head) $S/copies/ts-head/projects/chirality-piping/node_modules/.bin/tsc --noEmit -p tsconfig.json; echo "ts_head_tsc rc=$?"
for id in NONE W01 W02 W03 W04 W05 W06 W07 W08 W10; do
  mut=$([ "$id" = NONE ] || echo "$id"); mkdir -p $S/mutants/ts_runs/$id
  $J slot ts_mut_$id $(D ts-mut) /usr/bin/env RV120_MUT="$mut" $(VT ts-mut) run --reporter=dot --reporter=json --outputFile.json=$S/mutants/ts_runs/$id/vitest.json; echo "ts_mut_$id rc=$?"
  rm -rf $(D ts-mut)/node_modules/.vite
done
$J slot ts_mut_NONE_probes $(D ts-mut) /usr/bin/env RV113_PROBES=$S/probes/probes_rv120_all.json RV113_PROBES_OUT=$S/mutants/ts_runs/NONE/probes.jsonl $(VT ts-mut) run src/features/results/rv113Census.test.ts; echo "ts_mut_NONE_probes rc=$?"
rm -rf $(D ts-mut)/node_modules/.vite
echo ts-chain-done
