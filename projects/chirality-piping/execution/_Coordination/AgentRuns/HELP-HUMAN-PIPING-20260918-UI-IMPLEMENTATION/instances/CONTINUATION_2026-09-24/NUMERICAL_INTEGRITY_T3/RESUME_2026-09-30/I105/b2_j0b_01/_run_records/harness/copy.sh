#!/bin/bash
# I105 J0b: a git-archive copy of P (without execution/) at a commit of WT/b2, after I101's make_copy.sh: node_modules
# linked after a cmp of package-lock.json, an empty apps/desktop/node_modules (vite's cache stays in the copy), and the
# eight wasm assets copied (not built) from WT/sweep-skewpin. Usage: copy.sh <commit> <name>
set -e
WT=WT
S=$WT/scratch/i105_j0b
NMS=APPWT/projects/chirality-piping/node_modules
SRC=$WT/sweep-skewpin/projects/chirality-piping/apps/desktop/public
commit=$1; name=$2; C=$S/copies/$name
rm -rf "$C"; mkdir -p "$C"
(cd "$WT/b2-j0b" && GIT_OPTIONAL_LOCKS=0 git archive --format=tar "$commit" -- projects/chirality-piping ':(exclude)projects/chirality-piping/execution') | tar -x -C "$C"
P=$C/projects/chirality-piping
cmp "$P/package-lock.json" "$NMS/../package-lock.json"
ln -s "$NMS" "$P/node_modules"
mkdir "$P/apps/desktop/node_modules"
for d in self-weight-engine wasm-engine; do mkdir -p "$P/apps/desktop/public/$d"; cp "$SRC/$d/"* "$P/apps/desktop/public/$d/"; done
(cd "$P/apps/desktop/public" && shasum -a 256 self-weight-engine/* wasm-engine/*) > "$S/out/wasm_$name.sha256"
echo "$name: $(cd "$WT/b2-j0b" && GIT_OPTIONAL_LOCKS=0 git rev-parse "$commit"); package-lock equal; wasm assets copied"
