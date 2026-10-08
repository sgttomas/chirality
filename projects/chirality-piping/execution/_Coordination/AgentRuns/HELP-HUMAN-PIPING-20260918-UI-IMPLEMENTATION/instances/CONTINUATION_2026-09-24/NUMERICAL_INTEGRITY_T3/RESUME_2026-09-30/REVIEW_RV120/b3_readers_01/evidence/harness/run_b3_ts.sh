#!/bin/bash
# RV120 B3: heavy jobs on the TS head copy (77aaaa61d1; RE src = RS head c845e899da), one at a time:
# RE's whole suite (dumps the B3b shapes' readings and inputs), RV113's RS census (07m+07n), the TS census,
# TS's whole vitest suite (JSON), tsc, and PY's schema/retained test files (lane T's schema edits).
WT=WT
S=$WT/scratch/rv120_rvr
B3=$S/b3
export RV120_LOGDIR=$B3/logs
J=$S/tools/rv120_job.sh
c=${1:-ts}
P=$WT/rv120b3/$c/projects/chirality-piping
RE=$P/core/reporting/result_export
T=$WT/targets/rv120b3-$c
B=$WT/targets/rv120b3-pybins/release
ENV="OPENPIPESTRESS_CHECKED_JSON_BIN=$B/openpipestress_jcs_ijson OPENPIPESTRESS_BINARY64_JSON_BIN=$B/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$B/openpipestress_units PYTHONDONTWRITEBYTECODE=1"
env B3B_SHAPES_OUT=$B3/shapes/rs_${c}_shapes.jsonl B3B_INPUTS_OUT=$B3/shapes/rs_${c}_inputs.jsonl $J cargo ${c}_re_suite $RE $T test --locked --offline; echo "${c}_re_suite rc=$?"
D=$T/debug/deps; RSB=$D/$(ls -t $D | grep -E '^rv113_census-[0-9a-f]+$' | head -1)
$J slot ${c}_rs_census $RE /usr/bin/env RV113_OUT=$B3/census/rs_${c}.jsonl RUST_TEST_THREADS=2 "$RSB" rv113_census --exact; echo "${c}_rs_census rc=$?"
$J slot ${c}_ts_census $P/apps/desktop /usr/bin/env RV113_OUT=$B3/census/ts_${c}.jsonl $P/node_modules/.bin/vitest run src/features/results/rv113Census.test.ts; echo "${c}_ts_census rc=$?"
rm -rf $P/apps/desktop/node_modules/.vite
$J slot ${c}_ts_vitest $P/apps/desktop $P/node_modules/.bin/vitest run --reporter=dot --reporter=json --outputFile.json=$B3/suites/vitest_${c}.json; echo "${c}_ts_vitest rc=$?"
rm -rf $P/apps/desktop/node_modules/.vite
$J slot ${c}_tsc $P/apps/desktop $P/node_modules/.bin/tsc --noEmit -p tsconfig.json; echo "${c}_tsc rc=$?"
mkdir -p $B3/tmp/py_$c
$J slot ${c}_py_tests $P /usr/bin/env $ENV $WT/venv/bin/python -m pytest -p no:cacheprovider --basetemp=$B3/tmp/py_$c/basetemp -q -rf --junitxml=$B3/suites/py_${c}.xml tests/test_retained_precision_contract.py tests/test_retained_precision_carriers.py tests/test_retained_precision_schema.py tests/test_load_reference_schema.py tests/test_load_reference_source_schema.py tests/test_source_block_schema_contract.py $( [ -f $P/tests/test_retained_precision_b3.py ] && echo tests/test_retained_precision_b3.py ); echo "${c}_py_tests rc=$?"
echo "b3-$c-chain-done"
