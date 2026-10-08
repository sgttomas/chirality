#!/bin/bash
# RV120 (B3 readers): copy the evidence into R/REVIEW_RV120/b3_readers_01/evidence/ (placeholder paths; junit host
# attribute removed; large outputs gzipped).
set -e
WT=WT
S=$WT/scratch/rv120_rvr
B3=$S/b3
OUT=$WT/numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30/REVIEW_RV120/b3_readers_01/evidence
SAN="python3 -I $S/tools/sanitize.py"
rm -rf $OUT; mkdir -p $OUT/{harness,readers,suites,census,carriers,host}
for f in b3/gen_b3_probes.py b3/gen_i100_shapes.py b3/forge_eg.py b3/cmp3.py b3/rv120_b3_raw.rs b3/rv120B3Raw.test.ts b3/rv120_b3_py_raw.py \
         b3/rv120_census_env.rs b3/rv120CensusEnv.test.ts b3/rv120_py_harness_env.py b3/mutate_b3.py b3/make_b3_copies.sh \
         b3/run_b3_probes.sh b3/run_b3_rest.sh b3/run_b3_07n.sh b3/run_b3_forge.sh run_b3_ts.sh make_b3_copies.sh \
         compare_cargo_suite.py compare_vitest.py compare_junit.py compare_rv120.py rv120_job.sh; do
  [ -f $S/tools/$f ] && $SAN $S/tools/$f $OUT/harness/$(basename $f)
done
for set in probes s165 s52 s318 forge forge_B28 forge_B29; do for r in rs ts py; do
  [ -f $B3/probes/${set}_$r.jsonl ] && $SAN $B3/probes/${set}_$r.jsonl $OUT/readers/${set}_$r.jsonl.gz
done; done
for c in probes s165 s52 s318 forge; do [ -f $B3/probes/cmp_$c.json ] && cp $B3/probes/cmp_$c.json $OUT/readers/; done
python3 - "$B3" "$OUT" <<'PY'
import gzip, hashlib, json, sys
b3, out = sys.argv[1:3]
lines = []
for name in ("probes/b3_probes.jsonl", "inputs/i101_165.jsonl", "inputs/i100_52.jsonl", "inputs/i100_318.jsonl", "inputs/forge_eg.jsonl"):
    rows = [json.loads(l) for l in open(f"{b3}/{name}") if l.strip()]
    for r in rows:
        lines.append({"set": name, "name": r["name"], "want": r.get("want"), "input_sha256": hashlib.sha256(json.dumps([r["source"], r["invocation"]], sort_keys=True, separators=(",", ":")).encode()).hexdigest()})
open(f"{out}/readers/INPUTS_INDEX.jsonl", "w").write("".join(json.dumps(l) + "\n" for l in lines))
keep = [json.loads(l) for l in open(f"{b3}/probes/b3_probes.jsonl") if "G5b order" in l or "G5b control" in l]
gzip.open(f"{out}/readers/g5b_order_inputs.jsonl.gz", "wt").write("".join(json.dumps(k) + "\n" for k in keep))
PY
gzip -9 -n -c $B3/inputs/forge_eg.jsonl > $OUT/readers/forge_eg_inputs.jsonl.gz
for f in $B3/cmp/*.json; do cp $f $OUT/suites/; done
for f in base_re_suite ts_re_suite base_tsc ts_tsc; do $SAN $B3/logs/$f.log $OUT/suites/$f.log.gz; done
for f in vitest_base vitest_ts; do $SAN $B3/suites/$f.json $OUT/suites/$f.json.gz; done
for f in py_base py_ts py_py; do $SAN $B3/suites/$f.xml $OUT/suites/$f.xml.gz; done
for f in $B3/census/*.jsonl; do $SAN $f $OUT/census/$(basename $f).gz; done
[ -d $B3/cmp07n ] && cp $B3/cmp07n/*.json $OUT/census/
cp $B3/carriers/*.json $OUT/carriers/ 2>/dev/null || true
[ -f $B3/carriers/CARRIERS.txt ] && $SAN $B3/carriers/CARRIERS.txt $OUT/carriers/CARRIERS.txt
{ echo "# RV120 B3 jobs: each job log's own stamp lines"; for f in $B3/logs/*.log; do echo "== $(basename $f)"; grep -E "^# " $f; done; } > $B3/logs/job_stamps.txt
$SAN $B3/logs/job_stamps.txt $OUT/host/job_stamps.txt
echo packaged-b3
