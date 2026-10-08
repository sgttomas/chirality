#!/bin/bash
# I101 addendum 01: the three tests the N6(b) commit (57c92a7b33) touches, in copy n6 of it, one heavy job at a time.
# PY with I100's existing builds: only OPENPIPESTRESS_CHECKED_JSON_BIN and OPENPIPESTRESS_UNITS_BIN are set (ROOT's instruction).
WT=WT
S=$WT/scratch/i101_b1_sc_pins
J=$S/harness/job.sh
P=$S/copies/n6/projects/chirality-piping
TG=$WT/targets/i100-b1-i4p-py
RUST_TEST_THREADS=4 $J cargo a1_rs_carriers "$P/core/reporting/result_export" "$WT/targets/i101-b1-sc-pins/n6" test --locked --offline --test retained_precision_carriers
echo "rs carriers rc=$?"
$J slot a1_ts_integration "$P/apps/desktop" "$P/node_modules/.bin/vitest" run src/features/results/retainedPrecisionIntegration.test.tsx
echo "ts integration rc=$?"
mkdir -p "$S/tmp/a1_py_bt"
$J slot a1_py_carriers "$P" /usr/bin/env -u OPENPIPESTRESS_BINARY64_JSON_BIN OPENPIPESTRESS_CHECKED_JSON_BIN=$TG/checked-json/release/openpipestress_jcs_ijson \
  OPENPIPESTRESS_UNITS_BIN=$TG/units-authority/release/openpipestress_units PYTHONDONTWRITEBYTECODE=1 \
  $WT/venv/bin/python -m pytest -p no:cacheprovider --basetemp=$S/tmp/a1_py_bt/bt -q -rf tests/test_retained_precision_carriers.py
echo "py carriers rc=$?"
