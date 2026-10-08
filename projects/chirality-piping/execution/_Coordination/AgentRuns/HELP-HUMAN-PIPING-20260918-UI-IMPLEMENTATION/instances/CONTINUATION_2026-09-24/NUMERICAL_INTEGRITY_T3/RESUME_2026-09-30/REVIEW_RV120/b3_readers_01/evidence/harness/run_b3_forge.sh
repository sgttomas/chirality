#!/bin/bash
# RV120 B3: the forged E/G-hat inputs on the unmutated readers (probe copy; PY head), then on I101's B28 and B29 mutants
# (RS and TS, in the reviewer's mutant copy), one heavy job at a time.
WT=WT
S=$WT/scratch/rv120_rvr
B3=$S/b3
export RV120_LOGDIR=$B3/logs
J=$S/tools/rv120_job.sh
IN=$B3/inputs/forge_eg.jsonl
$S/tools/b3/run_b3_probes.sh forge $IN
P=$WT/rv120b3/mut/projects/chirality-piping; O=$WT/rv120b3/mut.orig/projects/chirality-piping
for m in B28 B29; do
  python3 $S/tools/b3/mutate_b3.py $P $O $m apply
  env RV120_IN=$IN RV120_OUT=$B3/probes/forge_${m}_rs.jsonl $J cargo forge_${m}_rs $P/core/reporting/result_export $WT/targets/rv120b3-mut test --locked --offline --test rv120_b3_raw; echo "forge_${m}_rs rc=$?"
  $J slot forge_${m}_ts $P/apps/desktop /usr/bin/env RV120_IN=$IN RV120_OUT=$B3/probes/forge_${m}_ts.jsonl $P/node_modules/.bin/vitest run src/features/results/rv120B3Raw.test.ts; echo "forge_${m}_ts rc=$?"
  rm -rf $P/apps/desktop/node_modules/.vite
  python3 $S/tools/b3/mutate_b3.py $P $O $m revert
done
cmp $P/core/reporting/result_export/src/retained_precision.rs $O/core/reporting/result_export/src/retained_precision.rs && cmp $P/apps/desktop/src/features/results/retainedPrecision.ts $O/apps/desktop/src/features/results/retainedPrecision.ts && echo reverted
echo forge-done
