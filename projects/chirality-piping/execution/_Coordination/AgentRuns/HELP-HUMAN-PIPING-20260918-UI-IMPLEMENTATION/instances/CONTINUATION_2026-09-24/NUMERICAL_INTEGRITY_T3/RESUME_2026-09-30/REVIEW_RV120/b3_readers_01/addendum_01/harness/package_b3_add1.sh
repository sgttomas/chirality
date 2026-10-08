#!/bin/bash
# RV120 (B3 repair 01): the addendum's evidence into R/REVIEW_RV120/b3_readers_01/addendum_01/ (placeholder paths;
# junit host attribute removed; large outputs gzipped).
set -e
WT=WT
S=$WT/scratch/rv120_rvr
B3=$S/b3
OUT=$WT/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30/REVIEW_RV120/b3_readers_01/addendum_01
SAN="python3 -I $S/tools/sanitize.py"
rm -rf $OUT; mkdir -p $OUT/{harness,readers,suites,census,host}
for f in b3/run_b3_r1.sh b3/run_b3_probes2.sh b3/py_bind_mutants.sh b3/rs_det.sh b3/package_b3_add1.sh; do $SAN $S/tools/$f $OUT/harness/$(basename $f); done
for set in r1probes r1forge r1s169 r1s52 r1s318; do for r in rs ts py; do $SAN $B3/probes/${set}_$r.jsonl $OUT/readers/${set}_$r.jsonl.gz; done; cp $B3/probes/cmp_$set.json $OUT/readers/; done
for m in R2 R3 R4 R5; do $SAN $B3/probes/r1forge_py_$m.jsonl $OUT/readers/r1forge_py_$m.jsonl; done
for i in 1 2 3 4 5; do $SAN $B3/probes/rs_det_$i.jsonl $OUT/readers/rs_det_$i.jsonl; done
cp $B3/cmp_r1/*.json $OUT/suites/
for f in ts2_re_suite ts2_tsc mut2_B28_rs mut2_B29_rs; do $SAN $B3/logs/$f.log $OUT/suites/$f.log.gz; done
for f in vitest_ts2 mut2_B28_ts mut2_B29_ts; do $SAN $B3/suites/$f.json $OUT/suites/$f.json.gz; done
for f in py_ts2 py_py2; do $SAN $B3/suites/$f.xml $OUT/suites/$f.xml.gz; done
for f in rs_ts2 ts_ts2 py_py2 rs_ts2_07n ts_ts2_07n py_py2_07n; do $SAN $B3/census/$f.jsonl $OUT/census/$f.jsonl.gz; done
mv $OUT/suites/census_*.json $OUT/census/ 2>/dev/null || true
{ echo "# RV120 B3 repair 01 jobs: each job log's own stamp lines"; for f in $B3/logs/ts2_*.log $B3/logs/py2*.log $B3/logs/n07_*2*.log $B3/logs/r1*.log $B3/logs/mut2_*.log $B3/logs/py2m_*.log $B3/logs/rs_det_*.log; do [ -f $f ] && { echo "== $(basename $f)"; grep -E "^# " $f; }; done; } > $B3/logs/job_stamps_r1.txt
$SAN $B3/logs/job_stamps_r1.txt $OUT/host/job_stamps.txt
echo packaged-add1
