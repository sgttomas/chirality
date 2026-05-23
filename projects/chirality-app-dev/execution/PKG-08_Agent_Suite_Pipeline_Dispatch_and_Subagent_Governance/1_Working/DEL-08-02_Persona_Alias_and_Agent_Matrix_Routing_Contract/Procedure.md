# Procedure: DEL-08-02 Persona Alias and Agent Matrix Routing Contract

## Purpose

Define the bounded procedure for producing, checking, and using the persona alias and agent matrix routing contract for DEL-08-02.

## Prerequisites

| Prerequisite | Status |
|---|---|
| Deliverable context file `_CONTEXT.md` is available. | Satisfied. |
| Reference record `_REFERENCES.md` is available. | Satisfied. |
| Authoritative sources listed in `_REFERENCES.md` are locally accessible. | Satisfied with PRD hash mismatch warning. |
| Dependency register is available. | Satisfied for extracted rows: `Dependencies.csv` exists with 13 ACTIVE rows; declared human upstream/downstream edges remain TBD. |
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
14. Read the current dependency register when closure or fixture coverage depends on dependency state; do not create or rewrite `Dependencies.csv` during this four-document procedure.
15. When implementation begins, fill F-001 with selected module paths and fixture/test file paths for alias resolver, matrix mapping, route fixtures, and persona resolver.
16. Fill D-001 with the actual route-state or query-parameter keys for selected agent, row, and column after code selects them.
17. Resolve B-001 by recording the governed unknown-alias behavior and adding the matching negative alias resolver test.

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
| Dependency register | Existing `Dependencies.csv` and `_DEPENDENCIES.md` are consumed as evidence; this procedure does not create or rewrite them. |
| P3 evidence capture | F-002 records concrete test result files or command output locations for alias, matrix, route, workbench-context, persona, fallback, unknown-key, and unsupported-option checks. |
| Acceptance transition | E-001 is closed only by refreshed REF-006 hash evidence or human acceptance of the current PRD hash. |

## Records

Required records for this document kit:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_run_records/TASK_RUN_2026-05-20_1614.md`
- `_run_records/TASK_RUN_2026-05-23_W37_four-documents-p3.md`

Future implementation records:

- Alias resolver tests.
- Route fixtures.
- Matrix mapping tests.
- Any human ruling on the PRD expected-hash mismatch.
- F-001 path selections for implementation modules and fixture/test files.
- F-002 evidence artifact names or command output locations.
- X-001 follow-up accepted dependency edge ruling if human-declared upstream/downstream edges change.
