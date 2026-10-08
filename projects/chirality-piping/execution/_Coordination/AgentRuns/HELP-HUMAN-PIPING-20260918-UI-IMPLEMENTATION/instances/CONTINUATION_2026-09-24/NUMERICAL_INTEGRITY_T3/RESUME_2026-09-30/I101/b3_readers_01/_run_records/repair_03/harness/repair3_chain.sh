#!/bin/bash
# I101 repair 03's evidence at the heads, one heavy job at a time: chain_final (RS and TS census over 07m, RE suites at both
# heads, vitest and tsc, PY carrier schemas, PP's B3 tests, the three readers' shapes), the RS and TS census over 07n, PY's
# census over 07m and 07n, and PY's B3 module at the base (101ebcff76, repair 02's head) and the head (junit).
# Usage: repair3_chain.sh <rs commit> <ts commit> <py commit>
WT=WT
S=$WT/scratch/i101_b3r
J=$S/harness/job.sh
$S/harness/chain_final.sh final5 "$1" "$2" "$3"; echo "# chain rc=$?"
$S/harness/census_07n.sh final5 "$1" "$2"; echo "# c07n rc=$?"
$S/harness/make_copy.sh b2-p "$3" pyc5 s > $S/repair3/pycensus_copy.txt && $J slot py_census_final5 $S /bin/bash $S/harness/py_census.sh pyc5 final5; echo "# py census rc=$?"
for x in "101ebcff76 pyb3" "$3 pyh3"; do set -- $x
  $S/harness/make_copy.sh b2-p "$1" $2 s > $S/repair3/copy_$2.txt || exit 1
  mkdir -p $S/tmp/$2_bt
  $J slot py_b3_$2 $S/copies/$2/projects/chirality-piping /usr/bin/env OPENPIPESTRESS_CHECKED_JSON_BIN=$WT/targets/i101-b3r-pyh/cj/release/openpipestress_jcs_ijson \
    OPENPIPESTRESS_BINARY64_JSON_BIN=$WT/targets/i101-b3r-pyh/cj64/release/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$WT/targets/i101-b3r-pyh/units/release/openpipestress_units \
    $WT/venv/bin/python -m pytest -p no:cacheprovider --basetemp=$S/tmp/$2_bt/bt -q -rf --junitxml=$S/repair3/py_b3_$2.junit.xml tests/test_retained_precision_b3.py tests/test_retained_precision_contract.py
  echo "# py b3 $2 rc=$?"
done
