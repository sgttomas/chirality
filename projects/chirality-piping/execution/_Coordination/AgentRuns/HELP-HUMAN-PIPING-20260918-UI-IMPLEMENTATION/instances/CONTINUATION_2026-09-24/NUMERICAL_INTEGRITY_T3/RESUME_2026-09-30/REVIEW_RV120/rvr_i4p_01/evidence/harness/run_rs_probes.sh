#!/bin/bash
# RV120: the reviewer harness's probe test alone (rv113_probes) on RS at I4 and at the head, one slot job each.
WT=WT
S=$WT/scratch/rv120_rvr
J=$S/tools/rv120_job.sh
REL=projects/chirality-piping/core/reporting/result_export
bin() { local D=$1/debug/deps; echo "$D/$(ls "$D" | grep -E "^$2-[0-9a-f]+\$" | head -1)"; }
for c in i4 head; do
  B=$(bin $WT/targets/rv120-rs-$c rv113_census)
  $J slot rs_${c}_probes $S/copies/rs-$c/$REL /usr/bin/env RV113_PROBES=$S/probes/probes_rv120_all.json RV113_PROBES_OUT=$S/probes/rs_${c}.jsonl RUST_TEST_THREADS=2 "$B" rv113_probes --exact; echo "rs_${c}_probes rc=$?"
done
echo rs-probes-done
