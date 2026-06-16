#!/usr/bin/env python3
"""Gate 3 deterministic Category assignment for chirality-app-dev.

The app-dev corpus is strongly pre-structured by its authors (PKG-00..10
deliverable packages + cross-cutting docs/governance/frontend groups). The most
FAITHFUL assignment is therefore source-routing: each IN atom inherits the
Category that owns the PKG / source-group its author placed it in. Keyword and
semantic signal are NOT used to override author placement here — they are
reserved for the Gate-3 ratification VERIFICATION layer (gate3_ratify.py), which
surfaces any atom that reads as off-theme as a misassignment candidate.

This is data-driven against Category_Register.csv (it validates that every
routed CategoryID exists) and is NOT the self-domain-specific
tools/decomp/refine_gate3_categories.py.

Routing rules (recorded verbatim in Category_Boundary_Decisions.csv):
  G3BR-001  EXECUTION_DELIVERABLE -> CAT by PKG: PKG-NN -> CAT-0(NN+1).
  G3BR-002  PRODUCT_DOCS -> CAT-012 (requirements/spec/architecture) or
            CAT-013 (process/build/release/validation) per explicit unit map.
  G3BR-003  EXECUTION_GOVERNANCE -> CAT-015 (decomposition/reconciliation/
            dependency-closure/PKG-00 governance/sources) else CAT-014
            (coordination/decisions/scope-change/scripts/execution).
  G3BR-004  FRONTEND_SRC + FRONTEND_DOCS -> CAT-016.
  G3BR-005  ROOT_DOCS (AGENTS.md operating posture) -> CAT-014.
  G3BR-006  No atom splits, no UnitStatement/ContentHash edits (lossless);
            forced source-routing decisions only.
  G3BR-007  Only InOutStatus==IN atoms are assigned; TBD/OUT carry blank
            CategoryID (TBD deferred per OI-013).

Usage:  python3 _adapter/gate3_assign.py
Run with cwd = MONOREPO_ROOT (chirality/). Prints a JSON summary.
"""
from __future__ import annotations
import csv, json, re, sys
from pathlib import Path
from collections import Counter

MONO = Path.cwd()
DEC = MONO / "domains/chirality-app-dev/_Decomposition"
LEDGER = DEC / "Atomic_Domain_Ledger.csv"
REGISTER = DEC / "Category_Register.csv"
PREFIX = DEC / "Source_Decomp_Prefix_Map.csv"

DECISION_REF = "GATE3_CATEGORY_PROPOSAL"

# --- explicit cross-cutting unit maps (G3BR-002) -------------------------------
PRODUCT_MAP = {
    "SRC-DOCS-PRD": "CAT-012", "SRC-DOCS-SPEC": "CAT-012",
    "SRC-DOCS-TYPES": "CAT-012", "SRC-DOCS-CONTRACT": "CAT-012",
    "SRC-DOCS-DIRECTIVE": "CAT-012", "SRC-DOCS-WHAT-IS-AN-AGENT": "CAT-012",
    "SRC-DOCS-README": "CAT-012",
    "SRC-DOCS-PLAN": "CAT-013", "SRC-DOCS-BUILD-AND-RELEASE": "CAT-013",
    "SRC-DOCS-RELEASE-QUALITY-GATES": "CAT-013",
    "SRC-DOCS-AGENTIC-DEVELOPMENT-WORKFLOW": "CAT-013",
    "SRC-DOCS-VALIDATION-STRATEGY": "CAT-013",
}
GOV_CAT015_KEYS = ("RECONCILIATION", "DECOMPOSITION", "PKG-00", "SOURCES")


def pkg_to_cat(pkg_num: int) -> str:
    return f"CAT-{pkg_num + 1:03d}"


def route(group: str, source_doc: str, source_ref: str):
    """Return (category_id, method, rule, rationale) or (None, ...) for TBD/OUT."""
    if group == "EXECUTION_DELIVERABLE":
        m = re.search(r"execution/PKG-(\d+)", source_ref)
        if not m:
            m = re.search(r"DEL-(\d+)-\d+", source_doc)  # fallback: DEL-NN -> PKG-NN
        if m:
            cat = pkg_to_cat(int(m.group(1)))
            return cat, "SOURCE_ROUTING", "G3BR-001", f"PKG-{int(m.group(1)):02d} deliverable -> {cat}"
        return None, None, None, "deliverable atom without resolvable PKG"
    if group == "PRODUCT_DOCS":
        cat = PRODUCT_MAP.get(source_doc)
        return cat, "SOURCE_ROUTING", "G3BR-002", f"product doc {source_doc} -> {cat}"
    if group == "EXECUTION_GOVERNANCE":
        cat = "CAT-015" if any(k in source_doc for k in GOV_CAT015_KEYS) else "CAT-014"
        return cat, "SOURCE_ROUTING", "G3BR-003", f"governance unit {source_doc} -> {cat}"
    if group in ("FRONTEND_SRC", "FRONTEND_DOCS"):
        return "CAT-016", "SOURCE_ROUTING", "G3BR-004", f"{group} -> CAT-016"
    if group == "ROOT_DOCS":
        return "CAT-014", "SOURCE_ROUTING", "G3BR-005", "AGENTS.md operating posture -> CAT-014"
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

    per_cat = Counter()
    unmapped = []
    bad_cat = []
    n_in = 0
    for r in rows:
        st = r["InOutStatus"]
        if st != "IN":
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

    # write Gate-3 ledger draft
    draft = DEC / "Domain_Ledger_Gate3_Category_Draft.csv"
    with open(draft, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out_cols)
        w.writeheader(); w.writerows(rows)

    # summary
    with open(DEC / "Category_Assignment_Summary.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["CategoryID", "InAtoms"])
        for c in sorted(cats):
            w.writerow([c, per_cat.get(c, 0)])

    # boundary decisions register
    rules = [
        ("G3BR-001", "PKG routing", "EXECUTION_DELIVERABLE", "PKG-NN deliverable atoms route to CAT-0(NN+1); one category per author package."),
        ("G3BR-002", "Product-doc split", "PRODUCT_DOCS", "Requirements/spec/architecture docs -> CAT-012; process/build/release/validation docs -> CAT-013 (explicit unit map)."),
        ("G3BR-003", "Governance split", "EXECUTION_GOVERNANCE", "Decomposition/reconciliation/dependency-closure/PKG-00-governance/sources -> CAT-015; coordination/decisions/scope-change/scripts/execution -> CAT-014."),
        ("G3BR-004", "Frontend grouping", "FRONTEND_SRC,FRONTEND_DOCS", "Frontend implementation source (grouped SRC-FRONTEND-SRC, OI-001) and harness docs route to CAT-016."),
        ("G3BR-005", "Root posture", "ROOT_DOCS", "AGENTS.md repository/agent operating posture routes to CAT-014."),
        ("G3BR-006", "Lossless", "ALL", "No atom splits; UnitStatement and ContentHash unchanged; forced source-routing decisions only."),
        ("G3BR-007", "IN-only", "ALL", "Only InOutStatus==IN atoms are assigned a CategoryID; TBD/OUT left blank (TBD deferred per OI-013)."),
    ]
    with open(DEC / "Category_Boundary_Decisions.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["RuleID", "Decision", "AppliesTo", "Rule"])
        w.writerows(rules)

    # findings register (header now; ratification appends misassignment candidates)
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
               "per_category": {c: per_cat.get(c, 0) for c in sorted(cats)},
               "draft_ledger": str(draft.relative_to(MONO))}
    print(json.dumps(summary, indent=2))
    return 0 if not unmapped and not bad_cat else 1


if __name__ == "__main__":
    raise SystemExit(main())
