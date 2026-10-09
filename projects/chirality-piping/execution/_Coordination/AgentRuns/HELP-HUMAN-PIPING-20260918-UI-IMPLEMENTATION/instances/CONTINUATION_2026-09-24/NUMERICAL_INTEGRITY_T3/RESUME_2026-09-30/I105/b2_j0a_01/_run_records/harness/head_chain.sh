#!/bin/bash
# I105 J0a: at one head (an archive copy), one heavy job at a time: PP's suite (all targets), the runner, result_export
# (all targets), desktop vitest (whole) and tsc, the PY reader set (pytest, junit); then the census with RV113's
# harnesses (RS, TS) and I100's PY harness (all three unchanged) over 07m, 07n and 07n-N (main's 07n, PR-N's re-pins).
# Usage: head_chain.sh <tag> <commit>
WT=WT
S=$WT/scratch/i105_j0a
J=$S/bin/job.sh
T=$1; C=$2; TG=$WT/targets/i105-j0a-$T
$S/bin/copy.sh "$C" "$T" || { echo "copy failed"; exit 1; }
P=$S/copies/$T/projects/chirality-piping; O=$S/out
export RUST_TEST_THREADS=4
$J cargo ${T}_pp "$P/core/product_physics" "$TG-pp" test --locked --offline --no-fail-fast; echo "$T pp rc=$?"
$J cargo ${T}_runner "$P/core/runner/headless" "$TG-runner" test --locked --offline --no-fail-fast; echo "$T runner rc=$?"
$J cargo ${T}_re "$P/core/reporting/result_export" "$TG-re" test --locked --offline --no-fail-fast; echo "$T re rc=$?"
$J slot ${T}_vitest "$P/apps/desktop" "$P/node_modules/.bin/vitest" run --reporter=dot --reporter=json --outputFile.json=$O/suites/${T}_vitest.json; echo "$T vitest rc=$?"
$J slot ${T}_tsc "$P/apps/desktop" "$P/node_modules/.bin/tsc" --noEmit -p tsconfig.json; echo "$T tsc rc=$?"
PYF=""
for f in test_retained_precision_b3.py test_retained_precision_contract.py test_retained_precision_carriers.py test_retained_precision_schema.py \
  test_precision_consumer_contract.py test_load_reference_schema.py test_load_reference_source_schema.py test_source_block_schema_contract.py \
  test_results_dispatcher_v0_3.py test_physics_consumer_contract.py test_preview_physics_consumer_contract.py test_result_export_v0_2.py \
  test_stress_neutral_physics_source.py test_stress_neutral_precision.py test_load_reference_headless_artifacts.py test_analysis_run_schema.py; do
  [ -f "$P/tests/$f" ] && PYF="$PYF tests/$f"
done
echo "$T py files:$PYF"
H=$WT/targets/i105-j0a-pyh
PYENV="OPENPIPESTRESS_CHECKED_JSON_BIN=$H/cj/release/openpipestress_jcs_ijson OPENPIPESTRESS_BINARY64_JSON_BIN=$H/cj64/release/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$H/units/release/openpipestress_units"
mkdir -p $S/tmp/${T}_py_bt
$J slot ${T}_py "$P" /usr/bin/env $PYENV $WT/venv/bin/python -m pytest -p no:cacheprovider --basetemp=$S/tmp/${T}_py_bt/bt -q -rf \
  --junitxml=$O/suites/${T}_py.junit.xml $PYF; echo "$T py rc=$?"
# The census: harnesses added after the suites, the corpus file replaced for each run.
cp $S/tools/rv113_census.rs "$P/core/reporting/result_export/tests/rv113_census.rs"
cp $S/tools/rv113Census.test.ts "$P/apps/desktop/src/features/results/rv113Census.test.ts"
for k in 07m 07n 07nN; do
  cp $S/corpora/$k.json "$P/fixtures/results/retained_precision_cases.json"
  echo "$T $k corpus $(shasum -a 256 "$P/fixtures/results/retained_precision_cases.json" | cut -c1-16)"
  RV113_OUT=$O/census/${T}_${k}_rs.jsonl RUST_TEST_THREADS=2 $J cargo ${T}_${k}_rs_census "$P/core/reporting/result_export" "$TG-re" test --locked --offline --test rv113_census
  echo "$T $k rs census rc=$?"
  $J slot ${T}_${k}_ts_census "$P/apps/desktop" /usr/bin/env RV113_OUT=$O/census/${T}_${k}_ts.jsonl "$P/node_modules/.bin/vitest" run src/features/results/rv113Census.test.ts
  echo "$T $k ts census rc=$?"
  $J slot ${T}_${k}_py_census "$S" /usr/bin/env $PYENV $WT/venv/bin/python -I $S/tools/rv113_py_harness.py "$P" census $O/census/${T}_${k}_py.jsonl
  echo "$T $k py census rc=$?"
done
