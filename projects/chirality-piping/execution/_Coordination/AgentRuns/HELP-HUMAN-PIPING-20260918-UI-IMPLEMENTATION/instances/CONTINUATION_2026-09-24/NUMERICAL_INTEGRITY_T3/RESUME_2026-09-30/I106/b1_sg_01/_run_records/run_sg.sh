#!/bin/bash
# I106 B1 SG: the Direct-entry gates (I61 u9_g8_01's method) on git-archive copies of the candidate
# (0d19f995b5 with R/I104/b1_sq_01/registration.diff applied) and of b1's base on main (2007709549),
# each registered and Stale. One cargo job of mine at a time, every one through WT/tools/t3_cargo.sh
# (--locked --offline); fresh targets WT/targets/i106-sg-<tree>-<build>. Stops at the first failure.
set -u
WT=WT; S=$WT/scratch/i106_b1_sg; LOG=$S/logs/chain.log
export TMPDIR=$S/tmp
run() { # <tree> <build> [extra env]
  local tree=$1 build=$2; shift 2
  echo "== $tree-$build start $(date -u +%FT%TZ)" >> $LOG
  ( cd $S/$tree/tree/projects/chirality-piping/core/product_physics && env -u RUSTFLAGS -u CARGO_ENCODED_RUSTFLAGS CARGO_BUILD_JOBS=4 RUST_TEST_THREADS=2 \
      I106_SG_SWEEP=$S/out/sweep_${tree}_${build}.tsv I106_SG_GATES_OUT=$S/out/gates_${tree}_${build}.json "$@" \
      perl -e 'alarm shift; exec @ARGV' 3600 $WT/tools/t3_cargo.sh test --locked --offline --lib --target-dir $WT/targets/i106-sg-$tree-$build zz_i106_ -- --ignored --nocapture \
      > $S/logs/${tree}_${build}.log 2>&1 )
  local rc=$?
  echo "== $tree-$build exit=$rc $(date -u +%FT%TZ)" >> $LOG
  grep -E "I106_SG_SWEEP|I106_SG_GATES_OUT|test result|^test " $S/logs/${tree}_${build}.log >> $LOG
  if [ $rc -ne 0 ]; then echo "CHAIN-FAIL $tree-$build rc=$rc $(date -u +%FT%TZ)" >> $LOG; exit $rc; fi
}
echo "chain start $(date -u +%FT%TZ)" >> $LOG
run cand reg
run cand stale RUSTFLAGS=--cfg=i106_sg_stale
run base reg
run base stale RUSTFLAGS=--cfg=i106_sg_stale
echo "CHAIN-DONE $(date -u +%FT%TZ)" >> $LOG
