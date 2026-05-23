# Dependencies: DEL-08-01 Instruction Root Packaging and Agent Conformance

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
- 2026-05-20 dependency-extract run used RuntimeOverrides: `SCOPE=DEL-08-01`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Run root: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution`.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (located and read).
- Source docs scanned: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority. `_SEMANTIC.md` and `_STATUS.md` were intentionally not read or consumed per human ruling and write restrictions.
- Anchor doc selection: `Datasheet.md` with `_CONTEXT.md` and decomposition cross-checks.
- Execution doc order: `Procedure.md`, `Guidance.md`, `Specification.md`, `Datasheet.md`, `_REFERENCES.md`.
- Conservative extraction emitted no downstream deliverable edges because local evidence names DEL-08-04 and DEL-08-05 only as out-of-scope/boundary owners, not accepted handoff targets.
- Implementation details for validator path, test framework, fixture path, CI/local command, and output artifact location remain `TBD`; no dependency target was invented for those unresolved choices.
- `[WARNING] SOURCE_HASH_MISMATCH`: `REF-006` (`docs/PRD.md`) has `HASH_MISMATCH` in `_REFERENCES.md`; row DEP-DEL-08-01-012 preserves this as a source warning with `Confidence=MEDIUM`.
- `[WARNING] UNRESOLVED_TARGET`: row DEP-DEL-08-01-015 records the explicitly required current instruction-root source tree, but the stable target location is unresolved and remains `UNKNOWN`/`TBD`.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` parent anchor was extracted.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` parent anchor was extracted.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1

| Metric | Count |
|---|---:|
| Total rows | 15 |
| ACTIVE rows | 15 |
| RETIRED rows | 0 |
| ANCHOR rows | 6 |
| EXECUTION rows | 9 |
| Parent anchors (`IMPLEMENTS_NODE`) | 1 |
| Trace anchors (`TRACES_TO_REQUIREMENT`) | 5 |
| Upstream document prerequisites | 8 |
| Upstream unresolved prerequisites | 1 |

| DependencyID | Class | Type | Direction | Target | Status | Satisfaction |
|---|---|---|---|---|---|---|
| DEP-DEL-08-01-001 | ANCHOR | OTHER | UPSTREAM | PKG-08 | ACTIVE | SATISFIED |
| DEP-DEL-08-01-002 | ANCHOR | OTHER | UPSTREAM | SOW-030 | ACTIVE | SATISFIED |
| DEP-DEL-08-01-003 | ANCHOR | OTHER | UPSTREAM | SOW-031 | ACTIVE | SATISFIED |
| DEP-DEL-08-01-004 | ANCHOR | OTHER | UPSTREAM | SOW-073 | ACTIVE | SATISFIED |
| DEP-DEL-08-01-005 | ANCHOR | OTHER | UPSTREAM | OBJ-007 | ACTIVE | SATISFIED |
| DEP-DEL-08-01-006 | ANCHOR | OTHER | UPSTREAM | OBJ-008 | ACTIVE | SATISFIED |
| DEP-DEL-08-01-007 | EXECUTION | PREREQUISITE | UPSTREAM | REF-001 `docs/DIRECTIVE.md` | ACTIVE | PENDING |
| DEP-DEL-08-01-008 | EXECUTION | PREREQUISITE | UPSTREAM | REF-002 `docs/CONTRACT.md` | ACTIVE | PENDING |
| DEP-DEL-08-01-009 | EXECUTION | PREREQUISITE | UPSTREAM | REF-003 `docs/SPEC.md` | ACTIVE | PENDING |
| DEP-DEL-08-01-010 | EXECUTION | PREREQUISITE | UPSTREAM | REF-004 `docs/TYPES.md` | ACTIVE | PENDING |
| DEP-DEL-08-01-011 | EXECUTION | PREREQUISITE | UPSTREAM | REF-005 `docs/PLAN.md` | ACTIVE | PENDING |
| DEP-DEL-08-01-012 | EXECUTION | PREREQUISITE | UPSTREAM | REF-006 `docs/PRD.md` | ACTIVE | PENDING |
| DEP-DEL-08-01-013 | EXECUTION | PREREQUISITE | UPSTREAM | REF-007 `AGENT_SOFTWARE_DECOMP.md` | ACTIVE | PENDING |
| DEP-DEL-08-01-014 | EXECUTION | PREREQUISITE | UPSTREAM | DEC-004 decomposition v3.2 | ACTIVE | PENDING |
| DEP-DEL-08-01-015 | EXECUTION | PREREQUISITE | UPSTREAM | TBD current instruction-root source tree | ACTIVE | PENDING |

## Run History

| Timestamp | Mode | Strictness | Decomposition status | Warnings | ACTIVE rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:54:20-0600 | UPDATE | CONSERVATIVE | Located and read | SOURCE_HASH_MISMATCH for REF-006; UNRESOLVED_TARGET for instruction-root source tree | 15 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 15 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 6 |
| PENDING | 9 |

## Downstream Handoff Notes

Not populated because `CONSUMER_CONTEXT=NONE`.
