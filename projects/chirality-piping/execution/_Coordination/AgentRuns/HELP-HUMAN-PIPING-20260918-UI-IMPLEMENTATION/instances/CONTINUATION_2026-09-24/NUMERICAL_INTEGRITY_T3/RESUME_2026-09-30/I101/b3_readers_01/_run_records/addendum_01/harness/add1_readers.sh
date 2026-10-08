#!/bin/bash
# I101 addendum 01: the RS and TS readers' three readings of I100's 52 shapes (its add1_inputs.jsonl), in archive copies of
# the given commits, through scratch harnesses never committed (tools/i101_add1.rs, tools/i101Add1.test.ts).
# Usage: add1_readers.sh <label> <rs commit> <ts commit>
WT=WT
S=$WT/scratch/i101_b3r
J=$S/harness/job.sh
L=$1; O=$S/add1/out; mkdir -p $O
$S/harness/make_copy.sh b2-r "$2" add1_${L}_r s > $O/copy_${L}_r.txt && $S/harness/make_copy.sh b2-t "$3" add1_${L}_t s > $O/copy_${L}_t.txt || { echo "copies failed"; exit 1; }
RE=$S/copies/add1_${L}_r/projects/chirality-piping/core/reporting/result_export; DT=$S/copies/add1_${L}_t/projects/chirality-piping/apps/desktop
cp $S/tools/i101_add1.rs $RE/tests/i101_add1.rs; cp $S/tools/i101Add1.test.ts $DT/src/features/results/i101Add1.test.ts
ADD1_INPUTS=$S/add1/in/add1_inputs.jsonl ADD1_OUT=$O/${L}_rs.jsonl $J cargo add1_${L}_rs $RE $WT/targets/i101-b3r-r test --locked --offline --test i101_add1
echo "rs rc=$?"
$J slot add1_${L}_ts $DT /usr/bin/env ADD1_INPUTS=$S/add1/in/add1_inputs.jsonl ADD1_OUT=$O/${L}_ts.jsonl $S/copies/add1_${L}_t/projects/chirality-piping/node_modules/.bin/vitest run src/features/results/i101Add1.test.ts
echo "ts rc=$?"
