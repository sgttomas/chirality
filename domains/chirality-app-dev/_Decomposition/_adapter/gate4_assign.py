#!/usr/bin/env python3
"""Gate 4 Knowledge-Type / Subject assignment for chirality-app-dev.

Knowledge-kind KTY axis (operator decision): within each category the Knowledge
Types are the knowledge KINDS the authors actually used. For the 11 PKG
deliverable categories CAT-001..011 these are the four document kinds
Datasheet->Reference, Specification, Guidance, Procedure (1:1 with the persona
canonical schemas). For the 5 cross-cutting categories CAT-012..016 they are the
real content kinds of their source docs (see CROSS_KTY below). Subjects are
per-deliverable (deliverable categories) or per-source-doc / per-frontend-module
(cross-cutting). Assignment is deterministic SOURCE_ROUTING: doc-kind and
deliverable both live in each atom's @repo SourceRef path; cross-cutting routes by
SourceDoc.

This embeds the hand-authored KTY taxonomy (the persona judgment) and MATERIALIZES
it into Knowledge_Type_Register.csv + Knowledge_Subject_Register.csv for review;
it is the app-dev pack-local analogue of the self-domain-specific
tools/decomp/propose_gate4_kty.py (which is NOT reusable).

Usage:  python3 _adapter/gate4_assign.py
Run with cwd = MONOREPO_ROOT (chirality/). Prints a JSON summary. Lossless: the
Gate-3 columns (incl. UnitStatement/ContentHash/CategoryID) are copied unchanged;
Gate-4 columns are appended; no atom splits.
"""
from __future__ import annotations
import csv, json, re, sys
from pathlib import Path
from collections import defaultdict, Counter

MONO = Path.cwd()
DEC = MONO / "domains/chirality-app-dev/_Decomposition"
G3_LEDGER = DEC / "Domain_Ledger_Gate3_Category_Draft.csv"
CAT_REG = DEC / "Category_Register.csv"

DELIV_CATS = {f"CAT-{i:03d}": i for i in range(1, 12)}   # CAT-001..011 -> CC index

# Doc-kind KTYs for every deliverable category (TT order fixed).
DOCKIND_KTY = [
    ("01", "Datasheet", "Datasheet (Reference)", "Reference",
     "Reference-grade datasheet facts, parameters, and definitions for the deliverables in this package."),
    ("02", "Specification", "Specification", "Specification",
     "Normative specifications and requirements for the deliverables in this package."),
    ("03", "Guidance", "Guidance", "Guidance / Playbook",
     "Guidance, rationale, and playbook material for the deliverables in this package."),
    ("04", "Procedure", "Procedure", "Procedure",
     "Step-by-step procedures and operational steps for the deliverables in this package."),
]

# Cross-cutting KTYs: CAT -> list of (TT, slug, Name, schema, routing_patterns, description)
# routing_patterns: substring(s) matched against SourceDoc WITHIN the category.
CROSS_KTY = {
    "CAT-012": [
        ("01", "Product-Requirements-and-Specification", "Product Requirements and System Specification",
         "Specification", ["-PRD", "-SPEC", "-DIRECTIVE"],
         "The product requirements document, system specification, and product directive that define what the app must do."),
        ("02", "Type-and-Interface-Reference", "Type System and Interface Reference",
         "Reference", ["-TYPES", "-CONTRACT"],
         "Type-system and interface/contract reference material."),
        ("03", "Conceptual-and-Overview-Reference", "Conceptual and Overview Reference",
         "Reference", ["WHAT-IS-AN-AGENT", "-README"],
         "Conceptual framing ('what is an agent') and product overview/README reference."),
    ],
    "CAT-013": [
        ("01", "Implementation-Plan", "Implementation Plan", "Reference", ["-PLAN"],
         "The implementation plan: milestones, sequencing, and execution plan of record."),
        ("02", "Build-and-Release-Guidance", "Build and Release Guidance", "Guidance / Playbook", ["RELEASE"],
         "Build-and-release guidance and release quality gates."),
        ("03", "Development-Process-Guidance", "Development Process Guidance", "Guidance / Playbook",
         ["AGENTIC", "VALIDATION"],
         "The agentic development workflow and validation strategy guidance."),
    ],
    "CAT-014": [
        ("01", "Coordination-and-Decision-Record", "Coordination and Decision Record", "Reference",
         ["COORDINATION"],
         "Execution coordination state, decision register, and rulings."),
        ("02", "Scope-Change-Corpus", "Scope-Change Corpus", "Reference", ["SCOPECHANGE"],
         "Provider/general-runtime PI-pattern scope-change packet corpora."),
        ("03", "Execution-Posture-and-Scripts", "Execution Operating Posture and Scripts", "Guidance / Playbook",
         ["SRC-AGENTS", "SCRIPTS", "-EXECUTION"],
         "Repository/agent operating posture (AGENTS.md) and execution scripts."),
    ],
    "CAT-015": [
        ("01", "Decomposition-Reference", "Decomposition Reference", "Reference",
         ["DECOMPOSITION", "-SOURCES"],
         "The app-dev domain decomposition records and source index."),
        ("02", "Dependency-Closure-Report", "Dependency-Closure Report", "Reference", ["DEPCLOSURE"],
         "Dependency-closure dossiers: orchestrator DAG closure, residual closeouts, tranches, handoffs."),
        ("03", "Scope-Closure-Audit", "Scope-Closure Audit", "Reference", ["SCOPECLOSUREAUDIT"],
         "Scope-closure audit records for the SCA scope-change cases."),
        ("04", "PKG00-Closure-Governance-Record", "PKG-00 Closure Governance Record", "Reference",
         ["PKG-00-DAG-CLOSURE"],
         "PKG-00 DAG-closure governance working/reference/checking/issued records."),
    ],
    "CAT-016": [
        ("01", "Frontend-Application-Source", "Frontend Application Source", "Reference",
         ["FRONTEND-SRC"],
         "The frontend application implementation source (grouped SRC-FRONTEND-SRC unit, OI-001)."),
        ("02", "Harness-Contract-and-Documentation", "Harness Contract and Documentation", "Reference",
         ["FRONTEND-DOCS"],
         "Frontend harness documentation: runtime-engine contract, README, traceability."),
    ],
}

DECISION_REF = "GATE4_KTY_PROPOSAL"


def humanize(token: str) -> str:
    return re.sub(r"[_\-]+", " ", token).strip()


def dockind_of(ref: str):
    m = re.search(r"/(?:Case_|Packet_)?(Datasheet|Specification|Guidance|Procedure)\.md", ref)
    return m.group(1) if m else None


def del_of(ref: str):
    m = re.search(r"/(DEL-\d+-\d+)_([A-Za-z0-9_]+?)/", ref)
    if m:
        return m.group(1), m.group(2)
    m = re.search(r"/(DEL-\d+-\d+)_([A-Za-z0-9_]+)", ref)
    return (m.group(1), m.group(2)) if m else (None, None)


def frontend_module(ref: str):
    m = re.search(r"@repo/(frontend/[^:|]+)", ref)
    if not m:
        return "frontend"
    parts = Path(m.group(1)).parts  # frontend / src / lib / harness / file.ts
    if len(parts) >= 4 and parts[1] == "src":
        return "/".join(parts[1:4])      # src/lib/harness
    if len(parts) >= 3 and parts[1] == "src":
        return "/".join(parts[1:3])      # src/components
    if len(parts) >= 2:
        return "/".join(parts[1:2]) or "frontend"  # electron, scripts, ...
    return "frontend"


def main():
    catshort = {r["CategoryID"]: r["Name"] for r in csv.DictReader(open(CAT_REG, encoding="utf-8"))}
    rows = list(csv.DictReader(open(G3_LEDGER, encoding="utf-8")))
    base_cols = list(rows[0].keys())
    g4_cols = ["KnowledgeTypeIDs", "SubjectIDs", "PrimaryKnowledgeTypeID", "PrimarySubjectID",
               "Gate4AssignmentStatus", "Gate4AssignmentMethod", "Gate4AssignmentConfidence",
               "Gate4CandidateSubjectIDs", "Gate4AssignmentRationale"]
    out_cols = base_cols + [c for c in g4_cols if c not in base_cols]

    # --- build KTY table ---
    ktys = {}   # kid -> dict
    def add_kty(kid, cat, tt, slug, name, schema, desc):
        ktys[kid] = {"KnowledgeTypeID": kid, "Name": name, "ParentCategoryID": cat,
                     "Description": desc, "IntendedUsers": "TBD", "WhenUsed": "TBD",
                     "CanonicalSchema": schema, "SourceBasis": "", "AssignmentBasis": "SOURCE_ROUTING",
                     "MappedUnitCount": 0, "SubjectCount": 0, "Status": "PROPOSED_GATE4", "Notes": ""}
    for cat, cc in DELIV_CATS.items():
        short = humanize(catshort[cat])
        for tt, dk, label, schema, desc in DOCKIND_KTY:
            kid = f"KTY-{cc:02d}-{tt}_{dk}-Reference" if dk == "Datasheet" else f"KTY-{cc:02d}-{tt}_{dk}"
            add_kty(kid, cat, tt, dk, f"{short} — {label}", schema, desc + f" (Category {cat}.)")
    for cat, specs in CROSS_KTY.items():
        cc = int(cat.split("-")[1])
        for tt, slug, name, schema, pats, desc in specs:
            add_kty(f"KTY-{cc:02d}-{tt}_{slug}", cat, tt, slug, name, schema, desc)

    def deliv_kty(cat, dk):
        cc = DELIV_CATS[cat]
        tt = {"Datasheet": "01", "Specification": "02", "Guidance": "03", "Procedure": "04"}[dk]
        return f"KTY-{cc:02d}-{tt}_{dk}-Reference" if dk == "Datasheet" else f"KTY-{cc:02d}-{tt}_{dk}"

    def cross_kty(cat, source_doc):
        for (tt, slug, name, schema, pats, desc) in CROSS_KTY.get(cat, []):
            if any(p in source_doc for p in pats):
                cc = int(cat.split("-")[1])
                return f"KTY-{cc:02d}-{tt}_{slug}"
        return None

    # --- assign atoms; collect subjects ---
    subjects = {}        # sid -> dict
    subj_seq = defaultdict(int)   # kid -> running SS
    subj_key2id = {}     # (kid, key) -> sid
    kty_units = Counter()
    subj_units = defaultdict(list)
    unmapped = []

    def subject_for(kid, key, name, cat, basis):
        if (kid, key) in subj_key2id:
            return subj_key2id[(kid, key)]
        subj_seq[kid] += 1
        cc_tt = kid.split("_")[0].replace("KTY-", "")   # CC-TT
        sid = f"SUB-{cc_tt}-{subj_seq[kid]:02d}_{key}"
        subj_key2id[(kid, key)] = sid
        subjects[sid] = {"SubjectID": sid, "Name": name, "ParentKnowledgeTypeID": kid,
                         "CategoryID": cat, "Description": name, "CoversUnits": "",
                         "MappedUnitCount": 0, "Keywords": "", "SourceBasis": basis,
                         "Status": "PROPOSED_GATE4", "Notes": ""}
        return sid

    for r in rows:
        if r["InOutStatus"] != "IN":
            for c in g4_cols:
                r[c] = ""
            continue
        cat = r["CategoryID"]; ref = r["SourceRef"]; sd = r["SourceDoc"]
        kid = sid = None
        if cat in DELIV_CATS:
            dk = dockind_of(ref)
            deln, deltitle = del_of(ref)
            if dk and deln:
                kid = deliv_kty(cat, dk)
                key = re.sub(r"[^A-Za-z0-9]+", "-", deln).strip("-")
                nm = f"{deln} {humanize(deltitle)} — {dk}"
                sid = subject_for(kid, key, nm, cat, f"EXECUTION_DELIVERABLE/{deln}")
        else:
            kid = cross_kty(cat, sd)
            if kid:
                if cat == "CAT-016" and "FRONTEND-SRC" in sd:
                    mod = frontend_module(ref)
                    key = re.sub(r"[^A-Za-z0-9]+", "-", mod).strip("-")
                    sid = subject_for(kid, key, f"Frontend module {mod}", cat, "FRONTEND_SRC")
                else:
                    key = re.sub(r"[^A-Za-z0-9]+", "-", sd.replace("SRC-", "")).strip("-")[:60]
                    sid = subject_for(kid, key, humanize(sd.replace("SRC-", "")), cat, sd)
        if not kid or not sid:
            unmapped.append((r["AtomicUnitID"], cat, sd))
            r.update({c: "" for c in g4_cols})
            r["KnowledgeTypeIDs"] = "TBD_GATE4"; r["SubjectIDs"] = "TBD_GATE4"
            r["Gate4AssignmentStatus"] = "TBD_GATE4"; r["OpenIssue"] = "TRUE"
            continue
        kty_units[kid] += 1
        subj_units[sid].append(r["AtomicUnitID"])
        r["KnowledgeTypeIDs"] = kid; r["SubjectIDs"] = sid
        r["PrimaryKnowledgeTypeID"] = kid; r["PrimarySubjectID"] = sid
        r["Gate4AssignmentStatus"] = "PROPOSED_GATE4"
        r["Gate4AssignmentMethod"] = "SOURCE_ROUTING"
        r["Gate4AssignmentConfidence"] = "HIGH"
        r["Gate4CandidateSubjectIDs"] = f"{sid}:1"
        r["Gate4AssignmentRationale"] = f"Source-routing: doc/content-kind -> {kid}; unit -> {sid}."
        r["DecisionRef"] = (r.get("DecisionRef", "") + ";" + DECISION_REF).strip(";")

    # finalize subject + kty counts / SourceBasis
    for sid, units in subj_units.items():
        subjects[sid]["CoversUnits"] = ";".join(units)
        subjects[sid]["MappedUnitCount"] = len(units)
    kty_subjcount = Counter(s["ParentKnowledgeTypeID"] for s in subjects.values())
    for kid, k in ktys.items():
        k["MappedUnitCount"] = kty_units.get(kid, 0)
        k["SubjectCount"] = kty_subjcount.get(kid, 0)
        basis = sorted({s["SourceBasis"] for s in subjects.values() if s["ParentKnowledgeTypeID"] == kid})
        k["SourceBasis"] = ";".join(basis[:6])

    # --- write registers + ledger ---
    with open(DEC / "Knowledge_Type_Register.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(next(iter(ktys.values())).keys()))
        w.writeheader()
        for kid in sorted(ktys):
            w.writerow(ktys[kid])
    with open(DEC / "Knowledge_Subject_Register.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(next(iter(subjects.values())).keys()))
        w.writeheader()
        for sid in sorted(subjects):
            w.writerow(subjects[sid])
    with open(DEC / "Domain_Ledger_Gate4_KTY_Draft.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out_cols)
        w.writeheader(); w.writerows(rows)
    # summary register
    with open(DEC / "KTY_Assignment_Summary.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["KnowledgeTypeID", "ParentCategoryID", "CanonicalSchema",
                                       "MappedUnitCount", "SubjectCount"])
        for kid in sorted(ktys):
            k = ktys[kid]
            w.writerow([kid, k["ParentCategoryID"], k["CanonicalSchema"], k["MappedUnitCount"], k["SubjectCount"]])

    n_in = sum(1 for r in rows if r["InOutStatus"] == "IN")
    assigned = sum(1 for r in rows if r["InOutStatus"] == "IN" and r["PrimaryKnowledgeTypeID"])
    summary = {"in_atoms": n_in, "assigned": assigned, "unmapped": len(unmapped),
               "ktys": len(ktys), "subjects": len(subjects),
               "ktys_per_cat": dict(Counter(k["ParentCategoryID"] for k in ktys.values())),
               "subjects_per_cat": dict(Counter(s["CategoryID"] for s in subjects.values())),
               "empty_ktys": [kid for kid in ktys if kty_units.get(kid, 0) == 0]}
    print(json.dumps(summary, indent=2))
    return 0 if not unmapped and not summary["empty_ktys"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
