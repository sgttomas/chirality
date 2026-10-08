#!/bin/bash
# I100: each reader's own corpus tests on the corpus now in M (one heavy job at a time): PY's three retained files
# (slot, junit), RS's retained_precision_contract test and the lib's corpus test (cargo), TS's retainedPrecision tests
# (slot, vitest JSON). Usage: own_suites.sh <label>
source WT/scratch/i100_b1_sc/tools/env_sc.sh
LABEL=$1; O=$S/runs/$LABEL; mkdir -p $O
$S/tools/job.sh slot ${LABEL}_own_py $P $VENV/bin/python -m pytest -p no:cacheprovider --basetemp=$S/tmp/${LABEL}_own_py/bt -q -rf --junitxml=$O/own_py.xml tests/test_retained_precision_contract.py tests/test_retained_precision_schema.py tests/test_retained_precision_carriers.py; echo "own py rc=$?"
$S/tools/job.sh cargo ${LABEL}_own_rs $P/core/reporting/result_export $WT/targets/i100-b1-sc/rs test --locked --offline --test retained_precision_contract --lib -- --test-threads=4; echo "own rs rc=$?"
$S/tools/job.sh slot ${LABEL}_own_ts $P/apps/desktop $NMS/.bin/vitest run --reporter=dot --reporter=json --outputFile.json=$O/own_ts.json src/features/results/retainedPrecision.test.ts; echo "own ts rc=$?"; rm -rf $P/apps/desktop/node_modules/.vite
