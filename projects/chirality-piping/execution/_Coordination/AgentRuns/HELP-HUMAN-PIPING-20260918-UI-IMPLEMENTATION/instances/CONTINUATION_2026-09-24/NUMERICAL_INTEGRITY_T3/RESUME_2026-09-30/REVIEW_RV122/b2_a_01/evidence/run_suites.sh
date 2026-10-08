#!/bin/bash
# RV122 (RV-Q2): suites on a git-archive copy, one heavy job at a time, through the T3 wrappers.
# Usage: run_suites.sh <archive root holding projects/chirality-piping> <tag> [parts...]
# parts: bins re pp runner py ts. Logs: $S/runs/<tag>/<part>.log; rc lines in meta.txt.
set -u
WT=WT
S=$WT/scratch/rv122_rvq2
ROOT=$1; TAG=$2; shift 2
PARTS=${*:-bins re pp runner py ts}
P=$ROOT/projects/chirality-piping
O=$S/runs/$TAG; mkdir -p "$O"
export TMPDIR=$S/tmp RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0 CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=4
unset RUSTFLAGS CARGO_ENCODED_RUSTFLAGS
TG=$WT/targets/rv122-$TAG
NMS=APPWT/projects/chirality-piping/node_modules
WASM=$WT/sweep-skewpin/projects/chirality-piping/apps/desktop/public
note() { echo "$1 rc=$2 $(date -u +%FT%TZ)" >> "$O/meta.txt"; }
case "$ROOT" in $S/*) ;; *) echo "not an archive in scratch: $ROOT" >&2; exit 9 ;; esac
cd "$P" || exit 9
echo "START $TAG $PARTS $(date -u +%FT%TZ)" >> "$O/meta.txt"
for part in $PARTS; do case $part in
bins)
  $WT/tools/t3_cargo.sh build --locked --offline --release --features checked-cli --bin openpipestress_jcs_ijson \
    --manifest-path core/serialization/canonical_json/Cargo.toml --target-dir "$TG-cj" > "$O/bins.log" 2>&1; note bins_cj $?
  $WT/tools/t3_cargo.sh build --locked --offline --release --features cli --bin openpipestress_units \
    --manifest-path core/units/Cargo.toml --target-dir "$TG-units" >> "$O/bins.log" 2>&1; note bins_units $? ;;
re)
  $WT/tools/t3_cargo.sh test --locked --offline --no-fail-fast --manifest-path core/reporting/result_export/Cargo.toml \
    --target-dir "$TG-re" > "$O/re.log" 2>&1; note re $? ;;
pp)
  $WT/tools/t3_cargo.sh test --locked --offline --no-fail-fast --manifest-path core/product_physics/Cargo.toml \
    --target-dir "$TG-pp" --lib --tests > "$O/pp.log" 2>&1; note pp $? ;;
pplib)
  $WT/tools/t3_cargo.sh test --locked --offline --no-fail-fast --manifest-path core/product_physics/Cargo.toml \
    --target-dir "$TG-pp" --lib -- --nocapture --test-threads=4 > "$O/pplib.log" 2>&1; note pplib $? ;;
runner)
  $WT/tools/t3_cargo.sh test --locked --offline --no-fail-fast --manifest-path core/runner/headless/Cargo.toml \
    --target-dir "$TG-runner" > "$O/runner.log" 2>&1; note runner $? ;;
py)
  OPENPIPESTRESS_CHECKED_JSON_BIN=$TG-cj/release/openpipestress_jcs_ijson OPENPIPESTRESS_UNITS_BIN=$TG-units/release/openpipestress_units \
  $WT/tools/t3_slot.sh env PYTHONDONTWRITEBYTECODE=1 $WT/venv/bin/python -m pytest -v -p no:cacheprovider --basetemp=$TMPDIR/pt_$TAG \
    tests/test_retained_precision_contract.py tests/test_retained_precision_carriers.py tests/test_retained_precision_schema.py \
    tests/test_load_reference_source_schema.py tests/test_load_reference_schema.py tests/test_analysis_run_schema.py \
    tests/test_analysis_run_compatibility.py tests/test_analysis_run_records.py tests/test_results_dispatcher_v0_3.py \
    tests/test_source_block_schema_contract.py tests/test_stress_neutral_physics_source.py tests/test_stress_neutral_precision.py \
    tests/test_preview_physics_consumer_contract.py tests/test_physics_consumer_contract.py tests/test_precision_consumer_contract.py \
    tests/test_load_reference_readers.py tests/test_load_reference_source_readers.py \
    > "$O/py.log" 2>&1; note py $? ;;
ts)
  cmp "$P/package-lock.json" "$NMS/../package-lock.json" || { note ts_lock 5; continue; }
  ln -sfn "$NMS" "$P/node_modules"
  for d in self-weight-engine wasm-engine; do mkdir -p "$P/apps/desktop/public/$d"; cp "$WASM/$d/"* "$P/apps/desktop/public/$d/"; done
  (cd "$P/apps/desktop/public" && shasum -a 256 self-weight-engine/* wasm-engine/*) > "$O/ts_wasm_assets.sha256"
  (cd "$P/apps/desktop" && $WT/tools/t3_slot.sh npx vitest run --reporter=verbose \
    src/features/results src/features/stress-neutral src/features/result-export \
    src/services/analysisRunCompatibility.test.ts src/services/retainedPrecisionAnalysisRun.test.ts) > "$O/ts.log" 2>&1; rc=$?
  rm "$P/node_modules"; note ts $rc ;;
esac; done
echo "DONE $TAG $(date -u +%FT%TZ)" >> "$O/meta.txt"
