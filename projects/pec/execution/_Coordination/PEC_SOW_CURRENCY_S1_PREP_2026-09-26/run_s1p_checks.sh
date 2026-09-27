#!/bin/zsh
# Run every S1 (provisional D-PEC-104) preparation check on fresh `git archive` exports (never on a checkout).
# Pattern of the D-PEC-100 runner run_s2p_checks.sh.
# Usage: run_s1p_checks.sh <repo (for git objects)> <commit> <prep dir> <out dir> [observation commit, default 125cfacc1]
# Writes all outputs under <out dir>; prints a summary; exit 0 only if every check passes.
set -u
REPO=$1; C=$2; PREP=${3:A}; OUT=${4:A}; OBS=${5:-125cfacc1}
export PYTHONDONTWRITEBYTECODE=1
mkdir -p "$OUT"
T=$(mktemp -d "${TMPDIR:-/tmp}/s1pchk.XXXXXX")
PRE=$T/pre; POST=$T/post; mkdir -p "$PRE" "$POST"
git -C "$REPO" archive "$C" | tar -x -C "$PRE"
git -C "$REPO" archive "$C" | tar -x -C "$POST"
# Give each export a Git identity without a second checkout: an empty repository whose
# object store borrows the source repository's objects (alternates), with HEAD at <commit>.
# The every-PR tools need a repo root and resolve commits; nothing is written to <repo>.
OBJ=$(cd "$REPO" && cd "$(git rev-parse --git-common-dir)" && pwd)/objects
SHA=$(git -C "$REPO" rev-parse "$C^{commit}")
for d in "$PRE" "$POST"; do
  git -C "$d" init -q && print -r -- "$OBJ" > "$d/.git/objects/info/alternates" && git -C "$d" update-ref HEAD "$SHA"
done
fail=0
note() { print -r -- "$1" | tee -a "$OUT/SUMMARY.out"; }
: > "$OUT/SUMMARY.out"
note "basis commit: $(git -C "$REPO" rev-parse "$C")"
note "python: $(python3 --version 2>&1)"

# 1. before-state every-PR and register checks
(cd "$PRE" && python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution > "$OUT/strict_pre.out" 2>&1; print "exit=$?" >> "$OUT/strict_pre.out")
(cd "$PRE" && python3 tools/practitioner_harness/harness.py self-check > "$OUT/harness_pre.out" 2>&1; print "exit=$?" >> "$OUT/harness_pre.out")
(cd "$PRE" && python3 tools/validation/validate_pec_loop_receipts.py --repo-root . > "$OUT/receipts_pre.out" 2>&1; print "exit=$?" >> "$OUT/receipts_pre.out")

# 2. the act: check-only, apply, second run
(cd "$POST" && python3 "$PREP/apply_s1p.py" --repo . --candidates "$PREP/candidates" --check-only > "$OUT/apply_checkonly.out" 2>&1; print "exit=$?" >> "$OUT/apply_checkonly.out")
(cd "$POST" && python3 "$PREP/apply_s1p.py" --repo . --candidates "$PREP/candidates" > "$OUT/apply.out" 2>&1; print "exit=$?" >> "$OUT/apply.out")
(cd "$POST" && python3 "$PREP/apply_s1p.py" --repo . --candidates "$PREP/candidates" > "$OUT/apply_rerun.out" 2>&1; print "exit=$?" >> "$OUT/apply_rerun.out")
grep -q '^exit=0$' "$OUT/apply_checkonly.out" && grep -q '^exit=0$' "$OUT/apply.out" && grep -q '^exit=1$' "$OUT/apply_rerun.out" \
  && note "PASS act: check-only 0, apply 0, rerun refuses 1" || { note "FAIL act"; fail=1; }

# 3. containment: diff of the two exports is exactly the twelve contracts
diff -rq -x .git "$PRE" "$POST" > "$OUT/containment.out" 2>&1   # .git is the borrowed-object identity added above, not tree content
n=$(grep -c . "$OUT/containment.out"); nsow=$(grep -c 'ScopeOfWork.md differ$' "$OUT/containment.out")
[[ $n -eq 12 && $nsow -eq 12 ]] && note "PASS containment: 12 differing files, all ScopeOfWork.md" || { note "FAIL containment ($n differing, $nsow SOW)"; fail=1; }

# 4. per-contract validation, checklist (twice), boundary owners
for d in ${(f)"$(cd "$POST" && python3 -c 'import importlib.util,sys;s=importlib.util.spec_from_file_location("a",sys.argv[1]);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);[print(r.rsplit("/",1)[0]) for r in m.TARGETS]' "$PREP/apply_s1p.py")"}; do
  id=${${d:t}[1,9]}
  (cd "$POST" && python3 tools/scope_of_work/validate_scope_of_work.py "$d" > "$OUT/validate_$id.out" 2>&1; print "exit=$?" >> "$OUT/validate_$id.out")
  grep -q '^PASS format=SOW_V1' "$OUT/validate_$id.out" && note "PASS validate $id" || { note "FAIL validate $id"; fail=1; }
  (cd "$POST" && python3 tools/scope_of_work/derive_review_checklist.py --output "$OUT/checklist_$id.json" "$d" > "$OUT/checklist_$id.out" 2>&1; print "exit=$?" >> "$OUT/checklist_$id.out")
  (cd "$POST" && python3 tools/scope_of_work/derive_review_checklist.py --output "$T/checklist_$id.2.json" "$d" > /dev/null 2>&1)
  cmp -s "$OUT/checklist_$id.json" "$T/checklist_$id.2.json" && grep -q '^exit=0$' "$OUT/checklist_$id.out" && note "PASS checklist $id (rerun byte-identical)" || { note "FAIL checklist $id"; fail=1; }
  (cd "$POST" && python3 tools/scope_of_work/check_boundary_owner_resolution.py --json "$OUT/boundary_$id.json" --show-not-checkable "$d/ScopeOfWork.md" > "$OUT/boundary_$id.out" 2>&1; print "exit=$?" >> "$OUT/boundary_$id.out")
  grep -qE 'UNRESOLVED_OWNER|UNDEFINED_CLAIM' "$OUT/boundary_$id.out" && { note "FAIL boundary $id"; fail=1; } || { grep -q '^exit=0$' "$OUT/boundary_$id.out" && note "PASS boundary $id (no UNRESOLVED_OWNER/UNDEFINED_CLAIM)" || { note "FAIL boundary $id exit"; fail=1; } }
done

# 5. quotes (two-sided, against the post-act tree) and commit-anchored state claims
python3 "$PREP/verify_s1p_quotes.py" --tree "$POST" --gitdir "$REPO" --prep "$PREP" --observation "${OBS}" --obs-exempt DEL-03-06 > "$OUT/verify_quotes.out" 2>&1; rq=$?
note "$( [[ $rq -eq 0 ]] && print PASS || print FAIL ) quotes: $(tail -1 "$OUT/verify_quotes.out")"; [[ $rq -eq 0 ]] || fail=1
python3 "$PREP/verify_s1p_state_claims.py" --gitdir "$REPO" --prep "$PREP" > "$OUT/verify_state_claims.out" 2>&1; rc=$?
note "$( [[ $rc -eq 0 ]] && print PASS || print FAIL ) state claims: $(tail -1 "$OUT/verify_state_claims.out")"; [[ $rc -eq 0 ]] || fail=1

python3 "$PREP/check_qualified_ids.py" --prep "$PREP" --gitdir "$REPO" --observation "${OBS}" > "$OUT/check_qualified_ids.out" 2>&1; rs=$?
note "$( [[ $rs -eq 0 ]] && print PASS || print FAIL ) qualified IDs: $(tail -1 "$OUT/check_qualified_ids.out")"; [[ $rs -eq 0 ]] || fail=1
# D-PEC-95 quote currency (gen_d95.py step 3): every ACTIVE EXECUTION EvidenceQuote verbatim in its EvidenceFile, before and after
for side in pre post; do
  dir=$PRE; [[ $side = post ]] && dir=$POST
  python3 "$PREP/check_dep_quote_currency.py" "$dir" > "$OUT/dep_quote_currency_$side.out" 2>&1; rd=$?
  note "$( [[ $rd -eq 0 ]] && print PASS || print FAIL ) dependency quote currency ($side): $(tail -1 "$OUT/dep_quote_currency_$side.out")"; [[ $rd -eq 0 ]] || fail=1
done
: > "$OUT/audit_quotes_post.out"
for f in "$PREP"/candidates/projects/pec/execution/PKG-*/1_Working/DEL-*/ScopeOfWork.md; do
  rel=${f#$PREP/candidates/}
  python3 "$PREP/aids/audit_quotes.py" --tree "$POST" --gitdir "$REPO" --s2-prior 9cf863697 "$POST/$rel" >> "$OUT/audit_quotes_post.out" 2>&1
done
note "INFO quote audit (informational): S2-STALE $(grep -c ' S2-STALE ' "$OUT/audit_quotes_post.out") NOTFOUND $(grep -c ' NOTFOUND' "$OUT/audit_quotes_post.out")"

# 6. after-state registers and every-PR checks identical to before (D-GOV-48: identical, not 0/0)
(cd "$POST" && python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution > "$OUT/strict_post.out" 2>&1; print "exit=$?" >> "$OUT/strict_post.out")
(cd "$POST" && python3 tools/practitioner_harness/harness.py self-check > "$OUT/harness_post.out" 2>&1; print "exit=$?" >> "$OUT/harness_post.out")
(cd "$POST" && python3 tools/validation/validate_pec_loop_receipts.py --repo-root . > "$OUT/receipts_post.out" 2>&1; print "exit=$?" >> "$OUT/receipts_post.out")
# The two exports live at different paths; outputs are compared with each export root
# replaced by the literal <export> (the raw outputs are kept unchanged).
for k in strict harness receipts; do
  sed "s#$PRE#<export>#g" "$OUT/${k}_pre.out" > "$T/${k}_pre.norm"; sed "s#$POST#<export>#g" "$OUT/${k}_post.out" > "$T/${k}_post.norm"
  cmp -s "$T/${k}_pre.norm" "$T/${k}_post.norm" && note "PASS $k identical before/after, export root normalized ($(tail -1 "$OUT/${k}_post.out"))" || { note "FAIL $k differs"; fail=1; }
done

# 7. whitespace (trailing blanks, tabs, missing final newline) in the twelve candidates
ws=0
for f in "$PREP"/candidates/**/ScopeOfWork.md; do
  grep -nE ' +$|	' "$f" && ws=1
  [[ -n "$(tail -c1 "$f")" ]] && { print "no final newline: $f"; ws=1; }
done > "$OUT/whitespace.out" 2>&1
[[ $ws -eq 0 ]] && note "PASS whitespace" || { note "FAIL whitespace"; fail=1; }

# 8. fault injection on a fresh export
python3 "$PREP/test_apply_s1p.py" "$PRE" "$PREP/candidates" > "$OUT/test_apply_s1p.out" 2>&1; rt=$?
note "$( [[ $rt -eq 0 ]] && print PASS || print FAIL ) fault injection: $(tail -1 "$OUT/test_apply_s1p.out")"; [[ $rt -eq 0 ]] || fail=1

rm -rf "$T"
note "OVERALL $( [[ $fail -eq 0 ]] && print PASS || print FAIL )"
exit $fail
