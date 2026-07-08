# D-PEC-27 - PROPOSAL: Action & Hold Log issue dashboard

**Status:** RULED 2026-07-08 (O-A).
**Date prepared:** 2026-07-08
**Decision ID:** D-PEC-27
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04). Packet form follows the D-PEC-20 source-tranche
packet precedent: verified current state, decision to rule, exact fence,
options, verification plan, rollback, and open human ruling.

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> It proposes a bounded source tranche under the adopted reporting-first PEC
> UI/UX redesign plan. Source execution remains prohibited unless and until the
> owner rules this packet. Sources govern on any disagreement.

## Why this row exists

The owner direction for the continuing development phase is an effective
reporting tool for project status, "according to issues tracked at a package
level and completeness tracked at a deliverable level." D-PEC-27 is the
standing plan's issue-dashboard tranche: it turns the Action & Hold Log into a
dashboard that reports open issue facts with drill-backed counts, without
becoming task management.

The T0 design specification pins the scope in
`projects/pec/execution/_Coordination/DESIGN_SPEC_2026-07-08_uiux_redesign.md`
§7, §11B P1-P4, and §12 F1.

## Dependencies

D-PEC-27 source execution depends on D-PEC-24 and D-PEC-25 being ruled and
executed first. D-PEC-24 supplies accessible shared affordances and D-PEC-25
supplies the `<RecordRef>` drill spine. The owner may rule the packets in one
slate, but execution must sequence 24 -> 25 -> 27.

D-PEC-27 also intersects open redesign slate item 3 (Log dashboard depth). The
recommended option below implements the full KPI band, aging strip, group-by,
and quick-view presets, but keeps the split-pane workbench out as task-manager
creep.

## Verified current state

| Fact | Source |
|---|---|
| `logRegisterView` currently includes work items, holds, interfaces, and intake items only. | `projects/pec/server/src/services/views.ts:491-557` |
| Log filters currently accept types `work_item`, `hold`, `interface_item`, and `intake_item`. | `projects/pec/server/src/services/views.ts:479-488` |
| Hold rows currently hardcode `packageId: null`. | `projects/pec/server/src/services/views.ts:516-524` |
| Interface log rows currently hardcode `ageWd: 0`. | `projects/pec/server/src/services/views.ts:526-533` |
| `isInPackage` can resolve only deliverable, revision, and work_item targets today. | `projects/pec/server/src/services/views.ts:160-167` |
| Package cockpit interface and risk rows also hardcode `ageWd: 0`; T0 assigns that factual-correctness fix to D-PEC-27 where `views.ts` is first touched. | `projects/pec/server/src/services/views.ts:257-270`; T0 §11B/P4 and §12/F1 |
| The Log page currently renders a flat table with filters, no KPI band or Explain-shaped dashboard counts. | `projects/pec/web/src/pages/LogHome.tsx:60-160` |
| Log Type is plain text, not the existing color-typed `.itype-*` visual vocabulary. | `projects/pec/web/src/pages/LogHome.tsx:89-92`; T0 §7(b) |
| Unanchored intake items are explicitly marked and must remain visible. | `projects/pec/server/src/services/views.ts:535-544` |

## Decision to rule

Whether to authorize one source tranche implementing the D-PEC-27 issue
dashboard:

1. **Read-side `logSummaryView`:** add an Explain-shaped summary over the
   loaded issue rows: open by type, overdue, aging buckets, untriaged intake
   count plus oldest, and active holds by cause. Every count carries
   `ruleId`, `detail`, and `contributing[]` refs.
2. **Widen `logRegisterView`:** include open decisions and open risks in the
   Log union where their source log/visibility basis supports display. The UI
   must state any risk visibility caveat until D-PEC-32 decides the fuller
   issue model.
3. **Fix factual basis F1:** replace fabricated interface/risk `ageWd: 0`
   display/sort basis with honest need-by based `overdueWd` or an explicit
   absent value where no `needBy` exists. No creation timestamp is invented.
4. **Package attribution for holds:** populate hold `packageId` where
   resolvable through existing `holdLinks` plus current `isInPackage`; state
   the partial basis instead of widening the model beyond the existing three
   target types.
5. **Dashboard UI:** add the KPI band, aging strip, group-by controls, and
   quick-view URL presets named by T0; render a color-typed Type column,
   render `state`, drop the redundant Anchor column, and sort
   overdue/aging-first per the server basis.
6. **Retain triage workflow unchanged:** the existing intake triage queue and
   disposition actions remain the only mutation path on the page. This packet
   adds dashboard/reporting visibility, not board/task-manager behavior.
7. **No board/workbench by default:** split-pane row workbench is excluded
   unless the owner selects the explicit option below.

**Not in scope:** inline status edits; bulk mutation; drag/board workflow;
editable severity; D-PEC-29 package/deliverable link projections; D-PEC-32
schema/model changes; new dependencies; import behavior; any professional or
go-live claim.

## Fence (exact; STOP outside it)

- `projects/pec/server/src/services/views.ts`
- `projects/pec/server/src/api.ts`
- `projects/pec/web/src/pages/LogHome.tsx`
- `projects/pec/web/src/shared.tsx`

No `core/**`, no database migration, no `agent-sidecar/**`, no root manifests,
no profile, no non-Log page source edits, no decision/register file edits
during execution except the post-run receipt.

## Options

- **O-A (recommended):** full issue-dashboard band, aging strip, group-by, and
  quick-view presets; split-pane row workbench excluded.
- **O-B:** O-A plus a read-only split-pane row workbench. No new mutations.
- **O-C:** lean first cut: KPI band plus summary route only; defer aging strip,
  group-by, and quick-view presets.
- **O-D:** defer D-PEC-27.

## Verification plan (workplan step-4 bar)

- PEC belt-and-braces: `npm run typecheck && npm test && npm run build &&
  npm run drill`.
- Server tests for `logSummaryView`, widened decision/risk rows, hold package
  attribution basis, and no fabricated `ageWd: 0` for interface/risk rows.
- Browser visual pass on Log at about 1280 px desktop and one narrow/mobile
  viewport: KPI band, aging strip, filters, quick views, grouping, and no
  overlap/overflow.
- Drill pass: every KPI opens Explain with contributing refs; each row routes
  through D-PEC-25 `<RecordRef>`; unanchored intake remains visible.
- Scope containment: `git diff --name-only` is a subset of the fence above.
- Repo checks: `PYTHONDONTWRITEBYTECODE=1 python3
  tools/practitioner_harness/harness.py self-check`, coord-check on the branch
  diff, `git diff --check`.
- Adversarial review of issue-count bases, visibility/redaction behavior,
  no task-manager creep, and no mutation surface expansion.

## Rollback

Single revert of the source tranche commit(s). If a route is added for
`logSummaryView`, reverting removes it with the UI changes; no schema/data
rollback is needed.

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
and D-PEC-25 source execution. Split-pane row workbench is not authorized.
