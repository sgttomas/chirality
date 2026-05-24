# Dependencies: DEL-08-03 Pipeline Category and Task Scope Dispatch

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

## Extracted Dependency Register

Register: `Dependencies.csv` v3.1

| Metric | Count |
|---|---:|
| Total rows | 10 |
| ACTIVE rows | 10 |
| RETIRED rows | 0 |
| ANCHOR rows | 5 |
| EXECUTION rows | 5 |

| DependencyID | Class | Type / Anchor | Direction | Target | Status |
|---|---|---|---|---|---|
| DEP-08-03-001 | ANCHOR | IMPLEMENTS_NODE | UPSTREAM | DEL-08-03 Pipeline Category and Task Scope Dispatch | ACTIVE |
| DEP-08-03-002 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | SOW-007 Pipeline selectors | ACTIVE |
| DEP-08-03-003 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | SOW-026 Metadata files and document kit | ACTIVE |
| DEP-08-03-004 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OBJ-001 governed local desktop harness/operator workflow objective | ACTIVE |
| DEP-08-03-005 | ANCHOR | TRACES_TO_REQUIREMENT | UPSTREAM | OBJ-007 agent-suite integrity/governed delegation objective | ACTIVE |
| DEP-08-03-006 | EXECUTION | PREREQUISITE | UPSTREAM | REF-004 `docs/TYPES.md` Section 4.4 vocabulary | ACTIVE |
| DEP-08-03-007 | EXECUTION | INTERFACE | UPSTREAM | REF-003 `docs/SPEC.md` Section 17.2 working-root scope API | ACTIVE |
| DEP-08-03-008 | EXECUTION | CONSTRAINT | UPSTREAM | REF-002 `docs/CONTRACT.md` Section 1.8 governance invariants | ACTIVE |
| DEP-08-03-009 | EXECUTION | PREREQUISITE | UPSTREAM | REF-006 `docs/PRD.md` Section 8.2 product requirements | ACTIVE |
| DEP-08-03-010 | EXECUTION | HANDOVER | DOWNSTREAM | Pipeline selector, knowledge-type discovery, and disabled option tests | ACTIVE |

## Run Notes — 2026-05-20 20:54

- Mode: `UPDATE`
- Strictness: `CONSERVATIVE`
- Consumer context: `NONE`
- Decomposition path: `/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- Decomposition status: found and used for anchor validation.
- Anchor doc: `Datasheet.md` plus `_CONTEXT.md` for identity confirmation.
- Execution docs scanned: `Specification.md`, `Guidance.md`, `Procedure.md`, `_REFERENCES.md`, existing `_DEPENDENCIES.md`.
- Human ruling applied: semantic lensing and P3 enrichment are skipped; `_SEMANTIC.md` was not read and was not consumed as evidence.
- No existing `Dependencies.csv` was present, so all extracted rows were newly created.
- `[WARNING] PRD_HASH_MISMATCH`: `_REFERENCES.md` records REF-006 expected SHA `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34` and actual SHA `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`; PRD-derived edge confidence is capped at `MEDIUM`.
- `[WARNING] UNKNOWN_DOWNSTREAM_TARGET`: downstream test/record handoff is explicit, but the consumer deliverable is not identified in the allowed evidence set; target remains `UNKNOWN`/`TBD`.

## Run History

| Timestamp | Mode | Strictness | Decomposition Status | Warnings | ACTIVE Count |
|---|---|---|---|---|---:|
| 2026-05-20 20:54 | UPDATE | CONSERVATIVE | found | PRD_HASH_MISMATCH; UNKNOWN_DOWNSTREAM_TARGET | 10 |

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 10 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| TBD | 10 |
