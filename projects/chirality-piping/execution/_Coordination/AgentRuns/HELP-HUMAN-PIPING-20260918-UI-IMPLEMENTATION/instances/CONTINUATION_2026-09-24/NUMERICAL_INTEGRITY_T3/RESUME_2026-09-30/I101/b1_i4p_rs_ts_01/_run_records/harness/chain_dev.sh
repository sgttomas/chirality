#!/bin/bash
# I101: quick development runs of the new tests in S/copies/dev (I4 with the working files overlaid), one job at a time.
WT=WT
S=$WT/scratch/i101_b1_i4p_rs_ts
J=$S/harness/job.sh
P=$S/copies/dev/projects/chirality-piping
n=$1
RUST_TEST_THREADS=4 $J cargo dev${n}_re "$P/core/reporting/result_export" "$WT/targets/i101-b1-i4p-rs-ts/dev-re" test --locked --offline --test retained_precision_contract b1_i4p
echo "re rc=$?"
$J slot dev${n}_ts "$P/apps/desktop" "$P/node_modules/.bin/vitest" run src/features/results/previewPhysicsEvidence.test.ts src/features/results/retainedPrecision.test.ts
echo "ts rc=$?"
$J slot dev${n}_tsc "$P/apps/desktop" "$P/node_modules/.bin/tsc" --noEmit -p tsconfig.json
echo "tsc rc=$?"
