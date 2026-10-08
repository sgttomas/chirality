#!/bin/bash
# I101: at the two heads, one heavy job at a time: the census and probes (RS at b1-r's head, TS at b1-t's head),
# RE's suite (b1-r), the desktop vitest suite and tsc (b1-t), and the contract test at RS's first commit.
WT=WT
S=$WT/scratch/i101_b1_i4p_rs_ts
J=$S/harness/job.sh
$S/harness/chain_census.sh head rsh tsh
$S/harness/chain_suites.sh head_rs rss rs
$S/harness/chain_suites.sh head_ts tss ts
P=$S/copies/rsi/projects/chirality-piping
RUST_TEST_THREADS=4 $J cargo rsi_contract "$P/core/reporting/result_export" "$WT/targets/i101-b1-i4p-rs-ts/rsi" test --locked --offline --test retained_precision_contract
echo "rsi rc=$?"
