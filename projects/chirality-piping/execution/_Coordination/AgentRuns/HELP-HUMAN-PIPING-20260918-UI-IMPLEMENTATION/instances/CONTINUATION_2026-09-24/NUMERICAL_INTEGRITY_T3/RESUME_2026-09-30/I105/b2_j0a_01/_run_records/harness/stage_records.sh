#!/bin/bash
# I105 J0a: stage the evidence records (sanitized to placeholder paths; junit host attributes removed) into S/rec.
WT=WT
S=$WT/scratch/i105_j0a; D=$S/rec/b2_j0a_01/_run_records
rm -rf $S/rec/b2_j0a_01; mkdir -p $D/{merge,pins,suites,census,logs,harness}
san() { /usr/bin/python3 -I $S/bin/sanitize.py "$1" "$2" || echo "SANITIZE FAILED $1"; }
sgz() { san "$1" "$S/tmp/stage.tmp" && gzip -n -c "$S/tmp/stage.tmp" > "$2"; }
# merge
san $S/runs/merge_start.log $D/merge/git_merge_output.log
san $S/out/merge_check.json $D/merge/merge_check.json
sgz $S/out/merge_cc_hand.diff $D/merge/merge_cc_hand.diff.gz
san $S/runs/host_screen_repin.log $D/merge/host_screen_repin.log
san $S/runs/host_screen_vs_main.log $D/merge/host_screen_vs_main.log
grep -v '^HIT' $S/runs/host_screen.log > $S/tmp/hs_tail.txt; san $S/tmp/hs_tail.txt $D/merge/host_screen_range_summary.txt
grep '^HIT' $S/runs/host_screen.log | awk '{print $2}' | cut -d: -f1 | awk -F/ '{print $1"/"$2}' | sort | uniq -c > $D/merge/host_screen_range_hits_by_project.txt
# pins
for f in moved_rows.log moved_rows_all.log; do san $S/runs/$f $D/pins/$f; done
san $S/tmp/newpins.txt $D/pins/new_pins.txt
(cd $S/out/new && shasum -a 256 *.json) > $D/pins/new_successors.sha256
for w in w_cb2.dense_scrutiny w_cb4a.dense_scrutiny w_cb4b.dense_scrutiny c1_range_mechanics.dense_scrutiny rv123_c1_two_mechanics.sparse_interactive rv123_c1_two_mechanics.dense_scrutiny; do
  gzip -n -c $S/out/new/$w.successor.json > $D/pins/$w.successor.new.json.gz; done
sgz $S/runs/dev/j1.log $D/logs/dev_j1_pp_lib_after_merge.log.gz
sgz $S/runs/dev/j2.log $D/logs/dev_j2_pins_before_repin.log.gz
san $S/runs/dev/j3.log $D/logs/dev_j3_pins_after_repin.log
# suites and census
san $S/out/SUITES_CMP.json $D/suites/SUITES_CMP.json
san $S/out/CENSUS_CMP.json $D/census/CENSUS_CMP.json
san $S/out/PROVENANCE.json $D/suites/PROVENANCE.json
san $S/out/PP_H2_VS_H.json $D/suites/PP_H2_VS_H.json
san $S/runs/dev/j4.log $D/logs/dev_j4_s11f_after_row.log
san $S/runs/h2_pp.out $D/logs/h2_pp.out
for t in h b m; do
  sgz $S/out/suites/${t}_vitest.json $D/suites/${t}_vitest.json.gz
  A=host; A=${A}name; sed -E "s/ ${A}=\"[^\"]*\"//g" $S/out/suites/${t}_py.junit.xml > $S/tmp/${t}_py.nohost.xml
  echo "${t}_py host attributes left: $(grep -c "${A}=" $S/tmp/${t}_py.nohost.xml)"
  sgz $S/tmp/${t}_py.nohost.xml $D/suites/${t}_py.junit.xml.gz
  for k in 07m 07n 07nN; do for r in rs ts py; do sgz $S/out/census/${t}_${k}_${r}.jsonl $D/census/${t}_${k}_${r}.jsonl.gz; done; done
  san $S/out/wasm_$t.sha256 $D/logs/wasm_$t.sha256
done
for l in $S/logs/*.log; do sgz $l $D/logs/$(basename $l).gz; done
san $S/runs/j0a_chain.out $D/logs/j0a_chain.out
san $S/out/inputs.sha256 $D/harness/inputs.sha256
for f in $S/bin/*; do san $f $D/harness/$(basename $f); done
find $D -type f | wc -l
