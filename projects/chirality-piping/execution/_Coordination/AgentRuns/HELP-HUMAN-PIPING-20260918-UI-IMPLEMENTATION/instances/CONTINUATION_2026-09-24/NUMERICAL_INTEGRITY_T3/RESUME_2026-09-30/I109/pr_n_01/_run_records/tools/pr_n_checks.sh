#!/bin/bash
# I109 round 2 (PR-N): the checks on the Mac for one branch revision, one heavy job at a time.
#   1. the affected crates' suites (PP, result_export) on a Git archive, fresh target;
#   2. the checked-JSON and units binaries for pytest, built through t3_cargo.sh;
#   3. the PY reader tests that read the corpus, and the TS reader test that reads it, from the worktree;
#   4. the 40 manifests (suites40.sh) on the archive, fresh target.
# Usage: I109_WT=<WT> pr_n_checks.sh <rev> <worktree> <out dir>
set -u
T=${I109_WT:?set I109_WT to WT}; REV=$1; WTREE=$2; O=$3; TL=$T/scratch/i109_norm/tools
mkdir -p "$O"; L=$O/chain.log; : > "$L"
export TMPDIR=$T/scratch/i109_norm/tmp CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=4 GIT_OPTIONAL_LOCKS=0
A=$O/tree; rm -rf "$A"; mkdir -p "$A"
git -C "$WTREE" archive "$REV" -- . ':(exclude)projects/chirality-piping/execution' | tar -x -C "$A" || { echo "ARCHIVE-FAIL" >> "$L"; exit 1; }
echo "archived $REV" >> "$L"
P=$A/projects/chirality-piping
for c in product_physics reporting/result_export; do
  pgrep -f memguard.sh >/dev/null || { echo "MEMGUARD NOT RUNNING" >> "$L"; exit 9; }
  n=$(basename $c)
  ( cd "$P/core/$c" && "$T/tools/t3_cargo.sh" test --locked --offline --no-fail-fast --target-dir "$T/targets/i109-n2-crates" ) > "$O/crate_$n.log" 2>&1
  echo "crate $n rc=$? $(grep -E '^test result:' "$O/crate_$n.log" | awk '{p+=$4; f+=$6; i+=$8} END {print "passed=" p " failed=" f " ignored=" i}')" >> "$L"
done
WP=$WTREE/projects/chirality-piping; BT=$T/targets/i109-n2-pybins
( cd "$WP/core/serialization/canonical_json" && "$T/tools/t3_cargo.sh" build --locked --offline --release --features checked-cli --bin openpipestress_jcs_ijson --target-dir "$BT" ) > "$O/pybins.log" 2>&1; echo "bin checked-json rc=$?" >> "$L"
( cd "$WP/core/units" && "$T/tools/t3_cargo.sh" build --locked --offline --release --features cli --bin openpipestress_units --target-dir "$BT" ) >> "$O/pybins.log" 2>&1; echo "bin units rc=$?" >> "$L"
( cd "$WP" && env OPENPIPESTRESS_CHECKED_JSON_BIN="$BT/release/openpipestress_jcs_ijson" OPENPIPESTRESS_UNITS_BIN="$BT/release/openpipestress_units" \
  "$T/tools/t3_slot.sh" "$T/venv/bin/python" -m pytest -q -p no:cacheprovider tests/test_retained_precision_contract.py tests/test_retained_precision_schema.py ) > "$O/pytest.log" 2>&1
echo "pytest rc=$? $(tail -1 "$O/pytest.log")" >> "$L"
( cd "$WP/apps/desktop" && "$T/tools/t3_slot.sh" npx vitest run src/features/results/retainedPrecision.test.ts ) > "$O/vitest.log" 2>&1
echo "vitest rc=$? $(grep -E 'Tests +[0-9]' "$O/vitest.log" | tail -1)" >> "$L"
"$TL/suites40.sh" "$A" "$O/suites" "$T/targets/i109-n2-suite" > "$O/suites.log" 2>&1; echo "suites40 rc=$?" >> "$L"
echo CHAIN-DONE >> "$L"
