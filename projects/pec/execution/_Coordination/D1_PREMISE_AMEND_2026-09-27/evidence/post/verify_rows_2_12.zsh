#!/bin/zsh
# D-PEC-105 act finite verification rows 2-12 on the act tree (run from the repository root
# of the act worktree; TMPDIR set outside the repository by the caller).
set -u
W=/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d105-act; cd $W
R=projects/pec/execution/_Coordination/D1_PREMISE_AMEND_2026-09-27; E=$R/evidence; O=$E/post
PREPEV=projects/pec/execution/_Coordination/PEC_D1_PREMISE_PREP_2026-09-26/evidence/run_main
export PYTHONDONTWRITEBYTECODE=1
mkdir -p $O
run() { local out=$1; shift; { echo "# $(date -u +%Y-%m-%dT%H:%M:%SZ) (date -u); cwd repo root; HEAD $(git rev-parse HEAD)"; echo "\$ $*"; eval "$@"; echo "exit=$?"; } > $out 2>&1; }
typeset -A PREPCK DIRS
PREPCK=(DEL-00-03_SOW a3bc80a0db9a1917aa54337f62cd2057ce154bdc792f3802d982012f667121b1 DEL-00-01_SOW 6e99f93c37c761b140c60d870ab0048bae814427d65143a60364f36896bb8cf9)
DIRS=(DEL-00-03_SOW projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-03_v2_SPEC_seed DEL-00-01_SOW projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures)
echo "# $(date -u +%Y-%m-%dT%H:%M:%SZ); HEAD $(git rev-parse HEAD); origin/main $(git rev-parse origin/main); $(python3 --version)" > $O/HEADER.out
# row 2: ledger rendering, and byte identity of each written target with its candidate and tabled postimage
run $O/render_candidates.out "python3 $R/render_candidates.py --gitdir . --prep $R"
run $O/byte_identity.out "python3 -c 'import importlib.util,hashlib,sys;s=importlib.util.spec_from_file_location(\"a\",\"$R/apply_d1p.py\");m=importlib.util.module_from_spec(s);s.loader.exec_module(m);ok=True
for p,v in m.TARGETS.items():
  t=open(p,\"rb\").read();c=open(\"$R/candidates/\"+p,\"rb\").read();h=hashlib.sha256(t).hexdigest();r=(t==c and h==v[3]);ok&=r;print((\"OK \" if r else \"MISMATCH \")+v[1]+\" \"+h+\" \"+p)
sys.exit(0 if ok else 1)'"
: > $O/checklist_compare.out; : > $O/boundary_summary.out
for k in DEL-00-03_SOW DEL-00-01_SOW; do
  d=${DIRS[$k]}
  # row 3: contract validity
  run $O/validate_$k.out "python3 tools/scope_of_work/validate_scope_of_work.py $d"
  # row 4: checklist, twice, byte-identical, equal to the prepared hash
  run $O/checklist_$k.out "python3 tools/scope_of_work/derive_review_checklist.py --output $R/checklist_$k.json $d"
  run $O/checklist_rerun_$k.out "python3 tools/scope_of_work/derive_review_checklist.py --output $O/checklist_rerun_$k.json $d"
  a=$(shasum -a 256 $R/checklist_$k.json | cut -d' ' -f1); b=$(shasum -a 256 $O/checklist_rerun_$k.json | cut -d' ' -f1)
  print -r -- "$k first=$a rerun=$b prepared=${PREPCK[$k]} $([[ $a == $b && $a == ${PREPCK[$k]} ]] && print MATCH || print MISMATCH)" >> $O/checklist_compare.out
  # row 5: boundary owners (QA 21)
  run $O/boundary_$k.out "python3 tools/scope_of_work/check_boundary_owner_resolution.py --json $R/boundary_$k.json --show-not-checkable $d/ScopeOfWork.md"
  bj=$(cmp -s $R/boundary_$k.json $PREPEV/boundary_AP_$k.json && print identical-to-prepared || print DIFFERS-from-prepared)
  print -r -- "$k exit=$(tail -1 $O/boundary_$k.out | cut -d= -f2) unresolved_or_undefined=$(grep -cE 'UNRESOLVED_OWNER|UNDEFINED_CLAIM' $O/boundary_$k.out) not_checkable_lines=$(grep -c NOT_CHECKABLE $O/boundary_$k.out) json=$bj" >> $O/boundary_summary.out
done
# rows 6-7: quotes and state claims
run $O/quotes.out "python3 $R/verify_d1p_quotes.py --tree . --gitdir . --prep $R --observation 6c6cc1b00"
run $O/state_claims.out "python3 $R/verify_d1p_state_claims.py --gitdir . --prep $R"
# row 8: lifecycle and review records preserved (also MEMORY.md and REV_* snapshots)
run $O/lifecycle.out "git diff --name-status origin/main...HEAD -- '**/_STATUS.md' '**/_REVIEW.md' '**/Review_Findings.csv' '**/MEMORY.md' '**/REV_*'"
# rows 9-10: registers, quote currency, every-PR checks; identical to the pre-act baselines
run $O/strict_post.out "python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution"
run $O/quote_currency_post.out "python3 $R/check_quote_currency.py --tree . --prep $R"
run $O/harness_post.out "python3 tools/practitioner_harness/harness.py self-check"
run $O/receipts_post.out "python3 tools/validation/validate_pec_loop_receipts.py --repo-root ."
{ echo "# comparison skips each file's first line (the date -u / HEAD header); the command line and all output are compared"
  for k in strict harness receipts quote_currency; do
    pre=$E/${k}_pre.out; post=$O/${k}_post.out
    if cmp -s <(tail -n +2 $pre) <(tail -n +2 $post); then print -r -- "$k: IDENTICAL ($(tail -1 $post))"; else print -r -- "$k: DIFFERS"; diff <(tail -n +2 $pre) <(tail -n +2 $post); fi
  done; } > $O/before_after_identity.out 2>&1
# informational: consequence scan on the post-act tree (the targets already hold their postimages)
run $O/scan_external_quotes.out "python3 $R/scan_external_quotes.py --tree . --prep $R --no-kept"
# pins at HEAD, and a second run refuses
run $O/pins.out "python3 -c 'import importlib.util,hashlib,sys;s=importlib.util.spec_from_file_location(\"a\",\"$R/apply_d1p.py\");m=importlib.util.module_from_spec(s);s.loader.exec_module(m);r=[(p,h==hashlib.sha256(open(p,\"rb\").read()).hexdigest()) for p,h in m.PINNED.items()];[print((\"OK \" if ok else \"MISMATCH \")+p) for p,ok in r];sys.exit(0 if all(ok for _,ok in r) else 1)'"
run $O/rerun_refuses.out "python3 $R/apply_d1p.py --repo $W --candidates $R/candidates --with-addon-p --check-only"
# rows 11-12: containment and whitespace
run $O/containment.out "git diff --name-status origin/main...HEAD"
run $O/whitespace.out "git diff --check origin/main...HEAD"
