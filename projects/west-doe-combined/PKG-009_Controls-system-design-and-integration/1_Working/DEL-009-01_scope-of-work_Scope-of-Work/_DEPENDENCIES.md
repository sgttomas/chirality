# Dependencies: DEL-009-01_scope-of-work — Scope of Work

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** EXTRACTED (dependency-extract skill run 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is authoritative (v3.1); this file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

10 rows extracted (ACTIVE). Schema version: v3.1.

| DependencyID | Class | AnchorType | Direction | Type | TargetType | TargetRefID / TargetDeliverableID | TargetName | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| DEP-009-01-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0009 | Scope decision SOW-0009 — Controls system design and integration (WBS 02) | HIGH | ACTIVE |
| DEP-009-01-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-002 | Project Objective OBJ-002 | HIGH | ACTIVE |
| DEP-009-01-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-003 | Project Objective OBJ-003 | HIGH | ACTIVE |
| DEP-009-01-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 | HIGH | ACTIVE |
| DEP-009-01-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 | HIGH | ACTIVE |
| DEP-009-01-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | Project Objective OBJ-007 | HIGH | ACTIVE |
| DEP-009-01-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 | HIGH | ACTIVE |
| DEP-009-01-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 | HIGH | ACTIVE |
| DEP-009-01-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07-SNAPSHOT | Gate 7 Final Published PROJECT_DECOMP Snapshot | HIGH | ACTIVE |
| DEP-009-01-010 | EXECUTION | NOT_APPLICABLE | DOWNSTREAM | INTERFACE | DELIVERABLE | DEL-009-02_package-datasheet | Package Datasheet | HIGH | ACTIVE |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned deliverable folder; source documents used: `_CONTEXT.md` (ANCHOR_DOC), `Specification.md`, `Guidance.md`, `Procedure.md` (EXECUTION_DOCS).
- **ANCHOR_DOC:** `_CONTEXT.md` (highest-confidence anchor signal; contains explicit SOW and objective IDs).
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used for anchor validation and label resolution.
  - Note: Brief specified `GATE-07_Final_Published_2026-05-24/` as a relative path; actual path resolved via `_CONTEXT.md` and `_REFERENCES.md` to the `_GateSnapshots` subfolder above.
- **Pass 1 (ANCHOR):** One IMPLEMENTS_NODE anchor to SOW-0009 (WBS_NODE); seven TRACES_TO_REQUIREMENT anchors to OBJ-002, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-009, OBJ-010 — all confirmed in GATE-07 DELIVERABLE_REGISTER.csv and OBJECTIVE_DELIVERABLE_MAP.csv.
- **Pass 2 (EXECUTION):** Two execution edges extracted:
  - UPSTREAM PREREQUISITE to Gate 7 snapshot — explicit prerequisite stated in `Procedure.md`.
  - DOWNSTREAM INTERFACE to DEL-009-02 — Guidance.md explicitly states that detailed interface requirements are left to the package datasheet.
- **Coordination-only signals excluded:** General statements about keeping alignment with sibling deliverables (Procedure.md verification row "Cross-document consistency") were treated as coordination, not information-flow dependencies, per skill policy.
- **Tree x DAG integrity:** Exactly one IMPLEMENTS_NODE anchor found — no FLOATING_NODE or AMBIGUOUS_ANCHOR warning.

## Lifecycle Summary

| Status | Count |
|---|---|
| ACTIVE | 10 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---|
| TBD | 10 |

| DependencyClass | ACTIVE count |
|---|---|
| ANCHOR | 8 |
| EXECUTION | 2 |

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract skill run; MODE=UPDATE; STRICTNESS=CONSERVATIVE; CONSUMER_CONTEXT=NONE; DECOMPOSITION=GATE-07_Final_Published_2026-05-24 (resolved); 10 rows extracted (ACTIVE); no warnings; schema validated VALID.
