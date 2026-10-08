#!/bin/bash
# RV124: assemble the sanitized evidence folder (placeholders only) from S's logs and analyses.
set -u
S=WT/scratch/rv124_rvq; E=$S/records/evidence; P=WT/venv/bin/python
san() { $P $S/bin/sanitize.py "$1" "$2"; }
sangz() { san "$1" "$2" && gzip -nf "$2"; }
cp $S/ana/audit_b1/audit_controls_g7.out.json $E/chain/audit_b1_controls.json
san $S/logs/audit_b1.txt $E/chain/audit_b1.txt
sangz $S/logs/law_registered_nocapture.log $E/law/law_registered_nocapture.log
grep -E '^test |test result|Running|panicked' $S/logs/reg_suite.out > $S/ana/reg_suite.summary
san $S/ana/reg_suite.summary $E/suite/pp_suite_registered.summary.txt
sangz $S/logs/reg_suite.out $E/suite/pp_suite_registered.log
san $S/logs/chain_reg_suite.log $E/suite/chain_reg_suite.log
for f in $S/logs/wit/*.log; do sangz $f $E/witnesses/$(basename $f); done
san $S/logs/chain_wit.log $E/witnesses/chain_wit_and_challenge.log
san $S/logs/witness_entries.txt $E/witnesses/witness_entries.txt
for f in $S/logs/chal/*.log; do sangz $f $E/challenge/$(basename $f); done
san $S/logs/challenge_entries.txt $E/challenge/challenge_entries.txt
# mutants: the list, the table, and each run's test lines (the compile output is dropped)
$P $S/bin/mutants.py json > $S/ana/mutants_def.json; san $S/ana/mutants_def.json $E/mutants/mutants_def.json
cp $S/ana/mutants.json $E/mutants/mutants_results.json
for f in $S/logs/mut/*.log; do grep -E '^test |test result|panicked at|^site table|unknown file|unlisted|applied|restored|RV124_DEF_O|I104_SQ_DEF_O|I104_SQ_CHALLENGE|assertion' "$f" > $S/ana/mut_trim.txt; san $S/ana/mut_trim.txt "$E/mutants/$(basename "$f" .log).tests.txt"; done
san $S/logs/chain_mut.log $E/mutants/chain_mut.log
# probes
for f in $S/logs/mut/M00.def_o*.log; do grep -E 'RV124_DEF_O_FAILS|I104_SQ_DEF_O|test result' "$f" > $S/ana/p.txt; san $S/ana/p.txt "$E/probes/$(basename "$f" .log | tr ':' '_').txt"; done
[ -f $S/logs/size_probe_run.log ] && san $S/logs/size_probe_run.log $E/probes/size_probe_run.log
$P $S/bin/i51_breakdown.py > $E/probes/b2_k1e3_failing_rows_by_kind.txt
# noncand
for f in noncand_compare.out.json noncand_compare_nomult.out.json; do san $S/ana/$f $E/noncand/$f; done
san $S/logs/chain_py2.log $E/noncand/chain_py2.log
# rss
if [ -d $S/logs/rss ]; then for f in $S/logs/rss/*; do san $f $E/rss/$(basename $f); done; fi
[ -f $S/logs/chain_final.log ] && san $S/logs/chain_final.log $E/rss/chain_final.log
# tools
for f in $S/bin/*; do san $f $E/tools/$(basename $f); done
for f in chain_text.log chain_probe2.log; do san $S/logs/$f $E/chain/$f; done
for t in g5_c3 n5_c1 n5_c2 n5_c3; do san $S/logs/point_$t.txt $E/chain/point_$t.txt; done
san $S/chain/linemap_b1q.out.json $E/chain/linemap_passA_to_b1q.json
echo done
