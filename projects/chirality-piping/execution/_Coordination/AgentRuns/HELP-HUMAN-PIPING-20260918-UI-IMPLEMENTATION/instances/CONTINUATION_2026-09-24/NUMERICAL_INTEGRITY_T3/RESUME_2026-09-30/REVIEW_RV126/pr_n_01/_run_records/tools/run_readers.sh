#!/bin/bash
# RV126: the corpus readers (PY, TS) on the archive copy of 8dd64c1835, after the crate chain.
#  1. pybins (checked-json, units) built from the archive through t3_cargo.sh;
#  2. pytest: the two PY files that read the corpus, through t3_slot.sh;
#  3. the wasm engine as build-wasm-engine.mjs builds it (cargo through t3_cargo.sh, wasm-bindgen 0.2.123);
#  4. node_modules: APFS clones of an existing T3 install with the identical package-lock.json (no install);
#  5. vitest: the four TS files that read the corpus, through t3_slot.sh.
set -u
WT=WT; S=$WT/scratch/rv126_n; P=$WT/rv126/projects/chirality-piping
export TMPDIR=$S/tmp CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8
L=$S/logs/readers_chain.log; : > "$L"
while ! grep -q CHAIN-DONE "$S/logs/crates_chain.log" 2>/dev/null; do sleep 20; done
BT=$WT/targets/rv126-pybins
( cd "$P/core/serialization/canonical_json" && "$WT/tools/t3_cargo.sh" build --locked --offline --release --features checked-cli --bin openpipestress_jcs_ijson --target-dir "$BT" ) > "$S/logs/pybins.log" 2>&1; echo "bin checked-json rc=$?" >> "$L"
( cd "$P/core/units" && "$WT/tools/t3_cargo.sh" build --locked --offline --release --features cli --bin openpipestress_units --target-dir "$BT" ) >> "$S/logs/pybins.log" 2>&1; echo "bin units rc=$?" >> "$L"
( cd "$P" && env PYTHONDONTWRITEBYTECODE=1 OPENPIPESTRESS_CHECKED_JSON_BIN="$BT/release/openpipestress_jcs_ijson" OPENPIPESTRESS_UNITS_BIN="$BT/release/openpipestress_units" \
  "$WT/tools/t3_slot.sh" "$WT/venv/bin/python" -m pytest -q -p no:cacheprovider --basetemp="$S/tmp/pytest" tests/test_retained_precision_contract.py tests/test_retained_precision_schema.py ) > "$S/logs/pytest.log" 2>&1
echo "pytest rc=$? $(tail -1 "$S/logs/pytest.log")" >> "$L"
WASM=$WT/targets/rv126-wasm
( cd "$P/core/model_operations/operation_applier" && "$WT/tools/t3_cargo.sh" build --locked --offline --target wasm32-unknown-unknown --features wasm --release --target-dir "$WASM" ) > "$S/logs/wasm_build.log" 2>&1
echo "wasm cargo rc=$?" >> "$L"
rm -rf "$P/apps/desktop/public/wasm-engine"
wasm-bindgen --version >> "$S/logs/wasm_build.log" 2>&1
wasm-bindgen --target web --out-dir "$P/apps/desktop/public/wasm-engine" "$WASM/wasm32-unknown-unknown/release/open_pipe_stress_operation_applier.wasm" >> "$S/logs/wasm_build.log" 2>&1; echo "wasm-bindgen rc=$?" >> "$L"
SRC=$WT/t3-norm/projects/chirality-piping
[ "$(shasum -a 256 < "$SRC/package-lock.json")" = "$(shasum -a 256 < "$P/package-lock.json")" ] || { echo "LOCK-MISMATCH" >> "$L"; exit 3; }
cp -cR "$SRC/node_modules" "$P/node_modules" && cp -cR "$SRC/apps/desktop/node_modules" "$P/apps/desktop/node_modules"; echo "node_modules clone rc=$?" >> "$L"
( cd "$P/apps/desktop" && "$WT/tools/t3_slot.sh" npx vitest run src/features/results/retainedPrecision.test.ts src/features/results/retainedPrecisionIntegration.test.tsx src/features/result-export/retainedPrecisionResultExport.test.tsx src/features/stress-neutral/retainedPrecisionStressNeutral.test.tsx ) > "$S/logs/vitest.log" 2>&1
echo "vitest rc=$? $(grep -E 'Tests +[0-9]' "$S/logs/vitest.log" | tail -1) $(grep -E 'Test Files' "$S/logs/vitest.log" | tail -1)" >> "$L"
echo CHAIN-DONE >> "$L"
