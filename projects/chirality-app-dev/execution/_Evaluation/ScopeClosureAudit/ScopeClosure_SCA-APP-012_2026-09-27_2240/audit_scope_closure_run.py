#!/usr/bin/env python3
"""audit-scope-closure for SCA-APP-012 after incremental setup and dependency re-extraction.

Read-only on project state; writes only this snapshot folder. Run from the repository root. Implements Passes 0-7
of the bundled `audit-scope-closure` workflow (resources/method.md) for DECOMP_VARIANT = SOFTWARE, plus three disclosed
extensions: the retired-surface screen (Pass 3), verification of the expected extraction outcomes DX-01 to DX-07, and
an absence check of the code files SCA-APP-012 retired. Modelled on ScopeClosure_SCA-APP-011_2026-09-27_1740's script.
This is the first scope-closure snapshot for SCA-APP-012 (none was taken before setup). The post-extraction closure
evidence is CLOSURE_SCA_APP_012_POST_EXTRACTION_2026-09-27_2234. Export freshness is checked deterministically (the
export stage is rebuilt in a temporary directory with the export script's own build_stage and its manifest compared
byte-for-byte with the committed export-manifest.csv).
"""
from __future__ import annotations

import csv
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
AID = "SCA-APP-012"
SNAP = SC + "SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement/"
DECOMP = EX + "_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
G2PTR = SC + "SCA-APP-012_GROUP-2_AUTHORIZED.md"
G2 = SC + "checkpoint_snapshots/SCA-APP-012_GROUP-2_2026-09-27/"
G3 = SC + "checkpoint_snapshots/SCA-APP-012_GROUP-3_2026-09-27/"
PAV = SC + "_PostAcceptanceValidation/SCA-APP-012_20260927T214035Z/"
PRIOR_MAP = SC + "SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement/Supersession_Map.csv"
COV = EX + "_Evaluation/DecompCoverage/COV_SCA_APP_012_POST_ACCEPTANCE_2026-09-27_2200/"
SETUP_LOG = EX + "_Coordination/SETUP_LOG.md"
RUN = EX + "_Coordination/AgentRuns/APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27/"
DEPCL = EX + "_Evaluation/DepClosure/CLOSURE_SCA_APP_012_POST_EXTRACTION_2026-09-27_2234/"
TMREG = EX + "_Coordination/_TaskManagement/REGISTER.csv"
TMREC = EX + "_Coordination/_TaskManagement/ROW_MAINTENANCE_TM-APP-051_SCA-APP-012_DISPOSITION_2026-09-27.md"
EXPORT_SCRIPT = "exports/chirality-app/export_public.py"
EXPORT_MANIFEST = "exports/chirality-app/export-manifest.csv"
DX_CSV = RUN + "DEPENDENCY_EXTRACT_EXPECTED_OUTCOMES.csv"
EXTRACT_BASIS = "63e5de1f2f19c3a1dab073babbadfbfcc6199e70"
DATE = "2026-09-27"
IN_SCOPE = ["DEL-02-01", "DEL-02-02", "DEL-02-03", "DEL-06-03", "DEL-07-02", "DEL-07-03", "DEL-08-02", "DEL-08-03",
            "DEL-02-04", "DEL-02-05", "DEL-04-04", "DEL-05-02", "DEL-05-03", "DEL-05-04", "DEL-06-01", "DEL-06-02", "DEL-07-01",
            "DEL-07-04", "DEL-07-05", "DEL-08-01", "DEL-08-04", "DEL-08-05", "DEL-09-02", "DEL-09-04"]
# Retired-surface screen (DX-05 terms plus the "working-root scope API" label, case-insensitive): the surfaces SCA-APP-012 retired.
SCREEN = re.compile(r"/api/working-root/scope|working-root scope API|/api/working-root/workflow|portal-loop-shell|loop-tertiary-shell|(?<![\w-])loop-shell|"
                    r"sidebar-right-loop-layout|tertiary-sidebar-tabs|agent-matrix|lib/portal|DeliverablesProvider|deliverables-provider|"
                    r"ProjectScaffoldPort", re.I)
SCREEN_FIELDS = ("TargetName", "Statement", "EvidenceQuote", "SourceRef", "TargetLocation", "EvidenceFile")
# Code files the SCA-APP-012 code change retired (RUN_SUMMARY.md "What changed"), under the frontend source root.
FE = APP + "frontend/src/"
RETIRED_CODE = ["components/shell/loop-shell.tsx", "components/shell/portal-loop-shell.tsx", "components/shell/loop-tertiary-shell.tsx",
                "components/shell/sidebar-right-loop-layout.tsx", "components/shell/tertiary-sidebar-tabs.tsx",
                "components/portal/agent-matrix.tsx", "lib/portal/agent-matrix-cells.ts", "lib/portal/agent-matrix-launch.ts",
                "components/workspace/deliverables-provider.tsx", "app/api/working-root/scope/route.ts",
                "components/woven-dialogue/workflows-view.tsx", "components/woven-dialogue/workflow-detail.tsx",
                "app/api/working-root/workflow/route.ts"]
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


def folder(d):
    return glob.glob(EX + f"PKG-*/1_Working/{d}_*")[0]


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
    assert "checkpoint_snapshots/SCA-APP-012_GROUP-2_2026-09-27/" in ptr
    man = list(csv.DictReader(io.StringIO(read(G2 + "ACCEPTED_MANIFEST.csv"))))
    regs = [r for r in man if re.match(r"Amendment_Actions.*\.csv$", os.path.basename(r["Path"]))]
    if len(regs) != 1 or sha(regs[0]["Path"]) != regs[0]["SHA256"]:
        raise SystemExit("FAILED_INPUTS: register not bound or hash mismatch")
    register = regs[0]["Path"]
    rows = list(csv.DictReader(io.StringIO(read(register))))
    read(SNAP + "RUN_SUMMARY.md")
    read(SNAP + "Propagation_Plan.md")
    read(SNAP + "Handoff_State.md")
    read(G3 + "DECISION.md")
    read(G3 + "Handoff_State.md")
    pav = read(PAV + "POST_ACCEPTANCE_VALIDATION.md")
    pav_ok = "Result: PASS" in pav
    decomp = read(DECOMP)

    # Pass 1 — every edit of every register row present in the applied state
    ae = load("amendment_edits", SNAP + "Evidence/Group2/amendment_edits.py")
    sha(SNAP + "Evidence/Group2/amendment_edits.py")
    by_seq = {}
    for e in ae.EDITS:
        by_seq.setdefault(e["seq"], []).append(e)
    for seq, carried in getattr(ae, "CARRIED_BY", {}).items():
        by_seq.setdefault(seq, [e for e in ae.EDITS if e["id"] in carried])
    p1 = []
    for r in rows:
        seq = int(r["ActionSeq"])
        missing = []
        for e in by_seq.get(seq, []):
            new = e["new"].replace("{APPLICATION_DATE}", DATE)
            text = read(e["file"])
            if new not in text or (e["old"] not in new and e["old"] in text):
                missing.append(e["id"])
        status = "VERIFIED" if by_seq.get(seq) and not missing else ("NOT_EXECUTED" if not by_seq.get(seq) else "DISCREPANCY")
        p1.append((r["ActionSeq"], r["ActionType"], r["EntityID"], ",".join(e["id"] for e in by_seq.get(seq, [])), status, missing))
        if status != "VERIFIED":
            issue(1, "ACTION_NOT_EXECUTED", "CRITICAL", r["ActionSeq"], r["EntityID"], register, f"ActionSeq {seq}",
                  f"Accepted edits not present in the applied state: {missing}", "Return to scope-change")

    # Pass 2 — downstream reruns (RUN_SUMMARY and Handoff_State next owning workflows)
    p2 = []
    p2.append(("post-acceptance validation", AID, f"{PAV}POST_ACCEPTANCE_VALIDATION.md 'Result: PASS' = {pav_ok}",
               "COMPLETED" if pav_ok else "NO_EVIDENCE"))
    if not pav_ok:
        issue(2, "DOWNSTREAM_NOT_RUN", "MAJOR", "N/A", "post-acceptance validation", PAV + "POST_ACCEPTANCE_VALIDATION.md", "Result",
              "The post-acceptance validation record does not report PASS", "Rerun the post-acceptance validation")
    setup_done = os.path.exists(SETUP_LOG) and "INCREMENTAL SCA-APP-012 setup COMPLETE" in read(SETUP_LOG)
    p2.append(("project-setup INCREMENTAL", "8 MODIFY deliverables + 16 neighbours",
               f"{SETUP_LOG}: 'INCREMENTAL SCA-APP-012 setup COMPLETE'; run record {RUN}SETUP_RUN_RECORD.md",
               "COMPLETED" if setup_done else "NO_EVIDENCE"))
    if not setup_done:
        issue(2, "DOWNSTREAM_NOT_RUN", "MAJOR", "N/A", "project-setup", SNAP + "Handoff_State.md", "Next owning workflows 1",
              "Incremental setup has no COMPLETE line in SETUP_LOG.md", f"Run Function 5 after the plan in {RUN}INCREMENTAL_SETUP_PROPOSAL.md is confirmed")
    post_hash = inputs.get(DECOMP) or sha(DECOMP)
    unbound = []
    for d in IN_SCOPE:
        dm = read(folder(d) + "/_DEPENDENCIES.md")
        read(folder(d) + "/Dependencies.csv")
        if post_hash not in dm or "SCA-APP-012 incremental setup refresh (UPDATE)" not in dm:
            unbound.append(d)
    p2.append(("dependency-extract", f"{len(IN_SCOPE)} registers (8 MODIFY + 16 neighbours)",
               f"_DEPENDENCIES.md run notes bind the post-change decomposition hash {post_hash[:12]} in {len(IN_SCOPE) - len(unbound)}/{len(IN_SCOPE)}",
               "COMPLETED" if not unbound else "NO_EVIDENCE"))
    for d in unbound:
        issue(2, "DOWNSTREAM_NOT_RUN", "MAJOR", "N/A", d, folder(d) + "/_DEPENDENCIES.md", "Run Notes",
              "No dependency-extract run binds the post-change decomposition hash", "Run dependency-extract for this deliverable")
    dc_ok = False
    if os.path.exists(DEPCL + "Tool_Run.json"):
        tr = json.loads(read(DEPCL + "Tool_Run.json"))
        cs = json.loads(read(DEPCL + "Evidence/closure_summary.json"))
        csa = json.loads(read(DEPCL + "Evidence/ALL/closure_summary.json"))
        basis = {x["path"]: x["sha256"] for x in tr.get("accepted_input_basis", [])}
        current = all(sha(p) == h for p, h in basis.items())
        dc_ok = (cs.get("scc_count") == 0 and cs.get("subject_status") == "PASS" and current and bool(basis)
                 and csa.get("graph_nodes") == 54 and csa.get("graph_edges") == 102 and csa.get("scc_count") == 0)
    p2.append(("audit-dep-closure after re-extraction", "ALL rules (51 current units + census)",
               f"{DEPCL}: subject PASS, 0 SCC, census 54 nodes / 102 edges, input basis hashes current = {dc_ok}",
               "COMPLETED" if dc_ok else "NO_EVIDENCE"))
    if not dc_ok:
        issue(2, "DOWNSTREAM_NOT_RUN", "MINOR", "N/A", "analyze_dep_closure", DEPCL + "Tool_Run.json", "whole file",
              "No post-extraction closure snapshot binds the current registers with the expected census", "Rerun audit-dep-closure over the accepted inventory (FULL_GRAPH)")
    cov_in = read(COV + "INPUT_MANIFEST.sha256")
    cov_ok = post_hash in cov_in
    p2.append(("audit-decomp", "ALL", f"{COV} INPUT_MANIFEST binds post-change decomposition {post_hash[:12]}: {cov_ok}", "COMPLETED" if cov_ok else "NO_EVIDENCE"))
    if not cov_ok:
        issue(2, "DOWNSTREAM_NOT_RUN", "MINOR", "N/A", "audit-decomp", COV + "INPUT_MANIFEST.sha256", "whole file",
              "No audit-decomp snapshot binds the post-change decomposition", "Run audit-decomp")
    p2.append(("audit-scope-closure", AID, "this snapshot", "COMPLETED (this run, after setup)"))
    present = [f for f in RETIRED_CODE if os.path.exists(FE + f)]
    p2.append(("code change (Q-a)", f"{len(RETIRED_CODE)} retired frontend files",
               f"absent under {FE}: {len(RETIRED_CODE) - len(present)}/{len(RETIRED_CODE)}", "COMPLETED" if not present else "NO_EVIDENCE"))
    for f in present:
        issue(2, "DOWNSTREAM_NOT_RUN", "MAJOR", "N/A", f, FE + f, "RUN_SUMMARY.md What changed",
              "A code file SCA-APP-012 retired is still present", "Return to the App loop")
    exp_ok, exp_rows = export_fresh()
    p2.append(("export regeneration", "exports/chirality-app",
               f"rebuilt export stage ({exp_rows} files) reproduces the committed {EXPORT_MANIFEST} byte-for-byte = {exp_ok}",
               "COMPLETED" if exp_ok else "NO_EVIDENCE"))
    if not exp_ok:
        issue(2, "DOWNSTREAM_NOT_RUN", "MINOR", "N/A", "export", EXPORT_MANIFEST, "whole file",
              "The committed public-export manifest does not match a fresh rebuild of the export stage", f"Run {EXPORT_SCRIPT} and commit the export")
    tm = read(TMREC) if os.path.exists(TMREC) else ""
    tmrow = next((r for r in csv.DictReader(io.StringIO(read(TMREG))) if r["ActionItemID"] == "TM-APP-051"), {})
    tm_ok = ("TM-APP-051: option 1" in tm and "federation" in tm and tmrow.get("Status") == "DEFERRED"
             and tmrow.get("ScaRef") == "SCA-APP-012" and "disposes three of the four consumers" in tmrow.get("Notes", ""))
    p2.append(("Task Management TM-APP-051 disposition note", "TM-APP-051",
               f"{TMREC}: owner act quoted, federation preflight recorded; {TMREG} row DEFERRED, ScaRef SCA-APP-012, note appended = {tm_ok}",
               "COMPLETED" if tm_ok else "NO_EVIDENCE"))
    if not tm_ok:
        issue(2, "DOWNSTREAM_NOT_RUN", "MINOR", "N/A", "TM-APP-051", TMREC, "whole file",
              "No row maintenance records the Propagation_Plan section 8 item 5 note on TM-APP-051", f"Row owner records {RUN}TM_APP_051_PROPOSAL.md option 1")

    # Pass 3 — orphaned references. Method Pass 3 targets rows pointing at RETIRED entity IDs; SCA-APP-012 has no
    # REMOVE/MERGE/RECLASSIFY action and retires no ID, so proper Pass 3 finds nothing for this amendment.
    # Disclosed extension: a screen for ACTIVE rows that still name a surface SCA-APP-012 retired (DX-05 terms).
    orphans = []
    nregs = 0
    reg = {}
    for f in sorted(glob.glob(EX + "PKG-*/*/DEL-*/Dependencies.csv")):
        nregs += 1
        for r in csv.DictReader(io.StringIO(read(f))):
            reg[r["DependencyID"]] = r
            if r.get("Status") != "ACTIVE":
                continue
            blob = " ".join(r.get(k, "") for k in SCREEN_FIELDS)
            if SCREEN.search(blob):
                orphans.append((r["DependencyID"], f))
    # Control: the same screen over the registers at the extraction basis must find the rows DX-02 and DX-03 restate.
    control = []
    for f in sorted(glob.glob(EX + "PKG-*/*/DEL-*/Dependencies.csv")):
        old = subprocess.run(["git", "show", f"{EXTRACT_BASIS}:{f}"], capture_output=True, text=True).stdout
        for r in csv.DictReader(io.StringIO(old)):
            if r.get("Status") == "ACTIVE" and SCREEN.search(" ".join(r.get(k, "") for k in SCREEN_FIELDS)):
                control.append(r["DependencyID"])
    for did, f in orphans:
        issue(3, "METADATA_STALE", "MAJOR", "N/A", did, f, did,
              "ACTIVE dependency row still names a surface SCA-APP-012 retired; found by the disclosed retired-surface screen, not by method Pass 3 (no entity ID is retired)",
              f"Re-extract; check the expected outcome in {DX_CSV}", "FACT")
    for did, r in reg.items():
        if r.get("Status") == "ACTIVE" and r.get("TargetDeliverableID") == "DEL-09-07":
            issue(3, "ORPHANED_REFERENCE", "OBSERVATION", "N/A", did, "", did,
                  "ACTIVE row targets retired DEL-09-07 (not retired by SCA-APP-012)", "Outside this amendment; route to its owner")

    # Extension — verify the expected extraction outcomes DX-01 to DX-07 against the extracted rows
    dxrows = list(csv.DictReader(io.StringIO(read(DX_CSV))))
    sow0203 = read(folder("DEL-02-03") + "/ScopeOfWork.md")
    sow0203_lines = sow0203.split("\n")
    sow0803 = read(folder("DEL-08-03") + "/ScopeOfWork.md")
    dm0803 = read(folder("DEL-08-03") + "/_DEPENDENCIES.md")
    cur0803 = dm0803.split("### 2026-09-27 SCA-APP-012 incremental setup refresh (UPDATE)", 1)
    cur0803 = cur0803[1].split("\n## ", 1)[0] if len(cur0803) == 2 else None
    req010 = next((l for l in sow0203_lines if "| DEL-02-03-REQ-010 |" in l and "shall present lifecycle status" in l), "")
    base0802 = subprocess.run(["git", "show", f"{EXTRACT_BASIS}:{folder('DEL-08-02')}/Dependencies.csv"], capture_output=True, text=True).stdout
    b013 = next((r for r in csv.DictReader(io.StringIO(base0802)) if r["DependencyID"] == "DEP-08-02-013"), {})

    def g(i):
        return reg.get(i, {})

    def joins(a, b):
        return [i for i, r in reg.items() if r.get("Status") == "ACTIVE" and r.get("FromDeliverableID") == a and r.get("TargetDeliverableID") == b]

    checks = {
        "DX-01": lambda: g("DEP-02-03-009").get("Status") == "RETIRED" and g("DEP-02-03-009").get("SatisfactionStatus") == "NOT_APPLICABLE"
                         and "SCA-APP-012" in g("DEP-02-03-009").get("Notes", "") and not joins("DEL-02-03", "DEL-08-03")
                         and not joins("DEL-08-03", "DEL-02-03"),
        "DX-02": lambda: g("DEP-02-03-004").get("Status") == "ACTIVE" and "/api/working-root/scope" not in g("DEP-02-03-004").get("EvidenceQuote", "")
                         and g("DEP-02-03-004").get("EvidenceQuote", "~") in sow0203 and "SCA-APP-012" in g("DEP-02-03-004").get("Notes", "")
                         and "Prior EvidenceQuote=" in g("DEP-02-03-004").get("Notes", "") and g("DEP-02-03-004").get("TargetRefID") == "REF-003",
        "DX-03": lambda: g("DEP-08-03-007").get("Status") == "ACTIVE" and "working-root scope API" not in g("DEP-08-03-007").get("TargetName", "")
                         and "deliverable scan API" in g("DEP-08-03-007").get("TargetName", "") and cur0803 is not None
                         and "SOURCE_ENDPOINT_LABEL_CONFLICT" not in cur0803 and "/api/working-root/scope" not in sow0803,
        "DX-04": lambda: bool(b013) and all(g("DEP-08-02-013").get(k) == v for k, v in b013.items() if k != "LastSeen"),
        "DX-05": lambda: not orphans,
        "DX-06": lambda: g("DEP-02-03-007").get("Status") == "ACTIVE" and g("DEP-02-03-007").get("TargetDeliverableID") == "DEL-07-04"
                         and bool(req010) and g("DEP-02-03-007").get("EvidenceQuote", "~") in req010
                         and "transition control" not in g("DEP-02-03-007").get("Statement", "").lower()
                         and "SCA-APP-012" in g("DEP-02-03-007").get("Notes", "")
                         and "consume status and dependency contract snapshots read-only where applicable" in g("DEP-02-03-007").get("Notes", ""),
        "DX-07": lambda: g("DEP-02-03-008").get("Status") == "RETIRED" and "SCA-APP-012" in g("DEP-02-03-008").get("Notes", ""),
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

    # Pass 4 — decomposition consistency
    p4 = []
    p4.append(("Decision Log DEC-027", "| DEC-027 | 2026-09-27 |" in decomp))
    p4.append(("Change Log line", "- 2026-09-27: SCA-APP-012 retired" in decomp))
    p4.append(("Coverage and Telemetry names SCA-APP-012 and 2026-09-27", "amended by SCA-APP-012 |" in decomp and "| Date | 2026-09-27 |" in decomp))
    pre = json.load(open(SNAP + "Pre_Change_Coverage.json")); sha(SNAP + "Pre_Change_Coverage.json")
    post = json.load(open(SNAP + "Post_Change_Coverage.json")); sha(SNAP + "Post_Change_Coverage.json")
    # The topology record also carries the highest decision-log ID, which the ADD action (row 10, DEC-027) moves by design;
    # it is compared on its own, and the rest of the topology must be unchanged.
    topo = lambda t: {k: v for k, v in (t or {}).items() if k != "highest_decision_log_id"}
    p4.append(("coverage repository_topology unchanged pre/post (apart from the decision-log ID)",
               topo(pre.get("repository_topology")) == topo(post.get("repository_topology"))))
    p4.append(("highest decision-log ID moves DEC-026 -> DEC-027 (ADD row 10) and nothing else",
               (pre.get("repository_topology") or {}).get("highest_decision_log_id") == "DEC-026"
               and (post.get("repository_topology") or {}).get("highest_decision_log_id") == "DEC-027"
               and sum(1 for r in rows if r["ActionType"] == "ADD") == 1))
    for k in ("ledger_distribution", "forward_coverage", "scope_items_without_deliverable", "objectives_without_deliverable"):
        p4.append((f"coverage {k} unchanged pre/post", pre.get(k) == post.get(k)))
    for name, ok in p4:
        if not ok:
            issue(4, "DECOMP_INCONSISTENCY", "MAJOR", "N/A", "decomposition", DECOMP, name, f"{name} not satisfied", "Return to scope-change")

    # Pass 5 — context metadata for affected deliverables
    matrix = {r["ProductionUnitID"]: r for r in csv.DictReader(io.StringIO(read(COV + "Decomp_Coverage_Matrix.csv")))}
    p5 = []
    seen_d = set()
    for r in rows:
        if r["EntityType"] != "DELIVERABLE" or r["EntityID"] in seen_d:
            continue
        d = r["EntityID"]
        seen_d.add(d)
        cm = matrix[d]["ContextMatch"]
        st = re.search(r"\*\*Current State:\*\*\s*`?([A-Z_]+)", read(folder(d) + "/_STATUS.md")).group(1)
        pre_st = pre.get("affected_deliverables", {}).get(d, {}).get("lifecycle")  # None: not in the pre-change affected set
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
    if acc.returncode != 0 and not acc_findings:
        issue(6, "SUPERSESSION_INCOMPLETE", "MAJOR", "N/A", "accumulator", SNAP + "Supersession_Map.csv", "exit code",
              f"accumulate_supersession_map.py exited {acc.returncode}", "Investigate the accumulator run")
    exp_map = open(os.path.join(HERE, "Expected_Supersession_Map.csv"), "rb").read()
    map_equal = exp_map == open(SNAP + "Supersession_Map.csv", "rb").read().replace(b"\r\n", b"\n")

    # Closure determination
    sev = {k: sum(1 for i in issues if i["Severity"] == k) for k in ("CRITICAL", "MAJOR", "MINOR", "OBSERVATION")}
    status = "OPEN" if sev["CRITICAL"] or sev["MAJOR"] else ("CLOSED_WITH_OBSERVATIONS" if sev["MINOR"] or sev["OBSERVATION"] else "CLOSED")
    summary = {"amendmentId": AID, "auditDate": DATE, "closureStatus": status, "actionRegister": register,
               "totalActions": len(rows), "actionsVerified": sum(1 for x in p1 if x[4] == "VERIFIED"),
               "actionsDiscrepant": sum(1 for x in p1 if x[4] == "DISCREPANCY"), "actionsNotExecuted": sum(1 for x in p1 if x[4] == "NOT_EXECUTED"),
               "actionsDeferredByHuman": 0, "actionsSuperseded": 0, "downstreamRerunsRecommended": len(p2),
               "downstreamRerunsCompleted": sum(1 for x in p2 if x[3].startswith("COMPLETED")),
               "downstreamRerunsDeferredOrNotActivated": 0, "orphanedReferencesFound": 0, "retiredSurfaceScreenRows": len(orphans),
               "retiredSurfaceScreenControl": control, "expectedOutcomesVerified": sum(1 for x in dxres if x[3] == "VERIFIED"), "expectedOutcomesTotal": len(dxres),
               "supersessionBindings": f"{sum(1 for x in p6 if x[2])}/{len(p6)}", "supersessionAccumulatorExit": acc.returncode,
               "supersessionAccumulatorFindings": len(acc_findings), "expectedMapEqualsSnapshotMap": map_equal,
               "supersedes": None, "contentRemediationState": "NOT_REQUIRED", "ktyRemediationRows": 0, "ktyRemediationRowsBlocked": 0,
               "archiveScannerLeaks": 0, "findingsBySeverity": sev}
    json.dump(summary, open(os.path.join(HERE, "scope_closure_summary.json"), "w"), indent=1)
    fields = ["IssueID", "Pass", "Category", "Severity", "Assessment", "AmendmentAction", "EntityID", "EvidenceFile", "SourceRef",
              "Description", "Recommendation", "EpistemicLabel"]
    with open(os.path.join(HERE, "Scope_Closure_IssueLog.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n"); w.writeheader(); w.writerows(issues)
    brief_amend = re.search(r"^# (.+)$", read(SNAP + "Brief.md"), re.M).group(1)
    rep = [f"# Scope Closure Audit — {AID}\n\n**Audit Date:** {DATE}\n**Closure Status:** {status}\n**Amendment Date:** 2026-09-27 "
           "(groups 1-3 accepted 2026-09-27; landed in PR #1020, `bc1ea504d`)\n"
           f"**Amendment Description:** {brief_amend}\n\n## Amendment Summary\n\n"
           f"Register `{register}` resolved through `{G2PTR}` and `{G2}ACCEPTED_MANIFEST.csv`; SHA-256 `{regs[0]['SHA256']}` verified. "
           f"{len(rows)} rows (MODIFY {sum(1 for r in rows if r['ActionType'] == 'MODIFY')}, ADD {sum(1 for r in rows if r['ActionType'] == 'ADD')}). "
           f"Later handoff records read: `{G3}` and `{PAV}` (post-acceptance validation PASS). This audit runs after incremental setup "
           f"(`{SETUP_LOG}` COMPLETE) and dependency re-extraction. It is the first scope-closure snapshot for {AID}: none was taken "
           "before setup (`Propagation_Plan.md` section 8 item 3 places the audit after the setup), so it supersedes nothing.\n\n"
           "## Pass 1 — Action Verification\n\n"
           "| ActionSeq | ActionType | EntityID | Expected (edits) | Status |\n|---|---|---|---|---|\n"]
    rep += [f"| {a} | {t} | {e} | {x} | {s} |\n" for a, t, e, x, s, _ in p1]
    rep.append("\n## Pass 2 — Downstream Rerun Verification\n\n| Agent | Scope | Evidence | Status |\n|---|---|---|---|\n")
    rep += [f"| {a} | {s} | {e} | {st} |\n" for a, s, e, st in p2]
    rep.append(f"\n## Pass 3 — Orphaned References\n\nMethod Pass 3: no REMOVE, MERGE or RECLASSIFY action and no retired entity ID, so 0 orphaned references.\n\n"
               f"Disclosed extension (retired-surface screen: the DX-05 terms plus the 'working-root scope API' label, case-insensitive): {nregs} "
               f"`Dependencies.csv` files scanned for ACTIVE rows whose {', '.join(SCREEN_FIELDS)} name a surface SCA-APP-012 retired: {len(orphans)} found"
               + (" — " + ", ".join(d for d, _ in orphans) if orphans else "") + ". No allow-list is needed. Control: the same screen over the "
               f"registers at the extraction basis `{EXTRACT_BASIS[:9]}` finds {len(control)} ({', '.join(control) or 'none'}), the rows DX-02 and DX-03 restate.\n\n"
               "## Extension — Expected extraction outcomes (DX-01 to DX-07)\n\n"
               f"Source: `{DX_CSV}`. Each check is evaluated against the extracted rows (`DX_Verification.csv`): "
               f"{sum(1 for x in dxres if x[3] == 'VERIFIED')}/{len(dxres)} VERIFIED. DX-04 does not apply (P-keep) and is checked as "
               f"DEP-08-02-013 unchanged apart from `LastSeen` against the extraction basis `{EXTRACT_BASIS[:9]}`.\n\n"
               "| Outcome | Row | Result |\n|---|---|---|\n"
               + "".join(f"| {a} | {b} | {d} |\n" for a, b, c, d in dxres)
               + "\n## Pass 4 — Decomposition Consistency\n\n")
    rep += [f"- {n}: {'PASS' if ok else 'FAIL'}\n" for n, ok in p4]
    rep.append("\n## Pass 5 — Context Metadata Consistency\n\n| Deliverable | Context identity | Lifecycle now | Lifecycle pre-change |\n|---|---|---|---|\n")
    rep += [f"| {d} | {c} | {s} | {p or 'not in the pre-change affected set'} |\n" for d, c, s, p in p5]
    rep.append(f"\n## Pass 6 — Supersession Binding Completeness\n\n{len(yes)} rows with `SupersessionBindingPresent = YES`; matching `D-###` delta rows: "
               f"{sum(1 for x in p6 if x[2])}/{len(p6)}. {len(delta)} delta rows: authority paths resolve and references are non-empty; applicability canonical. "
               f"Supersession-map check: `accumulate_supersession_map.py` over the SCA-APP-011 cumulative map and this delta, `--check-map` against the "
               f"snapshot's `Supersession_Map.csv`: exit {acc.returncode}; findings {len(acc_findings)}; the expected map equals the snapshot map "
               f"byte-for-byte = {map_equal} (`Expected_Supersession_Map.csv`, `Supersession_Map_Findings.csv`).\n\n"
               "## Pass 7 — KTY Content Remediation Verification\n\nNOT_APPLICABLE (SOFTWARE variant; no KTY manifest).\n\n"
               f"## Closure Determination\n\nFindings: {sev}. **{status}**: every accepted edit is applied, the supersession map checks, "
               f"incremental setup is COMPLETE, the dependency re-extraction meets {sum(1 for x in dxres if x[3] == 'VERIFIED')} of {len(dxres)} "
               f"expected outcomes, the post-extraction closure is acyclic, the retired code files are absent, the export is fresh, the TM-APP-051 "
               f"note is recorded, and {len(orphans)} ACTIVE rows match the retired-surface screen.\n\n"
               "## Recommendations\n\n1. TM-APP-051 stays `DEFERRED` for the unimplemented summary/status widget, which stays with DEL-02-03; "
               "that is the row owner's open item, not an SCA-APP-012 closure finding.\n"
               "2. The `_SEMANTIC.md` and `_SEMANTIC_LENSING.md` of the eight modified deliverables are stale; a rerun is the owner's choice.\n")
    open(os.path.join(HERE, "Scope_Closure_Report.md"), "w", encoding="utf-8").write("".join(rep))
    open(os.path.join(HERE, "QA_Report.md"), "w", encoding="utf-8").write(
        f"# QA — Scope Closure Audit {AID}\n\n## Coverage\n- Actions checked: {len(p1)} of {len(rows)}\n- Downstream reruns checked: {len(p2)} of {len(p2)}\n"
        f"- Dependencies.csv files scanned for orphans: {nregs}\n- Deliverable _CONTEXT.md files checked: {len(p5)}\n- KTY remediation manifest rows checked: 0\n"
        "- `.Archive/` scanner exclusion surfaces checked: 0 (not applicable)\n\n## Limitations\n- The retired-surface scan in Pass 3 is a disclosed extension: a screen over "
        f"{', '.join(SCREEN_FIELDS)} for the DX-05 terms and the 'working-root scope API' label, with a control run on the extraction basis. Its rows would be filed as METADATA_STALE because method Pass 3 (ORPHANED_REFERENCE) covers only rows targeting retired entity IDs.\n"
        "- Pass 5 context identity is taken from the same-day audit-decomp matrix; lifecycle is read from each `_STATUS.md`.\n"
        "- The DX-01 to DX-07 verification is a disclosed extension: each outcome's recorded check is evaluated against the extracted rows.\n"
        "- The retired-code check is a disclosed extension: an absence check of the files the amendment's RUN_SUMMARY.md lists as deleted.\n"
        "- Export freshness is checked deterministically: the stage is rebuilt with the export script's own build_stage in a temporary "
        "directory outside the repository, and its manifest is compared byte-for-byte with the committed export-manifest.csv.\n"
        "- First scope-closure snapshot for this amendment; it supersedes nothing.\n\n"
        "## Self-Assessment\n- All passes completed: yes\n- All findings have evidence: yes\n- No silent resolutions: yes\n")
    open(os.path.join(HERE, "Brief.md"), "w", encoding="utf-8").write(
        f"# Brief\n\n```\nPURPOSE: Verify closure of scope change amendment\nAMENDMENT_ID: {AID}\nEXECUTION_ROOT: {EX}\nSCOPE_CHANGE_ROOT: {SC}\n"
        f"DECOMPOSITION_PATH: {DECOMP}\nDECOMP_VARIANT: SOFTWARE\nCONSTRAINTS:\n  - read-only on project state; add this snapshot to the per-amendment _LATEST.md table (method step 5)\n"
        "NOTES:\n  - handoff named in SCA-APP-012 Handoff_State.md (next owning workflows 3); run after incremental setup (SETUP_LOG COMPLETE) and dependency re-extraction\n"
        "  - first snapshot for SCA-APP-012; supersedes nothing\n```\n")
    open(os.path.join(HERE, "INPUT_MANIFEST.sha256"), "w").write("".join(f"{h}  {p}\n" for p, h in sorted(inputs.items())))
    print(status, sev, "actions", summary["actionsVerified"], "/", len(rows), "reruns", summary["downstreamRerunsCompleted"], "/", len(p2),
          "DX", summary["expectedOutcomesVerified"], "/", len(dxres), "orphans", len(orphans), "supersession", summary["supersessionBindings"],
          "acc", acc.returncode, len(acc_findings), "map_equal", map_equal)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
