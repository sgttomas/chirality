#!/bin/bash
# I113: stage the records in S/records/stage (placeholders only), then screen them. Usage: gather.sh
set -e
source WT/scratch/i113_b3a/tools/env.sh
export I113_APPWT=APPWT
ST=$S/records/stage; rm -rf $ST; mkdir -p $ST/_run_records/{tools,suites,census,reverse,logs}
san() { $VENV/bin/python -I $S/tools/sanitize.py "$1" "$2" ${3:-}; }
for f in $S/tools/*; do san $f $ST/_run_records/tools/$(basename $f); done
for L in base cand; do
  for p in pp runner re; do san $S/logs/${L}_$p.log $ST/_run_records/logs/${L}_$p.log.gz gz; done
  for p in py vitest tsc; do san $S/logs/${L}_$p.log $ST/_run_records/logs/${L}_$p.log.gz gz; done
  san $S/runs/$L/py.log $ST/_run_records/logs/${L}_py_session.log.gz gz
  sed -E 's/ host[n]ame="[^"]*"//' $S/runs/$L/py.xml > $S/tmp/${L}_py_nohost.xml; san $S/tmp/${L}_py_nohost.xml $ST/_run_records/suites/${L}_py.xml.gz gz
  san $S/runs/$L/vitest.json $ST/_run_records/suites/${L}_vitest.json.gz gz
  san $S/runs/$L/meta.txt $ST/_run_records/suites/${L}_meta.txt
  san $S/runs/$L/corpora.sha256 $ST/_run_records/census/${L}_corpora.sha256
  for k in h n; do for r in rs ts py; do san $S/logs/${L}_census_${k}_$r.log $ST/_run_records/logs/${L}_census_${k}_$r.log.gz gz; done; done
  for c in 07m 07n; do for r in rs ts py; do san $S/runs/$L/c${c}_$r.jsonl $ST/_run_records/census/${L}_c${c}_$r.jsonl.gz gz; done; done
done
for f in $S/out/*.json $S/out/*.txt $S/out/*.log $S/out/*.diff $S/out/*.sha256; do [ -e "$f" ] && san $f $ST/_run_records/suites/$(basename $f); done
san $S/runs/rev1/py.log $ST/_run_records/reverse/py.log
san $S/runs/rev1/ts.json $ST/_run_records/reverse/ts.json.gz gz
san $S/logs/rev1_re.log $ST/_run_records/reverse/re.log.gz gz
san $S/logs/rev1_pp.log $ST/_run_records/reverse/pp.log.gz gz
for f in $S/records/*.json $S/records/*.txt $S/records/*.md; do [ -e "$f" ] && san $f $ST/_run_records/$(basename $f); done
echo staged
