#!/bin/bash
# RV113: SR-PY repair 02's further mutants (P37-P40) on the tests, then the probe runs of the control and of every
# mutant not killed by an assertion (P02, P18, P31) and of P37-P40.
S=WT/scratch/rv113_rvr_01
$S/tools/run_py_mutants_r2.sh tests P37 P38 P39 P40
echo py-extra-tests-done
$S/tools/run_py_mutants_r2.sh probes NONE P02 P18 P31 P37 P38 P39 P40
echo py-probes-done
