#!/bin/bash
S=WT/scratch/rv113_rvr_01
read -r -a ids < $S/tsr1/mutants/ids.txt
echo "${#ids[@]} runs"
$S/tools/run_ts_mutants_r1.sh tests "${ids[@]}"
$S/tools/run_ts_mutants_r1.sh probes NONE
echo ts-mutants-done
$S/tools/run_rsr2_extra.sh
