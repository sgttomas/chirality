# Dependencies: DEL-06-02 SDK Read Tool Surface and Tool Validation

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
- 2026-05-20 TASK dependency-extract run used `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Semantic lensing and P3 enrichment were skipped by human ruling; `_SEMANTIC.md` was not read or consumed.
- Decomposition authority was available and used for anchor validation and canonical target labels.
- Anchor document selected by AUTO/default heuristic: `Datasheet.md` with confirmation from `_CONTEXT.md` and decomposition authority.
- Execution document order selected by AUTO/default heuristic: `Procedure.md`, `Guidance.md`, `Specification.md`, `Datasheet.md`.
- [WARNING] PRD_HASH_MISMATCH: `_REFERENCES.md` reports `docs/PRD.md` REF-006 as `HASH_MISMATCH`; PRD-derived details remain warning-qualified until source-state reconciliation.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` parent anchor is present.
- No `[WARNING] AMBIGUOUS_ANCHOR`: only one ACTIVE `IMPLEMENTS_NODE` parent anchor is present.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1

| Count | Value |
|---:|---|
| Total rows | 11 |
| ACTIVE rows | 11 |
| RETIRED rows | 0 |
| ANCHOR rows | 4 |
| EXECUTION rows | 7 |

| DependencyID | Class | Type / Anchor | Direction | Target | Status |
|---|---|---|---|---|---|
| DEP-06-02-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | PKG-06 Permissioned Tools, MCP, and Hooks | ACTIVE |
| DEP-06-02-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | SOW-047 Tool option mapping | ACTIVE |
| DEP-06-02-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | SOW-049 Deterministic tool surface | ACTIVE |
| DEP-06-02-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | SOW-050 Read tools before writes/bash | ACTIVE |
| DEP-06-02-005 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-06-01 ChiralityPermissionOverlay and Mode Mapping | ACTIVE |
| DEP-06-02-006 | EXECUTION | INTERFACE | UPSTREAM | DEL-06-03 Initial Chirality MCP Read Tools | ACTIVE |
| DEP-06-02-007 | EXECUTION | PREREQUISITE | UPSTREAM | REF-003 `docs/SPEC.md` | ACTIVE |
| DEP-06-02-008 | EXECUTION | PREREQUISITE | UPSTREAM | REF-004 `docs/TYPES.md` | ACTIVE |
| DEP-06-02-009 | EXECUTION | PREREQUISITE | UPSTREAM | REF-002 `docs/CONTRACT.md` | ACTIVE |
| DEP-06-02-010 | EXECUTION | PREREQUISITE | UPSTREAM | REF-005 `docs/PLAN.md` | ACTIVE |
| DEP-06-02-011 | EXECUTION | CONSTRAINT | UPSTREAM | REF-006 `docs/PRD.md` | ACTIVE |

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:47:21-06:00 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` available | PRD_HASH_MISMATCH | 11 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 11 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| TBD | 11 |

Closure state: dependency register populated but not closed at project FULL_GRAPH level until aggregation/cycle checks are run.
