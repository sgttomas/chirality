#!/bin/bash
# I101: the proposed N6(b) patch (not committed), applied in copy hs: RS's carrier test and TS's carrier integration test.
WT=WT
S=$WT/scratch/i101_b1_sc_pins
J=$S/harness/job.sh
P=$S/copies/hs/projects/chirality-piping
RUST_TEST_THREADS=4 $J cargo n6b_rs_carriers "$P/core/reporting/result_export" "$WT/targets/i101-b1-sc-pins/hs" test --locked --offline --test retained_precision_carriers
echo "rs carriers rc=$?"
$J slot n6b_ts_integration "$P/apps/desktop" "$P/node_modules/.bin/vitest" run src/features/results/retainedPrecisionIntegration.test.tsx
echo "ts integration rc=$?"
