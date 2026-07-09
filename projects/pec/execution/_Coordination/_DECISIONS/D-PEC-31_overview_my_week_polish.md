# D-PEC-31 - PROPOSAL: Overview and My Week polish

**Status:** RULED 2026-07-09 (O-A).
**Date prepared:** 2026-07-09
**Decision ID:** D-PEC-31
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04). Packet form follows the D-PEC-20 source-tranche
packet precedent: verified current state, decision to rule, exact fence,
options, verification plan, rollback, and open human ruling.

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> It proposes a bounded source tranche under the adopted reporting-first PEC
> UI/UX redesign plan. Source execution remains prohibited unless and until the
> owner rules this packet. Sources govern on any disagreement.

## Why this row exists

Overview and My Week are reporting targets for sponsor/PM and contributor
use, but the standing plan records remaining polish after the reporting
foundation: drill consistency, affirmative empty states, export consistency,
honest action presentation, severity vocabulary alignment, and removal of
dead/stale UI code. These are not new workflow features; they make existing
facts easier to read and interrogate.

The T0 design specification pins the scope in
`projects/pec/execution/_Coordination/DESIGN_SPEC_2026-07-08_uiux_redesign.md`
§3, §4, §11A E1/E7/E15/E20, and §11B P14.

## Dependencies

D-PEC-31 source execution depends on D-PEC-25's drill spine and should execute
after the D-PEC-38 closeout branch is merged or rebased into the working base.
The optional My Week approvals/decisions-owed projection (P14) is an explicit
owner-open inline call and is not included in O-A.

## Verified current state (live tree, 2026-07-09)

| Fact | Source |
|---|---|
| Overview already uses Explain-shaped KPI cards, RecordRef in package/waiting/top-blocker rows, and package-rollup CSV export. | `web/src/pages/Overview.tsx:93-170` |
| Overview still carries stale sponsor/PM page framing and a `StateTag` import not needed by the current rendered surface. | `web/src/pages/Overview.tsx:2-13` |
| My Week has RecordRef wiring for waiting rows and notifications, but empty sections still depend on table rendering rather than consistent affirmative all-clear states. | `web/src/pages/MyWeek.tsx:118-195` |
| My Week still uses `window.prompt` for close/reason collection. | `web/src/pages/MyWeek.tsx:241-246` |
| `myWeekView` currently returns committed/checks/comments/waiting only; P14 approvals/decisions-owed would require a server view widening. | `server/src/services/views.ts:713-716`; design spec §11B P14 |

## Decision to rule

Whether to authorize one source tranche implementing D-PEC-31:

1. Overview polish: make sponsor-brief/export actions read as actions rather
   than KPI-like metrics; preserve export-what-is-displayed; remove dead imports
   and stale comments; align severity vocabulary to the shipped green/amber/red
   language.
2. Overview drill consistency: ensure all KPI/signal/package/waiting/blocker
   references use existing Explain/RecordRef patterns and gracefully render
   non-routable refs.
3. My Week empty states: add affirmative all-clear states for committed work,
   checks owed, comments owed, waiting-on-others, and notifications, without
   hiding rows that exist.
4. My Week action forms: replace close/reason `window.prompt` paths with the
   existing Drawer/form pattern, preserving current server actions and audit
   semantics.
5. My Week/Overview CSV consistency: ensure exported rows match displayed rows
   and labels.
6. No new task-board, cross-user workload, scheduling, or assignment features.
7. Optional under O-B only: implement P14 by widening `myWeekView` with
   approvals/decisions owed to the current actor and rendering those sections
   in My Week.

**Not in scope:** Plan redesign; Schedule/WBS view; cross-user management
views; new mutations beyond existing My Week actions; role assignment; new
dependencies; professional/go-live claims.

## Fence (exact; STOP outside it)

O-A:

- `projects/pec/web/src/pages/Overview.tsx`
- `projects/pec/web/src/pages/MyWeek.tsx`

O-B additionally opens:

- `projects/pec/server/src/services/views.ts`
- server tests matching `projects/pec/server/test/coverage-my-week-*.test.ts`

No `core/**`, no database files, no root manifests, no profile, no import
templates, no other page source edits, and no decision/register file edits
during execution except the post-run receipt.

## Options

- **O-A (recommended):** items 1-6 above; no P14 server widening.
- **O-B:** O-A plus item 7, P14 approvals/decisions-owed projection and tests.
- **O-C:** My Week prompt/empty-state repair only.
- **O-D:** defer D-PEC-31.

## Verification plan (workplan step-4 bar)

- PEC belt-and-braces: `npm run typecheck && npm test && npm run build &&
  npm run drill`.
- O-B server tests for the P14 projection, visibility basis, and empty result
  shape.
- Browser visual pass on Overview and My Week at about 1280 px desktop and one
  narrow/mobile viewport: no blank pages, no body overflow, no overlap, clear
  actions, clear empty states.
- Interaction pass: My Week Drawer forms open/submit/cancel, Escape close,
  keyboard focus stays visible, existing server actions still enforce RBAC.
- Scope containment: `git diff --name-only` is a subset of the ruled fence.
- Repo checks: `PYTHONDONTWRITEBYTECODE=1 python3
  tools/practitioner_harness/harness.py self-check`, coord-check on the branch
  diff, `git diff --check`.
- Adversarial review: no task-management creep, no cross-user data expansion
  under O-A, and no invented status/severity claim.

## Rollback

Single revert of the source tranche commit(s). No schema, data, dependency, or
runtime rollback is needed.

## Human ruling

O-A affirmed 2026-07-09.

Owner context/rationale: O-B's `myWeekView` widening is rejected as
task-management gravity on a surface that is peripheral to the PE/PD operating
model. The standing direction remains that PEC is not a task-management
platform at this time.

O-B may return only as its own future packet. D-PEC-31 execution must stay in
the O-A web-only fence and must not widen the server `myWeekView`.
