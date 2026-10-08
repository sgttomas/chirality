#!/bin/bash
# RV120 (SC): the heavy jobs at b1's head 57c92a7b33, one at a time: RE's whole suite (cargo, builds the harness too);
# RV113's three harnesses over the whole corpus (07m + 07n); TS's whole vitest suite; PY's retained test files.
WT=WT
S=$WT/scratch/rv120_rvr
J=$S/tools/rv120_job.sh
P=$S/copies/sc-head/projects/chirality-piping
RE=$P/core/reporting/result_export
T=$WT/targets/rv120-sc-head
B=$WT/targets/rv120-pybins/release
ENV="OPENPIPESTRESS_CHECKED_JSON_BIN=$B/openpipestress_jcs_ijson OPENPIPESTRESS_BINARY64_JSON_BIN=$B/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$B/openpipestress_units PYTHONDONTWRITEBYTECODE=1"
$J cargo sc_rs_suite $RE $T test --locked --offline; echo "sc_rs_suite rc=$?"
D=$T/debug/deps; RSB=$D/$(ls $D | grep -E '^rv113_census-[0-9a-f]+$' | head -1)
$J slot sc_rs_census $RE /usr/bin/env RV113_OUT=$S/sc/census/rs.jsonl RUST_TEST_THREADS=2 "$RSB" rv113_census --exact; echo "sc_rs_census rc=$?"
$J slot sc_ts_census $P/apps/desktop /usr/bin/env RV113_OUT=$S/sc/census/ts.jsonl $P/node_modules/.bin/vitest run src/features/results/rv113Census.test.ts; echo "sc_ts_census rc=$?"
rm -rf $P/apps/desktop/node_modules/.vite
$J slot sc_py_census $P /usr/bin/env $ENV $WT/venv/bin/python $S/tools/rv113_py_harness.py $P census $S/sc/census/py.jsonl; echo "sc_py_census rc=$?"
$J slot sc_ts_vitest $P/apps/desktop $P/node_modules/.bin/vitest run --reporter=dot --reporter=json --outputFile.json=$S/sc/suites/vitest_sc_head.json; echo "sc_ts_vitest rc=$?"
rm -rf $P/apps/desktop/node_modules/.vite
mkdir -p $S/sc/tmp/py
$J slot sc_py_tests $P /usr/bin/env $ENV $WT/venv/bin/python -m pytest -p no:cacheprovider --basetemp=$S/sc/tmp/py/basetemp -q -rf --junitxml=$S/sc/suites/py_sc_head.xml tests/test_retained_precision_contract.py tests/test_retained_precision_carriers.py tests/test_retained_precision_schema.py; echo "sc_py_tests rc=$?"
echo sc-chain-done
