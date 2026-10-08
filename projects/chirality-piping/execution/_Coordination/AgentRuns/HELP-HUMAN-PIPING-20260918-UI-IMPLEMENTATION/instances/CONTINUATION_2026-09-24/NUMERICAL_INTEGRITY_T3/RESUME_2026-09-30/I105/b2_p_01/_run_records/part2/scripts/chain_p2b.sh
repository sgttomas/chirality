#!/bin/bash
# I105 Part 2, after the mutant-kill commit: rerun the survivors on an archive of HEAD, then the suites
# (PP all targets, runner, deps, src-tauri check) on another archive of HEAD. One heavy job at a time.
# Usage: chain_p2b.sh <commit> <survivor ids...>
WT=WT
S=$WT/scratch/i105_b2_p
C=$1; shift
export TMPDIR=$S/tmp
mkdir -p $S/mut3 $S/p2head
git -C $WT/b2 archive $C projects/chirality-piping | tar -x -C $S/mut3
git -C $WT/b2 archive $C projects/chirality-piping | tar -x -C $S/p2head
echo "CHAIN-STEP archives $C $(date -u +%FT%TZ)" >> $S/runs/chain.log
# The lane-A proposal again (its doc comment was reworded after propcheck2), on 583fc758ee's archive.
(cd $S/propcheck2/projects/chirality-piping/core/product_physics && RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0 CARGO_INCREMENTAL=1 \
  CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=4 CARGO_TARGET_DIR=$WT/targets/i105-b2-p-mut \
  $WT/tools/t3_cargo.sh test --locked --offline --lib -- retained_memory::law_tests > $S/runs/propcheck2b.log 2>&1)
echo "CHAIN-STEP propcheck2b rc=$? $(date -u +%FT%TZ)" >> $S/runs/chain.log
python3 $S/mut_spec/p2.py $S/mut3/projects/chirality-piping/core/product_physics $S/mut_spec/p2.json > $S/runs/p2_spec_rerun.log 2>&1
python3 $S/bin/mutants.py $S/mut_spec/p2.json $S/mut3 $S/runs/mut_p2_rerun "$@" > $S/runs/mut_p2_rerun_driver.log 2>&1
echo "CHAIN-STEP mut_p2_rerun rc=$? $(date -u +%FT%TZ)" >> $S/runs/chain.log
$WT/tools/t3_slot.sh $WT/venv/bin/python -I $S/bin/readers_today_py.py $S/p2head/projects/chirality-piping \
  $S/p2head/projects/chirality-piping/fixtures/results/retained_precision_combination_successor_sparse_interactive.json \
  $S/p2head/projects/chirality-piping/fixtures/results/retained_precision_combination_successor_dense_scrutiny.json > $S/runs/readers_py.log 2>&1
echo "CHAIN-STEP readers_py rc=$? $(date -u +%FT%TZ)" >> $S/runs/chain.log
$S/bin/run_suites.sh $S/p2head p2head pp runner deps tauri
echo "CHAIN-DONE p2b rc=$? $(date -u +%FT%TZ)" >> $S/runs/chain.log
