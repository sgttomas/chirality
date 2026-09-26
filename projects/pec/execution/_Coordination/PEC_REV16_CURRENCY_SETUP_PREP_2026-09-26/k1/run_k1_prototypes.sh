#!/bin/zsh
# D-PEC-101 K1 prototype runner (scratch only; preparation aid).
# Usage: [PRECOMMIT=<sha>] run_k1_prototypes.sh <work_dir> <base_export> <repo_root_for_git_clone> <act_date> [<k4_generator>]
#   <base_export> : git archive export of aca930622 (never written)
# Every proto* tree is an APFS clone (cp -Rc) of base. Nothing touches the real checkout.
set -u
M=$1; BASE=$2; REPO=$3; D=$4; G4=${5:-}
H=${0:A:h}; G=$H/gen_d101_k1.py; V=$H/verify_d101_k1.py
E=$M/ev; rm -rf $M; mkdir -p $E
export PYTHONDONTWRITEBYTECODE=1
log() { print -r -- "$1	$2	$3" >> $E/RESULTS.tsv; }
: > $E/RESULTS.tsv
for v in protoK1 protoK1b protoR protoC; do cp -Rc $BASE $M/$v; done
D2=$(python3 -c "import datetime as d;print((d.date.fromisoformat('$D')+d.timedelta(days=1)).isoformat())")
python3 $G --repo $M/protoK1  --act-date $D > $E/genK1.tsv  2> $E/genK1.err;  log genK1  $? "K1 act"
python3 $G --repo $M/protoK1b --act-date $D > $E/genK1b.tsv 2> $E/genK1b.err; log genK1b $? "K1 act, second fresh clone"
cmp -s $E/genK1.tsv $E/genK1b.tsv; log det_report $? "reports identical (0 = identical)"
diff -rq $M/protoK1/projects $M/protoK1b/projects > /dev/null; log det_tree $? "trees identical (0 = identical)"
python3 $G --repo $M/protoK1 --act-date $D > $E/rerun.tsv 2> $E/rerun.err; log rerun $? "rerun on applied tree (expect 1)"
python3 $G --repo $M/protoC --act-date $D2 > /dev/null 2> $E/wrongdate.err; log wrongdate $? "act date != local date (expect 1)"
python3 $G --repo $M/protoC --act-date $D --check-only > $E/checkonly.tsv 2> $E/checkonly.err; log checkonly $? "check-only"
diff -rq $BASE/projects $M/protoC/projects > /dev/null; log checkonly_untouched $? "check-only tree equals base (0 = equal)"
python3 $G --repo $M/protoR --act-date $D2 --reproduction > $E/genR.tsv 2> $E/genR.err; log genR $? "K1 at another date (slot rule)"
diff -ru $M/protoK1/projects/pec $M/protoR/projects/pec > $E/slot_D_vs_D2.diff; log slot_diff $? "D vs D+1 diff written (1 = differences)"
python3 - $M/protoK1 $M/protoR $D $D2 > $E/slot_rule.out <<'EOF'
import os, sys
a, b, d, d2 = sys.argv[1:]
diff, same_after = [], []
for dp, _, fs in os.walk(os.path.join(a, "projects")):
    for f in fs:
        pa = os.path.join(dp, f); pb = pa.replace(a, b, 1)
        x, y = open(pa, "rb").read(), open(pb, "rb").read()
        if x != y:
            diff.append(pa[len(a) + 1:])
            same_after.append(x.replace(d.encode(), d2.encode()) == y)
print("files differing:", len(diff)); print("identical after substituting the date:", sum(same_after))
for p, s in zip(diff, same_after): print(("OK  " if s else "BAD ") + p)
sys.exit(0 if all(same_after) else 1)
EOF
log slot_rule $? "every difference is the date slot (0 = yes)"
(cd $M/protoK1 && python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict > $E/K1_strict.out 2>&1); log K1_strict $? "strict registers (exit 1 = warnings only)"
(cd $BASE && python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict > $E/base_strict.out 2>&1); log base_strict $? "strict registers on base"
(cd $M/protoK1 && python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir $E/K1_closure > /dev/null 2>&1); log K1_closure $? "closure"
(cd $BASE && python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir $E/base_closure > /dev/null 2>&1); log base_closure $? "closure on base"
for f in $(grep '^WRITE.*Dependencies.csv' $E/genK1.tsv | cut -f2); do
  (cd $M/protoK1 && python3 tools/validation/validate_dependencies_schema.py $f >> $E/K1_schema.out 2>&1); log schema $? "$f"
done
python3 $V $BASE $M/protoK1 > $E/verify_K1.out; log verify_K1 $? "independent postimage checks"
python3 $V $BASE $BASE > /dev/null; log verify_sanity $? "verify base against itself (expect 1)"
(cd $M/protoK1 && diff -ru $BASE/projects/pec projects/pec > $E/K1_vs_base.diff); log diff $? "K1 vs base diff written (1 = differences)"
sed -i '' "s#$BASE/##; s#$M/protoK1/##" $E/K1_vs_base.diff 2>/dev/null || true
# git-backed checks in a shared clone
rm -rf $M/gitmeta; git clone -q --shared --no-checkout $REPO $M/gitmeta
(cd $M/gitmeta && git checkout -q --detach ${PRECOMMIT:-aca930622ba167689881416044ba0feaee3ef003})
(cd $M/gitmeta && python3 tools/validation/validate_pec_loop_receipts.py --repo-root . > $E/G_pre_receipts.out 2>&1); log pre_receipts $? "receipts validator, pre"
(cd $M/gitmeta && python3 tools/practitioner_harness/harness.py self-check > $E/G_pre_harness.out 2>&1); log pre_harness $? "harness self-check, pre"
(cd $M/gitmeta && python3 $G --repo "$(git rev-parse --show-toplevel)" --act-date $D > $E/genG.tsv 2> $E/genG.err); log genG $? "K1 act in git clone"
diff <(cut -f1,2,3,4 $E/genG.tsv) <(cut -f1,2,3,4 $E/genK1.tsv) > /dev/null; log genG_same $? "git-clone report equals protoK1 report (0 = equal)"
(cd $M/gitmeta && git add -A -N . && git diff --name-only | sort > $E/G_changed.txt)
grep '^WRITE' $E/genG.tsv | cut -f2 | sort | diff -q - $E/G_changed.txt > /dev/null; log containment $? "changed paths == write set (0 = equal)"
(cd $M/gitmeta && git diff --check > $E/G_diffcheck.out); log diffcheck $? "git diff --check (.gitattributes in force)"
(cd $M/gitmeta && python3 tools/validation/validate_pec_loop_receipts.py --repo-root . > $E/G_post_receipts.out 2>&1); log post_receipts $? "receipts validator, post"
(cd $M/gitmeta && python3 tools/practitioner_harness/harness.py self-check > $E/G_post_harness.out 2>&1); log post_harness $? "harness self-check, post"
cmp -s $E/G_pre_receipts.out $E/G_post_receipts.out; log receipts_same $? "receipts output equal (0 = equal)"
cmp -s $E/G_pre_harness.out $E/G_post_harness.out; log harness_same $? "harness output equal (0 = equal)"
(cd $M/gitmeta && python3 tools/validation/validate_instruction_entrypoints.py . > $E/G_entry.out 2>&1); log entrypoints $? "instruction entrypoints"
# order independence with K4
if [[ -n $G4 ]]; then
  cp -Rc $BASE $M/protoK4K1; cp -Rc $BASE $M/protoK1K4
  python3 $G4 --repo $M/protoK4K1 > $E/o1_k4.tsv 2> $E/o1_k4.err; log o1_k4 $? "K4 first"
  python3 $G  --repo $M/protoK4K1 --act-date $D > $E/o1_k1.tsv 2> $E/o1_k1.err; log o1_k1 $? "then K1"
  python3 $G  --repo $M/protoK1K4 --act-date $D > $E/o2_k1.tsv 2> $E/o2_k1.err; log o2_k1 $? "K1 first"
  python3 $G4 --repo $M/protoK1K4 > $E/o2_k4.tsv 2> $E/o2_k4.err; log o2_k4 $? "then K4"
  diff -rq $M/protoK4K1/projects $M/protoK1K4/projects > /dev/null; log order_same $? "K4+K1 == K1+K4 trees (0 = equal)"
  (cd $M/protoK1K4 && python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict > $E/both_strict.out 2>&1); log both_strict $? "strict on K1+K4"
  (cd $M/protoK1K4 && python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir $E/both_closure > /dev/null 2>&1); log both_closure $? "closure on K1+K4"
  cmp -s $E/K1_closure/closure_summary.json $E/both_closure/closure_summary.json; log both_closure_same $? "closure equals K1-only (0 = equal)"
  python3 $V $BASE $M/protoK1K4 --allow-k4 > $E/verify_both.out; log verify_both $? "K1 checks on K1+K4 (--allow-k4)"
fi
