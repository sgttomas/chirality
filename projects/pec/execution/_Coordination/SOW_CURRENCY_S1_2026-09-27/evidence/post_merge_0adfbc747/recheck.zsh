#!/bin/zsh
# D-PEC-104 act: rechecks after the no-rebase merge of origin/main 0adfbc747 (run from the repo root of the act worktree).
set -u
W=/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d104-act; cd $W
R=projects/pec/execution/_Coordination/SOW_CURRENCY_S1_2026-09-27; E=$R/evidence; O=$E/post_merge_0adfbc747
export PYTHONDONTWRITEBYTECODE=1
: ${TMPDIR:?TMPDIR must be set to the session scratchpad}
M=0adfbc7476df33521883ce1573781237cd24d384
run() { local out=$1; shift; { echo "\$ $*"; eval "$@"; echo "exit=$?"; } > $out 2>&1; }
echo "# $(date -u +%Y-%m-%dT%H:%M:%SZ) (date -u); HEAD $(git rev-parse HEAD); origin/main $(git rev-parse origin/main); $(python3 --version); PYTHONDONTWRITEBYTECODE=$PYTHONDONTWRITEBYTECODE" > $O/HEADER.out
run $O/main_diff_pec.out "git diff --name-status 16010b4ca $M -- projects/pec"
run $O/checkonly_head.out "PYTHONDONTWRITEBYTECODE=1 python3 $R/apply_s1p.py --repo $W --candidates $R/candidates --check-only"
X=$(mktemp -d $TMPDIR/s1a_main_export.XXXXXX)
git archive $M | tar -x -C $X
run $O/checkonly_main_export.out "PYTHONDONTWRITEBYTECODE=1 python3 $R/apply_s1p.py --repo \$X --candidates $R/candidates --check-only"
sed -i '' "s#$X#<export of $M>#g" $O/checkonly_main_export.out
rm -rf $X
run $O/quotes.out "python3 $R/verify_s1p_quotes.py --tree . --gitdir . --prep $R --observation 125cfacc1 --obs-exempt DEL-03-06"
run $O/state_claims.out "python3 $R/verify_s1p_state_claims.py --gitdir . --prep $R"
run $O/qualified_ids.out "python3 $R/check_qualified_ids.py --prep $R --gitdir . --observation 125cfacc1"
run $O/dep_quote_currency.out "python3 $R/check_dep_quote_currency.py ."
run $O/pins.out "python3 -c 'import importlib.util,hashlib,sys;s=importlib.util.spec_from_file_location(\"a\",\"$R/apply_s1p.py\");m=importlib.util.module_from_spec(s);s.loader.exec_module(m);r=[(p,h==hashlib.sha256(open(p,\"rb\").read()).hexdigest()) for p,h in m.PINNED.items()];t=[(p,v[1]==hashlib.sha256(open(p,\"rb\").read()).hexdigest()) for p,v in m.TARGETS.items()];[print((\"MISMATCH \")+p) for p,ok in r+t if not ok];print(f\"pins {sum(ok for _,ok in r)}/{len(r)} postimages {sum(ok for _,ok in t)}/{len(t)}\");sys.exit(0 if all(ok for _,ok in r+t) else 1)'"
run $O/strict.out "python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution"
run $O/harness.out "python3 tools/practitioner_harness/harness.py self-check"
run $O/receipts.out "python3 tools/validation/validate_pec_loop_receipts.py --repo-root ."
{ for k in strict harness receipts dep_quote_currency; do
    pre=$E/${k}_pre.out; post=$O/${k}.out
    tail -n +2 $pre | sed 's#^\$ python3 projects/pec/execution/_Coordination/SOW_CURRENCY_S1_2026-09-27/#$ python3 #' > $TMPDIR/s1a_pre.norm
    sed 's#^\$ python3 projects/pec/execution/_Coordination/SOW_CURRENCY_S1_2026-09-27/#$ python3 #' $post > $TMPDIR/s1a_post.norm
    cmp -s $TMPDIR/s1a_pre.norm $TMPDIR/s1a_post.norm && print -r -- "$k: IDENTICAL to pre-act baseline ($(tail -1 $post))" || { print -r -- "$k: DIFFERS"; diff $TMPDIR/s1a_pre.norm $TMPDIR/s1a_post.norm; }
  done; rm -f $TMPDIR/s1a_pre.norm $TMPDIR/s1a_post.norm; } > $O/before_after_identity.out 2>&1
run $O/lifecycle.out "git diff --name-status origin/main...HEAD -- '**/_STATUS.md' '**/_REVIEW.md' '**/Review_Findings.csv' '**/MEMORY.md'"
run $O/containment_summary.out "git diff --name-status origin/main...HEAD | awk '{p=\$2; c=(p ~ /^projects\\/pec\\/execution\\/_Coordination\\/SOW_CURRENCY_S1_2026-09-27\\//)?\"run-root\":(p ~ /ScopeOfWork.md\$/)?\"contract-\"\$1:p; print c}' | sort | uniq -c"
run $O/whitespace.out "git diff --check origin/main...HEAD"
