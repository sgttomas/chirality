"""I104 SQ: the witness outcomes per build: each entry's result, its I65_G5_WITNESS / I104_SQ lines.
Usage: wit_table.py <wit dir> > json"""
import json, os, re, sys
D = sys.argv[1]; out = {}
for f in sorted(os.listdir(D)):
    if not f.endswith(".out"):
        continue
    t = open(os.path.join(D, f)).read()
    res = re.search(r"test result: (\w+)\. (\d+) passed; (\d+) failed", t)
    out[f[:-4]] = {"result": f"{res.group(1)} {res.group(2)}/{res.group(3)}" if res else "NO RESULT (abort?)",
                   "lines": [l.split("... ", 1)[-1] for l in t.splitlines() if "I65_G5_WITNESS" in l or "I104_SQ_" in l],
                   "panics": [l for l in t.splitlines() if "panicked" in l or "overflow" in l.lower() or "SIGABRT" in l]}
print(json.dumps(out, indent=1))
