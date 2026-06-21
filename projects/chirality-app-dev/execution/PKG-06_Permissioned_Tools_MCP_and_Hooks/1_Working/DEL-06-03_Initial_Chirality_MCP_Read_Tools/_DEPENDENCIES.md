# Dependencies: DEL-06-03 Initial Chirality MCP Read Tools

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

## Current ADQ-11 Reconciliation Note

ADQ-11/D-APP-43 updates the active structured register. `DEP-06-03-005` is now
`SATISFIED` because REF-002/REF-003 remain `MATCH` and REF-006 `docs/PRD.md` is
`MATCH` under the D-APP-38 authority corpus v2. Historical 2026-05-20 run warnings
remain extraction history and no longer describe the active source-state posture.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 TASK + dependency-extract ran in `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Source selection: anchor document `Datasheet.md`; execution documents `Procedure.md`, `Specification.md`, and `Guidance.md`; supporting context `_CONTEXT.md`, `_REFERENCES.md`, existing `_DEPENDENCIES.md`, and decomposition authority.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment skipped; `_SEMANTIC.md` was not read or consumed.
- Existing `Dependencies.csv`: absent before this run; no rows were retired.
- [HISTORICAL WARNING] SOURCE_STATE: the 2026-05-20 extraction saw REF-006 as `HASH_MISMATCH`; ADQ-11 records the current REF-006 state as `MATCH` under D-APP-38 corpus v2, and `DEP-06-03-005` is now `SATISFIED`.
- [WARNING] TARGET_UNRESOLVED: status lifecycle API owner is explicit in source text but not resolved to a deliverable/API identifier in accessible evidence.
- [WARNING] TARGET_UNRESOLVED: Chirality runtime event path is explicit in source text but final active implementation owner is conditional/TBD in accessible evidence.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1

| DependencyID | Class | Type | Direction | Target | Status |
|---|---|---|---|---|---|
| DEP-06-03-001 | ANCHOR | OTHER | UPSTREAM | PKG-06 Permissioned Tools, MCP, and Hooks | ACTIVE |
| DEP-06-03-002 | ANCHOR | OTHER | UPSTREAM | SOW-048 Chirality MCP descriptors | ACTIVE |
| DEP-06-03-003 | ANCHOR | OTHER | UPSTREAM | SOW-050 Read tools before writes/bash | ACTIVE |
| DEP-06-03-004 | EXECUTION | PREREQUISITE | UPSTREAM | Decomposition v3.2 document | ACTIVE |
| DEP-06-03-005 | EXECUTION | PREREQUISITE | UPSTREAM | MCP tools and permissions source contracts | ACTIVE |
| DEP-06-03-006 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-01 ChiralityPermissionOverlay and Mode Mapping | ACTIVE |
| DEP-06-03-007 | EXECUTION | INTERFACE | UPSTREAM | DEL-07-05 Dependencies.csv v3.1 Reader Writer and Linter | ACTIVE |
| DEP-06-03-008 | EXECUTION | INTERFACE | UPSTREAM | UNKNOWN/TBD status lifecycle API owner | ACTIVE |
| DEP-06-03-009 | EXECUTION | INTERFACE | UPSTREAM | UNKNOWN/TBD Chirality runtime event path | ACTIVE |

Counts:

- Total rows: 9
- By class: ANCHOR=3, EXECUTION=6
- By type: OTHER=3, PREREQUISITE=2, INTERFACE=4
- By status: ACTIVE=9
- Parent anchor check: PASS (one ACTIVE `IMPLEMENTS_NODE` row)

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 9 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 4 |
| TBD | 5 |

Open dependency closure items:

- `DEP-06-03-005`: source contracts remain active and are source-state satisfied under D-APP-38 corpus v2.
- `DEP-06-03-006`: permission overlay integration target is known (`DEL-06-01`), but satisfaction remains `TBD`.
- `DEP-06-03-007`: dependency reader behavior must align with `DEL-07-05`; satisfaction remains `TBD`.
- `DEP-06-03-008`: status lifecycle API owner remains `UNKNOWN/TBD`.
- `DEP-06-03-009`: runtime event path owner/availability remains `UNKNOWN/TBD`.

## Run History

- 2026-05-20 19:47 - `TASK + dependency-extract`; mode `UPDATE`; strictness `CONSERVATIVE`; decomposition available; created `Dependencies.csv` with 9 ACTIVE rows. Historical warnings: PRD hash mismatch later reconciled by D-APP-38 corpus v2, unresolved status lifecycle API owner, unresolved/conditional runtime event path.
