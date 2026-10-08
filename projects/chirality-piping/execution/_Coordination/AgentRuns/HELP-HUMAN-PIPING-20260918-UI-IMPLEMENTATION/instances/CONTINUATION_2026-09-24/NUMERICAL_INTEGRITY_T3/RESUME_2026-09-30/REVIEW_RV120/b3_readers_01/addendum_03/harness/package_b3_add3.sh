#!/bin/bash
# RV120 (B3 ADDENDUM_03): the evidence into R/REVIEW_RV120/b3_readers_01/addendum_03/ (placeholder paths; junit host
# attribute removed; large outputs gzipped).
set -e
W=WT; S=$W/scratch/rv120_rvr; B3=$S/b3
OUT=$W/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30/REVIEW_RV120/b3_readers_01/addendum_03
SAN="python3 -I $S/tools/sanitize.py"
rm -rf $OUT; mkdir -p $OUT/{harness,readers,suites,census,host}
for f in b3/run_b3_a3.sh b3/run_b3_probes2.sh b3/package_b3_add3.sh; do $SAN $S/tools/$f $OUT/harness/$(basename $f); done
for d in tsrs py; do $SAN $B3/a3/repair0203_$d.diff $OUT/harness/repair02_$d.diff; done
for set in a3probes a3forge a3s a3s52 a3s318; do for r in rs ts py; do $SAN $B3/probes/${set}_$r.jsonl $OUT/readers/${set}_$r.jsonl.gz; done; cp $B3/probes/cmp_$set.json $OUT/readers/; done
for i in 1 2 3 4 5; do $SAN $B3/probes/a3_rs_det_$i.jsonl $OUT/readers/a3_rs_det_$i.jsonl; done
for f in a3all_rs_1 a3all_rs_2 a3all_py_1 a3all_py_2; do $SAN $B3/probes/$f.jsonl $OUT/readers/$f.jsonl.gz; done
cp $B3/cmp_a3/*.json $OUT/suites/; mv $OUT/suites/census_*.json $OUT/census/; mv $OUT/suites/MOVED_SINCE_ADDENDUM_02.json $OUT/readers/
for f in m2_re_suite m2_tsc; do $SAN $B3/logs/$f.log $OUT/suites/$f.log.gz; done
$SAN $B3/suites/vitest_m2.json $OUT/suites/vitest_m2.json.gz
for f in py_m2; do $SAN $B3/suites/$f.xml $OUT/suites/$f.xml.gz; done
for f in rs_m2 ts_m2 py_m2 rs_m2_07n ts_m2_07n py_m2_07n; do $SAN $B3/census/$f.jsonl $OUT/census/$f.jsonl.gz; done
{ echo "# RV120 B3 ADDENDUM_03 jobs: each job log's own stamp lines"; for f in $B3/logs/m2_*.log $B3/logs/n07_*_m2.log $B3/logs/a3*.log; do [ -f $f ] && { echo "== $(basename $f)"; grep -E "^# " $f; }; done; } > $B3/logs/job_stamps_a3.txt
$SAN $B3/logs/job_stamps_a3.txt $OUT/host/job_stamps.txt
echo packaged-add3
