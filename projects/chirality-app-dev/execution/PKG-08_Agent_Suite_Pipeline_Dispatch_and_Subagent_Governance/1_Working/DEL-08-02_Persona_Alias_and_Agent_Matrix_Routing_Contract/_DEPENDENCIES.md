# Dependencies: DEL-08-02 Persona Alias and Agent Matrix Routing Contract

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no declared dependency edges have been accepted by a human.

## Declared Downstream

TBD - no declared dependency edges have been accepted by a human.

## Extracted Dependency Register

`Dependencies.csv` was created in v3.1 format with 13 ACTIVE extracted rows.

| Count | Class | Type | Status | Notes |
|---:|---|---|---|---|
| 6 | ANCHOR | OTHER | ACTIVE | One parent package anchor plus five trace anchors to SOW/objective identifiers. |
| 5 | EXECUTION | PREREQUISITE | ACTIVE | Document prerequisites grounded in deliverable-local source summaries and `_REFERENCES.md`. |
| 2 | EXECUTION | INTERFACE | ACTIVE | Explicit interface boundaries with DEL-04-04 and DEL-08-03. |

### Compact Register

| DependencyID | Class | Type | Direction | TargetType | Target | Status |
|---|---|---|---|---|---|---|
| DEP-08-02-001 | ANCHOR | OTHER | UPSTREAM | PACKAGE | PKG-08 Agent Suite, Pipeline Dispatch, and Subagent Governance | ACTIVE |
| DEP-08-02-002 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-005 Matrix rendering and routing | ACTIVE |
| DEP-08-02-003 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-006 Workbench context | ACTIVE |
| DEP-08-02-004 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | SOW-017 Persona resolution and prompt composition | ACTIVE |
| DEP-08-02-005 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | OBJ-001 Governed local desktop harness objective | ACTIVE |
| DEP-08-02-006 | ANCHOR | OTHER | UPSTREAM | REQUIREMENT | OBJ-007 Agent-suite integrity objective | ACTIVE |
| DEP-08-02-007 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-004 docs/TYPES.md | ACTIVE |
| DEP-08-02-008 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-006 docs/PRD.md | ACTIVE |
| DEP-08-02-009 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-003 docs/SPEC.md | ACTIVE |
| DEP-08-02-010 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-002 docs/CONTRACT.md | ACTIVE |
| DEP-08-02-011 | EXECUTION | PREREQUISITE | UPSTREAM | DOCUMENT | REF-001 docs/DIRECTIVE.md | ACTIVE |
| DEP-08-02-012 | EXECUTION | INTERFACE | DOWNSTREAM | DELIVERABLE | DEL-04-04 PersonaComposer from Instruction Root | ACTIVE |
| DEP-08-02-013 | EXECUTION | INTERFACE | DOWNSTREAM | DELIVERABLE | DEL-08-03 Pipeline Category and Task Scope Dispatch | ACTIVE |

## Run Notes

- Run timestamp: 2026-05-20T20:54:44-0600.
- TaskSkill: `dependency-extract`; mode `UPDATE`; strictness `CONSERVATIVE`; consumer context `NONE`.
- Decomposition authority: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority.
- Human ruling applied: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` is invalid evidence and was not read or consumed.
- Defaults applied: `SOURCE_DOCS=AUTO`, `DOC_ROLE_MAP=DEFAULT`, `ANCHOR_DOC=Datasheet.md`, `EXECUTION_DOC_ORDER=Specification.md -> Guidance.md -> Procedure.md -> _REFERENCES.md`.
- `[WARNING] PRD_HASH_MISMATCH`: `_REFERENCES.md` reports `docs/PRD.md` expected SHA `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34` and observed SHA `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. Rows using REF-006 preserve this warning.
- `[WARNING] TBD_IMPLEMENTATION_PATHS`: exact implementation module paths, fixture filenames, route-state keys, and unknown-alias behavior remain TBD in source documents.
- Non-emitted edge note: shared SOW ownership with DEL-02-01 and DEL-02-02 was not converted into execution edges because the allowed source documents do not state a concrete handoff or interface contract to those deliverables.
- Non-emitted edge note: REF-005 `docs/PLAN.md` and REF-007 `AGENT_SOFTWARE_DECOMP.md` were not emitted as dependency rows because evidence only identifies them as context/method references, not execution prerequisites for this deliverable.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Validator | ACTIVE Rows | Warnings |
|---|---|---|---|---|---:|---|
| 2026-05-20T20:54:44-0600 | UPDATE | CONSERVATIVE | v3.2 found | PASS: 29 columns, 13 rows | 13 | PRD_HASH_MISMATCH; TBD_IMPLEMENTATION_PATHS |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 13 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 6 |
| PENDING | 5 |
| TBD | 2 |

| DependencyClass | Count |
|---|---:|
| ANCHOR | 6 |
| EXECUTION | 7 |

| DependencyType | Count |
|---|---:|
| OTHER | 6 |
| PREREQUISITE | 5 |
| INTERFACE | 2 |
