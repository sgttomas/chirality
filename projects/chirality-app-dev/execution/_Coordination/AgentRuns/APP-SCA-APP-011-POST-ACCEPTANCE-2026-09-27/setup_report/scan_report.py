#!/usr/bin/env python3
"""project-setup Phase 5.7 -> Phase 3.1/3.2 scan and advisory report (read-only). Run from the repository root.

Writes SCAN_REPORT.md next to this script. FULL_GRAPH, no accepted project DAG: BLOCKED/UNBLOCKED is computed from the
recorded register (Dependencies.csv rows plus declared entries; no in-scope declared entries exist) after the closure
audit, which found no SCC, so no edge is HELD for a cycle.
"""
import csv, glob, os, re, subprocess

EX = "projects/chirality-app-dev/execution"
HERE = os.path.dirname(os.path.abspath(__file__))
ORDER = ["OPEN", "INITIALIZED", "SEMANTIC_READY", "IN_PROGRESS", "CHECKING", "ISSUED"]
ESR1 = {"DEP-02-02-021", "DEP-07-01-010", "DEP-02-01-014", "DEP-02-04-015", "DEP-02-04-016", "DEP-08-01-018", "DEP-08-01-019", "DEP-08-04-013"}
units = {}
for f in sorted(glob.glob(f"{EX}/PKG-*/1_Working/DEL-*")):
    d = re.match(r"(DEL-\d{2}-\d{2})", os.path.basename(f)).group(1)
    st = open(f + "/_STATUS.md", encoding="utf-8").read()
    m = re.search(r"\*\*Current State:\*\*\s*`?([A-Z_]+)", st)
    units[d] = {"folder": f, "state": m.group(1) if m else "UNKNOWN"}
for zone in ("2_Checking", "3_Issued"):
    units_in = glob.glob(f"{EX}/PKG-*/{zone}/*")
    units["_" + zone] = len(units_in)
needs = {}
for d, u in units.items():
    if d.startswith("_") or not os.path.exists(u["folder"] + "/Dependencies.csv"):
        continue
    for r in csv.DictReader(open(u["folder"] + "/Dependencies.csv", encoding="utf-8")):
        if r["Status"] != "ACTIVE" or r["DependencyClass"] != "EXECUTION" or r["TargetType"] != "DELIVERABLE":
            continue
        a, b = r["FromDeliverableID"], r["TargetDeliverableID"]
        down, up = (a, b) if r["Direction"] == "UPSTREAM" else (b, a)
        needs.setdefault(down, []).append((up, r["RequiredMaturity"], r["SatisfactionStatus"], r["DependencyID"]))
blocked, unblocked = {}, []
for d, u in sorted(units.items()):
    if d.startswith("_") or d == "DEL-09-07":
        continue
    unmet = []
    for up, req, sat, did in needs.get(d, []):
        if sat in ("SATISFIED", "WAIVED", "NOT_APPLICABLE"):
            continue
        need = req if req in ORDER else "SEMANTIC_READY"
        have = units.get(up, {}).get("state", "UNKNOWN")
        if have not in ORDER or ORDER.index(have) < ORDER.index(need):
            unmet.append(f"{did} needs {up} at {need} (now {have})")
    if unmet:
        blocked[d] = unmet
    else:
        unblocked.append(d)
count = subprocess.run(["bash", "tools/query/count_workspace_state.sh", EX], capture_output=True, text=True).stdout.strip()
states = {}
for d, u in units.items():
    if not d.startswith("_"):
        states.setdefault(u["state"], []).append(d)
out = ["# Phase 5.7 scan and report (Phase 3.1/3.2)", "",
       "Read-only. `tools/query/count_workspace_state.sh` output:", "", "```", count, "```", "",
       "## By lifecycle state", ""]
for s in ORDER:
    ds = sorted(states.get(s, []))
    out.append(f"- {s}: {len(ds)}" + (f" ({', '.join(ds)})" if 0 < len(ds) <= 3 else ""))
out += ["", f"`2_Checking/` items: {units['_2_Checking']}; `3_Issued/` items: {units['_3_Issued']}.", "",
        "## Dependencies (advisory; FULL_GRAPH; no accepted project DAG)", "",
        "Computed from the recorded register after the closure audit "
        "(`_Evaluation/DepClosure/CLOSURE_SCA_APP_011_POST_EXTRACTION_2026-09-27_1656`, 0 SCC).",
        "An upstream edge is met when its `SatisfactionStatus` is SATISFIED, WAIVED or NOT_APPLICABLE, "
        "or the upstream deliverable's lifecycle state is at least the row's `RequiredMaturity` (SEMANTIC_READY when TBD).",
        "Retired DEL-09-07 is listed separately and excluded.", "",
        f"- UNBLOCKED: {len(unblocked)}",
        f"- BLOCKED: {len(blocked)}"]
for d, why in sorted(blocked.items()):
    out.append(f"  - {d}: " + "; ".join(why))
out += ["- HELD (unresolved cycles): none (0 SCC).",
        "- DAG PENDING: not applicable (no accepted project DAG).",
        f"- Retired: DEL-09-07 (lifecycle `{units['DEL-09-07']['state']}`, unchanged).",
        "- Owner proposal ESR-1 covers eight ACTIVE edges whose evidence source was retired "
        f"({', '.join(sorted(ESR1))}); they are counted here as recorded.",
        "", "WORKING_ITEMS does not assign or recommend priorities."]
open(os.path.join(HERE, "SCAN_REPORT.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out[-14:]))
