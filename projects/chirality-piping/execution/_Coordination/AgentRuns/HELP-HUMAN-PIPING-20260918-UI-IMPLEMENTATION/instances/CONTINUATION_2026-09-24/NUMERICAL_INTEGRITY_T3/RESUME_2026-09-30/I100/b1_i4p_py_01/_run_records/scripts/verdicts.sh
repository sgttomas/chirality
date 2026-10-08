#!/bin/bash
# I100: RV113's PY harness (as published) over 07m (census), RV113's probes (probes_ts1, 392; probes_r2x, 2) and
# I100's four further probes (probes_i100x), on one P tree, as one T3 slot job. Usage: verdicts.sh <label> <P root>
set -u
source WT/scratch/i100_b1_i4p_py/tools/env.sh
LABEL=$1; P=$2; O=$S/verdicts/$LABEL; mkdir -p $O
$S/tools/job.sh slot verdicts_$LABEL $S /bin/bash -c "
$VENV/bin/python $S/tools/rv113_py_harness.py $P census $O/census.jsonl &&
$VENV/bin/python $S/tools/rv113_py_harness.py $P probes $S/inputs/probes_ts1.json $O/probes_ts1.jsonl &&
$VENV/bin/python $S/tools/rv113_py_harness.py $P probes $S/inputs/probes_r2x.json $O/probes_r2x.jsonl &&
$VENV/bin/python $S/tools/rv113_py_harness.py $P probes $S/inputs/probes_i100x.json $O/probes_i100x.jsonl"
echo "rc=$?"
