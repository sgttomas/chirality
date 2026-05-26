# Dependencies: DEL-029-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract v3.1)
**Default maturity threshold:** ACCEPTED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

8 rows extracted (ACTIVE). 0 RETIRED.

| DependencyID | Class | AnchorType | Dir | Type | TargetType | TargetID / TargetName | SatisfactionStatus | Confidence |
|---|---|---|---|---|---|---|---|---|
| DEP-029-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | PACKAGE | PKG-029 — Transformer TXP-8600-1 | SATISFIED | HIGH |
| DEP-029-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | WBS_NODE | SOW-0030 | SATISFIED | HIGH |
| DEP-029-04-003 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-029-01_scope-of-work | TBD | HIGH |
| DEP-029-04-004 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-029-02_package-datasheet | TBD | HIGH |
| DEP-029-04-005 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07_Final_Published_2026-05-24 | SATISFIED | HIGH |
| DEP-029-04-006 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-029-05_vendor-document-turnover-package | TBD | HIGH |
| DEP-029-04-007 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | DELIVERABLE | DEL-029-06_epc-vendor-package-review-and-acceptance | TBD | HIGH |
| DEP-029-04-008 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-029-03_construction-work-package | TBD | MEDIUM |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source documents scanned (AUTO):** `Datasheet.md`, `Specification.md`, `Procedure.md`, `Guidance.md`, `_CONTEXT.md`, `_REFERENCES.md`
- **ANCHOR_DOC:** `Datasheet.md` (contains Identification table with explicit PKG-029/SOW-0030 references; matches `datasheet` heuristic)
- **EXECUTION_DOC_ORDER:** `Specification.md`, `Procedure.md`, `Guidance.md`
- **Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
- **Decomposition status:** Present and used to validate PKG-029 anchor and all DEL-029-* target IDs. All referenced deliverable IDs confirmed in DELIVERABLE_REGISTER.csv.
- **Warnings:** None.
- **Assumptions / notes:**
  - DEP-029-04-008 (UPSTREAM INTERFACE to DEL-029-03 Construction Work Package) is MEDIUM confidence: REQ-029-04-007 explicitly names EPC Integrator coordination on foundations/spacing/access, but the direct dependency to the CWP deliverable is inferred from the decomposition register rather than named directly in text. Marked FACT for the coordination requirement; MEDIUM confidence for the specific deliverable link.
  - DEP-029-04-004 (UPSTREAM PREREQUISITE to DEL-029-02 Package Datasheet) is conditional: Specification states "DEL-029-02, if produced"; the deliverable is registered in decomposition and is an explicit prerequisite per the scope paragraph.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 8 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| SATISFIED | 3 |
| TBD | 5 |

| DependencyClass | Count |
|---|---|
| ANCHOR | 2 |
| EXECUTION | 6 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24 (present, used). 8 ACTIVE rows written. 0 RETIRED. No warnings.
