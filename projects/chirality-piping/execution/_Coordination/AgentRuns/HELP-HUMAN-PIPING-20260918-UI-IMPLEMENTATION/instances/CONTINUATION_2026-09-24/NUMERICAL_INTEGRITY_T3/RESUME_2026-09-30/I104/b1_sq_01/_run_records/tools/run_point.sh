#!/bin/bash
# I104 SQ G5: one TEXT + cap-priced point on the b1-q snapshot with a given chain copy (Python only).
# Call graph and lexicon from the chain's own callgraph rules, then sens.py at the cap vector, then (diagnostic)
# the loop log of the main text run at the converged D.
# Usage: run_point.sh <chain dir> <tag> '<G4_CAPS json>' [snapshot P dir]
set -euo pipefail
T=${I104_WT:?set I104_WT to WT}; S=$T/scratch/i104_b1_sq; CH=$1; TAG=$2; CAPS=$3
W=${4:-$S/snap_b1q/projects/chirality-piping}
export TMPDIR=$S/tmp PATH=$T/venv/bin:$PATH GIT_OPTIONAL_LOCKS=0
O=$S/${I104_RUNS:-runs}/$TAG; rm -rf $O; mkdir -p $O
ROOT=run_linear_static_preview_value_with_retained_direct
cd $W
env CG_REPAIR=1 CG_EXTRA_DEPS="core/product_physics:core/reporting/result_export" CG_RULES="$CH/callgraph_rules.g4.json" \
  CG_EDGES_OUT="$O/edges.json" CG_AUDIT_OUT="$O/audit.json" python3 "$CH/callgraph_g5.py" . "$O/cg.out.json" $ROOT $(cat "$CH/crate_dirs.txt") > /dev/null
python3 "$CH/text_lexicon.py" . "$O/edges.json" $ROOT "$O/lexicon.json" > /dev/null
set +e
python3 "$CH/sens.py" "$O/work" "$W" "$O/edges.json" "$O/lexicon.json" 2 "$CAPS" > "$O/summary.json" 2> "$O/sens.err"; rc=$?
set -e
echo "sens exit $rc"; cat "$O/summary.json"; echo
# diagnostic loop log at the run's D (the main variant)
D=$(python3 -c "import json;print(json.load(open('$O/work/text_budget.caps.out.json'))['D_diagnostics'])")
python3 $S/bin/mk_looplog.py "$O/work/text_budget.py" "$O/work/text_budget_looplog.py"
( cd $W && env G4_CAPS="$CAPS" TB_LEXICON=$O/lexicon.json TB_COMPOSITE=$O/work/composite_text.caps.json TB_D=$D TB_LOOPLOG=$O/looplog.json \
  python3 $O/work/text_budget_looplog.py $W $O/work/template_inventory_head.out.json $O/edges.json $O/work/loop_bounds.g4.json $O/work/text_args.g4.json $ROOT caps > $O/looplog_tb.json )
python3 -c "
import json; t=json.load(open('$O/work/text_budget.caps.out.json'))
print('complete', t['complete'], 'D', t['D_diagnostics'], 'TAV', t['total_text_requested_bytes'])
print('unmapped', t['unmapped_loop_headers']); print('unclassified', t['unclassified_args']); print('selfrec', t['self_recursive_ancestors'])"
