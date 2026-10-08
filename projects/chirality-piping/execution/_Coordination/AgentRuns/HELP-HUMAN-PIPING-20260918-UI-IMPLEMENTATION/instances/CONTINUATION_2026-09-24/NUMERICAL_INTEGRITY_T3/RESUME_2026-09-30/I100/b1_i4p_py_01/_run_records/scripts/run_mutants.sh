#!/bin/bash
# I100: the mutant runs, one T3 slot job each, one at a time: the control (NONE) and M1-M10 on the mutant copy,
# and PRE (the head's tests on I4's three reader files). Each runs the two retained test files and the
# preview-physics consumer contract in full, with junit. Usage: run_mutants.sh <id> [<id> ...]
set -u
source WT/scratch/i100_b1_i4p_py/tools/env.sh
FILES="tests/test_retained_precision_contract.py tests/test_retained_precision_carriers.py tests/test_preview_physics_consumer_contract.py"
for id in "$@"; do
  O=$S/mutants/runs/$id; mkdir -p $O
  if [ "$id" = PRE ]; then P=$S/pre/projects/chirality-piping; MUT=; else P=$S/mut/projects/chirality-piping; MUT=$id; [ "$id" = NONE ] && MUT=; fi
  $S/tools/job.sh slot mut_$id $P /usr/bin/env I100_MUT=$MUT $VENV/bin/python -m pytest -p no:cacheprovider --basetemp=$S/tmp/mut_$id/basetemp -q -rf --junitxml=$O/junit.xml $FILES > $O/pytest.log 2>&1
  echo "$id rc=$?"
done
echo mutants done
