#!/bin/bash
# I110 round 6: both demo recipe modes in a tree, every cargo call through t3_cargo.sh (shim). Usage: regen_shim.sh <tree> <label>
set -u
S=WT/scratch/i110_pret; TREE=$1; L=$2
export TMPDIR=$S/tmp CARGO_TARGET_DIR=WT/targets/i110-hb-dev I110_ORIG_PATH="$PATH"
export PATH="$S/r6/shim:$PATH"
cd $TREE/projects/chirality-piping || exit 2
command -v cargo
npm run generate:product-preview-mechanics > $S/ev6/regen_${L}_demo.out 2> $S/ev6/regen_${L}_demo.err; echo "demo rc=$?"
npm run generate:product-preview-mechanics -- --preview-physics-1 > $S/ev6/regen_${L}_pp1.out 2> $S/ev6/regen_${L}_pp1.err; echo "pp1 rc=$?"
GIT_OPTIONAL_LOCKS=0 git status --short
