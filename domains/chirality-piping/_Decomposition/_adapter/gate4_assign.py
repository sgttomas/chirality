#!/usr/bin/env python3
"""Gate 4 Knowledge-Type / Subject assignment for chirality-piping.

Mirrors the chirality-app-dev pack-local adapter, generalized to the piping
taxonomy (30 categories). Within each category the Knowledge Types are the
knowledge KINDS the authors actually used; Subjects are the finest faithful
author-grouping. Assignment is deterministic SOURCE_ROUTING — never semantic
override (semantic signal is reserved for the ratification verification layer,
gate4_ratify.py).

KTY axes
--------
* 18 deliverable categories CAT-001..018 (= PKG-00..17): the four author
  document kinds Datasheet->Reference, Specification, Guidance, Procedure
  (1:1 with the persona canonical schemas). The doc-kind lives in each atom's
  @repo SourceRef filename (.../DEL-NN-MM_Title/<DocKind>.md). Subjects are
  per-deliverable (per (KTY, DEL-NN-MM)).
* 12 cross-cutting categories CAT-019..030: the real content kinds of their
  source docs (see CROSS_KTY), routed by SourceDoc substring (first match wins,
  so order patterns specific-before-general). Subjects:
    - doc categories (CAT-019..025): one per SourceDoc.
    - code categories (CAT-026..030, SourceDoc SRC-CODE-*): one per source
      directory (the file's @repo parent dir) — the author's own folder grain.

Lossless: the Gate-3 columns (incl. UnitStatement/ContentHash/CategoryID) are
copied unchanged; Gate-4 columns are appended; no atom splits. Output column
schema matches the app-dev gate4 draft so gate4_ratify + gate5/6 adapters run
unchanged.

Usage:  python3 _adapter/gate4_assign.py     (cwd = MONOREPO_ROOT, chirality/)
Prints a JSON summary; exit 0 iff 0 unmapped IN atoms and 0 empty KTYs.
"""
from __future__ import annotations
import csv, json, re
from pathlib import Path
from collections import defaultdict, Counter

MONO = Path.cwd()
DEC = MONO / "domains/chirality-piping/_Decomposition"
G3_LEDGER = DEC / "Domain_Ledger_Gate3_Category_Draft.csv"
CAT_REG = DEC / "Category_Register.csv"

DELIV_CATS = {f"CAT-{i:03d}": i for i in range(1, 19)}   # CAT-001..018 -> CC index

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
# routing_patterns: substring(s) matched against SourceDoc WITHIN the category; FIRST match wins.
CROSS_KTY = {
    "CAT-019": [
        ("01", "Architecture-and-ADR-Reference", "Architecture and ADR Reference", "Reference",
         ["ARCHITECTURE", "THEORY"],
         "System-architecture decision records, boundary/contract architecture, and analysis theory reference."),
        ("02", "Product-Requirements-and-Intent", "Product Requirements and Intent", "Specification",
         ["-PRD", "-INTENT", "-DIRECTIVE"],
         "The product requirements document, product intent, and product directive that define what the app must do."),
        ("03", "System-Specification", "System Specification", "Specification", ["-SPEC"],
         "The system specification defining the normative behaviour of the application."),
        ("04", "Type-and-Interface-Contract-Reference", "Type and Interface Contract Reference", "Reference",
         ["-TYPES", "-CONTRACT"],
         "Type-system and interface/contract reference material."),
        ("05", "Product-Overview-Reference", "Product Overview Reference", "Reference", ["-README"],
         "Product overview / README reference framing the application."),
    ],
    "CAT-020": [
        ("01", "Implementation-Plan", "Implementation Plan", "Reference", ["-PLAN"],
         "The implementation plan: milestones, sequencing, and execution plan of record."),
        ("02", "Build-and-Release-Guidance", "Build and Release Guidance", "Guidance / Playbook",
         ["BUILD-AND-RELEASE", "RELEASE-QUALITY-GATES", "RELEASE-NOTES"],
         "Build-and-release guidance, release quality gates, and release-notes templates."),
        ("03", "Development-Process-Guidance", "Development Process Guidance", "Guidance / Playbook",
         ["AGENTIC"],
         "The agentic development workflow guidance."),
        ("04", "Validation-Strategy-Reference", "Validation Strategy Reference", "Reference",
         ["VALIDATION"],
         "Validation strategy and validation-manual reference material."),
        ("05", "Reporting-Template", "Reporting Notice Template", "Reference", ["REPORT-NOTICE"],
         "Report-notice template material for issued analysis outputs."),
    ],
    "CAT-021": [
        ("01", "IP-and-Professional-Boundary", "IP and Professional Boundary", "Specification",
         ["IP-AND-DATA-BOUNDARY", "PROFESSIONAL-BOUNDARY"],
         "Intellectual-property / data-boundary policy and professional-responsibility boundary."),
        ("02", "Security-and-Privacy-Policy", "Security and Privacy Policy", "Specification",
         ["SECURITY"],
         "Security and privacy policy: threat model, local-first storage, telemetry, secret/private-library handling, redaction/export controls."),
    ],
    "CAT-022": [
        ("01", "User-Guide", "User Guide", "Guidance / Playbook", ["USER-GUIDE"],
         "The end-user guide for operating the application."),
        ("02", "Developer-Guide", "Developer Guide", "Guidance / Playbook", ["DEVELOPER-GUIDE"],
         "The developer guide for extending and building on the application."),
        ("03", "Contributor-Guide", "Contributor Guide", "Guidance / Playbook", ["CONTRIBUTOR-GUIDE"],
         "The contributor guide for contributing to the project."),
        ("04", "Examples-and-Local-Analysis", "Examples and Local Analysis", "Guidance / Playbook",
         ["EXAMPLES", "LOCAL-ANALYSIS"],
         "Worked examples, rule-pack notices, and local-analysis / local-FEA handoff guidance."),
    ],
    "CAT-023": [
        ("01", "Decomposition-Reference", "Decomposition Reference", "Reference", ["DECOMPOSITION"],
         "The piping domain decomposition and reconciliation records."),
    ],
    "CAT-024": [
        ("01", "Scope-Change-PRD-Corpus", "Scope-Change PRD Corpus", "Reference",
         ["SCOPECHANGE-OPENPIPESTRESS-PRD"],
         "The revised PRD and scope-change brief produced under scope-change governance."),
        ("02", "Scope-Change-Authority-and-Case-Record", "Scope-Change Authority and Case Record",
         "Reference", ["SCA-"],
         "Scope-change authority packets and SCA case records (SCA-001..004)."),
    ],
    "CAT-025": [
        ("01", "Repository-Operating-Posture", "Repository Operating Posture", "Guidance / Playbook",
         ["SRC-AGENTS", "SRC-CONTRIBUTING", "SRC-README"],
         "Repository/agent operating posture: AGENTS.md, CONTRIBUTING, and the root README."),
        ("02", "Contribution-Governance", "Contribution Governance", "Reference", ["GOVERNANCE"],
         "Contribution governance: maintainers, review checklist, and contributor-certification template."),
    ],
    "CAT-026": [
        ("01", "Core-Engine-Implementation-Source", "Core Engine Implementation Source", "Reference",
         ["SRC-CODE-CORE"],
         "The core engine implementation source (grouped SRC-CODE-CORE unit)."),
    ],
    "CAT-027": [
        ("01", "Application-and-GUI-Implementation-Source", "Application and GUI Implementation Source",
         "Reference", ["SRC-CODE-APPS"],
         "The application / desktop GUI implementation source (grouped SRC-CODE-APPS unit)."),
    ],
    "CAT-028": [
        ("01", "Test-Suite-Source", "Test Suite Source", "Reference", ["SRC-CODE-TESTS"],
         "The test-suite implementation source (grouped SRC-CODE-TESTS unit)."),
    ],
    "CAT-029": [
        ("01", "Developer-Tooling-Source", "Developer Tooling and Scripts Source", "Reference",
         ["SRC-CODE-TOOLS"],
         "The developer tooling and scripts implementation source (grouped SRC-CODE-TOOLS unit)."),
    ],
    "CAT-030": [
        ("01", "Validation-Implementation-Source", "Validation and Quality-Oracle Implementation Source",
         "Reference", ["SRC-CODE-VALIDATION"],
         "The validation / quality-oracle implementation source (grouped SRC-CODE-VALIDATION unit)."),
    ],
}

CODE_CATS = {"CAT-026", "CAT-027", "CAT-028", "CAT-029", "CAT-030"}
DECISION_REF = "GATE4_KTY_PROPOSAL"


def humanize(token: str) -> str:
    return re.sub(r"[_\-]+", " ", token).strip()


def dockind_of(ref: str):
    m = re.search(r"/(Datasheet|Specification|Guidance|Procedure)\.md", ref)
    return m.group(1) if m else None


def del_of(ref: str):
    m = re.search(r"/(DEL-\d+-\d+)_([^/]+?)/", ref)
    return (m.group(1), m.group(2)) if m else (None, None)


def code_dir(ref: str):
    m = re.search(r"@repo/([^:|]+)", ref)
    if not m:
        return None
    parts = m.group(1).split("/")
    return "/".join(parts[:-1]) if len(parts) > 1 else parts[0]


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
    def add_kty(kid, cat, slug, name, schema, desc):
        ktys[kid] = {"KnowledgeTypeID": kid, "Name": name, "ParentCategoryID": cat,
                     "Description": desc, "IntendedUsers": "TBD", "WhenUsed": "TBD",
                     "CanonicalSchema": schema, "SourceBasis": "", "AssignmentBasis": "SOURCE_ROUTING",
                     "MappedUnitCount": 0, "SubjectCount": 0, "Status": "PROPOSED_GATE4", "Notes": ""}
    for cat, cc in DELIV_CATS.items():
        short = humanize(catshort[cat])
        for tt, dk, label, schema, desc in DOCKIND_KTY:
            kid = (f"KTY-{cc:02d}-{tt}_Datasheet-Reference" if dk == "Datasheet"
                   else f"KTY-{cc:02d}-{tt}_{dk}")
            add_kty(kid, cat, dk, f"{short} — {label}", schema, desc + f" (Category {cat}.)")
    for cat, specs in CROSS_KTY.items():
        cc = int(cat.split("-")[1])
        for tt, slug, name, schema, pats, desc in specs:
            add_kty(f"KTY-{cc:02d}-{tt}_{slug}", cat, slug, name, schema, desc)

    def deliv_kty(cat, dk):
        cc = DELIV_CATS[cat]
        tt = {"Datasheet": "01", "Specification": "02", "Guidance": "03", "Procedure": "04"}[dk]
        return (f"KTY-{cc:02d}-{tt}_Datasheet-Reference" if dk == "Datasheet"
                else f"KTY-{cc:02d}-{tt}_{dk}")

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
                if cat in CODE_CATS:
                    mod = code_dir(ref) or sd
                    key = re.sub(r"[^A-Za-z0-9]+", "-", mod).strip("-")[:80]
                    sid = subject_for(kid, key, f"Source directory {mod}", cat, f"{sd}/{mod}")
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
               "ktys_per_cat": dict(sorted(Counter(k["ParentCategoryID"] for k in ktys.values()).items())),
               "subjects_per_cat": dict(sorted(Counter(s["CategoryID"] for s in subjects.values()).items())),
               "empty_ktys": [kid for kid in ktys if kty_units.get(kid, 0) == 0]}
    print(json.dumps(summary, indent=2))
    return 0 if not unmapped and not summary["empty_ktys"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
