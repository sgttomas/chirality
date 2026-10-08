#!/bin/bash
# I101 lane T: the PY tests that read the three carrier schemas, in an archive copy, with WT/venv (no install).
# Usage: py_schema.sh <copy name> <label>
WT=WT
S=$WT/scratch/i101_b3r
C=$S/copies/$1/projects/chirality-piping
mkdir -p $S/tmp/$2_bt
# The two helper binaries, built once through t3_cargo.sh (py_helpers.sh), so the session builds nothing.
export OPENPIPESTRESS_CHECKED_JSON_BIN=$WT/targets/i101-b3r-pyh/cj/release/openpipestress_jcs_ijson
export OPENPIPESTRESS_UNITS_BIN=$WT/targets/i101-b3r-pyh/units/release/openpipestress_units
cd $C && $WT/venv/bin/python -m pytest -p no:cacheprovider --basetemp=$S/tmp/$2_bt/bt -q -rf --junitxml=$S/out/$2.junit.xml \
  tests/test_retained_precision_schema.py tests/test_load_reference_schema.py tests/test_load_reference_source_schema.py \
  tests/test_source_block_schema_contract.py tests/test_results_dispatcher_v0_3.py tests/test_physics_consumer_contract.py \
  tests/test_preview_physics_consumer_contract.py tests/test_result_export_v0_2.py tests/test_stress_neutral_physics_source.py \
  tests/test_stress_neutral_precision.py tests/test_load_reference_headless_artifacts.py tests/test_analysis_run_schema.py
