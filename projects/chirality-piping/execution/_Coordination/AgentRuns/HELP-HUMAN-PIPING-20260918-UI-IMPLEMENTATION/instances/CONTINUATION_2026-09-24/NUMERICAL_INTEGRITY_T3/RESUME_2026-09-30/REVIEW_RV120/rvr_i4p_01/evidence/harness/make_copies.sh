#!/bin/bash
# RV120: git-archive copies of P without execution/ (read-only Git; GIT_OPTIONAL_LOCKS=0), the reviewer harnesses
# copied in, and for TS the node_modules link (after a package-lock cmp) and the eight wasm assets.
set -e
export GIT_OPTIONAL_LOCKS=0
WT=WT
S=$WT/scratch/rv120_rvr
C=$S/copies
NMS=NMS
SRC=$WT/sweep-skewpin/projects/chirality-piping/apps/desktop/public
RE=projects/chirality-piping/core/reporting/result_export
RT=projects/chirality-piping/apps/desktop/src/features/results
mk() { rm -rf "$C/$2"; mkdir -p "$C/$2"; (cd "$WT/$1" && git archive --format=tar "$3" -- projects/chirality-piping ':(exclude)projects/chirality-piping/execution') | tar -x -C "$C/$2"; }
I4=30f3d1b24a271f6e407ee23814621087e249f879
RSH=e8791183483af1ba7b33032b022b5458fb97b6b6
TSH=819e44f63e39e01de46b593945cbcb14f0d4e65c
mk b1-r rs-i4 $I4; mk b1-r rs-head $RSH; mk b1-r rs-mut $RSH
mk b1-t ts-i4 $I4; mk b1-t ts-head $TSH; mk b1-t ts-mut $TSH
for c in rs-i4 rs-head rs-mut; do cp $S/tools/rv113_census.rs $C/$c/$RE/tests/rv113_census.rs; done
: > $S/static/wasm.sha256
for c in ts-i4 ts-head ts-mut; do
  P=$C/$c/projects/chirality-piping
  cmp $P/package-lock.json $NMS/../package-lock.json
  ln -s $NMS $P/node_modules
  cp $S/tools/rv113Census.test.ts $P/apps/desktop/src/features/results/rv113Census.test.ts
  for d in self-weight-engine wasm-engine; do mkdir -p $P/apps/desktop/public/$d; cp $SRC/$d/* $P/apps/desktop/public/$d/; done
  (cd $P/apps/desktop/public && shasum -a 256 self-weight-engine/* wasm-engine/* | sed "s#^#$c #") >> $S/static/wasm.sha256
done
{ for spec in "b1-r rs-head $RSH $RE/src/retained_precision.rs" "b1-r rs-head $RSH $RE/tests/retained_precision_contract.rs" \
              "b1-r rs-i4 $I4 $RE/src/retained_precision.rs" \
              "b1-t ts-head $TSH $RT/previewPhysicsEvidence.ts" "b1-t ts-head $TSH $RT/previewPhysicsEvidence.test.ts" \
              "b1-t ts-head $TSH $RT/retainedPrecision.ts" "b1-t ts-head $TSH $RT/retainedPrecision.test.ts" \
              "b1-t ts-i4 $I4 $RT/previewPhysicsEvidence.ts"; do
    set -- $spec
    echo "$(cd $WT/$1 && git show $3:$4 | shasum -a 256 | cut -c1-64) $(shasum -a 256 $C/$2/$4 | cut -c1-64) $2 $4"
  done
  echo "files changed I4..RS head:"; (cd $WT/b1-r && git diff --name-only $I4 $RSH)
  echo "files changed I4..TS head:"; (cd $WT/b1-t && git diff --name-only $I4 $TSH)
} > $S/static/copies.txt
cat $S/static/copies.txt
echo copies-done
