#!/bin/bash
# I105 J0b: write the evidence records (sanitized to placeholder paths; junit host attributes removed) directly into
# R/I105/b2_j0b_01/_run_records. RETURN.md and SHA256SUMS are written separately.
WT=WT
S=$WT/scratch/i105_j0b
R=$WT/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30
D=$R/I105/b2_j0b_01/_run_records
rm -rf $D; mkdir -p $D/{merge,t2,b3a,suites,census,probes,logs,harness}
san() { /usr/bin/python3 -I $S/bin/sanitize.py "$1" "$2" || echo "SANITIZE FAILED $1"; }
sgz() { san "$1" "$S/tmp/stage.tmp" && gzip -n -c "$S/tmp/stage.tmp" > "$2"; }
san $S/runs/merge.log $D/merge/git_merge_output.log
for t in h u; do grep "I105_J0B_PROBE" $S/logs/${t}_pp_probe.log > $S/tmp/pp_probe_$t.txt; san $S/tmp/pp_probe_$t.txt $D/b3a/pp_probe_$t.txt; done
for f in nine_files.txt nine_u3.diff nine_b2.diff merge_cc.diff host_screen_range_summary.txt host_screen_vs_u3.log host_screen_arity.log; do
  [ -f $S/out/$f ] && { case $f in *.diff) sgz $S/out/$f $D/merge/$f.gz;; *) san $S/out/$f $D/merge/$f;; esac; }; done
for f in t2_search.txt t2_old_all.txt b2_files.txt retired_fixture_refs.txt; do [ -f $S/out/$f ] && san $S/out/$f $D/t2/$f; done
for f in $S/out/probes/*.jsonl; do san $f $D/probes/$(basename $f); done
san $S/probes/reader_probes.json $D/probes/reader_probes.json
san $S/probes/i105_j0b_probe.rs $D/probes/i105_j0b_probe.rs
for f in SUITES_CMP.json; do san $S/out/$f $D/suites/$f; done
san $S/out/CENSUS_CMP.json $D/census/CENSUS_CMP.json
for t in h u; do
  sgz $S/out/suites/${t}_vitest.json $D/suites/${t}_vitest.json.gz
  A=host; A=${A}name; sed -E "s/ ${A}=\"[^\"]*\"//g" $S/out/suites/${t}_py.junit.xml > $S/tmp/${t}_py.nohost.xml
  echo "${t}_py host attributes left: $(grep -c "${A}=" $S/tmp/${t}_py.nohost.xml)"
  sgz $S/tmp/${t}_py.nohost.xml $D/suites/${t}_py.junit.xml.gz
  for k in 07m 07n 07nN; do for r in rs ts py; do sgz $S/out/census/${t}_${k}_${r}.jsonl $D/census/${t}_${k}_${r}.jsonl.gz; done; done
  san $S/out/wasm_$t.sha256 $D/logs/wasm_$t.sha256
done
for l in $S/logs/*.log; do sgz $l $D/logs/$(basename $l).gz; done
for l in $S/runs/dev/*.log; do sgz $l $D/logs/dev_$(basename $l).gz; done
san $S/runs/j0b_chain.out $D/logs/j0b_chain.out
cp $S/out/inputs.sha256 $S/tmp/inputs.sha256 2>/dev/null; (cd $S && shasum -a 256 tools/* corpora/* probes/*) > $S/tmp/inputs.sha256; san $S/tmp/inputs.sha256 $D/harness/inputs.sha256
for f in $S/bin/*; do san $f $D/harness/$(basename $f); done
find $D -type f | wc -l
