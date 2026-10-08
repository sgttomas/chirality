#!/bin/bash
# I100 B3: at the final head (head3): B3's test file with the two existing tests it touches, the control on the
# mutant copy with that test file, then the shapes.
source WT/scratch/i100_b3r/tools/env.sh
cp $S/head3/projects/chirality-piping/tests/test_retained_precision_b3.py $S/mut/projects/chirality-piping/tests/test_retained_precision_b3.py
$S/tools/pyt.sh head3 $S/head3/projects/chirality-piping tests/test_retained_precision_b3.py tests/test_retained_precision_contract.py::test_model_schema_versions_d31 tests/test_preview_physics_consumer_contract.py::test_table_identity_and_registry
$S/tools/run_mutants.sh NONE
$S/tools/job.sh slot shapes $S $VENV/bin/python $S/tools/b3_shapes.py $S/head3/projects/chirality-piping $S/shapes/b3_shapes.json $S/shapes/py_b3_shapes.jsonl
echo "shapes rc=$?"
