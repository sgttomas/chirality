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

## Current ADQ-11 Reconciliation Note

ADQ-11/D-APP-43 updates the active structured register. `DEP-06-01-010` is now
`SATISFIED` because `_REFERENCES.md` records REF-006 `docs/PRD.md` as `MATCH` under
the D-APP-38 authority corpus v2. Historical 2026-05-20 run warnings remain extraction
history and no longer describe the active source-state posture.

## Extracted Dependency Register

Register: `Dependencies.csv` v3.1

| Metric | Count |
|---|---:|
| Total rows | 14 |
| ACTIVE rows | 11 |
| RETIRED rows | 3 |
| ANCHOR rows | 5 |
| EXECUTION rows | 9 |

| DependencyClass | DependencyType | Status | Count |
|---|---|---|---:|
| ANCHOR | OTHER | ACTIVE | 5 |
| EXECUTION | PREREQUISITE | ACTIVE | 4 |
| EXECUTION | CONSTRAINT | ACTIVE | 1 |
| EXECUTION | INTERFACE | ACTIVE | 1 |
| EXECUTION | INTERFACE | RETIRED | 3 |

| DependencyID | Class | Type | Direction | TargetType | Target | Status |
|---|---|---|---|---|---|---|
| DEP-06-01-001 | ANCHOR | OTHER | UPSTREAM | PACKAGE | PKG-06 Permissioned Tools, MCP, and Hooks | ACTIVE |
| DEP-06-01-002 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-054 Structured permission decisions | ACTIVE |
| DEP-06-01-003 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-055 Permission modes and capability policy with explicit hard-deny precedence | ACTIVE |
| DEP-06-01-004 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-056 Tool permission events | ACTIVE |
| DEP-06-01-005 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-058 Interactive approval through `canUseTool` | ACTIVE |
| DEP-06-01-006 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-004 `docs/TYPES.md` Section 8 | ACTIVE |
| DEP-06-01-007 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-002 `docs/CONTRACT.md` Section 1.6 | ACTIVE |
| DEP-06-01-008 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-003 `docs/SPEC.md` Sections 14 and 15 | ACTIVE |
| DEP-06-01-009 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-005 `docs/PLAN.md` roadmap sequencing | ACTIVE |
| DEP-06-01-010 | EXECUTION | CONSTRAINT | UPSTREAM | DOCUMENT | REF-006 `docs/PRD.md` source-state reconciliation | ACTIVE |
| DEP-06-01-011 | EXECUTION | INTERFACE | UPSTREAM | DELIVERABLE | DEL-06-04 Write/Edit Surface and Path Hooks | ACTIVE |
| DEP-06-01-012 | EXECUTION | INTERFACE | UPSTREAM | DELIVERABLE | DEL-06-02 SDK Read Tool Surface and Tool Validation | ACTIVE |
| DEP-06-01-013 | EXECUTION | INTERFACE | UPSTREAM | DELIVERABLE | DEL-06-03 Initial Chirality MCP Read Tools | ACTIVE |
| DEP-06-01-014 | EXECUTION | INTERFACE | UPSTREAM | UNKNOWN | PKG-05/PKG-03 event writer and session JSONL append API | ACTIVE |

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 TASK dependency-extract run used RuntimeOverrides: `SCOPE=DEL-06-01`, `RUN_ROOT=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution`, `DECOMPOSITION_PATH=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority. `_SEMANTIC.md` was not read or consumed per human ruling.
- Anchor doc selection: `Datasheet.md` plus `_CONTEXT.md` and decomposition traceability fields.
- Execution doc order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- Decomposition validation status: available; parent anchor resolves to `PKG-06`; SOW trace anchors resolve to SOW-054, SOW-055, SOW-056, and SOW-058.
- Parent anchor check: PASS. One ACTIVE `IMPLEMENTS_NODE` anchor exists.
- [HISTORICAL WARNING] SOURCE_STATE: the 2026-05-20 extraction saw REF-006 as `HASH_MISMATCH`; ADQ-11 records the current REF-006 state as `MATCH` under D-APP-38 corpus v2, and `DEP-06-01-010` is now `SATISFIED`.
- [WARNING] TARGET_TBD: Event writer/session JSONL append API dependency is explicit in `Procedure.md` as an assumption, but exact target deliverable and call path remain `TBD`; row DEP-06-01-014 preserves `TargetType=UNKNOWN`.

## Run History

| Timestamp | Mode | Strictness | Decomposition path/status | ACTIVE counts | Warnings |
|---|---|---|---|---|---|
| 2026-05-20T19:41:28-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` / available | 14 total: 5 ANCHOR, 9 EXECUTION | Historical SOURCE_STATE REF-006 HASH_MISMATCH, later reconciled by D-APP-38 corpus v2; TARGET_TBD DEP-06-01-014 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 11 |
| RETIRED | 3 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 6 |
| PENDING | 5 |
| NOT_APPLICABLE | 3 |

## D-APP-56 R5 P45 current register summary (2026-07-12)

- **Source:** UPD-127
- **Current counts:** ACTIVE 11; RETIRED 3; NOT_APPLICABLE=3; PENDING=5; SATISFIED=6.
- **Correction:** DEP-06-01-014 now names the appendHarnessEvent call path; upstream deliverable identity remains unassigned.
- Earlier extraction and reconciliation history is preserved as dated evidence; this block is the current structured-register mirror.
