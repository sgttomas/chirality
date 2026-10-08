#!/bin/bash
# I109 round 2 (PR-N): the corpus readers on the worktree, after the cargo checks.
#   1. the TS suite's prerequisite, the wasm operation engine, built as apps/desktop's
#      scripts/build-wasm-engine.mjs builds it (operation_applier, wasm32, --features wasm,
#      --release; wasm-bindgen --target web into public/wasm-engine), with cargo through t3_cargo.sh;
#   2. the TS reader test that reads the corpus (vitest), through t3_slot.sh;
#   3. the PY reader tests that read the corpus (pytest), with the binaries pr_n_checks.sh built.
# Usage: I109_WT=<WT> pr_n_readers.sh <worktree> <out dir>
set -u
T=${I109_WT:?set I109_WT to WT}; WTREE=$1; O=$2; mkdir -p "$O"; L=$O/readers.log; : > "$L"
export TMPDIR=$T/scratch/i109_norm/tmp CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8
WP=$WTREE/projects/chirality-piping; WT_WASM=$T/targets/i109-n2-wasm; BT=$T/targets/i109-n2-pybins
( cd "$WP/core/model_operations/operation_applier" && "$T/tools/t3_cargo.sh" build --locked --offline --target wasm32-unknown-unknown --features wasm --release --target-dir "$WT_WASM" ) > "$O/wasm_build.log" 2>&1
echo "wasm cargo rc=$?" >> "$L"
ART=$WT_WASM/wasm32-unknown-unknown/release/open_pipe_stress_operation_applier.wasm
rm -rf "$WP/apps/desktop/public/wasm-engine"
wasm-bindgen --target web --out-dir "$WP/apps/desktop/public/wasm-engine" "$ART" >> "$O/wasm_build.log" 2>&1; echo "wasm-bindgen rc=$?" >> "$L"
( cd "$WP/apps/desktop" && "$T/tools/t3_slot.sh" npx vitest run src/features/results/retainedPrecision.test.ts ) > "$O/vitest.log" 2>&1
echo "vitest rc=$? $(grep -E 'Tests +[0-9]' "$O/vitest.log" | tail -1)" >> "$L"
( cd "$WP" && env OPENPIPESTRESS_CHECKED_JSON_BIN="$BT/release/openpipestress_jcs_ijson" OPENPIPESTRESS_UNITS_BIN="$BT/release/openpipestress_units" \
  "$T/tools/t3_slot.sh" "$T/venv/bin/python" -m pytest -q -p no:cacheprovider tests/test_retained_precision_contract.py tests/test_retained_precision_schema.py ) > "$O/pytest.log" 2>&1
echo "pytest rc=$? $(tail -1 "$O/pytest.log")" >> "$L"
echo CHAIN-DONE >> "$L"
