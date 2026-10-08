#!/bin/bash
# I101: a git-archive copy of P (without execution/) at a commit, for RS's cargo jobs and TS's vitest jobs.
# Mode h: adds RV113's two census harnesses (never committed). Mode s: no harness (suite runs).
# Both: links node_modules (after cmp of package-lock.json), creates an empty apps/desktop/node_modules in the copy
# (so vite's temp and cache files stay in the copy, not in the linked tree), and copies the eight wasm assets
# (not built) from WT/sweep-skewpin. Usage: make_copy.sh <worktree> <commit> <name> <h|s>
set -e
WT=WT
S=$WT/scratch/i101_b1_i4p_rs_ts
NMS=APPWT/projects/chirality-piping/node_modules
SRC=$WT/sweep-skewpin/projects/chirality-piping/apps/desktop/public
wt=$1; commit=$2; name=$3; mode=$4
C=$S/copies/$name
rm -rf "$C"; mkdir -p "$C"
(cd "$WT/$wt" && GIT_OPTIONAL_LOCKS=0 git archive --format=tar "$commit" -- projects/chirality-piping ':(exclude)projects/chirality-piping/execution') | tar -x -C "$C"
P=$C/projects/chirality-piping
if [ "$mode" = h ]; then
  cp "$S/tools/rv113_census.rs" "$P/core/reporting/result_export/tests/rv113_census.rs"
  cp "$S/tools/rv113Census.test.ts" "$P/apps/desktop/src/features/results/rv113Census.test.ts"
fi
cmp "$P/package-lock.json" "$NMS/../package-lock.json"
ln -s "$NMS" "$P/node_modules"
mkdir "$P/apps/desktop/node_modules"
for d in self-weight-engine wasm-engine; do mkdir -p "$P/apps/desktop/public/$d"; cp "$SRC/$d/"* "$P/apps/desktop/public/$d/"; done
(cd "$P/apps/desktop/public" && shasum -a 256 self-weight-engine/* wasm-engine/*) > "$S/out/wasm_$name.sha256"
echo "$name ($mode): $(cd "$WT/$wt" && GIT_OPTIONAL_LOCKS=0 git rev-parse "$commit"); package-lock equal; wasm assets copied"
