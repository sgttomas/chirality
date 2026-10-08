#!/bin/bash
# I113 (B3a drop): a git-archive copy of P (without execution/) at a commit of WT/b2, for cargo, pytest and vitest jobs.
# Mode h: adds RV113's two census harnesses (from I101's scratch, sha256 pinned; never committed). Mode s: no harness.
# Both: links node_modules (after cmp of package-lock.json), creates an empty apps/desktop/node_modules in the copy
# (vite's temp and cache files stay in the copy), and copies the wasm assets (not built) from WT/sweep-skewpin.
# Usage: make_copy.sh <commit> <name> <h|s>
set -e
WT=WT
S=$WT/scratch/i113_b3a
NMS=APPWT/projects/chirality-piping/node_modules
SRC=$WT/sweep-skewpin/projects/chirality-piping/apps/desktop/public
H=$WT/scratch/i101_b3r/tools
commit=$1; name=$2; mode=$3
C=$S/copies/$name
rm -rf "$C"; mkdir -p "$C"
(cd "$WT/b2" && GIT_OPTIONAL_LOCKS=0 git archive --format=tar "$commit" -- projects/chirality-piping ':(exclude)projects/chirality-piping/execution') | tar -x -C "$C"
P=$C/projects/chirality-piping
if [ "$mode" = h ]; then
  (cd "$H" && shasum -a 256 -c "$S/tools/RV113_HARNESS.sha256")
  cp "$H/rv113_census.rs" "$P/core/reporting/result_export/tests/rv113_census.rs"
  cp "$H/rv113Census.test.ts" "$P/apps/desktop/src/features/results/rv113Census.test.ts"
fi
cmp "$P/package-lock.json" "$NMS/../package-lock.json"
ln -s "$NMS" "$P/node_modules"
mkdir "$P/apps/desktop/node_modules"
for d in self-weight-engine wasm-engine; do mkdir -p "$P/apps/desktop/public/$d"; cp "$SRC/$d/"* "$P/apps/desktop/public/$d/"; done
(cd "$P/apps/desktop/public" && shasum -a 256 self-weight-engine/* wasm-engine/*) > "$S/out/wasm_$name.sha256"
echo "$name ($mode): $(cd "$WT/b2" && GIT_OPTIONAL_LOCKS=0 git rev-parse "$commit"); package-lock equal; wasm assets copied"
