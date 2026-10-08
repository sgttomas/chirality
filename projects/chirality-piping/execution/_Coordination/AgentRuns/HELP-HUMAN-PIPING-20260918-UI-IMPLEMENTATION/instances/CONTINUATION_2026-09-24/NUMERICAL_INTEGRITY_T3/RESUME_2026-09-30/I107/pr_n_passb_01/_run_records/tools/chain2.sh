#!/bin/bash
# I107 PR-N: one chain, one job at a time: the loop count (item 4), then Pass B's run 2 (tag pn).
export TMPDIR=WT/scratch/i107_pn/tmp
WT=WT
$WT/tools/t3_slot.sh rustc --edition 2021 -O -o WT/scratch/i107_pn/loopcount/loopcount WT/scratch/i107_pn/loopcount/main.rs > WT/scratch/i107_pn/loopcount/build.log 2>&1; echo "build rc=$?" > WT/scratch/i107_pn/loopcount/chain.log
$WT/tools/t3_slot.sh WT/scratch/i107_pn/loopcount/loopcount WT/scratch/i107_pn/basis/projects/chirality-piping/core/solver/frame_kernel/tests/correct_norm_vectors.txt 20000000 > WT/scratch/i107_pn/loopcount/loopcount.out 2>&1; echo "run rc=$?" >> WT/scratch/i107_pn/loopcount/chain.log
echo "start $(date -u +%FT%TZ)" > WT/scratch/i107_pn/logs/pass_pn.log
I107_WT=$WT bash WT/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30/I107/pr_n_passb_01/_run_records/tools/pn_pass.sh WT/scratch/i107_pn/basis 8dd64c1835698da87e5f0fd303c1b886daee956f pn WT/scratch/i107_pn/main >> WT/scratch/i107_pn/logs/pass_pn.log 2>&1
echo "CHAIN-DONE rc=$? $(date -u +%FT%TZ)" >> WT/scratch/i107_pn/logs/pass_pn.log
