#!/bin/bash
# RV113 (SR-TS repair 01): the heavy jobs, one at a time, each through WT/tools/t3_slot.sh.
WT=WT
S=$WT/scratch/rv113_rvr_01
J=$S/tools/rsr2_job.sh
NMS=NMS
DT=$WT/rv113/ts1-head/projects/chirality-piping/apps/desktop
T=$S/tsr1
# 1. TS at 6fa6a64658: the 07m census and the 391 probes, through the reviewer's harness.
$J slot ts1_harness $DT /usr/bin/env RV113_OUT=$T/census_ts1_head.jsonl RV113_PROBES=$T/probes/probes_ts1.json RV113_PROBES_OUT=$T/probes/ts1_head.jsonl $NMS/.bin/vitest run src/features/results/rv113Census.test.ts; echo "harness rc=$?"
rm -rf $DT/node_modules/.vite
# 2. RS at 6e3e4fe219 on the same 391 probes (the header set is new).
RE=$WT/rv113/rs2-head/projects/chirality-piping/core/reporting/result_export
$J slot rs2_probes_ts1 $RE /usr/bin/env RV113_PROBES=$T/probes/probes_ts1.json RV113_PROBES_OUT=$T/probes/rs2_head_ts1.jsonl RUST_TEST_THREADS=2 $WT/targets/rv113-rs2/debug/deps/rv113_census-2a7e1fb53dc907ac rv113_probes --exact; echo "rs rc=$?"
# 3. TS's whole vitest suite (JSON) and tsc.
$J slot ts1_vitest $DT $NMS/.bin/vitest run --reporter=dot --reporter=json --outputFile.json=$T/vitest_ts1_head.json; echo "vitest rc=$?"
rm -rf $DT/node_modules/.vite
$J slot ts1_tsc $DT $NMS/.bin/tsc --noEmit -p tsconfig.json; echo "tsc rc=$?"
echo done
