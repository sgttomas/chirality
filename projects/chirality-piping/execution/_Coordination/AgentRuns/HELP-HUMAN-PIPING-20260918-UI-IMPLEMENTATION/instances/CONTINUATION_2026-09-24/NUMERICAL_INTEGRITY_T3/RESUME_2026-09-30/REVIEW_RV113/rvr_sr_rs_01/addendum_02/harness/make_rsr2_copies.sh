#!/bin/bash
# RV113: archive copies for confirming SR-RS repair 02 (git archive, read-only; P without execution/).
set -e
WT=WT
S=$WT/scratch/rv113_rvr_01
mk() { mkdir -p "$3"; (cd "$WT/$1" && GIT_OPTIONAL_LOCKS=0 git archive --format=tar "$2" -- projects/chirality-piping ':(exclude)projects/chirality-piping/execution') | tar -x -C "$3"; }
mk b1-r 6e3e4fe219733652e38c3878f6c63de8acbd9a40 $WT/rv113/rs2-head
mk b1-r 6e3e4fe219733652e38c3878f6c63de8acbd9a40 $WT/rv113/rs2-mut
mk b1-p 11cc14e3e65363790f43943b09933a57f4da28e4 $WT/rv113/py-cmp
mk b1-t 7e47e51b5d935fda7a8289d14b21f8979e4f4876 $WT/rv113/ts-cmp
for c in rs2-head rs2-mut; do cp $S/tools/rv113_census.rs $WT/rv113/$c/projects/chirality-piping/core/reporting/result_export/tests/rv113_census.rs; done
TS=$WT/rv113/ts-cmp/projects/chirality-piping
cp $S/tools/rv113Census.test.ts $TS/apps/desktop/src/features/results/rv113Census.test.ts
ln -s NMS $TS/node_modules
SRC=$WT/sweep-skewpin/projects/chirality-piping/apps/desktop/public
for f in self-weight-engine/open_pipe_stress_self_weight_wasm.d.ts self-weight-engine/open_pipe_stress_self_weight_wasm.js self-weight-engine/open_pipe_stress_self_weight_wasm_bg.wasm self-weight-engine/open_pipe_stress_self_weight_wasm_bg.wasm.d.ts wasm-engine/open_pipe_stress_operation_applier.d.ts wasm-engine/open_pipe_stress_operation_applier.js wasm-engine/open_pipe_stress_operation_applier_bg.wasm wasm-engine/open_pipe_stress_operation_applier_bg.wasm.d.ts; do
  mkdir -p "$TS/apps/desktop/public/$(dirname $f)"; cp "$SRC/$f" "$TS/apps/desktop/public/$f"
done
(cd $TS/apps/desktop/public && shasum -a 256 self-weight-engine/* wasm-engine/* | sed 's#^\([0-9a-f]*\)  #\1  ./#') > $S/rsr2/static/wasm_assets.sha256
diff <(sort $S/rsr2/static/wasm_assets.sha256) <(sort $WT/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30/REVIEW_RV113/rvr_sr_ts_01/evidence/host/wasm_assets.sha256) && echo "wasm: I71's eight"
RE=projects/chirality-piping/core/reporting/result_export
{ cd $WT/b1-r; for f in $RE/src/retained_precision.rs $RE/tests/retained_precision_contract.rs; do echo "$(GIT_OPTIONAL_LOCKS=0 git show 6e3e4fe219:$f | shasum -a 256 | cut -c1-64) $(shasum -a 256 $WT/rv113/rs2-head/$f | cut -c1-64) $f"; done; echo "src files changed b5cb7faaeb..6e3e4fe219:"; GIT_OPTIONAL_LOCKS=0 git diff --name-only b5cb7faaeb 6e3e4fe219; } > $S/rsr2/static/copies.txt
cat $S/rsr2/static/copies.txt
