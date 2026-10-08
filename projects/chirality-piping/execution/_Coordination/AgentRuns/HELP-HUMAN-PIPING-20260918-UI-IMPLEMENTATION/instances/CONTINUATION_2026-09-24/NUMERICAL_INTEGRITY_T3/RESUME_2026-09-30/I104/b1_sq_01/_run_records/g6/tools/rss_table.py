"""I104 SQ (PLAN_v2 §3.6): parse rss_batch.sh outputs into one JSON table: per tag and repetition,
time -l's maximum resident set size and peak memory footprint (bytes), real/user/sys seconds, the
test's own printed lines (challenge peak and outcome, witness outcome and timings), and its result.
Usage: python3 rss_table.py <out dir> > table.json"""
import json, os, re, sys, collections
D = sys.argv[1]
rows = collections.defaultdict(dict)
for f in sorted(os.listdir(D)):
    m = re.match(r"(.+)\.r(\d+)\.time$", f)
    if not m:
        continue
    tag, rep = m.group(1), int(m.group(2))
    t = open(os.path.join(D, f)).read()
    o = open(os.path.join(D, f"{tag}.r{rep}.out")).read()
    g = lambda pat, s=t: (lambda x: x.group(1) if x else None)(re.search(pat, s, re.M))
    r = {"real_s": float(g(r"^\s*([\d.]+) real") or "nan"), "user_s": float(g(r"([\d.]+) user") or "nan"),
         "sys_s": float(g(r"([\d.]+) sys") or "nan"),
         "max_rss_bytes": int(g(r"^\s*(\d+)\s+maximum resident set size") or -1),
         "peak_footprint_bytes": int(g(r"^\s*(\d+)\s+peak memory footprint") or -1),
         "result": "ok" if re.search(r"test result: ok\. 1 passed", o) else ("FAILED" if "FAILED" in o or "panicked" in o else "?"),
         "lines": [l.split("... ", 1)[-1] for l in o.splitlines() if "I104_SQ_" in l or "I65_G5_WITNESS" in l]}
    rows[tag][rep] = r
print(json.dumps(rows, indent=1, sort_keys=True))
