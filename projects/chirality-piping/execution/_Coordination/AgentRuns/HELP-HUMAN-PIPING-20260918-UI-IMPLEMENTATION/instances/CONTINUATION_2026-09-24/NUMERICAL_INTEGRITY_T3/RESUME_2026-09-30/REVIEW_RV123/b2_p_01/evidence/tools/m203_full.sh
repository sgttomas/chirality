#!/bin/bash
# RV123 round 2: M2-03 against the whole product_physics lib suite (mut copy), then restore.
WT=WT
S2=$WT/scratch/rv123_rvp2/r2
M=$WT/rv123/mut/projects/chirality-piping/core/product_physics
F=$M/src/retained_product.rs
cp "$F" "$S2/tmp/retained_product.rs.orig"
WT/venv/bin/python -I - "$F" <<'PY'
import sys
p=sys.argv[1]; s=open(p).read()
old='if matches!(&run.outcome, k::ExecutionOutcome::Refused { refusal: k::Refusal::LedgerUnavailable(_), .. }) {'
assert s.count(old)==1
open(p,'w').write(s.replace(old,'if false {'))
PY
$S2/tools/runjob.sh m203_full $M rv123-r2-mut 0 test --locked --offline --no-fail-fast --lib -- --test-threads=2
cp "$S2/tmp/retained_product.rs.orig" "$F"
cmp -s "$F" "$WT/rv123/cand/projects/chirality-piping/core/product_physics/src/retained_product.rs" && echo "restored=identical-to-cand" >> $S2/logs/chain.log
echo "CHAIN-DONE m203_full $(date -u '+%FT%TZ')" >> $S2/logs/chain.log
