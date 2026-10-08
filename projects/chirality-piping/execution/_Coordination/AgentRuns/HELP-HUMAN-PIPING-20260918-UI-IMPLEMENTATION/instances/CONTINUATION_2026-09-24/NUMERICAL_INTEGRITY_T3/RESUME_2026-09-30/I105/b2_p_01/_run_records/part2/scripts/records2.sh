#!/bin/bash
# I105 Part 2: assemble R/I105/b2_p_01/_run_records/part2 from scratch (placeholder paths only, via sanitize.py).
set -eu
WT=WT
S=$WT/scratch/i105_b2_p
R=$WT/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30/I105/b2_p_01
PY="$WT/venv/bin/python -I"
san() { mkdir -p "$(dirname "$2")"; $PY $S/bin/sanitize.py "$1" "$2"; }
RR=$R/_run_records/part2
for f in run_suites.sh dev.sh compare.py sanitize.py mutants.py schema_check.py screen_files.py mut_summary.py records2.sh; do san $S/bin/$f $RR/scripts/$f; done
san $S/mut_spec/p2.py $RR/mutants/p2.py
[ -f $S/mut_spec/p2.json ] && san $S/mut_spec/p2.json $RR/mutants/p2.json
[ -f $S/runs/mutants_p2_results.json ] && san $S/runs/mutants_p2_results.json $RR/mutants/results.json
[ -f $S/runs/mutants_p2_results_first.json ] && san $S/runs/mutants_p2_results_first.json $RR/mutants/results_first_run.json
[ -f $S/runs/mutants_p2_results_rerun.json ] && san $S/runs/mutants_p2_results_rerun.json $RR/mutants/results_rerun.json
for d in mut_p2 mut_p2_rerun; do
  [ -d $S/runs/$d ] || continue
  for f in $S/runs/$d/*.log; do san $f $RR/mutants/logs_${d#mut_}/$(basename $f); done
done
san $S/mut_spec/rv123.json $RR/rv123/mutants.json
[ -f $S/runs/mutants_rv123_results.json ] && san $S/runs/mutants_rv123_results.json $RR/rv123/results.json
for f in $S/runs/mut_rv123/*.log; do san $f $RR/rv123/logs/$(basename $f); done
for tag in oracle oracle2 p2head; do
  [ -d $S/runs/$tag ] || continue
  for f in $S/runs/$tag/*; do san $f $RR/suites/$tag/$(basename $f); done
done
for f in $S/runs/compare_oracle.json $S/runs/compare_oracle2.json $S/runs/compare_p2head.json; do [ -f $f ] && san $f $RR/suites/$(basename $f); done
[ -f $S/proposal2/lane_a_b2_admitted_combinations.diff ] && san $S/proposal2/lane_a_b2_admitted_combinations.diff $RR/proposal/lane_a_b2_admitted_combinations.diff
[ -f $S/runs/propcheck2.filtered.log ] && san $S/runs/propcheck2.filtered.log $RR/proposal/propcheck2_law_tests.log
[ -f $S/runs/schema_check_p2.log ] && san $S/runs/schema_check_p2.log $RR/schema_check.log
[ -f $S/rec/pins2.txt ] && san $S/rec/pins2.txt $RR/pins.txt
[ -f $S/rec/commits2.txt ] && san $S/rec/commits2.txt $RR/commits.txt
[ -f $S/rec/inputs_check.txt ] && san $S/rec/inputs_check.txt $RR/inputs_check.txt
[ -f $S/rec/merge_check.txt ] && san $S/rec/merge_check.txt $RR/lane_a_merge_check.txt
[ -f $S/runs/schema_check_p2_hooks.log ] && san $S/runs/schema_check_p2_hooks.log $RR/schema_check_hooks.log
[ -f $S/rec/b2p_tests.txt ] && san $S/rec/b2p_tests.txt $RR/b2p_tests.txt
[ -f $S/runs/na45.log ] && san $S/runs/na45.log $RR/na45.log
[ -f $S/runs/readers_py.log ] && san $S/runs/readers_py.log $RR/readers_py.log
[ -f $S/rec/rv125.txt ] && san $S/rec/rv125.txt $RR/rv125.txt
[ -f $S/rec/lane_a_applied_check.txt ] && san $S/rec/lane_a_applied_check.txt $RR/lane_a_applied_check.txt
for f in na45_ulps.py readers_today_py.py chain_p2.sh chain_p2b.sh rederive.py finalize_records.sh py_reader_job.sh; do [ -f $S/bin/$f ] && san $S/bin/$f $RR/scripts/$f; done
true
