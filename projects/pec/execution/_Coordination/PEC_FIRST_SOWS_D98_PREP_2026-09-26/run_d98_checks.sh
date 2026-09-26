#!/bin/zsh
# Rerunnable D-PEC-98 preparation checks.
# Usage: run_d98_checks.sh <s3_dir> <base_export_at_OBS> <scratch_clone_at_OBS>
# The clone must be a disposable clone detached at the observation commit; this
# script resets and cleans the deliverable folders in it. Writes only to <s3_dir>/evidence.
set -u
S=$1; B=$2; G=$3
P=projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working
E=$S/evidence; mkdir -p $E
export PYTHONDONTWRITEBYTECODE=1
{
echo "# D-PEC-98 preparation checks"; echo "python: $(python3 --version)"; echo "scratch clone HEAD: $(git -C $G rev-parse HEAD)"
cd $G
git reset -q --hard HEAD; git clean -qfd -- $P
echo "## pre-candidate checks"
python3 tools/validation/validate_pec_loop_receipts.py --repo-root . > $E/receipts_pre.out 2>&1; echo "receipts pre exit=$?"
python3 tools/practitioner_harness/harness.py self-check > $E/harness_pre.out 2>&1; echo "harness pre exit=$?"
python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution > $E/strict_pre.out 2>&1; echo "strict pre exit=$?"
echo "strict pre summary: $(grep -E 'WARNING XRG-013 +[0-9]+' $E/strict_pre.out | tr -s ' ' | cut -c1-60) | $(tail -2 $E/strict_pre.out | tr -s ' ' | tr '\n' ' ')"
for d in DEL-02-08_Work_graph_parser DEL-02-09_MEMORY_run_index_parser; do cp $S/candidates/$P/$d/ScopeOfWork.md $P/$d/ScopeOfWork.md; done
git add -N $P/DEL-02-08_Work_graph_parser/ScopeOfWork.md $P/DEL-02-09_MEMORY_run_index_parser/ScopeOfWork.md
echo "## containment"; git status --porcelain
echo "## whitespace"; git diff --check; echo "diff --check exit=$?"
echo "## scope-of-work tools (mechanical method checks)"
for d in DEL-02-08_Work_graph_parser DEL-02-09_MEMORY_run_index_parser; do k=${d[1,9]}
  python3 tools/scope_of_work/validate_scope_of_work.py $P/$d; echo "$k validate exit=$?"
  python3 tools/scope_of_work/validate_scope_of_work.py --json $P/$d > $E/validate_$k.json
  python3 tools/scope_of_work/derive_review_checklist.py --output $E/checklist_$k.json $P/$d; echo "$k checklist exit=$?"
  python3 tools/scope_of_work/derive_review_checklist.py --output $E/checklist_${k}_rerun.json $P/$d
  cmp -s $E/checklist_$k.json $E/checklist_${k}_rerun.json && echo "$k checklist rerun byte-identical" || echo "$k checklist rerun DIFFERS"
  rm -f $E/checklist_${k}_rerun.json
  echo "$k checklist items: $(python3 -c "import json;print(json.load(open('$E/checklist_$k.json'))['item_count'])")"
  python3 tools/scope_of_work/check_boundary_owner_resolution.py --json $E/boundary_$k.json --show-not-checkable $P/$d/ScopeOfWork.md > $E/boundary_$k.out; echo "$k boundary exit=$? $(tail -1 $E/boundary_$k.out)"
  echo "$k _STATUS.md blob unchanged: $( [ "$(git hash-object $P/$d/_STATUS.md)" = "$(git rev-parse HEAD:$P/$d/_STATUS.md)" ] && echo yes || echo NO)"
done
echo "## quote fidelity (two-sided)"
python3 $S/verify_d98_quotes.py . $P/DEL-02-08_Work_graph_parser $P/DEL-02-09_MEMORY_run_index_parser > $E/verify_d98_quotes.out; echo "verify_d98_quotes exit=$? $(tail -1 $E/verify_d98_quotes.out)"
echo "## commit-anchored state claims"
python3 $S/verify_d98_state_claims.py . > $E/verify_d98_state_claims.out; echo "verify_d98_state_claims exit=$? $(tail -1 $E/verify_d98_state_claims.out)"
echo "## post-candidate checks"
python3 tools/validation/validate_pec_loop_receipts.py --repo-root . > $E/receipts_post.out 2>&1; echo "receipts post exit=$?"; cmp -s $E/receipts_pre.out $E/receipts_post.out && echo "receipts output identical"
python3 tools/practitioner_harness/harness.py self-check > $E/harness_post.out 2>&1; echo "harness post exit=$?"; cmp -s $E/harness_pre.out $E/harness_post.out && echo "harness output identical"
python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution > $E/strict_post.out 2>&1; echo "strict post exit=$?"; cmp -s $E/strict_pre.out $E/strict_post.out && echo "strict output identical"
echo "## reliance-hold preflight (exact-correction-preparation)"
cd projects/pec
for t in $P/DEL-02-08_Work_graph_parser/ScopeOfWork.md $P/DEL-02-09_MEMORY_run_index_parser/ScopeOfWork.md $P/DEL-02-08_Work_graph_parser/_STATUS.md $P/DEL-02-09_MEMORY_run_index_parser/_STATUS.md $P/DEL-02-08_Work_graph_parser/MEMORY.md $P/DEL-02-09_MEMORY_run_index_parser/MEMORY.md; do rel=${t#projects/pec/}
  python3 execution/_Scripts/pec_reliance_hold.py --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target $rel --operation exact-correction-preparation; echo " exit=$? $rel"; done
cd $G; git reset -q --hard HEAD; git clean -qfd -- $P
echo "## add-on S prototype (write_status.sh at clone HEAD)"
echo "write_status.sh sha256: $(shasum -a 256 tools/scaffolding/write_status.sh | cut -c1-64)"
for d in DEL-02-08_Work_graph_parser DEL-02-09_MEMORY_run_index_parser; do
  zsh tools/scaffolding/write_status.sh "$P/$d" INITIALIZED "TASK+status-advance" > /dev/null; echo "$d write_status exit=$? postimage=$(shasum -a 256 $P/$d/_STATUS.md | cut -c1-64)"; done
git diff --stat; git reset -q --hard HEAD
echo "## bound act prototype on a fresh copy of the base export"
A=$(mktemp -d ${S:h}/s3apply.XXXXXX); cp -R $B/. $A/
python3 $S/apply_d98.py --repo $A --candidates $S/candidates --check-only; echo "check-only exit=$?"
python3 $S/apply_d98.py --repo $A --candidates $S/candidates; echo "apply exit=$?"
python3 $S/apply_d98.py --repo $A --candidates $S/candidates; echo "second run exit=$? (expected 1)"
diff -rq $B $A | sed "s#$A#<applied>#"; rm -rf $A
echo "## act-script fault injection"
python3 $S/test_apply_d98.py $B $S/candidates > $E/test_apply_d98.out 2>&1; echo "test_apply_d98 exit=$? $(tail -1 $E/test_apply_d98.out)"
} 2>&1
