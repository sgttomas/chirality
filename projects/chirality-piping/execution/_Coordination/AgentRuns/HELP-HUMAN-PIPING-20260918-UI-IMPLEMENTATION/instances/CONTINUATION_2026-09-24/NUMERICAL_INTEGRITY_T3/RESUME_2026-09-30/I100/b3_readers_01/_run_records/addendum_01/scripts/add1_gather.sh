#!/bin/bash
# I100 B3 addendum 01: stage the addendum's run records (sanitized copies) into WT/scratch/i100_b3r/stage_add1.
set -eu
source WT/scratch/i100_b3r/tools/env.sh
ST=$S/stage_add1/_run_records/addendum_01
rm -rf $S/stage_add1; mkdir -p $ST/scripts $ST/readers $ST/shapes $ST/diffs $ST/census $ST/suites $ST/mutants $ST/host
san() { $VENV/bin/python $S/tools/sanitize.py "$1" "$2"; }
gz() { gzip -n -c "$1" > "$S/tmp/$(basename "$1").gz"; san "$S/tmp/$(basename "$1").gz" "$2"; }
for f in add1_probes.py add1_readers.sh add1_table.py add1_mutants.py add1_chain.sh add1_exact_corpus.py add1_exact.sh add1_shapes.py add1_chain2.sh add1_gather.sh \
         env.sh job.sh census.sh census_head.sh census_cmp.py suites.sh compare_suites.py mutant_table.py rv113_py_harness.py sanitize.py screen_dir.py; do
  san $S/tools/$f $ST/scripts/$f; done
san $S/add1/probes.json $ST/readers/probes.json
for r in base:today aligned:aligned exact_today:exact_today exact_aligned:exact_aligned; do
  src=${r%%:*}; dst=${r##*:}; d=$S/add1/runs/$src
  for x in py rs ts; do mv_tmp=$S/tmp/${dst}_$x.jsonl; cp $d/$x.jsonl $mv_tmp; gz $mv_tmp $ST/readers/${dst}_$x.jsonl.gz; done
  san $d/TABLE.tsv $ST/readers/${dst}_TABLE.tsv
  [ -f $d/ts_wasm_assets.sha256 ] && san $d/ts_wasm_assets.sha256 $ST/readers/${dst}_ts_wasm_assets.sha256
  [ -f $d/corpus.sha256 ] && san $d/corpus.sha256 $ST/readers/${dst}_corpus.sha256
done
gz $S/add1/shapes/add1_shapes.json $ST/shapes/add1_shapes.json.gz
gz $S/add1/shapes/py_add1_shapes.jsonl $ST/shapes/py_add1_shapes.jsonl.gz
gz $S/add1/shapes/add1_inputs.jsonl $ST/shapes/add1_inputs.jsonl.gz
san $S/add1/shapes/SHAPES.tsv $ST/shapes/SHAPES.tsv
for f in $S/add1/diffs/*.diff; do san $f $ST/diffs/$(basename $f); done
for r in c_add1 c_add107n; do gz $S/runs/$r/py.jsonl $ST/census/$r.py.jsonl.gz; san $S/runs/$r/corpus.sha256 $ST/census/$r.corpus.sha256; done
san $S/add1/cmp/census_07m.json $ST/census/c_add1_VS_BASE.json
san $S/add1/cmp/census_07n.json $ST/census/c_add107n_VS_BASE07N.json
gz $S/suites/add1/py.xml $ST/suites/add1.py.xml.gz
san $S/add1/cmp/suites.json $ST/suites/COMPARE_add1_VS_BASE.json
san $S/add1/mutants/MUTANTS.json $ST/mutants/MUTANTS.json
san $S/add1/mutants/TABLE.json $ST/mutants/TABLE.json
for f in $S/logs/add1_*.log $S/logs/add1_chain*.out $S/logs/census_c_add1*.log $S/logs/suites_add1.log; do san $f $ST/host/$(basename $f); done
for id in NONE C1 C2 C3; do san $S/add1/mutants/runs/$id/pytest.log $ST/host/pytest_add1_mut_$id.log; done
echo staged
