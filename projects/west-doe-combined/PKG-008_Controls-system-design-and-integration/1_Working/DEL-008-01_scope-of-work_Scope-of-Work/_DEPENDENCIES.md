# Dependencies: DEL-008-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register; this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

Total rows: 8 | ACTIVE: 8 | RETIRED: 0

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID | TargetName | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-008-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0008 | Scope decision SOW-0008 — Controls system design and integration (WBS 01) | ACTIVE |
| DEP-008-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Project Objective OBJ-001 | ACTIVE |
| DEP-008-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-003 | Project Objective OBJ-003 | ACTIVE |
| DEP-008-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 | ACTIVE |
| DEP-008-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 | ACTIVE |
| DEP-008-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | Project Objective OBJ-007 | ACTIVE |
| DEP-008-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 | ACTIVE |
| DEP-008-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 | ACTIVE |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned Specification.md (ANCHOR_DOC), Datasheet.md, Procedure.md, Guidance.md from deliverable folder.
- **DECOMPOSITION_PATH:** `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — used to validate anchors and resolve canonical labels.
- **ANCHOR_DOC:** Datasheet.md (contains identification table with SOW reference and source basis).
- **Pass 1 (ANCHOR):** One parent anchor emitted for SOW-0008 (IMPLEMENTS_NODE). Seven objective traces emitted for OBJ-001, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-009, OBJ-010 per DELIVERABLE_REGISTER.csv SupportsObjectives column.
- **Pass 2 (EXECUTION):** No EXECUTION rows emitted. Sources declare no upstream or downstream deliverable dependencies. No explicit prerequisite information flows, "requires receipt of," or "shall not proceed until" statements referencing other deliverables were found. The controls power-panel interface note (Specification.md) is structural adjacency only — no artifact transfer stated. CONSERVATIVE strictness applied.
- **[WARNING] FLOATING_NODE:** Not applicable — one IMPLEMENTS_NODE anchor present (DEP-008-01-001).

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — First EXTRACTED run. MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE. Decomposition: GATE-07_Final_Published_2026-05-24. Emitted 8 ANCHOR rows (1 IMPLEMENTS_NODE + 7 TRACES_TO_REQUIREMENT). 0 EXECUTION rows (no explicit execution dependencies found in sources). ACTIVE: 8, RETIRED: 0.

## Lifecycle Summary

- ACTIVE: 8
- RETIRED: 0
- ANCHOR rows: 8 (1 IMPLEMENTS_NODE, 7 TRACES_TO_REQUIREMENT)
- EXECUTION rows: 0
- SatisfactionStatus breakdown: TBD: 8
