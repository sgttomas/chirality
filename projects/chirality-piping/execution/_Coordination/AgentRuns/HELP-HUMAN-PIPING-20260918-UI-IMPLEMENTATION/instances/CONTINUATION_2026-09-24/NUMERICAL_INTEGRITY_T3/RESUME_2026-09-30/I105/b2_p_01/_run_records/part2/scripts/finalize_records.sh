#!/bin/bash
# I105 Part 2: run records2.sh, append Part 2 to RETURN.md (Part 1's text unchanged), refresh SHA256SUMS,
# then screen the records. Usage: finalize_records.sh <filled RETURN2 markdown>
set -eu
WT=WT
S=$WT/scratch/i105_b2_p
R=$WT/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30/I105/b2_p_01
bash $S/bin/records2.sh
PART1=$(git -C $WT/numerics show HEAD:projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30/I105/b2_p_01/RETURN.md)
{ printf '%s\n' "$PART1"; cat "$1"; } > $S/tmp/RETURN_full.md
$WT/venv/bin/python -I $S/bin/sanitize.py $S/tmp/RETURN_full.md $R/RETURN.md
(cd $R && find . -type f ! -name SHA256SUMS | sed 's#^\./##' | LC_ALL=C sort | while IFS= read -r f; do shasum -a 256 "$f"; done > SHA256SUMS)
find $R -type l | sed 's#.*#SYMLINK &#'
find $R -type d -name build | sed 's#.*#BUILD-DIR &#'
$WT/venv/bin/python -I $S/bin/screen_files.py $R
