#!/bin/zsh
# D-PEC-102 act finite verification rows 2-12 (run from repo root).
set -u
W=/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d102-act; cd $W
R=projects/pec/execution/_Coordination/SOW_CURRENCY_S4_2026-09-26; E=$R/evidence; O=$E/post
PREPEV=projects/pec/execution/_Coordination/PEC_SOW_CURRENCY_S4_PREP_2026-09-26/evidence/run_main
export PYTHONDONTWRITEBYTECODE=1
mkdir -p $O
run() { local out=$1; shift; { echo "\$ $*"; eval "$@"; echo "exit=$?"; } > $out 2>&1; }
TGTS=(${(f)"$(cat $E/targets.txt)"})
typeset -A PREPCK
PREPCK=(DEL-04-01 1d8cccbc189dbab444dd91defcc5e7aa9cb7b41d75351aad45571129eadf61f5 DEL-04-02 4b0399562616101e31181bc22fa0656c9c9c5e57388e8c779f792b533e009fa7 DEL-08-01 2b5beadb0edaf471a25706ac4c4022aa83ab598bfeb1b216c3a6bf42bc7e50b4 DEL-08-03 b91cf9f452134c60f7e569fb415a5842770e61df120aacf3dc6f8e9ed361c1af DEL-08-04 afe85efd4dd03949737c8f2d4edd9b2da08b853ceaecad562242d58ceb7b61c1 DEL-04-03 85f0d3bcb133687e7ad0d721e1e5980b4a56adff21c286e9b265b7fa9c000e0c DEL-03-04 1a86fa421c0d79bb8c0a080979d4e4f1bbde3c3beed95b832244fcc86d0dbeda DEL-10-03 24272d5dc8fd2907fc1b87259b449623d6015bdaf6a02936c2c7ec1f34a060fd)
echo "# $(date -u +%Y-%m-%dT%H:%M:%SZ); HEAD $(git rev-parse HEAD); origin/main $(git rev-parse origin/main); $(python3 --version)" > $O/HEADER.out
: > $O/checklist_compare.out; : > $O/boundary_summary.out
for t in $TGTS; do
  d=projects/pec/${t%/ScopeOfWork.md}; id=${${d:t}[1,9]}
  run $O/validate_$id.out "python3 tools/scope_of_work/validate_scope_of_work.py $d"
  run $O/checklist_$id.out "python3 tools/scope_of_work/derive_review_checklist.py --output $R/checklist_$id.json $d"
  run $O/checklist_rerun_$id.out "python3 tools/scope_of_work/derive_review_checklist.py --output $O/checklist_rerun_$id.json $d"
  a=$(shasum -a 256 $R/checklist_$id.json | cut -d' ' -f1); b=$(shasum -a 256 $O/checklist_rerun_$id.json | cut -d' ' -f1)
  print -r -- "$id first=$a rerun=$b prepared=${PREPCK[$id]} $([[ $a == $b && $a == ${PREPCK[$id]} ]] && print MATCH || print MISMATCH)" >> $O/checklist_compare.out
  run $O/boundary_$id.out "python3 tools/scope_of_work/check_boundary_owner_resolution.py --json $R/boundary_$id.json --show-not-checkable $d/ScopeOfWork.md"
  bj=$(cmp -s $R/boundary_$id.json $PREPEV/boundary_$id.json && print identical-to-prepared || print DIFFERS-from-prepared)
  print -r -- "$id exit=$(tail -1 $O/boundary_$id.out | cut -d= -f2) unresolved_or_undefined=$(grep -cE 'UNRESOLVED_OWNER|UNDEFINED_CLAIM' $O/boundary_$id.out) not_checkable_lines=$(grep -c NOT_CHECKABLE $O/boundary_$id.out) json=$bj" >> $O/boundary_summary.out
done
run $O/quotes.out "python3 $R/verify_s4p_quotes.py --tree . --gitdir . --prep $R --observation 125cfacc1"
run $O/state_claims.out "python3 $R/verify_s4p_state_claims.py --gitdir . --prep $R"
run $O/sibling_ids.out "python3 $R/check_sibling_ids.py $R ."
run $O/scan_s2_quotes.out "python3 $R/scan_s2_quotes.py --tree . --gitdir . --prior-commit ce934ac33 --candidates $R"
run $O/scan_external_quotes.out "python3 $R/scan_external_quotes.py --tree . --prep $R"
run $O/quote_currency_post.out "python3 $R/check_quote_currency.py --tree ."
run $O/lifecycle.out "git diff --name-status origin/main...HEAD -- '**/_STATUS.md' '**/_REVIEW.md' '**/Review_Findings.csv' '**/MEMORY.md'"
run $O/strict_post.out "python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution"
run $O/harness_post.out "python3 tools/practitioner_harness/harness.py self-check"
run $O/receipts_post.out "python3 tools/validation/validate_pec_loop_receipts.py --repo-root ."
{ for k in strict harness receipts quote_currency; do
    pre=$E/${k}_pre.out; post=$O/${k}_post.out
    cmp -s $pre $post && print -r -- "$k: IDENTICAL ($(tail -1 $post))" || { print -r -- "$k: DIFFERS"; diff $pre $post; }
  done; } > $O/before_after_identity.out 2>&1
run $O/pins.out "python3 -c 'import importlib.util,hashlib,sys;s=importlib.util.spec_from_file_location(\"a\",\"$R/apply_s4p.py\");m=importlib.util.module_from_spec(s);s.loader.exec_module(m);r=[(p,h==hashlib.sha256(open(p,\"rb\").read()).hexdigest()) for p,h in m.PINNED.items()];[print((\"OK \" if ok else \"MISMATCH \")+p) for p,ok in r];t=[(p,v[1]==hashlib.sha256(open(p,\"rb\").read()).hexdigest()) for p,v in m.TARGETS.items()];[print((\"POST-OK \" if ok else \"POST-MISMATCH \")+p) for p,ok in t];sys.exit(0 if all(ok for _,ok in r+t) else 1)'"
run $O/rerun_refuses.out "python3 $R/apply_s4p.py --repo $W --candidates $R/candidates --check-only"
run $O/containment.out "git diff --name-status origin/main...HEAD"
run $O/whitespace.out "git diff --check origin/main...HEAD"
