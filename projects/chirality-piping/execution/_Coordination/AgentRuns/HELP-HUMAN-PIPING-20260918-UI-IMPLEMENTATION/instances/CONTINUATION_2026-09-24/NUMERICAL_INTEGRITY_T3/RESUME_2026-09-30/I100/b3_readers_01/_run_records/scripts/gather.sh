#!/bin/bash
# I100 B3: stage the records (sanitized copies) into WT/scratch/i100_b3r/stage. Usage: gather.sh
set -eu
source WT/scratch/i100_b3r/tools/env.sh
ST=$S/stage
mkdir -p $ST/_run_records/scripts $ST/_run_records/census $ST/_run_records/suites $ST/_run_records/mutants $ST/_run_records/shapes $ST/_run_records/host
san() { $VENV/bin/python $S/tools/sanitize.py "$1" "$2"; }
gz() { gzip -n -c "$1" > "$S/tmp/$(basename "$1").gz"; san "$S/tmp/$(basename "$1").gz" "$2"; }
for f in $S/tools/*.py $S/tools/*.sh; do san $f $ST/_run_records/scripts/$(basename $f); done
for r in base c_b3a c_head c_final c_base07n c_b3a07n c_head07n c_final07n; do
  [ -f $S/runs/$r/py.jsonl ] || continue
  gz $S/runs/$r/py.jsonl $ST/_run_records/census/$r.py.jsonl.gz
  san $S/runs/$r/corpus.sha256 $ST/_run_records/census/$r.corpus.sha256
  for v in $S/runs/$r/VS_*.json; do [ -f $v ] && san $v $ST/_run_records/census/${r}_$(basename $v); done
done
for r in base head final; do [ -f $S/suites/$r/py.xml ] && gz $S/suites/$r/py.xml $ST/_run_records/suites/$r.py.xml.gz; done
for f in $S/suites/COMPARE*.json; do san $f $ST/_run_records/suites/$(basename $f); done
san $S/mutants/MUTANTS.json $ST/_run_records/mutants/MUTANTS.json
san $S/mutants/TABLE.json $ST/_run_records/mutants/TABLE.json
gz $S/shapes/b3_shapes.json $ST/_run_records/shapes/b3_shapes.json.gz
gz $S/shapes/py_b3_shapes.jsonl $ST/_run_records/shapes/py_b3_shapes.jsonl.gz
san $S/shapes/SHAPES.tsv $ST/_run_records/shapes/SHAPES.tsv
san $S/shapes/RS_LABEL_MAP.tsv $ST/_run_records/shapes/RS_LABEL_MAP.tsv
san $S/shapes/PY_ON_I101_INPUTS.json $ST/_run_records/shapes/PY_ON_I101_INPUTS.json
san $S/inputs/i101.sha256 $ST/_run_records/shapes/i101_inputs.sha256
for f in $S/logs/*.log; do san $f $ST/_run_records/host/$(basename $f); done
for f in $S/runs/*/pytest.log; do d=$(basename $(dirname $f)); san $f $ST/_run_records/host/pytest_$d.log; done
echo staged
