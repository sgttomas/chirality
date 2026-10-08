#!/bin/bash
# I100: copy the run outputs into the records folder through the sanitizer (placeholders; junit hostname removed);
# large JSON lines are gzipped (mtime 0). Usage: gather_records.sh <records dir>
set -eu
S=WT/scratch/i100_b1_i4p_py
D=$1/_run_records
PY=VENV/bin/python
san() { $PY $S/tools/sanitize.py "$1" "$2"; }
gzc() { mkdir -p "$(dirname "$2")"; $PY -c "import gzip,sys; d=open(sys.argv[1],'rb').read(); f=open(sys.argv[2],'wb'); z=gzip.GzipFile(filename='',mode='wb',fileobj=f,mtime=0); z.write(d); z.close(); f.close()" "$1" "$2"; }
mkdir -p $D
# diff
for f in commits.txt diffstat.txt i4p_py.diff docstring_followup.diff ast_same.txt; do san $S/stage/diff/$f $D/diff/$f; done
# static
for f in heads.txt copies.txt; do san $S/stage/static/$f $D/static/$f; done
# census
for f in I4_VS_RV113_PY2.json HEAD_VS_I4.json FINAL_VS_I4.json; do san $S/census/$f $D/census/$f; done
for l in i4 head final; do san $S/verdicts/$l/census.jsonl $S/tmp/rec_$l.census.jsonl; gzc $S/tmp/rec_$l.census.jsonl $D/census/census_$l.jsonl.gz; done
# probes
san $S/inputs/probes_i100x.json $S/tmp/rec_probes_i100x.json; gzc $S/tmp/rec_probes_i100x.json $D/probes/probes_i100x.json.gz
for f in I4_PROBES_TS1.json HEAD_PROBES_TS1.json FINAL_PROBES_TS1.json HEAD_PROBES_R2X.json FINAL_PROBES_R2X.json HEAD_DIFF_CLASSES.json FINAL_DIFF_CLASSES.json inputs.txt; do san $S/probes/$f $D/probes/$f; done
for l in i4 head final; do for p in probes_ts1 probes_r2x probes_i100x; do
  if [ -f $S/verdicts/$l/$p.jsonl ]; then san $S/verdicts/$l/$p.jsonl $S/tmp/rec_$l.$p.jsonl; gzc $S/tmp/rec_$l.$p.jsonl $D/probes/${l}_$p.jsonl.gz; fi
done; done
# suites
for l in i4 head final; do
  san $S/suites/$l/py.xml $S/tmp/rec_$l.py.xml; gzc $S/tmp/rec_$l.py.xml $D/suites/py_$l.xml.gz
  tail -5 $S/suites/$l/py.log > $S/tmp/rec_$l.tail; san $S/tmp/rec_$l.tail $D/suites/py_$l.tail
done
for f in SUITE_COMPARE_I4_HEAD.json SUITE_COMPARE_I4_FINAL.json SUITE_COMPARE_HEAD_FINAL.json; do san $S/suites/$f $D/suites/$f; done
# mutants
san $S/mutants/MUTANTS.json $D/mutants/MUTANTS.json; san $S/mutants/MUTANT_TABLE.json $D/mutants/MUTANT_TABLE.json
for r in $S/mutants/runs/*; do id=$(basename $r)
  san $r/junit.xml $S/tmp/rec_mut_$id.xml; gzc $S/tmp/rec_mut_$id.xml $D/mutants/runs/$id/junit.xml.gz
  tail -6 $S/logs/mut_$id.log > $S/tmp/rec_mut_$id.tail; san $S/tmp/rec_mut_$id.tail $D/mutants/runs/$id/pytest.tail
done
# scripts
for f in $S/tools/*.sh $S/tools/*.py; do case $(basename $f) in rv113_py_harness.py|cross_heads.py) continue;; esac; san $f $D/scripts/$(basename $f); done
# host
for f in $S/logs/*.log $S/logs/*.out; do san $f $D/host/job_logs/$(basename $f); done
san $S/stage/host/binaries.txt $D/host/binaries.txt; san $S/stage/host/cargo_jobs_i100.log $D/host/cargo_jobs_i100.log
echo gathered
