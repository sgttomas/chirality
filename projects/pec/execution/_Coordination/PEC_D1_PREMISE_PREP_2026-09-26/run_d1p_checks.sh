#!/bin/zsh
# Run every D1 premise-amendment (provisional D-PEC-105) preparation check on fresh
# `git archive` exports (never on a checkout). Adapted from run_s4p_checks.sh.
# Usage: run_d1p_checks.sh <repo (for git objects)> <commit> <prep dir> <out dir> [observation commit, default 6c6cc1b00]
#   <prep dir> holds targets.json, candidates/, premise/, quotes/, claims/, the rendered
#   apply_d1p.py and the aids (apply_d1p.template.py, build_apply_d1p.py, test_apply_d1p.py,
#   render_candidates.py, verify_d1p_quotes.py, verify_d1p_state_claims.py,
#   check_quote_currency.py, scan_external_quotes.py).
# Three exports of <commit>: PRE (untouched), POST_A (act without add-on P) and POST_AP
# (act with add-on P). Scratch lives in a mktemp -d directory under $TMPDIR, removed at exit
# (set D1P_KEEP=1 to keep it). Writes all outputs under <out dir>, prints a summary to
# <out dir>/SUMMARY.out ending `OVERALL PASS|FAIL`; exit 0 only if every check passes.
# Nothing is written to <repo> or <prep dir>.
set -u
REPO=$1; C=$2; PREP=${3:A}; OUT=${4:A}; OBS=${5:-6c6cc1b00}
export PYTHONDONTWRITEBYTECODE=1
mkdir -p "$OUT"
T=$(mktemp -d "${TMPDIR:-/tmp}/d1pchk.XXXXXX")
[[ ${D1P_KEEP:-0} == 1 ]] || trap 'rm -rf "$T"' EXIT
PRE=$T/pre; PA=$T/post_a; PAP=$T/post_ap; mkdir -p "$PRE"
git -C "$REPO" archive "$C" | tar -x -C "$PRE"
# POST exports: an APFS clone of PRE when available (copy-on-write, byte-identical, saves
# ~2 GB each), otherwise a second and third `git archive`. The act replaces files by rename,
# so a clone shares no written bytes with PRE.
for d in "$PA" "$PAP"; do
  cp -Rpc "$PRE" "$d" 2>/dev/null || { rm -rf "$d"; mkdir -p "$d"; git -C "$REPO" archive "$C" | tar -x -C "$d"; }
done
# Give each export a Git identity without a second checkout: an empty repository whose
# object store borrows the source repository's objects (alternates), with HEAD at <commit>.
OBJ=$(cd "$REPO" && cd "$(git rev-parse --git-common-dir)" && pwd)/objects
SHA=$(git -C "$REPO" rev-parse "$C^{commit}")
for d in "$PRE" "$PA" "$PAP"; do
  git -C "$d" init -q && print -r -- "$OBJ" > "$d/.git/objects/info/alternates" && git -C "$d" update-ref HEAD "$SHA"
done
fail=0
: > "$OUT/SUMMARY.out"
note() { print -r -- "$1" | tee -a "$OUT/SUMMARY.out"; }
pf() { if [[ $1 -eq 0 ]]; then note "PASS $2"; else note "FAIL $2"; fail=1; fi; }
note "basis commit: $SHA; observation: $OBS"
note "python: $(python3 --version 2>&1)"
note "apply_d1p.py sha256: $(shasum -a 256 "$PREP/apply_d1p.py" | cut -d' ' -f1)"
# targets: key group kind path
TL=$(python3 -c 'import json,sys; [print(t["key"],t["group"],t["kind"],t["path"]) for t in json.load(open(sys.argv[1],encoding="utf-8"))["targets"]]' "$PREP/targets.json")
keys_in() { print -r -- "$TL" | awk -v g="$1" '$2 ~ "^("g")$" {print $1}'; }
paths_in() { print -r -- "$TL" | awk -v g="$1" '$2 ~ "^("g")$" {print $4}' | sort; }

# 0. the bound script is a fresh rendering: same basis, same candidates, same template
B=$(sed -n 's/^# Rendered by build_apply_d1p.py at basis commit \([0-9a-f]\{40\}\) .*/\1/p' "$PREP/apply_d1p.py")
if [[ -n $B ]]; then
  python3 "$PREP/build_apply_d1p.py" --prep "$PREP" --basis "$B" --gitdir "$REPO" --template "$PREP/apply_d1p.template.py" --out "$T/apply_rerender.py" > "$OUT/build_rerender.out" 2>&1
  cmp -s "$T/apply_rerender.py" "$PREP/apply_d1p.py"; pf $? "apply_d1p.py equals a fresh rendering at its basis ${B[1,9]} (template, targets.json, candidates)"
else pf 1 "apply_d1p.py names no basis commit"; fi

# 1. candidates are exactly the premise-ledger renderings; every target has one
python3 "$PREP/render_candidates.py" --gitdir "$REPO" --prep "$PREP" --observation "$OBS" > "$OUT/render_candidates.out" 2>&1; rr=$?
miss=0; for k in $(keys_in 'A|P'); do grep -q "^PASS $k " "$OUT/render_candidates.out" || miss=1; done
[[ $rr -eq 0 && $miss -eq 0 ]]; pf $? "render_candidates check: every target's candidate equals its ledger rendering ($(tail -1 "$OUT/render_candidates.out"))"

# 2. before-state every-PR and register checks
(cd "$PRE" && python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution > "$OUT/strict_pre.out" 2>&1; print "exit=$?" >> "$OUT/strict_pre.out")
(cd "$PRE" && python3 tools/practitioner_harness/harness.py self-check > "$OUT/harness_pre.out" 2>&1; print "exit=$?" >> "$OUT/harness_pre.out")
(cd "$PRE" && python3 tools/validation/validate_pec_loop_receipts.py --repo-root . > "$OUT/receipts_pre.out" 2>&1; print "exit=$?" >> "$OUT/receipts_pre.out")

# 3. the act in both modes: check-only, apply, second run; then containment
for M in A AP; do
  if [[ $M == A ]]; then X=$PA; FLAG=(); G='A'; else X=$PAP; FLAG=(--with-addon-p); G='A|P'; fi
  (cd "$X" && python3 "$PREP/apply_d1p.py" --repo . --candidates "$PREP/candidates" $FLAG --check-only > "$OUT/apply_${M}_checkonly.out" 2>&1; print "exit=$?" >> "$OUT/apply_${M}_checkonly.out")
  (cd "$X" && python3 "$PREP/apply_d1p.py" --repo . --candidates "$PREP/candidates" $FLAG > "$OUT/apply_${M}.out" 2>&1; print "exit=$?" >> "$OUT/apply_${M}.out")
  (cd "$X" && python3 "$PREP/apply_d1p.py" --repo . --candidates "$PREP/candidates" $FLAG > "$OUT/apply_${M}_rerun.out" 2>&1; print "exit=$?" >> "$OUT/apply_${M}_rerun.out")
  grep -q '^exit=0$' "$OUT/apply_${M}_checkonly.out" && grep -q '^CHECK preflight passed' "$OUT/apply_${M}_checkonly.out" \
    && grep -q '^exit=0$' "$OUT/apply_${M}.out" && grep -q '^exit=1$' "$OUT/apply_${M}_rerun.out"
  pf $? "act mode $M: check-only 0 (CHECK preflight passed), apply 0, rerun refuses 1"
  diff -rq -x .git "$PRE" "$X" > "$OUT/containment_${M}.out" 2>&1   # .git is the borrowed-object identity, not tree content
  got=$(sed -n "s#^Files $PRE/\(.*\) and $X/.* differ\$#\1#p" "$OUT/containment_${M}.out" | sort)
  want=$(paths_in "$G")
  nlines=$(grep -c . "$OUT/containment_${M}.out"); nwant=$(print -r -- "$want" | grep -c .)
  [[ "$got" == "$want" && $nlines -eq $nwant ]]
  pf $? "containment mode $M: exactly the $nwant target file(s) differ from PRE ($nlines differing, nothing created or removed)"
done

# 4. Scope of Work targets: validity, checklist (twice, byte-identical), boundary owners (QA 21)
for M in A AP; do
  if [[ $M == A ]]; then X=$PA; G='A'; else X=$PAP; G='A|P'; fi
  print -r -- "$TL" | awk -v g="$G" '$3 == "sow" && $2 ~ "^("g")$" {print $1, $4}' | while read -r k p; do
    d=${p:h}
    (cd "$X" && python3 tools/scope_of_work/validate_scope_of_work.py "$d" > "$OUT/validate_${M}_$k.out" 2>&1; print "exit=$?" >> "$OUT/validate_${M}_$k.out")
    grep -q '^PASS format=SOW_V1' "$OUT/validate_${M}_$k.out" && grep -q '^exit=0$' "$OUT/validate_${M}_$k.out"
    pf $? "validate mode $M $k: $(grep -m1 -E '^(PASS|FAIL)' "$OUT/validate_${M}_$k.out" | cut -d' ' -f1-2)"
    (cd "$X" && python3 tools/scope_of_work/derive_review_checklist.py --output "$OUT/checklist_${M}_$k.json" "$d" > "$OUT/checklist_${M}_$k.out" 2>&1; print "exit=$?" >> "$OUT/checklist_${M}_$k.out")
    (cd "$X" && python3 tools/scope_of_work/derive_review_checklist.py --output "$T/checklist_${M}_$k.2.json" "$d" > /dev/null 2>&1)
    cmp -s "$OUT/checklist_${M}_$k.json" "$T/checklist_${M}_$k.2.json" && grep -q '^exit=0$' "$OUT/checklist_${M}_$k.out"
    pf $? "checklist mode $M $k: exit 0, rerun byte-identical (sha256 $(shasum -a 256 "$OUT/checklist_${M}_$k.json" 2>/dev/null | cut -c1-12))"
    (cd "$X" && python3 tools/scope_of_work/check_boundary_owner_resolution.py --json "$OUT/boundary_${M}_$k.json" --show-not-checkable "$p" > "$OUT/boundary_${M}_$k.out" 2>&1; print "exit=$?" >> "$OUT/boundary_${M}_$k.out")
    ! grep -qE 'UNRESOLVED_OWNER|UNDEFINED_CLAIM' "$OUT/boundary_${M}_$k.out" && grep -q '^exit=0$' "$OUT/boundary_${M}_$k.out"
    pf $? "boundary mode $M $k: exit 0, no UNRESOLVED_OWNER/UNDEFINED_CLAIM ($(grep -c NOT_CHECKABLE "$OUT/boundary_${M}_$k.out") NOT_CHECKABLE line(s) for hand resolution)"
    if [[ $M == AP ]]; then  # informational: the preimage checklist and its diff, for reviewers
      (cd "$PRE" && python3 tools/scope_of_work/derive_review_checklist.py --output "$OUT/checklist_PRE_$k.json" "$d" > /dev/null 2>&1)
      diff -u -L "checklist_PRE_$k.json" -L "checklist_${M}_$k.json" "$OUT/checklist_PRE_$k.json" "$OUT/checklist_${M}_$k.json" > "$OUT/checklist_diff_$k.patch"
      note "INFO checklist diff PRE -> post $k: $(grep -c '^[-+] *"text"' "$OUT/checklist_diff_$k.patch") changed text line(s) (checklist_diff_$k.patch)"
    fi
  done
done

# 5. quotes (two-sided, against the post-act tree with add-on P) and commit-anchored state claims
python3 "$PREP/verify_d1p_quotes.py" --tree "$PAP" --gitdir "$REPO" --prep "$PREP" --observation "$OBS" > "$OUT/verify_quotes.out" 2>&1
pf $? "quotes: $(tail -1 "$OUT/verify_quotes.out")"
python3 "$PREP/verify_d1p_state_claims.py" --gitdir "$REPO" --prep "$PREP" > "$OUT/verify_state_claims.out" 2>&1
pf $? "state claims: $(tail -1 "$OUT/verify_state_claims.out")"

# 6. after-state registers and every-PR checks identical to before (D-GOV-48: identical, not 0/0).
# The exports live at different paths; outputs are compared with each export root replaced
# by the literal <export> (the raw outputs are kept unchanged).
for M in A AP; do
  if [[ $M == A ]]; then X=$PA; else X=$PAP; fi
  (cd "$X" && python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution > "$OUT/strict_post_$M.out" 2>&1; print "exit=$?" >> "$OUT/strict_post_$M.out")
  (cd "$X" && python3 tools/practitioner_harness/harness.py self-check > "$OUT/harness_post_$M.out" 2>&1; print "exit=$?" >> "$OUT/harness_post_$M.out")
  (cd "$X" && python3 tools/validation/validate_pec_loop_receipts.py --repo-root . > "$OUT/receipts_post_$M.out" 2>&1; print "exit=$?" >> "$OUT/receipts_post_$M.out")
  for k in strict harness receipts; do
    sed "s#$PRE#<export>#g" "$OUT/${k}_pre.out" > "$T/${k}_pre.norm"; sed "s#$X#<export>#g" "$OUT/${k}_post_$M.out" > "$T/${k}_post_$M.norm"
    cmp -s "$T/${k}_pre.norm" "$T/${k}_post_$M.norm"
    pf $? "$k identical before/after mode $M, export root normalized ($(grep -E 'WARNING findings|ERROR findings' "$OUT/${k}_post_$M.out" | tr -s ' ' | tr '\n' ';')$(tail -1 "$OUT/${k}_post_$M.out"))"
  done
done

# 7. corpus-wide dependency quote currency (D-PEC-95 rule): identical before/after; no
# ACTIVE row citing a D1 target fails
python3 "$PREP/check_quote_currency.py" --tree "$PRE" --prep "$PREP" > "$OUT/quote_currency_pre.out" 2>&1
for M in A AP; do
  if [[ $M == A ]]; then X=$PA; else X=$PAP; fi
  python3 "$PREP/check_quote_currency.py" --tree "$X" --prep "$PREP" > "$OUT/quote_currency_post_$M.out" 2>&1
  cmp -s "$OUT/quote_currency_pre.out" "$OUT/quote_currency_post_$M.out" && ! grep -q '^FAIL TARGET-cited' "$OUT/quote_currency_post_$M.out"
  pf $? "dependency quote currency identical before/after mode $M ($(grep '^SUMMARY' "$OUT/quote_currency_post_$M.out"); $(tail -1 "$OUT/quote_currency_post_$M.out"))"
done

# 8. informational consequence scan (quotations of the preimages held elsewhere; hash anchors)
python3 "$PREP/scan_external_quotes.py" --tree "$PRE" --prep "$PREP" > "$OUT/scan_external_quotes.out" 2>&1
note "INFO external-quote scan (informational): $(tail -1 "$OUT/scan_external_quotes.out")"

# 9. whitespace (trailing blanks, tabs, CR, missing final newline) in every candidate
ws=0
print -r -- "$TL" | while read -r k g kind p; do
  f="$PREP/candidates/$p"
  [[ -f $f ]] || { print "missing candidate: $k $p"; ws=1; continue; }
  grep -nE $' +$|\t|\r' "$f" | sed "s#^#$k:#" && ws=1
  [[ -n "$(tail -c1 "$f")" ]] && { print "no final newline: $k"; ws=1; }
done > "$OUT/whitespace.out" 2>&1
[[ ! -s "$OUT/whitespace.out" ]]; pf $? "whitespace: no trailing blanks, tabs or CR; final newline ($(print -r -- "$TL" | grep -c .) candidates)"

# 10. unified diffs preimage -> postimage, for reviewers
print -r -- "$TL" | while read -r k g kind p; do
  diff -u -L "a/$p" -L "b/$p" "$PRE/$p" "$PREP/candidates/$p" > "$OUT/diff_$k.patch"
  note "INFO diff_$k.patch (group $g): +$(tail -n +3 "$OUT/diff_$k.patch" | grep -c '^+') -$(tail -n +3 "$OUT/diff_$k.patch" | grep -c '^-') lines"
done

# 11. fault injection on fresh copies of the PRE export
python3 "$PREP/test_apply_d1p.py" "$PRE" "$PREP/candidates" --script "$PREP/apply_d1p.py" > "$OUT/test_apply_d1p.out" 2>&1
pf $? "fault injection: $(tail -1 "$OUT/test_apply_d1p.out")"

note "OVERALL $( [[ $fail -eq 0 ]] && print PASS || print FAIL )"
exit $fail
