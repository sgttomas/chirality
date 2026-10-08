#!/bin/bash
# I113: the new tests against the base code (a discrimination check). copies/rev1 is the development copy with the five
# production files (PY, TS and RS readers; PP's retained_memory.rs and lib.rs) restored to 51f339a11e. Every new or
# edited B3a test must fail there, and nothing else in the targeted sets.
source WT/scratch/i113_b3a/tools/env.sh
J=$S/tools/job.sh; P=$S/copies/rev1/projects/chirality-piping; O=$S/runs/rev1; mkdir -p $O
$J slot rev1_py $P /bin/bash -c "$VENV/bin/python -m pytest -p no:cacheprovider --basetemp=$S/tmp/rev1_py/bt -q -rf --junitxml=$O/py.xml tests/test_retained_precision_b3.py tests/test_retained_precision_contract.py -k 'b3a or d31 or b3b_carriers' > $O/py.log 2>&1"; echo "py rc=$?"
$J slot rev1_ts $P/apps/desktop /bin/bash -c "$P/node_modules/.bin/vitest run src/features/results/retainedPrecision.test.ts --reporter=json --outputFile.json=$O/ts.json > $O/ts.log 2>&1"; echo "ts rc=$?"
RUST_TEST_THREADS=4 $J cargo rev1_re $P/core/reporting/result_export $WT/targets/i113-dev-re test --locked --offline --test retained_precision_contract -- b3a d31 b3b_exact; echo "re rc=$?"
RUST_TEST_THREADS=4 $J cargo rev1_pp $P/core/product_physics $WT/targets/i113-dev-pp test --locked --offline --lib -- b3a b3b every_family_clause; echo "pp rc=$?"
