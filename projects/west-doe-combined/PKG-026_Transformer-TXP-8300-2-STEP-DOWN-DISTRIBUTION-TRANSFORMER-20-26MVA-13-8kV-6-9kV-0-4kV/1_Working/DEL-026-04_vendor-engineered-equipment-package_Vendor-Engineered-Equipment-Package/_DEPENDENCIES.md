# Dependencies: DEL-026-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** ACCEPTED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1). This file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

`Dependencies.csv` — v3.1 schema, 6 rows (6 ACTIVE, 0 RETIRED).

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetID / TargetRefID | TargetName | SatisfactionStatus | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| DEP-026-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0027 | Scope of Work Item SOW-0027 | TBD | HIGH |
| DEP-026-04-002 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-026-01_scope-of-work | Scope of Work | TBD | HIGH |
| DEP-026-04-003 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-026-02_package-datasheet | Package Datasheet | TBD | HIGH |
| DEP-026-04-004 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-026-03_construction-work-package | Construction Work Package | TBD | HIGH |
| DEP-026-04-005 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-026-05_vendor-document-turnover-package | Vendor Document Turnover Package | TBD | HIGH |
| DEP-026-04-006 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | DELIVERABLE | DEL-026-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | TBD | HIGH |

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 6 |
| RETIRED | 0 |

| SatisfactionStatus | Count (ACTIVE rows) |
|---|---|
| TBD | 6 |

| DependencyClass | ACTIVE count |
|---|---|
| ANCHOR | 1 |
| EXECUTION | 5 |

## Run Notes

- **Run date:** 2026-05-25
- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder: Datasheet.md (ANCHOR_DOC), Procedure.md, Specification.md, Guidance.md
- **ANCHOR_DOC selected:** Datasheet.md (contains Identification table with CoversScopeItem, ParentPackageID)
- **EXECUTION_DOC_ORDER:** Procedure.md (primary workflow signal), Specification.md, Guidance.md
- **DECOMPOSITION_PATH used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
- **Decomposition status:** AVAILABLE — used for anchor validation (SOW-0027 confirmed in SCOPE_LEDGER.csv; deliverable IDs DEL-026-01 through DEL-026-06 confirmed in DELIVERABLE_REGISTER.csv)

**Pass 1 (ANCHOR):** One parent anchor emitted (SOW-0027 as WBS_NODE / IMPLEMENTS_NODE). The CoversScopeItem=SOW-0027 is explicitly stated in Datasheet.md and confirmed in SCOPE_LEDGER.csv GATE-07. Objective associations (OBJ-002 etc.) are flagged ASSUMPTION/package heuristic in Datasheet.md; omitted under CONSERVATIVE strictness.

**Pass 2 (EXECUTION):** Five EXECUTION edges extracted:
- Two UPSTREAM PREREQUISITE edges to DEL-026-01 and DEL-026-02 — Procedure.md step 1 states these must be issued and accepted before vendor engineering; Specification.md R-026-04-001 confirms both as anchor authorities.
- One DOWNSTREAM HANDOVER to DEL-026-03 — Procedure.md step 11 explicitly states shipping/installation instructions are issued to DEL-026-03.
- One DOWNSTREAM HANDOVER to DEL-026-05 — Procedure.md step 12 and Specification R-026-04-009 require vendor documents to flow through DEL-026-05.
- One DOWNSTREAM INTERFACE to DEL-026-06 — Procedure.md step 8 and Specification R-026-04-010 name DEL-026-06 as the review/acceptance mechanism.

**No warnings:** Parent anchor count = 1 (IMPLEMENTS_NODE). No FLOATING_NODE or AMBIGUOUS_ANCHOR conditions.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run; MODE=UPDATE, STRICTNESS=CONSERVATIVE; 6 ACTIVE rows written to Dependencies.csv v3.1; schema VALID.
