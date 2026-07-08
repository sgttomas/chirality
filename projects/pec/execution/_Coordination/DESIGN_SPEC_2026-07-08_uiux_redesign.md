# PEC UI/UX redesign — design specification + data contract inventory (T0)

> **Epistemic status: agent-authored design specification — NOT authority.**
> Authored 2026-07-08 as roadmap step **T0** of the adopted standing plan
> `_DomainEngines/pec/WORKPLAN_2026-07-08_pec_uiux_redesign.md` (see its
> "Roadmap — T0" section). Sources govern on any disagreement: live tree first,
> then the two provenance proposals in `_DomainEngines/proposals/pec/`. This
> spec **authorizes no source work** — every implementation tranche remains a
> future owner-ruled D-PEC packet (F-PEC-1 forbids `web/**`, `server/**`,
> `core/**` writes by default; K-AUTH-1: adoption/ruling is the owner's act).
> The redesign slate items 1–6 (standing plan §"Open owner decisions") are
> **owner-open and none is defaulted here**: any spec content depending on one
> is marked `[COND-SLATE-n]` and activates only per the owner's ruling (§14).
> Every file:line citation below was spot-checked against the live tree on
> 2026-07-08; the "live-tree deltas" in §1.3 record where this spec corrects
> its inputs. Subsequent D-PEC packets (24..33) cite this spec's section/row
> IDs instead of re-deriving design.

Paths in citations are relative to `projects/pec/` unless prefixed.

---

## §1 Scope & method

### §1.1 What was merged, from which proposal

- **Operator proposal** `_DomainEngines/proposals/pec/PLAN_2026-07-08_pec_uiux_redesign.md`
  (+ 69-defect appendix): contributes the per-surface target designs §5.1–5.8
  (Admin tabs, Log KPI band + aging strip + group-by + quick-view presets,
  Plan heatmap/rollups/legend, Packages/Deliverables drill fixes, Registers
  consistency, token/a11y foundation, `<RecordRef>` drill spine), the
  data-readiness tiers U/S/M/O, and the verified defect register this spec's
  §12 fixes derive from.
- **Peer proposal** `_DomainEngines/proposals/pec/WORKPLAN_2026-07-08_pec_ui_redesign.md`
  (+ screenshot evidence `PEC_2026-07-08_ui-redesign-planning/`): contributes
  the one-job-per-page principle framing, the Admin "operations console"
  section vocabulary incl. the **system-evidence panel**, the Log
  saved-view/quick-view vocabulary and queue metrics, the Plan **readiness
  header + planning intake/backlog rail + commit readiness checklist**, the
  direct-import "no visual parity" demotion, and the exit criterion this spec
  closes in §13 (every dashboard count → existing field or named projection).
- **Merge decisions already made by the adopted standing plan govern** (its
  roadmap table D-PEC-24..33): the Log split-pane row workbench is carried
  only as `[COND-SLATE-3]`; the route rename Log→"Issues" is NOT carried
  (conceptual labeling only, per peer proposal's own deferral); the peer's
  "issue indicators on Deliverables register rows" is NOT carried by the
  adopted D-PEC-29 scope and is recorded here as merged-out (revisitable by
  owner direction); the peer's regression-evidence pass rides every tranche
  as the step-4 visual check, not as a tranche.

### §1.2 Verification stance

The live tree wins over both proposals and over the prepared digests. Every
load-bearing file:line in this spec was re-read from source during authoring.
Where a needed value has **no record basis** (e.g. interface/risk "age" —
neither type carries `raisedAt`/`createdAt`, core/src/types.ts:464-487 and
:492-506), the spec specifies the honest derivable substitute or absence
(design principle 3: factual or absent), never an invented value.

### §1.3 Live-tree deltas found while authoring (vs proposals/digests)

- **D1.** `planView` already ships a `plannable[]` backlog — eligible-but-
  unplanned work items / checks / approval records with `{itemType, itemId,
  ref, label}` (server/src/services/plan.ts:509-520, returned at plan.ts:525).
  Neither proposal cited it. The Plan intake/backlog rail (§8) therefore maps
  to an **existing field** for its count and membership; only its grouping
  enrichment (owner/package/due) is new (P9).
- **D2.** Interface **and risk** age is underivable, not merely unwired:
  `Risk` (core/src/types.ts:464-487) and `InterfaceItem` (core/src/types.ts:492-506)
  carry no creation timestamp. The Age-0 fix (F1, P4) must substitute
  needBy-based `overdueWd` (the working `interfaceRegisterView` pattern,
  views.ts:664-670) rather than "fix ageWd" as both proposals loosely say.
- **D3.** `commitWeek` already accepts any valid ISO week (plan.ts:336-338)
  and `reviewPlanShift` already accepts an optional reviewer `note`
  (plan.ts:273-277) — Plan's week-locked commit and missing reject-reason are
  purely client gaps (Tier U), confirming the operator's claim.
- **D4.** No server route lists per-project `project_role` rows for display:
  the table exists (server/src/db.ts:94-99) and is read internally
  (server/src/auth.ts:68; api.ts:87,104), but `GET /api/people` returns only
  `{id,name,email,discipline}` (api.ts:112-116). Admin "real role pills"
  therefore need a named read projection (P13) even before any assignment
  route (which stays `[COND-SLATE-2]`, Tier O).
- **D5.** Hex-literal counts confirmed live: **64** in `web/src/styles.css`,
  **2** inline across `web/src/**/*.tsx` (grep, 2026-07-08) — vs the
  operator's "~30 hardcoded hex outside :root" (the 64 includes `:root`
  tokens; the token migration scope in D-PEC-24 should plan on the full 64).

---

## §2 Global / shell specification

Implementing packets: **D-PEC-24** (§2.1–§2.5), **D-PEC-25** (§2.6).
Fences per the standing plan roadmap table.

### §2.1 Navigation grouping

Sidebar today is 8 flat `NavLink`s (web/src/main.tsx:96-107). Target: two
labeled groups with a divider — the **six lenses** (Overview · Packages ·
Deliverables · Plan · Action & Hold Log · My Week) then **Registers · Admin**.
No route changes; "Issues" appears only as in-page copy, never as a route
rename (peer deferral, §1.1).

### §2.2 Breadcrumb primitive

New shared `<Breadcrumb>` in `web/src/shared.tsx`: ordered `<nav aria-label=
"breadcrumb">` of real links. First consumers: Package detail (→ Packages
register) and Deliverable detail (→ Deliverables MDL, + owning package),
per §5/§6.

### §2.3 Project switcher and Sign-out

Switcher currently discards the lens — `onChange` navigates to
`/p/:id/overview` (main.tsx:112-118). Target: preserve the current lens path
segment on switch. Sign-out is `<a href="#">` with an inline hex color
(main.tsx:120); target: a real `<button>` styled via tokens.

### §2.4 Two-tier token layer

All color flows through primitive-palette tokens + semantic-role tokens
(`--surface`, `--text`, `--text-muted`, `--border`, `--accent`,
`--row-hover`, `--shadow`, badge/severity roles). Live fact: **64 hex
literals in `web/src/styles.css`** and **2 inline hex in tsx** (§1.3 D5) —
all migrate onto the layer; pages keep emitting semantic classNames.
Dark-mode toggle is `[COND-SLATE-6]`; the token layer itself lands
unconditionally (slate 6 only gates the toggle).

### §2.5 Accessibility foundation

- Global `:focus-visible` ring (none exists today — styles.css has no focus
  styles).
- `Drawer` (shared.tsx:175-190) becomes a real dialog: `role="dialog"`,
  `aria-modal`, focus trap, focus restore on close, Esc to close.
- `KpiCard`, clickable rows (`RegisterTable` `onRowClick`), and `.reflink`
  affordances become real `<button>`/`<a href>` — keyboard-operable with
  Enter/Space, in tab order.
- AA contrast for amber/green badges (operator-verified ~3.1:1 / ~4.4:1
  against styles.css badge palette).
- `role="tablist"`/`aria-selected` on tab bars (Registers §9, Admin §10).

### §2.6 Drill-spine primitive `<RecordRef>`

Shared `<RecordRef recordType id ref>` in `web/src/shared.tsx`: renders the
`.reflink` affordance and routes via **`refRoute`** (shared.tsx:47-60), which
today maps deliverable → own detail page; hold/decision/risk/interface_item/
approval_record → `registers/:tab?ref=`; intake_item → `/log?ref=`;
plan_item → `/plan`; **default → `null`** (work_item, revision,
review_comment, check — drawer-only records keyed by a parent id the ref
doesn't carry). `useHighlightRef` (shared.tsx:63-66) + `RegisterTable`
row-flash land the `?ref=` deep link. **Graceful null-route degradation is
mandatory**: when `refRoute` returns `null`, `<RecordRef>` renders a
non-interactive styled ref (no dead link, no fake cursor) until **D-PEC-33**
adds deep-linkable drawer records (`?open=check:123` pattern). Consumers per
surface in §3–§10. `issueHref` (web/src/pages/Packages.tsx:79-83) is deleted
in favor of `<RecordRef>` (F-class misroute; see §5).

---

## §3 Overview

*(a) Job:* the project's headline answer — "is the project on plan, and what
is pulling it off plan?" — for sponsor/PM eyes. *(g) Packet:* **D-PEC-31**
(drill fixes + polish; data unchanged).

*(b) Layout:* KPI band (existing cards) → governance signals → package
rollup table → waiting-on-you → top blockers → schedule pressure strip.
Sponsor brief becomes a real labeled action (today a KPI look-alike
non-focusable div, Overview.tsx:98-100); severity vocabulary unified to
green/amber/red; affirmative all-clear empty states; consistent CSV export;
dead `StateTag` import removed.

*(c) Metrics table:*

| # | Metric | Data basis | Existing field (file:line) / projection | Drill target |
|---|---|---|---|---|
| M3.1 | Project health badge | Explain | `overviewView.health` (views.ts:88) | ExplainDrawer → contributing refs via `<RecordRef>` |
| M3.2 | % on plan | Explain | `kpis.pctOnPlan` (views.ts:90) | ExplainDrawer |
| M3.3 | Holds by cause | Explain | `kpis.holdsByCause` (views.ts:91) | ExplainDrawer → holds register |
| M3.4 | Open decisions | Explain | `kpis.openDecisions` (views.ts:92) | ExplainDrawer → decisions register |
| M3.5 | Approvals in flight | Explain | `kpis.approvalsInFlight` (views.ts:93) | ExplainDrawer → approvals register |
| M3.6 | Schedule forecast (wd) | Explain | `kpis.scheduleForecastWd` (views.ts:94) | ExplainDrawer |
| M3.7 | Governance signals | Explain[] | `signals[]` (views.ts:98) | ExplainDrawer per signal |
| M3.8 | Package rollup row counts (onPlan/total, holds, checksDue, approvalsDue, openDecisions, openIssues) | per-package status | `packageRollup[]` (views.ts:99-113; openDecisions :109-110, openIssues :112) | row → Package detail (§5) |
| M3.9 | Waiting on you (breaching/other) | queue rows | `waitingOnYou` (views.ts:116, composed views.ts:73) | rows via `<RecordRef>` |
| M3.10 | Top blockers (ageWd, blocks) | active holds by age | `topBlockers[]` (views.ts:77-84) | rows → holds register `?ref=` |
| M3.11 | Schedule pressure ×6 weeks (loadH, capacityH, pct, level, breaches) | capacity cells + thresholds | `schedulePressure` (views.ts:124-143, over `capacityView`) | week → Plan (§8), cell explain P5 once D-PEC-28 lands |

*(d) Drill paths:* every KPI/signal opens its ExplainDrawer (existing
`useExplain`); all `contributing[]` refs render via `<RecordRef>` (§2.6);
package rollup rows navigate to package detail; blockers deep-link with
`?ref=`. *(e) Interactions/RBAC:* read-only page; sponsor-brief link and CSV
exports visible to all members (export-what-is-displayed). *(f) OUT:* no new
aggregates, no editable anything, no "readiness" claims beyond computed
health.

---

## §4 My Week

*(a) Job:* the individual contributor's committed week — what I owe, what
I'm waiting on. *(g) Packet:* **D-PEC-31** (+ D-PEC-25 for drill wiring).

*(b) Layout:* committed items → checks owed → comments owed → waiting on
others → notifications. Empty tables get affirmative all-clear states (today
headers render over nothing, MyWeek.tsx:189-198). `window.prompt` at
MyWeek.tsx:241/246 replaced by Drawer forms (D-PEC-24 dialog primitive).

*(c) Metrics table:*

| # | Metric | Data basis | Existing field / projection | Drill target |
|---|---|---|---|---|
| M4.1 | Committed items (count + rows) | plan-stamped work | `myWeek().committed` (core/src/status.ts:741; view views.ts:561-564) | item drawer (existing) |
| M4.2 | Checks owed | checks where reviewer | `myWeek().checksOwed` (status.ts:741) | check drawer; deep link D-PEC-33 |
| M4.3 | Comments owed | open comments | `myWeek().commentsOwed` (status.ts:741) | comment drawer; deep link D-PEC-33 |
| M4.4 | Waiting on others (holds/decisions gating me) | gating records | `myWeek().waitingOnOthers` (status.ts:741; rows carry recordType-compatible kind/ref/id) | `<RecordRef>` → registers `?ref=` |
| M4.5 | Unread notifications (nav dot + list) | notification rows | GET `notifications?unread=` (api.ts:311) | notification → `<RecordRef>` where the payload carries recordType/id; else mark-read only |
| M4.6 | `[COND-OWNER]` Approvals/decisions owed to me | approval/decision authority rows | **P14** (conditional projection) | registers `?ref=` |

*(d) Drill paths:* M4.4/M4.5 are the two dead-ends fixed by D-PEC-25
(MyWeek.tsx:118-125, :140-148). *(e) RBAC:* work-item transition/progress/
evidence actions already server-guarded; no new mutations. *(f) OUT:* no
task board; no cross-user views. M4.6 activates only on the owner's inline
D-PEC-31 call (standing plan roadmap row).

---

## §5 Packages

*(a) Job:* scope ownership — each package's health, its open issues, and
what its lead owes this week. *(g) Packets:* **D-PEC-25** (drill spine),
**D-PEC-29** (linkage/chips).

*(b) Layout:* register (health/onPlan/openIssues + new issue-mix chips) →
detail page: breadcrumb (§2.2) → summary chips → issues cockpit (typed,
urgency-first, group toggles + per-type count chips) → needs-the-lead →
capacity (current week) → deliverables (workflow status).

*(c) Metrics table:*

| # | Metric | Data basis | Existing field / projection | Drill target |
|---|---|---|---|---|
| M5.1 | Register: package health | Explain | `packagesView[].health` (views.ts:194-205) | ExplainDrawer |
| M5.2 | Register: on-plan / total | deliverable status | `packagesView[].onPlan/total` (views.ts:199-204) | row → detail |
| M5.3 | Register: open issues count | typed union | `openIssueCount` (views.ts:173-192) | row → detail cockpit |
| M5.4 | Register: issue mix / worst-issue chip | per-type counts + max-urgency issue | **P7** `packagesView.issueMix` | detail cockpit pre-filtered by type |
| M5.5 | Detail summary (deliverablesOnPlan, openIssues, overdueIssues, holdsByCause, openHolds, openInterfaces, openDecisions, openRisks, openActionItems) | cockpit union | `packageDetailView.summary` (views.ts:316-326) | chips filter the cockpit table |
| M5.6 | Issues cockpit rows (type, ref, owner, needBy, overdue, ageWd/overdueWd, state) | 5-type union | `issues[]` (views.ts:251-276; sort :277-281) — ageWd basis fixed by **P4** | `<RecordRef>` per row (replaces `issueHref`, Packages.tsx:79-83) |
| M5.7 | Needs the lead this week | lead's queue | `needsLead[]` (views.ts:283-296; rows carry recordType/id/ref) | `<RecordRef>` per row |
| M5.8 | Package capacity rows (packageLoadH, disciplineLoadH, capacityH, pct, level) | plan items via `planItemIds` | `capacity.rows` (views.ts:300-314, returned :327, over core/src/plan.ts:209) | cell → Plan (§8); explain P5 once D-PEC-28 lands |
| M5.9 | Deliverables-in-package rows (workflow state, due) | deliverable rows | `packageDetailView.deliverables` (views.ts:332 ff.) | row → deliverable detail |

*(d) Drill paths:* cockpit and needs-lead rows route through `refRoute` with
`?ref=` (the F-class `issueHref` misroute — decisions/risks→/log,
interface→bare /registers, no highlight — is deleted); MDL "Package" cell on
§6 links back here. *(e) RBAC:* read-only page apart from existing
package-pack report link. *(f) OUT:* no issue mutation from the cockpit; no
duplicate issue store — the cockpit renders typed source records only
(principle 1).

---

## §6 Deliverables

*(a) Job:* document workflow — where each deliverable is in its lifecycle
and what blocks its next transition. *(g) Packets:* **D-PEC-25** (drill),
**D-PEC-29** (risks on detail, breadcrumb, MDL package link), **D-PEC-32**
`[COND-SLATE-5]` (model completeness).

*(b) Layout:* MDL register (filters unchanged) → detail: breadcrumb →
workflow stages → facts strip → open items (typed tables incl. new Risks) →
transitions (gated, with `beforeIssue` explain) → evidence/history.
`window.prompt` sites (Deliverables.tsx:151, :653, :659) replaced by Drawer
forms.

*(c) Metrics table:*

| # | Metric | Data basis | Existing field / projection | Drill target |
|---|---|---|---|---|
| M6.1 | MDL rows (state, package, due, hold badges) | deliverable rows | `deliverablesView` (route api.ts:121-129) | row → detail; Package cell → §5 detail (new link) |
| M6.2 | Detail health/status facts (distinct booleans) | facts | `facts{}` (views.ts:445-454) | n/a (facts strip; each fact names its records) |
| M6.3 | Open items: work items | anchored open work | `openItems.workItems` (views.ts:421-423) | drawer; deep link D-PEC-33 |
| M6.4 | Open items: checks (openComments/totalComments, checklistDone/Total) | checks on current rev | `openItems.checks` (views.ts:424-430) | drawer; deep link D-PEC-33 |
| M6.5 | Open items: comments | open review comments | `openItems.comments` (views.ts:431-432) | drawer; deep link D-PEC-33 |
| M6.6 | Open items: holds | active holds on deliverable/rev | `openItems.holds` (views.ts:433) | `<RecordRef>` → holds register |
| M6.7 | Open items: approval records | revision approvals | `openItems.approvalRecords` (views.ts:434) | `<RecordRef>` → approvals register |
| M6.8 | Open items: decision dependencies | open decision conditions | `openItems.decisionDependencies` (views.ts:435-438) | `<RecordRef>` → decisions register |
| M6.9 | Open items: **risks** (new) | risks with `deliverableId` = this | **P6** `openItems.risks` | `<RecordRef>` → risks register |
| M6.10 | Transition gate explain | TransitionExplanation | `beforeIssue` (views.ts:466); GET `revisions/:id/explain` (api.ts:180) | contributing refs via `<RecordRef>` |
| M6.11 | Related records panel (optional) | link edges | **P8** `relatedRecordsView` | `<RecordRef>` per edge |

*(d) Drill paths:* every cross-record reference renders as a `<RecordRef>`;
today the detail metadata card grid renders Package as dead text
(Deliverables.tsx:164, card grid :184-190) and the typed open-items tables
are inert (~Deliverables.tsx:200-291, :268-291). *(e) RBAC:* existing
transition/check/comment/approval actions stay server-guarded; forms shown
only where the relevant `can/:action` probe (api.ts:155-158) affirms.
*(f) OUT:* merged-out peer idea "issue chips on MDL rows" (§1.1); no
interface/decision→deliverable links until `[COND-SLATE-5]` D-PEC-32 adds
the FKs (core/src/types.ts:492-506 and :416-446 today have none).

---

## §7 Action & Hold Log

*(a) Job:* issue awareness + triage — "what is open, what is overdue, what
is falling through" — a dashboard, NOT a task manager (owner steer verbatim
in the standing plan). *(g) Packet:* **D-PEC-27**.

*(b) Layout:* KPI band (M7.1–M7.5, each click-to-explain) → pure-CSS
three-segment aging strip (click-to-filter) `[COND-SLATE-3: deferrable under
a leaner-first-cut ruling]` → controls row (group-by select `[COND-SLATE-3:
deferrable under a leaner-first-cut ruling]` · quick-view presets
`[COND-SLATE-3: deferrable under a leaner-first-cut ruling]` · filters incl.
area as a `<select>` of known values) →
register (color-typed Type column via existing `.itype-*` classes — defined
styles.css:111-120, already used by the package issues cockpit
(Packages.tsx:87 renders `itype itype-${r.type}`) but unused by the Log page,
whose LogHome renders Type as plain text (LogHome.tsx:90);
`state` column rendered; redundant Anchor column dropped; default sort
overdue-first) → triage queue surfaced as a KPI deep-link into the retained,
unchanged disposition workflow (api.ts:298-301). Quick-view URL presets:
**Overdue · Aging>5 · Holds-by-cause · Untriaged · Mine** (URL params only;
last-used may persist in localStorage — no server state). Split-pane row
workbench: `[COND-SLATE-3]` only.

*(c) Metrics table:*

| # | Metric | Data basis | Existing field / projection | Drill target |
|---|---|---|---|---|
| M7.1 | Open by type (work_item/hold/interface/intake + decision/risk after P2) | widened union | **P1** `logSummaryView.openByType` | filters register by type; Explain contributing[] |
| M7.2 | Overdue count | row `overdue` flags | **P1** `logSummaryView.overdue` | preset Overdue |
| M7.3 | Aging buckets (0–2 / 3–5 / >5 wd; ">5" KPI) | row `ageWd`/`overdueWd` (post-P4 basis) | **P1** `logSummaryView.aging` | aging strip segment → filtered register |
| M7.4 | Untriaged intake count + oldest (wd) | intake rows | **P1** `logSummaryView.untriaged` (basis exists: `intakeQueueView.untriagedAgeWd`, views.ts:568-582) | deep-link to triage queue |
| M7.5 | Active holds (count, by cause) | hold rows | **P1** `logSummaryView.activeHolds` | preset Holds-by-cause |
| M7.6 | Register rows (type, ref, title, package, owner, state, age/overdue basis, needBy) | typed union | `logRegisterView` (views.ts:491-557) widened by **P2**; package attribution fixed by **P3**; age basis fixed by **P4** | `<RecordRef>` per row (rows are inert today, LogHome.tsx:158-159) |
| M7.7 | Group-by section headers (none/owner/package/cause) + per-group row counts | client regroup of loaded M7.6 rows | display aggregation over **P2** rows (sanctioned by adopted D-PEC-27 scope; export-what-is-displayed) | rows within group |
| M7.8 | Dispositioned intake list | dispositioned rows | GET `intake?state=dispositioned` (api.ts:298; view views.ts:568-582) | intake `<RecordRef>` (`/log?ref=`) |

*(d) Drill paths:* every KPI's ExplainDrawer lists real `contributing[]`
refs (I-4 discipline — a bare number is a spec violation); every register
row routes via `<RecordRef>`. *(e) RBAC:* triage actions (open-triage,
disposition) stay the existing guarded POSTs; no new mutations; intake
statements remain verbatim (OM-3) and unanchored items stay visible (I-2 —
the `anchorStatus:'unanchored'` flag, views.ts:542, is never hidden by
default views). *(f) OUT:* no board, no inline status edits, no bulk
mutation, no editable severity (principle 6 + fences corollary).

---

## §8 Plan

*(a) Job:* weekly planning control — commit a credible week: what's
eligible, what's planned, does it fit capacity. *(g) Packets:* **D-PEC-28**;
WBS view **D-PEC-28b** `[COND-SLATE-4]`.

*(b) Layout:* readiness header (M8.1) → planning intake/backlog rail (M8.2;
empty horizon lanes route here) → Now/Next/Later horizons with rollups
(M8.3) → discipline×week capacity heatmap (M8.4–M8.6) → six-week lookahead
(M8.7) → shifts "needs my review" (M8.8) → commit control (week-selectable,
readiness checklist). Native `<input type="week">`/week-`<select>` and
discipline `<select>` replace free text (Plan.tsx:290-292, :351-353, :397).
Plan-item edit wires the **existing PUT** `plan-items/:id` (api.ts:148 —
zero web callers today; Plan.tsx calls only POST create :256 and POST shift
:324). Raise-risk gets confirm + preview ("may create", honest) and drops
fabricated scores (F2). Lookahead gets a legend, distinct check/work marks,
sticky first column, current-week highlight.

*(c) Metrics table:*

| # | Metric | Data basis | Existing field / projection | Drill target |
|---|---|---|---|---|
| M8.1 | Readiness header: current week · commit status · planned hours · capacity coverage · unplanned-eligible count · schedule coverage · blockers | plan payload + derived | week: `planView.currentWeek` (plan.ts:523); commit status: `periods[].state` (plan.ts:526-528); unplanned-eligible: `plannable.length` (plan.ts:509-525, **existing** — §1.3 D1); planned hours / capacity coverage / blockers / schedule coverage: **P9** `planReadinessView` (Explain each; schedule coverage beyond raw `scheduleActivityCount` plan.ts:539 is `[COND-SLATE-4]`) | each headline chip → ExplainDrawer; unplanned → backlog rail |
| M8.2 | Backlog rail rows (eligible-but-unplanned, grouped by source/owner/package/due) | plannable records | membership: `planView.plannable` (plan.ts:509-520); grouping enrichment (owner/package/due fields): **P9** | row → create-plan-item form (existing POST); ref via `<RecordRef>` where routable |
| M8.3 | Horizon rollups (WIP count + hours per Now/Next/Later, per-discipline) + "fits capacity?" chip | plan items vs capacity | **P9** `planReadinessView.horizons` (Explain; server-computed per principle 2) | chip → ExplainDrawer → contributing plan items |
| M8.4 | Capacity cell % + level | capacity cells | `capacityView` (core/src/plan.ts:181-219; `CapacityCell` :166-178) | cell → **P5** explain |
| M8.5 | Capacity cell work/check/approve mini stacked bar | per-type hours | `CapacityCell.byType` (core/src/plan.ts:175, filled :208) | same P5 explain |
| M8.6 | Capacity cell contributing plan items | ids | `CapacityCell.planItemIds` (core/src/plan.ts:177, filled :209) | **P5** `planCellExplain` → items → `<RecordRef>` |
| M8.7 | Lookahead cells (per deliverable × week; doc-no, package, due) | lookahead rows | `planView.lookahead` (plan.ts:532-536) | cell → **P5** explain; doc-no → deliverable detail (inert today, Plan.tsx:198) |
| M8.8 | Shifts needing my review (count + rows, reject-with-reason) | proposed shifts | `planView.shifts` (plan.ts:538, rows plan.ts:490-501); review POST accepts `note` (plan.ts:273-277 — §1.3 D3) | row → shift drawer |
| M8.9 | Commit readiness checklist (what stamps into My Week, what's excluded) | commit preview | **P9** `planReadinessView.commitPreview` (over `commitWeek` logic, plan.ts:336+; week-selectable per §1.3 D3) | checklist rows → `<RecordRef>` |
| M8.10 | `[COND-SLATE-4]` WBS tree/week-grid (baseline vs actual, % complete, variance-days) | imported schedule rows | **P10** `planScheduleView` (source: `schedule_activity`, server/src/db.ts:581-599; WBS cols db.ts:726-732; today only `scheduleActivityCount` reaches /plan, plan.ts:539) | activity → schedule register `?ref=` semantics; deliverableRef → detail |

*(d) Drill paths:* every capacity %, lookahead cell, and readiness chip is
click-to-explain (the current bypass — Plan.tsx:165-169, :204-207 — is an
F-class defect of principle 1); deliverable doc-nos link to detail.
*(e) RBAC:* commit/capacity/shift-review actions gated on their existing
server permissions (`plan.commit` plan.ts:337, `plan.review` plan.ts:280);
forms shown per `can/:action` probe. *(f) OUT:* no Gantt library, no
critical path (PEC imports WBS parentage, not logic links — principle 3),
no drag-to-mutate (drag may at most open the governed shift drawer), no
client-side capacity math (principle 2).

---

## §9 Registers

*(a) Job:* the authoritative typed registers — complete, scannable,
consistent. *(g) Packet:* **D-PEC-30**.

*(b) Layout:* `role="tablist"` tab bar with read-only tabs (Schedule ·
Tracker) visually grouped/marked; unified row-actionability signal; wide
registers (16–17 cols) wrapped in `overflow-x` container with sticky Ref
column; hold-withdraw `window.prompt` (Registers.tsx:1065) → Drawer form;
Schedule tab brought to Tracker parity (agent context, deep-link/highlight);
optional per-tab summary strip; docstring refreshed (says "Five", ships
seven — Registers.tsx:1-7 vs TABS Registers.tsx:18-26).

*(c) Metrics table:*

| # | Metric | Data basis | Existing field / projection | Drill target |
|---|---|---|---|---|
| M9.1 | Approvals rows (latencyWd, outcome, prerequisites) | approval records | `approvalRegisterView` (views.ts:584-600) | row drawer; `?ref=` highlight |
| M9.2 | Decisions rows (overdueDays, links[]) | decisions | `decisionRegisterView` (views.ts:602-612) | linked records via `<RecordRef>` |
| M9.3 | Risks rows | raw risks (no derivation — no age basis exists, §1.3 D2) | `riskRegisterView` (views.ts:614-617) | row drawer |
| M9.4 | Interfaces rows (overdueWd, aging vs thresholds) | derived | `interfaceRegisterView` (views.ts:651-676; overdueWd :665; aging :671-672) | row drawer |
| M9.5 | Holds rows (ageWd, targets[]) | derived | `holdRegisterView` (views.ts:678-691) | targets via `<RecordRef>` |
| M9.6 | Schedule rows (WBS: outlineLevel indent, %complete, baseline, package, deliverableRef) | import-owned | `scheduleRegisterView` (views.ts:628-642) | deliverableRef → detail; package → §5 |
| M9.7 | Tracker rows | import-owned | `trackerRegisterView` (views.ts:621-623) | deliverable/package cells → `<RecordRef>`-style links |
| M9.8 | Optional per-tab summary strip (e.g. overdue/red counts) | loaded rows' existing per-row signals (M9.1–M9.5 fields) | client display aggregation over the loaded register (sanctioned by adopted D-PEC-30 scope; export-what-is-displayed) | strip segment filters the tab |

*(d) Drill paths:* reference cells (today dead text, Registers.tsx:87)
render via `<RecordRef>`; `?ref=` highlight already works (RegisterTable).
*(e) RBAC:* existing create/edit/resolve/withdraw forms stay; gate their
visibility on `can/:action`. *(f) OUT:* no bulk edit; Schedule/Tracker stay
import-owned read-only (D-PEC-23 posture).

---

## §10 Admin

*(a) Job:* operational control of the project instance — import, exchange,
thresholds, people, evidence — with high-risk actions visually fenced
(principle 7). *(g) Packet:* **D-PEC-26**.

*(b) Layout:* route-tabbed `admin/:section` (reusing the Registers
`registers/:tab` pattern): **Import** (proposals-first: list + states +
dry-run summary + hash-bound accept/apply; import-history feed; direct/force
import demoted behind a labeled, confirm-gated danger boundary with **no
visual parity** to proposal apply) · **Exports & data exchange** (grouped,
described; report links; templates) · **Thresholds** (grouped by signal
family, warn/escalate adjacent, "drives: <signal>" link per group,
client+server validation, override-vs-default visibility) · **People**
(directory + real role pills + role→capability matrix; renamed "People
directory" unless `[COND-SLATE-2]` rules the assignment route) ·
**Activity / system evidence** (audit trail via `HistoryTrail`; app/version/
DB-basis notice; recent proposal states; runbook links). All write forms
gated on server `can/:action` probes (api.ts:155-158) — never client-
invented RBAC; reject-reason `window.prompt` (Admin.tsx:177) → Drawer form.

*(c) Metrics table:*

| # | Metric | Data basis | Existing field / projection | Drill target |
|---|---|---|---|---|
| M10.1 | Import proposal list + per-state counts | proposal rows | GET `import-proposals` (api.ts:349-374) | proposal detail drawer (existing GET :id) |
| M10.2 | Import/config activity feed | audit rows | **P11** `adminActivityView` (writer exists: `repo.audit`, server/src/repo.ts:197; config audit written api.ts:421-427; record-scoped reader `historyFor` repo.ts:190 / api.ts:321 is insufficient for a project-wide feed) | feed row → record via `<RecordRef>` where routable |
| M10.3 | Effective thresholds (grouped) | merged config | GET `config` (api.ts:394-399; `DEFAULT_THRESHOLDS` core/src/types.ts:99) | "drives: <signal>" → Overview signal explain |
| M10.4 | Override-vs-default per threshold | raw row vs defaults | **P12** config `{defaults, overrides, effective}` split | n/a (display) |
| M10.5 | People directory rows | people | GET `/api/people` (api.ts:112-116) | person row detail |
| M10.6 | Role pills + role→capability matrix | project_role rows + permission map | **P13** `projectPeopleView` (table server/src/db.ts:94-99; no read route today — §1.3 D4) | matrix cell → static capability description |
| M10.7 | System evidence (app/version, project, DB/demo basis, proposal states) | config + build info + M10.1 | GET `config` (api.ts:394-399) + client build constant + M10.1 fields | runbook links (static) |

*(d) Drill paths:* thresholds → the Overview signals they drive; activity
rows → records. *(e) RBAC:* import + config forms require `config.manage`
(server: api.ts:326, :401); UI additionally probes `can/config.manage`
before showing forms (today forms show to all members and 403 on submit).
*(f) OUT:* no role **assignment** route unless `[COND-SLATE-2]` rules it
(Tier O — no such route exists, §1.3 D4); no import-behavior changes
(D-PEC-14/15/19 stay postponed); direct import is demoted, not removed.

---

## §11 Data contract inventory

### §11A Existing contracts relied on (live-verified 2026-07-08)

| ID | Contract | Citation | Consumed by |
|---|---|---|---|
| E1 | `overviewView` — health, 5 Explain KPIs, signals[], packageRollup, waitingOnYou, topBlockers, schedulePressure | server/src/services/views.ts:70-145 (kpis :89-95; blockers :77-84; pressure :124-143) | §3 |
| E2 | `packagesView` + `openIssueCount` (holds+interfaces+decisions+risks+actions, log-scoped) | views.ts:194-205; :173-192 | §5 |
| E3 | `packageDetailView` — **`issues[]` composed server-side** (5-type union, sorted overdue→age→needBy), `needsLead[]`, capacity rows over `planItemIds`, summary | views.ts:207-360 (issues :251-276, sort :277-281, returned :329; needsLead :283-296; capacity :300-314, returned :327; summary :316-326) | §5 |
| E4 | `deliverableDetailView.openItems` — workItems, checks, comments, holds, approvalRecords, decisionDependencies; **no risks key** — + `facts{}`, `beforeIssue` | views.ts:419-439; :445-454; :466 | §6 |
| E5 | `logRegisterView` — union of work_item/hold/interface_item/intake_item ONLY; hold `packageId: null` hardcoded; interface `ageWd: 0` hardcoded; sorted `ageWd` desc | views.ts:491-557 (hold pkg :520; iface age :531; sort :556) | §7 |
| E6 | `intakeQueueView` — `untriagedAgeWd`, links[] | views.ts:568-582 | §7 |
| E7 | `myWeekView` → core `myWeek` — {week, committed, checksOwed, commentsOwed, waitingOnOthers} | views.ts:561-564; core/src/status.ts:649-741 | §4 |
| E8 | `planView` — currentWeek, **`plannable[]`**, periods, horizons, lookahead, capacity, shifts, scheduleActivityCount | server/src/services/plan.ts:522-540 (plannable :509-520) | §8 |
| E9 | `capacityView` / `CapacityCell` — pct, level, `byType`, **`planItemIds`** | core/src/plan.ts:181-219 (cell type :166-178; byType :175/:208; planItemIds :177/:209) | §3, §5, §8 |
| E10 | Register views: approvals :584-600 (latencyWd), decisions :602-612 (overdueDays, links), risks :614-617 (**raw, no derivation**), tracker :621-623, schedule :628-642 (WBS), interfaces :651-676 (**working `overdueWd` pattern :665**, aging :671-672), holds :678-691 (ageWd, targets) | server/src/services/views.ts as cited | §9 |
| E11 | `Explain` shape `{value, ruleId, detail, threshold?, contributing[]}` + `ContributingRef` | core/src/types.ts:46-52; :38-43; web mirror web/src/api.ts:63-69 | all Explain emitters; every P-row below |
| E12 | `refRoute` coverage map + `useHighlightRef` + row-flash; **default → null** for work_item/revision/review_comment/check | web/src/shared.tsx:47-60; :63-66 | §2.6, all surfaces |
| E13 | Thresholds: `DEFAULT_THRESHOLDS`; GET merges defaults (effective values); **PUT persists `thresholds` via blind `JSON.stringify` — no shape/bounds validation** | core/src/types.ts:99; server/src/api.ts:394-399; :400-429 (stringify :405-411; audit :421-427) | §10, §12 F3 |
| E14 | `can/:action` probe — **path segment cast to `PermissionAction` unvalidated** | server/src/api.ts:155-158 | all RBAC gating; §12 F3 |
| E15 | MyWeek payload + notifications (separate endpoint) + record history | api.ts:311-313 (notifications); :321 (history); repo.historyFor server/src/repo.ts:190; repo.audit :197 | §4, §10 |
| E16 | Plan mutations: **PUT `plan-items/:id` exists with no web caller** (Plan.tsx POSTs only, :256/:324); `reviewPlanShift` accepts optional `note` (plan.ts:273-277); `commitWeek` accepts any valid ISO week (plan.ts:336-338) | server/src/api.ts:148; plan.ts as cited | §8 |
| E17 | `schedule_activity` table + WBS columns; only `scheduleActivityCount` reaches /plan | server/src/db.ts:581-599; :726-732; plan.ts:539 | §8 M8.10, §9 M9.6 |
| E18 | `project_role` table; internal reads only; `GET /api/people` returns id/name/email/discipline | server/src/db.ts:94-99; auth.ts:68; api.ts:87,104; :112-116 | §10 |
| E19 | Exports/reports/import: `export/:register` CSV, sponsor-brief, package-pack, `import/:contract` (requireCan `config.manage`), import-proposals CRUD | api.ts:331; :337; :341; :325-330; :349-374 | §3, §5, §10 |
| E20 | UI vocabulary: KpiCard, HealthBadge, Drawer (shared.tsx:175-190), RegisterTable (onRowClick/exportName/highlightRef), WorkflowStages, HistoryTrail, StateTag, `.itype-*` classes (defined styles.css:111-120; used by the package issues cockpit, Packages.tsx:87 `itype itype-${r.type}`, but unused by the Log page — LogHome renders Type as plain text, LogHome.tsx:90); 64 hex in styles.css + 2 inline tsx; 7 `window.prompt` sites (Deliverables.tsx:151/653/659, MyWeek.tsx:241/246, Registers.tsx:1065, Admin.tsx:177) | as cited | §2, all surfaces |
| E21 | `deliverablesView` — MDL rows (state, package, due, hold badges) | views.ts:375-399; route api.ts:121-129 | §6 M6.1 |

### §11B Named new read-only projections (all Tier S; Explain-shaped where they carry counts)

Payload sketches use `Explain<V> = {value, ruleId, detail, contributing[]}`
(E11). Route names are indicative; the implementing packet fixes final
naming. **None of these mutates anything**; RBAC visibility scoping
(`logsFor`/redaction, views.ts:43-66) applies to every `contributing[]`.

| ID | Name | Route / view | Payload sketch | Consuming surface | Packet |
|---|---|---|---|---|---|
| P1 | `logSummaryView` | GET `log/summary` (server/src/services/views.ts + api.ts) | `{ openByType: Explain<Record<type,number>>, overdue: Explain<number>, aging: Explain<{buckets: {label,count}[]}>, untriaged: Explain<{count, oldestWd}>, activeHolds: Explain<{count, byCause}> }` — each `contributing[]` = the rows behind the number | §7 M7.1–M7.5 | D-PEC-27 |
| P2 | `logRegisterView` widened to **decision + risk** rows | same view (views.ts:491-557) | adds decision rows (basis: state ≠ decided/superseded, `overdueDays` pattern views.ts:609) and risk rows (state ≠ closed; **no `log` field on Risk** — visibility scoping is the packet's design point, `[COND-SLATE-5]` for the full fix via D-PEC-32) | §7 M7.6 | D-PEC-27 |
| P3 | Hold `packageId` population | same view, hold loop (views.ts:520) | derive via `holdLinks` × `isInPackage` (views.ts:160-167 — resolves deliverable/revision/work_item, 3 of 10 target types today; **widening beyond 3 types is `[COND-SLATE-5]`** D-PEC-32) | §7 M7.6 package filter/grouping | D-PEC-27 |
| P4 | Interface/risk age basis fix | views.ts:260 (iface, pkg cockpit), :270 (risk, pkg cockpit), :531 (iface, log) | replace hardcoded `ageWd: 0` with needBy-based `overdueWd = workingDaysOverdue(needBy, today, cal)` — the proven `interfaceRegisterView` pattern (views.ts:665). **No creation timestamp exists on either type (§1.3 D2)**, so the column is honestly relabeled overdue-basis, and the union sort (views.ts:277-281, :556) stops sinking old items | §5 M5.6, §7 M7.3/M7.6, §12 F1 | D-PEC-27 (+ cockpit sites) |
| P5 | `planCellExplain` | GET `plan/explain?week&discipline` (or embedded per-cell in planView) | `Explain<{pct}>` with `detail` = loadH/capacityH/byType and `contributing[]` = plan items from `planItemIds` (E9) resolved to refs | §8 M8.4–M8.7; §3 M3.11 / §5 M5.8 cells once landed | D-PEC-28 |
| P6 | `openItems.risks` | `deliverableDetailView` (views.ts:419-439) | risks where `deliverableId === id` and state ≠ closed (fields exist, core/src/types.ts:472; already counted in `openIssueCount` views.ts:184-186) | §6 M6.9 | D-PEC-29 |
| P7 | `packagesView.issueMix` | `packagesView` (views.ts:194-205) | per package: `Explain<{byType: Record<type,number>, worst: {ref, recordType, id, basis}}>` — same membership as `openIssueCount` (views.ts:173-192), exposed by type instead of collapsed | §5 M5.4 | D-PEC-29 |
| P8 | `relatedRecordsView` (optional) | GET `records/:recordType/:id/links` | typed edges from existing link tables: `holdLinks`, `decisionLinks`, conditions, risk `packageId`/`deliverableId` — `{edges: [{recordType, id, ref, why}]}` (ContributingRef shape) | §6 M6.11; §5 cockpit context | D-PEC-29 |
| P9 | `planReadinessView` | folded into GET `plan` payload (plan.ts:522-540) | `{ plannedHours: Explain<number>, capacityCoverage: Explain<pct>, horizons: Explain<{perHorizon: {count, hours, byDiscipline}}>, fitsCapacity: Explain<boolean>, blockers: Explain<number>, commitPreview: {stamps[], excluded[]}, backlog: plannable[] enriched with {ownerId, packageId, needBy} }` — count/membership basis is the existing `plannable` (E8, §1.3 D1); schedule-coverage element `[COND-SLATE-4]` | §8 M8.1–M8.3, M8.9 | D-PEC-28 |
| P10 | `planScheduleView` `[COND-SLATE-4]` | joined into GET `plan` | WBS rows (rowType, outlineLevel, parentActivityId, percentComplete, durationDays, baselineStart/Finish — db.ts:726-732) + package/deliverableRef resolution as in `scheduleRegisterView` (views.ts:628-642); read-only; no logic links, no critical path | §8 M8.10 | D-PEC-28b |
| P11 | `adminActivityView` | GET `admin/activity` | project-scoped audit/import feed: recent `audit` rows (writer repo.ts:197) + import-proposal state transitions; `[{at, actorId, action, recordType, recordId, ref?}]`; read-only | §10 M10.2 | D-PEC-26 |
| P12 | Config override visibility | GET `config` widened (api.ts:394-399) | `{ thresholds: { defaults, overrides, effective } }` instead of pre-merged only — Admin shows which values are project overrides vs shipped defaults | §10 M10.4 | D-PEC-26 |
| P13 | `projectPeopleView` | GET `people` widened or `admin/people` | people rows + their `project_role` rows (db.ts:94-99) + a server-emitted role→capability matrix (from the permission map behind `can()`); **read-only — the assignment route is `[COND-SLATE-2]`, Tier O, NOT specced here** | §10 M10.5–M10.6 | D-PEC-26 |
| P14 | `[COND-OWNER]` MyWeek approvals/decisions-owed | `myWeekView` widened (views.ts:561-564) | approval records where `signatoryIds` ∋ me and state ready; decisions where `authorityId` = me and pending (both derivable from existing rows, cf. `needsLead` views.ts:283-296) | §4 M4.6 | D-PEC-31 (owner-open inline call) |

**Server-side fixes riding packets (not projections, listed for
completeness; detail in §12):** threshold shape/bounds validation on PUT
`/config` and validation of the `can/:action` path segment — both D-PEC-26
(F3).

**Fence notes:** P8 (`GET records/:recordType/:id/links`) requires route
registration in `server/src/api.ts`, so D-PEC-29's ruled fence must include
`server/src/api.ts` (the standing plan's indicative fence omits it). P14
widens `myWeekView` in `server/src/services/views.ts`, so D-PEC-31's ruled
fence must include that file (the indicative fence lists only the two page
files).

---

## §12 Factual-correctness fixes register

The three standing violations of the owner's "report only what is factual
and has a clear basis" value (Receipt 51). These are the redesign's
first-order obligations (principle 3: fix wrongly-shown values first).

| ID | Violation (live sites) | Fix owner | Acceptance statement |
|---|---|---|---|
| F1 | **Interface/risk Age-0 + mis-sort.** `ageWd: 0` hardcoded for interface rows at views.ts:260 (package cockpit) and views.ts:531 (log register), and for risk rows at views.ts:270; the age-desc sorts (views.ts:277-281, :556) therefore sink every old interface/risk below fresher items. No creation timestamp exists on either type (core/src/types.ts:464-487, :492-506). | **D-PEC-27** (log register + summary) with the package-cockpit sites riding whichever of D-PEC-27/29 first touches views.ts (per its ruled fence) | No surface displays a fabricated 0 age: interface/risk rows show a needBy-based `overdueWd` (pattern: views.ts:665) or an explicit "—" where needBy is null; union sorts order these rows by that basis; column labeling states the basis. Verified by pec belt-and-braces + a register/cockpit visual pass showing an old open interface sorting above a fresh one. |
| F2 | **Plan raise-risk fabricates scores + dup-creates.** `raiseCapacityRisk` POSTs `probability: 4, impact: 3` hardcoded regardless of the overload (web/src/pages/Plan.tsx:65) and re-clicking creates duplicate risks with no confirm/preview (button Plan.tsx:171-174). | **D-PEC-34** *(dated pointer 2026-07-08: re-homed from D-PEC-28 — D-PEC-28/28b deferred by the adopted reporting-first amendment, `_DomainEngines/proposals/pec/PLAN_AMENDMENT_2026-07-08_reporting_first.md` §3(c)–(d))* | The create call sends **no probability/impact** (fields are nullable, core/src/types.ts:474-475) unless a human enters them in the confirm drawer; a preview names the week/discipline/load basis verbatim and says "may create"; a second invocation for the same cell surfaces the existing risk ref instead of silently duplicating. Verified by drill test + visual pass. |
| F3 | **Threshold write path accepts garbage; permission probe unvalidated.** PUT `/config` blindly `JSON.stringify`s `thresholds` — no numeric/key/bounds checks, so `warn > escalate` and negatives persist and silently corrupt computed severity (api.ts:405-411; defaults merged only on GET, :398). `can/:action` casts the path segment to `PermissionAction` with no validation (api.ts:156-157). | **D-PEC-26** | Server PUT rejects unknown threshold keys, non-numeric/negative values, and any warn>escalate pair with a 400 naming the offending key; the Admin client validates the same rules pre-submit; `can/:action` rejects (or returns false for) actions outside the known `PermissionAction` set. Verified by server tests on the PUT path + belt-and-braces. |

---

## §13 Exit-criterion checklist (T0 gate)

Every count/metric proposed in §§3–10 maps to an existing server field
(cited) or a named §11B projection. **70 metric rows; 0 unmapped.**

| Metric | Mapping |
|---|---|
| M3.1 health | E1 views.ts:88 |
| M3.2 pctOnPlan | E1 views.ts:90 |
| M3.3 holdsByCause | E1 views.ts:91 |
| M3.4 openDecisions | E1 views.ts:92 |
| M3.5 approvalsInFlight | E1 views.ts:93 |
| M3.6 scheduleForecastWd | E1 views.ts:94 |
| M3.7 signals[] | E1 views.ts:98 |
| M3.8 packageRollup counts | E1 views.ts:99-113 |
| M3.9 waitingOnYou | E1 views.ts:73,116 |
| M3.10 topBlockers | E1 views.ts:77-84 |
| M3.11 schedulePressure | E1 views.ts:124-143 |
| M4.1 committed | E7 status.ts:741 |
| M4.2 checksOwed | E7 status.ts:741 |
| M4.3 commentsOwed | E7 status.ts:741 |
| M4.4 waitingOnOthers | E7 status.ts:741 |
| M4.5 notifications | E15 api.ts:311 |
| M4.6 approvals/decisions owed | P14 `[COND-OWNER]` |
| M5.1 pkg health | E2 views.ts:194-205 |
| M5.2 onPlan/total | E2 views.ts:199-204 |
| M5.3 openIssues | E2 views.ts:173-192 |
| M5.4 issue mix / worst chip | P7 |
| M5.5 detail summary chips | E3 views.ts:316-326 |
| M5.6 cockpit issues[] | E3 views.ts:251-276 (+P4 basis) |
| M5.7 needsLead | E3 views.ts:283-296 |
| M5.8 pkg capacity rows | E3 views.ts:300-314 / E9 plan.ts:209 |
| M5.9 pkg deliverables | E3 views.ts:332 ff. |
| M6.1 MDL rows | E21 `deliverablesView` views.ts:375-399, route api.ts:121-129 |
| M6.2 facts | E4 views.ts:445-454 |
| M6.3 openItems.workItems | E4 views.ts:421-423 |
| M6.4 openItems.checks | E4 views.ts:424-430 |
| M6.5 openItems.comments | E4 views.ts:431-432 |
| M6.6 openItems.holds | E4 views.ts:433 |
| M6.7 openItems.approvalRecords | E4 views.ts:434 |
| M6.8 openItems.decisionDependencies | E4 views.ts:435-438 |
| M6.9 openItems.risks | P6 |
| M6.10 beforeIssue explain | E4 views.ts:466; api.ts:180 |
| M6.11 related records | P8 (optional) |
| M7.1 open by type | P1 (rows via P2) |
| M7.2 overdue | P1 |
| M7.3 aging buckets | P1 (basis P4) |
| M7.4 untriaged + oldest | P1 (basis E6 views.ts:568-582) |
| M7.5 active holds | P1 |
| M7.6 register rows | E5 views.ts:491-557 + P2/P3/P4 |
| M7.7 group-by headers | client display aggregation over P2 rows (adopted-plan-sanctioned; no new server truth) |
| M7.8 dispositioned list | E6 / api.ts:298 |
| M8.1 readiness header | E8 plan.ts:523,:526,:509-525 + P9 (schedule element `[COND-SLATE-4]`) |
| M8.2 backlog rail | E8 plan.ts:509-520 + P9 enrichment |
| M8.3 horizon rollups + fits chip | P9 |
| M8.4 capacity pct/level | E9 core/plan.ts:181-219 |
| M8.5 byType bar | E9 core/plan.ts:175,:208 |
| M8.6 cell contributors | E9 core/plan.ts:177,:209 → P5 |
| M8.7 lookahead cells | E8 plan.ts:532-536 (+P5 explain) |
| M8.8 shifts needing review | E8 plan.ts:538,:490-501; note E16 plan.ts:273-277 |
| M8.9 commit readiness checklist | P9 commitPreview (over plan.ts:336+) |
| M8.10 WBS view | P10 `[COND-SLATE-4]` |
| M9.1 approvals rows | E10 views.ts:584-600 |
| M9.2 decisions rows | E10 views.ts:602-612 |
| M9.3 risks rows | E10 views.ts:614-617 |
| M9.4 interfaces rows | E10 views.ts:651-676 |
| M9.5 holds rows | E10 views.ts:678-691 |
| M9.6 schedule rows | E10 views.ts:628-642 |
| M9.7 tracker rows | E10 views.ts:621-623 |
| M9.8 per-tab summary strip | client display aggregation over the loaded tab's E10 fields (adopted-plan-sanctioned, optional) |
| M10.1 proposal list/states | E19 api.ts:349-374 |
| M10.2 activity feed | P11 |
| M10.3 effective thresholds | E13 api.ts:394-399 |
| M10.4 override-vs-default | P12 |
| M10.5 people directory | E18 api.ts:112-116 |
| M10.6 role pills + matrix | P13 |
| M10.7 system evidence | E13 api.ts:394-399 + M10.1 + client build constant (no count) |

(70 rows listed; 66 carry counts/values — M6.11, M9.8, M10.7 and M7.7 are
display compositions whose every underlying number is itself mapped above.
No unmapped count remains. Exit criterion **met**.)

---

## §14 Conditional-on-slate matrix

Slate items are the standing plan's "Open owner decisions" 1–6. Nothing
below activates without the owner's ruling; rows not listed are unaffected.

| Slate item | Ruling → effect on this spec |
|---|---|
| **1. Zero-new-dependency posture** | *Confirm (recommended in plan):* spec stands as written — all §§2–10 visuals are hand-written CSS + inline SVG. *Decline / allow a library:* §2.4 tokens, §7 aging strip, §8 heatmap/lookahead marks, and §8 M8.10 rendering re-open as design questions; every affected packet must restate its visual approach; F-PEC-3 still requires each dependency to be its own owner decision. |
| **2. Admin role management** | *Rename-only:* §10 People section ships read-only as specced (P13); title "People directory". *Assignment route ruled in:* adds a Tier-O write route + form to §10 (new spec section required — NOT covered here); P13 remains its read basis; `can/:action` gating per §10(e). |
| **3. Log dashboard depth* | *Full band, no workbench (recommended):* §7 stands as written. *Workbench in:* adds a split-pane row detail (record summary, source links, package/deliverable context, contributing history, existing allowed actions — peer proposal vocabulary) to §7(b); no new mutations either way. *Leaner first cut:* M7.1–M7.5 band ships; aging strip/group-by/presets defer to a follow-up packet. |
| **4. Plan schedule view (D-PEC-28b)** | *Now:* P10 + M8.10 activate; M8.1's schedule-coverage element gains its linked/unlinked basis. *Later/not:* M8.10 and P10 dormant; M8.1 shows only the existing `scheduleActivityCount` (plan.ts:539) as "imported activities" with no coverage claim (principle 3). |
| **5. Issue-model completeness (D-PEC-32)** | *Pursue:* Risk gains `log` (fixing P2's visibility-scoping caveat), interfaces/decisions gain deliverable FKs (enabling §6 interface/decision open-items rows — new M-rows in a spec addendum), `isInPackage` widens beyond 3 of 10 hold target types (completing P3). *Accept under-counts:* P2 ships with documented risk-visibility caveat; P3 ships partial (3 resolvable types) with the basis stated in the UI; §6 stays deliverable-FK-less. Either way the shipped numbers state their true basis. |
| **6. Dark mode** | *Now:* D-PEC-24 ships the toggle (`prefers-color-scheme` + `:root[data-theme]` override + persisted preference) over §2.4's semantic tokens. *Defer:* §2.4 token layer lands unchanged; toggle is a later S-effort packet. No other section depends on this. |

---

*End of T0 spec. Subsequent D-PEC packets cite sections/rows by ID
(e.g. "§7 M7.3", "§11B P4", "§12 F2").*
