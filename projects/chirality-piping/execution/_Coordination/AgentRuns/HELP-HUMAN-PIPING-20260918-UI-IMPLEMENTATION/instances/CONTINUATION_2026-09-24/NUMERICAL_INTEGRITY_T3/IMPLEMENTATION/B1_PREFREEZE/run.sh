#!/bin/bash
# ROOT's pre-freeze gates for B1 (PLAN_v2 §3.9): the full 40-manifest suite and the src-tauri suite,
# on the candidate (b1 0d19f995b5 + registration.diff, archived) and on its base (main 2007709549, archived).
WT=WT; O=$WT/scratch/root_b1_suite
T3R=$WT/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30
log() { echo "$* $(date -u +%FT%TZ)" >> $O/chain.txt; }
log start
for side in cand base; do
  A=$O/$side; rm -rf $A; mkdir -p $A
  if [ $side = cand ]; then c=0d19f995b5; else c=2007709549; fi
  git -C $WT/numerics archive $c | tar -x -C $A || { log "ARCHIVE-FAIL $side"; exit 1; }
  if [ $side = cand ]; then (cd $A && patch -p1 < $T3R/I104/b1_sq_01/registration.diff > $O/patch.txt 2>&1) || { log "PATCH-FAIL"; exit 1; }; fi
  echo "$side $c" >> $O/sides.txt
  $WT/tools/t3_slot.sh $WT/scratch/calib/run_suites_nff.sh $A $O/suites_$side $WT/targets/root-b1s-$side > $O/suites_$side.log 2>&1; log "suites-$side rc=$?"
  (cd $A/projects/chirality-piping/apps/desktop/src-tauri && RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0 CARGO_INCREMENTAL=0 CARGO_TARGET_DIR=$WT/targets/root-b1t-$side $WT/tools/t3_cargo.sh test --offline --locked --no-fail-fast > $O/srctauri_$side.log 2>&1); log "srctauri-$side rc=$?"
done
log CHAIN-DONE
