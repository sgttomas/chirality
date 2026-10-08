#!/bin/bash
# I100: the suites at I4 and at the head, then I4's further probes; one slot job at a time.
S=WT/scratch/i100_b1_i4p_py
$S/tools/suites.sh i4 $S/i4/projects/chirality-piping
$S/tools/suites.sh head $S/head/projects/chirality-piping
source $S/tools/env.sh
$S/tools/job.sh slot verdicts_i4_x100 $S $VENV/bin/python $S/tools/rv113_py_harness.py $S/i4/projects/chirality-piping probes $S/inputs/probes_i100x.json $S/verdicts/i4/probes_i100x.jsonl; echo "i4 x100 rc=$?"
echo chain done
