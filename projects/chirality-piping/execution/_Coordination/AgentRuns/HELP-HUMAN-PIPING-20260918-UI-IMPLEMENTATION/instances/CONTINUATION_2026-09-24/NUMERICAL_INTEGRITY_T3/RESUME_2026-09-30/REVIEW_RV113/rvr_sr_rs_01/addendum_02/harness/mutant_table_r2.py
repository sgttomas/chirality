"""RV113 (RV-R): SR-RS repair 02's mutant table. Usage: mutant_table_r2.py <runs dir> <MUTANTS_R2.json> <head probes jsonl> <out.json>
Per mutant: the lib and contract test binaries' failing tests (a kill is a test that panics at an assertion), and, where
a probe run exists, the probes whose verdict differs from the control's."""
import json
import os
import re
import sys

runs, manifest, head_probes, out = sys.argv[1:5]
M = json.load(open(manifest))
FAIL = re.compile(r"^test (\S+) \.\.\. FAILED", re.M)
PAN = re.compile(r"panicked at ((?:tests|src)/[\w./]+):(\d+):\d+")
SRC = "WT/rv113/rs2-head/projects/chirality-piping/core/reporting/result_export/"
PANIC = re.compile(r"panicked at")


def failures(log):
    if not os.path.exists(log):
        return None, None
    text = open(log, errors="replace").read()
    failed = FAIL.findall(text)
    # Each panic's source line: a kill counts as an assertion when the panicking line is an assert! or assert_eq!.
    sites = []
    for f, line in PAN.findall(text):
        src = open(SRC + f).read().split("\n")[int(line) - 1].strip()
        sites.append({"site": f"{f}:{line}", "assert": src.startswith(("assert!", "assert_eq!", "assert_ne!"))})
    return failed, sites


def probes(path):
    return {json.loads(l)["id"]: json.loads(l) for l in open(path)} if os.path.exists(path) else None


ctrl = probes(f"{runs}/NONE/probes.jsonl")
head = probes(head_probes)
rows = []
for mid in ["NONE"] + [m["id"] for m in M]:
    d = f"{runs}/{mid}"
    lib_failed, lib_sites = failures(f"{d}/lib.log")
    con_failed, con_sites = failures(f"{d}/contract.log")
    sites = (lib_sites or []) + (con_sites or [])
    pr = probes(f"{d}/probes.jsonl")
    moved = None
    if pr is not None and ctrl is not None and mid != "NONE":
        moved = [k for k in ctrl for v in ("bound", "unbound", "transport") if pr[k].get(v) != ctrl[k].get(v)]
    m = next((x for x in M if x["id"] == mid), {"item": "control", "description": "RV113_MUT unset"})
    rows.append({"id": mid, "item": m["item"], "description": m["description"], "lib_failed": lib_failed, "contract_failed": con_failed,
                 "killed": bool((lib_failed or []) + (con_failed or [])), "panic_sites": sites,
                 "all_panics_at_asserts": all(x["assert"] for x in sites) if sites else None, "probes_moved": None if moved is None else sorted(set(moved))})
same = None
if ctrl is not None and head is not None:
    same = all(ctrl[k].get(v) == head[k].get(v) for k in head for v in ("bound", "unbound", "transport"))
json.dump({"control_probes_equal_head": same, "rows": rows}, open(out, "w"), indent=1)
print("control probes equal head:", same)
for r in rows:
    fl = (r["lib_failed"] or []) + (r["contract_failed"] or [])
    pm = "" if r["probes_moved"] is None else f' probes_moved={len(r["probes_moved"])}'
    print(f'{r["id"]:5} {r["item"]:6} killed={str(r["killed"]):5} asserts={r["all_panics_at_asserts"]!s:5} {", ".join(fl)[:150]}{pm}')
