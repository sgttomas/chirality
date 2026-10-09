#!/bin/bash
# I105 (lane P): the suites, one heavy job at a time, each through the T3 slot wrappers.
# Usage: run_suites.sh <tree-root (holds projects/chirality-piping)> <tag> [parts...]
# parts: pp pplib runner deps re (default: pp runner deps). Logs: $S/runs/<tag>/<part>.log; rc in meta.txt.
set -u
WT=WT
S=$WT/scratch/i105_j0a
ROOT=$1; TAG=$2; shift 2
PARTS=${*:-pp runner deps}
P=$ROOT/projects/chirality-piping
O=$S/runs/$TAG; mkdir -p "$O" "$S/tmp"
export TMPDIR=$S/tmp RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0 CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=4
unset RUSTFLAGS CARGO_ENCODED_RUSTFLAGS
TG=$WT/targets/i105-j0a
note() { echo "$1 rc=$2 $(date -u +%FT%TZ)" >> "$O/meta.txt"; }
cd "$P" || exit 9
echo "START $TAG $(date -u +%FT%TZ) root=$ROOT parts=$PARTS" >> "$O/meta.txt"
for part in $PARTS; do case $part in
pp)
  CARGO_TARGET_DIR=$TG-pp $WT/tools/t3_cargo.sh test --locked --offline --no-fail-fast \
    --manifest-path core/product_physics/Cargo.toml > "$O/pp.log" 2>&1; note pp $? ;;
pplib)
  CARGO_TARGET_DIR=$TG-pp $WT/tools/t3_cargo.sh test --locked --offline --no-fail-fast \
    --manifest-path core/product_physics/Cargo.toml --lib --test retained_precision_admission --test s11f_site_test > "$O/pplib.log" 2>&1; note pplib $? ;;
runner)
  CARGO_TARGET_DIR=$TG-runner $WT/tools/t3_cargo.sh test --locked --offline --no-fail-fast \
    --manifest-path core/runner/headless/Cargo.toml > "$O/runner.log" 2>&1; note runner $? ;;
re)
  CARGO_TARGET_DIR=$TG-re $WT/tools/t3_cargo.sh test --locked --offline --no-fail-fast \
    --manifest-path core/reporting/result_export/Cargo.toml > "$O/re.log" 2>&1; note re $? ;;
deps)
  # PP's other dependents: compiled with all targets (their own lockfiles, own targets).
  for c in core/loads/self_weight_wasm core/model_operations/operation_applier; do
    n=$(basename $c)
    CARGO_TARGET_DIR=$TG-$n $WT/tools/t3_cargo.sh test --locked --offline --no-run --all-targets \
      --manifest-path $c/Cargo.toml > "$O/deps_$n.log" 2>&1; note deps_$n $?
  done ;;
tauri)
  CARGO_TARGET_DIR=$TG-tauri $WT/tools/t3_cargo.sh check --locked --offline --all-targets \
    --manifest-path apps/desktop/src-tauri/Cargo.toml > "$O/tauri.log" 2>&1; note tauri $? ;;
esac; done
echo "DONE $TAG $(date -u +%FT%TZ)" >> "$O/meta.txt"
