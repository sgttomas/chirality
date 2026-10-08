#!/bin/bash
# RV124: B1-site identifier-audit controls and QUAL §11's non-candidate sweep on RV124's own c = 3 N-5 point.
S=WT/scratch/rv124_rvq; WT=WT; LOG=$S/logs/chain_py2.log
export TMPDIR=$S/tmp PATH=$WT/venv/bin:$PATH
WAITPID=$1
echo "waiting for pid $WAITPID $(date -u +%FT%TZ)" >> $LOG
while kill -0 $WAITPID 2>/dev/null; do sleep 20; done
echo "start $(date -u +%FT%TZ)" >> $LOG
O=$S/chain/runs/n5_c3; W=$S/base/projects/chirality-piping
R0=$WT/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30
REC=$R0/I65/u4_g7_06/_run_records; REV87=$R0/REVIEW_RV87/u4_g6_02/_run_records/rv87_g6r_noncandidates.out.json
X=$R0/I104/b1_sq_01/_run_records/g6/tools
$WT/tools/t3_slot.sh /usr/bin/env TB_D_RUN=41769 G4_CAPS_RUN='{"l": 128, "c": 3}' python3 $S/bin/audit_controls_rv124.py $O/work $W $O/edges.json $O/lexicon.json $S/ana/audit_b1 > $S/logs/audit_b1.txt 2>&1
echo "audit controls rc=$? $(date -u +%FT%TZ)" >> $LOG
cd $W && $WT/tools/t3_slot.sh /usr/bin/env G4_CAPS='{"l": 128, "c": 3}' TB_LEXICON=$O/lexicon.json TB_COMPOSITE=$O/work/composite_text.caps.json TB_D=41769 TB_NONCAND_OUT=$S/ana/noncand.json \
  python3 $O/work/text_budget.py $W $O/work/template_inventory_head.out.json $O/edges.json $O/work/loop_bounds.g4.json $O/work/text_args.g4.json run_linear_static_preview_value_with_retained_direct caps > $S/ana/whole_nc.out.json 2>$S/logs/noncand.err
echo "noncand run rc=$? $(date -u +%FT%TZ)" >> $LOG
python3 $REC/noncand_compare.py $REV87 $S/ana/noncand.json > $S/ana/noncand_compare.out.json; echo "noncand_compare rc=$?" >> $LOG
python3 $X/noncand_compare_nomult.py $REV87 $S/ana/noncand.json > $S/ana/noncand_compare_nomult.out.json; echo "nomult rc=$?" >> $LOG
echo "CHAIN-DONE" >> $LOG
