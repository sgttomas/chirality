#!/bin/bash
# RV124: re-run I65's delta_inventory2.py with I107's PR-N inputs, on the code commit (reproduction) and on the repair head.
set -u
T=WT
R0=$T/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30
REC=$R0/I65/u4_g7_06/_run_records; SQ=$R0/I104/b1_sq_01/_run_records; RB=$R0/I107/pr_n_passb_01/_run_records
IP=$T/scratch/i107_pn/pass_pn; S=$T/scratch/rv124_rvq/passb/delta; mkdir -p $S
export GIT_OPTIONAL_LOCKS=0 TMPDIR=$T/scratch/rv124_rvq/tmp
OLD=7eae707bb77722a69b61678c149aa816976bc162
run() { # run <tag> <rev> <tree>
  python3 $REC/delta_inventory2.py $T/numerics $OLD $2 $3 $SQ/chain/crate_dirs.txt $IP/n5/edges.json $IP/n5/work/loop_bounds.g4.json $RB/delta_reviewed_pn.json $S/$1.json > $S/$1.out.txt; echo "$1 exit=$?"; }
run code 8dd64c1835698da87e5f0fd303c1b886daee956f $IP/work/projects/chirality-piping
run repair $(git -C $T/numerics rev-parse 8ca80508b6) $T/scratch/rv124_rvq/passb/rep/projects/chirality-piping
