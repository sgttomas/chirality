#!/bin/bash
# I100 B3: at the final head (archive given): the control, B31 and B40 on the mutant copy with that head's B3 test
# file; the shapes (and their inputs in I101's format); PY on I101's RS inputs. Usage: chain_final2.sh <archive dir>
source WT/scratch/i100_b3r/tools/env.sh
A=$1
cp $A/projects/chirality-piping/tests/test_retained_precision_b3.py $S/mut/projects/chirality-piping/tests/test_retained_precision_b3.py
$S/tools/run_mutants.sh NONE B31 B40
$S/tools/job.sh slot shapes $S $VENV/bin/python $S/tools/b3_shapes.py $A/projects/chirality-piping $S/shapes/b3_shapes.json $S/shapes/py_b3_shapes.jsonl $S/tmp/b3_inputs_i101_format.jsonl
echo "shapes rc=$?"
$S/tools/job.sh slot py_on_rs $S $VENV/bin/python $S/tools/py_on_inputs.py $A/projects/chirality-piping $S/inputs/i101/rs_inputs.jsonl $S/inputs/i101/rs_shapes.jsonl $S/inputs/i101/ts_shapes.jsonl $S/shapes/PY_ON_I101_INPUTS.json
echo "py_on_rs rc=$?"
$VENV/bin/python $S/tools/shapes_tsv.py $S/shapes/b3_shapes.json $S/shapes/py_b3_shapes.jsonl $S/shapes/SHAPES.tsv
