#!/bin/bash
# RV125 (RV-X of PR-B1): spot checks on a git-archive copy of the PR head (WT/rv125/cand). One heavy job of
# mine at a time, each through the T3 wrappers (cargo: t3_cargo.sh --locked --offline; others: t3_slot.sh).
# Targets WT/targets/rv125-*. Writes only WT/scratch/rv125_b1_x and the copy. Stops at the first failure.
set -u
WT=WT; S=$WT/scratch/rv125_b1_x; LOG=$S/logs/chain.log
P=$WT/rv125/cand/projects/chirality-piping
export TMPDIR=$S/tmp RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0 CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=2
step() { echo "== $1 start $(date -u +%FT%TZ)" >> $LOG; }
done_or_fail() { local name=$1 rc=$2; echo "== $name exit=$rc $(date -u +%FT%TZ)" >> $LOG; if [ $rc -ne 0 ]; then echo "CHAIN-FAIL $name rc=$rc $(date -u +%FT%TZ)" >> $LOG; exit $rc; fi; }
echo "chain start $(date -u +%FT%TZ)" >> $LOG
# 1. Registered build (debug, no RUSTFLAGS): the Direct entry's spot checks and the Rust reader.
step pp_reg
( cd $P/core/product_physics && env -u RUSTFLAGS -u CARGO_ENCODED_RUSTFLAGS RV125_OUT=$S/out/reg.json \
  perl -e 'alarm shift; exec @ARGV' 3600 $WT/tools/t3_cargo.sh test --locked --offline --lib --target-dir $WT/targets/rv125-reg zz_rv125_ -- --ignored --nocapture ) > $S/logs/pp_reg.log 2>&1
done_or_fail pp_reg $?
# 2. A Stale build (RUSTFLAGS changes the D-6 identity): the ordinary bytes.
step pp_stale
( cd $P/core/product_physics && env -u CARGO_ENCODED_RUSTFLAGS RUSTFLAGS=--cfg=rv125_stale RV125_OUT=$S/out/stale.json \
  perl -e 'alarm shift; exec @ARGV' 3600 $WT/tools/t3_cargo.sh test --locked --offline --lib --target-dir $WT/targets/rv125-stale zz_rv125_ -- --ignored --nocapture ) > $S/logs/pp_stale.log 2>&1
done_or_fail pp_stale $?
# 3. The Python reader's two authority binaries (unchanged by B1), built here.
step auth
( cd $P/core/serialization/canonical_json && env -u RUSTFLAGS $WT/tools/t3_cargo.sh build --locked --offline --release --features checked-cli --bin openpipestress_jcs_ijson --target-dir $WT/targets/rv125-auth ) > $S/logs/auth_cj.log 2>&1
rc=$?; [ $rc -eq 0 ] && ( cd $P/core/units && env -u RUSTFLAGS $WT/tools/t3_cargo.sh build --locked --offline --release --features cli --bin openpipestress_units --target-dir $WT/targets/rv125-auth ) > $S/logs/auth_units.log 2>&1
rc2=$?; [ $rc -eq 0 ] && rc=$rc2
done_or_fail auth $rc
# 4. The Python reader.
step py
rm -f $S/out/py.jsonl
( cd $P && $WT/tools/t3_slot.sh env PYTHONDONTWRITEBYTECODE=1 OPENPIPESTRESS_CHECKED_JSON_BIN=$WT/targets/rv125-auth/release/openpipestress_jcs_ijson \
  OPENPIPESTRESS_UNITS_BIN=$WT/targets/rv125-auth/release/openpipestress_units RV125_OUT=$S/out/reg.json RV125_PY_OUT=$S/out/py.jsonl \
  $WT/venv/bin/python -m pytest -q -p no:cacheprovider tests/test_zz_rv125_readers.py ) > $S/logs/py.log 2>&1
done_or_fail py $?
# 5. The TypeScript reader, as I92 and ROOT at I4 ran vitest: node_modules linked (package-lock equal), the eight
#    wasm assets copied from WT/sweep-skewpin.
step ts
NMS=$WT/sweep-skewpin/projects/chirality-piping/node_modules
SRC=$WT/sweep-skewpin/projects/chirality-piping/apps/desktop/public
cmp $P/package-lock.json $NMS/../package-lock.json || { echo "CHAIN-FAIL ts package-lock differs" >> $LOG; exit 5; }
ln -s $NMS $P/node_modules
mkdir -p $P/apps/desktop/node_modules   # vite writes its cache here, not into the linked tree (as RV120 did)
for d in self-weight-engine wasm-engine; do mkdir -p $P/apps/desktop/public/$d; cp $SRC/$d/* $P/apps/desktop/public/$d/; done
(cd $P/apps/desktop/public && shasum -a 256 self-weight-engine/* wasm-engine/*) > $S/out/ts_wasm_assets.sha256
rm -f $S/out/ts.jsonl
( cd $P/apps/desktop && $WT/tools/t3_slot.sh env RV125_OUT=$S/out/reg.json RV125_TS_OUT=$S/out/ts.jsonl npx vitest run src/features/results/zzRv125Readers.test.ts ) > $S/logs/ts.log 2>&1
rc=$?
rm $P/node_modules
done_or_fail ts $rc
echo "CHAIN-DONE $(date -u +%FT%TZ)" >> $LOG
