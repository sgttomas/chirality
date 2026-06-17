#!/usr/bin/env python3
"""Gate 3 deterministic Category assignment for chirality-piping.

The piping corpus is strongly pre-structured by its authors (PKG-00..17
deliverable packages + cross-cutting docs/governance/root/code groups). The most
FAITHFUL assignment is therefore source-routing: each IN atom inherits the
Category that owns the PKG / source-group its author placed it in. Keyword and
semantic signal are NOT used to override author placement here — they are
reserved for the Gate-3 ratification VERIFICATION layer (gate3_ratify.py), which
surfaces any atom that reads as off-theme as a misassignment candidate.

Data-driven against Category_Register.csv (validates every routed CategoryID
exists). Lossless: no atom splits, no UnitStatement/ContentHash edits.

Routing rules (recorded in Category_Boundary_Decisions.csv):
  G3BR-001  EXECUTION_DELIVERABLE -> CAT by PKG: PKG-NN -> CAT-0(NN+1).
  G3BR-002  PRODUCT_DOCS -> per explicit unit map (CAT-019..022, plus the docs/
            _ScopeChange units -> CAT-024 and the governance/ units -> CAT-025).
  G3BR-003  EXECUTION_GOVERNANCE -> CAT-023 (decomposition) else CAT-024
            (scope-change).
  G3BR-004  CODE_* -> CAT-026 (core) / CAT-027 (apps) / CAT-028 (tests) /
            CAT-029 (tools) / CAT-030 (validation).
  G3BR-005  ROOT_DOCS (AGENTS/CONTRIBUTING/README operating posture) -> CAT-025.
  G3BR-006  No atom splits, no UnitStatement/ContentHash edits (lossless);
            forced source-routing decisions only.
  G3BR-007  Only InOutStatus==IN atoms are assigned; TBD/OUT carry blank
            CategoryID.

Usage:  python3 _adapter/gate3_assign.py    (cwd = MONOREPO_ROOT)
"""
from __future__ import annotations
import csv, json, re
from pathlib import Path
from collections import Counter

MONO = Path.cwd()
DEC = MONO / "domains/chirality-piping/_Decomposition"
LEDGER = DEC / "Atomic_Domain_Ledger.csv"
REGISTER = DEC / "Category_Register.csv"
PREFIX = DEC / "Source_Decomp_Prefix_Map.csv"

DECISION_REF = "GATE3_CATEGORY_PROPOSAL"

# --- explicit PRODUCT_DOCS unit map (G3BR-002) -------------------------------
PRODUCT_MAP = {
    # CAT-019 Product Requirements, Specification, and System Architecture
    "SRC-DOCS-PRD": "CAT-019", "SRC-DOCS-SPEC": "CAT-019",
    "SRC-DOCS-TYPES": "CAT-019", "SRC-DOCS-CONTRACT": "CAT-019",
    "SRC-DOCS-DIRECTIVE": "CAT-019", "SRC-DOCS-INTENT": "CAT-019",
    "SRC-DOCS-README": "CAT-019",
    "SRC-DOCS-ARCHITECTURE-ADR-ADR-0001-OPERATION-SEAM-ENGINE-UNIFICATION": "CAT-019",
    "SRC-DOCS-ARCHITECTURE-ADR-INDEX": "CAT-019",
    "SRC-DOCS-ARCHITECTURE-ADR-TEMPLATE": "CAT-019",
    "SRC-DOCS-ARCHITECTURE-ANALYSIS-STATUS-SEMANTICS": "CAT-019",
    "SRC-DOCS-ARCHITECTURE-CODE-NEUTRAL-ANALYSIS-BOUNDARY": "CAT-019",
    "SRC-DOCS-ARCHITECTURE-EXTENSION-DOMAIN-CONTRACTS": "CAT-019",
    "SRC-DOCS-ARCHITECTURE-PERSISTENCE-CONTRACT": "CAT-019",
    "SRC-DOCS-ARCHITECTURE-PLUGIN-BOUNDARY": "CAT-019",
    "SRC-DOCS-THEORY-CENTERLINE-ANALYSIS": "CAT-019",
    # CAT-020 Development Process, Build, Release, and Validation Strategy
    "SRC-DOCS-PLAN": "CAT-020", "SRC-DOCS-BUILD-AND-RELEASE": "CAT-020",
    "SRC-DOCS-RELEASE-QUALITY-GATES": "CAT-020",
    "SRC-DOCS-RELEASE-NOTES-TEMPLATE": "CAT-020",
    "SRC-DOCS-AGENTIC-DEVELOPMENT-WORKFLOW": "CAT-020",
    "SRC-DOCS-VALIDATION-STRATEGY": "CAT-020",
    "SRC-DOCS-VALIDATION-MANUAL-INDEX": "CAT-020",
    "SRC-DOCS-REPORT-NOTICE-TEMPLATE": "CAT-020",
    # CAT-021 IP, Data Boundary, Security, and Privacy Policy
    "SRC-DOCS-IP-AND-DATA-BOUNDARY": "CAT-021",
    "SRC-DOCS-PROFESSIONAL-BOUNDARY": "CAT-021",
    "SRC-DOCS-SECURITY-LOCAL-FIRST-STORAGE-POLICY": "CAT-021",
    "SRC-DOCS-SECURITY-REDACTION-EXPORT-CONTROLS": "CAT-021",
    "SRC-DOCS-SECURITY-SECRET-PRIVATE-LIBRARY-HANDLING": "CAT-021",
    "SRC-DOCS-SECURITY-TELEMETRY-POLICY": "CAT-021",
    "SRC-DOCS-SECURITY-THREAT-MODEL": "CAT-021",
    # CAT-022 User, Developer, and Contributor Guides, Examples, and Local Analysis
    "SRC-DOCS-USER-GUIDE-INDEX": "CAT-022",
    "SRC-DOCS-DEVELOPER-GUIDE-INDEX": "CAT-022",
    "SRC-DOCS-CONTRIBUTOR-GUIDE-INDEX": "CAT-022",
    "SRC-DOCS-EXAMPLES-README": "CAT-022",
    "SRC-DOCS-EXAMPLES-RULE-PACK-NOTICE": "CAT-022",
    "SRC-DOCS-LOCAL-ANALYSIS-LOCAL-FEA-HANDOFF-GUIDANCE": "CAT-022",
    # CAT-024 Scope-Change Governance (docs/_ScopeChange units)
    "SRC-DOCS-SCOPECHANGE-OPENPIPESTRESS-PRD-V0-2": "CAT-024",
    "SRC-DOCS-SCOPECHANGE-OPENPIPESTRESS-PRD-V0-2-SCOPE-CHANGE-BRIEF": "CAT-024",
    "SRC-DOCS-SCOPECHANGE-SCA-002-2026-05-02-1854-AUTHORITY": "CAT-024",
    "SRC-DOCS-SCOPECHANGE-SCA-003-2026-05-17-1658-AUTHORITY": "CAT-024",
    # CAT-025 Repository Operating Posture and Contribution Governance (governance/ units)
    "SRC-GOVERNANCE-CONTRIBUTION-REVIEW-CHECKLIST": "CAT-025",
    "SRC-GOVERNANCE-CONTRIBUTOR-CERTIFICATION-TEMPLATE": "CAT-025",
    "SRC-GOVERNANCE-MAINTAINERS": "CAT-025",
}
CODE_MAP = {
    "CODE_CORE": "CAT-026", "CODE_APPS": "CAT-027", "CODE_TESTS": "CAT-028",
    "CODE_TOOLS": "CAT-029", "CODE_VALIDATION": "CAT-030",
}


def pkg_to_cat(pkg_num: int) -> str:
    return f"CAT-{pkg_num + 1:03d}"


def route(group: str, source_doc: str, source_ref: str):
    """Return (category_id, method, rule, rationale) or (None, ...)."""
    if group == "EXECUTION_DELIVERABLE":
        m = re.search(r"PKG-(\d+)", source_ref) or re.search(r"PKG-(\d+)", source_doc)
        if m:
            cat = pkg_to_cat(int(m.group(1)))
            return cat, "SOURCE_ROUTING", "G3BR-001", f"PKG-{int(m.group(1)):02d} deliverable -> {cat}"
        return None, None, None, "deliverable atom without resolvable PKG"
    if group == "PRODUCT_DOCS":
        cat = PRODUCT_MAP.get(source_doc)
        return cat, "SOURCE_ROUTING", "G3BR-002", f"product doc {source_doc} -> {cat}"
    if group == "EXECUTION_GOVERNANCE":
        cat = "CAT-023" if "DECOMPOSITION" in source_doc else "CAT-024"
        return cat, "SOURCE_ROUTING", "G3BR-003", f"governance unit {source_doc} -> {cat}"
    if group in CODE_MAP:
        return CODE_MAP[group], "SOURCE_ROUTING", "G3BR-004", f"{group} -> {CODE_MAP[group]}"
    if group == "ROOT_DOCS":
        return "CAT-025", "SOURCE_ROUTING", "G3BR-005", "operating posture -> CAT-025"
    return None, None, None, f"unmapped group {group}"


def main():
    cats = {r["CategoryID"] for r in csv.DictReader(open(REGISTER, encoding="utf-8"))}
    src2grp = {r["SourceUnitID"]: r["SourceGroup"]
               for r in csv.DictReader(open(PREFIX, encoding="utf-8"))}

    rows = list(csv.DictReader(open(LEDGER, encoding="utf-8")))
    base_cols = list(rows[0].keys())
    g3_cols = ["CategoryID", "CategoryAssignmentStatus", "CategoryAssignmentMethod",
               "CategoryAssignmentConfidence", "CategoryCandidateIDs",
               "CategoryAssignmentRationale", "KnowledgeTypeIDs", "SubjectIDs",
               "DecisionRef", "OpenIssue"]
    out_cols = base_cols + g3_cols

    per_cat = Counter(); unmapped = []; bad_cat = []; n_in = 0
    for r in rows:
        if r["InOutStatus"] != "IN":
            for c in g3_cols:
                r[c] = ""
            continue
        n_in += 1
        group = src2grp.get(r["SourceDoc"], "?")
        cat, method, rule, rationale = route(group, r["SourceDoc"], r["SourceRef"])
        if cat is None:
            unmapped.append((r["AtomicUnitID"], group, r["SourceDoc"]))
            r.update({c: "" for c in g3_cols})
            r["OpenIssue"] = "UNMAPPED_GATE3"
            continue
        if cat not in cats:
            bad_cat.append((r["AtomicUnitID"], cat))
        per_cat[cat] += 1
        r["CategoryID"] = cat
        r["CategoryAssignmentStatus"] = "PROPOSED_GATE3"
        r["CategoryAssignmentMethod"] = method
        r["CategoryAssignmentConfidence"] = "HIGH"
        r["CategoryCandidateIDs"] = f"{cat}:1"
        r["CategoryAssignmentRationale"] = f"Assigned by {rule}: {rationale}."
        r["KnowledgeTypeIDs"] = "TBD_GATE4"
        r["SubjectIDs"] = "TBD_GATE4"
        r["DecisionRef"] = DECISION_REF
        r["OpenIssue"] = "FALSE"

    draft = DEC / "Domain_Ledger_Gate3_Category_Draft.csv"
    with open(draft, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out_cols)
        w.writeheader(); w.writerows(rows)

    with open(DEC / "Category_Assignment_Summary.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["CategoryID", "InAtoms"])
        for c in sorted(cats):
            w.writerow([c, per_cat.get(c, 0)])

    rules = [
        ("G3BR-001", "PKG routing", "EXECUTION_DELIVERABLE", "PKG-NN deliverable atoms route to CAT-0(NN+1); one category per author package (PKG-00..17 -> CAT-001..018)."),
        ("G3BR-002", "Product-doc map", "PRODUCT_DOCS", "Explicit unit map: requirements/spec/architecture -> CAT-019; process/build/release/validation -> CAT-020; IP/security policy -> CAT-021; guides/examples -> CAT-022; docs/_ScopeChange -> CAT-024; governance/ -> CAT-025."),
        ("G3BR-003", "Governance split", "EXECUTION_GOVERNANCE", "execution/_Decomposition -> CAT-023; execution/_ScopeChange (SCA-NNN) -> CAT-024."),
        ("G3BR-004", "Code grouping", "CODE_*", "core/ -> CAT-026; apps/ -> CAT-027; tests/ -> CAT-028; tools/ -> CAT-029; validation/ -> CAT-030."),
        ("G3BR-005", "Root posture", "ROOT_DOCS", "AGENTS/CONTRIBUTING/README operating posture routes to CAT-025."),
        ("G3BR-006", "Lossless", "ALL", "No atom splits; UnitStatement and ContentHash unchanged; forced source-routing decisions only."),
        ("G3BR-007", "IN-only", "ALL", "Only InOutStatus==IN atoms are assigned a CategoryID; TBD/OUT left blank."),
    ]
    with open(DEC / "Category_Boundary_Decisions.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["RuleID", "Decision", "AppliesTo", "Rule"])
        w.writerows(rules)

    findings = DEC / "Category_Assignment_Findings.csv"
    with open(findings, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["FindingID", "AtomicUnitID", "SourceDoc", "PriorAssignedCategoryID",
                    "AssignedCategoryID", "CandidateCategoryIDs", "FindingType",
                    "Severity", "Status", "Evidence", "Recommendation",
                    "ResolutionRuleID", "ResolutionNote"])
        for i, (aid, grp, sd) in enumerate(unmapped, 1):
            w.writerow([f"G3F-{i:05d}", aid, sd, "", "", "", "UNMAPPED_SOURCE_ROUTING",
                        "BLOCKER", "OPEN", f"group={grp}", "Add routing rule or fix manifest", "", ""])

    summary = {"in_atoms": n_in, "assigned": sum(per_cat.values()),
               "unmapped": len(unmapped), "bad_category_refs": len(bad_cat),
               "categories": len(cats),
               "per_category": {c: per_cat.get(c, 0) for c in sorted(cats)},
               "draft_ledger": str(draft.relative_to(MONO))}
    print(json.dumps(summary, indent=2))
    return 0 if not unmapped and not bad_cat else 1


if __name__ == "__main__":
    raise SystemExit(main())
