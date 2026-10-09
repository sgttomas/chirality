#!/bin/bash
# I105 J0b: at one head (an archive copy), one heavy job at a time: PP's suite (all targets), the runner, result_export
# (all targets), desktop vitest (whole) and tsc, the PY reader set (pytest, junit); the census with RV113's harnesses
# (RS, TS) and I100's PY harness (all unchanged) over 07m, 07n and 07n-N, and the two legacy-label reader probes; then
# the PP scratch probe (an uncommitted test module added to the copy after the suites).
# Usage: head_chain.sh <tag> <commit>
WT=WT
S=$WT/scratch/i105_j0b
J=$S/bin/job.sh
T=$1; C=$2; TG=$WT/targets/i105-j0b-$T
$S/bin/copy.sh "$C" "$T" || { echo "copy failed"; exit 1; }
P=$S/copies/$T/projects/chirality-piping; O=$S/out
mkdir -p $O/suites $O/census $O/probes
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
H=$WT/targets/i105-j0b-pyh
PYENV="OPENPIPESTRESS_CHECKED_JSON_BIN=$H/cj/release/openpipestress_jcs_ijson OPENPIPESTRESS_BINARY64_JSON_BIN=$H/cj64/release/openpipestress_jcs_binary64 OPENPIPESTRESS_UNITS_BIN=$H/units/release/openpipestress_units"
mkdir -p $S/tmp/${T}_py_bt
$J slot ${T}_py "$P" /usr/bin/env $PYENV $WT/venv/bin/python -m pytest -p no:cacheprovider --basetemp=$S/tmp/${T}_py_bt/bt -q -rf \
  --junitxml=$O/suites/${T}_py.junit.xml $PYF; echo "$T py rc=$?"
cp $S/tools/rv113_census.rs "$P/core/reporting/result_export/tests/rv113_census.rs"
cp $S/tools/rv113Census.test.ts "$P/apps/desktop/src/features/results/rv113Census.test.ts"
for k in 07m 07n 07nN; do
  cp $S/corpora/$k.json "$P/fixtures/results/retained_precision_cases.json"
  echo "$T $k corpus $(shasum -a 256 "$P/fixtures/results/retained_precision_cases.json" | cut -c1-16)"
  RV113_OUT=$O/census/${T}_${k}_rs.jsonl RUST_TEST_THREADS=2 $J cargo ${T}_${k}_rs_census "$P/core/reporting/result_export" "$TG-re" test --locked --offline --test rv113_census rv113_census
  echo "$T $k rs census rc=$?"
  $J slot ${T}_${k}_ts_census "$P/apps/desktop" /usr/bin/env RV113_OUT=$O/census/${T}_${k}_ts.jsonl "$P/node_modules/.bin/vitest" run src/features/results/rv113Census.test.ts
  echo "$T $k ts census rc=$?"
  $J slot ${T}_${k}_py_census "$S" /usr/bin/env $PYENV $WT/venv/bin/python -I $S/tools/rv113_py_harness.py "$P" census $O/census/${T}_${k}_py.jsonl
  echo "$T $k py census rc=$?"
done
# The reader probes, on the head's own corpus (07n-N, the last copied).
RV113_PROBES=$S/probes/reader_probes.json RV113_PROBES_OUT=$O/probes/${T}_rs.jsonl RUST_TEST_THREADS=2 $J cargo ${T}_rs_probes "$P/core/reporting/result_export" "$TG-re" test --locked --offline --test rv113_census rv113_probes
echo "$T rs probes rc=$?"
$J slot ${T}_ts_probes "$P/apps/desktop" /usr/bin/env RV113_PROBES=$S/probes/reader_probes.json RV113_PROBES_OUT=$O/probes/${T}_ts.jsonl "$P/node_modules/.bin/vitest" run src/features/results/rv113Census.test.ts
echo "$T ts probes rc=$?"
$J slot ${T}_py_probes "$S" /usr/bin/env $PYENV $WT/venv/bin/python -I $S/tools/rv113_py_harness.py "$P" probes $S/probes/reader_probes.json $O/probes/${T}_py.jsonl
echo "$T py probes rc=$?"
# The PP scratch probe (copy only).
cp $S/probes/i105_j0b_probe.rs "$P/core/product_physics/src/i105_j0b_probe.rs"
printf '\n#[cfg(test)]\nmod i105_j0b_probe;\n' >> "$P/core/product_physics/src/lib.rs"
$J cargo ${T}_pp_probe "$P/core/product_physics" "$TG-pp" test --locked --offline --lib i105_j0b -- --nocapture; echo "$T pp probe rc=$?"
