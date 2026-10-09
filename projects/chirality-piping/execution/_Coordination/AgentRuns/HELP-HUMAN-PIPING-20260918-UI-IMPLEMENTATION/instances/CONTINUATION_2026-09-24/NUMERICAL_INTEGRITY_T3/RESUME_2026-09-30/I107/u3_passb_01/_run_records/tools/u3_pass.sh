#!/bin/bash
# I107 SB round 3: Pass B on the U3 PR's code commit (R/BRIEFS/U3_SB.md), against main ba500defa4 (B1 + PR-N).
# A copy of round 2's pn_pass.sh (R/I107/pr_n_passb_01/_run_records/tools/), retargeted: constants, scratch, targets, tools;
# the line map's copy also handles deleted files, and rules keyed only to deleted lines are pruned (prune_deleted.py);
# TEXT is compared by text_u3.py (removals attributed to deleted code, additions to added code; N-5's call graph is
# counted against SQ's G5 graph carried by the line map, the same graph); the reviewed table is delta_reviewed_u3.json,
# built by mk_delta_reviewed_u3.py from a dry run's inventory. Three U3 readings sit beside the gates they read, each in
# the verdict under its own name (u3_checks.py): forms_u3 (the committed block over-prices the regeneration), noncand_u3
# (SQ's sweep less the rows on deleted lines) and controls_u3 (SQ's controls, TAV offsets from c0 equal). The gates
# they read stay in the verdict unchanged (noncand_sq, controls_sq).
# Round 2's header follows.
# I107 SB round 2: Pass B on PR-N's code commit (R/BRIEFS/PR_N_SB.md), against B1 as merged (main 7eae707bb7).
# A copy of round 1's b1_pass.sh (R/I107/b1_passb_01/_run_records/tools/), itself I72's g7_pass.sh retargeted to B1.
# Every gate, stop and the verdict logic are kept. What changes:
#   - the delta runs from main 7eae707bb7 (B1 as merged) to the basis, with this round's reviewed table;
#   - the entry is compared byte for byte with main's (B1's registration), and its code with b1 ddc8eaaf54's;
#   - TEXT is compared with SQ's points by text_pn.py: round 1's equalities, with the norm's added call-graph nodes,
#     edges, site loops and spans attributed (every other output byte-equal);
#   - the controls are SQ's, re-keyed by +2 in PP lib.rs (audit_controls_pn.py), compared with SQ's with line numbers
#     dropped (pn_checks.py controls_pn);
#   - the rules are still SQ's chain keyed to 57c92a7b33, carried to the basis by the line map (g7_linemap_crates_rows.py:
#     SQ's copy, which resolves a short `lib.rs:N` key made ambiguous by three changed lib.rs files to the one with a
#     TEXT row there at the basis, each resolution reported); TEXT, FORMS, the
#     non-candidates and the controls are still compared with SQ's points (B1's Pass A, which round 1 matched);
#   - PP's and the runner's outcomes are compared with the same suites on main's tree (run_cargo_pn.sh);
#   - the witnesses and the challenge are compared with SQ's tables, as in round 1.
# Usage: I107_WT=<WT> pn_pass.sh <basis dir holding projects/chirality-piping> <basis rev> <tag> <main tree dir>
#   I107_SKIP_CARGO=1 skips the law gate and item 5 (a dry run of the Python gates).
# Exit: I65's: 0 PASS; 2 tree; 3 entry/M/law; 4 rule line or premise pin edited; 5 a production hunk needs a
#   reviewed entry; 6 deltas to read; 9 memguard.
set -u
T=${I107_WT:?set I107_WT to WT}; BASIS=$1; REV=$2; TAG=$3; MAINW=$4
[[ "$TAG" =~ ^[A-Za-z0-9_]+$ ]] || { echo "tag must be [A-Za-z0-9_]+"; exit 1; }
R0=$T/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30
REC=$R0/I65/u4_g7_06/_run_records; SQ=$R0/I104/b1_sq_01/_run_records; RB=$R0/I107/u3_passb_01/_run_records
TOOLS=$RB/tools; CHK="python3 $R0/I107/b1_passb_01/_run_records/tools/b1_checks.py"   # round 1's checks, unchanged
REV87=$R0/REVIEW_RV87/u4_g6_02/_run_records/rv87_g6r_noncandidates.out.json
NUMREPO=$T/numerics; I65_PASS_A=ba1faa1c858ce3630a22767677310b1902a14b83
PASS_A_REV=57c92a7b3310229406733a7134e271c29bcc6978; G5_REV=b075c5c59f397ad1bf8a0ba6fdf3d50bf7145d21
APPLIED_REV=ddc8eaaf5496e8fc0f4d6b905b38cae1e9b88bd0; M=11_274_289_152   # b1 with SQ's registration.diff applied (R6b)
REGISTERED_REV=ba500defa498a454be182ed46db795fc3e04d627   # main: B1 + PR-N as merged, its registered entry
DELTA_OLD=ba500defa498a454be182ed46db795fc3e04d627        # the delta's base: main as merged
CAPS='{"l": 128, "c": 3}'; ROOT=run_linear_static_preview_value_with_retained_direct
O=$T/scratch/i107_u3/pass_$TAG; WK=$O/work; RR=$O/rr_g5; RN=$O/rr_n5
TGT=$T/targets/i107-u3-$TAG
export GIT_OPTIONAL_LOCKS=0 TMPDIR=$T/scratch/i107_u3/tmp PATH=$T/venv/bin:$PATH I107_WT=$T LINEMAP_CRATES=$SQ/chain/crate_dirs.txt
rm -rf "${O:?}"; mkdir -p $O/logs $TMPDIR; : > $O/verdict.tsv
guard() { pgrep -f memguard.sh >/dev/null || { echo "MEMGUARD NOT RUNNING"; exit 9; }; }
say() { echo "== $* ($(date -u +%FT%TZ))"; }
gate() { # gate <name> <I65 check args...>
  local name=$1; shift; python3 $REC/pass_checks.py "$@" > $O/gate_$name.json; local c=$?
  printf "%s\t%s\n" "$name" "$c" >> $O/verdict.tsv; say "gate $name: code $c $(head -c 300 $O/gate_$name.json)"; return $c; }
gateb() { # gateb <name> <B1 check args...>
  local name=$1; shift; $CHK "$@" > $O/gate_$name.json; local c=$?
  printf "%s\t%s\n" "$name" "$c" >> $O/verdict.tsv; say "gate $name: code $c $(head -c 300 $O/gate_$name.json)"; return $c; }
gatet() { # gatet <name> <text_u3.py args...>: the TEXT gate, every difference attributed (text_u3.py)
  local name=$1; shift; python3 $TOOLS/text_u3.py "$@" > $O/gate_$name.json; local c=$?
  printf "%s\t%s\n" "$name" "$c" >> $O/verdict.tsv; say "gate $name: code $c $(head -c 300 $O/gate_$name.json)"; return $c; }
finish() { # I65's: the first stop code, else 6 on any delta, else 0
  local code=$(awk -F'\t' '$2==2||$2==3||$2==4||$2==5{print $2; exit}' $O/verdict.tsv)
  [ -z "$code" ] && code=$(awk -F'\t' '$2!=0{print 6; exit}' $O/verdict.tsv); [ -z "$code" ] && code=0
  local word=PASS; [ $code -ne 0 ] && word="STOP"; [ $code -eq 6 ] && word="DELTAS TO READ"
  echo "VERDICT $word exit=$code basis=$REV tag=$TAG passA=SQ($PASS_A_REV..69002bc862+registration) delta_old=main($DELTA_OLD) gates=$(awk -F'\t' '{printf "%s:%s ", $1, $2}' $O/verdict.tsv)" | tee $O/VERDICT.txt
  exit $code; }
guard
# ---- 0. a fresh copy, checked blob for blob against the revision
rm -rf "${WK:?}"; mkdir -p $WK; cp -R $BASIS/projects $WK/
git -C $NUMREPO ls-tree -r $REV -- projects/chirality-piping | grep -v "projects/chirality-piping/execution/" | awk '$2=="blob"{print $3"\t"$4}' > $O/tree_blobs.tsv
gate tree tree $O/tree_blobs.tsv $WK || finish
W=$WK/projects/chirality-piping; P=$W/core/product_physics; RM=$P/src/retained_memory.rs
# ---- the entry against main's (B1 as merged), byte for byte; its code against the applied registration's (b1 ddc8eaaf54); M; the law tests
git -C $NUMREPO show $REGISTERED_REV:projects/chirality-piping/core/product_physics/src/retained_memory.rs > $O/registered_retained_memory.rs
gate entry entry $RM $O/registered_retained_memory.rs || finish
git -C $NUMREPO show $APPLIED_REV:projects/chirality-piping/core/product_physics/src/retained_memory.rs > $O/applied_registration_retained_memory.rs
gateb entry_code entry_code $RM $O/applied_registration_retained_memory.rs || finish
gateb m m $RM $M || finish
if [ "${I107_SKIP_CARGO:-0}" = 1 ]; then printf "law\tskipped\n" >> $O/verdict.tsv; say "law: skipped (I107_SKIP_CARGO)"; else
  guard
  ( cd $P && env CARGO_BUILD_JOBS=8 RUST_TEST_THREADS=2 $T/tools/t3_cargo.sh test --locked --offline --lib --target-dir $TGT retained_memory -- --nocapture --test-threads=1 > $O/logs/law.log 2>&1 )
  gate law law $O/logs/law.log $RM || finish
  gateb law_sq law_sq $O/logs/law.log $SQ/g6/law/law_tests.registered_dev.log
fi
python3 $REC/statics_list.py $MAINW/projects/chirality-piping $SQ/chain/crate_dirs.txt > $O/statics_sq.json   # reference: main
python3 $REC/statics_list.py $W $SQ/chain/crate_dirs.txt $O/statics_sq.json > $O/statics.json
gate statics statics $O/statics.json
python3 $REC/statics_list.py $W $SQ/chain/crate_dirs.txt $REC/reference/statics_a2.json > $O/statics_vs_u4_passA.info.json
# ---- the rules: I65's premise pins to SQ's basis, then SQ's chain to this basis (the pins are rule lines)
mkdir -p $O/rules57 $O/rules $RR
python3 $SQ/tools/g7_linemap_crates.py $NUMREPO $I65_PASS_A $PASS_A_REV $O/rules57 $REC/premise_pins.json > $O/linemap_premise57.out.json
lp=$?; cp $O/rules57/g7_linemap.out.json $O/linemap_premise57.json
gateb premise57 premise57 $O/linemap_premise57.json $SQ/g5/linemap_passA_to_b1q.json; [ $lp -eq 0 ] || { printf "premise57_run\t4\n" >> $O/verdict.tsv; finish; }
cp $SQ/chain/* $RR/
LINEMAP_ROWS=$SQ/g5/g5_c3/text_budget.caps.out.json.gz python3 $TOOLS/g7_linemap_crates_rows3.py $NUMREPO $PASS_A_REV $REV $O/rules $SQ/chain/callgraph_rules.g4.json $SQ/chain/loop_bounds.g4.json $SQ/chain/text_args.g4.json $SQ/chain/sens.py $O/rules57/premise_pins.json > $O/linemap.out.json
lm=$?
# U3: rules keyed only to lines the commit deleted (nothing in their place) are pruned; any other unmapped key stops (4)
if [ $lm -ne 0 ]; then python3 $TOOLS/prune_deleted.py $O/rules > $O/linemap_prune.json; pr=$?; say "prune: exit $pr $(head -c 300 $O/linemap_prune.json)"; [ $pr -eq 0 ] && lm=0; fi
printf "linemap\t%s\n" $([ $lm -eq 0 ] && echo 0 || echo 4) >> $O/verdict.tsv; say "linemap: exit $lm"; [ $lm -eq 0 ] || finish
cp $O/rules/callgraph_rules.g4.json $O/rules/loop_bounds.g4.json $O/rules/text_args.g4.json $O/rules/sens.py $RR/
gate premise premise $O/rules/premise_pins.json $W || finish
# ---- TEXT on the basis at C = 3 (inventory regenerated; D read from the run), on G5's chain and on N-5's
python3 - $W $SQ/chain/crate_dirs.txt $RR <<'PY'
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
python3 $SQ/g6/tools/sq_n5_chain.py $RR $RN > $O/logs/sq_n5_chain.log 2>&1 || { printf "text_run\t6\n" >> $O/verdict.tsv; finish; }
guard
$T/tools/t3_slot.sh bash $TOOLS/run_point_u3.sh $RR $O/g5 "$CAPS" $W > $O/logs/point_g5.txt 2>&1; t5=$?
guard
$T/tools/t3_slot.sh bash $TOOLS/run_point_u3.sh $RN $O/n5 "$CAPS" $W > $O/logs/point_n5.txt 2>&1; tn=$?
printf "text_run\t%s\n" $([ $t5 -eq 0 ] && [ $tn -eq 0 ] && echo 0 || echo 6) >> $O/verdict.tsv; say "TEXT points exit g5=$t5 n5=$tn"
D=$(python3 -c "import json;print(json.load(open('$O/n5/summary.json'))['D'])" 2>/dev/null || echo 0); echo $D > $O/D.txt; say "D from the run: $D"
[ "$D" -gt 0 ] 2>/dev/null || { printf "text_summary\t6\n" >> $O/verdict.tsv; say "the TEXT chain produced no summary"; finish; }
# ---- the production delta from B1 as merged, every hunk classified; unreviewed production hunks stop
python3 $TOOLS/delta_inventory2_u3.py $NUMREPO $DELTA_OLD $REV $W $SQ/chain/crate_dirs.txt $O/n5/edges.json $O/n5/work/loop_bounds.g4.json $RB/delta_reviewed_u3.json $O/delta_inventory.json > $O/delta.out.txt
dc=$?; [ $dc -ne 0 ] && [ $dc -ne 5 ] && [ $dc -ne 6 ] && dc=6
printf "delta\t%s\n" $dc >> $O/verdict.tsv; say "delta: exit $dc $(head -1 $O/delta.out.txt)"
[ $dc -eq 6 ] && [ ! -s $O/delta_inventory.json ] && finish
[ $dc -eq 5 ] && finish
# ---- TEXT against SQ's points (SQ's line-keyed edges and loop log carried 57c92a7b33 -> basis by the line map)
mkdir -p $O/ref_g5 $O/ref_g5_mapped
for f in edges.json looplog.json; do gzip -dc $SQ/g5/g5_c3/$f.gz > $O/ref_g5/$f; done
LINEMAP_ROWS=$SQ/g5/g5_c3/text_budget.caps.out.json.gz python3 $TOOLS/g7_linemap_crates_rows3.py $NUMREPO $PASS_A_REV $REV $O/ref_g5_mapped $O/ref_g5/edges.json $O/ref_g5/looplog.json > $O/linemap_sq_edges_looplog.out.json; say "SQ's edges/looplog line map: exit $?"
R1INV=$R0/I107/b1_passb_01/_run_records/runs/b1/delta_inventory.json.gz   # round 1's rows (57c92a7b33 -> B1)
R2INV=$R0/I107/pr_n_passb_01/_run_records/runs/pn/delta_inventory.json.gz   # round 2's rows (B1 -> PR-N)
gatet text $O/g5 $SQ/g5/g5_c3 $REC/text_row_diff.py $O/ref_g5_mapped $O/delta_inventory.json $O/linemap.out.json $R1INV $R2INV $WK $NUMREPO
gatet text_n5 $O/n5 $SQ/g6/n5/g5_c3 - $O/ref_g5_mapped $O/delta_inventory.json $O/linemap.out.json $R1INV $R2INV $WK $NUMREPO
gate forms forms $RM $O/n5/work/profile_tree.json $RN/g5_profile.py $O
git -C $NUMREPO show $G5_REV:projects/chirality-piping/core/product_physics/src/retained_memory.rs > $O/g5_retained_memory.rs; mkdir -p $O/forms_g5
gate forms_g5 forms $O/g5_retained_memory.rs $O/g5/work/profile_tree.json $RR/g5_profile.py $O/forms_g5
U3C="python3 $TOOLS/u3_checks.py"
u3gate() { # u3gate <name> <u3_checks.py args...>
  local name=$1; shift; $U3C "$@" > $O/gate_$name.json; local c=$?
  printf "%s\t%s\n" "$name" "$c" >> $O/verdict.tsv; say "gate $name: code $c $(head -c 300 $O/gate_$name.json)"; return $c; }
u3gate forms_u3 forms_u3 $O/gate_forms.json
u3gate forms_g5_u3 forms_u3 $O/gate_forms_g5.json
# ---- QUAL §11's non-candidates (multiplicity-free, Q-N5) on N-5's point, as SQ's noncand_b1.sh
guard
( cd $W && $T/tools/t3_slot.sh env G4_CAPS="$CAPS" TB_LEXICON=$O/n5/lexicon.json TB_COMPOSITE=$O/n5/work/composite_text.caps.json TB_D=$(python3 -c "import json;print(json.load(open('$O/n5/work/text_budget.caps.out.json'))['D_diagnostics'])") TB_NONCAND_OUT=$O/noncand.json python3 $O/n5/work/text_budget.py $W $O/n5/work/template_inventory_head.out.json $O/n5/edges.json $O/n5/work/loop_bounds.g4.json $O/n5/work/text_args.g4.json $ROOT caps > $O/whole_nc.out.json ); nc=$?
printf "noncand_run\t%s\n" $([ $nc -eq 0 ] && echo 0 || echo 6) >> $O/verdict.tsv; say "section 11 run exit $nc"
python3 $SQ/g6/tools/noncand_compare_nomult.py $REV87 $O/noncand.json > $O/noncand_compare_nomult.out.json
python3 $REC/noncand_compare.py $REV87 $O/noncand.json > $O/noncand_compare.info.json   # information only (Q-N5)
gateb noncand_sq noncand_sq $O/noncand_compare_nomult.out.json $SQ/g6/noncand/noncand_compare_nomult.out.json $O/noncand.json $SQ/g6/noncand/noncand.json
u3gate noncand_u3 noncand_u3 $O/noncand_compare_nomult.out.json $SQ/g6/noncand/noncand_compare_nomult.out.json $O/noncand.json $SQ/g6/noncand/noncand.json $O/linemap_prune.json
# ---- the controls (SQ's 12, on G5's point, as SQ ran them)
guard
( cd $W && $T/tools/t3_slot.sh env G4_CAPS_RUN="$CAPS" TB_D_RUN=$D python3 $TOOLS/audit_controls_u3.py $O/g5/work $W $O/g5/edges.json $O/g5/lexicon.json $O/ctl > $O/controls.out.txt ); cr=$?
printf "controls_run\t%s\n" $([ $cr -eq 0 ] && echo 0 || echo 6) >> $O/verdict.tsv; say "controls run exit $cr"
gate controls controls $O/ctl/audit_controls_g7.out.json 12
python3 $R0/I107/pr_n_passb_01/_run_records/tools/pn_checks.py controls_pn $O/ctl/audit_controls_g7.out.json $SQ/g5/g5_c3/audit_controls.out.json > $O/gate_controls_sq.json; c=$?
printf "controls_sq\t%s\n" $c >> $O/verdict.tsv; say "gate controls_sq: code $c $(head -c 300 $O/gate_controls_sq.json)"
u3gate controls_u3 controls_u3 $O/ctl/audit_controls_g7.out.json $SQ/g5/g5_c3/audit_controls.out.json
# ---- item 5: PP, runner/headless (and SQ's registered tree for its reference), the witnesses, the challenge
if [ "${I107_SKIP_CARGO:-0}" = 1 ]; then printf "item5\tskipped\n" >> $O/verdict.tsv; say "item 5: skipped (I107_SKIP_CARGO)"; finish; fi
guard
bash $TOOLS/run_cargo_u3.sh $TAG $WK $MAINW $O > $O/logs/cargo.out 2>&1
grep -E '^== |passed' $O/logs/cargo.out > $O/cargo_summary.txt
# SQ's registered PP suite (R/I104/.../g6/registration/pp_suite.registered.log), through I65's outcome extraction
awk '/^ *Running /{t=$2} /^test .* \.\.\. (ok|FAILED|ignored)/{sub(/ \(.*\)/,""); print t" :: "$0}' $SQ/g6/registration/pp_suite.registered.log | sed -E 's#target/[^ ]*/deps/##; s#-[0-9a-f]{16}##' | sort > $O/sq_pp.outcomes
gate pp_outcomes outcomes $O/logs/main_pp.outcomes $O/logs/${TAG}_pp.outcomes
gate runner_outcomes outcomes $O/logs/main_runner.outcomes $O/logs/${TAG}_runner.outcomes
gateb witnesses witnesses_sq $O/wit $SQ/g6/witnesses/table_dev.json
gateb challenge challenge_sq $O/chal $SQ/g6/rss/dev_table.json
finish
