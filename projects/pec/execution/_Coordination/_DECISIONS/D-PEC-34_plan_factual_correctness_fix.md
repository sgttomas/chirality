# D-PEC-34 - PROPOSAL: Plan factual-correctness fix (minimal F2)

**Status:** RULED 2026-07-08 (O-A).
**Date prepared:** 2026-07-08
**Decision ID:** D-PEC-34
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04). Packet form follows the D-PEC-20 source-tranche
packet precedent: verified current state, decision to rule, exact fence,
options, verification plan, rollback, and open human ruling.

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> It proposes a bounded source tranche under the adopted reporting-first
> amendment. Source execution remains prohibited unless and until the owner
> rules this packet. Sources govern on any disagreement.

## Why this row exists

The reporting-first amendment deferred the larger Plan redesign (D-PEC-28 and
D-PEC-28b) because this phase is not a planning or scheduling platform phase,
but it kept the factual-correctness fix F2 as an early minimal tranche. The
standing plan records this as D-PEC-34:
`_DomainEngines/pec/WORKPLAN_2026-07-08_pec_uiux_redesign.md` roadmap row
"D-PEC-34 - Plan factual-correctness fix (F2) - minimal." The T0 design spec
records the same owner pointer in
`projects/pec/execution/_Coordination/DESIGN_SPEC_2026-07-08_uiux_redesign.md`
§12/F2.

This packet asks whether to authorize only that minimal factual-correctness
source change. It does not reopen the deferred D-PEC-28/28b planning phase.

## Verified current state

| Fact | Source |
|---|---|
| `raiseCapacityRisk` posts a new risk directly from the capacity table. | `projects/pec/web/src/pages/Plan.tsx:58-71` |
| The create payload hardcodes `probability: 4, impact: 3`. | `projects/pec/web/src/pages/Plan.tsx:61-66` |
| The "raise risk" button invokes that POST without a confirmation or preview. | `projects/pec/web/src/pages/Plan.tsx:171-174` |
| Risk `probability` and `impact` are nullable in the core type. | `projects/pec/core/src/types.ts:474-475` |
| T0 F2 acceptance requires no probability/impact unless a human enters them, a preview that names the week/discipline/load basis, and a duplicate guard. | `DESIGN_SPEC_2026-07-08_uiux_redesign.md` §12/F2 |
| The standing plan limits this tranche to `web/src/pages/Plan.tsx`. | `_DomainEngines/pec/WORKPLAN_2026-07-08_pec_uiux_redesign.md` D-PEC-34 row |

## Decision to rule

Whether to authorize one source tranche implementing the minimal F2 fix:

1. **Remove fabricated scores:** the risk create call sends no
   `probability`/`impact` unless values are explicitly entered in the confirm
   drawer. The minimal tranche may omit score inputs entirely; in that case
   both fields are absent/null by server behavior.
2. **Confirm before create:** clicking "raise risk" opens a confirmation drawer
   that previews the factual basis verbatim: week, discipline, load hours,
   capacity hours, percent, and the generated title/cause text. The copy must
   say the action **may create** a risk, not that a risk already exists.
3. **Duplicate guard:** before creating, the UI checks already loaded or
   freshly fetched project risks for the same generated capacity-overload
   title/cause basis. If a matching open risk exists, the UI surfaces that
   reference instead of silently creating a duplicate.
4. **No broader Plan redesign:** do not add readiness headers, backlog rails,
   WBS views, drag/reorder behavior, scheduling claims, or capacity math
   changes.

**Not in scope:** D-PEC-28/28b; server route changes; core model changes;
threshold work; report generation; schedule/WBS views; any new dependency;
database mutation outside the user-triggered existing risk-create endpoint;
any `force` behavior; any professional or go-live claim.

## Fence (exact; STOP outside it)

- `projects/pec/web/src/pages/Plan.tsx`

No `server/**`, no `core/**`, no `shared.tsx`, no styles outside what already
exists in `Plan.tsx`, no root manifests, no database files, no profile, no
decision/register file edits during execution except the post-run receipt.

## Options

- **O-A (recommended):** authorize the complete minimal F2 fix above.
- **O-B:** authorize only removal of fabricated probability/impact values and
  the confirmation drawer; defer duplicate guard.
- **O-C:** defer D-PEC-34.

## Verification plan (workplan step-4 bar)

- PEC belt-and-braces: `npm run typecheck && npm test && npm run build &&
  npm run drill`.
- Browser visual pass on the Plan page at about 1280 px desktop and one
  narrow/mobile viewport: confirmation drawer fits, no overlap, no page
  breakage.
- Interaction pass: "raise risk" opens the confirm drawer; confirm sends no
  fabricated probability/impact; duplicate basis surfaces the existing risk
  instead of creating another.
- Scope containment: `git diff --name-only` is a subset of the fence above.
- Repo checks: `PYTHONDONTWRITEBYTECODE=1 python3
  tools/practitioner_harness/harness.py self-check`, coord-check on the branch
  diff, `git diff --check`.
- Adversarial review of the factual claim: no user-facing Plan surface reports
  fabricated scores after the tranche.

## Rollback

Single revert of the `Plan.tsx` source tranche commit. No schema, data, or
dependency rollback is needed.

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
implementation is authorized inside this packet's fence only. This tranche may
execute independently as the minimal Plan factual-correctness fix.
