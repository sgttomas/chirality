#!/bin/bash
# RV120 B3: git-archive copies under WT/rv120b3/ (read-only Git; GIT_OPTIONAL_LOCKS=0) without execution/,
# with RV113's harnesses; TS copies get node_modules linked (after a package-lock cmp), their own
# apps/desktop/node_modules and the eight wasm assets.
set -e
export GIT_OPTIONAL_LOCKS=0
WT=WT
S=$WT/scratch/rv120_rvr
C=$WT/rv120b3
NMS=NMS
SRC=$WT/sweep-skewpin/projects/chirality-piping/apps/desktop/public
RE=projects/chirality-piping/core/reporting/result_export
mk() { rm -rf "$C/$1"; mkdir -p "$C/$1"; (cd "$WT/b2" && git archive --format=tar "$2" -- projects/chirality-piping ':(exclude)projects/chirality-piping/execution') | tar -x -C "$C/$1"; }
ts() {
  P=$C/$1/projects/chirality-piping
  cmp $P/package-lock.json $NMS/../package-lock.json
  ln -s $NMS $P/node_modules
  mkdir -p $P/apps/desktop/node_modules
  cp $S/tools/rv113Census.test.ts $P/apps/desktop/src/features/results/rv113Census.test.ts
  for d in self-weight-engine wasm-engine; do mkdir -p $P/apps/desktop/public/$d; cp $SRC/$d/* $P/apps/desktop/public/$d/; done
}
for spec in "base e67c3646808f19d61a77e77e8006dda723105243" "ts 77aaaa61d1e2354c5528cdeaaa7bbb4eeda0e76d" "py b7721d27e9e0e9850eb4ee6fffeca432ad9552e6" "rs c845e899da76cf6074543d4d5e1e81a995bf5054"; do
  set -- $spec; mk $1 $2; cp $S/tools/rv113_census.rs $C/$1/$RE/tests/rv113_census.rs
done
ts base; ts ts
ls -la $C/*/projects/chirality-piping | head -40
echo copies-done
