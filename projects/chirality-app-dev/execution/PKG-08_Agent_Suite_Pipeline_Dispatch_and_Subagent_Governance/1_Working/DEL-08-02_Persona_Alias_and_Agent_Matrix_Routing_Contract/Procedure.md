# Procedure: DEL-08-02 Persona Alias and Agent Matrix Routing Contract

## Purpose

Define the bounded procedure for producing, checking, and using the persona alias and agent matrix routing contract for DEL-08-02.

## Prerequisites

| Prerequisite | Status |
|---|---|
| Deliverable context file `_CONTEXT.md` is available. | Satisfied. |
| Reference record `_REFERENCES.md` is available. | Satisfied. |
| Authoritative sources listed in `_REFERENCES.md` are locally accessible. | Satisfied with PRD hash mismatch warning. |
| Declared upstream dependencies are available. | TBD; `_DEPENDENCIES.md` has no accepted extracted edges yet. |
| ResponsibleParty assigned. | TBD. |
| Exact implementation module paths for alias resolver, matrix fixture, and route tests are known. | TBD. |

## Steps

1. Read `_CONTEXT.md` and confirm the deliverable identity is DEL-08-02 with ResponsibleParty left as TBD.
2. Read `_REFERENCES.md` and record source status, including the PRD hash mismatch warning.
3. Read the DEL-08-02 decomposition entry and confirm the deliverable scope, anticipated artifacts, SOW links, and objectives.
4. Extract the canonical alias map from `docs/TYPES.md` Section 3.4 and cross-check against `docs/PRD.md` FR-026.
5. Extract the canonical matrix row, column, and cell vocabulary from `docs/TYPES.md` Section 4.
6. Extract matrix routing acceptance from `docs/PRD.md` Section 7.2 and FR-008.
7. Extract WORKBENCH context behavior from `docs/PRD.md` Section 7.4 and FR-009.
8. Extract persona resolution and fallback requirements from `docs/PRD.md` FR-023 through FR-026 and `docs/SPEC.md` Section 13.
9. Build or update alias resolver tests for the five sourced aliases.
10. Build or update matrix mapping tests for the canonical 3x4 row/column vocabulary.
11. Build or update route fixtures proving row-to-surface routing.
12. Build or update persona resolver tests for `agents/AGENT_*.md` lookup and `PERSONA_NOT_FOUND`.
13. Mark any unsupported behavior as TBD rather than inventing requirements.
14. Defer dependency extraction until the authorized `TASK + dependency-extract` phase; do not create `Dependencies.csv` in this procedure.

## Verification

| Check | Expected Result |
|---|---|
| Alias map completeness | All five sourced aliases are covered by tests. |
| Alias map conservatism | No unsourced aliases are asserted as requirements. |
| Matrix vocabulary | Rows and columns match `docs/TYPES.md` and PRD FR-007. |
| Route destination | NORMATIVE/EVALUATIVE route to WORKBENCH; OPERATIVE routes to PIPELINE. |
| Workbench context | Selected agent, row, and column are preserved from route state or query parameters. |
| Persona lookup | Canonical persona names resolve to `agents/AGENT_*.md`; missing personas return `PERSONA_NOT_FOUND`. |
| Unknown fields | Unknown runtime option keys warn rather than mutating behavior. |
| Source warnings | PRD hash mismatch is recorded as a warning, not silently ignored. |
| Dependency deferral | No `Dependencies.csv` is created by this deliverable-document run. |

## Records

Required records for this P1/P2 run:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` updated to `INITIALIZED` only after the four required documents are written and non-empty.
- `_run_records/TASK_RUN_2026-05-20_1614.md`

Future implementation records:

- Alias resolver tests.
- Route fixtures.
- Matrix mapping tests.
- Any human ruling on the PRD expected-hash mismatch.
