#!/bin/bash
# I104 SQ: stage G6's records into R/I104/b1_sq_01 with placeholder paths (sanitize_copy.py).
set -euo pipefail
S=WT/scratch/i104_b1_sq; RD=R/I104/b1_sq_01
G=$RD/_run_records/g6
sc() { WT/venv/bin/python $S/bin/sanitize_copy.py "$1" "$2"; }
mkdir -p $G
GIT_OPTIONAL_LOCKS=0 git -C WT/b1-q show 69002bc862 2>/dev/null > $S/tmp/g6_commit.diff; sc $S/tmp/g6_commit.diff $G/g6_commit.diff
sc $S/reg/registration.diff $RD/registration.diff
for c in 1 2 3; do sc $S/runs_n5/g5_c$c/summary.json $G/n5/g5_c$c/summary.json; sc $S/logs/run_n5_c$c.txt $G/n5/g5_c$c/run_point.log; done
sc $S/runs_n5/g5_c3/work/profile_tree.json $G/n5/g5_c3/profile_tree.json
sc $S/runs_n5/g5_c1/work/profile_tree.json $G/n5/g5_c1/profile_tree.json
sc $S/runs_n5/g5_c3/work/producer_caps.caps.out.json $G/n5/g5_c3/producer_caps.caps.out.json
sc $S/runs_n5/g5_c3/cg.out.json $G/n5/g5_c3/cg.out.json
sc $S/mcn_b1q/SQ_N5_PATCHES.json $G/n5/SQ_N5_PATCHES.json
sc $S/g6rec/n5_points.json $G/n5/n5_points.json
for f in sf1_late_form_exact.json deepest_chain_b1_c3.json census_published_inputs.json; do sc $S/g6rec/$f $G/$f; done
sc $S/logs/g6_law_2.log $G/law/g6_law_tests.unregistered.log
sc $S/logs/law_dev.log $G/law/law_tests.registered_dev.log
sc $S/logs/law_rel.log $G/law/law_tests.release.log
diff <(grep "I65_G5_ATOM" $S/logs/g5_law.log | sort) <(grep "I65_G5_ATOM" $S/logs/g6_law_1.log | sort) > $S/tmp/atoms.diff || true; sc $S/tmp/atoms.diff $G/law/atoms_g5_vs_g6.diff
set +e
diff <(grep -E "I65_G5_(ATOM|PHASE|PROFILE|ESTIMATE)" $S/logs/law_dev.log | sed 's/^test [^ ]* \.\.\. //') <(grep -E "I65_G5_(ATOM|PHASE|PROFILE|ESTIMATE)" $S/logs/law_rel.log | sed 's/^test [^ ]* \.\.\. //') > $S/tmp/devrel.diff
rc=$?; set -e
n=$(grep -cE "I65_G5_(ATOM|PHASE|PROFILE|ESTIMATE)" $S/logs/law_rel.log)
echo "the I65_G5_ATOM/PHASE/PROFILE/ESTIMATE lines of the registered dev/test and release law records: diff exit $rc, $(wc -c < $S/tmp/devrel.diff) bytes of difference over $n lines" > $S/tmp/devrel.txt; sc $S/tmp/devrel.txt $G/law/record_dev_vs_release.txt
sc $S/logs/g6_s11f_2.log $G/s11f.log
sc $S/logs/g6_s11f_1.log $G/s11f_probe_before_rows.log
sc $S/logs/reg_pp_suite.log $G/registration/pp_suite.registered.log
sc $S/logs/chain_reg.log $G/registration/chain_reg.log
sc $S/logs/mutant_g04.log $G/mutant_g04.log
for b in dev rel; do for f in $S/wit/$b/*.out; do sc $f $G/witnesses/$b/$(basename $f); done; sc $S/wit/table_$b.json $G/witnesses/table_$b.json; sc $S/logs/witness_$b.log $G/witnesses/witness_$b.log; done
for f in noncand.json noncand_compare.out.json noncand_compare_nomult.out.json whole_nc.out.json; do sc $S/runs_n5/g5_c3/$f $G/noncand/$f; done
sc $S/logs/noncand.log $G/noncand/noncand.log
for f in sq_n5_chain.py chain_n5.sh sf1_exact.py deepest_chain.py mk_regcopy.sh chain_reg.sh witness_chain.sh chain_wit.sh wit_table.py noncand_b1.sh noncand_compare_nomult.py mutant_g04.sh census_inputs.py rss_batch.sh chain_rss.sh mk_rss_lists.py rss_table.py sanitize_copy.py stage_g6.sh; do sc $S/bin/$f $G/tools/$f; done
du -sh $G; find $G -type f | wc -l
# the witness outputs carry the product's cfg(test) debug lines (I51_DUAL_LANES, about 1-3.5 MB each): gzip -n
gzip -n -9 $G/witnesses/dev/*.out $G/witnesses/rel/*.out $G/noncand/whole_nc.out.json
du -sh $G
# RSS_TIME's measurements: lists, outputs (gzip -n), the time -l files, the merged tables; the chain log
for b in devA devB devC rel; do
  sc $S/rss/lists/$b.list $G/rss/lists/$b.list
  for f in $S/rss/$b/*; do sc $f $G/rss/$b/$(basename $f); done
  gzip -n -9 $G/rss/$b/*.out
done
sc $S/rss/merged/dev_table.json $G/rss/dev_table.json; sc $S/rss/merged/rel_table.json $G/rss/rel_table.json; sc $S/rss/merged/tables.md $G/rss/tables.md
sc $S/logs/chain_rss.log $G/rss/chain_rss.log
for f in rss_md.py rss_table.py stage_g6.sh; do sc $S/bin/$f $G/tools/$f; done
sc $S/g6rec/QUAL_B1.md $RD/QUAL_B1.md; sc $S/g6rec/RSS_TIME.md $RD/RSS_TIME.md
du -sh $G; find $RD -type f | wc -l
