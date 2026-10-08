#!/bin/bash
# I100: on the final head (52d83da275): the census and probes, the suites, then the mutant runs; one slot job at a time.
S=WT/scratch/i100_b1_i4p_py
$S/tools/verdicts.sh final $S/final/projects/chirality-piping
$S/tools/suites.sh final $S/final/projects/chirality-piping
$S/tools/run_mutants.sh NONE M1 M2 M3 M4 M5 M6 M7 M8 M9 M10 PRE
echo chain done
