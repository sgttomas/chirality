#!/bin/zsh
# Run every K2 (provisional D-PEC-103) preparation check on fresh `git archive`
# exports (never on a checkout).
# Usage: run_k2_checks.sh <repo (for git objects)> <commit> <prep dir> <out dir> [observation commit, default 125cfacc1]
# Writes all outputs under <out dir>; prints a summary; exit 0 only if every check passes.
# Scratch lives in one `mktemp -d` directory, which is the only thing it deletes.
set -u
REPO=$1; C=$2; PREP=${3:A}; OUT=${4:A}; OBS=${5:-125cfacc1}
export PYTHONDONTWRITEBYTECODE=1
mkdir -p "$OUT"
T=$(mktemp -d "${TMPDIR:-/tmp}/k2chk.XXXXXX")
PRE=$T/pre; POST=$T/post; mkdir -p "$PRE" "$POST"
git -C "$REPO" archive "$C" | tar -x -C "$PRE"
git -C "$REPO" archive "$C" | tar -x -C "$POST"
# Give each export a Git identity without a second checkout (alternates borrow the
# source repository's objects); nothing is written to <repo>.
OBJ=$(cd "$REPO" && cd "$(git rev-parse --git-common-dir)" && pwd)/objects
SHA=$(git -C "$REPO" rev-parse "$C^{commit}")
for d in "$PRE" "$POST"; do
  git -C "$d" init -q && print -r -- "$OBJ" > "$d/.git/objects/info/alternates" && git -C "$d" update-ref HEAD "$SHA"
done
fail=0
note() { print -r -- "$1" | tee -a "$OUT/SUMMARY.out"; }
: > "$OUT/SUMMARY.out"
note "basis commit: $SHA"
note "python: $(python3 --version 2>&1)"
E=projects/pec/execution
D86=$E/PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface
D13=$E/PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate

# 0. reliance-hold preflight (exact-correction-preparation) on every possible target
: > "$OUT/reliance_hold_preflight.out"; rh=0
for f in $D86/ScopeOfWork.md $D86/_STATUS.md $D86/MEMORY.md $D13/ScopeOfWork.md $D13/_STATUS.md $D13/MEMORY.md $D13/_DEPENDENCIES.md; do
  r=${f#projects/pec/}
  (cd "$PRE/projects/pec" && print -r -- "\$ python3 execution/_Scripts/pec_reliance_hold.py --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target $r --operation exact-correction-preparation" && python3 execution/_Scripts/pec_reliance_hold.py --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target "$r" --operation exact-correction-preparation; print "exit=$?") >> "$OUT/reliance_hold_preflight.out" 2>&1
done
n_allow=$(grep -c '"status": "ALLOW"' "$OUT/reliance_hold_preflight.out"); n_ok=$(grep -c '^exit=0$' "$OUT/reliance_hold_preflight.out")
[[ $n_allow -eq 7 && $n_ok -eq 7 ]] && note "PASS reliance preflight: ALLOW x7" || { note "FAIL reliance preflight"; fail=1; }

# 1. before-state register, closure and every-PR checks
run_state() {  # $1 export root, $2 tag
  (cd "$1" && python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution > "$OUT/strict_$2.out" 2>&1; print "exit=$?" >> "$OUT/strict_$2.out")
  (cd "$1" && python3 tools/practitioner_harness/harness.py self-check > "$OUT/harness_$2.out" 2>&1; print "exit=$?" >> "$OUT/harness_$2.out")
  (cd "$1" && python3 tools/validation/validate_pec_loop_receipts.py --repo-root . > "$OUT/receipts_$2.out" 2>&1; print "exit=$?" >> "$OUT/receipts_$2.out")
  mkdir -p "$T/closure_$2"
  (cd "$1" && python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir "$T/closure_$2" > "$OUT/closure_$2.out" 2>&1; print "exit=$?" >> "$OUT/closure_$2.out")
  python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); [d.pop(k,None) for k in ("generated_at","timestamp","run_date","output_dir","execution_root")]; print(json.dumps(d,sort_keys=True,indent=1))' "$T/closure_$2/closure_summary.json" > "$OUT/closure_summary_$2.json" 2>>"$OUT/closure_$2.out"
}
check_state() {  # $1 tag: harness and receipts exit 0; closure summary non-empty with 0 cycles
  grep -q '^exit=0$' "$OUT/harness_$1.out" && grep -q '^exit=0$' "$OUT/receipts_$1.out" && note "PASS harness and receipts exit 0 ($1)" || { note "FAIL harness/receipts exit ($1)"; fail=1; }
  python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); assert d and d.get("checks",{}).get("circular_dependencies")=="PASS" and d.get("bidirectional_pair_count")==0' "$OUT/closure_summary_$1.json" 2>/dev/null && note "PASS closure summary non-empty, no cycles, no bidirectional pairs ($1)" || { note "FAIL closure summary ($1)"; fail=1; }
}
compare_state() {  # $1 tag a, $2 tag b, $3 export a, $4 export b
  for k in strict harness receipts closure_summary; do
    ext=out; [[ $k == closure_summary ]] && ext=json
    sed "s#$3#<export>#g" "$OUT/${k}_$1.$ext" > "$T/${k}_$1.norm"; sed "s#$4#<export>#g" "$OUT/${k}_$2.$ext" > "$T/${k}_$2.norm"
    cmp -s "$T/${k}_$1.norm" "$T/${k}_$2.norm" && note "PASS $k identical $1/$2, export root normalized" || { note "FAIL $k differs $1/$2"; fail=1; }
  done
}
run_state "$PRE" pre
check_state pre

# 2. option A: check-only, apply, second run
(cd "$POST" && python3 "$PREP/apply_k2.py" --repo . --candidates "$PREP/candidates" --check-only > "$OUT/apply_checkonly.out" 2>&1; print "exit=$?" >> "$OUT/apply_checkonly.out")
(cd "$POST" && python3 "$PREP/apply_k2.py" --repo . --candidates "$PREP/candidates" > "$OUT/apply.out" 2>&1; print "exit=$?" >> "$OUT/apply.out")
(cd "$POST" && python3 "$PREP/apply_k2.py" --repo . --candidates "$PREP/candidates" > "$OUT/apply_rerun.out" 2>&1; print "exit=$?" >> "$OUT/apply_rerun.out")
grep -q '^exit=0$' "$OUT/apply_checkonly.out" && grep -q '^exit=0$' "$OUT/apply.out" && grep -q '^exit=1$' "$OUT/apply_rerun.out" \
  && note "PASS act A: check-only 0, apply 0, rerun refuses 1" || { note "FAIL act A"; fail=1; }

# 3. containment: the exports differ by exactly the two new contracts
diff -rq -x .git "$PRE" "$POST" > "$OUT/containment.out" 2>&1
n=$(grep -c . "$OUT/containment.out"); nnew=$(grep -cE "^Only in $POST/.*: ScopeOfWork.md$" "$OUT/containment.out")
[[ $n -eq 2 && $nnew -eq 2 ]] && note "PASS containment: 2 new files, both ScopeOfWork.md" || { note "FAIL containment ($n differing, $nnew new SOW)"; fail=1; }

# 4. per-contract validation, checklist (twice), boundary owners
for d in $D86 $D13; do
  id=${${d:t}[1,9]}
  (cd "$POST" && python3 tools/scope_of_work/validate_scope_of_work.py "$d" > "$OUT/validate_$id.out" 2>&1; print "exit=$?" >> "$OUT/validate_$id.out")
  grep -q '^PASS format=SOW_V1' "$OUT/validate_$id.out" && note "PASS validate $id" || { note "FAIL validate $id"; fail=1; }
  (cd "$POST" && python3 tools/scope_of_work/derive_review_checklist.py --output "$OUT/checklist_$id.json" "$d" > "$OUT/checklist_$id.out" 2>&1; print "exit=$?" >> "$OUT/checklist_$id.out")
  (cd "$POST" && python3 tools/scope_of_work/derive_review_checklist.py --output "$T/checklist_$id.2.json" "$d" > /dev/null 2>&1)
  cmp -s "$OUT/checklist_$id.json" "$T/checklist_$id.2.json" && grep -q '^exit=0$' "$OUT/checklist_$id.out" && note "PASS checklist $id (rerun byte-identical)" || { note "FAIL checklist $id"; fail=1; }
  (cd "$POST" && python3 tools/scope_of_work/check_boundary_owner_resolution.py --json "$OUT/boundary_$id.json" --show-not-checkable "$d/ScopeOfWork.md" > "$OUT/boundary_$id.out" 2>&1; print "exit=$?" >> "$OUT/boundary_$id.out")
  grep -qE 'UNRESOLVED_OWNER|UNDEFINED_CLAIM' "$OUT/boundary_$id.out" && { note "FAIL boundary $id"; fail=1; } || { grep -q '^exit=0$' "$OUT/boundary_$id.out" && note "PASS boundary $id (no UNRESOLVED_OWNER/UNDEFINED_CLAIM)" || { note "FAIL boundary $id exit"; fail=1; } }
  grep -q 'per-act exclusions for skill QA: 0 ' "$OUT/boundary_$id.out" && note "PASS boundary $id: 0 NOT_CHECKABLE" || { note "FAIL boundary $id: NOT_CHECKABLE present"; fail=1; }
  # checklist item count equals the number of AC definitions in the contract
  nac=$(grep -cE '^- \*\*AC-[0-9]{3}\*\*' "$POST/$d/ScopeOfWork.md")
  nitem=$(python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); it=d.get("items", d.get("checklist", d if isinstance(d, list) else [])); print(len(it))' "$OUT/checklist_$id.json" 2>/dev/null)
  [[ -n "$nitem" && "$nitem" == "$nac" ]] && note "PASS checklist $id: $nitem items = $nac AC" || { note "FAIL checklist $id item count ($nitem vs $nac AC)"; fail=1; }
  print -r -- "checklist $id sha256 $(shasum -a 256 "$OUT/checklist_$id.json" | cut -c1-64)" >> "$OUT/SUMMARY.out"
done

# 5. quotes (two-sided; tree quotations pinned to the observation commit), state claims,
#    qualified citations, old-S2 text
python3 "$PREP/verify_k2_quotes.py" --tree "$POST" --gitdir "$REPO" --prep "$PREP" --observation "$OBS" > "$OUT/verify_quotes.out" 2>&1; r=$?
note "$( [[ $r -eq 0 ]] && print PASS || print FAIL ) quotes: $(tail -1 "$OUT/verify_quotes.out") ($(grep '^INFO' "$OUT/verify_quotes.out" | tr '\n' ' '))"; [[ $r -eq 0 ]] || fail=1
python3 "$PREP/verify_k2_state_claims.py" --gitdir "$REPO" --prep "$PREP" > "$OUT/verify_state_claims.out" 2>&1; r=$?
note "$( [[ $r -eq 0 ]] && print PASS || print FAIL ) state claims: $(tail -1 "$OUT/verify_state_claims.out")"; [[ $r -eq 0 ]] || fail=1
python3 "$PREP/check_cited_ids.py" --prep "$PREP" --gitdir "$REPO" --commit "$OBS" > "$OUT/check_cited_ids.out" 2>&1; r=$?
note "$( [[ $r -eq 0 ]] && print PASS || print FAIL ) cited IDs: $(tail -1 "$OUT/check_cited_ids.out")"; [[ $r -eq 0 ]] || fail=1
python3 "$PREP/scan_old_s2_text.py" --prep "$PREP" --gitdir "$REPO" --prior ce934ac33 --current "$OBS" > "$OUT/scan_old_s2_text.out" 2>&1; r=$?
note "$( [[ $r -eq 0 ]] && print PASS || print FAIL ) old S2 text: $(tail -1 "$OUT/scan_old_s2_text.out")"; [[ $r -eq 0 ]] || fail=1

# 6. after-A state identical to before (D-GOV-48: identical, not 0/0)
run_state "$POST" postA
check_state postA
compare_state pre postA "$PRE" "$POST"

# 7. add-on C8 (after A): check-only, apply, rerun; containment; state identical
(cd "$POST" && python3 "$PREP/apply_k2_c8.py" --repo . --candidates "$PREP/addons/C8" --check-only > "$OUT/c8_checkonly.out" 2>&1; print "exit=$?" >> "$OUT/c8_checkonly.out")
(cd "$POST" && python3 "$PREP/apply_k2_c8.py" --repo . --candidates "$PREP/addons/C8" > "$OUT/c8_apply.out" 2>&1; print "exit=$?" >> "$OUT/c8_apply.out")
(cd "$POST" && python3 "$PREP/apply_k2_c8.py" --repo . --candidates "$PREP/addons/C8" > "$OUT/c8_rerun.out" 2>&1; print "exit=$?" >> "$OUT/c8_rerun.out")
grep -q '^exit=0$' "$OUT/c8_checkonly.out" && grep -q '^exit=0$' "$OUT/c8_apply.out" && grep -q '^exit=1$' "$OUT/c8_rerun.out" \
  && note "PASS add-on C8: check-only 0, apply 0, rerun refuses 1" || { note "FAIL add-on C8"; fail=1; }
diff -rq -x .git "$PRE" "$POST" > "$OUT/containment_c8.out" 2>&1
n=$(grep -c . "$OUT/containment_c8.out"); nd=$(grep -c "_DEPENDENCIES.md differ$" "$OUT/containment_c8.out")
[[ $n -eq 3 && $nd -eq 1 ]] && note "PASS containment after C8: 2 new contracts + 1 modified _DEPENDENCIES.md" || { note "FAIL containment after C8 ($n)"; fail=1; }
run_state "$POST" postC8
check_state postC8
compare_state pre postC8 "$PRE" "$POST"

# 8. whitespace in the candidates and the C8 postimage
ws=0
for f in "$PREP"/candidates/**/ScopeOfWork.md "$PREP"/addons/C8/**/_DEPENDENCIES.md; do
  grep -nE ' +$|	' "$f" && ws=1
  [[ -n "$(tail -c1 "$f")" ]] && { print "no final newline: $f"; ws=1; }
done > "$OUT/whitespace.out" 2>&1
[[ $ws -eq 0 ]] && note "PASS whitespace" || { note "FAIL whitespace"; fail=1; }

# 9. fault injection on a fresh export
python3 "$PREP/test_apply_k2.py" "$PRE" "$PREP/candidates" "$PREP/addons/C8" > "$OUT/test_apply_k2.out" 2>&1; r=$?
note "$( [[ $r -eq 0 ]] && print PASS || print FAIL ) fault injection: $(tail -1 "$OUT/test_apply_k2.out")"; [[ $r -eq 0 ]] || fail=1

rm -rf "$T"
note "OVERALL $( [[ $fail -eq 0 ]] && print PASS || print FAIL )"
exit $fail
