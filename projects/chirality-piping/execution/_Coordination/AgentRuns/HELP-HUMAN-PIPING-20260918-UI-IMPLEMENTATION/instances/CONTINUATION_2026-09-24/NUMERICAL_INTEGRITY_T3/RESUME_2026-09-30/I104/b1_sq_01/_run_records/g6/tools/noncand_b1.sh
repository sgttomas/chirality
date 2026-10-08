#!/bin/bash
# I104 SQ (PLAN_v2 §3.7; QUALIFICATION §11, RV87 G6r N-1): RV87's by-type non-candidate sweep on B1's
# c = 3 TEXT point (runs_n5/g5_c3: the N-5 chain on the b1-q snapshot), with I65's noncand_compare.py.
set -uo pipefail
T=WT; S=$T/scratch/i104_b1_sq; O=$S/runs_n5/g5_c3; W=$S/snap_b1q/projects/chirality-piping
R0=$T/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30
REV87=$R0/REVIEW_RV87/u4_g6_02/_run_records/rv87_g6r_noncandidates.out.json
REC=$R0/I65/u4_g7_06/_run_records
export TMPDIR=$S/tmp PATH=$T/venv/bin:$PATH
D=$(python3 -c "import json;print(json.load(open('$O/work/text_budget.caps.out.json'))['D_diagnostics'])")
( cd $W && env G4_CAPS='{"l": 128, "c": 3}' TB_LEXICON=$O/lexicon.json TB_COMPOSITE=$O/work/composite_text.caps.json TB_D=$D TB_NONCAND_OUT=$O/noncand.json \
  python3 $O/work/text_budget.py $W $O/work/template_inventory_head.out.json $O/edges.json $O/work/loop_bounds.g4.json $O/work/text_args.g4.json run_linear_static_preview_value_with_retained_direct caps > $O/whole_nc.out.json ); echo "noncand run exit $?"
python3 $REC/noncand_compare.py $REV87 $O/noncand.json > $O/noncand_compare.out.json; echo "noncand compare exit $?"
python3 -c "
import json; d=json.load(open('$O/noncand_compare.out.json')); print(d['verdict'], 'rv87', d['rv87_rows'], 'run', d['run_rows'], 'new', len(d['new_noncandidates']), 'absent', len(d['rv87_rows_absent_now']))"
