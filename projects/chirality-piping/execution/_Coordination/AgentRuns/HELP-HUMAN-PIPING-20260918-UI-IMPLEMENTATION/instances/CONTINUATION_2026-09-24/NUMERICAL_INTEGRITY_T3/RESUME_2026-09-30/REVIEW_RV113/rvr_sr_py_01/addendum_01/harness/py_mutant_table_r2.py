"""RV113 (RV-R): SR-PY repair 02's mutant table.
Usage: py_mutant_table_r2.py <runs dir> <MUTANTS_PY2.json> <head probes jsonl> <out.json>
Per mutant: the junit report of the two retained files (--maxfail=10): tests run, failing tests, and whether a failure
is an assertion (a kill counts only for an AssertionError, never an error or a collection failure); and, where the
mutant has a probe run, every probe verdict (bound, unbound, transport) that differs from the control's probe run."""
import json
import os
import sys
import xml.etree.ElementTree as ET

runs, mutants, head, out = sys.argv[1:5]
table = json.load(open(mutants))


def junit(path):
    res = {"tests": 0, "failed": [], "errors": [], "assertion_failures": []}
    if not os.path.exists(path):
        res["missing"] = True
        return res
    for tc in ET.parse(path).getroot().iter("testcase"):
        res["tests"] += 1
        name = f'{tc.get("classname").rsplit(".", 1)[-1]}::{tc.get("name")}'
        for child in tc:
            if child.tag == "failure":
                res["failed"].append(name)
                msg = (child.get("message") or "") + "\n" + (child.text or "")
                if "AssertionError" in msg or msg.lstrip().startswith("assert"):
                    res["assertion_failures"].append(name)
            elif child.tag == "error":
                res["errors"].append(name)
    return res


def lines(path):
    return {json.loads(l)["id"]: json.loads(l) for l in open(path) if l.strip()} if os.path.exists(path) else None


def short(v):
    if v is None:
        return None
    if "ok" in v:
        return ["admitted", v["ok"]["numerical_eligible"], v["ok"]["standing"]]
    if "err" in v:
        return [v["err"]["gate"], v["err"]["code"]]
    return ["escape", str(v)[:120]]


E = ("bound", "unbound", "transport")
ctrl = lines(f"{runs}/NONE/probes.jsonl")
hd = lines(head)
control_equals_head = ctrl is not None and set(ctrl) == set(hd) and all(short(ctrl[i][e]) == short(hd[i][e]) for i in hd for e in E)
rows = []
for mid in ["NONE"] + [m["id"] for m in table]:
    d = f"{runs}/{mid}"
    j = junit(f"{d}/pytest.xml")
    got = lines(f"{d}/probes.jsonl") if mid != "NONE" else None
    moved = None
    if got is not None:
        moved = [{"probe": pid, "verdict": e, "control": short(ctrl[pid][e]), "mutant": short(line[e])}
                 for pid, line in got.items() for e in E if short(line[e]) != short(ctrl[pid][e])]
    m = next((m for m in table if m["id"] == mid), {"item": "control", "description": "RV113_MUT unset"})
    rows.append({"id": mid, "item": m["item"], "description": m["description"], "tests": j["tests"], "failed": j["failed"],
                 "errors": j["errors"], "killed_by_assertion": bool(j["assertion_failures"]),
                 "assertion_failures": j["assertion_failures"], "probes_run": got is not None,
                 "probes_moved": None if moved is None else len(moved), "probe_moves": moved})
json.dump({"control_probes_equal_head": control_equals_head, "rows": rows}, open(out, "w"), indent=1)
print(json.dumps({"control_probes_equal_head": control_equals_head}))
for r in rows:
    print(f'{r["id"]:5} {r["item"]:8} tests={r["tests"]:3} failed={len(r["failed"]):2} errors={len(r["errors"])} killed={r["killed_by_assertion"]!s:5} moved={r["probes_moved"]} | '
          f'{", ".join(sorted(set(x.split("::")[1].split("[")[0] for x in r["failed"])))[:220]}')
