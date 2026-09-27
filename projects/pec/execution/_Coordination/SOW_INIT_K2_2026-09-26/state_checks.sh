#!/bin/zsh
# usage: state.sh <tag>  — run from anywhere; runs the every-PR/register/closure checks on the act worktree
set -u
W=/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d103-act
RR=$W/projects/pec/execution/_Coordination/SOW_INIT_K2_2026-09-26; OUT=$RR/evidence
SP=/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/k2a
export PYTHONDONTWRITEBYTECODE=1; tag=$1; cd $W
{ echo '$ python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution'; python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution; echo "exit=$?"; } > $OUT/strict_$tag.out 2>&1
{ echo '$ python3 tools/practitioner_harness/harness.py self-check'; python3 tools/practitioner_harness/harness.py self-check; echo "exit=$?"; } > $OUT/harness_$tag.out 2>&1
{ echo '$ python3 tools/validation/validate_pec_loop_receipts.py --repo-root .'; python3 tools/validation/validate_pec_loop_receipts.py --repo-root .; echo "exit=$?"; } > $OUT/receipts_$tag.out 2>&1
rm -rf $SP/closure_$tag; mkdir -p $SP/closure_$tag
{ echo "\$ python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir <scratchpad>/k2a/closure_$tag"; python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir $SP/closure_$tag; echo "exit=$?"; } 2>&1 | sed "s#$SP#<scratchpad>/k2a#g" > $OUT/closure_$tag.out
python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); [d.pop(k,None) for k in ("generated_at","timestamp","run_date","output_dir","execution_root")]; print(json.dumps(d,sort_keys=True,indent=1))' $SP/closure_$tag/closure_summary.json > $OUT/closure_summary_$tag.json
for f in strict harness receipts closure; do echo "$f: $(tail -1 $OUT/${f}_$tag.out)"; done
python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); print("closure circular:",d.get("checks",{}).get("circular_dependencies"),"bidir:",d.get("bidirectional_pair_count"))' $OUT/closure_summary_$tag.json
