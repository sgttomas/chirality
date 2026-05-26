# Dependencies: DEL-076-06_epc-vendor-package-review-and-acceptance — EPC Vendor Package Review and Acceptance

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill; UPDATE mode)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is authoritative; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

10 rows extracted (all ACTIVE). Schema version v3.1.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-076-06-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-076 — Lube Oil Supply | HIGH | ACTIVE |
| DEP-076-06-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0135 | HIGH | ACTIVE |
| DEP-076-06-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0136 | HIGH | ACTIVE |
| DEP-076-06-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0137 | HIGH | ACTIVE |
| DEP-076-06-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0138 | HIGH | ACTIVE |
| DEP-076-06-006 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-076-01 — Scope of Work | HIGH | ACTIVE |
| DEP-076-06-007 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-076-02 — Package Datasheet | HIGH | ACTIVE |
| DEP-076-06-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-076-03 — Construction Work Package | HIGH | ACTIVE |
| DEP-076-06-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-076-04 — Vendor Engineered Equipment Package | HIGH | ACTIVE |
| DEP-076-06-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-076-05 — Vendor Document Turnover Package | HIGH | ACTIVE |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source docs (AUTO):** Datasheet.md, Guidance.md, Procedure.md, Specification.md
- **ANCHOR_DOC (AUTO):** Datasheet.md (contains Identification table with ParentPackageID and Covers Scope Items — highest-confidence anchor signals)
- **EXECUTION_DOC_ORDER (AUTO):** Procedure.md (explicit prerequisites and steps), Specification.md (requirements R-076-06-07), Guidance.md (considerations), Datasheet.md (supplemental)
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/PACKAGE_REGISTER.csv` and `DELIVERABLE_REGISTER.csv` (live working surface; GATE-07 snapshot referenced in `_REFERENCES.md` is at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`)
- **DECOMPOSITION_PATH override:** Invoker supplied path `GATE-07_Final_Published_2026-05-24/` which does not exist as a standalone directory; resolved to live working decomposition surface. No validation failure — decomposition confirmed present.
- **Pass 1 (ANCHOR):** One IMPLEMENTS_NODE parent anchor (PKG-076) + four TRACES_TO_REQUIREMENT rows (SOW-0135 through SOW-0138). All identifiers appear explicitly in Datasheet.md Identification table and confirmed against DELIVERABLE_REGISTER.csv.
- **Pass 2 (EXECUTION):** Five UPSTREAM PREREQUISITE edges to sibling deliverables DEL-076-01 through DEL-076-05. All five are explicitly listed in Procedure.md Prerequisites and/or Specification.md R-076-06-07. No DOWNSTREAM edges extracted — no explicit downstream consumers stated in source documents.
- **[WARNING] FLOATING_NODE:** Not applicable — IMPLEMENTS_NODE parent anchor present (DEP-076-06-001).
- **Objective traces (OBJ-001, OBJ-004 through OBJ-010):** Not extracted as separate rows per CONSERVATIVE strictness; objectives appear in source as package-grouping heuristic (ASSUMPTION label in Datasheet.md). These are traceability from the decomposition map, not explicitly stated in deliverable source documents as information-flow dependencies.
- **`_REFERENCES.md` usage:** Confirmed sibling deliverable paths for TargetLocation fields on EXECUTION rows.
- No source documents were modified.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 10 |
| RETIRED | 0 |

| Class | ACTIVE |
|---|---|
| ANCHOR | 5 |
| EXECUTION | 5 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 5 (ANCHOR rows — SOW traces and parent node) |
| PENDING | 5 (EXECUTION prerequisite rows) |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — Full two-pass extraction (dependency-extract skill; UPDATE; CONSERVATIVE). 10 rows extracted (5 ANCHOR, 5 EXECUTION). Schema VALID. Row count: 10.
