# Dependencies: DEL-02-04 Toolkit Options and Local UI State

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no declared upstream dependency edges have been accepted outside the extracted register.

## Declared Downstream

TBD - no declared downstream dependency edges have been accepted outside the extracted register.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1

| Metric | Count |
|---|---:|
| Total ACTIVE rows | 14 |
| ANCHOR rows | 6 |
| EXECUTION rows | 8 |
| RETIRED rows | 0 |

| DependencyID | Class | Type | Target | Status | Evidence |
|---|---|---|---|---|---|
| DEP-02-04-001 | ANCHOR | OTHER | PKG-02 | ACTIVE | `_CONTEXT.md` > Identity and Package Scope |
| DEP-02-04-002 | ANCHOR | OTHER | SOW-004 | ACTIVE | `Datasheet.md` > Identification |
| DEP-02-04-003 | ANCHOR | OTHER | SOW-008 | ACTIVE | `Datasheet.md` > Identification |
| DEP-02-04-004 | ANCHOR | OTHER | SOW-016 | ACTIVE | `Datasheet.md` > Identification |
| DEP-02-04-005 | ANCHOR | OTHER | OBJ-001 | ACTIVE | `Datasheet.md` > Identification |
| DEP-02-04-006 | ANCHOR | OTHER | OBJ-004 | ACTIVE | `Guidance.md` > Purpose |
| DEP-02-04-007 | EXECUTION | PREREQUISITE | REF-001 `docs/DIRECTIVE.md` | ACTIVE | `Procedure.md` > Prerequisites |
| DEP-02-04-008 | EXECUTION | PREREQUISITE | REF-002 `docs/CONTRACT.md` | ACTIVE | `Procedure.md` > Prerequisites |
| DEP-02-04-009 | EXECUTION | PREREQUISITE | REF-003 `docs/SPEC.md` | ACTIVE | `Procedure.md` > Prerequisites |
| DEP-02-04-010 | EXECUTION | PREREQUISITE | REF-004 `docs/TYPES.md` | ACTIVE | `Procedure.md` > Prerequisites |
| DEP-02-04-011 | EXECUTION | PREREQUISITE | REF-005 `docs/PLAN.md` | ACTIVE | `Procedure.md` > Prerequisites |
| DEP-02-04-012 | EXECUTION | PREREQUISITE | REF-006 `docs/PRD.md` | ACTIVE | `Procedure.md` > Prerequisites |
| DEP-02-04-013 | EXECUTION | PREREQUISITE | DECOMP-v3.2 | ACTIVE | `Procedure.md` > Prerequisites |
| DEP-02-04-014 | EXECUTION | PREREQUISITE | TBD adjacent deliverables | ACTIVE | `Procedure.md` > Prerequisites |

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- TASK + dependency-extract ran on 2026-05-20 with `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, and `CONSUMER_CONTEXT=NONE`.
- Runtime overrides used: `SCOPE=DEL-02-04`; `RUN_ROOT=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution`; `DECOMPOSITION_PATH=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Human ruling honored: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` was not read or consumed.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the specified decomposition authority.
- `Dependencies.csv` did not previously exist in this deliverable folder; all rows in this run are new extracted rows.
- Objective traces `OBJ-001` and `OBJ-004` are encoded with `TargetType=WBS_NODE` because the v3.1 target enum has no `OBJECTIVE` value.
- [WARNING] PRD_HASH_MISMATCH: `_REFERENCES.md` reports REF-006 expected SHA `86cb6f...` and actual SHA `fb1c73...`; PRD-derived dependencies remain active with warning and closure remains pending for that source.
- No `[WARNING] FLOATING_NODE`: one ACTIVE `IMPLEMENTS_NODE` parent anchor was found.
- No `[WARNING] AMBIGUOUS_ANCHOR`: exactly one ACTIVE `IMPLEMENTS_NODE` parent anchor was found.
- No `[WARNING] MISSING_DECOMPOSITION`: the runtime override decomposition file was available and used.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Rows |
|---|---|---|---|---|---:|
| 2026-05-20T19:30:43-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | PRD_HASH_MISMATCH | 14 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 14 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| NOT_APPLICABLE | 6 |
| SATISFIED | 6 |
| PENDING | 1 |
| TBD | 1 |

Closure notes:

- The extracted register is schema-valid and evidence-first, but project-level availability must still wait for FULL_GRAPH cycle checks.
- `DEP-02-04-012` remains `PENDING` because REF-006 has a hash mismatch.
- `DEP-02-04-014` remains `TBD` because the source explicitly leaves adjacent runtime option contracts and permission policy integration points unresolved.
