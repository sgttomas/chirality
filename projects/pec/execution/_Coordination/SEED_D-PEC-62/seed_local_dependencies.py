#!/usr/bin/env python3
"""D-PEC-62 §3.2 deliverable-local dependency-register seeder.

Deterministic one-time DAG materialization from the owner-accepted exhibit
(inputs manifest: edges_v02.csv + constraints.csv in this folder). Writes
per-deliverable Dependencies.csv (v3.1) and _DEPENDENCIES.md. Outside the
dependency-extract lifecycle by packet ruling; later refreshes use
TASK + dependency-extract.
"""
import csv, re, sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
EXEC = REPO / "projects/pec/execution"
DECOMP = EXEC / "_Decomposition"
SEED_DATE = "2026-07-25"
PLAN = "execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md"

V31 = ["RegisterSchemaVersion","DependencyID","FromPackageID","FromDeliverableID",
       "FromDeliverableName","DependencyClass","AnchorType","Direction",
       "DependencyType","TargetType","TargetPackageID","TargetDeliverableID",
       "TargetRefID","TargetName","TargetLocation","Statement",
       "EvidenceFile","SourceRef","EvidenceQuote","Explicitness",
       "RequiredMaturity","ProposedMaturity","SatisfactionStatus","Confidence",
       "Origin","FirstSeen","LastSeen","Status","Notes"]

STANDING = {"DEL-01-05","DEL-03-04","DEL-10-02","DEL-10-03","DEL-10-10"}
ROOTS_NOTE = "no upstream predecessors (root node)"

def sanitize(name):
    return re.sub(r"_+", "_", re.sub(r"[^A-Za-z0-9]", "_", name)).strip("_")

def stratum_map(stratum, flag):
    if stratum == "DECLARED":
        return "EXPLICIT", "DECLARED", "HIGH"
    if stratum == "DERIVED":
        return "EXPLICIT", "EXTRACTED", "MEDIUM"
    conf = "LOW" if "LOW_CONFIDENCE" in (flag or "") else "MEDIUM"
    return "IMPLICIT", "EXTRACTED", conf

def main():
    with open(DECOMP / "Deliverables.csv", newline="") as f:
        dels = {r["DeliverableID"]: r for r in csv.DictReader(f)}
    with open(HERE / "edges_v02.csv", newline="") as f:
        edges = list(csv.DictReader(f))
    with open(HERE / "constraints.csv", newline="") as f:
        constraints = list(csv.DictReader(f))

    folders = {}
    for ddir in EXEC.glob("PKG-*/1_Working/DEL-*"):
        folders[ddir.name.split("_")[0]] = ddir
    missing = set(dels) - set(folders)
    if missing:
        sys.exit(f"FAIL: no folder for {sorted(missing)}")

    incoming = defaultdict(list); outgoing = defaultdict(list)
    for e in edges:
        incoming[e["SuccessorID"]].append(e)
        outgoing[e["PredecessorID"]].append(e)

    pkg_names = {r["PackageID"]: None for r in dels.values()}
    # Package display names via folder labels
    pkg_dirs = {p.name.split("_")[0]: p.name for p in EXEC.glob("PKG-*")}

    for del_id, d in dels.items():
        ddir = folders[del_id]
        pp, ll = del_id.split("-")[1], del_id.split("-")[2]
        rows, n = [], 0
        def base(): return {k: "" for k in V31}

        # ANCHOR: IMPLEMENTS_NODE -> parent package
        n += 1; r = base()
        r.update(RegisterSchemaVersion="v3.1", DependencyID=f"DEP-{pp}-{ll}-{n:03d}",
                 FromPackageID=d["PackageID"], FromDeliverableID=del_id,
                 FromDeliverableName=d["Name"], DependencyClass="ANCHOR",
                 AnchorType="IMPLEMENTS_NODE", Direction="UPSTREAM",
                 DependencyType="OTHER", TargetType="PACKAGE",
                 TargetPackageID=d["PackageID"], TargetRefID=d["PackageID"],
                 TargetName=pkg_dirs.get(d["PackageID"], d["PackageID"]),
                 TargetLocation="execution/_Decomposition/SOFTWARE_DECOMP.md",
                 Statement=f"{del_id} is package-local to {d['PackageID']}.",
                 EvidenceFile="execution/_Decomposition/Deliverables.csv",
                 SourceRef=f"Deliverables.csv row {del_id}",
                 EvidenceQuote=f"PackageID {d['PackageID']}", Explicitness="EXPLICIT",
                 RequiredMaturity="NOT_APPLICABLE", ProposedMaturity="TBD",
                 SatisfactionStatus="SATISFIED", Confidence="HIGH", Origin="DECLARED",
                 FirstSeen=SEED_DATE, LastSeen=SEED_DATE, Status="ACTIVE",
                 Notes="Tree anchor seeded under D-PEC-62")
        rows.append(r)

        # ANCHOR: TRACES_TO_REQUIREMENT per covered scope item
        for sow in filter(None, (s.strip() for s in d["CoversScopeItems"].split(";"))):
            n += 1; r = base()
            r.update(RegisterSchemaVersion="v3.1", DependencyID=f"DEP-{pp}-{ll}-{n:03d}",
                     FromPackageID=d["PackageID"], FromDeliverableID=del_id,
                     FromDeliverableName=d["Name"], DependencyClass="ANCHOR",
                     AnchorType="TRACES_TO_REQUIREMENT", Direction="UPSTREAM",
                     DependencyType="OTHER", TargetType="REQUIREMENT",
                     TargetRefID=sow, TargetName=sow,
                     TargetLocation="execution/_Decomposition/ScopeLedger.csv",
                     Statement=f"{del_id} covers scope item {sow}.",
                     EvidenceFile="execution/_Decomposition/ScopeLedger.csv",
                     SourceRef=f"ScopeLedger.csv row {sow}",
                     EvidenceQuote=f"DeliverableIDs include {del_id}",
                     Explicitness="EXPLICIT", RequiredMaturity="NOT_APPLICABLE",
                     ProposedMaturity="TBD", SatisfactionStatus="SATISFIED",
                     Confidence="HIGH", Origin="DECLARED", FirstSeen=SEED_DATE,
                     LastSeen=SEED_DATE, Status="ACTIVE",
                     Notes="Tree anchor seeded under D-PEC-62")
            rows.append(r)

        # EXECUTION: one row per incoming accepted edge
        for e in sorted(incoming[del_id], key=lambda x: x["EdgeID"]):
            pred = dels[e["PredecessorID"]]
            pred_dir = folders[e["PredecessorID"]]
            expl, origin, conf = stratum_map(e["Stratum"], e["Flag"])
            cite = e["BasisCitation"].strip()
            n += 1; r = base()
            r.update(RegisterSchemaVersion="v3.1", DependencyID=f"DEP-{pp}-{ll}-{n:03d}",
                     FromPackageID=d["PackageID"], FromDeliverableID=del_id,
                     FromDeliverableName=d["Name"], DependencyClass="EXECUTION",
                     AnchorType="NOT_APPLICABLE", Direction="UPSTREAM",
                     DependencyType="PREREQUISITE", TargetType="DELIVERABLE",
                     TargetPackageID=pred["PackageID"],
                     TargetDeliverableID=e["PredecessorID"], TargetRefID=e["PredecessorID"],
                     TargetName=pred["Name"],
                     TargetLocation=str(pred_dir.relative_to(REPO / "projects/pec")),
                     Statement=e["Rationale"], EvidenceFile=PLAN,
                     SourceRef=(cite if cite else "location TBD"),
                     EvidenceQuote=cite, Explicitness=expl,
                     RequiredMaturity="INITIALIZED", ProposedMaturity="TBD",
                     SatisfactionStatus="PENDING", Confidence=conf, Origin=origin,
                     FirstSeen=SEED_DATE, LastSeen=SEED_DATE, Status="ACTIVE",
                     Notes=f"{e['Stratum']}; Flag={e['Flag'] or 'none'}; EdgeID={e['EdgeID']}")
            rows.append(r)

        with open(ddir / "Dependencies.csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=V31)
            w.writeheader(); w.writerows(rows)

        # _DEPENDENCIES.md human-readable view.
        # Constraint applicability (closure-refuter F3 fix): register-wide
        # rows apply everywhere; C-03's set-described parties resolve to
        # DEL-01-01 plus every PKG-03/04/05 member; others match by ID.
        def applies(c):
            if c["ConstraintID"] in ("C-04", "C-10"):
                return True
            if c["ConstraintID"] == "C-03":
                return del_id == "DEL-01-01" or d["PackageID"] in ("PKG-03", "PKG-04", "PKG-05")
            return del_id in c["Parties"]
        my_constraints = [c for c in constraints if applies(c)]
        lines = [f"# _DEPENDENCIES — {del_id}", "",
                 f"Seeded deterministically under `D-PEC-62` ({SEED_DATE}) from the",
                 f"owner-accepted DAG exhibit (`{PLAN}` §4.1). `Dependencies.csv` (v3.1)",
                 "is the structured register; this file is the human-readable view.",
                 "Register storage is deliverable-local by owner ruling (no central register).", ""]
        ins = sorted(incoming[del_id], key=lambda x: x["EdgeID"])
        if ins:
            lines += ["## Upstream (this deliverable depends on)", "",
                      "| Predecessor | Stratum | Kind | Flag | EdgeID |", "|---|---|---|---|---|"]
            lines += [f"| {e['PredecessorID']} ({dels[e['PredecessorID']]['Name']}) | {e['Stratum']} | {e['EdgeKind']} | {e['Flag'] or ''} | {e['EdgeID']} |" for e in ins]
        else:
            lines += [f"## Upstream", "", f"**{ROOTS_NOTE}** — expected and valid (D-PEC-62 §3.2)."]
        outs = sorted(outgoing[del_id], key=lambda x: x["EdgeID"])
        if outs:
            lines += ["", "## Downstream (informational; consumers of this deliverable)", ""]
            lines += [f"- {e['SuccessorID']} ({dels[e['SuccessorID']]['Name']}) — {e['EdgeKind']} [{e['EdgeID']}]" for e in outs]
        if del_id in STANDING:
            lines += ["", "## Standing obligation (constraint C-08)", "",
                      "This deliverable is a STANDING node: it gates releases, not successors,",
                      "and is excluded from one-shot COMPLETE/UNBLOCKED arithmetic (owner-confirmed at D-PEC-62 ruling)."]
        if my_constraints:
            lines += ["", "## Non-gating constraints and register-wide rules", ""]
            lines += [f"- **{c['ConstraintID']} ({c['Kind']})** — {c['Statement']}" for c in my_constraints]
        lines += ["", "## Blocker semantics", "",
                  "Mode FULL_GRAPH; RequiredMaturity `INITIALIZED` (owner-ruled Phase 1.3).",
                  "Blocker output is advisory visibility only — never work assignment.", ""]
        (ddir / "_DEPENDENCIES.md").write_text("\n".join(lines))

    print(f"OK: seeded {len(dels)} Dependencies.csv + _DEPENDENCIES.md")

if __name__ == "__main__":
    main()
