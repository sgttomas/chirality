#!/bin/bash
# I101 (07n pins): development runs of the changed test files in S/copies/dev (SC's head with the working files laid over it).
WT=WT
S=$WT/scratch/i101_b1_sc_pins
J=$S/harness/job.sh
P=$S/copies/dev/projects/chirality-piping
n=$1
RUST_TEST_THREADS=4 $J cargo dev${n}_rt "$P/core/reporting/result_export" "$WT/targets/i101-b1-sc-pins/dev" test --locked --offline --test retained_precision_contract
echo "rt rc=$?"
$J slot dev${n}_ts "$P/apps/desktop" "$P/node_modules/.bin/vitest" run src/features/results/retainedPrecision.test.ts --reporter=dot --reporter=json --outputFile.json="$S/out/dev${n}_ts.json"
echo "ts rc=$?"
$J slot dev${n}_tsc "$P/apps/desktop" "$P/node_modules/.bin/tsc" --noEmit -p tsconfig.json
echo "tsc rc=$?"
