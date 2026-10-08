#!/bin/bash
# I100 B3 addendum 01: one heavy job at a time. The shared shapes and PY's verdicts at b7721d27e9; then the exact-route
# shapes in census mode, unaligned (arch3: RS b2-r b2b58699bb, TS b2-t 36823f5b2d) and aligned (arch2: both diffs).
source WT/scratch/i100_b3r/tools/env.sh
$S/tools/job.sh slot add1_shapes $S $VENV/bin/python $S/tools/add1_shapes.py $S/head5/projects/chirality-piping $S/add1/probes.json $S/add1/shapes/add1_shapes.json $S/add1/shapes/py_add1_shapes.jsonl $S/add1/shapes/add1_inputs.jsonl
echo "shapes rc=$?"
ARCH=$S/add1/arch3 TGT=i100-b3r-rs-x3 $S/tools/add1_exact.sh exact_today
$VENV/bin/python $S/tools/add1_exact_corpus.py $S/head5/projects/chirality-piping $S/add1/arch2/projects/chirality-piping/fixtures/results/retained_precision_cases.json
ARCH=$S/add1/arch2 TGT=i100-b3r-rs-aligned $S/tools/add1_exact.sh exact_aligned
echo "chain2 done"
