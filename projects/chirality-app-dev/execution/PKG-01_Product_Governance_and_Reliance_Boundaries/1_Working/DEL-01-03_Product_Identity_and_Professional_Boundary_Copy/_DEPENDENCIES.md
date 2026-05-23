# Dependencies: DEL-01-03 Product Identity and Professional Boundary Copy

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
- 2026-05-20 TASK + dependency-extract ran in `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`.
- Runtime override `SCOPE=DEL-01-03`; `RUN_ROOT=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution`.
- Decomposition authority used: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`; anchor validation was available.
- Source document defaults: `SOURCE_DOCS=AUTO`, `DOC_ROLE_MAP=DEFAULT`, `ANCHOR_DOC=Datasheet.md`, `EXECUTION_DOC_ORDER=Procedure.md, Guidance.md, Specification.md, Datasheet.md`.
- Human ruling applied: semantic lensing and P3 enrichment are skipped; existing `_SEMANTIC.md` output is invalid evidence and was not read or consumed.
- Conservative extraction emitted only explicit anchors and explicit upstream information-flow prerequisites. No inferred cross-deliverable execution edges were emitted.
- `[WARNING] SOURCE_HASH_MISMATCH`: `_REFERENCES.md` records `REF-006` / `docs/PRD.md` as `HASH_MISMATCH`; retained as an active prerequisite because `Procedure.md` says to use PRD with the hash mismatch warning.

## Extracted Dependency Register

Structured register: `Dependencies.csv` v3.1

| Metric | Count |
|---|---:|
| Total rows | 12 |
| ACTIVE rows | 12 |
| RETIRED rows | 0 |
| ANCHOR rows | 5 |
| EXECUTION rows | 7 |

| DependencyID | Class | Type | Direction | Target | Status |
|---|---|---|---|---|---|
| DEP-DEL-01-03-001 | ANCHOR | OTHER | UPSTREAM | PKG-01 Product Governance and Reliance Boundaries | ACTIVE |
| DEP-DEL-01-03-002 | ANCHOR | OTHER | UPSTREAM | SOW-071 Domain professional boundary | ACTIVE |
| DEP-DEL-01-03-003 | ANCHOR | OTHER | UPSTREAM | SOW-074 Human authority/professional boundaries | ACTIVE |
| DEP-DEL-01-03-004 | ANCHOR | OTHER | UPSTREAM | OBJ-009 Governance identity objective | ACTIVE |
| DEP-DEL-01-03-005 | ANCHOR | OTHER | UPSTREAM | OBJ-010 Future domain-engine compatibility objective | ACTIVE |
| DEP-DEL-01-03-006 | EXECUTION | PREREQUISITE | UPSTREAM | REF-001 `docs/DIRECTIVE.md` | ACTIVE |
| DEP-DEL-01-03-007 | EXECUTION | PREREQUISITE | UPSTREAM | REF-002 `docs/CONTRACT.md` | ACTIVE |
| DEP-DEL-01-03-008 | EXECUTION | PREREQUISITE | UPSTREAM | REF-003 `docs/SPEC.md` | ACTIVE |
| DEP-DEL-01-03-009 | EXECUTION | PREREQUISITE | UPSTREAM | REF-004 `docs/TYPES.md` | ACTIVE |
| DEP-DEL-01-03-010 | EXECUTION | PREREQUISITE | UPSTREAM | REF-005 `docs/PLAN.md` | ACTIVE |
| DEP-DEL-01-03-011 | EXECUTION | PREREQUISITE | UPSTREAM | REF-006 `docs/PRD.md` | ACTIVE |
| DEP-DEL-01-03-012 | EXECUTION | PREREQUISITE | UPSTREAM | DECOMP-v3.2 decomposition authority | ACTIVE |

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE counts |
|---|---|---|---|---|---|
| 2026-05-20T19:24:25-0600 | UPDATE | CONSERVATIVE | `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` available | `SOURCE_HASH_MISMATCH` for REF-006; `_SEMANTIC.md` ignored by ruling | ANCHOR 5; EXECUTION 7; TOTAL 12 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 12 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| TBD | 12 |

Closure state: dependency register created and schema-valid; satisfaction lifecycle remains `TBD` pending downstream FULL_GRAPH/cycle checks and any human closure decisions.
