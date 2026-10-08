#!/bin/bash
# Repair 01 confirmation (one heavy job, sequential): FK's suite at the repair head; the four mutants
# there; the RK-4 mutant at ef51a2d295 for contrast.
S=WT/scratch/rv121_rvk
$S/scripts/fk_suite.sh rep1
cd $S && PYTHONDONTWRITEBYTECODE=1 WT/venv/bin/python -I -B scripts/rv121_mutants_repair.py rep1 > logs/mutants_repair_rep1.log 2>&1
cd $S && PYTHONDONTWRITEBYTECODE=1 WT/venv/bin/python -I -B scripts/rv121_mutants_repair.py head rk4 > logs/mutants_repair_head_rk4.log 2>&1
