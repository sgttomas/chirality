# Dependencies: DEL-056-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill, UPDATE run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register (v3.1 schema). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Dependencies.csv generated 2026-05-25 by dependency-extract skill.

| Count class | Count |
|---|---|
| ACTIVE rows | 18 |
| RETIRED rows | 0 |
| ANCHOR rows (ACTIVE) | 14 |
| EXECUTION rows (ACTIVE) | 4 |
| UPSTREAM rows (ACTIVE) | 16 |
| DOWNSTREAM rows (ACTIVE) | 2 |

### Compact table — ACTIVE rows

| DependencyID | Class | AnchorType | Dir | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence |
|---|---|---|---|---|---|---|---|---|
| DEP-056-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | PKG-056 | Inlet Separators 4-25 | HIGH |
| DEP-056-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0127 | SOW-0127 | HIGH |
| DEP-056-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0128 | SOW-0128 | HIGH |
| DEP-056-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0129 | SOW-0129 | HIGH |
| DEP-056-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | SOW-0130 | SOW-0130 | HIGH |
| DEP-056-04-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | OBJ-001 | MEDIUM |
| DEP-056-04-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-003 | OBJ-003 | MEDIUM |
| DEP-056-04-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | OBJ-004 | MEDIUM |
| DEP-056-04-009 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | OBJ-005 | MEDIUM |
| DEP-056-04-010 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | OBJ-006 | MEDIUM |
| DEP-056-04-011 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | OBJ-007 | MEDIUM |
| DEP-056-04-012 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | OBJ-008 | MEDIUM |
| DEP-056-04-013 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | OBJ-009 | MEDIUM |
| DEP-056-04-014 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | OBJ-010 | MEDIUM |
| DEP-056-04-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-056-01_scope-of-work | Scope of Work | HIGH |
| DEP-056-04-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-056-02_package-datasheet | Package Datasheet | HIGH |
| DEP-056-04-017 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-056-05_vendor-document-turnover-package | Vendor Document Turnover Package | HIGH |
| DEP-056-04-018 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | DELIVERABLE | DEL-056-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance | HIGH |

## Run Notes

**Run date:** 2026-05-25
**Mode:** UPDATE
**Strictness:** CONSERVATIVE
**Consumer context:** NONE
**Source documents scanned (AUTO):** Datasheet.md (ANCHOR_DOC), Procedure.md, Guidance.md, Specification.md (EXECUTION_DOCs)
**Decomposition path used:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
**Decomposition status:** FOUND — used to validate PKG-056 parent anchor, DEL-056-0* target IDs, SOW IDs, and OBJ IDs.
**_REFERENCES.md status:** Present — consulted for decomposition path; no additional TargetLocation pointers resolved (source docs not locally extracted to slices beyond existing .md files).
**Prior Dependencies.csv:** Not present — new file created.

**Decisions logged:**
- Pass 1 produced one IMPLEMENTS_NODE anchor to PKG-056 (WBS_NODE) and 13 TRACES_TO_REQUIREMENT anchors (4x SOW, 9x OBJ). Objective anchors marked MEDIUM confidence per ASSUMPTION flag in source (package-grouping heuristic per _CONTEXT.md), consistent with decomposition OBJECTIVE_DELIVERABLE_MAP confirmation.
- Pass 2 produced 4 EXECUTION edges: 2 UPSTREAM PREREQUISITE (DEL-056-01, DEL-056-02), 1 DOWNSTREAM HANDOVER (DEL-056-05), 1 DOWNSTREAM INTERFACE (DEL-056-06). DEL-056-03 (Construction Work Package) was evaluated: Specification and Procedure do not state an explicit information/artifact transfer from DEL-056-03 to this deliverable; construction installation is downstream consumer, not a prerequisite input — not extracted (information-flow-only rule).
- No TargetType=UNKNOWN rows required; all targets resolved via decomposition.
- No rows marked RETIRED (no prior register).

**Warnings:** None.

## Lifecycle Summary

| Dimension | Value |
|---|---|
| Total rows | 18 |
| ACTIVE | 18 |
| RETIRED | 0 |
| SatisfactionStatus = TBD | 18 |
| SatisfactionStatus = PENDING | 0 |
| SatisfactionStatus = SATISFIED | 0 |
| ANCHOR / IMPLEMENTS_NODE | 1 |
| ANCHOR / TRACES_TO_REQUIREMENT | 13 |
| EXECUTION / UPSTREAM / PREREQUISITE | 2 |
| EXECUTION / DOWNSTREAM / HANDOVER | 1 |
| EXECUTION / DOWNSTREAM / INTERFACE | 1 |

Parent anchor check: 1 IMPLEMENTS_NODE row — OK (no FLOATING_NODE or AMBIGUOUS_ANCHOR warning).

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill, UPDATE, CONSERVATIVE, decomposition GATE-07_Final_Published_2026-05-24 FOUND. New file created. 18 ACTIVE rows extracted (14 ANCHOR, 4 EXECUTION). No warnings.
