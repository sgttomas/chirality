#!/bin/bash
# RV120: RV113's 15 survivors at 6e3e4fe219 (12 S-1 plus 3 equivalent) and my 7, tests mode, one slot job each.
S=WT/scratch/rv120_rvr
read -r -a ids < $S/mutants/rs_ids_targeted.txt
echo "${#ids[@]} runs"
$S/tools/run_rs_mutants.sh tests "${ids[@]}"
