#!/bin/bash
# ROOT's TS check at I4, as I92 ran vitest: a scratch archive of P without execution/, node_modules linked,
# the eight wasm assets copied (not built) from WT/sweep-skewpin. One slot job.
WT=WT; O=$WT/scratch/root_i4; A=$O/arch_ts
NMS=APPWT/projects/chirality-piping/node_modules
SRC=$WT/sweep-skewpin/projects/chirality-piping/apps/desktop/public
rm -rf "$A"; mkdir -p "$A"
git -C $WT/b1 archive HEAD projects/chirality-piping ':(exclude)projects/chirality-piping/execution' | tar -x -C "$A"
P=$A/projects/chirality-piping
cmp $P/package-lock.json $NMS/../package-lock.json || { echo "package-lock differs"; exit 5; }
ln -s $NMS $P/node_modules
for d in self-weight-engine wasm-engine; do mkdir -p $P/apps/desktop/public/$d; cp $SRC/$d/* $P/apps/desktop/public/$d/; done
(cd $P/apps/desktop/public && shasum -a 256 self-weight-engine/* wasm-engine/*) > $O/ts_wasm_assets.sha256
cd $P/apps/desktop
export TMPDIR=$O/tmp; mkdir -p $TMPDIR
$WT/tools/t3_slot.sh npx vitest run src/features/results/retainedPrecision.test.ts src/features/results/previewPhysicsEvidence.test.ts > $O/ts_reader2.log 2>&1; rc=$?
echo "ts_reader (archive) rc=$rc $(date -u +%T)" >> $O/meta.txt
rm $P/node_modules
exit $rc
