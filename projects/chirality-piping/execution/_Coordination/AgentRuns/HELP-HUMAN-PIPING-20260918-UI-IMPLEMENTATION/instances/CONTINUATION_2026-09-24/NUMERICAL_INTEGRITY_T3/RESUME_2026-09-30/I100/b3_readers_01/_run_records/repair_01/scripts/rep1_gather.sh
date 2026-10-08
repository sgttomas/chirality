#!/bin/bash
# I100 B3 repair 01: stage the repair's run records (sanitized copies) into WT/scratch/i100_b3r/stage_rep1.
set -eu
source WT/scratch/i100_b3r/tools/env.sh
ST=$S/stage_rep1/_run_records/repair_01
rm -rf $S/stage_rep1; mkdir -p $ST/scripts $ST/agreement $ST/census $ST/suites $ST/mutants $ST/host
san() { $VENV/bin/python $S/tools/sanitize.py "$1" "$2"; }
gz() { gzip -n -c "$1" > "$S/tmp/$(basename "$1").gz"; san "$S/tmp/$(basename "$1").gz" "$2"; }
for f in rep1_compact.py rep1_mutants.py rep1_chain.sh rep1_mut2.sh rep1_trace.py rep1_gather.sh rv120_b3_py_raw.py cmp3.py \
         env.sh job.sh census.sh census_head.sh census_cmp.py suites.sh compare_suites.py mutant_table.py sanitize.py screen_dir.py; do
  san $S/tools/$f $ST/scripts/$f; done
for s in probes forge s52 s165 s318; do
  cp $S/rep1/agree/${s}_py.jsonl $S/tmp/rep1_${s}_py.jsonl; gz $S/tmp/rep1_${s}_py.jsonl $ST/agreement/${s}_py.jsonl.gz
  san $S/rep1/agree/cmp_$s.json $ST/agreement/cmp_$s.json
done
san $S/rep1/agree/INPUTS_CHECK.txt $ST/agreement/INPUTS_CHECK.txt
for r in c_rep1 c_rep107n; do gz $S/runs/$r/py.jsonl $ST/census/$r.py.jsonl.gz; san $S/runs/$r/corpus.sha256 $ST/census/$r.corpus.sha256; done
san $S/rep1/cmp/census_07m.json $ST/census/c_rep1_VS_BASE.json
san $S/rep1/cmp/census_07n.json $ST/census/c_rep107n_VS_BASE07N.json
gz $S/suites/rep1/py.xml $ST/suites/rep1.py.xml.gz
san $S/rep1/cmp/suites_vs_add1.json $ST/suites/COMPARE_rep1_VS_b7721d27e9.json
san $S/rep1/MUTANTS.json $ST/mutants/MUTANTS.json
san $S/rep1/mutants2/TABLE.json $ST/mutants/TABLE.json
san $S/rep1/mutants/TABLE.json $ST/mutants/TABLE_first_run_R1-R3.json
san $S/rep1/mutants2/FORGE_TRACE.txt $ST/mutants/FORGE_TRACE.txt
for f in $S/logs/rep1_*.log $S/logs/rep1_chain.out $S/logs/census_c_rep1*.log $S/logs/suites_rep1.log; do san $f $ST/host/$(basename $f); done
for id in NONE R1 R2 R3 R4 R5; do san $S/rep1/mutants2/runs/$id/pytest.log $ST/host/pytest_rep1_mut2_$id.log; done
san $S/logs/rep1_mut2.out $ST/host/rep1_mut2.out
echo staged
