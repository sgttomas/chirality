# Sealed brief — N1 carrier estimates

You are a bounded Agent 2 ephemeral generalist executing an owner-specific estimate-snapshot task. Role entry is instruction-asserted. Do not delegate.

## Basis

- Repository root: `/Users/ryan/.codex/worktrees/0b6e/chirality`
- Basis: `origin/main@7974f2d4a456777f2132fb5726a67a042137ca78`
- Selection authority: Phase 4 steer at `plans/steers/chirality_app_v3_phase4_steer_root_2026-08-23.md`, SHA-256 `54595fe5060bed81fb9b871d623d15505ee7ff42b4e7349d238b9c4d0f9cc644`.
- Candidate-whitespace and G0–G4 passed before dispatch.

Read root `AGENTS.md`, the Phase 4 steer, the accepted R7 record, the applied deliverable-register rows, and for DEL-02-07..12 and DEL-04-11 each accepted `ScopeOfWork.md`, `_CONTEXT.md`, and Phase-3 `_DEPENDENCIES.md`. Read DEL-02-12's accepted ten-binding hold table. Use the provenance/no-invention/uncertainty discipline of `skills/estimate-snapshot/SKILL.md`; the steer controls this bespoke hours-only form and exact destination, so do not introduce cost, currency, rates, price sources, or schedule calculations.

## Objective and write scope

Write only these files under `execution/_ScopeChange/SCA-004_2026-08-22_1749/Evidence/ESTIMATE_SNAPSHOT_POST_PHASE3/`:

- `ESTIMATE_METHOD.md`
- `DEL-02-07_ESTIMATE.md`
- `DEL-02-08_ESTIMATE.md`
- `DEL-02-09_ESTIMATE.md`
- `DEL-02-10_ESTIMATE.md`
- `DEL-02-11_ESTIMATE.md`
- `DEL-02-12_ESTIMATE.md`
- `DEL-04-11_ESTIMATE.md`

You may additionally write only this instance's `RETURN.md` and `STATUS.json`. Use `apply_patch` for all file writes.

## Estimate contract

`ESTIMATE_METHOD.md` defines once and consistently applies three uncertainty classes: `LOW_UNCERTAINTY`, `MEDIUM_UNCERTAINTY`, and `HIGH_UNCERTAINTY`, with explicit percentage spread bands and deterministic rounding. It records that hours are decision-support estimates, not accepted commitments or schedule durations. It lists, by exact identifier, all ten held DEL-02-06 bindings plus TM-ROOT-106, TM-ROOT-122, C1, and App-owned obligations as exclusions.

Each deliverable estimate must include:

1. status `DRAFT_AWAITING_OWNER_ACCEPTANCE` and derivative/non-authorizing boundary;
2. exact accepted input paths and clause/output citations;
3. output-level work breakdown with stable element IDs, base hours, named uncertainty class, low/high hours, and a short source-grounded rationale;
4. arithmetic totals that reproduce from the line items;
5. assumptions separated from exclusions;
6. the global exclusions plus deliverable-specific exclusions, with held/App/pin/C1 matters never treated as assumptions;
7. Phase-3 dependency interactions and sequencing risk without dates, precedence decisions, or a schedule.

Estimate only work within the accepted SOW outputs and acceptance/verification work. Do not invent interfaces, dependencies, tools, implementation authority, staffing, calendars, or productivity rates. If a requested element cannot be grounded, omit it and report the gap.

## Return contract

Report written files and SHA-256 values, total/base/range per deliverable, source coverage, omissions, changed paths, and fresh self-review findings. Terminal status is `COMPLETE` or `BLOCKED`.
