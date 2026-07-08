# D-PEC-26 - PROPOSAL: Admin operations console

**Status:** RULED 2026-07-08 (O-A).
**Date prepared:** 2026-07-08
**Decision ID:** D-PEC-26
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04). Packet form follows the D-PEC-20 source-tranche
packet precedent: verified current state, decision to rule, exact fence,
options, verification plan, rollback, and open human ruling.

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> It proposes a bounded source tranche under the adopted reporting-first PEC
> UI/UX redesign plan. Source execution remains prohibited unless and until the
> owner rules this packet. Sources govern on any disagreement.

## Why this row exists

The owner named the Admin page as a poor UI/UX surface, and the reporting-first
direction depends on Admin as the operational control point for upload,
accept/apply, exports, thresholds, people visibility, and system evidence.
D-PEC-26 turns Admin into an operations console while preserving the existing
human-gated import proposal pathway and high-risk action boundaries.

The T0 design specification pins the scope in
`projects/pec/execution/_Coordination/DESIGN_SPEC_2026-07-08_uiux_redesign.md`
§10, §11B P11-P13, and §12 F3.

## Dependencies

D-PEC-26 source execution depends on D-PEC-24 and D-PEC-25 being ruled and
executed first. D-PEC-24 supplies the dialog/focus/token foundation and
D-PEC-25 supplies drill refs for activity/system evidence rows.

The role-assignment route is an open owner decision (standing plan slate item
2). The recommended D-PEC-26 option keeps assignment out and renames the
section "People directory"; adding assignment is a separate explicit owner
choice.

## Verified current state

| Fact | Source |
|---|---|
| Admin currently renders sections sequentially: proposals, direct import, exports, thresholds, people. | `projects/pec/web/src/pages/Admin.tsx:12-21` |
| Import proposals exist and list/apply/accept through `import-proposals` routes. | `projects/pec/web/src/pages/Admin.tsx:58-188`; `projects/pec/server/src/api.ts:349-374` |
| Direct import remains visually close to proposal import and posts CSV directly with optional `force`. | `projects/pec/web/src/pages/Admin.tsx:191-260`; `projects/pec/server/src/api.ts:325-330` |
| Reject reason still uses `window.prompt`. | `projects/pec/web/src/pages/Admin.tsx:173-179` |
| `GET /api/people` returns only id/name/email/discipline, not project roles. | `projects/pec/server/src/api.ts:112-115` |
| `project_role` table exists. | `projects/pec/server/src/db.ts:94-99` |
| `GET config` returns merged effective thresholds only. | `projects/pec/server/src/api.ts:394-399` |
| `PUT config` blindly stringifies thresholds/config keys without shape, key, numeric, or warn/escalate validation. | `projects/pec/server/src/api.ts:400-429` |
| `can/:action` casts the path segment to `PermissionAction` without validation. | `projects/pec/server/src/api.ts:154-158` |
| Audit writing exists, but only record-scoped history reading is exposed today. | `projects/pec/server/src/repo.ts:190-205`; T0 §10 M10.2 |

## Decision to rule

Whether to authorize one source tranche implementing the D-PEC-26 Admin
operations console:

1. **Route-tabbed Admin:** split Admin into route-addressable sections:
   Import, Exports & data exchange, Thresholds, People directory, and
   Activity / system evidence. Reuse existing app routing patterns; no route
   names change outside Admin.
2. **Proposals first:** make import proposals the primary import lane. Show
   proposal states, dry-run/apply report summaries, hashes, versions, and
   stale/accepted/applied status clearly.
3. **Danger boundary for direct import:** keep direct import available only as
   a visually fenced, confirm-gated high-risk area with no visual parity to
   proposal apply. Do not change import semantics.
4. **Exports & data exchange:** group register exports, templates, sponsor
   brief, package pack, and runbook links by task. Export-what-is-displayed
   behavior is preserved.
5. **Thresholds:** group thresholds by signal family, show default vs project
   override vs effective value, add client validation, and add server
   validation so unknown keys, non-numeric/negative values, and warn>escalate
   pairs reject with 400.
6. **Permission probe repair:** validate `can/:action` against the known
   permission-action set instead of blindly casting the path segment.
7. **People directory:** show people plus project role pills and a role to
   capability matrix from server truth. Do not add role assignment unless the
   owner chooses O-B.
8. **Activity/system evidence:** add a read-only project-scoped activity feed
   from audit/import proposal transitions plus app/project/DB-basis evidence
   notice. Rows drill through D-PEC-25 where record refs are routable.
9. **Replace prompt:** replace Admin reject-reason `window.prompt` with the
   D-PEC-24 Drawer pattern.

**Not in scope:** changing import contracts; changing proposal lifecycle;
removing direct import; adding new runtime dependencies; role assignment route
unless O-B is ruled; DB schema migration; professional/go-live claims; any
mutation not already protected by server permissions.

## Fence (exact; STOP outside it)

- `projects/pec/web/src/pages/Admin.tsx`
- `projects/pec/web/src/main.tsx`
- `projects/pec/server/src/api.ts`
- `projects/pec/server/src/services/views.ts`

No `core/**`, no database migration, no `agent-sidecar/**`, no root manifests,
no profile, no non-Admin page source edits, no decision/register file edits
during execution except the post-run receipt.

## Options

- **O-A (recommended):** Admin operations console as specified, with People
  directory read-only and no role-assignment route.
- **O-B:** O-A plus a new project-role assignment route and UI. This opens the
  Tier-O role-management choice and must include server tests for permission
  boundaries.
- **O-C:** thresholds/F3 repair only: server/client threshold validation plus
  `can/:action` validation; defer Admin layout.
- **O-D:** defer D-PEC-26.

## Verification plan (workplan step-4 bar)

- PEC belt-and-braces: `npm run typecheck && npm test && npm run build &&
  npm run drill`.
- Server tests for threshold validation, config override/default/effective
  split, `can/:action` invalid-action handling, project people roles, and
  activity feed read behavior. O-B adds role-assignment route tests.
- Browser visual pass on Admin at about 1280 px desktop and one narrow/mobile
  viewport: tabs/sections, import proposal table, danger boundary, thresholds,
  people directory, activity/system evidence, no overlap/overflow.
- Interaction pass: proposal accept/apply still hash/version bound; direct
  import confirms and remains visually separated; reject reason uses Drawer;
  forms visible only when `can/config.manage` permits.
- Scope containment: `git diff --name-only` is a subset of the ruled fence.
- Repo checks: `PYTHONDONTWRITEBYTECODE=1 python3
  tools/practitioner_harness/harness.py self-check`, coord-check on the branch
  diff, `git diff --check`.
- Adversarial review of high-risk action separation, no direct-import
  privilege widening, no role-assignment slip under O-A, and no new dependency.

## Rollback

Single revert of the source tranche commit(s). If O-A is ruled, no schema/data
rollback is needed. If O-B is ruled, rollback includes the project-role route
and UI only; existing `project_role` data remains because the table already
exists.

## Human ruling

**RULED - 2026-07-08** (owner in-session, Ryan Tufts, verbatim slate ruling
covering D-PEC-24, D-PEC-25, D-PEC-26, D-PEC-27, D-PEC-29, and D-PEC-34):

> I rule O-A for D-PEC-24, D-PEC-25, D-PEC-26, D-PEC-27, D-PEC-29, and
> D-PEC-34. Execution must respect packet dependencies and fences. D-PEC-24
> executes before D-PEC-25; D-PEC-26 and D-PEC-27 execute after D-PEC-24/25;
> D-PEC-29 executes after D-PEC-25; D-PEC-34 may execute as the independent
> minimal Plan factual-correctness fix. No source work outside the ruled
> packet fences is authorized.
>
> You may merge the PR when complete.

Recorded interpretation: O-A is affirmed for this packet. Source
implementation is authorized inside this packet's fence only, after D-PEC-24
and D-PEC-25 source execution. Role assignment is not authorized.
