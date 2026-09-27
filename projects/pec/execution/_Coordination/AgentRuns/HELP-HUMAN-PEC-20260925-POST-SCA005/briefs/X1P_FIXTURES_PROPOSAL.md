# Brief X1P — X1 P1 fixture suites for DEL-02-03, DEL-02-08 and DEL-02-09 (provisional D-PEC-106) — WORKING_ITEMS preparation

- **Parent:** HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node X1.
- **Role:** WORKING_ITEMS (Type 1).
- **Branch:** `claude/pec-x1-fixtures-proposal`.
- **Prep folder:** `projects/pec/execution/_Coordination/PEC_X1_FIXTURES_PREP_2026-09-27/` (use the actual date).

Read `COMMON.md` beside this brief. It applies with the overrides below.

## What X1 is

Prepare the owner-ruled packet that commits the P1 fixture suites named in SCA-005 `Propagation_Plan.md` §B7 (`_ScopeChange/SCA-005_2026-09-23_2139/`). These are golden-by-reference `(commit, path, blob)` fixtures pinned at `d61981ee2`, with content-minimal goldens and nothing copied into PEC's tree:
- FC-1, receipt present (Piping `PIPING_LINTER_SCOPE_20260923`);
- FC-2, evidence-only (Piping `PIP-DEC025-BASELINE-2026-09-23`);
- FC-3, no AgentRuns record (App `APP-REPLAY-BOUNDARY-2026-09-23`);
- FX-PEC-0, PEC self-ingest;
- the synthetic grammar-edge fixture;
- any others §B7 names.

The fixtures serve the current contracts of DEL-02-03 (`D-PEC-100`), DEL-02-08 and DEL-02-09 (`D-PEC-98`). Read those contracts' fixture and verification requirements, and bind each fixture to the requirement, acceptance criterion and verification item (REQ/AC/VER) it serves.

## Carried items (binding)

- **From `D-PEC-96`:** FX-PEC-0 is redefined without the `## Remaining` sections, which `D-PEC-99` retired. It must not reference or scan for `## Remaining` or `remaining-items`; the owner said there must be none going forward. PEC's own former undertaking `remaining-loop` is not a fixture source.
- **SCA-005 risk R-05** is re-read against the `D-PEC-96` revision-4 vocabulary, and the reading is recorded.
- **The DEL-02-08/09 contract-wording items** carried in the graph: report how they bear on the fixtures, without changing any contract.

## Overrides of COMMON.md

- **Targets are source and test files under `projects/pec/v2/**`**, for example `v2/tests/fixtures/…`, together with any fixture manifest. They are not `ScopeOfWork.md` files.
  - Follow the `v2/**` slice precedents: `D-PEC-85`, `D-PEC-87`, `D-PEC-89` and `D-PEC-91` (their proposals in `_DECISIONS/` and their run roots).
  - Follow the v2 layout and test conventions in `projects/pec/v2/`.
  - The packet gives exact new files with postimage hashes, a bound act script, tests that run in the existing v2 test runner, and rollback.
- **Pinned commit.** The golden references pin foreign commits.
  - Verify each `(commit, path, blob)` resolves in this repository.
  - Verify the golden content-minimal expectations against those blobs.
  - Say what happens if a pinned commit becomes unreachable.
- **Lifecycle.** DEL-02-03, DEL-02-08 and DEL-02-09 are `INITIALIZED`. Committing fixtures is production work in those deliverables. Say what lifecycle transition, if any, the method implies (for example `INITIALIZED → IN_PROGRESS` through WORKING_ITEMS activation), and offer it as an owner add-on. Do not assume it. If any is `CHECKING` or `ISSUED`, stop and report.
- **Reliance preflight:** use `dispatch-for-production` semantics in the packet, and `exact-correction-preparation` for preparation.
- **No parser code.** The parsers are later production packets. If a fixture cannot be meaningful without parser code, say so and propose the smallest honest scope.

## Return

Everything COMMON.md lists, plus:
- the fixture inventory with its bindings;
- the pinned-reference verification;
- the FX-PEC-0 redefinition;
- the R-05 reading;
- the lifecycle add-on question.
