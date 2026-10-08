#!/bin/bash
# I110 round 2 evidence: src-tauri cargo tests, P/tests pytest, wasm build and vitest, at one tree.
# Usage: app_py_chain.sh <tree> <label>
set -u
WT=WT; S=$WT/scratch/i110_pret; TREE=$1; L=$2
export TMPDIR=$S/tmp
P=$TREE/projects/chirality-piping
echo "# start $(date -u +%FT%TZ) $L $(GIT_OPTIONAL_LOCKS=0 git -C $TREE rev-parse --short=10 HEAD)"
( cd $P/apps/desktop/src-tauri && $WT/tools/t3_cargo.sh test --locked --offline --no-fail-fast --target-dir $WT/targets/i110-tauri-$L ) > $S/ev/tauri_$L.log 2>&1; echo "tauri rc=$?"
( cd $P && $WT/tools/t3_slot.sh $WT/venv/bin/python -m pytest -q -rA -p no:cacheprovider tests ) > $S/ev/pytest_$L.log 2>&1; echo "pytest rc=$?"
( cd $P && CARGO_TARGET_DIR=$WT/targets/i110-wasm-$L $WT/tools/t3_slot.sh npm run build:wasm:desktop ) > $S/ev/wasm_$L.log 2>&1; echo "wasm rc=$?"
( cd $P/apps/desktop && $WT/tools/t3_slot.sh npx vitest run --reporter=json --outputFile=$S/ev/vitest_$L.json ) > $S/ev/vitest_$L.log 2>&1; echo "vitest rc=$?"
echo "# end $(date -u +%FT%TZ)"
