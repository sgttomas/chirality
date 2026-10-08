#!/bin/bash
# K-13 / C01 cross-build witness: the same modules at J2k (p1x = p1 plus head's C01 witness) and at head.
S=WT/scratch/rv121_rvk
F="source_bridge_tests source_residual_tests product_final_case_tests product_certificate::tests combine::tests origins::tests"
$S/scripts/fk_filtered.sh p1x fk-p1x k13_p1x $F --nocapture --test-threads=1
$S/scripts/fk_filtered.sh head fk-head k13_head $F --nocapture --test-threads=1
