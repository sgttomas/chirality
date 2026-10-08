#!/bin/bash
# RV124: I104's run_point.sh retargeted to RV124's scratch. Usage: run_point_rv.sh <chain dir> <out dir> '<G4_CAPS json>' <snapshot P dir>
set -euo pipefail
T=WT; CH=$1; O=$2; CAPS=$3; W=$4
export TMPDIR=$T/scratch/rv124_rvq/tmp PATH=$T/venv/bin:$PATH GIT_OPTIONAL_LOCKS=0
mkdir -p $O
ROOT=run_linear_static_preview_value_with_retained_direct
cd $W
env CG_REPAIR=1 CG_EXTRA_DEPS="core/product_physics:core/reporting/result_export" CG_RULES="$CH/callgraph_rules.g4.json" \
  CG_EDGES_OUT="$O/edges.json" CG_AUDIT_OUT="$O/audit.json" python3 "$CH/callgraph_g5.py" . "$O/cg.out.json" $ROOT $(cat "$CH/crate_dirs.txt") > /dev/null
python3 "$CH/text_lexicon.py" . "$O/edges.json" $ROOT "$O/lexicon.json" > /dev/null
set +e
python3 "$CH/sens.py" "$O/work" "$W" "$O/edges.json" "$O/lexicon.json" 2 "$CAPS" > "$O/summary.json" 2> "$O/sens.err"; rc=$?
set -e
echo "sens exit $rc"; cat "$O/summary.json"; echo
D=$(python3 -c "import json;print(json.load(open('$O/work/text_budget.caps.out.json'))['D_diagnostics'])")
python3 $T/scratch/rv124_rvq/bin/mk_looplog.py "$O/work/text_budget.py" "$O/work/text_budget_looplog.py"
( cd $W && env G4_CAPS="$CAPS" TB_LEXICON=$O/lexicon.json TB_COMPOSITE=$O/work/composite_text.caps.json TB_D=$D TB_LOOPLOG=$O/looplog.json \
  python3 $O/work/text_budget_looplog.py $W $O/work/template_inventory_head.out.json $O/edges.json $O/work/loop_bounds.g4.json $O/work/text_args.g4.json $ROOT caps > $O/looplog_tb.json )
python3 -c "
import json; t=json.load(open('$O/work/text_budget.caps.out.json'))
print('complete', t['complete'], 'D', t['D_diagnostics'], 'TAV', t['total_text_requested_bytes'])
print('unmapped', t['unmapped_loop_headers']); print('unclassified', t['unclassified_args']); print('selfrec', t['self_recursive_ancestors'])"
