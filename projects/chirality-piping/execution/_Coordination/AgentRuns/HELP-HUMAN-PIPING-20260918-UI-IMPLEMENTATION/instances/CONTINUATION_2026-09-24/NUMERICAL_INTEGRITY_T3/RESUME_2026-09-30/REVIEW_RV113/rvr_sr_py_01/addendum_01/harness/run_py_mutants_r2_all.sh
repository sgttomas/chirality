#!/bin/bash
# RV113: SR-PY repair 02's mutant chain (bash, so the ids split): the tests for NONE and P01-P36.
S=WT/scratch/rv113_rvr_01
read -r -a ids < $S/pyr2/mutants/ids.txt
echo "${#ids[@]} runs"
$S/tools/run_py_mutants_r2.sh tests "${ids[@]}"
echo py-mutants-tests-done
