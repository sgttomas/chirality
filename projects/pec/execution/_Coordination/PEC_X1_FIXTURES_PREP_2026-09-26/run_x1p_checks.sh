#!/bin/zsh
# Run every X1 preparation check on fresh `git archive` exports (never on a checkout).
# Usage: run_x1p_checks.sh <repo (for git objects)> <commit> <prep dir> <out dir>
# Writes all outputs under <out dir>; prints a summary; exit 0 only if every check passes.
set -u
REPO=$1; C=$2; PREP=${3:A}; OUT=${4:A}
export PYTHONDONTWRITEBYTECODE=1
mkdir -p "$OUT"
T=$(mktemp -d "${TMPDIR:-/tmp}/x1pchk.XXXXXX")
PRE=$T/pre; POST=$T/post; mkdir -p "$PRE" "$POST"
git -C "$REPO" archive "$C" | tar -x -C "$PRE"
git -C "$REPO" archive "$C" | tar -x -C "$POST"
# Each export gets a Git identity whose object store borrows the source repository's
# objects (alternates), with HEAD at <commit>; nothing is written to <repo>.
OBJ=$(cd "$REPO" && cd "$(git rev-parse --git-common-dir)" && pwd)/objects
SHA=$(git -C "$REPO" rev-parse "$C^{commit}")
for d in "$PRE" "$POST"; do
  git -C "$d" init -q && print -r -- "$OBJ" > "$d/.git/objects/info/alternates" && git -C "$d" update-ref HEAD "$SHA"
done
fail=0
note() { print -r -- "$1" | tee -a "$OUT/SUMMARY.out"; }
: > "$OUT/SUMMARY.out"
note "basis commit: $SHA"
note "python: $(python3 --version 2>&1); git: $(git --version)"
CHECKS=(v2-parsers v2-core-posture v2-api-contract v2-loop-registry v2-store-guard harness-self-check)

# 1. before-state every-PR, register and registered checks
(cd "$PRE" && python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution > "$OUT/strict_pre.out" 2>&1; print "exit=$?" >> "$OUT/strict_pre.out")
(cd "$PRE" && python3 tools/practitioner_harness/harness.py self-check > "$OUT/harness_pre.out" 2>&1; print "exit=$?" >> "$OUT/harness_pre.out")
(cd "$PRE" && python3 tools/validation/validate_pec_loop_receipts.py --repo-root . > "$OUT/receipts_pre.out" 2>&1; print "exit=$?" >> "$OUT/receipts_pre.out")
(cd "$PRE/projects/pec" && python3 v2/tools/check_service_core_posture.py --config v2/config/service_core_posture.json --workflow software-workflow.json > "$OUT/posture_pre.out" 2>&1; print "exit=$?" >> "$OUT/posture_pre.out")

# 2. the act: check-only, apply, second run
(cd "$POST" && python3 "$PREP/apply_x1p.py" --repo . --candidates "$PREP/candidates" --check-only > "$OUT/apply_checkonly.out" 2>&1; print "exit=$?" >> "$OUT/apply_checkonly.out")
(cd "$POST" && python3 "$PREP/apply_x1p.py" --repo . --candidates "$PREP/candidates" > "$OUT/apply.out" 2>&1; print "exit=$?" >> "$OUT/apply.out")
(cd "$POST" && python3 "$PREP/apply_x1p.py" --repo . --candidates "$PREP/candidates" > "$OUT/apply_rerun.out" 2>&1; print "exit=$?" >> "$OUT/apply_rerun.out")
grep -q '^exit=0$' "$OUT/apply_checkonly.out" && grep -q '^exit=0$' "$OUT/apply.out" && grep -q '^exit=1$' "$OUT/apply_rerun.out" \
  && note "PASS act: check-only 0, apply 0, rerun refuses 1" || { note "FAIL act"; fail=1; }

# 3. containment: the two exports differ by exactly the tabled targets
diff -rq -x .git "$PRE" "$POST" > "$OUT/containment.out" 2>&1
nmod=$(grep -c ' differ$' "$OUT/containment.out"); nnew=$(grep -c '^Only in ' "$OUT/containment.out")
grep -q 'projects/pec/software-workflow.json and .* differ$' "$OUT/containment.out" && okmod=1 || okmod=0
grep -q "^Only in $POST/projects/pec/v2/tests: parsers$" "$OUT/containment.out" && oknew=1 || oknew=0
created=$(cd "$POST" && find projects/pec/v2/tests/parsers -type f | wc -l | tr -d ' ')
[[ $nmod -eq 1 && $okmod -eq 1 && $nnew -eq 1 && $oknew -eq 1 && $created -eq 34 ]] \
  && note "PASS containment: software-workflow.json modified; new directory v2/tests/parsers with 34 files; nothing else" \
  || { note "FAIL containment (modified $nmod, new entries $nnew, created files $created)"; fail=1; }

# 4. affected-check selection and registered checks after the act
(cd "$POST/projects/pec" && python3 ../../tools/software_workflow/select_affected_checks.py software-workflow.json software-workflow.json v2/tests/parsers/test_parser_fixture_integrity.py v2/tests/parsers/fixtures/pinned/MANIFEST.json > "$OUT/select_affected.out" 2>&1; print "exit=$?" >> "$OUT/select_affected.out")
note "INFO affected checks: $(python3 -c 'import json,sys; t=open(sys.argv[1]).read(); print(" ".join(json.loads(t[:t.rfind("exit=")])["checks"]))' "$OUT/select_affected.out" 2>/dev/null)"
(cd "$POST/projects/pec" && python3 ../../tools/software_workflow/run_registered_checks.py software-workflow.json $(for c in $CHECKS; do print -- "--check $c"; done) --output "$POST/registered_post.json" > "$OUT/registered_post.out" 2>&1; print "exit=$?" >> "$OUT/registered_post.out"; cp "$POST/registered_post.json" "$OUT/registered_post.json")
python3 - "$OUT/registered_post.json" > "$OUT/registered_post.summary" 2>&1 <<'PY'
import json, sys
d = json.load(open(sys.argv[1]))
res = d.get("results", d.get("checks", []))
if isinstance(res, dict): res = [dict(id=k, **v) for k, v in res.items()]
bad = 0
for r in res:
    rc = r.get("exit_code", r.get("returncode"))
    print(f"{r.get('id', r.get('check'))} exit={rc}")
    bad += rc != 0
print("ALL_ZERO" if not bad and res else "NONZERO")
PY
grep -q '^ALL_ZERO$' "$OUT/registered_post.summary" && note "PASS registered checks after the act: $(grep -v ALL_ZERO "$OUT/registered_post.summary" | tr '\n' ' ')" || { note "FAIL registered checks: $(cat "$OUT/registered_post.summary" | tr '\n' ' ')"; fail=1; }
(cd "$POST/projects/pec" && python3 -m unittest discover -s v2/tests/parsers -p 'test_*.py' -v > "$OUT/v2_parsers_verbose.out" 2>&1; print "exit=$?" >> "$OUT/v2_parsers_verbose.out")
grep -q '^exit=0$' "$OUT/v2_parsers_verbose.out" && note "PASS v2-parsers verbose: $(grep -c ' ... ok$' "$OUT/v2_parsers_verbose.out") tests ok" || { note "FAIL v2-parsers verbose"; fail=1; }

# 5. bindings and pins
python3 "$PREP/verify_x1p_bindings.py" "$REPO" "$C" "$PREP/candidates" > "$OUT/verify_bindings.out" 2>&1; rb=$?
note "$( [[ $rb -eq 0 ]] && print PASS || print FAIL ) bindings: $(tail -1 "$OUT/verify_bindings.out")"; [[ $rb -eq 0 ]] || fail=1
python3 "$PREP/report_x1p_pins.py" "$REPO" "$C" "$PREP/candidates/projects/pec/v2/tests/parsers/fixtures/pinned/MANIFEST.json" > "$OUT/pins.md" 2>&1; rp=$?
note "$( [[ $rp -eq 0 ]] && print PASS || print FAIL ) pins: $(tail -1 "$OUT/pins.md")"; [[ $rp -eq 0 ]] || fail=1

# 6. after-state registers and every-PR checks identical to before
(cd "$POST" && python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution > "$OUT/strict_post.out" 2>&1; print "exit=$?" >> "$OUT/strict_post.out")
(cd "$POST" && python3 tools/practitioner_harness/harness.py self-check > "$OUT/harness_post.out" 2>&1; print "exit=$?" >> "$OUT/harness_post.out")
(cd "$POST" && python3 tools/validation/validate_pec_loop_receipts.py --repo-root . > "$OUT/receipts_post.out" 2>&1; print "exit=$?" >> "$OUT/receipts_post.out")
for k in strict harness receipts; do
  sed "s#$PRE#<export>#g" "$OUT/${k}_pre.out" > "$T/${k}_pre.norm"; sed "s#$POST#<export>#g" "$OUT/${k}_post.out" > "$T/${k}_post.norm"
  cmp -s "$T/${k}_pre.norm" "$T/${k}_post.norm" && note "PASS $k identical before/after, export root normalized ($(tail -1 "$OUT/${k}_post.out"))" || { note "FAIL $k differs"; fail=1; }
done

# 7. candidate hygiene: UTF-8 with U+2014 as the only non-ASCII character; LF; no tabs or
#    trailing blanks; final newline. Plus the carried FX-PEC-0 constraint, checked once on the
#    candidate bytes at preparation (no committed test scans for it).
python3 - "$PREP/candidates" > "$OUT/hygiene.out" 2>&1 <<'PY'
import sys, pathlib
bad = 0
for p in sorted(pathlib.Path(sys.argv[1]).rglob("*")):
    if not p.is_file(): continue
    b = p.read_bytes(); t = b.decode("utf-8")
    probs = []
    if any(ord(ch) > 127 and ch != "—" for ch in t): probs.append("non-ASCII other than U+2014")
    if b"\r" in b: probs.append("CR")
    if b"\t" in b: probs.append("tab")
    if any(l.endswith(" ") for l in t.split("\n")): probs.append("trailing blank")
    if not b.endswith(b"\n"): probs.append("no final newline")
    if "remaining" in t.lower(): probs.append("carried-constraint word present")
    if probs: bad += 1; print(p, probs)
print("RESULT", "PASS" if not bad else "FAIL")
PY
grep -q 'RESULT PASS' "$OUT/hygiene.out" && note "PASS candidate hygiene and carried-constraint word absent" || { note "FAIL hygiene"; fail=1; }

# 8. fault injection on a fresh export
python3 "$PREP/test_apply_x1p.py" "$PRE" "$PREP/candidates" > "$OUT/test_apply_x1p.out" 2>&1; rt=$?
note "$( [[ $rt -eq 0 ]] && print PASS || print FAIL ) fault injection: $(tail -1 "$OUT/test_apply_x1p.out")"; [[ $rt -eq 0 ]] || fail=1

# 9. negative controls of the fixture suite
zsh "$PREP/negative_controls_x1p.sh" "$REPO" "$C" "$PREP" > "$OUT/negative_controls.out" 2>&1; rn=$?
note "$( [[ $rn -eq 0 ]] && print PASS || print FAIL ) negative controls: $(tail -1 "$OUT/negative_controls.out")"; [[ $rn -eq 0 ]] || fail=1

rm -rf "$T"
note "OVERALL $( [[ $fail -eq 0 ]] && print PASS || print FAIL )"
exit $fail
