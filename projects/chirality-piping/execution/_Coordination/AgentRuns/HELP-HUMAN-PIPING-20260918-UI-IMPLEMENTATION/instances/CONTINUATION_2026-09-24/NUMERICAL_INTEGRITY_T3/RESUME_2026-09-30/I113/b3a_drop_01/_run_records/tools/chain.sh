#!/bin/bash
# I113 (B3a drop): at one commit of WT/b2, archive copies, then the suites (PP all targets, the headless runner, RE, the
# PY reader set, desktop vitest whole and tsc) and RV113's census (RS, TS and PY over 07m and 07n). This chain's jobs
# run one after another. Usage: chain.sh <label> <commit> [parts...]
#   parts: copies pyh pp runner re py ts tsc census (default: copies pp runner re py ts tsc census)
set -u
source WT/scratch/i113_b3a/tools/env.sh
J=$S/tools/job.sh
L=$1; C=$2; shift 2
PARTS=${*:-copies pp runner re py ts tsc census}
O=$S/runs/$L; mkdir -p $O
C07N=$WT/scratch/i101_b3r/add1/c07n/retained_precision_cases.07n.json
PYHARNESS=$WT/scratch/i100_b3r/tools/rv113_py_harness.py
SP=$S/copies/${L}_s/projects/chirality-piping
HP=$S/copies/${L}_h/projects/chirality-piping
NP=$S/copies/${L}_n/projects/chirality-piping
TG=$WT/targets/i113-$L
note() { echo "$1 rc=$2 $(date -u +%FT%TZ)" >> "$O/meta.txt"; }
echo "START $L $C $(date -u +%FT%TZ) parts=$PARTS" >> $O/meta.txt
PYSET="tests/test_adapter_framework_contract.py tests/test_analysis_run_schema.py tests/test_analysis_run_records.py tests/test_analysis_status_schema.py tests/test_analysis_run_compatibility.py tests/test_comparison_contracts.py tests/test_handoff_package_schema.py tests/test_handoff_export_workflow.py tests/test_load_reference_headless_artifacts.py tests/test_invented_example_models.py tests/test_load_reference_schema.py tests/test_load_reference_source_schema.py tests/test_persistence_schema.py tests/test_physics_consumer_contract.py tests/test_preview_physics_consumer_contract.py tests/test_precision_consumer_contract.py tests/test_project_persistence_service.py tests/test_result_export_v0_2.py tests/test_stress_neutral_physics_source.py tests/test_results_schema.py tests/test_source_block_schema_contract.py tests/test_stress_neutral_precision.py tests/test_stress_neutral_export_package.py tests/test_retained_precision_contract.py tests/test_retained_precision_schema.py tests/test_retained_precision_carriers.py tests/test_results_dispatcher_v0_3.py tests/test_physics_source_contract.py tests/test_retained_precision_b3.py"
for part in $PARTS; do case $part in
copies)
  { $S/tools/make_copy.sh $C ${L}_s s && $S/tools/make_copy.sh $C ${L}_h h && $S/tools/make_copy.sh $C ${L}_n h \
    && cp $C07N $NP/fixtures/results/retained_precision_cases.json; } > $O/copies.txt 2>&1; note copies $?
  shasum -a 256 $HP/fixtures/results/retained_precision_cases.json $NP/fixtures/results/retained_precision_cases.json | sed "s#$S/copies/##" > $O/corpora.sha256 ;;
pyh)
  $J cargo ${L}_pyh_cj $SP/core/serialization/canonical_json $PYH/cj build --locked --offline --release --features checked-cli --bin openpipestress_jcs_ijson --bin openpipestress_jcs_binary64; note pyh_cj $?
  $J cargo ${L}_pyh_units $SP/core/units $PYH/units build --locked --offline --release --features cli --bin openpipestress_units; note pyh_units $? ;;
pp)
  RUST_TEST_THREADS=4 $J cargo ${L}_pp $SP/core/product_physics $TG-pp test --locked --offline --no-fail-fast; note pp $? ;;
runner)
  RUST_TEST_THREADS=4 $J cargo ${L}_runner $SP/core/runner/headless $TG-runner test --locked --offline --no-fail-fast; note runner $? ;;
re)
  RUST_TEST_THREADS=4 $J cargo ${L}_re $SP/core/reporting/result_export $TG-re test --locked --offline --no-fail-fast; note re $? ;;
py)
  $J slot ${L}_py $SP /bin/bash -c "$VENV/bin/python -m pytest -p no:cacheprovider --basetemp=$S/tmp/${L}_py/basetemp -q -rs -rf -v --junitxml=$O/py.xml $PYSET > $O/py.log 2>&1"; note py $? ;;
ts)
  $J slot ${L}_vitest $SP/apps/desktop $SP/node_modules/.bin/vitest run --reporter=dot --reporter=json --outputFile.json=$O/vitest.json; note vitest $? ;;
tsc)
  $J slot ${L}_tsc $SP/apps/desktop $SP/node_modules/.bin/tsc --noEmit -p tsconfig.json; note tsc $? ;;
census)
  for k in h n; do
    CP=$S/copies/${L}_$k/projects/chirality-piping
    RV113_OUT=$O/c07${k/h/m}_rs.jsonl RUST_TEST_THREADS=2 $J cargo ${L}_census_${k}_rs $CP/core/reporting/result_export $TG-rh test --locked --offline --test rv113_census; note census_${k}_rs $?
    $J slot ${L}_census_${k}_ts $CP/apps/desktop /usr/bin/env RV113_OUT=$O/c07${k/h/m}_ts.jsonl $CP/node_modules/.bin/vitest run src/features/results/rv113Census.test.ts; note census_${k}_ts $?
    $J slot ${L}_census_${k}_py $S $VENV/bin/python $PYHARNESS $CP census $O/c07${k/h/m}_py.jsonl; note census_${k}_py $?
  done ;;
esac; done
echo "DONE $L $(date -u +%FT%TZ)" >> $O/meta.txt
