#!/bin/bash
# RV123: assemble the records (placeholder paths only; no symlink; no folder named build).
WT=WT
S=$WT/scratch/rv123_rvp2
R=$WT/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30/REVIEW_RV123/b3b_p_01
PY=$WT/venv/bin/python
rm -rf $R/evidence; mkdir -p $R/evidence/logs $R/evidence/tools $R/evidence/results
for f in $S/logs/*.log; do $PY -I $S/tools/logfilter.py "$f" > $S/tmp/filtered.txt; $PY -I $S/tools/sanitize.py $S/tmp/filtered.txt "$R/evidence/logs/$(basename $f .log).txt"; done
for f in $S/tools/*; do $PY -I $S/tools/sanitize.py "$f" "$R/evidence/tools/$(basename $f)"; done
for f in $S/results/*; do $PY -I $S/tools/sanitize.py "$f" "$R/evidence/results/$(basename $f)"; done
grep 'rv123' $WT/guard/cargo_jobs.log > $S/tmp/jobs.txt; $PY -I $S/tools/sanitize.py $S/tmp/jobs.txt $R/evidence/cargo_jobs_rv123.txt
