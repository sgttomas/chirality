# D-PEC-25 - PROPOSAL: drill-to-source spine

**Status:** RULED 2026-07-08 (O-A).
**Date prepared:** 2026-07-08
**Decision ID:** D-PEC-25
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04). Packet form follows the D-PEC-20 source-tranche
packet precedent: verified current state, decision to rule, exact fence,
options, verification plan, rollback, and open human ruling.

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> It proposes a bounded source tranche under the adopted PEC UI/UX redesign
> standing plan. Source execution remains prohibited unless and until the owner
> rules this packet. Sources govern on any disagreement.

## Why this row exists

The adopted standing plan names D-PEC-25 as the second P0 redesign tranche:
the drill-to-source spine that makes counts and references navigable. It is
the natural successor to D-PEC-24 because D-PEC-24 supplies the shared
accessibility and keyboard-operability foundation. The T0 design specification
pins the details in
`projects/pec/execution/_Coordination/DESIGN_SPEC_2026-07-08_uiux_redesign.md`
§2.6, §11A/E12, and the per-surface drill rows in §§3-10.

This row asks whether to authorize the bounded source tranche that introduces
a shared `<RecordRef>` primitive and wires existing dead or misrouted
references to their source records. It does not authorize any new server
projection, model change, task-manager surface, or page redesign beyond
reference routing.

## Dependency

D-PEC-25 source execution depends on D-PEC-24 being ruled and executed first,
because D-PEC-24 supplies the token/focus/shared-affordance groundwork this
tranche relies on. The owner may rule both packets in one slate, but execution
must sequence D-PEC-24 before D-PEC-25.

## Verified current state

| Fact | Source |
|---|---|
| `refRoute` already maps deliverables, holds, decisions, risks, interfaces, approvals, intake, and plan items, and returns `null` for drawer-only types. | `projects/pec/web/src/shared.tsx:47-60` |
| `useHighlightRef` already reads `?ref=` for row highlight/scroll. | `projects/pec/web/src/shared.tsx:63-66` |
| Explain contributing rows manually call `refRoute` and navigate on row click instead of using a reusable record-ref component. | `projects/pec/web/src/shared.tsx:122-130` |
| Package cockpit routing uses local `issueHref`; the T0 spec records it as a misroute to replace. | `projects/pec/web/src/pages/Packages.tsx:79-83`; T0 §2.6 and §5(d) |
| Log rows are rendered by `RegisterTable` without row routing. | `projects/pec/web/src/pages/LogHome.tsx:158-159`; T0 §7 M7.6 |
| My Week waiting/notification tables are rendered without drill routing. | `projects/pec/web/src/pages/MyWeek.tsx:195-198`; T0 §4(d) |
| Registers already import `useHighlightRef`, but reference/link cells are not consistently rendered through a shared routable primitive. | `projects/pec/web/src/pages/Registers.tsx`; T0 §9(d) |
| T0 requires graceful null-route degradation: drawer-only record types render as non-interactive refs until D-PEC-33. | `DESIGN_SPEC_2026-07-08_uiux_redesign.md` §2.6 |

## Decision to rule

Whether to authorize one source tranche implementing the D-PEC-25 drill spine:

1. **Shared `<RecordRef>` primitive:** add a component in `shared.tsx` that
   renders a real link/button-like affordance for routable records using
   `refRoute`, and renders a non-interactive styled ref when `refRoute`
   returns `null`.
2. **Explain drawer reuse:** replace the manual contributing-record routing in
   `ExplainProvider` with `<RecordRef>`, preserving close-before-navigate
   behavior and null-route degradation.
3. **Package cockpit routing:** replace `issueHref` with `<RecordRef>` for
   package issue rows and needs-lead rows; eliminate the decisions/risks/log
   misroute and preserve `?ref=` highlight for register/log homes.
4. **Deliverable detail references:** render open holds, approval records,
   decision dependencies, transition-explain contributing records, and other
   existing cross-record references through `<RecordRef>` where the row carries
   `recordType`/`id`/`ref`.
5. **Log and My Week dead rows:** wire Log register rows, dispositioned intake
   rows, My Week waiting rows, and notification rows to `<RecordRef>` where the
   payload carries a routable record basis. Non-routable rows remain visibly
   non-interactive.
6. **Plan and Registers references:** wire Plan document/record refs and
   register reference/link cells to `<RecordRef>` where existing payload fields
   support it; do not invent missing parent ids for drawer-only records.
7. **No new data:** use only existing payload fields. Any missing route/data
   basis is explicitly degraded to non-interactive display and left for
   D-PEC-33 or the later packet that adds the needed projection.

**Not in scope:** D-PEC-24 token/focus/dialog work; D-PEC-26 Admin redesign;
D-PEC-27 Log summary projections; D-PEC-29 package/deliverable issue
linkage projections; D-PEC-30 register layout redesign; D-PEC-31 Overview/My
Week polish; D-PEC-33 deep-linkable drawer URLs; any server route; any core
model change; any new dependency; any record-state mutation.

## Fence (exact; STOP outside it)

- `projects/pec/web/src/shared.tsx`
- `projects/pec/web/src/pages/Overview.tsx`
- `projects/pec/web/src/pages/Packages.tsx`
- `projects/pec/web/src/pages/Deliverables.tsx`
- `projects/pec/web/src/pages/LogHome.tsx`
- `projects/pec/web/src/pages/MyWeek.tsx`
- `projects/pec/web/src/pages/Plan.tsx`
- `projects/pec/web/src/pages/Registers.tsx`

No `server/**`, no `core/**`, no `agent-sidecar/**`, no `web/src/main.tsx`,
no root manifests, no database files, no profile, no decision/register file
edits during execution except the post-run receipt.

## Options

- **O-A (recommended):** authorize the full D-PEC-25 drill-to-source spine,
  sequenced after D-PEC-24.
- **O-B:** authorize only the shared `<RecordRef>` primitive plus Explain
  drawer and Package cockpit routing; defer the broader page wiring.
- **O-C:** defer D-PEC-25.

## Verification plan (workplan step-4 bar)

- PEC belt-and-braces: `npm run typecheck && npm test && npm run build &&
  npm run drill`.
- Browser visual pass on every changed surface at about 1280 px desktop and
  one narrow/mobile viewport: Overview, Packages, Deliverables, Log, My Week,
  Plan, Registers.
- Keyboard pass: every newly routable ref is reachable/operable by keyboard;
  non-routable refs are not fake links and do not enter the tab order.
- Drill pass: representative refs land on deliverable detail, registers tabs
  with `?ref=`, log with `?ref=`, and Plan; drawer-only record types degrade
  visibly without dead links.
- Scope containment: `git diff --name-only` is a subset of the fence above.
- Repo checks: `PYTHONDONTWRITEBYTECODE=1 python3
  tools/practitioner_harness/harness.py self-check`, coord-check on the branch
  diff, `git diff --check`.
- Adversarial review of routing claims, null-route degradation, no new data
  invention, and no accidental mutation surface.

## Rollback

Single revert of the source tranche commit(s). Because the tranche adds no
server route, schema change, dependency, or data migration, rollback restores
the prior routing/display behavior.

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
source execution.
