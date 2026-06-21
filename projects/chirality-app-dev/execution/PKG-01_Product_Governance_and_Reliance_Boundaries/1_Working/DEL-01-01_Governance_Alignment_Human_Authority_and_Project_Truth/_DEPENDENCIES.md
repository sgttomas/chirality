# Dependencies: DEL-01-01 Governance Alignment, Human Authority, and Project Truth

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

See `Dependencies.csv` for the derivative dependency-extract register. No downstream product edge is
accepted by this reconciliation.

## Declared Downstream

No downstream deliverable edge is accepted in the derivative register.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1

| Metric | Count |
|---|---:|
| Total rows | 12 |
| ACTIVE rows | 12 |
| RETIRED rows | 0 |
| ANCHOR rows | 4 |
| EXECUTION rows | 8 |
| Parent anchors (`IMPLEMENTS_NODE`) | 1 |
| Trace anchors (`TRACES_TO_REQUIREMENT`) | 3 |
| Upstream document prerequisites | 8 |

| DependencyID | Class | Type | Direction | Target | Status | Satisfaction |
|---|---|---|---|---|---|---|
| DEP-01-01-001 | ANCHOR | OTHER | UPSTREAM | PKG-01 | ACTIVE | SATISFIED |
| DEP-01-01-002 | ANCHOR | OTHER | UPSTREAM | SOW-074 | ACTIVE | SATISFIED |
| DEP-01-01-003 | ANCHOR | OTHER | UPSTREAM | SOW-075 | ACTIVE | SATISFIED |
| DEP-01-01-004 | ANCHOR | OTHER | UPSTREAM | OBJ-009 | ACTIVE | SATISFIED |
| DEP-01-01-005 | EXECUTION | PREREQUISITE | UPSTREAM | REF-001 `docs/DIRECTIVE.md` | ACTIVE | PENDING |
| DEP-01-01-006 | EXECUTION | PREREQUISITE | UPSTREAM | REF-002 `docs/CONTRACT.md` | ACTIVE | PENDING |
| DEP-01-01-007 | EXECUTION | PREREQUISITE | UPSTREAM | REF-003 `docs/SPEC.md` | ACTIVE | PENDING |
| DEP-01-01-008 | EXECUTION | PREREQUISITE | UPSTREAM | REF-004 `docs/TYPES.md` | ACTIVE | PENDING |
| DEP-01-01-009 | EXECUTION | PREREQUISITE | UPSTREAM | REF-005 `docs/PLAN.md` | ACTIVE | PENDING |
| DEP-01-01-010 | EXECUTION | PREREQUISITE | UPSTREAM | REF-006 `docs/PRD.md` | ACTIVE | PENDING |
| DEP-01-01-011 | EXECUTION | PREREQUISITE | UPSTREAM | REF-007 `AGENT_SOFTWARE_DECOMP.md` | ACTIVE | PENDING |
| DEP-01-01-012 | EXECUTION | PREREQUISITE | UPSTREAM | DEC-001 decomposition v3.2 | ACTIVE | PENDING |

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 dependency-extract run used RuntimeOverrides: `SCOPE=DEL-01-01`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Run root: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution`.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (located and read).
- Source docs scanned: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority. `_SEMANTIC.md` was intentionally not read or consumed per human ruling.
- Anchor doc selection: `Datasheet.md` with `_CONTEXT.md` and decomposition cross-checks.
- Execution doc order: `Guidance.md`, `Procedure.md`, `Specification.md`, `Datasheet.md`, `_REFERENCES.md`.
- Conservative extraction emitted no downstream deliverable edges because the approved local documents state upstream and downstream dependencies are `TBD` and do not identify accepted downstream consumers.
- `[RECONCILED] REF-006`: D-APP-38 corpus `v1` reconciled `docs/PRD.md`; `_REFERENCES.md` now reports `MATCH`. Row `DEP-01-01-010` remains an active prerequisite until dependency/evidence disposition, but it is no longer blocked by a PRD hash mismatch.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` parent anchor was extracted.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` parent anchor was extracted.

## Run History

| Timestamp | Mode | Strictness | Decomposition status | Warnings | ACTIVE rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:24:23-0600 | UPDATE | CONSERVATIVE | Located and read | SOURCE_HASH_MISMATCH for REF-006 at extraction time; later reconciled by D-APP-38 corpus `v1` | 12 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 12 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 4 |
| PENDING | 8 |

## Downstream Handoff Notes

Not populated because `CONSUMER_CONTEXT=NONE`.
