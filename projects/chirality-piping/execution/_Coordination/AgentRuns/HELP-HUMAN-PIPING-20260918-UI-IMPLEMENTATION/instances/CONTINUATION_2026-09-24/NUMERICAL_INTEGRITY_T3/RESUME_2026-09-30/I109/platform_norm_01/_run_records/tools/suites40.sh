#!/bin/bash
# I109: CI's numerical cargo profile on one tree, as ROOT's run_suites_nff.sh (the 40 manifests from
# tools/release/check_release_readiness.py's discovery; `cargo test --no-fail-fast` per manifest; -j 8,
# RUST_TEST_THREADS=4), except that every cargo goes through WT/tools/t3_cargo.sh (--locked --offline),
# one manifest at a time, and nothing is fetched. Not a measurement: no timing or RSS is recorded.
# Usage: I109_WT=<WT> suites40.sh <tree holding projects/chirality-piping> <out dir> <target dir>
set -u
T=${I109_WT:?set I109_WT to WT}; TREE=$1; OUT=$2; TGT=$3
mkdir -p "$OUT"
export TMPDIR=$T/scratch/i109_norm/tmp CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=4
P=$TREE/projects/chirality-piping
cd "$P" || exit 1
"$T/venv/bin/python" - <<'PY' > "$OUT/manifests.txt"
import importlib.util, sys
from pathlib import Path
spec = importlib.util.spec_from_file_location('r', 'tools/release/check_release_readiness.py'); m = importlib.util.module_from_spec(spec); sys.modules['r'] = m; spec.loader.exec_module(m)
for p in m.discover_cargo_manifests(Path('.')): print(p)
PY
i=0
for mf in $(cat "$OUT/manifests.txt"); do
  pgrep -f memguard.sh >/dev/null || { echo "MEMGUARD NOT RUNNING"; exit 9; }
  log=$OUT/$(printf '%03d' $i)_$(echo "$mf" | tr '/' '_').log
  ( cd "$P/$(dirname "$mf")" && "$T/tools/t3_cargo.sh" test --locked --offline --no-fail-fast --manifest-path "$P/$mf" --target-dir "$TGT" ) > "$log" 2>&1; rc=$?
  pass=$(grep -E '^test result:' "$log" | awk '{s+=$4} END {print s+0}'); fail=$(grep -E '^test result:' "$log" | awk '{s+=$6} END {print s+0}'); ign=$(grep -E '^test result:' "$log" | awk '{s+=$8} END {print s+0}')
  echo "$rc passed=$pass failed=$fail ignored=$ign $mf" | tee -a "$OUT/summary.txt"
  i=$((i+1))
done
echo SUITES-DONE | tee -a "$OUT/summary.txt"
