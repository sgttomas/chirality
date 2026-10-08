#!/bin/bash
# RV120 (SC): each reader's own corpus tests on a copy whose corpus carries nine corrupted 07n expectations
# (corrupt_expectations.py). Every run is expected to fail; the failures must name the corrupted entries.
WT=WT
S=$WT/scratch/rv120_rvr
J=$S/tools/rv120_job.sh
P=$S/copies/sc-exp/projects/chirality-piping
B=$WT/targets/rv120-pybins/release
ENV="OPENPIPESTRESS_CHECKED_JSON_BIN=$B/openpipestress_jcs_ijson OPENPIPESTRESS_BINARY64_JSON_BIN=$B/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$B/openpipestress_units PYTHONDONTWRITEBYTECODE=1"
$J cargo sc_exp_rs $P/core/reporting/result_export $WT/targets/rv120-sc-exp test --locked --offline --test retained_precision_contract -- --test-threads 4; echo "sc_exp_rs rc=$?"
$J slot sc_exp_ts $P/apps/desktop $P/node_modules/.bin/vitest run src/features/results/retainedPrecision.test.ts --reporter=dot --reporter=json --outputFile.json=$S/sc/exp/vitest_exp.json; echo "sc_exp_ts rc=$?"
rm -rf $P/apps/desktop/node_modules/.vite
mkdir -p $S/sc/tmp/pyexp
$J slot sc_exp_py $P /usr/bin/env $ENV $WT/venv/bin/python -m pytest -p no:cacheprovider --basetemp=$S/sc/tmp/pyexp/basetemp -q -rf --junitxml=$S/sc/exp/py_exp.xml tests/test_retained_precision_contract.py; echo "sc_exp_py rc=$?"
echo sc-exp-done
