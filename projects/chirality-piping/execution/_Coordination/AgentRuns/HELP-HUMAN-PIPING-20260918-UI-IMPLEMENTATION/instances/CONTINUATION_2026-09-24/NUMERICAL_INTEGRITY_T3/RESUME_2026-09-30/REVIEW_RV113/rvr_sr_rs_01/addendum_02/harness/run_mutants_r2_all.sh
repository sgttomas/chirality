#!/bin/bash
S=WT/scratch/rv113_rvr_01
ids=(NONE $(python3 -c "import json;print(' '.join(m['id'] for m in json.load(open('$S/rsr2/mutants/MUTANTS_R2.json'))))"))
echo "${#ids[@]} runs"
"$S/tools/run_mutants_r2.sh" tests "${ids[@]}"
"$S/tools/run_mutants_r2.sh" probes NONE
echo done
