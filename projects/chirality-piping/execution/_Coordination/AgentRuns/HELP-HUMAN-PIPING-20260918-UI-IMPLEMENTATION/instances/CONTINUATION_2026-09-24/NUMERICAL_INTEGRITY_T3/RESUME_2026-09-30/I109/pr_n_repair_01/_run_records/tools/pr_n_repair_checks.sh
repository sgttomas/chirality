#!/bin/bash
# I109 round 4 (PR-N repair round 01): the checks on the Mac for one revision, one heavy job at a time,
# every cargo through WT/tools/t3_cargo.sh (--locked --offline), vitest and pytest through WT/tools/t3_slot.sh,
# fresh targets WT/targets/i109-n4-*.
#   1. the PP, FK and result_export suites on a Git archive of <rev>;
#   2. the checked-JSON and units binaries for pytest, from the archive;
#   3. the wasm operation engine from the archive (as apps/desktop's scripts/build-wasm-engine.mjs: operation_applier,
#      wasm32, --features wasm, --release; wasm-bindgen --target web into the worktree's ignored public/wasm-engine);
#   4. the four TS files that read the corpus (vitest) and the two PY files (pytest), from the worktree, whose
#      non-execution tree must equal <rev>.
# Usage: I109_WT=<WT> pr_n_repair_checks.sh <rev> <worktree> <out dir>
set -u
T=${I109_WT:?set I109_WT to WT}; REV=$1; WTREE=$2; O=$3
mkdir -p "$O"; L=$O/chain.log; : > "$L"
export TMPDIR=$T/scratch/i109_norm/tmp CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=4 GIT_OPTIONAL_LOCKS=0 PYTHONDONTWRITEBYTECODE=1
A=$O/tree; rm -rf "$A"; mkdir -p "$A"
git -C "$WTREE" archive "$REV" -- . ':(exclude)projects/chirality-piping/execution' | tar -x -C "$A" || { echo "ARCHIVE-FAIL" >> "$L"; exit 1; }
echo "archived $(git -C "$WTREE" rev-parse "$REV")" >> "$L"
P=$A/projects/chirality-piping
for c in product_physics solver/frame_kernel reporting/result_export; do
  pgrep -f memguard.sh >/dev/null || { echo "MEMGUARD NOT RUNNING" >> "$L"; exit 9; }
  n=$(basename $c)
  ( cd "$P/core/$c" && "$T/tools/t3_cargo.sh" test --locked --offline --no-fail-fast --target-dir "$T/targets/i109-n4-crates" ) > "$O/crate_$n.log" 2>&1
  echo "crate $n rc=$? $(grep -E '^test result:' "$O/crate_$n.log" | awk '{p+=$4; f+=$6; i+=$8} END {print "passed=" p " failed=" f " ignored=" i}')" >> "$L"
done
BT=$T/targets/i109-n4-pybins
( cd "$P/core/serialization/canonical_json" && "$T/tools/t3_cargo.sh" build --locked --offline --release --features checked-cli --bin openpipestress_jcs_ijson --target-dir "$BT" ) > "$O/pybins.log" 2>&1; echo "bin checked-json rc=$?" >> "$L"
( cd "$P/core/units" && "$T/tools/t3_cargo.sh" build --locked --offline --release --features cli --bin openpipestress_units --target-dir "$BT" ) >> "$O/pybins.log" 2>&1; echo "bin units rc=$?" >> "$L"
WW=$T/targets/i109-n4-wasm
( cd "$P/core/model_operations/operation_applier" && "$T/tools/t3_cargo.sh" build --locked --offline --target wasm32-unknown-unknown --features wasm --release --target-dir "$WW" ) > "$O/wasm_build.log" 2>&1
echo "wasm cargo rc=$?" >> "$L"
WP=$WTREE/projects/chirality-piping
git -C "$WTREE" diff --quiet "$REV" -- . ':(exclude)projects/chirality-piping/execution' && echo "worktree equals $REV outside execution" >> "$L" || { echo "WORKTREE-DIFFERS" >> "$L"; exit 3; }
rm -rf "$WP/apps/desktop/public/wasm-engine"
wasm-bindgen --target web --out-dir "$WP/apps/desktop/public/wasm-engine" "$WW/wasm32-unknown-unknown/release/open_pipe_stress_operation_applier.wasm" >> "$O/wasm_build.log" 2>&1; echo "wasm-bindgen rc=$?" >> "$L"
( cd "$WP/apps/desktop" && "$T/tools/t3_slot.sh" npx vitest run src/features/results/retainedPrecision.test.ts src/features/results/retainedPrecisionIntegration.test.tsx src/features/result-export/retainedPrecisionResultExport.test.tsx src/features/stress-neutral/retainedPrecisionStressNeutral.test.tsx ) > "$O/vitest.log" 2>&1
echo "vitest rc=$? $(grep -E 'Test Files +[0-9]' "$O/vitest.log" | tail -1) / $(grep -E 'Tests +[0-9]' "$O/vitest.log" | tail -1)" >> "$L"
( cd "$WP" && env OPENPIPESTRESS_CHECKED_JSON_BIN="$BT/release/openpipestress_jcs_ijson" OPENPIPESTRESS_UNITS_BIN="$BT/release/openpipestress_units" \
  "$T/tools/t3_slot.sh" "$T/venv/bin/python" -m pytest -q -p no:cacheprovider tests/test_retained_precision_contract.py tests/test_retained_precision_schema.py ) > "$O/pytest.log" 2>&1
echo "pytest rc=$? $(tail -1 "$O/pytest.log")" >> "$L"
echo CHAIN-DONE >> "$L"
