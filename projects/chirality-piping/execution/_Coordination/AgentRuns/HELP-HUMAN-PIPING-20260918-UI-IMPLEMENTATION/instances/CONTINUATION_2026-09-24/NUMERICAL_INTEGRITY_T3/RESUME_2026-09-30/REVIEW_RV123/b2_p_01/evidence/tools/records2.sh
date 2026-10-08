#!/bin/bash
# RV123 round 2: assemble the records (placeholder paths only; no symlink; no folder named build).
WT=WT
S2=$WT/scratch/rv123_rvp2/r2
R=$WT/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30/REVIEW_RV123/b2_p_01
PY=$WT/venv/bin/python
rm -rf $R/evidence; mkdir -p $R/evidence/logs $R/evidence/tools $R/evidence/results
for f in $S2/logs/*.log; do $PY -I $S2/tools/logfilter.py "$f" > $S2/tmp/filtered.txt; $PY -I $S2/tools/sanitize2.py $S2/tmp/filtered.txt "$R/evidence/logs/$(basename $f .log).txt"; done
for f in $S2/logs/*.out $S2/logs/chain.log; do $PY -I $S2/tools/sanitize2.py "$f" "$R/evidence/logs/$(basename $f).txt"; done
for f in $S2/logs/*.rc; do printf '%s %s\n' "$(basename $f .rc)" "$(cat $f)"; done > $S2/tmp/rcs.txt; $PY -I $S2/tools/sanitize2.py $S2/tmp/rcs.txt $R/evidence/logs/exit_codes.txt
for f in $S2/tools/*; do $PY -I $S2/tools/sanitize2.py "$f" "$R/evidence/tools/$(basename $f)"; done
for f in $S2/results/*; do $PY -I $S2/tools/sanitize2.py "$f" "$R/evidence/results/$(basename $f)"; done
$PY -I $S2/tools/sanitize2.py $S2/tmp/jobs_r2.txt $R/evidence/cargo_jobs_rv123_r2.txt
