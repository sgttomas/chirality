#!/bin/bash
# RV113: archive copies for confirming SR-TS repair 01 (6fa6a64658): the head, and the head for mutants.
set -e
WT=WT
S=$WT/scratch/rv113_rvr_01
NMS=NMS
SRC=$WT/sweep-skewpin/projects/chirality-piping/apps/desktop/public
mkdir -p $S/tsr1/static
for c in ts1-head ts1-mut; do
  mkdir -p $WT/rv113/$c
  (cd $WT/b1-t && GIT_OPTIONAL_LOCKS=0 git archive --format=tar 6fa6a64658f6e94c817d26e0cab28e5087b2cf01 -- projects/chirality-piping ':(exclude)projects/chirality-piping/execution') | tar -x -C $WT/rv113/$c
  TS=$WT/rv113/$c/projects/chirality-piping
  cp $S/tools/rv113Census.test.ts $TS/apps/desktop/src/features/results/rv113Census.test.ts
  ln -s $NMS $TS/node_modules
  for f in self-weight-engine/open_pipe_stress_self_weight_wasm.d.ts self-weight-engine/open_pipe_stress_self_weight_wasm.js self-weight-engine/open_pipe_stress_self_weight_wasm_bg.wasm self-weight-engine/open_pipe_stress_self_weight_wasm_bg.wasm.d.ts wasm-engine/open_pipe_stress_operation_applier.d.ts wasm-engine/open_pipe_stress_operation_applier.js wasm-engine/open_pipe_stress_operation_applier_bg.wasm wasm-engine/open_pipe_stress_operation_applier_bg.wasm.d.ts; do
    mkdir -p "$TS/apps/desktop/public/$(dirname $f)"; cp "$SRC/$f" "$TS/apps/desktop/public/$f"
  done
  (cd $TS/apps/desktop/public && shasum -a 256 self-weight-engine/* wasm-engine/* | sed 's#^\([0-9a-f]*\)  #\1  ./#') > $S/tsr1/static/wasm_$c.sha256
  diff <(sort $S/tsr1/static/wasm_$c.sha256) <(sort $S/rsr2/static/wasm_assets.sha256) && echo "$c wasm: I71's eight"
done
RT=projects/chirality-piping/apps/desktop/src/features/results
{ cd $WT/b1-t; for f in $RT/retainedPrecision.ts $RT/retainedPrecision.test.ts $RT/previewPhysicsEvidence.ts; do echo "$(GIT_OPTIONAL_LOCKS=0 git show 6fa6a64658:$f | shasum -a 256 | cut -c1-64) $(shasum -a 256 $WT/rv113/ts1-head/$f | cut -c1-64) $f"; done
  echo "files changed 7e47e51b5d..6fa6a64658:"; GIT_OPTIONAL_LOCKS=0 git diff --name-only 7e47e51b5d 6fa6a64658; } > $S/tsr1/static/copies.txt
cat $S/tsr1/static/copies.txt
