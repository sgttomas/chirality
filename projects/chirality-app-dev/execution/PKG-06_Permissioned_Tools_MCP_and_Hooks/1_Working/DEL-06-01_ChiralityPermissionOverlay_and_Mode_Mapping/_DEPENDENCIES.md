# Dependencies: DEL-06-01 ChiralityPermissionOverlay and Mode Mapping

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

## Extracted Dependency Register

Register: `Dependencies.csv` v3.1

| Metric | Count |
|---|---:|
| Total rows | 14 |
| ACTIVE rows | 14 |
| RETIRED rows | 0 |
| ANCHOR rows | 5 |
| EXECUTION rows | 9 |

| DependencyClass | DependencyType | Status | Count |
|---|---|---|---:|
| ANCHOR | OTHER | ACTIVE | 5 |
| EXECUTION | PREREQUISITE | ACTIVE | 4 |
| EXECUTION | CONSTRAINT | ACTIVE | 1 |
| EXECUTION | INTERFACE | ACTIVE | 4 |

| DependencyID | Class | Type | Direction | TargetType | Target | Status |
|---|---|---|---|---|---|---|
| DEP-06-01-A001 | ANCHOR | OTHER | UPSTREAM | PACKAGE | PKG-06 Permissioned Tools, MCP, and Hooks | ACTIVE |
| DEP-06-01-A002 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-054 Structured permission decisions | ACTIVE |
| DEP-06-01-A003 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-055 Permission modes and deny-first overlay | ACTIVE |
| DEP-06-01-A004 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-056 Tool permission events | ACTIVE |
| DEP-06-01-A005 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-058 Interactive approval through `canUseTool` | ACTIVE |
| DEP-06-01-E001 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-004 `docs/TYPES.md` Section 8 | ACTIVE |
| DEP-06-01-E002 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-002 `docs/CONTRACT.md` Section 1.6 | ACTIVE |
| DEP-06-01-E003 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-003 `docs/SPEC.md` Sections 14 and 15 | ACTIVE |
| DEP-06-01-E004 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-005 `docs/PLAN.md` roadmap sequencing | ACTIVE |
| DEP-06-01-E005 | EXECUTION | CONSTRAINT | UPSTREAM | DOCUMENT | REF-006 `docs/PRD.md` source-state reconciliation | ACTIVE |
| DEP-06-01-E006 | EXECUTION | INTERFACE | UPSTREAM | DELIVERABLE | DEL-06-04 Write/Edit Surface and Path Hooks | ACTIVE |
| DEP-06-01-E007 | EXECUTION | INTERFACE | UPSTREAM | DELIVERABLE | DEL-06-02 SDK Read Tool Surface and Tool Validation | ACTIVE |
| DEP-06-01-E008 | EXECUTION | INTERFACE | UPSTREAM | DELIVERABLE | DEL-06-03 Initial Chirality MCP Read Tools | ACTIVE |
| DEP-06-01-E009 | EXECUTION | INTERFACE | UPSTREAM | UNKNOWN | PKG-05/PKG-03 event writer and session JSONL append API | ACTIVE |

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 TASK dependency-extract run used RuntimeOverrides: `SCOPE=DEL-06-01`, `RUN_ROOT=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution`, `DECOMPOSITION_PATH=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority. `_SEMANTIC.md` was not read or consumed per human ruling.
- Anchor doc selection: `Datasheet.md` plus `_CONTEXT.md` and decomposition traceability fields.
- Execution doc order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- Decomposition validation status: available; parent anchor resolves to `PKG-06`; SOW trace anchors resolve to SOW-054, SOW-055, SOW-056, and SOW-058.
- Parent anchor check: PASS. One ACTIVE `IMPLEMENTS_NODE` anchor exists.
- [WARNING] SOURCE_STATE: `_REFERENCES.md` reports `docs/PRD.md` REF-006 as `HASH_MISMATCH`; PRD-derived details remain warning-qualified until reconciled.
- [WARNING] TARGET_TBD: Event writer/session JSONL append API dependency is explicit in `Procedure.md` as an assumption, but exact target deliverable and call path remain `TBD`; row DEP-06-01-E009 preserves `TargetType=UNKNOWN`.

## Run History

| Timestamp | Mode | Strictness | Decomposition path/status | ACTIVE counts | Warnings |
|---|---|---|---|---|---|
| 2026-05-20T19:41:28-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` / available | 14 total: 5 ANCHOR, 9 EXECUTION | SOURCE_STATE REF-006 HASH_MISMATCH; TARGET_TBD DEP-06-01-E009 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 14 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 5 |
| PENDING | 9 |
