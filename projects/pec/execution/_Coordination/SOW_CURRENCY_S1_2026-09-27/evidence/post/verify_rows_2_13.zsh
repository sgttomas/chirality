#!/bin/zsh
# D-PEC-104 act finite verification rows 2-13 (run from the repo root of the act worktree).
set -u
W=/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d104-act; cd $W
R=projects/pec/execution/_Coordination/SOW_CURRENCY_S1_2026-09-27; E=$R/evidence; O=$E/post
PREPEV=projects/pec/execution/_Coordination/PEC_SOW_CURRENCY_S1_PREP_2026-09-26/evidence/run_main
export PYTHONDONTWRITEBYTECODE=1
: ${TMPDIR:?TMPDIR must be set to the session scratchpad}
mkdir -p $O
run() { local out=$1; shift; { echo "\$ $*"; eval "$@"; echo "exit=$?"; } > $out 2>&1; }
TGTS=(${(f)"$(cat $E/targets.txt)"})
typeset -A PREPCK
while read h p; do id=${${p:t}#checklist_}; id=${id%.json}; PREPCK[$id]=$h; done < <(grep -E 'evidence/run_main/checklist_DEL-[0-9-]+\.json$' projects/pec/execution/_Coordination/PEC_SOW_CURRENCY_S1_PREP_2026-09-26/SHA256SUMS)
echo "# $(date -u +%Y-%m-%dT%H:%M:%SZ) (date -u); HEAD $(git rev-parse HEAD); origin/main $(git rev-parse origin/main); $(python3 --version)" > $O/HEADER.out
: > $O/checklist_compare.out; : > $O/boundary_summary.out; : > $O/validate_summary.out
for t in $TGTS; do
  d=${t%/ScopeOfWork.md}; id=${${d:t}[1,9]}
  run $O/validate_$id.out "python3 tools/scope_of_work/validate_scope_of_work.py $d"
  print -r -- "$id $(grep -m1 -E '^(PASS|FAIL)' $O/validate_$id.out) $(tail -1 $O/validate_$id.out)" >> $O/validate_summary.out
  run $O/checklist_$id.out "python3 tools/scope_of_work/derive_review_checklist.py --output $R/checklist_$id.json $d"
  run $O/checklist_rerun_$id.out "python3 tools/scope_of_work/derive_review_checklist.py --output $TMPDIR/s1a_checklist_rerun_$id.json $d"
  a=$(shasum -a 256 $R/checklist_$id.json | cut -c1-64); b=$(shasum -a 256 $TMPDIR/s1a_checklist_rerun_$id.json | cut -c1-64); rm -f $TMPDIR/s1a_checklist_rerun_$id.json
  print -r -- "$id first=$a rerun=$b prepared=${PREPCK[$id]} exits=$(tail -1 $O/checklist_$id.out),$(tail -1 $O/checklist_rerun_$id.out) $([[ $a == $b && $a == ${PREPCK[$id]} ]] && print MATCH || print MISMATCH)" >> $O/checklist_compare.out
  run $O/boundary_$id.out "python3 tools/scope_of_work/check_boundary_owner_resolution.py --json $R/boundary_$id.json --show-not-checkable $d/ScopeOfWork.md"
  bj=$(cmp -s $R/boundary_$id.json $PREPEV/boundary_$id.json && print identical-to-prepared || print DIFFERS-from-prepared)
  print -r -- "$id exit=$(tail -1 $O/boundary_$id.out | cut -d= -f2) unresolved_or_undefined=$(grep -cE 'UNRESOLVED_OWNER|UNDEFINED_CLAIM' $O/boundary_$id.out) not_checkable_lines=$(grep -c NOT_CHECKABLE $O/boundary_$id.out) json=$bj" >> $O/boundary_summary.out
done
run $O/quotes.out "python3 $R/verify_s1p_quotes.py --tree . --gitdir . --prep $R --observation 125cfacc1 --obs-exempt DEL-03-06"
run $O/state_claims.out "python3 $R/verify_s1p_state_claims.py --gitdir . --prep $R"
run $O/qualified_ids.out "python3 $R/check_qualified_ids.py --prep $R --gitdir . --observation 125cfacc1"
run $O/dep_quote_currency_post.out "python3 $R/check_dep_quote_currency.py ."
run $O/s4_postimages.out "shasum -a 256 projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/ScopeOfWork.md projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/ScopeOfWork.md; git diff --name-status origin/main...HEAD -- projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping"
run $O/lifecycle.out "git diff --name-status origin/main...HEAD -- '**/_STATUS.md' '**/_REVIEW.md' '**/Review_Findings.csv' '**/MEMORY.md'"
run $O/strict_post.out "python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution"
run $O/harness_post.out "python3 tools/practitioner_harness/harness.py self-check"
run $O/receipts_post.out "python3 tools/validation/validate_pec_loop_receipts.py --repo-root ."
# before/after identity: drop the pre-act files' timestamp/HEAD header line (line 1) before comparing; the command line and all output must match
{ for k in strict harness receipts dep_quote_currency; do
    pre=$E/${k}_pre.out; post=$O/${k}_post.out
    tail -n +2 $pre | sed 's#^\$ python3 projects/pec/execution/_Coordination/SOW_CURRENCY_S1_2026-09-27/#$ python3 #' > $TMPDIR/s1a_pre.norm
    sed 's#^\$ python3 projects/pec/execution/_Coordination/SOW_CURRENCY_S1_2026-09-27/#$ python3 #' $post > $TMPDIR/s1a_post.norm
    cmp -s $TMPDIR/s1a_pre.norm $TMPDIR/s1a_post.norm && print -r -- "$k: IDENTICAL ($(tail -1 $post))" || { print -r -- "$k: DIFFERS"; diff $TMPDIR/s1a_pre.norm $TMPDIR/s1a_post.norm; }
  done; rm -f $TMPDIR/s1a_pre.norm $TMPDIR/s1a_post.norm; } > $O/before_after_identity.out 2>&1
run $O/pins.out "python3 -c 'import importlib.util,hashlib,sys;s=importlib.util.spec_from_file_location(\"a\",\"$R/apply_s1p.py\");m=importlib.util.module_from_spec(s);s.loader.exec_module(m);r=[(p,h==hashlib.sha256(open(p,\"rb\").read()).hexdigest()) for p,h in m.PINNED.items()];[print((\"OK \" if ok else \"MISMATCH \")+p) for p,ok in r];t=[(p,v[1]==hashlib.sha256(open(p,\"rb\").read()).hexdigest()) for p,v in m.TARGETS.items()];[print((\"POST-OK \" if ok else \"POST-MISMATCH \")+p) for p,ok in t];print(f\"pins {sum(ok for _,ok in r)}/{len(r)} postimages {sum(ok for _,ok in t)}/{len(t)}\");sys.exit(0 if all(ok for _,ok in r+t) else 1)'"
run $O/rerun_refuses.out "python3 $R/apply_s1p.py --repo $W --candidates $R/candidates --check-only"
# REQ/AC/VER definition lines of DEL-01-03 and DEL-01-05 against their preimages (origin/main)
: > $O/req_ac_ver_identity.out
for t in $TGTS; do
  case $t in *DEL-01-03_*|*DEL-01-05_*) ;; *) continue;; esac
  id=${${${t%/ScopeOfWork.md}:t}[1,9]}
  git show origin/main:$t | grep -E '^- \*\*(REQ|AC|VER)-[0-9]{3}\*\*' > $TMPDIR/s1a_pre_rav.txt
  grep -E '^- \*\*(REQ|AC|VER)-[0-9]{3}\*\*' $t > $TMPDIR/s1a_post_rav.txt
  print -r -- "$id pre_lines=$(wc -l < $TMPDIR/s1a_pre_rav.txt | tr -d ' ') post_lines=$(wc -l < $TMPDIR/s1a_post_rav.txt | tr -d ' ') $(cmp -s $TMPDIR/s1a_pre_rav.txt $TMPDIR/s1a_post_rav.txt && print BYTE-IDENTICAL-IN-ORDER || print DIFFERS)" >> $O/req_ac_ver_identity.out
  rm -f $TMPDIR/s1a_pre_rav.txt $TMPDIR/s1a_post_rav.txt
done
# DEL-03-06 diff hunks (correction-only; expected loci L220, L222-225, L229, L476)
run $O/del_03_06_hunks.out "git diff -U0 origin/main...HEAD -- projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/ScopeOfWork.md | grep '^@@'"
run $O/containment.out "git diff --name-status origin/main...HEAD"
run $O/whitespace.out "git diff --check origin/main...HEAD"
