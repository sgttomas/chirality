#!/bin/bash
# I101 addendum 01: RV113's census over corpus 07n (SC's corpus, b1 09fe4cc69b, sha256 ea113e7b…e283) at given RS and TS
# commits: archive copies with the census harnesses (mode h), the corpus file replaced by 07n's bytes. A commit "-" skips a lane.
# Usage: census_07n.sh <label> <rs commit> <ts commit>
WT=WT
S=$WT/scratch/i101_b3r
J=$S/harness/job.sh
L=$1; O=$S/add1/c07n; C07N=$O/retained_precision_cases.07n.json
if [ "$2" != - ]; then
  $S/harness/make_copy.sh b2-r "$2" c07n_${L}_r h > $O/copy_${L}_r.txt || exit 1
  P=$S/copies/c07n_${L}_r/projects/chirality-piping; cp $C07N $P/fixtures/results/retained_precision_cases.json
  RV113_OUT=$O/${L}_rs_census.jsonl RUST_TEST_THREADS=2 $J cargo c07n_${L}_rs "$P/core/reporting/result_export" "$WT/targets/i101-b3r-b2h" test --locked --offline --test rv113_census
  echo "rs rc=$?"
fi
if [ "$3" != - ]; then
  $S/harness/make_copy.sh b2-t "$3" c07n_${L}_t h > $O/copy_${L}_t.txt || exit 1
  P=$S/copies/c07n_${L}_t/projects/chirality-piping; cp $C07N $P/fixtures/results/retained_precision_cases.json
  $J slot c07n_${L}_ts "$P/apps/desktop" /usr/bin/env RV113_OUT=$O/${L}_ts_census.jsonl "$P/node_modules/.bin/vitest" run src/features/results/rv113Census.test.ts
  echo "ts rc=$?"
fi
