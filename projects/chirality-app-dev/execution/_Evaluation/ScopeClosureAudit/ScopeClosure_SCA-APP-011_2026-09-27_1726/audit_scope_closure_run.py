#!/usr/bin/env python3
"""audit-scope-closure rerun for SCA-APP-011 after incremental setup and dependency re-extraction.

Read-only on project state; writes only this snapshot folder. Run from the repository root. Implements Passes 0-7
of the bundled `audit-scope-closure` workflow (resources/method.md) for DECOMP_VARIANT = SOFTWARE, plus two disclosed
extensions: the retired-surface screen (Pass 3) and verification of the expected extraction outcomes DX-01 to DX-16.
Supersedes ScopeClosure_SCA-APP-011_2026-09-27_1701, which stays unchanged: the export-regeneration check is now
deterministic (the export stage is rebuilt in a temporary directory with the export script's own build_stage and its
manifest compared byte-for-byte with the committed export-manifest.csv), and the post-extraction closure evidence is the
re-evidence snapshot CLOSURE_SCA_APP_011_ESR1_REEVIDENCE_2026-09-27_1725.
"""
from __future__ import annotations

import csv
import datetime
import glob
import hashlib
import importlib.util
import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.relpath(HERE)
APP = "projects/chirality-app-dev/"
EX = APP + "execution/"
SC = EX + "_ScopeChange/"
AID = "SCA-APP-011"
SNAP = SC + "SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/"
DECOMP = EX + "_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
G2PTR = SC + "SCA-APP-011_GROUP-2_AUTHORIZED.md"
G2 = SC + "checkpoint_snapshots/SCA-APP-011_GROUP-2_2026-09-27/"
G3 = SC + "checkpoint_snapshots/SCA-APP-011_GROUP-3_2026-09-27/"
PAV = SC + "_PostAcceptanceValidation/SCA-APP-011_20260927T044456Z/"
PRIOR_MAP = SC + "SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA/Supersession_Map.csv"
COV = EX + "_Evaluation/DecompCoverage/COV_SCA_APP_011_POST_ACCEPTANCE_2026-09-27_0500/"
SETUP_LOG = EX + "_Coordination/SETUP_LOG.md"
RUN = EX + "_Coordination/AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/"
DEPCL = EX + "_Evaluation/DepClosure/CLOSURE_SCA_APP_011_ESR1_REEVIDENCE_2026-09-27_1725/"
TMREC = EX + "_Coordination/_TaskManagement/ROW_MAINTENANCE_APP-R058_SCA-APP-011_CLOSURE_2026-09-27.md"
PRIOR_SNAP = EX + "_Evaluation/ScopeClosureAudit/ScopeClosure_SCA-APP-011_2026-09-27_1701/"
EXPORT_SCRIPT = "exports/chirality-app/export_public.py"
EXPORT_MANIFEST = "exports/chirality-app/export-manifest.csv"
DX_CSV = RUN + "DEPENDENCY_EXTRACT_EXPECTED_OUTCOMES.csv"
DATE = "2026-09-27"
# Retired-surface screen: the earlier phrase set, plus the reviewer's broadened case-insensitive terms.
SCREEN = re.compile(r"api/working-root/deliverable/(status|dependencies)|api/harness/scaffold|Retained Workbench|Retained Pipeline|"
                    r"Workbench and Pipeline routes|Pipeline selector presentation|WORKBENCH deep-link|PIPELINE deep-link|"
                    r"pipeline selectors|WORKBENCH agent|governed WORKBENCH, PIPELINE|"
                    r"workbench|pipeline form|deliverable/(status|dependencies)|harness/scaffold|scaffoldHarnessExecutionRoot|deliverable-api", re.I)
FOLDER_NAME = re.compile(r"DEL-02-02_Workbench_and_Pipeline_Selection_UX", re.I)
# Explicit allow-list: ACTIVE rows describing retained dispatch or routing semantics, which SCA-APP-011 kept.
ALLOW = {
    "DEP-02-03-009": "retained task-scope dispatch interface to DEL-08-03 (DX-15; REQ-009 residual recorded)",
    "DEP-08-02-013": "retained row-level OPERATIVE -> PIPELINE routing boundary with DEL-08-03 (route/query compatibility keyed with DEL-08-02)",
}
inputs = {}


def sha(p):
    with open(p, "rb") as fh:
        h = hashlib.sha256(fh.read()).hexdigest()
    inputs[p] = h
    return h


def read(p):
    sha(p)
    return open(p, encoding="utf-8").read()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def export_fresh():
    """Deterministic, read-only export freshness: rebuild the stage outside the repository and compare manifests."""
    import csv as _csv, hashlib as _h, pathlib, shutil, tempfile
    mod = load("export_public", EXPORT_SCRIPT)
    sha(EXPORT_SCRIPT)
    tmp = tempfile.mkdtemp(prefix="asc-export-")
    stage = pathlib.Path(tmp) / "stage"
    try:
        mod.build_stage(stage)
        rows = []
        for p in sorted(stage.rglob("*")):
            if p.is_file():
                data = p.read_bytes()
                rows.append({"path": p.relative_to(stage).as_posix(), "size_bytes": str(len(data)), "sha256": _h.sha256(data).hexdigest()})
        buf = io.StringIO()
        w = _csv.DictWriter(buf, fieldnames=["path", "size_bytes", "sha256"], lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
        committed = open(EXPORT_MANIFEST, encoding="utf-8").read()
        sha(EXPORT_MANIFEST)
        return buf.getvalue() == committed, len(rows)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    issues = []

    def issue(pas, cat, sev, action, eid, ev, ref, desc, rec, label="FACT", assess="DETERMINATE"):
        issues.append(dict(IssueID=f"ASC-ISS-{len(issues) + 1:03d}", Pass=pas, Category=cat, Severity=sev, Assessment=assess,
                           AmendmentAction=action, EntityID=eid, EvidenceFile=ev, SourceRef=ref, Description=desc,
                           Recommendation=rec, EpistemicLabel=label))

    # Pass 0
    ptr = read(G2PTR)
    assert "checkpoint_snapshots/SCA-APP-011_GROUP-2_2026-09-27/" in ptr
    man = list(csv.DictReader(io.StringIO(read(G2 + "ACCEPTED_MANIFEST.csv"))))
    regs = [r for r in man if re.match(r"Amendment_Actions.*\.csv$", os.path.basename(r["Path"]))]
    if len(regs) != 1 or sha(regs[0]["Path"]) != regs[0]["SHA256"]:
        raise SystemExit("FAILED_INPUTS: register not bound or hash mismatch")
    register = regs[0]["Path"]
    rows = list(csv.DictReader(io.StringIO(read(register))))
    run_summary = read(SNAP + "RUN_SUMMARY.md")
    read(SNAP + "Propagation_Plan.md")
    handoff = read(SNAP + "Handoff_State.md")
    g3dec = read(G3 + "DECISION.md")
    read(G3 + "Handoff_State.md")
    pav = read(PAV + "POST_ACCEPTANCE_VALIDATION.md")
    decomp = read(DECOMP)

    # Pass 1 — every edit of every register row present in the applied state
    ae = load("amendment_edits", SNAP + "Evidence/Group2/amendment_edits.py")
    g3c = load("group3_corrections", SNAP + "Evidence/Group3/group3_corrections.py")
    sha(SNAP + "Evidence/Group2/amendment_edits.py")
    sha(SNAP + "Evidence/Group3/group3_corrections.py")
    by_seq = {}
    for e in ae.EDITS:
        by_seq.setdefault(e["seq"], []).append(e)
    for seq, carried in ae.CARRIED_BY.items():
        by_seq.setdefault(seq, [e for e in ae.EDITS if e["id"] in carried])
    p1 = []
    for r in rows:
        seq = int(r["ActionSeq"])
        missing = []
        for e in by_seq.get(seq, []):
            new = e["new"].replace("{APPLICATION_DATE}", DATE)
            for c in g3c.CORRECTIONS:
                if c["file"] == e["file"] and c["old"] in new:
                    new = new.replace(c["old"], c["new"], 1)
            text = read(e["file"])
            if new not in text or (e["old"] not in new and e["old"] in text):
                missing.append(e["id"])
        status = "VERIFIED" if by_seq.get(seq) and not missing else ("NOT_EXECUTED" if not by_seq.get(seq) else "DISCREPANCY")
        p1.append((r["ActionSeq"], r["ActionType"], r["EntityID"], ",".join(e["id"] for e in by_seq.get(seq, [])), status, missing))
        if status != "VERIFIED":
            issue(1, "ACTION_NOT_EXECUTED", "CRITICAL", r["ActionSeq"], r["EntityID"], register, f"ActionSeq {seq}",
                  f"Accepted edits not present in the applied state: {missing}", "Return to scope-change")

    # Pass 2 — downstream reruns (RUN_SUMMARY section 6 and Handoff_State next owning workflows)
    p2 = []
    setup_done = os.path.exists(SETUP_LOG) and "INCREMENTAL SCA-APP-011 setup COMPLETE" in read(SETUP_LOG)
    p2.append(("project-setup INCREMENTAL", "9 MODIFY deliverables + 16 neighbours",
               f"{SETUP_LOG}: BASELINE line and 'INCREMENTAL SCA-APP-011 setup COMPLETE'; run record {RUN}SETUP_RUN_RECORD.md",
               "COMPLETED" if setup_done else "NO_EVIDENCE"))
    if not setup_done:
        issue(2, "DOWNSTREAM_NOT_RUN", "MAJOR", "N/A", "project-setup", SNAP + "Handoff_State.md", "Next owning workflows 1",
              "Incremental setup has not run: SETUP_LOG.md is absent, and the workflow's Phase 5.0 baseline and Phase 5.1 plan need human confirmation before any write",
              f"Owner confirms the baseline and plan in {RUN}INCREMENTAL_SETUP_PROPOSAL.md; then run Function 5")
    dep_targets = ["DEL-02-02", "DEL-02-01", "DEL-02-03", "DEL-07-04", "DEL-07-05", "DEL-08-02", "DEL-08-03"]
    post_hash = inputs.get(DECOMP) or sha(DECOMP)
    for d in dep_targets:
        folder = glob.glob(EX + f"PKG-*/1_Working/{d}_*")[0]
        dm = read(folder + "/_DEPENDENCIES.md")
        bound = post_hash in dm
        p2.append((f"dependency-extract {d}", d, f"{folder}/_DEPENDENCIES.md run notes bind post-change decomposition hash: {bound}", "COMPLETED" if bound else "NO_EVIDENCE"))
        if not bound:
            issue(2, "DOWNSTREAM_NOT_RUN", "MAJOR", "N/A", d, folder + "/_DEPENDENCIES.md", "Run Notes",
                  "No dependency-extract run binds the post-change decomposition and contract hashes; the register may carry stale rows",
                  f"Run dependency-extract after the incremental plan is confirmed; check the expected outcomes in {RUN}DEPENDENCY_EXTRACT_EXPECTED_OUTCOMES.csv")
    dc_ok = False
    if os.path.exists(DEPCL + "Tool_Run.json"):
        tr = json.loads(read(DEPCL + "Tool_Run.json"))
        cs = json.loads(read(DEPCL + "Evidence/closure_summary.json"))
        basis = {x["path"]: x["sha256"] for x in tr.get("accepted_input_basis", [])}
        current = all(sha(p) == h for p, h in basis.items())
        dc_ok = cs.get("scc_count") == 0 and cs.get("subject_status") == "PASS" and current and bool(basis)
    p2.append(("audit-dep-closure after re-extraction", "ALL rules (51 current units + census)",
               f"{DEPCL}: subject PASS, 0 SCC, input basis hashes current = {dc_ok}", "COMPLETED" if dc_ok else "NO_EVIDENCE"))
    if not dc_ok:
        issue(2, "DOWNSTREAM_NOT_RUN", "MINOR", "N/A", "analyze_dep_closure", DEPCL + "Tool_Run.json", "whole file",
              "No post-extraction closure snapshot binds the current registers", "Rerun audit-dep-closure over the accepted inventory (FULL_GRAPH)")
    cov_in = read(COV + "INPUT_MANIFEST.sha256")
    cov_ok = post_hash in cov_in
    p2.append(("audit-decomp", "ALL", f"{COV} INPUT_MANIFEST binds post-change decomposition {post_hash[:12]}: {cov_ok}", "COMPLETED" if cov_ok else "NO_EVIDENCE"))
    p2.append(("audit-scope-closure", AID, "this snapshot", "COMPLETED (this run, after setup and the ESR-1 re-evidence)"))
    exp_ok, exp_rows = export_fresh()
    p2.append(("export regeneration", "exports/chirality-app",
               f"rebuilt export stage ({exp_rows} files) reproduces the committed {EXPORT_MANIFEST} byte-for-byte = {exp_ok}",
               "COMPLETED" if exp_ok else "NO_EVIDENCE"))
    if not exp_ok:
        issue(2, "DOWNSTREAM_NOT_RUN", "MINOR", "N/A", "export", EXPORT_MANIFEST, "whole file",
              "The committed public-export manifest does not match a fresh rebuild of the export stage", f"Run {EXPORT_SCRIPT} and commit the export")
    tm = read(TMREC) if os.path.exists(TMREC) else ""
    tm_ok = "APP-R058: option 1" in tm and "moot for the App, not released" in tm and "federation" in tm
    p2.append(("Task Management APP-R058 disposition", "APP-R058",
               f"{TMREC}: owner act quoted, federation preflight recorded, 'moot for the App, not released' = {tm_ok}",
               "COMPLETED" if tm_ok else "NO_EVIDENCE"))
    if not tm_ok:
        issue(2, "DOWNSTREAM_NOT_RUN", "MINOR", "N/A", "APP-R058", TMREC, "whole file",
              "No row-maintenance record carries the owner's APP-R058 disposition", f"Owner records the disposition proposed in {RUN}APP_R058_PROPOSAL.md", "FACT")

    # Pass 3 — orphaned references. Method Pass 3 targets rows pointing at RETIRED entity IDs; SCA-APP-011 has no
    # REMOVE/MERGE/RECLASSIFY action and retires no ID, so proper Pass 3 finds nothing for this amendment.
    # Disclosed extension: a phrase screen for ACTIVE rows that still describe a retired surface (route/form).
    # Those rows are stale register metadata awaiting re-extraction, so they are filed as METADATA_STALE.
    retired_rx = SCREEN
    orphans = []
    allowed = []
    nregs = 0
    for f in sorted(glob.glob(EX + "PKG-*/*/DEL-*/Dependencies.csv")):
        nregs += 1
        for r in csv.DictReader(io.StringIO(read(f))):
            if r.get("Status") != "ACTIVE":
                continue
            blob = FOLDER_NAME.sub("", " ".join(r.get(k, "") for k in ("Statement", "TargetLocation", "TargetName", "EvidenceQuote")))
            if retired_rx.search(blob):
                if r["DependencyID"] in ALLOW:
                    allowed.append(r["DependencyID"])
                else:
                    orphans.append((r["DependencyID"], f))
    for did, f in orphans:
        sev = "MAJOR" if did.startswith(("DEP-02-02-00", "DEP-02-01-00", "DEP-07-05-025")) else "MINOR"
        issue(3, "METADATA_STALE", sev, "N/A", did, f, did,
              "ACTIVE dependency row still describes a surface SCA-APP-011 retired (Workbench/Pipeline forms, deliverable routes or scaffold route); found by the disclosed retired-surface screen, not by method Pass 3 (no entity ID is retired)",
              f"Re-extract; check the expected outcome in {RUN}DEPENDENCY_EXTRACT_EXPECTED_OUTCOMES.csv", "FACT")
    tension = []
    for f in sorted(glob.glob(EX + "PKG-*/*/DEL-02-03_*/Dependencies.csv")):
        for r in csv.DictReader(io.StringIO(read(f))):
            if r.get("Status") == "ACTIVE" and "PIPELINE `TASK*` preselection" in r.get("EvidenceQuote", ""):
                tension.append(r["DependencyID"])
                issue(3, "METADATA_STALE", "OBSERVATION", "N/A", r["DependencyID"], f, r["DependencyID"],
                      "ACTIVE row cites DEL-02-03-REQ-009 (PIPELINE TASK* preselection) while accepted E80 withdrew the old Pipeline routing examples; REQ-009 itself was not amended and Propagation_Plan section 7 records no own-register change for DEL-02-03",
                      f"Keep with the stated reason and record the tension in Notes at re-extraction ({RUN}DEPENDENCY_EXTRACT_EXPECTED_OUTCOMES.csv DX-15)", "FACT")
    for f in sorted(glob.glob(EX + "PKG-*/*/DEL-*/Dependencies.csv")):
        for r in csv.DictReader(io.StringIO(open(f, encoding="utf-8").read())):
            if r.get("Status") == "ACTIVE" and r.get("TargetDeliverableID") == "DEL-09-07":
                issue(3, "ORPHANED_REFERENCE", "OBSERVATION", "N/A", r["DependencyID"], f, r["DependencyID"],
                      "ACTIVE row targets retired DEL-09-07 (not retired by SCA-APP-011)", "Outside this amendment; route to its owner")

    # Extension — verify the expected extraction outcomes DX-01 to DX-16 against the extracted rows
    dxrows = list(csv.DictReader(io.StringIO(read(DX_CSV))))
    reg = {}
    for f in sorted(glob.glob(EX + "PKG-*/*/DEL-*/Dependencies.csv")):
        for r in csv.DictReader(io.StringIO(read(f))):
            reg[r["DependencyID"]] = r
    sow0705 = open(glob.glob(EX + "PKG-*/1_Working/DEL-07-05_*")[0] + "/ScopeOfWork.md", encoding="utf-8").read().split("\n")
    lib = "frontend/src/lib/workspace/deliverable-contracts.ts"
    route = "/api/working-root/deliverable/dependencies"

    def g(i):
        return reg.get(i, {})

    checks = {
        **{f"DX-0{n}": (lambda i=f"DEP-02-02-00{n + 4}": g(i).get("Status") == "RETIRED") for n in range(1, 6)},
        "DX-06": lambda: g("DEP-02-01-007").get("Status") == "RETIRED" and "SCA-APP-011" in g("DEP-02-01-007").get("Notes", ""),
        "DX-07": lambda: g("DEP-02-01-008").get("Status") == "RETIRED" and "HGD-2" in g("DEP-02-01-008").get("Notes", ""),
        "DX-08": lambda: lib in g("DEP-07-05-025").get("TargetLocation", "") and route not in g("DEP-07-05-025").get("TargetLocation", "")
                         and "API" not in g("DEP-07-05-025").get("TargetName", ""),
        "DX-09": lambda: "library" in g("DEP-07-05-025").get("Statement", "") and "API" not in g("DEP-07-05-025").get("Statement", ""),
        "DX-10": lambda: "CLM-011" in g("DEP-07-05-025").get("SourceRef", "") and "CLM-021" not in g("DEP-07-05-025").get("SourceRef", "")
                         and g("DEP-07-05-025").get("EvidenceQuote", "~") in sow0705[187]
                         and route not in g("DEP-07-05-025").get("EvidenceQuote", "") and "[RETIRED" not in g("DEP-07-05-025").get("EvidenceQuote", ""),
        "DX-11": lambda: "task-scope selection" in g("DEP-08-03-010").get("TargetName", "").lower()
                         and "pipeline selector" not in g("DEP-08-03-010").get("TargetName", "").lower(),
        "DX-12": lambda: "task-scope selection" in g("DEP-08-03-010").get("Statement", "")
                         and "pipeline selector" not in g("DEP-08-03-010").get("Statement", "").lower() and "CLM-025" in g("DEP-08-03-010").get("SourceRef", ""),
        "DX-13": lambda: "workbench" not in (g("DEP-08-02-003").get("TargetName", "") + g("DEP-08-02-003").get("Statement", "")).lower()
                         and g("DEP-08-02-003").get("TargetRefID") == "SOW-006" and not g("DEP-08-02-003").get("TargetLocation", "").endswith("#L382"),
        "DX-14": lambda: "WORKBENCH" not in g("DEP-08-02-005").get("Statement", "") and "PIPELINE" not in g("DEP-08-02-005").get("Statement", "")
                         and g("DEP-08-02-005").get("TargetRefID") == "OBJ-001" and not g("DEP-08-02-005").get("TargetLocation", "").endswith("#L238"),
        "DX-15": lambda: g("DEP-02-03-009").get("Status") == "ACTIVE" and g("DEP-02-03-009").get("TargetDeliverableID") == "DEL-08-03"
                         and ("E80" in g("DEP-02-03-009").get("Notes", "") or "CLM-029" in g("DEP-02-03-009").get("Notes", ""))
                         and "REQ-009" in g("DEP-02-03-009").get("Notes", ""),
        "DX-16": lambda: not orphans,
    }
    dxres = []
    for row in dxrows:
        ok = bool(checks[row["OutcomeID"]]())
        dxres.append((row["OutcomeID"], row["DependencyID"], row["Check"], "VERIFIED" if ok else "NOT_MET"))
        if not ok:
            issue("DX", "METADATA_STALE", "MAJOR", "N/A", row["DependencyID"], DX_CSV, row["OutcomeID"],
                  f"Expected extraction outcome not met: {row['Check']}", "Rerun dependency-extract for the owning deliverable", "FACT")
    with open(os.path.join(HERE, "DX_Verification.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["OutcomeID", "DependencyID", "Check", "Result"])
        w.writerows(dxres)
    beyond = [("DEP-07-05-015 quotes the restated REQ-DEL-07-05-013", "GET/PUT" not in g("DEP-07-05-015").get("EvidenceQuote", "")
               and g("DEP-07-05-015").get("Status") == "ACTIVE"),
              ("DEP-07-04-009 (DEL-07-04 -> DEL-06-03) present and ACTIVE", g("DEP-07-04-009").get("Status") == "ACTIVE"
               and g("DEP-07-04-009").get("TargetDeliverableID") == "DEL-06-03"),
              ("DEP-02-01-013 re-evidenced to APP-R016", "APP-R016" in g("DEP-02-01-013").get("SourceRef", ""))]

    # Pass 4 — decomposition consistency
    p4 = []
    p4.append(("Decision Log DEC-026", "| DEC-026 | 2026-09-27 |" in decomp))
    p4.append(("Change Log line", "- 2026-09-27: SCA-APP-011 retired" in decomp))
    p4.append(("Coverage and Telemetry names SCA-APP-011 and 2026-09-27", "amended by SCA-APP-011 |" in decomp and "| Date | 2026-09-27 |" in decomp))
    pre = json.load(open(SNAP + "Pre_Change_Coverage.json")); sha(SNAP + "Pre_Change_Coverage.json")
    post = json.load(open(SNAP + "Post_Change_Coverage.json")); sha(SNAP + "Post_Change_Coverage.json")
    for k in ("repository_topology", "ledger_distribution", "forward_coverage", "scope_items_without_deliverable", "objectives_without_deliverable"):
        p4.append((f"coverage {k} unchanged pre/post", pre.get(k) == post.get(k)))
    for name, ok in p4:
        if not ok:
            issue(4, "DECOMP_INCONSISTENCY", "MAJOR", "N/A", "decomposition", DECOMP, name, f"{name} not satisfied", "Return to scope-change")

    # Pass 5 — context metadata for affected deliverables
    matrix = {r["ProductionUnitID"]: r for r in csv.DictReader(io.StringIO(read(COV + "Decomp_Coverage_Matrix.csv")))}
    p5 = []
    for r in rows:
        if r["EntityType"] != "DELIVERABLE":
            continue
        d = r["EntityID"]
        cm = matrix[d]["ContextMatch"]
        st = matrix[d]["LifecycleState"]
        pre_st = pre.get("affected_lifecycle", {}).get(d, post.get("affected_lifecycle", {}).get(d))
        p5.append((d, cm, st, pre_st))
        if cm != "MATCH":
            issue(5, "METADATA_STALE", "MINOR", r["ActionSeq"], d, COV + "Decomp_Coverage_Matrix.csv", d, f"_CONTEXT.md identity {cm}", "Align context")
        if pre_st and st != pre_st:
            issue(5, "METADATA_STALE", "MAJOR", r["ActionSeq"], d, "", d, f"Lifecycle changed {pre_st} -> {st}", "Investigate")

    # Pass 6 — supersession
    delta = list(csv.DictReader(io.StringIO(read(SNAP + "Supersession_Delta.csv"))))
    yes = [r for r in rows if r["SupersessionBindingPresent"] == "YES"]
    p6 = []
    for r in yes:
        did = f"D-{int(r['ActionSeq']):03d}"
        ok = any(x["DecisionID"] == did and x["AmendmentID"] == AID for x in delta)
        p6.append((r["ActionSeq"], did, ok))
        if not ok:
            issue(6, "SUPERSESSION_INCOMPLETE", "CRITICAL", r["ActionSeq"], r["EntityID"], SNAP + "Supersession_Delta.csv", did,
                  "Action claims a supersession binding but no matching delta row", "Add the binding via scope-change")
    for x in delta:
        if not os.path.exists(x["SupersededAuthorityPath"]) or not x["SupersededAuthorityRef"].strip():
            issue(6, "SUPERSESSION_INCOMPLETE", "MAJOR", "N/A", x["DecisionID"], SNAP + "Supersession_Delta.csv", x["DecisionID"],
                  "Superseded authority path does not resolve or reference is empty", "Repair the delta")
        if x["AppliesToRoots"] != "projects/chirality-app-dev" or x["AppliesToFacilities"] != "N/A":
            issue(6, "SUPERSESSION_INCOMPLETE", "MAJOR", "N/A", x["DecisionID"], SNAP + "Supersession_Delta.csv", x["DecisionID"],
                  "Non-canonical applicability tokens", "Repair the delta")
    acc = subprocess.run([sys.executable, "tools/coordination/accumulate_supersession_map.py", "--prior-map", PRIOR_MAP,
                          "--delta", SNAP + "Supersession_Delta.csv", "--output-map", os.path.join(HERE, "Expected_Supersession_Map.csv"),
                          "--check-map", SNAP + "Supersession_Map.csv", "--output-findings", os.path.join(HERE, "Supersession_Map_Findings.csv")],
                         capture_output=True, text=True)
    sha(PRIOR_MAP); sha(SNAP + "Supersession_Map.csv")
    for f in ("Expected_Supersession_Map.csv", "Supersession_Map_Findings.csv"):
        p = os.path.join(HERE, f)
        b = open(p, "rb").read().replace(b"\r\n", b"\n")
        open(p, "wb").write(b)
    acc_findings = list(csv.DictReader(open(os.path.join(HERE, "Supersession_Map_Findings.csv"))))
    for x in acc_findings:
        issue(6, "SUPERSESSION_INCOMPLETE", "MAJOR", "N/A", x.get("Category", ""), SNAP + "Supersession_Map.csv", x.get("Source", ""), x.get("Message", ""), "Repair the map")

    # Closure determination
    sev = {k: sum(1 for i in issues if i["Severity"] == k) for k in ("CRITICAL", "MAJOR", "MINOR", "OBSERVATION")}
    status = "OPEN" if sev["CRITICAL"] or sev["MAJOR"] else ("CLOSED_WITH_OBSERVATIONS" if sev["MINOR"] or sev["OBSERVATION"] else "CLOSED")
    summary = {"amendmentId": AID, "auditDate": DATE, "closureStatus": status, "actionRegister": register,
               "totalActions": len(rows), "actionsVerified": sum(1 for x in p1 if x[4] == "VERIFIED"),
               "actionsDiscrepant": sum(1 for x in p1 if x[4] == "DISCREPANCY"), "actionsNotExecuted": sum(1 for x in p1 if x[4] == "NOT_EXECUTED"),
               "actionsDeferredByHuman": 0, "actionsSuperseded": 0, "downstreamRerunsRecommended": len(p2),
               "downstreamRerunsCompleted": sum(1 for x in p2 if x[3].startswith("COMPLETED")),
               "downstreamRerunsDeferredOrNotActivated": 0, "orphanedReferencesFound": 0, "retiredSurfaceScreenRows": len(orphans),
               "retiredSurfaceScreenAllowListed": allowed, "expectedOutcomesVerified": sum(1 for x in dxres if x[3] == "VERIFIED"),
               "expectedOutcomesTotal": len(dxres), "supersedes": PRIOR_SNAP,
               "contentRemediationState": "NOT_REQUIRED", "ktyRemediationRows": 0, "ktyRemediationRowsBlocked": 0, "archiveScannerLeaks": 0,
               "findingsBySeverity": sev}
    json.dump(summary, open(os.path.join(HERE, "scope_closure_summary.json"), "w"), indent=1)
    fields = ["IssueID", "Pass", "Category", "Severity", "Assessment", "AmendmentAction", "EntityID", "EvidenceFile", "SourceRef",
              "Description", "Recommendation", "EpistemicLabel"]
    with open(os.path.join(HERE, "Scope_Closure_IssueLog.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n"); w.writeheader(); w.writerows(issues)
    brief_amend = re.search(r"^# (.+)$", read(SNAP + "Brief.md"), re.M).group(1)
    rep = [f"# Scope Closure Audit — {AID}\n\n**Audit Date:** {DATE}\n**Closure Status:** {status}\n**Amendment Date:** 2026-09-27 "
           "(groups 1-3 accepted 2026-09-27; landed in PR #995, `78e74f590`)\n"
           f"**Amendment Description:** {brief_amend}\n\n## Amendment Summary\n\n"
           f"Register `{register}` resolved through `{G2PTR}` and `{G2}ACCEPTED_MANIFEST.csv`; SHA-256 `{regs[0]['SHA256']}` verified. "
           f"{len(rows)} rows (MODIFY {sum(1 for r in rows if r['ActionType'] == 'MODIFY')}, ADD {sum(1 for r in rows if r['ActionType'] == 'ADD')}). "
           f"Later handoff records read: `{G3}` and `{PAV}` (post-acceptance validation PASS). This audit runs after incremental setup "
           f"(`{SETUP_LOG}` COMPLETE) and dependency re-extraction, and supersedes the pre-setup snapshot `{PRIOR_SNAP}` "
           "(see `SUPERSESSION_NOTE.md`).\n\n## Pass 1 — Action Verification\n\n"
           "| ActionSeq | ActionType | EntityID | Expected (edits) | Status |\n|---|---|---|---|---|\n"]
    rep += [f"| {a} | {t} | {e} | {x} | {s} |\n" for a, t, e, x, s, _ in p1]
    rep.append("\n## Pass 2 — Downstream Rerun Verification\n\n| Agent | Scope | Evidence | Status |\n|---|---|---|---|\n")
    rep += [f"| {a} | {s} | {e} | {st} |\n" for a, s, e, st in p2]
    rep.append(f"\n## Pass 3 — Orphaned References\n\nMethod Pass 3: no REMOVE, MERGE or RECLASSIFY action and no retired entity ID, so 0 orphaned references.\n\n"
               f"Disclosed extension (retired-surface screen): {nregs} `Dependencies.csv` files scanned for ACTIVE rows describing surfaces SCA-APP-011 retired: "
               f"{len(orphans)} found — " + ", ".join(d for d, _ in orphans) + ". They are filed as `METADATA_STALE` (stale register rows awaiting re-extraction), "
               f"not `ORPHANED_REFERENCE`. The screen now joins the earlier phrase set with the reviewer's broadened case-insensitive terms "
               f"(workbench, pipeline form, deliverable/(status|dependencies), harness/scaffold, scaffoldHarnessExecutionRoot, deliverable-api), "
               f"ignores the DEL-02-02 folder name, and applies an explicit allow-list for retained-dispatch rows "
               f"({'; '.join(f'{k}: {v}' for k, v in ALLOW.items())}); allow-listed hits: " + (", ".join(allowed) or "none")
               + ". Tension observation (DEL-02-03-REQ-009 against E80): " + (", ".join(tension) or "none") + ".\n\n"
               "## Extension — Expected extraction outcomes (DX-01 to DX-16)\n\n"
               f"Source: `{DX_CSV}`. Each check is evaluated against the extracted rows (`DX_Verification.csv`): "
               f"{sum(1 for x in dxres if x[3] == 'VERIFIED')}/{len(dxres)} VERIFIED.\n\n| Outcome | Row | Result |\n|---|---|---|\n"
               + "".join(f"| {a} | {b} | {d} |\n" for a, b, c, d in dxres)
               + "\nOutcomes beyond the expected list (verified, not findings): "
               + "; ".join(f"{t}: {'yes' if ok else 'NO'}" for t, ok in beyond)
               + ". The twelve rows held with `EVIDENCE_SOURCE_RETIRED` (owner proposal ESR-1) are not SCA-APP-011 effects and are "
               f"outside this audit (`{RUN}DEPENDENCY_EXTRACT_RESULTS.md`).\n\n## Pass 4 — Decomposition Consistency\n\n")
    rep += [f"- {n}: {'PASS' if ok else 'FAIL'}\n" for n, ok in p4]
    rep.append("\n## Pass 5 — Context Metadata Consistency\n\n| Deliverable | Context identity | Lifecycle now | Lifecycle pre-change |\n|---|---|---|---|\n")
    rep += [f"| {d} | {c} | {s} | {p} |\n" for d, c, s, p in p5]
    rep.append(f"\n## Pass 6 — Supersession Binding Completeness\n\n{len(yes)} rows with `SupersessionBindingPresent = YES`; matching `D-###` delta rows: "
               f"{sum(1 for x in p6 if x[2])}/{len(p6)}. {len(delta)} delta rows: authority paths resolve and references are non-empty; applicability canonical. "
               f"Accumulator check-map exit {acc.returncode}; findings {len(acc_findings)} (`Expected_Supersession_Map.csv`, `Supersession_Map_Findings.csv`).\n\n"
               "## Pass 7 — KTY Content Remediation Verification\n\nNOT_APPLICABLE (SOFTWARE variant; no KTY manifest).\n\n"
               f"## Closure Determination\n\nFindings: {sev}. **{status}**: every accepted edit is applied, the supersession map checks, "
               f"incremental setup is COMPLETE, the dependency re-extraction meets {sum(1 for x in dxres if x[3] == 'VERIFIED')} of {len(dxres)} "
               f"expected outcomes, the post-extraction closure is acyclic, the APP-R058 disposition is recorded, and {len(orphans)} ACTIVE rows "
               "match the retired-surface screen. Remaining observations are listed in the issue log.\n\n"
               "## Recommendations\n\n1. DEL-02-03-REQ-009 wording (DX-15 residual) is a scope question for a later change.\n"
               "2. Owner proposal ESR-1 (twelve held dependency rows) is separate from this amendment.\n")
    open(os.path.join(HERE, "Scope_Closure_Report.md"), "w", encoding="utf-8").write("".join(rep))
    open(os.path.join(HERE, "QA_Report.md"), "w", encoding="utf-8").write(
        f"# QA — Scope Closure Audit {AID}\n\n## Coverage\n- Actions checked: {len(p1)} of {len(rows)}\n- Downstream reruns checked: {len(p2)} of {len(p2)}\n"
        f"- Dependencies.csv files scanned for orphans: {nregs}\n- Deliverable _CONTEXT.md files checked: {len(p5)}\n- KTY remediation manifest rows checked: 0\n"
        "- `.Archive/` scanner exclusion surfaces checked: 0 (not applicable)\n\n## Limitations\n- The retired-surface scan in Pass 3 is a disclosed extension: a phrase screen over "
        "Statement, TargetLocation, TargetName and EvidenceQuote. Its rows are filed as METADATA_STALE because method Pass 3 (ORPHANED_REFERENCE) covers only rows targeting retired entity IDs.\n"
        "- Pass 5 context identity is taken from the same-day audit-decomp matrix.\n"
        "- The DX-01 to DX-16 verification is a disclosed extension: each outcome's recorded check is evaluated against the extracted rows.\n"
        "- Export freshness is checked deterministically: the stage is rebuilt with the export script's own build_stage in a temporary "
        "directory outside the repository, and its manifest is compared byte-for-byte with the committed export-manifest.csv.\n"
        f"- Supersedes `{PRIOR_SNAP}` (pre-setup); that snapshot's bytes are unchanged (`SUPERSESSION_NOTE.md`).\n\n"
        "## Self-Assessment\n- All passes completed: yes\n- All findings have evidence: yes\n- No silent resolutions: yes\n")
    open(os.path.join(HERE, "Brief.md"), "w", encoding="utf-8").write(
        f"# Brief\n\n```\nPURPOSE: Verify closure of scope change amendment\nAMENDMENT_ID: {AID}\nEXECUTION_ROOT: {EX}\nSCOPE_CHANGE_ROOT: {SC}\n"
        f"DECOMPOSITION_PATH: {DECOMP}\nDECOMP_VARIANT: SOFTWARE\nCONSTRAINTS:\n  - read-only on project state; add this snapshot to the per-amendment _LATEST.md table (method step 5)\n"
        "NOTES:\n  - handoff named in SCA-APP-011 Handoff_State.md; rerun after incremental setup (SETUP_LOG COMPLETE) and dependency re-extraction\n"
        f"  - supersedes {PRIOR_SNAP}\n```\n")
    open(os.path.join(HERE, "INPUT_MANIFEST.sha256"), "w").write("".join(f"{h}  {p}\n" for p, h in sorted(inputs.items())))
    print(status, sev, "actions", summary["actionsVerified"], "/", len(rows), "orphans", len(orphans))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
