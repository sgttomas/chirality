"""RV113 (RV-R): SR-TS repair 01's mutant table. Usage: ts_mutant_table_r1.py <runs dir> <MUTANTS_TS1.json> <head probes jsonl> <out.json>
A kill counts only when every test file loaded (the control's test count) and a test failed at an assertion."""
import json
import os
import sys

runs, manifest, head_probes, out = sys.argv[1:5]
M = json.load(open(manifest))


def vt(path):
    if not os.path.exists(path):
        return None
    d = json.load(open(path))
    failed, asserts = [], 0
    for f in d["testResults"]:
        for a in f["assertionResults"]:
            if a["status"] == "failed":
                failed.append(a["fullName"][:160])
                msg = " ".join(a.get("failureMessages") or [])
                asserts += ("AssertionError" in msg) or ("expected" in msg)
    return {"total": d["numTotalTests"], "files_failed_to_load": sum(1 for f in d["testResults"] if f["status"] == "failed" and not f["assertionResults"]),
            "failed": failed, "assertion_failures": asserts}


def probes(path):
    return {json.loads(l)["id"]: json.loads(l) for l in open(path)} if os.path.exists(path) else None


ctrl = vt(f"{runs}/NONE/vitest.json")
cp = probes(f"{runs}/NONE/probes.jsonl"); hp = probes(head_probes)
rows = []
for mid in ["NONE"] + [m["id"] for m in M]:
    r = vt(f"{runs}/{mid}/vitest.json")
    pr = probes(f"{runs}/{mid}/probes.jsonl")
    moved = None if pr is None or cp is None or mid == "NONE" else sorted({k for k in cp for v in ("bound", "unbound", "transport") if pr[k][v] != cp[k][v]})
    m = next((x for x in M if x["id"] == mid), {"item": "control", "description": "RV113_MUT unset"})
    killed = bool(r and r["failed"] and r["total"] == ctrl["total"] and r["files_failed_to_load"] == 0 and r["assertion_failures"] == len(r["failed"]))
    rows.append({"id": mid, "item": m["item"], "description": m["description"], "vitest": r, "killed_by_assertion": killed, "probes_moved": moved})
same = None if cp is None or hp is None else all(cp[k][v] == hp[k][v] for k in hp for v in ("bound", "unbound", "transport"))
json.dump({"control_probes_equal_head": same, "rows": rows}, open(out, "w"), indent=1)
print("control:", ctrl and {k: ctrl[k] for k in ("total", "files_failed_to_load")}, "control probes equal head:", same)
for r in rows:
    v = r["vitest"] or {}
    print(f'{r["id"]:5} {r["item"]:9} killed={r["killed_by_assertion"]!s:5} failed={len(v.get("failed", []))} asserts={v.get("assertion_failures")} moved={None if r["probes_moved"] is None else len(r["probes_moved"])} | {"; ".join(v.get("failed", []))[:150]}')
