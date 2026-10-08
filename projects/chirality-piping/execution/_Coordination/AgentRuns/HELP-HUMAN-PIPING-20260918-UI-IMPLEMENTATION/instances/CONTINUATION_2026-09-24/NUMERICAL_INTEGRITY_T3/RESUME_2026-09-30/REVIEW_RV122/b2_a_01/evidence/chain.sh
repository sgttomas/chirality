#!/bin/bash
# RV122: after the base driver exits, run the rest sequentially (one heavy job at a time).
S=WT/scratch/rv122_rvq2
while kill -0 7054 2>/dev/null; do sleep 10; done
echo "base-done $(date -u +%FT%TZ)" >> $S/runs/chain.txt
$S/scripts/run_suites.sh $S/arch_head head re pp runner py ts; echo "head-done $(date -u +%FT%TZ)" >> $S/runs/chain.txt
$S/scripts/run_suites.sh $S/arch_b2a b2a pp runner; echo "b2a-done $(date -u +%FT%TZ)" >> $S/runs/chain.txt
$S/scripts/run_probes.sh; echo "probes-done $(date -u +%FT%TZ)" >> $S/runs/chain.txt
$S/scripts/run_mutants.sh; echo "mutants-done $(date -u +%FT%TZ)" >> $S/runs/chain.txt
echo "CHAIN-DONE $(date -u +%FT%TZ)" >> $S/runs/chain.txt
