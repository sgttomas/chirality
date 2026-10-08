"""I101: the mutant table. RS runs (S/mutants/runs/<id>/{lib,contract}.log): the failing tests per binary, and
whether each failure panics at an assertion line (the panic's file:line, read in the mutant copy's sources, holds
`assert`). TS runs (vitest.json): the failing tests and whether each failure is an AssertionError.
Usage: mutant_table.py <S> <out.json>
"""
import json
import re
import sys

S, out_path = sys.argv[1], sys.argv[2]
RE = f"{S}/copies/rsm/projects/chirality-piping/core/reporting/result_export"
rs_manifest = json.load(open(f"{S}/mutants/MUTANTS_RS.json"))
ts_manifest = json.load(open(f"{S}/mutants/MUTANTS_TS.json"))
src_cache = {}


def line_text(rel, n):
    path = f"{RE}/{rel}"
    if path not in src_cache:
        src_cache[path] = open(path).read().splitlines()
    lines = src_cache[path]
    return lines[n - 1] if 0 < n <= len(lines) else ""


def assertion_at(rel, n):
    # The macro may span lines: the panic location is the macro's first line.
    return "assert" in line_text(rel, n)


def rs_run(mid):
    d = f"{S}/mutants/runs/{mid}"
    res = {"id": mid, "failed": [], "panics": [], "rc": {}}
    for part in ("lib", "contract"):
        try:
            text = open(f"{d}/{part}.log", errors="replace").read()
        except FileNotFoundError:
            res["rc"][part] = "missing"
            continue
        m = re.search(r"test result: (\w+)\. (\d+) passed; (\d+) failed", text)
        res["rc"][part] = m.groups() if m else "no result line"
        res["failed"] += [f"{part}:{t}" for t in re.findall(r"^test (\S+) \.\.\. FAILED", text, re.M)]
        lines = text.splitlines()
        for k, line in enumerate(lines):
            m = re.match(r"thread '([^']+)'(?: \(\d+\))? panicked at ([^:\n]+):(\d+):\d+:", line)
            if not m:
                continue
            test, rel, n = m.group(1), m.group(2), int(m.group(3))
            msg = []
            for follow in lines[k + 1:]:
                if not follow.strip() or follow.startswith(("note:", "thread '")):
                    break
                msg.append(follow)
            rows = [x.split(": got ")[0] for x in msg if ": got " in x]
            res["panics"].append({"test": f"{part}:{test}", "at": f"{rel}:{n}", "assertion": assertion_at(rel, n),
                                  "missed_rows": rows, "message": [x[:300] for x in msg[:3]]})
    res["killed"] = bool(res["failed"])
    res["killed_by_assertion"] = res["killed"] and all(p["assertion"] for p in res["panics"]) and len(res["panics"]) >= len(res["failed"])
    return res


def ts_run(mid):
    d = f"{S}/mutants/runs/{mid}"
    res = {"id": mid, "failed": [], "assertion_failures": 0}
    try:
        j = json.load(open(f"{d}/vitest.json"))
    except FileNotFoundError:
        res["missing"] = True
        return res
    res["tests"] = {"passed": j["numPassedTests"], "failed": j["numFailedTests"], "total": j["numTotalTests"], "suites_failed": j["numFailedTestSuites"]}
    for f in j["testResults"]:
        for a in f["assertionResults"]:
            if a["status"] == "failed":
                name = re.sub(r"^.*/apps/desktop/", "", f["name"]) + " :: " + a["fullName"]
                res["failed"].append(name)
                if any("AssertionError" in m for m in a.get("failureMessages", [])):
                    res["assertion_failures"] += 1
    res["killed"] = bool(res["failed"])
    res["killed_by_assertion"] = res["killed"] and res["assertion_failures"] == len(res["failed"])
    return res


rows = {"rs_control": rs_run("NONE"), "ts_control": ts_run("NONE"), "rs": [], "ts": []}
for m in rs_manifest:
    r = rs_run(m["id"]); r.update(item=m["item"], description=m["description"]); rows["rs"].append(r)
for m in ts_manifest:
    r = ts_run(m["id"]); r.update(item=m["item"], description=m["description"]); rows["ts"].append(r)
json.dump(rows, open(out_path, "w"), indent=1)
print("RS control:", rows["rs_control"]["rc"], "failed", len(rows["rs_control"]["failed"]))
print("TS control:", rows["ts_control"].get("tests"))
for r in rows["rs"] + rows["ts"]:
    short = sorted({f.split(" :: ")[-1].split(":")[-1] if " :: " not in f else f.split(" :: ")[1][:70] for f in r["failed"]})
    print(f"{r['id']:4} killed={r['killed']!s:5} by_assertion={r['killed_by_assertion']!s:5} n={len(r['failed']):2} {short[:4]}")
