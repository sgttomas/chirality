#!/bin/zsh
# D-PEC-95 prototype runner (scratch only). Usage: run_prototypes.sh <mktemp_dir> <h9_dir>
#   <mktemp_dir>/base    : git archive export of 13df8b795 (never written)
#   <mktemp_dir>/gitmeta : git clone --shared of the repository, detached at 13df8b795 (scratch)
# Every proto* tree is an APFS clone (cp -Rc) of base. Nothing touches the real checkout.
set -u
M=$1; H=$2; E=$M/ev; mkdir -p $E
export PYTHONDONTWRITEBYTECODE=1
G=$H/gen_d95.py; D=2026-09-25
log() { print -r -- "$1	$2	$3" >> $E/RESULTS.tsv; }
: > $E/RESULTS.tsv
rm -rf $M/protoA $M/protoA2 $M/protoP $M/protoAR $M/protoR
for v in protoA protoA2 protoP protoAR protoR; do cp -Rc $M/base $M/$v; done
python3 $G --repo $M/protoA  --act-date $D            > $E/genA.tsv  2> $E/genA.err;  log genA  $? "option A"
python3 $G --repo $M/protoA2 --act-date $D            > $E/genA2.tsv 2> $E/genA2.err; log genA2 $? "option A, second fresh clone"
python3 $G --repo $M/protoP  --act-date $D --option P > $E/genP.tsv  2> $E/genP.err;  log genP  $? "option P"
python3 $G --repo $M/protoAR --act-date $D --retired-covers > $E/genAR.tsv 2> $E/genAR.err; log genAR $? "option A + add-on R"
python3 $G --repo $M/protoR  --act-date 2026-09-26 --reproduction > $E/genR.tsv 2> $E/genR.err; log genR $? "option A at another date (slot rule)"
cmp -s $E/genA.tsv $E/genA2.tsv; log det_report $? "reports A vs A2 identical (0 = identical)"
diff -rq $M/protoA/projects $M/protoA2/projects > /dev/null; log det_tree $? "trees A vs A2 identical (0 = identical)"
python3 $G --repo $M/protoA --act-date $D > $E/genA_rerun.tsv 2> $E/genA_rerun.err; log rerun $? "rerun on applied tree (expect 1)"
python3 $G --repo $M/base --act-date 2026-09-26 > /dev/null 2> $E/gen_wrongdate.err; log wrongdate $? "act date != local date (expect 1)"
python3 $G --repo $M/base --act-date $D --check-only > $E/gen_checkonly.tsv 2> $E/gen_checkonly.err; log checkonly $? "check-only on base"
diff -rq $M/base/projects $M/fresh/projects > /dev/null 2>&1; log base_untouched $? "base projects/ equals a fresh export (0 = equal)"
for v in protoA protoP protoAR; do
  (cd $M/$v && python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict > $E/${v}_strict.out 2>&1); log ${v}_strict $? "strict registers"
  (cd $M/$v && python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir $E/${v}_closure > /dev/null 2>&1); log ${v}_closure $? "closure"
  cmp -s $E/base_closure/closure_summary.json $E/${v}_closure/closure_summary.json; log ${v}_closure_same $? "closure_summary equals base (0 = equal)"
  cmp -s $E/base_strict.out $E/${v}_strict.out; log ${v}_strict_same $? "strict output equals base (0 = equal)"
done
python3 $H/verify_d95.py $M/base $M/protoA  --option A > $E/verify_A.out;  log verify_A $? "postimage checks"
python3 $H/verify_d95.py $M/base $M/protoP  --option P > $E/verify_P.out;  log verify_P $? "postimage checks"
python3 $H/verify_d95.py $M/base $M/protoAR --option A --retired-covers > $E/verify_AR.out; log verify_AR $? "postimage checks"
python3 $H/verify_d95.py $M/base $M/base > /dev/null; log verify_sanity $? "verify base against itself (expect 1)"
# git-based checks in the shared clone
(cd $M/gitmeta && git reset --quiet --hard 13df8b795e47ab2284018eeefc9d5473d00c232d && git clean -qfd)
(cd $M/gitmeta && git status --short | wc -l | tr -d ' ' > $E/G_pre_status_count.txt)
(cd $M/gitmeta && python3 tools/validation/validate_pec_loop_receipts.py --repo-root . > $E/G_pre_receipts.out 2>&1); log pre_receipts $? "receipts validator, pre-state"
(cd $M/gitmeta && python3 tools/practitioner_harness/harness.py self-check > $E/G_pre_harness.out 2>&1); log pre_harness $? "harness self-check, pre-state"
for R in REGISTER.csv REGISTER_CLOSED.csv; do
  (cd $M/gitmeta && python3 tools/taskmgmt/taskmgmt.py validate --register projects/pec/execution/_Coordination/_TaskManagement/$R > $E/pre_validate_$R.out 2>&1); log pre_validate_$R $? "taskmgmt validate, pre-state"
done
(cd $M/gitmeta && python3 $G --repo "$(git rev-parse --show-toplevel)" --act-date $D > $E/genG.tsv 2> $E/genG.err); log genG $? "option A in git clone"
diff <(cut -f1,2,3,4 $E/genG.tsv) <(cut -f1,2,3,4 $E/genA.tsv) > /dev/null; log genG_same $? "git-clone report equals protoA report (0 = equal)"
(cd $M/gitmeta && git diff --name-only | sort > $E/G_changed.txt; grep '^WRITE' $E/genG.tsv | cut -f2 | sort | diff -q - $E/G_changed.txt > /dev/null); log containment $? "changed paths == write set (0 = equal)"
(cd $M/gitmeta && git diff --check > $E/G_diffcheck.out); log diffcheck $? "git diff --check (.gitattributes in force)"
(cd $M/gitmeta && python3 tools/validation/validate_pec_loop_receipts.py --repo-root . > $E/G_post_receipts.out 2>&1); log receipts $? "receipts validator"
(cd $M/gitmeta && python3 tools/practitioner_harness/harness.py self-check > $E/G_post_harness.out 2>&1); log harness $? "harness self-check"
cmp -s $E/G_pre_harness.out $E/G_post_harness.out; log harness_same $? "harness output equals pre-state (0 = equal)"
cmp -s $E/G_pre_receipts.out $E/G_post_receipts.out; log receipts_same $? "receipts output equals pre-state (0 = equal)"
(cd $M/gitmeta && python3 $H/t1_tm_pec_023.py --repo . --act-date $D > $E/t1.tsv 2>&1); log t1 $? "T1 row closure"
for R in REGISTER.csv REGISTER_CLOSED.csv; do
  (cd $M/gitmeta && python3 tools/taskmgmt/taskmgmt.py validate --register projects/pec/execution/_Coordination/_TaskManagement/$R > $E/t1_validate_$R.out 2>&1); log t1_validate_$R $? "taskmgmt validate after close"
done
(cd $M/gitmeta && python3 tools/taskmgmt/taskmgmt.py archive --register projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv > $E/t1_archive.out 2>&1); log t1_archive $? "taskmgmt archive"
for R in REGISTER.csv REGISTER_CLOSED.csv; do
  (cd $M/gitmeta && python3 tools/taskmgmt/taskmgmt.py validate --register projects/pec/execution/_Coordination/_TaskManagement/$R > $E/t1_validate2_$R.out 2>&1); log t1_validate2_$R $? "taskmgmt validate after archive"
done
(cd $M/gitmeta && shasum -a 256 projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv projects/pec/execution/_Coordination/_TaskManagement/REGISTER_CLOSED.csv > $E/t1_hashes.txt)
(cd $M/gitmeta && git diff -- ':!projects/pec/execution/_Coordination/_TaskManagement' > $E/optionA_vs_13df8b795.diff; git diff -- projects/pec/execution/_Coordination/_TaskManagement > $E/T1_vs_13df8b795.diff)
diff -ru $M/protoA/projects/pec $M/protoP/projects/pec > $E/optionP_vs_optionA.diff; log diffP $? "P vs A diff written (1 = differences)"
diff -ru $M/protoA/projects/pec $M/protoAR/projects/pec > $E/addonR_vs_optionA.diff; log diffR $? "A+R vs A diff written (1 = differences)"
