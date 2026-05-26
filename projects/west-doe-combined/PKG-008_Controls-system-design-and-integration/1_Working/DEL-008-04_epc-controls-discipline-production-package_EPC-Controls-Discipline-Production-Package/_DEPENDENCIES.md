# Dependencies: DEL-008-04_epc-controls-discipline-production-package — EPC / Controls Discipline Production Package

**Coordination Mode:** DECLARED + EXTRACTED
**Dependency tracking mode:** DECLARED + EXTRACTED (dependency-extract run completed 2026-05-25)
**Default maturity threshold:** INITIALIZED
**Register convention:** `Dependencies.csv` is the canonical structured register (v3.1, 29 required columns). This file is the human-readable view.

## Declared Upstream Dependencies

- None declared during PREPARATION.

## Declared Downstream Dependencies

- None declared during PREPARATION.

## Extracted Dependency Register

| DependencyID | Class | AnchorType | Direction | DependencyType | TargetType | TargetRefID | TargetName | Status |
|---|---|---|---|---|---|---|---|---|
| DEP-008-04-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | OTHER | WBS_NODE | SOW-0008 | Scope decision SOW-0008 — Controls system design and integration | ACTIVE |
| DEP-008-04-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-001 | Project Objective OBJ-001 | ACTIVE |
| DEP-008-04-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-003 | Project Objective OBJ-003 | ACTIVE |
| DEP-008-04-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-005 | Project Objective OBJ-005 | ACTIVE |
| DEP-008-04-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-006 | Project Objective OBJ-006 | ACTIVE |
| DEP-008-04-006 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-007 | Project Objective OBJ-007 | ACTIVE |
| DEP-008-04-007 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-009 | Project Objective OBJ-009 | ACTIVE |
| DEP-008-04-008 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OTHER | REQUIREMENT | OBJ-010 | Project Objective OBJ-010 | ACTIVE |
| DEP-008-04-009 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | GATE-07 | Gate 7 PROJECT_DECOMP snapshot (all registers) | ACTIVE |
| DEP-008-04-010 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-DEEPCUT-SEC13 | 4-25 Deepcut DBM — SEC-13 Controls System Basis | ACTIVE |
| DEP-008-04-011 | EXECUTION | NOT_APPLICABLE | UPSTREAM | PREREQUISITE | DOCUMENT | DBM-COMPLIQ-SEC13 | 3-25 Comp and Liquids DBM — SEC-13 Control System Basis | ACTIVE |

**Counts:** 11 rows total — 8 ANCHOR, 3 EXECUTION. All ACTIVE.

## Lifecycle Summary

| Dimension | Count |
|---|---|
| ACTIVE | 11 |
| RETIRED | 0 |
| ANCHOR / IMPLEMENTS_NODE | 1 |
| ANCHOR / TRACES_TO_REQUIREMENT | 7 |
| EXECUTION / PREREQUISITE | 3 |
| SatisfactionStatus = TBD | 11 |

## Run Notes

- **MODE:** UPDATE
- **STRICTNESS:** CONSERVATIVE
- **CONSUMER_CONTEXT:** NONE
- **SOURCE_DOCS:** AUTO — scanned: `Datasheet.md`, `Procedure.md`, `Specification.md`, `Guidance.md`, `_REFERENCES.md`
- **ANCHOR_DOC:** `Datasheet.md` (highest-confidence anchor signal; contains Identification table with SOW and WBS references)
- **EXECUTION_DOC_ORDER:** `Procedure.md` (primary execution signal), `Specification.md`, `Guidance.md`
- **DECOMPOSITION_PATH:** `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` — used for anchor validation and label resolution.
- **Decomposition status:** FOUND — DELIVERABLE_REGISTER.csv, SCOPE_LEDGER.csv, OBJECTIVE_DELIVERABLE_MAP.csv, INTERFACE_REGISTER.csv all consulted.
- **Pass 1 (ANCHOR):** One IMPLEMENTS_NODE row emitted for SOW-0008 (confirmed in SCOPE_LEDGER.csv and DELIVERABLE_REGISTER.csv). Seven TRACES_TO_REQUIREMENT rows emitted for OBJ-001, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-009, OBJ-010 (confirmed in OBJECTIVE_DELIVERABLE_MAP.csv).
- **Pass 2 (EXECUTION):** Three PREREQUISITE rows emitted for documents explicitly listed as required source materials in Procedure.md prerequisites: Gate 7 snapshot, 4-25 Deepcut DBM SEC-13 (primary authority), 3-25 Comp and Liquids DBM SEC-13 (supporting context). No deliverable-to-deliverable EXECUTION edges emitted — source documents do not state explicit information/artifact transfer from sibling deliverables DEL-008-01, DEL-008-02, or DEL-008-03 as formal inputs; those relationships remain structural adjacency inferred from decomposition. CONSERVATIVE posture applied.
- **PKG-008 interface types noted:** Process Piping, Utility Piping, Relief / Flare / Vent, Electrical Power, I&C / Control Cabling, Communications / Network, Building HVAC / Services, Fire & Gas / Safety Systems — recorded in INTERFACE_REGISTER.csv; carried by this deliverable per Specification REQ-002.
- **HRR-001 / HRR-002:** Open human ruling items from Guidance.md conflict table not reflected as dependency edges; they represent internal scope/authority decisions, not information-flow edges.
- **No DOWNSTREAM edges extracted:** No source document states explicit outputs from DEL-008-04 consumed by named downstream deliverables.

## Run History

- 2026-05-24 — Initialized dependency view in DECLARED mode (PREPARATION).
- 2026-05-25 — dependency-extract run (UPDATE / CONSERVATIVE / CONSUMER_CONTEXT=NONE). 11 rows extracted (8 ANCHOR, 3 EXECUTION). All ACTIVE. Decomposition: Gate 7 snapshot found and used. No schema errors. Validator: VALID.
