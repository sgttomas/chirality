"""RV120: the mutant table. Usage:
  python3 mutant_table.py rs <runs dir> <manifest.json>... <out.json>
  python3 mutant_table.py ts <runs dir> <manifest.json>... <out.json>
RS: each run's lib.log and contract.log (failed tests; each failure's panic location). TS: each run's vitest.json
(failed tests and their first failure message line). A kill counts when a test fails; load failures are listed."""
import json
import os
import re
import sys

kind, runs, *rest = sys.argv[1:]
out = rest[-1]
manifest = []
for m in rest[:-1]:
    manifest += json.load(open(m))
rows = []
for m in [{"id": "NONE", "item": "control", "description": "RV113_MUT/RV120_MUT unset"}] + manifest:
    d = os.path.join(runs, m["id"])
    row = dict(m)
    if not os.path.isdir(d):
        row["result"] = "not run"
        rows.append(row)
        continue
    failed, panics, load = [], [], []
    if kind == "rs":
        for f in ("lib.log", "contract.log"):
            p = os.path.join(d, f)
            if not os.path.exists(p):
                load.append(f + " missing")
                continue
            text = open(p, errors="replace").read()
            failed += [f"{f[:-4]}::{t}" for t in re.findall(r"^test (\S+) \.\.\. FAILED$", text, re.M)]
            panics += sorted(set(re.findall(r"panicked at ([^\n]+?):\d+:\d+:", text)))
            res = re.search(r"test result: (\w+)\. (\d+) passed; (\d+) failed", text)
            row[f[:-4]] = res.group(0) if res else "no result line"
            if not res:
                load.append(f + ": no result line")
    else:
        p = os.path.join(d, "vitest.json")
        if not os.path.exists(p):
            load.append("vitest.json missing")
        else:
            v = json.load(open(p))
            row["tests"] = {"passed": v.get("numPassedTests"), "failed": v.get("numFailedTests"), "total": v.get("numTotalTests")}
            for f in v["testResults"]:
                name = re.sub(r"^.*/apps/desktop/", "", f["name"])
                if f.get("status") == "failed" and not f["assertionResults"]:
                    load.append(f"{name}: {f.get('message', '')[:200]}")
                for a in f["assertionResults"]:
                    if a["status"] == "failed":
                        msg = (a.get("failureMessages") or [""])[0].split("\n")[0][:160]
                        failed.append(f"{name} :: {a['fullName']} :: {msg}")
    row["failed_tests"] = failed
    row["panic_locations"] = panics
    row["load_failures"] = load
    row["result"] = "control" if m["id"] == "NONE" else ("killed" if failed else "survives")
    rows.append(row)
json.dump(rows, open(out, "w"), indent=1)
for r in rows:
    print(r["id"], r["result"], len(r.get("failed_tests", [])), "|", "; ".join(x.split(" :: ")[0] if kind == "ts" else x for x in r.get("failed_tests", [])[:4]))
