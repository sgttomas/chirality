# Dependencies: DEL-020-04_vendor-engineered-equipment-package — Vendor Engineered Equipment Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** DECLARED + EXTRACTED
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1); this file is the human-readable index.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

18 rows extracted (all ACTIVE). Schema version: v3.1.

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence |
|---|---|---|---|---|---|---|---|---|
| DEP-020-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0021 | Scope decision SOW-0021 — 13.8kV SWITCHGEAR EQUIPMENT | HIGH |
| DEP-020-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Project Objective OBJ-001 — Provide the 04-25 Deepcut facility scope | HIGH |
| DEP-020-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-004 | Project Objective OBJ-004 — Vendor-owned package responsibility model | HIGH |
| DEP-020-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 — Facility electrical power basis and switchgear | HIGH |
| DEP-020-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 — Controls instrumentation and communications interfaces | HIGH |
| DEP-020-04-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-008 | Project Objective OBJ-008 — Civil structural foundations and buildings | HIGH |
| DEP-020-04-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 — Safety relief regulatory and codes requirements | HIGH |
| DEP-020-04-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 — Operability maintainability vendor documentation and turnover | HIGH |
| DEP-020-04-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-020-01_scope-of-work | Scope of Work — PKG-020 DEL-020-01 | HIGH |
| DEP-020-04-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DELIVERABLE | DEL-020-02_package-datasheet | Package Datasheet — PKG-020 DEL-020-02 | HIGH |
| DEP-020-04-011 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-020-05_vendor-document-turnover-package | Vendor Document Turnover Package — PKG-020 DEL-020-05 | HIGH |
| DEP-020-04-012 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | HANDOVER | DELIVERABLE | DEL-020-06_epc-vendor-package-review-and-acceptance | EPC Vendor Package Review and Acceptance — PKG-020 DEL-020-06 | HIGH |
| DEP-020-04-013 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | IFC-611474D99C | Interface IFC-611474D99C — Electrical Power | HIGH |
| DEP-020-04-014 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | IFC-F3098CE7CD | Interface IFC-F3098CE7CD — Grounding / Bonding | HIGH |
| DEP-020-04-015 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | IFC-8BF7209227 | Interface IFC-8BF7209227 — I&C / Control Cabling | HIGH |
| DEP-020-04-016 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | IFC-340091634A | Interface IFC-340091634A — Communications / Network | HIGH |
| DEP-020-04-017 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | IFC-2FB786FC10 | Interface IFC-2FB786FC10 — Maintenance Access | HIGH |
| DEP-020-04-018 | EXECUTION | NOT_APPLICABLE | UPSTREAM | CONSTRAINT | EXTERNAL | IFC-08E563D004 | Interface IFC-08E563D004 — Structural / Foundations / Supports | HIGH |

## Run Notes

- **Run date:** 2026-05-25
- **Mode:** UPDATE
- **Strictness:** CONSERVATIVE
- **Consumer context:** NONE
- **Source docs (AUTO):** Datasheet.md (ANCHOR_DOC), Procedure.md, Guidance.md, _CONTEXT.md (EXECUTION_DOCS)
- **Decomposition path:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (resolved from _CONTEXT.md Decomposition Reference; validated SOW-0021 and OBJ-* anchors)
- **DECOMPOSITION_PATH brief value:** `GATE-07_Final_Published_2026-05-24/` (relative); full absolute path above used for validation.
- **DOC_ROLE_MAP:** DEFAULT — Datasheet.md matched ANCHOR_DOC heuristic (contains "datasheet"); Procedure.md and Guidance.md matched EXECUTION_DOC heuristic.
- **ANCHOR_DOC:** Datasheet.md
- **EXECUTION_DOC_ORDER:** Procedure.md, Guidance.md, _CONTEXT.md
- **Pass 1 (ANCHOR):** One IMPLEMENTS_NODE row emitted for SOW-0021 (parent scope node confirmed in SCOPE_LEDGER.csv). Seven TRACES_TO_REQUIREMENT rows emitted for OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 (all confirmed in DELIVERABLE_REGISTER.csv and OBJECTIVE_REGISTER.csv).
- **Pass 2 (EXECUTION):** Two PREREQUISITE rows for DEL-020-01 and DEL-020-02 (explicit in Procedure.md Prerequisites). Two HANDOVER rows for DEL-020-05 and DEL-020-06 (explicit in Procedure.md Step 7). Six CONSTRAINT rows for the six EPC-defined interfaces (explicit in Datasheet.md Conditions table and Guidance.md Principles; interface IDs confirmed in Datasheet.md References section).
- **No warnings.**
- **Tree x DAG integrity:** 1 IMPLEMENTS_NODE row — no FLOATING_NODE or AMBIGUOUS_ANCHOR warning.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 18 |
| RETIRED | 0 |

| DependencyClass | ACTIVE count |
|---|---|
| ANCHOR | 8 |
| EXECUTION | 10 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 18 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — UPDATE run; CONSERVATIVE; dependency-extract skill; 18 rows extracted (8 ANCHOR, 10 EXECUTION); all ACTIVE; decomposition validated; no warnings.
