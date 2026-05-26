# Dependencies: DEL-016-03_construction-work-package — Construction Work Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract run completed)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Register produced by `TASK + dependency-extract` skill run on 2026-05-25.

**Counts — ACTIVE rows:** 17 total (8 ANCHOR, 9 EXECUTION)

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetID / TargetName | Confidence |
|---|---|---|---|---|---|---|---|
| DEP-016-03-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0017 | HIGH |
| DEP-016-03-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | HIGH |
| DEP-016-03-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | HIGH |
| DEP-016-03-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | HIGH |
| DEP-016-03-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | HIGH |
| DEP-016-03-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | HIGH |
| DEP-016-03-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | HIGH |
| DEP-016-03-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | HIGH |
| DEP-016-03-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-016-01_scope-of-work | HIGH |
| DEP-016-03-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-016-02_package-datasheet | HIGH |
| DEP-016-03-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-016-04_vendor-engineered-equipment-package | MEDIUM |
| DEP-016-03-012 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-016-05_vendor-document-turnover-package | MEDIUM |
| DEP-016-03-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | INTERFACE | DELIVERABLE | DEL-016-06_epc-vendor-package-review-and-acceptance | MEDIUM |
| DEP-016-03-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | EXTERNAL | Final Geotechnical Report | HIGH |
| DEP-016-03-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | Detailed Electrical Construction Specification | HIGH |
| DEP-016-03-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | Hazardous-Area Classification Drawings | HIGH |
| DEP-016-03-017 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | EXTERNAL | Commissioning — TXP-8200-1 Transformer | HIGH |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; all four documents used: Datasheet.md (ANCHOR_DOC), Specification.md, Guidance.md, Procedure.md (EXECUTION_DOC_ORDER)
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — found and used; SCOPE_LEDGER.csv row 18, DELIVERABLE_REGISTER.csv row 80, OBJECTIVE_REGISTER.csv consulted for anchor label resolution.
- **ANCHOR_DOC:** Datasheet.md — selected as highest-confidence anchor; contains explicit SOW-0017 and Supports Objectives fields.
- **EXECUTION_DOC_ORDER:** Specification.md → Guidance.md → Procedure.md
- **Pass 1 (ANCHOR):** 1 IMPLEMENTS_NODE anchor (SOW-0017) and 7 TRACES_TO_REQUIREMENT anchors (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010) extracted from Datasheet.md; confirmed against Gate 7 DELIVERABLE_REGISTER.csv row 80 and SCOPE_LEDGER.csv row 18.
- **Pass 2 (EXECUTION):** 9 execution edges extracted from Specification.md, Guidance.md, and Procedure.md. Evidence-grounded; no IMPLICIT edges emitted — all have explicit source text.
- **TBD items from sources:** Three conflict-table entries (HRR-016-03-001, HRR-016-03-002, HRR-016-03-003) noted in Guidance.md with open human rulings; they do not produce additional dependency rows but affect how several UPSTREAM PREREQUISITE targets resolve (location TBD for specs/drawings).
- **FLOATING_NODE check:** 1 IMPLEMENTS_NODE row found — PASS.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First extraction run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition=GATE-07_Final_Published_2026-05-24 (used). 17 ACTIVE rows produced (8 ANCHOR, 9 EXECUTION). No rows retired (first run). Schema validation: VALID.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 17 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 17 |
