#!/bin/bash
# RV120 B3 repair 01: the Rust reader's G7 transport code on the two "extra exact_cases entry" probes, five fresh
# processes (RS physics_evidence iterates a HashMap of cases), then I100's PY note (py_bind_mutants.sh).
WT=WT; S=$WT/scratch/rv120_rvr; B3=$S/b3; export RV120_LOGDIR=$B3/logs; J=$S/tools/rv120_job.sh
P=$WT/rv120b3/probe2/projects/chirality-piping
for i in 1 2 3 4 5; do env RV120_IN=$B3/inputs/rs_det.jsonl RV120_OUT=$B3/probes/rs_det_$i.jsonl $J cargo rs_det_$i $P/core/reporting/result_export $WT/targets/rv120b3-probe2 test --locked --offline --test rv120_b3_raw; echo "rs_det_$i rc=$?"; done
$S/tools/b3/py_bind_mutants.sh
echo det-done
