#!/bin/bash
# I100 B3: the control and B40 on the mutant copy (its B3 test file at the final head), then the shapes at the final head.
source WT/scratch/i100_b3r/tools/env.sh
$S/tools/run_mutants.sh NONE B40
$S/tools/job.sh slot shapes $S $VENV/bin/python $S/tools/b3_shapes.py $S/head2/projects/chirality-piping $S/shapes/b3_shapes.json $S/shapes/py_b3_shapes.jsonl
echo "shapes rc=$?"
