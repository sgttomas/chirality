#!/bin/bash
# RV120: RS's heavy jobs, one at a time: RE's whole suite at I4 and at the head (cargo, which builds), the reviewer
# harness (07m census and the 437 probes) on each, then the mutant copy's test build.
WT=WT
S=$WT/scratch/rv120_rvr
J=$S/tools/rv120_job.sh
REL=projects/chirality-piping/core/reporting/result_export
bin() { local D=$1/debug/deps; echo "$D/$(ls "$D" | grep -E "^$2-[0-9a-f]+\$" | head -1)"; }
for c in i4 head; do
  $J cargo rs_${c}_suite $S/copies/rs-$c/$REL $WT/targets/rv120-rs-$c test --locked --offline; echo "rs_${c}_suite rc=$?"
done
for c in i4 head; do
  B=$(bin $WT/targets/rv120-rs-$c rv113_census)
  $J slot rs_${c}_harness $S/copies/rs-$c/$REL /usr/bin/env RV113_OUT=$S/census/rs_${c}.jsonl RV113_PROBES=$S/probes/probes_rv120_all.json RV113_PROBES_OUT=$S/probes/rs_${c}.jsonl RUST_TEST_THREADS=2 "$B"; echo "rs_${c}_harness rc=$?"
done
$J cargo rs_mut_build $S/copies/rs-mut/$REL $WT/targets/rv120-rs-mut test --locked --offline --no-run; echo "rs_mut_build rc=$?"
echo rs-chain-done
