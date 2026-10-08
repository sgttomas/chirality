#!/bin/bash
# Batch 3 (one heavy job, sequential): J2k's acceptance (FK and PP at Part 1), then every other FK
# dependent's suite at head and at main, each in its own fresh target.
S=WT/scratch/rv121_rvk
$S/scripts/fk_suite.sh p1
$S/scripts/crate_suite.sh p1 core/product_physics test
$S/scripts/deps_suite.sh head
$S/scripts/deps_suite.sh main
