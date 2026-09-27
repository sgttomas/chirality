#!/usr/bin/env python3
"""SCA-APP-011 checkpoint-group-1 pre-change baseline (read-only).

Synthesizes the pre-change coverage baseline for SCA-APP-011 from the
authoritative App decomposition and the registered deterministic tools. It
writes only inside this SCA snapshot folder and never modifies an input.

Run from the repository root:

    python3 projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/Evidence/Group1/build_pre_change_baseline.py

Inputs (read-only):
  - execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md
  - execution/_Decomposition/contract_invariant_coverage_register.csv
  - execution/_ScopeChange/_LATEST.md
  - execution/PKG-*/1_Working/DEL-*/{_STATUS.md,Dependencies.csv}
Registered tools invoked (report-only):
  - tools/evaluation/audit_structure.py --variant SOFTWARE
  - tools/coordination/analyze_dep_closure.py
  - tools/validation/validate_decomposition_registers.py
Outputs:
  - ../../Pre_Change_Coverage.json (tool summaries embedded, path-sanitized)
"""
from __future__ import annotations

import csv
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter

SNAP_REL = (
    "projects/chirality-app-dev/execution/_ScopeChange/"
    "SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement"
)
APP = "projects/chirality-app-dev"
EXEC = f"{APP}/execution"
DECOMP = f"{EXEC}/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
REGISTER = f"{EXEC}/_Decomposition/contract_invariant_coverage_register.csv"
POINTER = f"{EXEC}/_ScopeChange/_LATEST.md"
PRIOR_AUDIT = (
    f"{EXEC}/_Evaluation/DecompCoverage/"
    "COV_SCA_APP_010_POST_RECORD_RECON_2026-09-22_2026-09-22_1513"
)
AFFECTED = [
    "DEL-02-01", "DEL-02-02", "DEL-02-03", "DEL-05-01", "DEL-07-04",
    "DEL-07-05", "DEL-08-02", "DEL-08-03", "DEL-09-03",
]
TARGET = "DEL-02-02"


def sha256(path: str) -> str:
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout.strip()


def section(lines: list[str], heading: str) -> list[str]:
    """Lines under the first heading whose text starts with `heading`, up to the next ## heading."""
    out: list[str] = []
    inside = False
    for line in lines:
        if line.startswith("## "):
            if inside:
                break
            inside = line[3:].strip().startswith(heading)
            continue
        if inside:
            out.append(line)
    if not out:
        raise SystemExit(f"unresolved section binding: {heading}")
    return out


def table_rows(lines: list[str], id_pattern: str) -> list[list[str]]:
    rows = []
    rx = re.compile(r"^\|\s*(" + id_pattern + r")\s*\|")
    for line in lines:
        if rx.match(line):
            rows.append([c.strip() for c in line.strip().strip("|").split("|")])
    return rows


def ids(cell: str, prefix: str) -> list[str]:
    return re.findall(prefix + r"-\d\d(?:-\d\d)?", cell) if prefix in ("PKG", "DEL") else re.findall(prefix + r"-\d{3}", cell)


def run_tool(cmd: list[str]) -> int:
    return subprocess.run(cmd, capture_output=True, text=True).returncode


def main() -> int:
    if not os.path.isfile(DECOMP):
        print("run from the repository root", file=sys.stderr)
        return 2
    lines = open(DECOMP, encoding="utf-8").read().splitlines()

    ssow = table_rows(section(lines, "5. SSOW"), r"SOW-\d{3}")
    objectives = table_rows(section(lines, "6. Objectives"), r"OBJ-\d{3}")
    packages = table_rows(section(lines, "7. Packages"), r"PKG-\d\d")
    deliverables = table_rows(section(lines, "8. Deliverables"), r"DEL-\d\d-\d\d")
    ledger = table_rows(section(lines, "9. Scope Ledger"), r"SOW-\d{3}")

    del_by_id = {r[0]: r for r in deliverables}
    retired = sorted(d for d, r in del_by_id.items() if "[RETIRED" in r[1] or "[RETIRED" in r[4])
    ledger_map = {r[0]: {"status": r[1], "package": r[4], "deliverables": ids(r[5], "DEL"), "objectives": ids(r[6], "OBJ")} for r in ledger}

    folders = {}
    for path in glob.glob(f"{EXEC}/PKG-*/1_Working/DEL-*"):
        m = re.search(r"(DEL-\d\d-\d\d)", os.path.basename(path))
        if m:
            folders[m.group(1)] = path
    declared = set(del_by_id)
    found = set(folders)

    # Deliverable -> covered scope items / supported objectives (reverse view).
    del_scope = {d: ids(r[6], "SOW") for d, r in del_by_id.items()}
    del_obj = {d: ids(r[7], "OBJ") for d, r in del_by_id.items()}

    # Scope items mapped to the target deliverable, and whether another carrier remains.
    target_items = []
    for sow, row in sorted(ledger_map.items()):
        if TARGET in row["deliverables"]:
            others = [d for d in row["deliverables"] if d != TARGET]
            target_items.append({"scope_item": sow, "status": row["status"], "other_mapped_deliverables": others,
                                 "only_deliverable": not others})
    target_objectives = []
    for obj in del_obj.get(TARGET, []):
        supporters = sorted(d for d, objs in del_obj.items() if obj in objs and d != TARGET and d not in retired)
        target_objectives.append({"objective": obj, "other_active_supporting_deliverables": len(supporters)})

    lifecycle = {}
    for d in AFFECTED:
        status = os.path.join(folders[d], "_STATUS.md")
        m = re.search(r"\*\*Current State:\*\*\s*(\S+)", open(status, encoding="utf-8").read())
        lifecycle[d] = m.group(1) if m else "UNKNOWN"
    all_states = Counter()
    for d, path in folders.items():
        m = re.search(r"\*\*Current State:\*\*\s*(\S+)", open(os.path.join(path, "_STATUS.md"), encoding="utf-8").read())
        all_states[m.group(1) if m else "UNKNOWN"] += 1

    # Dependency rows touching the target deliverable.
    dep_rows = []
    for reg in sorted(glob.glob(f"{EXEC}/PKG-*/1_Working/DEL-*/Dependencies.csv")):
        for r in csv.DictReader(open(reg, newline="", encoding="utf-8")):
            if r.get("FromDeliverableID") == TARGET or r.get("TargetDeliverableID") == TARGET:
                dep_rows.append({"DependencyID": r["DependencyID"], "From": r["FromDeliverableID"],
                                 "Class": r["DependencyClass"], "Direction": r["Direction"],
                                 "Type": r["DependencyType"], "Target": r["TargetDeliverableID"] or r["TargetRefID"],
                                 "Status": r.get("Status", ""), "SatisfactionStatus": r.get("SatisfactionStatus", "")})

    # Registered tools, into a temporary directory; summaries are path-sanitized.
    root = os.getcwd()
    tool = {}
    with tempfile.TemporaryDirectory() as tmp:
        rc = run_tool([sys.executable, "tools/evaluation/audit_structure.py", "--root", EXEC,
                       "--output", f"{tmp}/structure.json", "--variant", "SOFTWARE"])
        s = json.load(open(f"{tmp}/structure.json"))
        tool["audit_structure"] = {"exit": rc, "run_status": s["run_status"], "subject_status": s["subject_status"],
                                   "summary": s["summary"], "issues": s["issues"],
                                   "target_unit": next(({"current_state": u["current_state"],
                                                          "production_format": u["production_format"]["state"],
                                                          "valid": u["production_format"]["valid"]}
                                                         for u in s["units"] if u["id"] == TARGET), None)}
        rc = run_tool([sys.executable, "tools/coordination/analyze_dep_closure.py", EXEC, "--output-dir", f"{tmp}/closure"])
        c = json.load(open(f"{tmp}/closure/closure_summary.json"))
        tool["analyze_dep_closure"] = {"exit": rc, **{k: v for k, v in c.items() if not isinstance(v, (list, dict))}}
        rc = run_tool([sys.executable, "tools/validation/validate_decomposition_registers.py", EXEC,
                       "--json", f"{tmp}/registers.json", "--evidence-root", "."])
        v = json.load(open(f"{tmp}/registers.json"))
        tool["validate_decomposition_registers"] = {"exit": rc, "skipped": v.get("skipped"),
                                                    "registers_scanned": v.get("registers_scanned"),
                                                    "dependency_rows": v.get("dependency_rows"),
                                                    "findings_by_code": v.get("findings_by_code"),
                                                    "error_count": v.get("error_count"),
                                                    "warning_count": v.get("warning_count"),
                                                    "note": "XRG is skipped because the App carries no Deliverables.csv/ScopeLedger.csv; "
                                                            "EVQ-006 reflects deliverable-relative EvidenceFile paths (carried convention)."}
    text = json.dumps(tool, indent=2, sort_keys=True).replace(root + "/", "").replace(root, ".")
    tool = json.loads(text)

    prior_inputs = []
    manifest = os.path.join(PRIOR_AUDIT, "INPUT_MANIFEST.sha256")
    for line in open(manifest, encoding="utf-8"):
        h, rest = line.split(None, 1)
        p = rest.split("  #")[0].strip()
        cur = sha256(p) if os.path.isfile(p) else "MISSING"
        prior_inputs.append({"path": p, "prior": h, "current": cur, "identical": cur == h})

    envelopes = Counter(r[8] for r in deliverables)
    baseline = {
        "run_label": "SCA_APP_011_GROUP1_PRECHANGE",
        "decomp_variant": "SOFTWARE",
        "method": "Synthesized deterministic baseline from the authoritative decomposition plus registered structure, "
                  "dependency-closure and register tools (scope-change method step 5). A full audit-decomp TASK run was not "
                  "dispatched; the latest full audit is referenced below and its decomposition and companion-register inputs "
                  "are byte-identical to this basis.",
        "basis_commit": git("rev-parse", "HEAD"),
        "decomposition_path": DECOMP,
        "decomposition_sha256": sha256(DECOMP),
        "companion_register_path": REGISTER,
        "companion_register_sha256": sha256(REGISTER),
        "scope_change_pointer_sha256": sha256(POINTER),
        "active_snapshot": "execution/_ScopeChange/SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/",
        "accepted_project_dag": None,
        "repository_topology": {"packages": len(packages), "deliverables": len(deliverables),
                                "retired_deliverables": retired, "objectives": len(objectives),
                                "scope_items": len(ssow), "ledger_rows": len(ledger)},
        "ledger_distribution": dict(Counter(r[1] for r in ledger)),
        "context_envelopes": dict(sorted(envelopes.items())),
        "forward_coverage": {"declared": len(declared), "found": len(declared & found),
                             "missing_folders": sorted(declared - found)},
        "reverse_coverage": {"folders": len(found), "undeclared_folders": sorted(found - declared)},
        "scope_items_without_deliverable": sorted(s for s, r in ledger_map.items() if r["status"] == "IN" and not r["deliverables"]),
        "objectives_without_deliverable": sorted(o[0] for o in objectives
                                                 if not any(o[0] in v for d, v in del_obj.items() if d not in retired)),
        "lifecycle_distribution": dict(all_states),
        "issued_deliverables": sorted(d for d, p in folders.items()
                                      if "**Current State:** ISSUED" in open(os.path.join(p, "_STATUS.md"), encoding="utf-8").read()),
        "affected_lifecycle": lifecycle,
        "target_deliverable": {
            "id": TARGET,
            "decomposition_name": del_by_id[TARGET][1],
            "covers_scope_items": del_scope[TARGET],
            "supports_objectives": del_obj[TARGET],
            "scope_items_mapped_in_ledger": target_items,
            "objectives": target_objectives,
            "dependency_rows_touching": dep_rows,
        },
        "prior_full_audit": {"path": PRIOR_AUDIT, "inputs": prior_inputs,
                             "reuse": "Not reused as the baseline: instruction, workflow and pointer inputs differ. "
                                      "Decomposition and companion register are byte-identical."},
        "tools": tool,
    }
    out = os.path.join(SNAP_REL, "Pre_Change_Coverage.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(baseline, fh, indent=2, sort_keys=False)
        fh.write("\n")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
