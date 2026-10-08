#!/bin/bash
# I100 B3: the mutant runs, one T3 slot job each, one at a time, on the mutant copy (WT/scratch/i100_b3r/mut):
# the control (NONE) and each mutant id, running B3's test file and the D31 test with junit. Usage: run_mutants.sh <id>...
set -u
source WT/scratch/i100_b3r/tools/env.sh
FILES="tests/test_retained_precision_b3.py tests/test_retained_precision_contract.py::test_model_schema_versions_d31"
P=$S/mut/projects/chirality-piping
for id in "$@"; do
  O=$S/mutants/runs/$id; mkdir -p $O
  MUT=$id; [ "$id" = NONE ] && MUT=
  $S/tools/job.sh slot mut_$id $P /usr/bin/env I100_MUT=$MUT $VENV/bin/python -m pytest -p no:cacheprovider --basetemp=$S/tmp/mut_$id/basetemp -q -rf --junitxml=$O/junit.xml $FILES > $O/pytest.log 2>&1
  echo "$id rc=$?"
done
echo mutants done
