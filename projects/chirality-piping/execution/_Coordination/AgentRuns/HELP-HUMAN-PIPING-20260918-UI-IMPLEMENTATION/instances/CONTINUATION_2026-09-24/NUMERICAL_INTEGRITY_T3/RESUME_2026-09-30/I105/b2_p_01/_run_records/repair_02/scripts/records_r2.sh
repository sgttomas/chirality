#!/bin/bash
# I105 B2-P repair 02: R/I105/b2_p_01/REPAIR_02.md and _run_records/repair_02 (placeholder paths only), then
# SHA256SUMS over the whole folder and the record screen. Usage: records_r2.sh <filled REPAIR_02 markdown>
set -eu
WT=WT
S=$WT/scratch/i105_b2_p
R=$WT/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30/I105/b2_p_01
PY="$WT/venv/bin/python -I"
san() { mkdir -p "$(dirname "$2")"; $PY $S/bin/sanitize.py "$1" "$2"; }
RR=$R/_run_records/repair_02
san $S/mut_spec/r2.json $RR/mutants/r2.json
[ -f $S/runs/mut_r2/results.json ] && $PY $S/bin/mut_summary.py $S/runs/mut_r2/results.json $S/runs/mutants_r2_results.json > /dev/null && san $S/runs/mutants_r2_results.json $RR/mutants/results.json
for f in $S/runs/mut_r2/*.log; do [ -f "$f" ] && san $f $RR/mutants/logs/$(basename $f); done
for tag in r2base r2head; do
  [ -d $S/runs/$tag ] || continue
  for f in $S/runs/$tag/*; do san $f $RR/suites/$tag/$(basename $f); done
done
[ -f $S/runs/compare_r2.json ] && san $S/runs/compare_r2.json $RR/suites/compare_r2.json
[ -f $S/rec/r2_tests.txt ] && san $S/rec/r2_tests.txt $RR/r2_tests.txt
for f in chain_r2.sh records_r2.sh mutants.py; do san $S/bin/$f $RR/scripts/$f; done
san "$1" $R/REPAIR_02.md
(cd $R && find . -type f ! -name SHA256SUMS | sed 's#^\./##' | LC_ALL=C sort | while IFS= read -r f; do shasum -a 256 "$f"; done > SHA256SUMS)
find $R -type l | sed 's#.*#SYMLINK &#'
find $R -type d -name build | sed 's#.*#BUILD-DIR &#'
$PY $S/bin/screen_files.py $R
