# Dependencies: DEL-05-05 ToolResultStore and Session Artifacts

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

- `docs/SPEC.md` Sections 8-9 for session layout, `HarnessEvent`, and JSONL append/replay behavior.
- `docs/CONTRACT.md` K-EVENT and K-KEY invariants for audit, replay, redaction, and artifact constraints.
- `docs/PRD.md` Sections 10.4-10.5 and NFR-017 from the D-APP-38 authority corpus v2 (`REF-006` = `MATCH`).
- D-APP-42 for SHA-256 artifact checksums and session-lifetime retention policy.

## Declared Downstream

No downstream dependency row is active in this DEL-05-05-local register. DEL-05-04 consumes artifact-link projections separately.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 19:41 dependency-extract run used `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and decomposition authority `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling applied: semantic lensing and P3 enrichment were skipped; `_SEMANTIC.md` was not read or consumed as evidence.
- Anchor doc selection: `Datasheet.md` and `_CONTEXT.md` for deliverable identity/traceability, validated against the decomposition authority.
- Execution doc order: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- [RETIRED] SOURCE_STATE_PRD_HASH_MISMATCH: D-APP-38 authority corpus v2 and `_REFERENCES.md` now report `docs/PRD.md` REF-006 as `MATCH`.
- [WARNING] UNKNOWN_TARGETS: Objective IDs are anchored with `TargetType=UNKNOWN` because the v3.1 schema has no `OBJECTIVE` target enum.
- [RETIRED] TBD_POLICY_INPUTS: ADQ-10 records the `ToolResultStore` artifact implementation path and D-APP-42 checksum/retention policy. Thresholds, preview length, and artifact naming remain the existing descriptor/artifact-writer policy and are unchanged by D-APP-42.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` anchor exists.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` anchor exists.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1.

| Metric | Count |
|---|---:|
| Total rows | 10 |
| ACTIVE rows | 10 |
| RETIRED rows | 0 |
| ANCHOR rows | 5 |
| EXECUTION rows | 5 |

| DependencyID | Class | Type | Target | Status | Satisfaction |
|---|---|---|---|---|---|
| DEP-05-05-001 | ANCHOR | OTHER / IMPLEMENTS_NODE | PKG-05 Session Audit, Replay, and Tool Result Records | ACTIVE | SATISFIED |
| DEP-05-05-002 | ANCHOR | OTHER / TRACES_TO_REQUIREMENT | SOW-053 Deterministic event ordering under tool concurrency | ACTIVE | SATISFIED |
| DEP-05-05-003 | ANCHOR | OTHER / TRACES_TO_REQUIREMENT | SOW-059 Tool result budgets and artifacts | ACTIVE | SATISFIED |
| DEP-05-05-004 | ANCHOR | OTHER / TRACES_TO_REQUIREMENT | OBJ-003 Audit and session objective | ACTIVE | SATISFIED |
| DEP-05-05-005 | ANCHOR | OTHER / TRACES_TO_REQUIREMENT | OBJ-005 Tool governance objective | ACTIVE | SATISFIED |
| DEP-05-05-006 | EXECUTION | PREREQUISITE | REF-003 `docs/SPEC.md` | ACTIVE | SATISFIED |
| DEP-05-05-007 | EXECUTION | PREREQUISITE | REF-002 `docs/CONTRACT.md` | ACTIVE | SATISFIED |
| DEP-05-05-008 | EXECUTION | PREREQUISITE | REF-006 `docs/PRD.md` | ACTIVE | SATISFIED |
| DEP-05-05-009 | EXECUTION | PREREQUISITE | ToolResultStore implementation location | ACTIVE | SATISFIED |
| DEP-05-05-010 | EXECUTION | CONSTRAINT | Output budget policy parameters | ACTIVE | SATISFIED |

## Lifecycle Summary

| Class | Type | Status | Count |
|---|---|---|---:|
| ANCHOR | OTHER | ACTIVE | 5 |
| EXECUTION | PREREQUISITE | ACTIVE | 4 |
| EXECUTION | CONSTRAINT | ACTIVE | 1 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 10 |

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE rows |
|---|---|---|---|---|---:|
| 2026-05-20 19:41 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` validated | SOURCE_STATE, UNKNOWN_TARGETS, TBD_POLICY_INPUTS | 10 |
| 2026-06-21 ADQ-10 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` unchanged | SOURCE_STATE retired; TBD_POLICY_INPUTS retired for ADQ-10; UNKNOWN_TARGETS retained by schema | 10 |
