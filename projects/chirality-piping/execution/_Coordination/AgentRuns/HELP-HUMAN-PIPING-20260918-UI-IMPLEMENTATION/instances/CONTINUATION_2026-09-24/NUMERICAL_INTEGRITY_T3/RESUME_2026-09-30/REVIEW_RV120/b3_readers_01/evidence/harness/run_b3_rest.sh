#!/bin/bash
# RV120 B3: the remaining heavy jobs, one at a time: the base chain (run_b3_ts.sh base); PY's test files at the TS head
# (re-run with the authority binaries); PY's census (07m) and test files at PY's head.
WT=WT
S=$WT/scratch/rv120_rvr
B3=$S/b3
export RV120_LOGDIR=$B3/logs
J=$S/tools/rv120_job.sh
B=$WT/targets/rv120b3-pybins/release
ENV="OPENPIPESTRESS_CHECKED_JSON_BIN=$B/openpipestress_jcs_ijson OPENPIPESTRESS_BINARY64_JSON_BIN=$B/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$B/openpipestress_units PYTHONDONTWRITEBYTECODE=1"
$S/tools/run_b3_ts.sh base
PYT="tests/test_retained_precision_contract.py tests/test_retained_precision_carriers.py tests/test_retained_precision_schema.py tests/test_load_reference_schema.py tests/test_load_reference_source_schema.py tests/test_source_block_schema_contract.py"
P=$WT/rv120b3/ts/projects/chirality-piping; mkdir -p $B3/tmp/py_ts2
$J slot ts_py_tests2 $P /usr/bin/env $ENV $WT/venv/bin/python -m pytest -p no:cacheprovider --basetemp=$B3/tmp/py_ts2/basetemp -q -rf --junitxml=$B3/suites/py_ts.xml $PYT; echo "ts_py_tests2 rc=$?"
P=$WT/rv120b3/base/projects/chirality-piping
$J slot base_py_census $P /usr/bin/env $ENV $WT/venv/bin/python $S/tools/rv113_py_harness.py $P census $B3/census/py_base.jsonl; echo "base_py_census rc=$?"
P=$WT/rv120b3/py/projects/chirality-piping; mkdir -p $B3/tmp/py_py
$J slot py_py_census $P /usr/bin/env $ENV $WT/venv/bin/python $S/tools/rv113_py_harness.py $P census $B3/census/py_py.jsonl; echo "py_py_census rc=$?"
$J slot py_py_tests $P /usr/bin/env $ENV $WT/venv/bin/python -m pytest -p no:cacheprovider --basetemp=$B3/tmp/py_py/basetemp -q -rf --junitxml=$B3/suites/py_py.xml $PYT tests/test_retained_precision_b3.py; echo "py_py_tests rc=$?"
echo b3-rest-done
