#!/bin/bash
# I104 SQ step 0 (tool sanity): I82's b1_text_base.sh retargeted to I104's scratch and to a given snapshot
# and mapping target. Copies u4_g7_06's chain, carries its line-keyed rules from Pass A with g7_linemap.py
# (or I104's crate-filtered copy), regenerates the template inventory and runs run_text_part2.sh.
# Usage: text_base.sh <snap dir> <map-to rev> <tag> [linemap script]
set -euo pipefail
T=${I104_WT:?set I104_WT to WT}; S=$T/scratch/i104_b1_sq; SNAP=$1; MAP_TO=$2; TAG=$3
R0=$T/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30
REC=$R0/I65/u4_g7_06/_run_records
LM=${4:-$REC/g7_linemap.py}
PASS_A=ba1faa1c858ce3630a22767677310b1902a14b83
export GIT_OPTIONAL_LOCKS=0 TMPDIR=$S/tmp PATH=$T/venv/bin:$PATH
W=$SNAP/projects/chirality-piping; RR=$S/rr_$TAG; O=$S/base_$TAG
rm -rf $RR $O $S/rules_$TAG; mkdir -p $RR $O $S/rules_$TAG
cp $REC/chain/* $RR/
set +e
python3 $LM $T/numerics $PASS_A $MAP_TO $S/rules_$TAG $REC/chain/callgraph_rules.g4.json $REC/chain/loop_bounds.g4.json $REC/chain/text_args.g4.json $REC/chain/sens.py $REC/premise_pins.json > $S/linemap_$TAG.out.json
echo "linemap exit $?"
set -e
cp $S/rules_$TAG/callgraph_rules.g4.json $S/rules_$TAG/loop_bounds.g4.json $S/rules_$TAG/text_args.g4.json $S/rules_$TAG/sens.py $RR/
python3 - $W $REC/chain/crate_dirs.txt $RR <<'PY'
import os, sys, subprocess
W, crates, RR = sys.argv[1:4]
files = []
for c in open(crates).read().split():
    for d, _, fs in os.walk(os.path.join(W, c)):
        if "/tests" in d or "/bin" in d: continue
        files += [os.path.relpath(os.path.join(d, f), W) for f in fs if f.endswith(".rs") and not f.endswith("_tests.rs") and f != "tests.rs"]
out = subprocess.run(["python3", RR + "/template_inventory.py", "."] + sorted(files), cwd=W, capture_output=True, text=True, check=True).stdout
open(RR + "/template_inventory_head.out.json", "w").write(out)
PY
set +e
( cd $W && bash $RR/run_text_part2.sh $TAG $O > $O/text.log 2>&1 ); echo "text chain exit $?"
set -e
A=$R0/I65/u4_g7_01/_run_records/pass_a/text_g7
for f in composite_text.caps.json g4_caps.caps.eps2.out.json ordinary_caps.caps.out.json producer_caps.caps.out.json profile_tree.json t07_repair.caps.out.json t08_closure.caps.log t25_g4.caps.eps2.out.json text_budget.caps.out.json text_budget_W.caps.out.json text_budget_X.caps.out.json text_budget_env.caps.out.json; do
  cmp -s $A/$f $O/sens_$TAG/$f && echo "identical $f" || echo "DIFFERS $f"; done
cat $O/sens_$TAG.summary.json 2>/dev/null; echo
