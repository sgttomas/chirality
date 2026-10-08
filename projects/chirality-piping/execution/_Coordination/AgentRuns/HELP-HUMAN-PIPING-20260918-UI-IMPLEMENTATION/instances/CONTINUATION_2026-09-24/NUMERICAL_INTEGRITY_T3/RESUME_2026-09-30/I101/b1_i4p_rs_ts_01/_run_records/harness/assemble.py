"""I101: assemble the records' _run_records/ from scratch, every text file through sanitize.py's placeholders
(large ones gzipped with mtime 0). Usage: assemble.py <S> <records dir>   (I101_APPWT in the environment)
"""
import os
import shutil
import subprocess
import sys

S, R = sys.argv[1], sys.argv[2]
RR = os.path.join(R, "_run_records")
SAN = os.path.join(S, "harness", "sanitize.py")


def put(src, rel, gz=False):
    dst = os.path.join(RR, rel + (".gz" if gz else ""))
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    subprocess.run([sys.executable, "-I", SAN, src, dst] + (["gz"] if gz else []), check=True, env=os.environ)


if os.path.exists(RR):
    shutil.rmtree(RR)
os.makedirs(RR)
# commits and diffs
put(f"{S}/records_stage/commits.txt", "commits.txt")
put(f"{S}/records_stage/rs_i4_to_head.diff", "diffs/rs_i4_to_head.diff")
put(f"{S}/records_stage/ts_i4_to_head.diff", "diffs/ts_i4_to_head.diff")
put(f"{S}/records_stage/inputs.sha256", "inputs.sha256")
# harness
for f in sorted(os.listdir(f"{S}/harness")):
    if f.endswith((".sh", ".py", ".txt")):
        put(f"{S}/harness/{f}", f"harness/{f}")
# census and probes
for lab in ("i4", "head"):
    for reader in ("rs", "ts"):
        put(f"{S}/out/{lab}/{reader}_census.jsonl", f"census/{reader}_{lab}.jsonl", gz=True)
        put(f"{S}/out/{lab}/{reader}_probes.jsonl", f"probes/{reader}_{lab}.jsonl", gz=True)
for f, rel in [("census_rs_rv113rs2_vs_i4.json", "census/CENSUS_RS_RV113_VS_I4.json"),
               ("census_ts_rv113ts1_vs_i4.json", "census/CENSUS_TS_RV113_VS_I4.json"),
               ("census_rs_i4_vs_head.json", "census/CENSUS_RS_I4_VS_HEAD.json"),
               ("census_ts_i4_vs_head.json", "census/CENSUS_TS_I4_VS_HEAD.json"),
               ("probes_rs_i4_vs_head.json", "probes/PROBES_RS_I4_VS_HEAD.json"),
               ("probes_ts_i4_vs_head.json", "probes/PROBES_TS_I4_VS_HEAD.json"),
               ("suite_re_i4_vs_head.json", "suites/SUITE_RE_I4_VS_HEAD.json"),
               ("suite_vitest_i4_vs_head.json", "suites/SUITE_VITEST_I4_VS_HEAD.json")]:
    put(f"{S}/out/cmp/{f}", rel)
put(f"{S}/out/cmp/cross_head.json", "probes/CROSS_HEAD.json", gz=True)
put(f"{S}/records_stage/probes_vs_rv113.out", "probes/probes_vs_rv113.out")
# suites and job logs
for f in sorted(os.listdir(f"{S}/logs")):
    src = f"{S}/logs/{f}"
    big = os.path.getsize(src) > 20000
    put(src, f"logs/{f}", gz=big)
put(f"{S}/out/i4/vitest.json", "suites/vitest_i4.json", gz=True)
put(f"{S}/out/head_ts/vitest.json", "suites/vitest_head.json", gz=True)
# mutants
for f in ("MUTANTS_RS.json", "MUTANTS_TS.json", "mutant_schema_RS.diff", "mutant_schema_TS.diff", "MUTANT_TABLE.json"):
    put(f"{S}/mutants/{f}", f"mutants/{f}")
put(f"{S}/records_stage/mutants_vs_rv113.out", "mutants/mutants_vs_rv113.out")
for mid in sorted(os.listdir(f"{S}/mutants/runs")):
    for f in sorted(os.listdir(f"{S}/mutants/runs/{mid}")):
        src = f"{S}/mutants/runs/{mid}/{f}"
        put(src, f"mutants/runs/{mid}/{f}", gz=not f.endswith("run.log"))
# host
for f in sorted(os.listdir(f"{S}/records_stage/host")):
    put(f"{S}/records_stage/host/{f}", f"host/{f}")
for f in sorted(os.listdir(f"{S}/out")):
    if f.startswith("wasm_") and f.endswith(".sha256"):
        put(f"{S}/out/{f}", f"host/{f}")
print("assembled")
