# D-PEC-38 - PROPOSAL: Reporting-foundation fix-forward tranche

**Status:** AWAITING_RULING (STOP: the ruling act is the owner's).
**Date prepared:** 2026-07-08
**Decision ID:** D-PEC-38
**Prepared by:** PEC work loop agent. The ruling act is the owner's
(K-AUTH-1; D-GOV-04). Packet form follows the D-PEC-20 source-tranche
packet precedent: verified current state, decision to rule, exact fence,
options, verification plan, rollback, and open human ruling.

> **Epistemic status: agent-prepared source-tranche packet, not authority.**
> It proposes a bounded fix-forward source tranche closing gaps an
> adversarial review (2026-07-08, against live `main` at `4c40dcf33`) found
> in the merged PR #115 execution of the ruled slate
> D-PEC-24/25/26/27/29/34. Source execution remains prohibited unless and
> until the owner rules this packet. Sources govern on any disagreement.

## Why this row exists

PR #115 executed the six ruled O-A packets and merged. Adversarial review of
the merged tree found ruled-scope items left incomplete: an F1 display gap,
the D-PEC-26 threshold-form acceptance not met client-side, ruled server
tests never written, the D-PEC-27 hold package attribution not done, Log
dashboard tiles absent or dead, two Explain/server-truth shapes short of
spec, and a11y/token migration unfinished. D-PEC-35/36/37 are reserved by
the standing plan's roadmap (upload/reporting lanes,
`_DomainEngines/pec/WORKPLAN_2026-07-08_pec_uiux_redesign.md` roadmap PR
rows), hence D-PEC-38. The standing plan's fences corollary and F-PEC-1..4 bind.

## Dependencies

All six parent tranches (D-PEC-24/25/26/27/29/34) are RULED O-A 2026-07-08
and merged in PR #115 (`main` at `4c40dcf33`). No other sequencing
dependency. This packet reopens no ruled scope decision; it completes them.

## Verified current state (live tree, 2026-07-08)

| Fact | Source |
|---|---|
| Package cockpit Age column renders raw `r.ageWd` — blank for interface/risk rows, whose `ageWd` is now honestly `null`; `overdueWd` computed but not displayed; label states no basis. | `web/src/pages/Packages.tsx:100`; `server/src/services/views.ts:218,228` |
| Null-needBy convention diverges: `packageIssueRows` emits `overdueWd: null` (helper, views.ts:190) while log rows emit `0` (`workingDaysOverdue` returns 0 for null, `core/src/calendar.ts:161-166`). | `server/src/services/views.ts:186-242` vs `:549-608` |
| Clearing a threshold field persists a `0` override (`Number('') === 0`); no client pre-submit warn<=escalate/bounds validation; no way to remove an override once set. | `web/src/pages/Admin.tsx:504-508,481` |
| Server-side threshold validation and `can/:action` validation exist (landed with PR #115). | `server/src/api.ts:436-462`, `:182-186` |
| No server test exercises the PUT `/config` validation path, `can/:action` rejection, or `logSummaryView`/`adminPeopleView`/`adminActivityView` (grep of `server/test/*.test.ts`: no hits). | `projects/pec/server/test/` |
| Hold log rows still hardcode `packageId: null` (ruled D-PEC-27 item 4; spec P3 basis exists: `holdLinks` x `isInPackage`, views.ts:160-167). | `server/src/services/views.ts:563` |
| Log aging tile is a dead `div` (`cursor: 'default'`, no Explain drawer) though `agingBuckets.contributing[]` exists server-side. | `web/src/pages/LogHome.tsx:144-151`; `views.ts:663-673` |
| Ruled KPI tiles absent: open-by-type (M7.1) and holds-by-cause (M7.5) — `byType`/`holdsByCause` computed server-side, unconsumed. | `views.ts:651-656,680-685`; `LogHome.tsx:139-152` |
| Untriaged tile lacks `oldestWd` (M7.4; basis exists: intake rows carry `ageWd`; cf. `intakeQueueView` views.ts:698-711). | `LogHome.tsx:143`; `views.ts:674-679` |
| Grouped view drops the CSV export button (`exportName={label ? undefined : ...}`) — export-what-is-displayed regression. | `web/src/pages/LogHome.tsx:199-205` |
| One inline hex survives in LogHome (`background: '#fbfcfd'`). | `web/src/pages/LogHome.tsx:444` |
| `issueMix` returns bare `{counts, worst}`, not the Explain shape spec P7 requires. | `server/src/services/views.ts:244-248` |
| Admin role->capability matrix is a client-hardcoded table, not server truth. | `web/src/pages/Admin.tsx:528-538`; truth: `core/src/permissions.ts` |
| `RegisterTable` clickable rows are mouse-only: `onClick` with no `tabIndex`, key handler, or role. | `web/src/shared.tsx:408-416` |
| `styles.css` has 44 hex-bearing lines: 30 inside the `:root` token block (28 palette primitives, lines 4-31, plus `--row-hover`/`--focus-ring` defined with raw hex, lines 42/50) and 14 rule lines outside it (94, 175, 179, 188, 189, 191, 229, 230, 232, 235, 238, 262, 264, 265). | `web/src/styles.css` |

## Decision to rule

Whether to authorize one fix-forward source tranche:

1. **F1 display closeout (spec §12 F1 acceptance):** package cockpit Age
   column shows the row's basis — `ageWd` where real, `overdueWd` where
   need-by based, explicit "—" where absent — with a basis-stating column
   label; unify the null-needBy convention (`overdueWd: null`, the
   `packageIssueRows` form) across `logRegisterView` rows.
2. **Threshold form repair (spec §12 F3, client half):** clearing a field
   removes the key instead of persisting a `0` override; client pre-submit
   validation mirrors the server rules (numeric, non-negative,
   warn<=escalate, naming the offending key); an explicit control removes an
   existing override (falls back to the default).
3. **Ruled tests, written:** one new server test file covering the PUT
   `/config` validation path (unknown key, negative, warn>escalate -> 400
   naming the key), `can/:action` unknown-action rejection, and the
   `logSummaryView`/`adminPeopleView`/`adminActivityView` payload shapes.
4. **Hold package attribution (spec P3):** populate hold `packageId` at
   views.ts:563 via `holdLinks` x existing `isInPackage` (first resolvable
   link; partial 3-of-10-target-type basis stated, widening stays D-PEC-32).
5. **Log dashboard completeness (spec §7 M7.1/M7.3/M7.4/M7.5):** aging tile
   becomes a drillable `KpiCard` over the existing `agingBuckets` Explain;
   add open-by-type and holds-by-cause tiles from the unconsumed server
   fields; add `oldestWd` to the untriaged tile (server + client); restore
   CSV export in grouped view (export what is displayed, per group or
   whole); migrate the LogHome.tsx:444 inline hex onto tokens.
6. **Explain-shape closeout:** `issueMix` becomes Explain-shaped per spec
   P7 (`{value: {byType, worst}, ruleId, detail, contributing[]}`); the
   Admin role->capability matrix is emitted from server truth
   (`core/src/permissions.ts`) via `adminPeopleView` per spec P13 —
   **finding:** the existing GET `admin/people` route (api.ts:491) carries
   it; no `server/src/api.ts` edit is needed, so it stays outside the fence.
7. **A11y/token closeout (spec §2.4/§2.5):** `RegisterTable` clickable rows
   get `tabIndex={0}`, Enter/Space activation, and a role; migrate the 14
   hex rule lines outside `:root` onto tokens (adding palette/semantic
   tokens as needed) and re-point `--row-hover`/`--focus-ring` at palette
   primitives. The `:root` palette primitives lawfully keep their hex
   definitions — they ARE the token layer's ground truth.

**Not in scope:** D-PEC-32/33 model work; new routes or mutations; new
dependencies; import behavior; Plan/Drawer/activity-feed optional items
except under O-B; any professional or go-live claim.

## Fence (exact; STOP outside it)

- `projects/pec/web/src/pages/Packages.tsx`
- `projects/pec/web/src/pages/Admin.tsx`
- `projects/pec/web/src/pages/LogHome.tsx`
- `projects/pec/web/src/shared.tsx`
- `projects/pec/web/src/styles.css`
- `projects/pec/server/src/services/views.ts`
- one new server test file matching `projects/pec/server/test/coverage-reporting-*.test.ts` (house `coverage-*` naming; exact name fixed at execution — glob per the coord-check future-ref precedent)

O-B additionally adds `projects/pec/web/src/pages/Plan.tsx`. No
`server/src/api.ts` (finding in item 6), no `core/**`, no database files, no
root manifests, no profile, no decision/register file edits during execution
except the post-run receipt.

## Options

- **O-A (recommended):** items 1-7 as itemized — minimal, ruled-scope-closing.
- **O-B:** O-A plus the adversarial review's optional flags: Drawer
  focus-restore churn on parent re-render (effect depends on `[onClose]`,
  `shared.tsx:255`); Plan.tsx duplicate-guard hardening (open-state-only +
  exact string-match fragility, `Plan.tsx:64-66`); Admin activity feed's
  fabricated `recordType#id` recordRef (`Admin.tsx:605`); risk log-rows'
  hardcoded `log: 'package'` honesty caveat (`views.ts:591`).
- **O-C:** decline; the gaps stand as merged.

## Verification plan (workplan step-4 pec-source bar)

Run PER this packet's own plan BEFORE commit — stated explicitly given the
PR #115 lapse; every check at the exact final commit SHA:

- pec belt-and-braces: `npm run typecheck && npm test && npm run build &&
  npm run drill` green — PLUS a visual pass on every changed surface:
  browser screenshots at a ~1280px desktop viewport and one narrow/mobile
  viewport, keyboard operability of changed interactions, no blank
  pages/overflow/overlap.
- Per-item acceptance: cockpit Age column shows basis-labeled values with
  explicit "—" (spec §12 F1); threshold form clears/removes overrides and
  pre-submit-validates, server still 400s naming the key (spec §12 F3); new
  test file red-green against api.ts:436-462/:182-186 and the three views;
  Log package filter/group now includes attributed holds (spec P3); all
  five KPI tiles drill to Explain contributing refs (spec §7 M7.1-M7.5);
  grouped view exports what is displayed; `issueMix` Explain-shaped (P7);
  role matrix served from `core/src/permissions.ts` (P13); RegisterTable
  rows operable by keyboard; zero hex outside `:root` in styles.css.
- Scope containment: `git diff --name-only` is a subset of the fence above.
- Repo checks: `PYTHONDONTWRITEBYTECODE=1 python3
  tools/practitioner_harness/harness.py self-check`, coord-check on the
  branch diff, `git diff --check`.
- Adversarial review of citations and of the factual claims: no fabricated
  age/basis remains displayed; no client-invented RBAC.

## Rollback

Single revert of the source tranche commit. No schema, data, or dependency
rollback is needed; the new test file reverts with it.

## Human ruling

**OPEN — STOP.** No source execution until the owner rules O-A, O-B, or O-C
(K-AUTH-1; D-GOV-04). The ruling and any owner amendment will be recorded
here verbatim.
