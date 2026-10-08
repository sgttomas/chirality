#!/bin/bash
# RV123 round 2, repair 02 (cf607a02cd): the registered PP suite, M2-03 against the new pin, the runner.
WT=WT
S2=$WT/scratch/rv123_rvp2/r2
J=$S2/tools/runjob.sh
PY=$WT/venv/bin/python
$J rep2_pp_reg $WT/rv123/rep2/projects/chirality-piping/core/product_physics rv123-r2-rep2 0 test --locked --offline --no-fail-fast
F=$WT/rv123/rep2m/projects/chirality-piping/core/product_physics/src/retained_product.rs
$PY -I - "$F" <<'PY'
import sys
p=sys.argv[1]; s=open(p).read()
old='if matches!(&run.outcome, k::ExecutionOutcome::Refused { refusal: k::Refusal::LedgerUnavailable(_), .. }) {'
assert s.count(old)==1
open(p,'w').write(s.replace(old,'if false {'))
PY
$J rep2_m203 $WT/rv123/rep2m/projects/chirality-piping/core/product_physics rv123-r2-rep2m 0 test --locked --offline --no-fail-fast --lib -- b2p_ledger_unavailable_operand_has_no_source b2p_hooks_and_failure_set b2p_rv123_n3_shapes_are_pinned --test-threads=2
$J rep2_runner $WT/rv123/rep2/projects/chirality-piping/core/runner/headless rv123-r2-runner-rep2 0 test --locked --offline --no-fail-fast
echo "CHAIN-DONE phaseR2 $(date -u '+%FT%TZ')" >> $S2/logs/chain.log
