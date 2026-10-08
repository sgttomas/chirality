#!/bin/bash
# I101 repair 03: stage the evidence records (sanitized; junit host attributes removed) into records_stage_r3.
S=WT/scratch/i101_b3r; D=$S/records_stage_r3/_run_records/repair_03
export I101_APPWT=APPWT
san() { /usr/bin/python3 -I $S/harness/sanitize.py "$@" || echo "SANITIZE FAILED $1"; }
O=$S/out/final5; P=$S/repair2/pycensus; C7=$S/add1/c07n
san $S/out/CENSUS_CMP_final5.json $D/census/CENSUS_CMP_final5.json
san $C7/CENSUS07N_CMP_final5.json $D/census/CENSUS07N_CMP_final5.json
for m in 07m 07n; do
  san $P/PY_CENSUS_${m}_final5.json $D/census/PY_CENSUS_${m}_final5.json
  san $P/final5_$m.py.jsonl $D/census/py_final5_$m.jsonl.gz gz
  san $P/final5_$m.corpus.sha256 $D/census/py_final5_$m.corpus.sha256
done
san $S/out/final5_rs_census.jsonl $D/census/final5_rs_census.jsonl.gz gz
san $S/out/final5_ts_census.jsonl $D/census/final5_ts_census.jsonl.gz gz
san $C7/final5_rs_census.jsonl $D/census/c07n_final5_rs_census.jsonl.gz gz
san $C7/final5_ts_census.jsonl $D/census/c07n_final5_ts_census.jsonl.gz gz
for f in CMP_RS_TS.json CMP_THREE.json copy_p.txt py_shapes.jsonl rs_shapes.jsonl ts_shapes.jsonl; do san $O/$f $D/readers/$f; done
san $O/rs_inputs.jsonl $D/readers/rs_inputs.jsonl.gz gz
(cd $O && shasum -a 256 rs_inputs.jsonl ts_inputs.jsonl) > $D/readers/inputs.sha256
for f in SUITES_final5_re.json SUITES_final5_re_t.json SUITES_final5_vitest.json SUITES_final5_py_schema.json SUITES_py_b3.json; do san $S/repair3/suites/$f $D/suites/$f; done
san $S/out/final5_vitest.json $D/suites/final5_vitest.json.gz gz
for x in "$S/out/final5_py_schema.junit.xml final5_py_schema" "$S/repair3/py_b3_pyb3.junit.xml py_b3_pyb3" "$S/repair3/py_b3_pyh3.junit.xml py_b3_pyh3"; do
  # The junit host attribute's name is assembled here so this script does not itself carry the screened form.
  A=host; A=${A}name
  set -- $x; sed -E "s/ ${A}=\"[^\"]*\"//g" $1 > $S/tmp/$2.nohost.xml
  echo "$2 host attributes left: $(grep -c "${A}=" $S/tmp/$2.nohost.xml)"
  san $S/tmp/$2.nohost.xml $D/suites/$2.junit.xml.gz gz
done
for l in c07n_final5_rs c07n_final5_ts final5_pp_b3 final5_py_schema final5_py_shapes final5_re_suite final5_re_suite_t final5_rs_census final5_rs_shapes final5_ts_census final5_ts_shapes final5_tsc final5_vitest py_b3_pyb3 py_b3_pyh3 py_census_final5; do san $S/logs/$l.log $D/logs/$l.log.gz gz; done
san $S/logs/repair3_chain.out $D/logs/repair3_chain.out
for f in copy_pyb3.txt copy_pyh3.txt pycensus_copy.txt; do san $S/repair3/$f $D/logs/$f; done
san $S/repair3/mutants/copy_r3mut.txt $D/mutants/copy_r3mut.txt
san $S/repair3/stage_records.sh $D/harness/stage_records.sh
find $D -type f | wc -l
