#!/bin/bash
# I105: assemble R/I105/b2_p_01/_run_records from scratch (placeholder paths only, via sanitize.py).
set -eu
WT=WT
S=$WT/scratch/i105_b2_p
R=$WT/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30/I105/b2_p_01
PY="$WT/venv/bin/python -I"
san() { mkdir -p "$(dirname "$2")"; $PY $S/bin/sanitize.py "$1" "$2"; }
RR=$R/_run_records
# scripts (current copies)
for f in run_suites.sh dev.sh compare.py sanitize.py mutants.py schema_check.py n11_py.py screen_files.py mut_summary.py records.sh; do san $S/bin/$f $RR/scripts/$f; done
# suites: logs per tag, meta, comparisons
for tag in base p1 head; do
  [ -d $S/runs/$tag ] || continue
  for f in $S/runs/$tag/*; do san $f $RR/suites/$tag/$(basename $f); done
done
for f in $S/runs/compare_*.json; do case $f in *partial*) continue;; esac; san $f $RR/suites/$(basename $f); done
# mutants: spec, results (no timing field), per-mutant filtered logs
san $S/mut_spec/p1.json $RR/mutants/p1.json
san $S/mut_spec/p1.py $RR/mutants/p1.py
san $S/runs/mutants_p1_results.json $RR/mutants/results.json
for d in mut_p1 mut_p1_rerun; do
  [ -d $S/runs/$d ] || continue
  for f in $S/runs/$d/*.log; do san $f $RR/mutants/logs_${d#mut_}/$(basename $f); done
done
# pins, schema, n11, proposal, commits
san $S/rec/pins.txt $RR/pins.txt
san $S/runs/schema_check.log $RR/schema_check.log
san $S/rec/commits.txt $RR/commits.txt
san $S/rec/diffstat.txt $RR/diffstat.txt
