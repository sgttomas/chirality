#!/usr/bin/env python3
"""audit-decomp run for the Chirality App SOFTWARE decomposition after SCA-APP-011 acceptance.

Run from the repository root. Read-only on every input; writes only into this
snapshot folder. Implements the twelve checks of the bundled `audit-decomp`
workflow (resources/method.md) for DECOMP_VARIANT = SOFTWARE with SCOPE = ALL.
"""
from __future__ import annotations

import csv
import datetime
import glob
import hashlib
import io
import json
import os
import re
import subprocess
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.relpath(HERE)
APP = "projects/chirality-app-dev/"
EX = APP + "execution/"
DECOMP = EX + "_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
REGISTER = EX + "_Decomposition/contract_invariant_coverage_register.csv"
POINTER = EX + "_ScopeChange/_LATEST.md"
PRIOR = EX + "_Evaluation/DecompCoverage/COV_SCA_APP_010_POST_RECORD_RECON_2026-09-22_2026-09-22_1513/"
LABEL = "SCA_APP_011_POST_ACCEPTANCE"
SCA_REQUIRED = ["Brief.md", "Intake_Actions.csv", "Impact_Assessment.md", "Amendment_Preview.md", "Propagation_Plan.md",
                "Amendment_Actions.csv", "Pre_Change_Coverage.json", "Post_Change_Coverage.json", "Decision_Log.md",
                "Handoff_State.md", "RUN_SUMMARY.md"]
RECOGNIZED = {"OPEN", "INITIALIZED", "SEMANTIC_READY", "IN_PROGRESS", "CHECKING", "ISSUED", "RETIRED"}
DECISIONS = {
    "SCA-APP-011": EX + "_ScopeChange/SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/",
    "D-APP-127": EX + "_Coordination/_DECISIONS/",
}


def sha(p):
    with open(p, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True, check=True).stdout.strip()


def headings(lines):
    out = []
    for i, ln in enumerate(lines):
        if ln.startswith("## "):
            t = re.sub(r"^\d+[A-Z]?\.\s*", "", ln[3:].strip()).strip().lower()
            out.append((i, t))
    return out


def section(lines, target):
    hs = headings(lines)
    t = target.lower()
    for rank in ("exact", "prefix", "sub"):
        hits = [(i, h) for i, h in hs if (h == t if rank == "exact" else h.startswith(t) if rank == "prefix" else t in h)]
        if hits:
            start = hits[0][0]
            nxt = [i for i, _ in hs if i > start]
            end = nxt[0] if nxt else len(lines)
            return lines[start + 1:end], start + 1
    raise SystemExit(f"FAILED_INPUTS: unresolved section {target}")


def table(sec_lines, offset, idcol_rx):
    rows, header = [], None
    for k, ln in enumerate(sec_lines):
        if not ln.startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if cells and not re.match(idcol_rx, cells[0]) and not set(cells[0]) <= set("-: "):
            header = cells
            continue
        if header and re.match(idcol_rx, cells[0]):
            rows.append(dict(zip(header, cells), _line=offset + k + 1))
    return rows


def ids(cell, rx):
    return re.findall(rx, cell or "")


def main():
    now = datetime.datetime.now(datetime.timezone.utc)
    lines = open(DECOMP, encoding="utf-8").read().split("\n")
    pk_sec, pk_off = section(lines, "Packages")
    dl_sec, dl_off = section(lines, "Deliverables")
    lg_sec, lg_off = section(lines, "Scope Ledger")
    ob_sec, ob_off = section(lines, "Objectives")
    packages = table(pk_sec, pk_off, r"^PKG-\d\d$")
    delivs = table(dl_sec, dl_off, r"^DEL-\d\d-\d\d$")
    ledger = table(lg_sec, lg_off, r"^SOW-\d{3}$")
    objectives = table(ob_sec, ob_off, r"^OBJ-\d{3}$")
    dmap = {d["DeliverableID"]: d for d in delivs}
    pids = {p["PackageID"] for p in packages}
    issues, matrix = [], []

    def issue(check, sev, etype, eid, desc, dref, fref, decision=""):
        issues.append(dict(IssueID=f"COV-{len(issues) + 1:03d}", CheckNumber=str(check), Severity=sev, EntityType=etype,
                           ConcreteLabel={"PARTITION": "Package", "PRODUCTION_UNIT": "Deliverable", "CONTEXT": "Deliverable",
                                          "ARTIFACT": "Deliverable", "OBJECTIVE": "Objective", "ATOMIC_UNIT": "Scope Item",
                                          "SNAPSHOT": "ScopeChange snapshot", "HANDOFF_STATE": "Handoff state",
                                          "DERIVATIVE_SURFACE": "Derivative surface"}.get(etype, etype),
                           EntityID=eid, Description=desc, DecompositionRef=dref, FilesystemRef=fref, DecisionRef=decision))

    # inventory
    pkg_folders = {re.match(r"(PKG-\d\d)", os.path.basename(p)).group(1): p for p in glob.glob(EX + "PKG-*") if os.path.isdir(p)}
    del_folders = {}
    for p in glob.glob(EX + "PKG-*/*/DEL-*"):
        if os.path.isdir(p):
            m = re.match(r"(DEL-\d\d-\d\d)", os.path.basename(p))
            del_folders.setdefault(m.group(1), []).append(p)
    struct_out = os.path.join(HERE, "structure.json")
    inv = {"schema_version": 1, "units": [{"path": os.path.relpath(v[0], EX), "required_files": []} for k, v in sorted(del_folders.items())]}
    json.dump(inv, open(os.path.join(HERE, "inventory.json"), "w"), indent=1)
    rc_struct = subprocess.run([sys.executable, "tools/evaluation/audit_structure.py", "--root", EX, "--variant", "SOFTWARE",
                                "--output", struct_out, "--inventory", os.path.join(HERE, "inventory.json")],
                               capture_output=True, text=True).returncode
    raw = open(struct_out, encoding="utf-8").read().replace(os.getcwd() + "/", "").replace(os.getcwd(), ".")
    open(struct_out, "w", encoding="utf-8").write(raw)  # path-sanitized
    struct = json.loads(raw)

    def state_of(path):
        m = re.search(r"\*\*Current State:\*\*\s*(\S+)", open(os.path.join(path, "_STATUS.md"), encoding="utf-8").read())
        return m.group(1) if m else "UNKNOWN"

    retired = {d for d, r in dmap.items() if "[RETIRED" in r.get("Name", "") or "[RETIRED" in r.get("Description", "")}
    dref = lambda d: f"{DECOMP}:{dmap[d]['_line']}"

    # Check 1
    c1_missing = sorted(pids - set(pkg_folders))
    for p in c1_missing:
        issue(1, "BLOCKER", "PARTITION", p, "Declared package has no folder", f"{DECOMP}:Packages", "NOT_FOUND")
    # Check 2
    c2_missing = sorted(set(dmap) - set(del_folders))
    for d in c2_missing:
        issue(2, "BLOCKER" if d not in retired else "EXPECTED_CONSEQUENCE", "PRODUCTION_UNIT", d, "Declared deliverable has no folder",
              dref(d), "NOT_FOUND")
    # Check 3
    extra_pk = sorted(set(pkg_folders) - pids)
    extra_dl = sorted(set(del_folders) - set(dmap))
    for p in extra_pk:
        issue(3, "WARNING", "PARTITION", p, "Package folder not declared in the decomposition (control-only surface)",
              f"{DECOMP}:Packages", pkg_folders[p])
    for d in extra_dl:
        issue(3, "WARNING", "PRODUCTION_UNIT", d, "Deliverable folder not declared in the decomposition (control-only surface)",
              f"{DECOMP}:Deliverables", del_folders[d][0])
    # Check 4
    c4 = 0
    for d, paths in del_folders.items():
        if len(paths) > 1:
            c4 += 1
            issue(4, "WARNING", "PRODUCTION_UNIT", d, "Deliverable found in more than one lifecycle folder", dref(d) if d in dmap else "", ";".join(paths))
        if d in dmap:
            expect = "PKG-" + d.split("-")[1]
            if not os.path.basename(os.path.dirname(os.path.dirname(paths[0]))).startswith(expect):
                c4 += 1
                issue(4, "WARNING", "PRODUCTION_UNIT", d, "Parent package folder does not match the ID", dref(d), paths[0])
    # Checks 5, 6, 11 and matrix
    ctx_counts = Counter()
    art_total = art_found = 0
    incomplete_ip = 0
    states = Counter()
    for d, paths in sorted(del_folders.items()):
        path = paths[0]
        st = state_of(path)
        states[st] += 1
        if st not in RECOGNIZED:
            issue(11, "INFO", "PRODUCTION_UNIT", d, f"Unexpected lifecycle state '{st}'", "", path + "/_STATUS.md")
        if d not in dmap:
            matrix.append(dict(ProductionUnitID=d, PartitionID="PKG-" + d.split("-")[1], ConcreteProductionUnitLabel="Deliverable",
                               ConcretePartitionLabel="Package", FolderExists=True, ContextPresent=os.path.exists(path + "/_CONTEXT.md"),
                               ContextMatch="N/A (undeclared)", ArtifactCoverage="N/A", ObjectivesMapped="N/A", LifecycleState=st,
                               IssueCount=sum(1 for i in issues if i["EntityID"] == d)))
            continue
        row = dmap[d]
        ctxp = path + "/_CONTEXT.md"
        cm = "MISSING"
        if os.path.exists(ctxp):
            ctx = open(ctxp, encoding="utf-8").read()
            fields = dict(re.findall(r"^\| (\w+) \| (.*?) \|$", ctx, re.M))
            want = {"PackageID": "PKG-" + d.split("-")[1], "DeliverableName": row["Name"], "ResponsibleParty": row["ResponsibleParty"],
                    "Type": row["Type"], "ContextEnvelope": row["ContextEnvelope"]}
            bad = []
            for k, v in want.items():
                got = fields.get(k, "")
                norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
                if k == "ResponsibleParty" and "TBD" in (got, v):
                    continue
                if norm(got) != norm(v):
                    bad.append((k, v, got))
            cm = "MATCH" if not bad else "PARTIAL"
            for k, v, got in bad:
                note = " (retired deliverable; its historical scaffold context is retained, as in the prior full audit)" if d in retired else ""
                issue(5, "WARNING", "CONTEXT", d, f"{k} in _CONTEXT.md does not match the Deliverables section: expected '{v}', found '{got}'{note}",
                      dref(d), ctxp)
        else:
            issue(5, "WARNING", "CONTEXT", d, "No _CONTEXT.md", dref(d), ctxp)
        ctx_counts[cm] += 1
        arts = [a.strip() for a in re.split(r";|<br>", row.get("AnticipatedArtifacts", "")) if a.strip()]
        files = [os.path.relpath(f, path).lower() for f in glob.glob(path + "/**/*", recursive=True) if os.path.isfile(f)]
        found = 0
        for a in arts:
            paths_in = re.findall(r"`([^`]+)`", a)
            hit = False
            for pth in paths_in:
                for base in (APP, APP + "frontend/", ""):
                    if os.path.exists(base + pth.strip("/")):
                        hit = True
            if not hit:
                toks = [t for t in re.findall(r"[a-z0-9]+", re.sub(r"`[^`]*`", "", a.lower())) if len(t) > 3]
                hit = bool(toks) and any(sum(t in f for t in toks) >= min(2, len(toks)) for f in files)
            found += hit
        if d not in retired:
            art_total += len(arts)
            art_found += found
            if found < len(arts):
                if st in ("IN_PROGRESS", "CHECKING", "ISSUED"):
                    incomplete_ip += 1
                issue(6, "WARNING" if st in ("IN_PROGRESS", "CHECKING", "ISSUED") else "INFO", "ARTIFACT", d,
                      f"{len(arts) - found}/{len(arts)} anticipated artifact descriptions have no path or filename match. "
                      "Structural screen only; not product acceptance.", dref(d) + " AnticipatedArtifacts", path)
        objs = ids(row.get("SupportsObjectives", ""), r"OBJ-\d{3}")
        matrix.append(dict(ProductionUnitID=d, PartitionID="PKG-" + d.split("-")[1], ConcreteProductionUnitLabel="Deliverable",
                           ConcretePartitionLabel="Package", FolderExists=True, ContextPresent=os.path.exists(ctxp), ContextMatch=cm,
                           ArtifactCoverage=f"{found}/{len(arts)}", ObjectivesMapped=f"{len(objs)}/{len(objs)}", LifecycleState=st,
                           IssueCount=0))
    for d in c2_missing:
        matrix.append(dict(ProductionUnitID=d, PartitionID="PKG-" + d.split("-")[1], ConcreteProductionUnitLabel="Deliverable",
                           ConcretePartitionLabel="Package", FolderExists=False, ContextPresent=False, ContextMatch="MISSING",
                           ArtifactCoverage="0/0", ObjectivesMapped="0/0", LifecycleState="UNKNOWN", IssueCount=0))
    # Check 7 (ledger ObjectiveID(s) authoritative for SOFTWARE)
    ledger_objs = sorted({o for r in ledger for o in ids(r.get("ObjectiveID(s)", ""), r"OBJ-\d{3}")})
    c7_bad = []
    for o in ledger_objs:
        sup = [d for d, r in dmap.items() if o in ids(r.get("SupportsObjectives", ""), r"OBJ-\d{3}") and d in del_folders and d not in retired]
        if not sup:
            c7_bad.append(o)
            issue(7, "WARNING", "OBJECTIVE", o, f"Objective {o} has no active supporting deliverable", f"{DECOMP}:Scope Ledger", "")
    declared_objs = sorted(o["ObjectiveID"] for o in objectives)
    unmapped = sorted(set(ledger_objs) ^ set(declared_objs))
    for o in unmapped:
        issue(7, "WARNING", "OBJECTIVE", o, "Objective appears in only one of the Objectives section and the Scope Ledger", f"{DECOMP}:Objectives", "")
    # Check 8
    c8_bad = 0
    ledger_states = Counter(r["InOutStatus"] for r in ledger)
    for r in ledger:
        if r["InOutStatus"] != "IN":
            continue
        if r["PackageID"] not in pids:
            c8_bad += 1
            issue(8, "WARNING", "ATOMIC_UNIT", r["ScopeItemID"], f"References package {r['PackageID']} which does not exist", f"{DECOMP}:{r['_line']}", "")
        for d in ids(r["DeliverableID(s)"], r"DEL-\d\d-\d\d"):
            if d not in dmap:
                c8_bad += 1
                issue(8, "WARNING", "ATOMIC_UNIT", r["ScopeItemID"], f"References deliverable {d} which does not exist", f"{DECOMP}:{r['_line']}", "")
            elif d in retired:
                issue(8, "WARNING", "ATOMIC_UNIT", r["ScopeItemID"], f"IN row mapped to retired deliverable {d}", f"{DECOMP}:{r['_line']}", "")
    reverse_mm = 0
    for d, row in dmap.items():
        cov = set(ids(row.get("CoversScopeItems", ""), r"SOW-\d{3}"))
        led = {r["ScopeItemID"] for r in ledger if d in ids(r["DeliverableID(s)"], r"DEL-\d\d-\d\d")}
        if cov != led:
            reverse_mm += 1
            issue(8, "WARNING", "PRODUCTION_UNIT", d, f"Deliverables CoversScopeItems and Scope Ledger reverse view differ: "
                  f"only in Deliverables {sorted(cov - led)}, only in Ledger {sorted(led - cov)}", dref(d), "")
    # Check 9b
    text = "\n".join(lines)
    companion = "contract_invariant_coverage_register" in text and "authoritative" in text.lower()
    if not companion:
        issue("9b", "WARNING", "DERIVATIVE_SURFACE", "companion inventory", "Main decomposition lacks a companion inventory statement", DECOMP, "")
    # Check 10
    ptr = open(POINTER, encoding="utf-8").read()
    snaps = re.findall(r"\*\*Active snapshot:\*\* `execution/_ScopeChange/([^`]+)/`", ptr)
    c10 = "PASS"
    active = None
    if len(snaps) != 1 or not os.path.isdir(EX + "_ScopeChange/" + snaps[0]):
        c10 = "BLOCKER"
        issue(10, "BLOCKER", "SNAPSHOT", "_LATEST.md", "Active snapshot contract failed: pointer does not name exactly one existing snapshot", POINTER, POINTER)
    else:
        active = EX + "_ScopeChange/" + snaps[0] + "/"
        missing = [f for f in SCA_REQUIRED if not os.path.exists(active + f)]
        smap = os.path.exists(active + "Supersession_Map.csv")
        if missing or not smap:
            c10 = "BLOCKER"
            issue(10, "BLOCKER", "SNAPSHOT", snaps[0], f"Active snapshot contract failed: missing {missing + ([] if smap else ['Supersession_Map.csv'])}", POINTER, active)
        hs = open(active + "Handoff_State.md", encoding="utf-8").read()
        closure_ok = "OPEN_PENDING_DERIVATIVE_CLOSURE" in hs and "`ACCEPTED`" in hs
        if not closure_ok:
            c10 = "WARNING" if c10 == "PASS" else c10
            issue(10, "WARNING", "HANDOFF_STATE", snaps[0], "Handoff_State.md does not show the accepted, open-pending-closure state", POINTER, active + "Handoff_State.md")
    # Other derivative observation: Coverage and Telemetry revision vs latest SCA
    tel_rev = re.search(r"\| Revision \| (.+?) \|", text)
    if tel_rev and "SCA-APP-011" not in tel_rev.group(1):
        issue(9, "INFO", "DERIVATIVE_SURFACE", "Coverage and Telemetry", "Telemetry revision does not name the latest accepted amendment", DECOMP, "")
    for m in matrix:
        m["IssueCount"] = sum(1 for i in issues if i["EntityID"] == m["ProductionUnitID"])

    sev = Counter(i["Severity"] for i in issues)
    status = "BLOCKERS" if sev.get("BLOCKER") else ("WARNINGS" if sev.get("WARNING") else "OK")
    verdict = lambda chk: ("BLOCKER" if any(i["CheckNumber"] == str(chk) and i["Severity"] == "BLOCKER" for i in issues) else
                           "WARNING" if any(i["CheckNumber"] == str(chk) and i["Severity"] == "WARNING" for i in issues) else "PASS")
    checks = [
        ("1 — Forward coverage: packages", verdict(1), f"{len(pids)} declared; {len(pids) - len(c1_missing)} with folders"),
        ("2 — Forward coverage: deliverables", verdict(2), f"{len(dmap)} declared; {len(dmap) - len(c2_missing)} with folders"),
        ("3 — Reverse coverage: folders", verdict(3), f"undeclared package folders {extra_pk}; undeclared deliverable folders {extra_dl} (control-only surfaces)"),
        ("4 — ID consistency", verdict(4), f"{c4} findings"),
        ("5 — Context fidelity", verdict(5), f"{dict(ctx_counts)} across {len(dmap)} declared deliverables; retired {sorted(retired)}"),
        ("6 — Artifact presence", verdict(6), f"path/filename screen {art_found}/{art_total} anticipated artifact descriptions over active declared units; "
                                              f"{incomplete_ip} IN_PROGRESS deliverables with incomplete matches. Structural screen, not product acceptance"),
        ("7 — Objective mapping", verdict(7), f"{len(ledger_objs)} ledger objectives; {len(c7_bad)} without active support; Objectives/ledger mismatches {unmapped}"),
        ("8 — Ledger integrity", verdict(8), f"{len(ledger)} rows {dict(ledger_states)}; {c8_bad} dangling references; {reverse_mm} reverse-view mismatches"),
        ("9 — Derivative package parity", "SKIPPED", "Not variant-owned for SOFTWARE (method Step 9); other derivative observations in the issue log"),
        ("9b — Package-shape conformance", verdict("9b"), "companion register labeled authoritative in the main document" if companion else "see issue log"),
        ("10 — Active snapshot and handoff state", c10 if c10 != "PASS" else verdict(10), f"active snapshot {snaps}"),
        ("11 — Lifecycle distribution", "PASS", f"{dict(states)}"),
    ]
    # SOW validator across physical folders
    sow = {}
    for d, paths in sorted(del_folders.items()):
        r = subprocess.run([sys.executable, "tools/scope_of_work/validate_scope_of_work.py", paths[0]], capture_output=True, text=True)
        sow[d] = r.returncode
    sow_pass = sum(1 for v in sow.values() if v == 0)
    # comparison mode
    prior = json.load(open(PRIOR + "coverage_summary.json"))
    prior_issue = Counter(r["Severity"] for r in csv.DictReader(open(PRIOR + "Decomp_Coverage_IssueLog.csv")))
    summary = {
        "run_label": LABEL, "timestamp": now.isoformat(timespec="seconds"), "decomp_variant": "SOFTWARE", "scope": "ALL",
        "requested_by": "WORKING_ITEMS (SCA-APP-011 post-acceptance follow-up)", "run_status": status,
        "expected_source_snapshot": active, "expected_handoff_phase": "SCA-APP-011 accepted; post-acceptance audit-decomp handoff (Propagation_Plan.md section 8 item 3); incremental setup and dependency re-extraction not yet run",
        "decomposition_path": DECOMP, "decomposition_sha256": sha(DECOMP), "companion_register_path": REGISTER,
        "companion_register_sha256": sha(REGISTER), "scope_change_pointer_sha256": sha(POINTER), "basis_commit": git("rev-parse", "HEAD"),
        "repository_topology": {"packages": len(pids), "deliverables": len(dmap), "objectives": len(declared_objs), "ledger_rows": len(ledger)},
        "ledger_distribution": dict(ledger_states),
        "physical_inventory": {"packages": len(pkg_folders), "deliverable_folders": len(del_folders), "undeclared_packages": extra_pk,
                               "undeclared_deliverables": extra_dl},
        "context_fidelity": dict(ctx_counts), "artifact_presence": {"matches": art_found, "descriptions": art_total,
                                                                     "incomplete_in_progress_deliverables": incomplete_ip},
        "lifecycle_distribution": dict(states), "scope_of_work_validator": f"{sow_pass}/{len(sow)} pass",
        "audit_structure": {"exit": rc_struct, "run_status": struct.get("run_status"), "summary": struct.get("summary"), "issues": struct.get("issues")},
        "checks": {c[0]: c[1] for c in checks}, "issue_counts": dict(sev), "overall_status": status,
        "closure_readiness": "FAIL" if (sev.get("BLOCKER") or "OPEN_PENDING_DERIVATIVE_CLOSURE" in open(active + "Handoff_State.md").read()) else "PASS",
        "comparison": {"prior_run": PRIOR, "prior_status": prior.get("run_status"), "prior_issue_counts": dict(prior_issue),
                       "prior_topology": prior.get("repository_topology"), "prior_ledger": prior.get("ledger_distribution")},
    }
    json.dump(summary, open(os.path.join(HERE, "coverage_summary.json"), "w"), indent=1)
    fields = ["IssueID", "CheckNumber", "Severity", "EntityType", "ConcreteLabel", "EntityID", "Description", "DecompositionRef", "FilesystemRef", "DecisionRef"]
    with open(os.path.join(HERE, "Decomp_Coverage_IssueLog.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n"); w.writeheader(); w.writerows(issues)
    mf = ["ProductionUnitID", "PartitionID", "ConcreteProductionUnitLabel", "ConcretePartitionLabel", "FolderExists", "ContextPresent",
          "ContextMatch", "ArtifactCoverage", "ObjectivesMapped", "LifecycleState", "IssueCount"]
    with open(os.path.join(HERE, "Decomp_Coverage_Matrix.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=mf, lineterminator="\n"); w.writeheader(); w.writerows(sorted(matrix, key=lambda m: m["ProductionUnitID"]))
    rep = [f"# SOFTWARE Decomposition Coverage Report\n\n- Run: `{LABEL}`\n- Timestamp: `{summary['timestamp']}`\n- Scope: `ALL`\n\n"
           f"Result: **{status}**; blockers: **{sev.get('BLOCKER', 0)}**.\n\n## Basis and boundary\n\n"
           f"Full structural audit of the App SOFTWARE decomposition after SCA-APP-011 was accepted and applied (active snapshot `{active}`). "
           f"Decomposition SHA-256 `{summary['decomposition_sha256']}`; companion register `{summary['companion_register_sha256']}`; "
           f"`_LATEST.md` `{summary['scope_change_pointer_sha256']}`; basis commit `{summary['basis_commit']}`. It checks structure and records; it is not "
           "product verification and asserts no owner acceptance. Incremental setup and dependency re-extraction for SCA-APP-011 have not run.\n\n"
           "## Core checks\n\n| Check | Result | Evidence |\n|---|---|---|\n"]
    rep += [f"| {c[0]} | **{c[1]}** | {c[2]} |\n" for c in checks]
    rep.append(f"\n## Scope of Work validation\n\n`validate_scope_of_work.py` on every physical deliverable folder: **{sow_pass}/{len(sow)}** pass.\n\n")
    rep.append(f"## Comparison with the prior full audit\n\nPrior: `{PRIOR}` ({prior.get('run_status')}; issues {dict(prior_issue)}). "
               f"Now: {status}; issues {dict(sev)}. Topology prior {prior.get('repository_topology')}, now {summary['repository_topology']}; "
               f"ledger prior {prior.get('ledger_distribution')}, now {dict(ledger_states)}. The artifact screen here is this run's path/filename "
               "heuristic (Step 6); its counts are not directly comparable with the prior run's filename-token screen.\n\n")
    rep.append("## Closure readiness\n\n" + ("**FAIL**: the active SCA-APP-011 snapshot remains `OPEN_PENDING_DERIVATIVE_CLOSURE` "
               "(incremental setup, dependency re-extraction and `audit-scope-closure` pending)." if summary["closure_readiness"] == "FAIL" else "PASS") + "\n")
    open(os.path.join(HERE, "Decomp_Coverage_Report.md"), "w", encoding="utf-8").write("".join(rep))
    open(os.path.join(HERE, "RUN_SUMMARY.md"), "w", encoding="utf-8").write(
        f"# Run Summary\n\n- RUN_STATUS = {status}\n- SCOPE = ALL\n- DECOMP_VARIANT = SOFTWARE\n- Declared topology: {len(pids)} packages / {len(dmap)} deliverables / "
        f"{len(declared_objs)} objectives / {len(ledger)} scope-ledger rows\n- Physical inventory: {len(pkg_folders)} package folders / {len(del_folders)} deliverable folders\n"
        f"- Checks: 12 core checks reported (Check 9 SKIPPED for SOFTWARE); blockers {sev.get('BLOCKER', 0)}\n- Issue counts: {dict(sev)}\n"
        f"- Closure readiness: {summary['closure_readiness']}\n- Owner or product acceptance: NOT ASSERTED\n- Full report: `Decomp_Coverage_Report.md`; metrics: `coverage_summary.json`\n")
    open(os.path.join(HERE, "QA_Report.md"), "w", encoding="utf-8").write(
        "# QA Report\n\n"
        f"- Inputs: decomposition `{summary['decomposition_sha256']}`; companion register `{summary['companion_register_sha256']}`; `_LATEST.md` `{summary['scope_change_pointer_sha256']}`.\n"
        f"- Parser (heading-text binding): {len(packages)} package rows, {len(delivs)} deliverable rows, {len(ledger)} ledger rows, {len(objectives)} objective rows.\n"
        f"- `tools/evaluation/audit_structure.py --root {EX} --variant SOFTWARE --inventory inventory.json --output structure.json`: exit {rc_struct}; "
        f"run_status {struct.get('run_status')}; summary {struct.get('summary')}; issues {struct.get('issues')}.\n"
        f"- `tools/scope_of_work/validate_scope_of_work.py` per physical deliverable folder: {sow_pass}/{len(sow)} pass.\n"
        "- Artifact presence is a path and filename screen (backticked paths resolved against the App root, the frontend root and the repository root; "
        "otherwise at least two long tokens of the description in one file name in the deliverable folder). Absence of a match is not proof the behavior is absent.\n"
        "- Limits: no semantic product verification; no file outside this snapshot folder was written; no decomposition, Scope of Work, dependency, "
        "lifecycle or pointer change. The DecompCoverage `_LATEST.md` pointer is not moved (not authorized by the brief).\n"
        "- Layout disclosure: before this snapshot's `MANIFEST.sha256` was generated, the report header was changed from Markdown hard line breaks (two trailing spaces) to plain list items so that `git diff --check` passes. The committed `audit_decomp_run.py` emits that layout, and a rerun of it with this run's timestamp reproduces the committed report files. The one checkout-dependent field, `basis_commit` in `coverage_summary.json`, is read from HEAD, so it matches only on the basis commit `78e74f590`.\n")
    open(os.path.join(HERE, "Decision_Log.md"), "w", encoding="utf-8").write(
        "# Decision Log\n\n- DECOMP_VARIANT = SOFTWARE; SCOPE = ALL; RUN_LABEL = SCA_APP_011_POST_ACCEPTANCE.\n"
        "- Check 7 objectives come from the Scope Ledger `ObjectiveID(s)` column (SOFTWARE rule); the Objectives section is compared for mismatches.\n"
        "- Check 8 uses the main document's Scope Ledger (no ScopeLedger.csv companion is named).\n"
        "- Undeclared PKG-00 / DEL-00-01 / DEL-00-02 are the disclosed control-only DAG-closure surfaces (WARNING, as in the prior run).\n"
        "- Retired deliverables are rows annotated `[RETIRED` in the Deliverables section.\n"
        "- Comparison mode against the prior full audit; artifact-screen counts are heuristic-specific.\n")
    open(os.path.join(HERE, "Brief.md"), "w", encoding="utf-8").write(
        "# Brief\n\n## Verbatim task brief\n\n"
        "Run the `audit-decomp` handoff that SCA-APP-011's records name (Propagation_Plan.md section 8 item 3; Handoff_State.md next owning workflows), "
        "following the workflow's own method, after the owner's checkpoint-group-3 acceptance and the merge of PR #995. Stop before any write that needs a "
        "human checkpoint, changes scope or changes lifecycle state.\n\n## Normalized parameters\n\n"
        f"- EXECUTION_ROOT: `{EX}`\n- DECOMPOSITION_PATH: `{DECOMP}`\n- DECOMP_VARIANT: `SOFTWARE`\n- SCOPE: `ALL`\n- RUN_LABEL: `{LABEL}`\n"
        f"- REQUESTED_BY: WORKING_ITEMS (coordinating session relay)\n- EXPECTED_SOURCE_SNAPSHOT: `{active}`\n"
        f"- ACCEPTED_DECISIONS: SCA-APP-011 (`checkpoint_snapshots/SCA-APP-011_GROUP-3_2026-09-27/`)\n- PRIOR_RUN_LABEL: `{PRIOR}`\n- Snapshot: `{OUT}`\n")
    ins = sorted(set([DECOMP, REGISTER, POINTER] + [active + f for f in SCA_REQUIRED] + [p + "/_CONTEXT.md" for v in del_folders.values() for p in v if os.path.exists(p + "/_CONTEXT.md")]
                     + [p + "/_STATUS.md" for v in del_folders.values() for p in v]))
    open(os.path.join(HERE, "INPUT_MANIFEST.sha256"), "w").write("".join(f"{sha(p)}  {p}\n" for p in ins))
    outs = [f for f in sorted(os.listdir(HERE)) if f not in ("MANIFEST.sha256", "__pycache__")]
    open(os.path.join(HERE, "MANIFEST.sha256"), "w").write("".join(f"{sha(os.path.join(HERE, f))}  {f}\n" for f in outs))
    print(status, dict(sev), summary["closure_readiness"])
    for c in checks:
        print(" ", c[1], c[0], "|", c[2][:150])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
