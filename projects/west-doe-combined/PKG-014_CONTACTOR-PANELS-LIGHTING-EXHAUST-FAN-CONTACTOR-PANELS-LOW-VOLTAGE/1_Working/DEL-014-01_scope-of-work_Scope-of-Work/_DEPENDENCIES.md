# Dependencies: DEL-014-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable view and index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Dependencies.csv produced by `TASK + dependency-extract` on 2026-05-25.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Status | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| DEP-014-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0015 | Scope decision SOW-0015 | ACTIVE | HIGH |
| DEP-014-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 | ACTIVE | HIGH |
| DEP-014-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 | ACTIVE | HIGH |
| DEP-014-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 | ACTIVE | HIGH |
| DEP-014-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 | ACTIVE | HIGH |
| DEP-014-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 | ACTIVE | HIGH |
| DEP-014-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 | ACTIVE | HIGH |
| DEP-014-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 | ACTIVE | HIGH |
| DEP-014-01-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07 | Gate 7 Final Published PROJECT_DECOMP Snapshot | ACTIVE | HIGH |
| DEP-014-01-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-014-02_package-datasheet | Package Datasheet | ACTIVE | HIGH |
| DEP-014-01-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-014-03_construction-work-package | Construction Work Package | ACTIVE | HIGH |
| DEP-014-01-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-014-04_vendor-engineered-equipment-package | Vendor Engineered Equipment Package | ACTIVE | HIGH |
| DEP-014-01-013 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-014-05_vendor-document-turnover-package | Vendor Document Turnover Package | ACTIVE | HIGH |
| DEP-014-01-014 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | ENABLES | DELIVERABLE | DEL-014-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | ACTIVE | HIGH |

**Total ACTIVE rows: 14** (8 ANCHOR, 6 EXECUTION)
**Total RETIRED rows: 0**

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 14 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 14 |

**ANCHOR rows (ACTIVE):** 8
- IMPLEMENTS_NODE: 1 (DEP-014-01-001 → SOW-0015)
- TRACES_TO_REQUIREMENT: 7 (OBJ-002 through OBJ-010)

**EXECUTION rows (ACTIVE):** 6
- UPSTREAM PREREQUISITE: 1 (Gate 7 decomposition snapshot)
- DOWNSTREAM ENABLES: 5 (DEL-014-02 through DEL-014-06)

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source docs (AUTO):** Specification.md (ANCHOR_DOC — contains "scope"); Guidance.md, Procedure.md, Datasheet.md (EXECUTION_DOC_ORDER)
- **Decomposition path:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
- **Decomposition status:** FOUND — SCOPE_LEDGER.csv, DELIVERABLE_REGISTER.csv, and OBJECTIVE_DELIVERABLE_MAP.csv consulted; anchors resolved and labeled.
- **_REFERENCES.md:** Present and consulted for TargetLocation resolution.
- **Pass 1 (ANCHOR):** SOW-0015 confirmed as parent scope decision node via SCOPE_LEDGER.csv. Seven objectives (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010) confirmed via DELIVERABLE_REGISTER.csv and OBJECTIVE_DELIVERABLE_MAP.csv.
- **Pass 2 (EXECUTION):** Gate 7 snapshot identified as required upstream prerequisite (DOCUMENT). Five downstream ENABLES edges extracted from Specification.md Scope section — DEL-014-02 through DEL-014-06 are explicitly named as downstream deliverables requiring this SOW's scope boundaries.
- **Parent anchor check:** 1 IMPLEMENTS_NODE row present — OK.
- **No warnings.**

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run; MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Produced 14 ACTIVE rows (8 ANCHOR, 6 EXECUTION). Decomposition snapshot found and consulted. No warnings.
