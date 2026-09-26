#!/bin/bash
# Provisional D-PEC-101 part K4 prototype runner (scratch only).
# Usage: run_k4_prototypes.sh <work_dir> <k4_dir> <base_export> <repo_worktree>
#   <base_export>   : `git archive` export of aca930622 (never written; only cloned and read)
#   <work_dir>      : scratch; receives APFS clones (cp -Rc) of <base_export> and a
#                     `git clone --shared --no-checkout` of the repository, detached at aca930622
#   <k4_dir>        : holds gen_d101_k4.py, verify_d101_k4.py, tables_k4.py; evidence goes to <k4_dir>/evidence
#   <repo_worktree> : used only to locate the repository for the shared clone (not written)
# RESULTS.tsv rows: step <TAB> exit code <TAB> meaning. Nothing touches the real checkout.
set -u
W=$1; K=$2; BASE=$3; REPO=$4; E=$K/evidence; C=aca930622ba167689881416044ba0feaee3ef003
mkdir -p "$E" "$W"
export PYTHONDONTWRITEBYTECODE=1
G=$K/gen_d101_k4.py; V=$K/verify_d101_k4.py
log() { printf '%s\t%s\t%s\n' "$1" "$2" "$3" >> "$E/RESULTS.tsv"; }
: > "$E/RESULTS.tsv"
python3 --version > "$E/python_version.txt" 2>&1
shasum -a 256 "$G" | sed "s#  .*/#  #" > "$E/generator_sha256.txt"
manifest() { (cd "$1" && find projects -type f -print0 | sort -z | xargs -0 shasum -a 256 | shasum -a 256 | cut -d' ' -f1); }
BASE_M0=$(manifest "$BASE")

rm -rf "$W"/protoA "$W"/protoA2 "$W"/protoAC "$W"/protoCO "$W"/gitmeta
for v in protoA protoA2 protoAC protoCO; do cp -Rc "$BASE" "$W/$v"; done

# 1. generator runs on clones
python3 "$G" --repo "$W/protoA"            > "$E/genA.tsv"  2> "$E/genA.err";  log genA  $? "option A (re-pin) on clone"
python3 "$G" --repo "$W/protoA2"           > "$E/genA2.tsv" 2> "$E/genA2.err"; log genA2 $? "option A on a second fresh clone"
python3 "$G" --repo "$W/protoAC" --covers  > "$E/genAC.tsv" 2> "$E/genAC.err"; log genAC $? "option A + add-on C (--covers) on clone"
cmp -s "$E/genA.tsv" "$E/genA2.tsv"; log det_report $? "reports A vs A2 identical (0 = identical)"
diff -rq "$W/protoA" "$W/protoA2" > /dev/null; log det_tree $? "whole trees A vs A2 identical (0 = identical)"
python3 "$G" --repo "$W/protoA" > "$E/genA_rerun.tsv" 2> "$E/genA_rerun.err"; log rerun $? "rerun on applied tree (expect 1)"
diff -rq "$W/protoA" "$W/protoA2" > /dev/null; log rerun_nothing_written $? "after rerun, tree A still equals A2 (0 = nothing written)"
python3 "$G" --repo "$W/protoCO" --check-only > "$E/gen_checkonly.tsv" 2> "$E/gen_checkonly.err"; log checkonly $? "check-only on clone"
diff -rq "$BASE" "$W/protoCO" > /dev/null; log checkonly_unchanged $? "check-only clone equals base (0 = unchanged)"
python3 "$G" --repo "$W/protoCO" --check-only --covers > "$E/gen_checkonly_covers.tsv" 2> "$E/gen_checkonly_covers.err"; log checkonly_covers $? "check-only --covers on clone"
diff <(grep -v '^RENDER' "$E/gen_checkonly.tsv") <(grep -v '^WRITE' "$E/genA.tsv") > /dev/null; log checkonly_same $? "check-only report equals A report apart from RENDER/WRITE rows (0 = equal)"
diff <(grep '^RENDER' "$E/gen_checkonly.tsv" | cut -f2-) <(grep '^WRITE' "$E/genA.tsv" | cut -f2-) > /dev/null; log checkonly_rows $? "RENDER rows equal WRITE rows of A (0 = equal)"

# 2. independent verifier
python3 "$V" "$BASE" "$W/protoA"           > "$E/verify_A.out"  2>&1; log verify_A  $? "verify A (expect 0)"
python3 "$V" "$BASE" "$W/protoAC" --covers > "$E/verify_AC.out" 2>&1; log verify_AC $? "verify A+C (expect 0)"
python3 "$V" "$BASE" "$BASE"               > "$E/verify_base_vs_base.out" 2>&1; log verify_sanity $? "verify base vs base (expect 1)"
python3 "$V" "$BASE" "$W/protoAC"          > "$E/verify_AC_without_flag.out" 2>&1; log verify_AC_noflag $? "verify A+C without --covers (expect 1: covers flag discipline)"

# 3. strict validator and closure: base, A, A+C
for v in base protoA protoAC; do
  T=$W/$v; [ "$v" = base ] && T=$BASE
  (cd "$T" && python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict > "$E/${v}_strict.out" 2>&1); log ${v}_strict $? "strict registers (expect 1: warnings under --strict)"
  rm -rf "$W/closure_$v"
  (cd "$T" && python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir "$W/closure_$v" > "$E/${v}_closure.out" 2>&1); log ${v}_closure $? "closure (full output in scratch; summary copied)"
  cp "$W/closure_$v/closure_summary.json" "$E/${v}_closure_summary.json"
done
for v in protoA protoAC; do
  cmp -s "$E/base_strict.out" "$E/${v}_strict.out"; log ${v}_strict_same $? "strict output equals base (0 = equal)"
  cmp -s "$E/base_closure_summary.json" "$E/${v}_closure_summary.json"; log ${v}_closure_same $? "closure_summary.json equals base (0 = equal)"
done
for v in base protoA protoAC; do
  e=$(grep -E '^ *ERROR findings: *0$' "$E/${v}_strict.out" | wc -l | tr -d ' ')
  x=$(grep -E '^ *WARNING XRG-013 +26 ' "$E/${v}_strict.out" | wc -l | tr -d ' ')
  d=$(grep -E '^ *WARNING DRB-008 +2 ' "$E/${v}_strict.out" | wc -l | tr -d ' ')
  w=$(grep -E '^ *WARNING findings: *28$' "$E/${v}_strict.out" | wc -l | tr -d ' ')
  [ "$e$x$d$w" = 1111 ]; log ${v}_strict_counts $? "0 ERROR / 26 XRG-013 / 2 DRB-008 / 28 WARNING (0 = as expected)"
done

# 4. whitespace on the written files (A and A+C): no CR, no trailing blanks, single final LF
python3 - "$W/protoA" "$W/protoAC" "$E/genA.tsv" > "$E/whitespace.out" 2>&1 <<'PY'
import sys
from pathlib import Path
bad = 0
paths = [ln.split("\t")[1] for ln in Path(sys.argv[3]).read_text().splitlines() if ln.startswith("WRITE\t")]
for root in sys.argv[1:3]:
    for p in paths:
        b = (Path(root) / p).read_bytes()
        probs = []
        if b"\r" in b: probs.append("CR")
        if not b.endswith(b"\n") or b.endswith(b"\n\n"): probs.append("final newline")
        if any(ln.rstrip(b" \t") != ln for ln in b.split(b"\n")): probs.append("trailing whitespace")
        if probs:
            bad += 1
            print("FAIL", root, p, ",".join(probs))
print(f"checked {len(paths)} files x 2 trees; problems {bad}")
sys.exit(1 if bad else 0)
PY
log whitespace $? "written files: no CR, no trailing whitespace, one final LF (A and A+C)"

# 5. git-based checks in a shared clone detached at aca930622
git clone --quiet --shared --no-checkout "$(git -C "$REPO" rev-parse --path-format=absolute --git-common-dir)" "$W/gitmeta" 2> "$E/G_clone.err"; log G_clone $? "git clone --shared --no-checkout"
(cd "$W/gitmeta" && git checkout --quiet --detach $C 2>> "$E/G_clone.err"); log G_checkout $? "checkout detached at aca930622"
(cd "$W/gitmeta" && git rev-parse HEAD > "$E/G_head.txt")
diff -rq "$BASE/projects" "$W/gitmeta/projects" > "$E/G_base_vs_commit.out" 2>&1; log base_equals_commit $? "BASE projects/ equals the aca930622 checkout (0 = equal)"
(cd "$W/gitmeta" && git status --porcelain | wc -l | tr -d ' ' > "$E/G_pre_status_count.txt")
(cd "$W/gitmeta" && python3 tools/validation/validate_pec_loop_receipts.py --repo-root . > "$E/G_pre_receipts.out" 2>&1); log G_pre_receipts $? "receipts validator, pre-state"
(cd "$W/gitmeta" && python3 tools/practitioner_harness/harness.py self-check > "$E/G_pre_harness.out" 2>&1); log G_pre_harness $? "harness self-check, pre-state"
(cd "$W/gitmeta" && python3 "$G" --repo "$(git rev-parse --show-toplevel)" > "$E/genG.tsv" 2> "$E/genG.err"); log genG $? "option A in the git clone via --repo \$(git rev-parse --show-toplevel)"
cmp -s "$E/genG.tsv" "$E/genA.tsv"; log genG_same $? "git-clone report equals protoA report (0 = equal)"
(cd "$W/gitmeta" && git diff --name-only | LC_ALL=C sort > "$E/G_changed.txt")
grep '^WRITE' "$E/genG.tsv" | cut -f2 | LC_ALL=C sort | diff -q - "$E/G_changed.txt" > /dev/null; log G_containment $? "git diff --name-only equals the write set (0 = equal)"
(cd "$W/gitmeta" && git status --porcelain --untracked-files=all | grep -v '^ M ' | wc -l | tr -d ' ' > "$E/G_untracked_or_other.txt")
[ "$(cat "$E/G_untracked_or_other.txt")" = 0 ]; log G_no_other_status $? "no untracked or non-modify status entries (0 = none)"
(cd "$W/gitmeta" && git diff --check > "$E/G_diffcheck.out" 2>&1); log G_diffcheck $? "git diff --check"
(cd "$W/gitmeta" && git diff -- projects/pec > "$E/optionA_vs_base.diff")
(cd "$W/gitmeta" && python3 tools/validation/validate_pec_loop_receipts.py --repo-root . > "$E/G_post_receipts.out" 2>&1); log G_post_receipts $? "receipts validator, post-state"
(cd "$W/gitmeta" && python3 tools/practitioner_harness/harness.py self-check > "$E/G_post_harness.out" 2>&1); log G_post_harness $? "harness self-check, post-state"
cmp -s "$E/G_pre_receipts.out" "$E/G_post_receipts.out"; log G_receipts_same $? "receipts output identical pre/post (0 = equal)"
cmp -s "$E/G_pre_harness.out" "$E/G_post_harness.out"; log G_harness_same $? "harness output identical pre/post (0 = equal)"
python3 "$V" "$BASE" "$W/gitmeta" > "$E/verify_G.out" 2>&1; log verify_G $? "verify the git-clone post-state (expect 0)"

# 6. K1 tolerance (synthetic): a K1-shaped folder born at revision 1.6 / PRD v2.4 is tolerated by the
#    generator and by `verify --allow-k1`; a stray unpinned context still at revision 1.5 is refused.
#    The synthetic folder copies the DEL-04-03 A2-mirror context and its revision-1.6 reference packet
#    (covers list set to DEL-10-13's register cell, SOW-100); it is not K1's real content.
rm -rf "$W/protoK1" "$W/protoK1bad"; cp -Rc "$BASE" "$W/protoK1"; cp -Rc "$BASE" "$W/protoK1bad"
SRC=projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping
NEWD=projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-13_Synthetic_K1_shaped_folder
mkdir -p "$W/protoK1/$NEWD" "$W/protoK1bad/$NEWD"
cp "$W/protoK1/$SRC/_CONTEXT.md" "$W/protoK1/$NEWD/_CONTEXT.md"
sed -e 's/covers SOW-006;SOW-007)/covers SOW-100)/' "$W/protoA/$SRC/_REFERENCES.md" > "$W/protoK1/$NEWD/_REFERENCES.md"  # DEL-10-13 register cell
python3 "$G" --repo "$W/protoK1" > "$E/genK1.tsv" 2> "$E/genK1.err"; log genK1 $? "synthetic K1-first tree: generator tolerates the new folder (expect 0)"
grep -q 'population_folders	67	1 contexts / 1 references already at 1.6 beyond the pins' "$E/genK1.tsv"; log genK1_population $? "report counts the tolerated folder (0 = as expected)"
diff <(grep '^WRITE' "$E/genK1.tsv") <(grep '^WRITE' "$E/genA.tsv") > /dev/null; log genK1_same_writes $? "same 129 writes and postimages as A (0 = equal)"
python3 "$V" "$BASE" "$W/protoK1" --allow-k1 > "$E/verify_K1_allow.out" 2>&1; log verify_K1_allow $? "verify with --allow-k1 (expect 0)"
python3 "$V" "$BASE" "$W/protoK1" > "$E/verify_K1_noallow.out" 2>&1; log verify_K1_noallow $? "verify without --allow-k1 (expect 1)"
cp "$W/protoK1bad/$SRC/../DEL-04-01"*/_CONTEXT.md "$W/protoK1bad/$NEWD/_CONTEXT.md"
python3 "$G" --repo "$W/protoK1bad" > /dev/null 2> "$E/genK1bad.err"; log genK1bad $? "unpinned context still at revision 1.5 (expect 1)"
diff -rq "$BASE/projects" "$W/protoK1bad/projects" 2>&1 | grep -v "Only in .*PKG-10_Validation_Measurement/1_Working: DEL-10-13_Synthetic_K1_shaped_folder" | wc -l | tr -d ' ' > "$E/genK1bad_other_changes.txt"
[ "$(cat "$E/genK1bad_other_changes.txt")" = 0 ]; log genK1bad_nothing_written $? "refused run wrote nothing (0 = nothing written)"

# 7. diffs and tables
(cd "$W" && diff -ru protoA/projects/pec protoAC/projects/pec > "$W/addonC_raw.diff"); log diff_addonC $? "A+C vs A diff written (1 = differences; file timestamps stripped from ---/+++ lines)"
sed -E 's/^((---|\+\+\+) [^	]*)	.*$/\1/' "$W/addonC_raw.diff" > "$E/addonC_vs_optionA.diff"
python3 "$K/tables_k4.py" "$BASE" "$W/protoA" "$W/protoAC" "$E/genA.tsv" "$E" > "$E/tables.out" 2>&1; log tables $? "grant_table.md, aggregates.txt, census.md"
[ "$(manifest "$BASE")" = "$BASE_M0" ]; log base_untouched $? "BASE projects/ manifest unchanged across the run (0 = unchanged)"
