# Dependencies: DEL-03-02 Thin TurnEngine and Session Locking

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no accepted dependency edges have been extracted yet.

## Declared Downstream

TBD - no accepted dependency edges have been extracted yet.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 19:30 dependency-extract run used MODE=UPDATE, STRICTNESS=CONSERVATIVE, CONSUMER_CONTEXT=NONE.
- Decomposition authority: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (available; anchors and deliverable targets resolved conservatively).
- Source docs used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Source docs intentionally not consumed: `_SEMANTIC.md` (invalid evidence per human ruling) and `_STATUS.md` (outside the human-authorized evidence set for this run).
- Anchor doc selected by AUTO: `Datasheet.md`.
- Execution doc order selected by AUTO: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- [WARNING] SOURCE_STATE: `_REFERENCES.md` records `docs/PRD.md` as `HASH_MISMATCH`; PRD-derived dependency evidence was used only where already represented in the permitted deliverable docs and/or decomposition.
- [WARNING] TBD_IMPLEMENTATION_PATHS: current route/session implementation paths, lock storage mechanism, event writer API, exact test file locations, and full interrupt/cancel mapping remain TBD and were not converted into invented dependency targets.
- [WARNING] ID_FORMAT_TOOL_MISMATCH: `tools/validation/validate_id_format.sh` expects `DEL-NNN-NN` and `PKG-NNN`, but the accepted decomposition uses `DEL-03-02` and `PKG-03`; authoritative decomposition IDs were preserved.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1

| Metric | Count |
|---|---:|
| Total rows | 10 |
| ACTIVE rows | 10 |
| RETIRED rows | 0 |
| ANCHOR rows | 5 |
| EXECUTION rows | 5 |
| DECLARED rows | 0 |
| EXTRACTED rows | 10 |

| DependencyID | Class | Direction | Type | Target | Status |
|---|---|---|---|---|---|
| DEL-03-02-DEP-001 | ANCHOR | UPSTREAM | OTHER | PKG-03 Runtime Engine Contract and Turn Lifecycle | ACTIVE |
| DEL-03-02-DEP-002 | ANCHOR | UPSTREAM | OTHER | SOW-009 Session CRUD | ACTIVE |
| DEL-03-02-DEP-003 | ANCHOR | UPSTREAM | OTHER | SOW-010 Session boot metadata | ACTIVE |
| DEL-03-02-DEP-004 | ANCHOR | UPSTREAM | OTHER | SOW-011 SSE turn stream and session locking | ACTIVE |
| DEL-03-02-DEP-005 | ANCHOR | UPSTREAM | OTHER | SOW-038 Thin TurnEngine and route extraction | ACTIVE |
| DEL-03-02-DEP-006 | EXECUTION | UPSTREAM | INTERFACE | DEL-03-01 AgentEnginePort and Engine Conformance Suite | ACTIVE |
| DEL-03-02-DEP-007 | EXECUTION | UPSTREAM | INTERFACE | DEL-05-02 HarnessEvent Schema and Append-Only JSONL | ACTIVE |
| DEL-03-02-DEP-008 | EXECUTION | DOWNSTREAM | INTERFACE | DEL-03-03 Harness API and SSE Compatibility Adapter | ACTIVE |
| DEL-03-02-DEP-009 | EXECUTION | DOWNSTREAM | INTERFACE | DEL-03-04 Interrupt Cancel and Terminal Outcome Handling | ACTIVE |
| DEL-03-02-DEP-010 | EXECUTION | DOWNSTREAM | ENABLES | DEL-09-03 Unit and Integration Test Expansion | ACTIVE |

## Lifecycle Summary

| Field | Count |
|---|---:|
| ACTIVE | 10 |
| RETIRED | 0 |
| SatisfactionStatus=PENDING | 10 |
| SatisfactionStatus=TBD | 0 |
| ProposedMaturity=TBD | 10 |

No `[WARNING] FLOATING_NODE` condition: one ACTIVE `ANCHOR` / `IMPLEMENTS_NODE` row exists.

No `[WARNING] AMBIGUOUS_ANCHOR` condition: exactly one ACTIVE `ANCHOR` / `IMPLEMENTS_NODE` row exists.

## Run History

| Timestamp | Mode | Strictness | Decomposition Status | ACTIVE Rows | Warnings |
|---|---|---|---|---:|---|
| 2026-05-20 19:30 | UPDATE | CONSERVATIVE | available: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | 10 | SOURCE_STATE; TBD_IMPLEMENTATION_PATHS; ID_FORMAT_TOOL_MISMATCH |
