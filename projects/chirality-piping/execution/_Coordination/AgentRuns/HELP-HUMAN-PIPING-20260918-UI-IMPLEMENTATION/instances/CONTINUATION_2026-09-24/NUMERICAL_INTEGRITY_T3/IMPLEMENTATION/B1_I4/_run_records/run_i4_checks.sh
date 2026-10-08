#!/bin/bash
# ROOT's check at I4 on b1 (merged tree). One heavy job at a time, each through the T3 lock wrappers.
WT=WT; O=$WT/scratch/root_i4; P=$WT/b1/projects/chirality-piping
export RUSTUP_TOOLCHAIN=1.97.1 RUSTUP_AUTO_INSTALL=0 CARGO_INCREMENTAL=0 CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=4 CARGO_TARGET_DIR=$WT/targets/root-i4
echo "head $(git -C $WT/b1 rev-parse HEAD) start $(date -u +%FT%TZ)" > $O/meta.txt
cd $P
$WT/tools/t3_cargo.sh test --locked --offline --manifest-path core/reporting/result_export/Cargo.toml > $O/rs_result_export.log 2>&1; echo "rs_result_export rc=$? $(date -u +%T)" >> $O/meta.txt
$WT/tools/t3_slot.sh env PYTHONDONTWRITEBYTECODE=1 $WT/venv/bin/python -m pytest -q -p no:cacheprovider tests/test_retained_precision_contract.py tests/test_retained_precision_carriers.py tests/test_retained_precision_schema.py > $O/py_readers.log 2>&1; echo "py_readers rc=$? $(date -u +%T)" >> $O/meta.txt
ln -s APPWT/projects/chirality-piping/node_modules $P/node_modules
(cd apps/desktop && $WT/tools/t3_slot.sh npx vitest run src/features/results/retainedPrecision.test.ts) > $O/ts_reader.log 2>&1; echo "ts_reader rc=$? $(date -u +%T)" >> $O/meta.txt
rm $P/node_modules
$WT/tools/t3_cargo.sh test --locked --offline --manifest-path core/product_physics/Cargo.toml --lib > $O/pp_lib.log 2>&1; echo "pp_lib rc=$? $(date -u +%T)" >> $O/meta.txt
echo "ALL-DONE $(date -u +%FT%TZ)" >> $O/meta.txt
