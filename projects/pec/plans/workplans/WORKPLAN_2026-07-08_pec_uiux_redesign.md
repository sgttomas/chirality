# PEC Work Loop — standing plan (UI/UX redesign phase)

> **SUPERSEDED (2026-07-09) — RETIRED into `.archive/` (2026-07-09, owner
> direction, Receipt 70):** this file is no longer the loop's standing plan.
> The owner-directed successor is
> `_DomainEngines/pec/WORKPLAN_2026-07-09_pec_reporting_product.md` (the
> newest — and now only — `WORKPLAN_*.md` in the loop directory, which
> LOOP_INIT §2 reads as the standing plan), authored from the 2026-07-08
> product-direction interview whose findings of record live in
> `_DomainEngines/proposals/pec/FINDINGS_2026-07-09_pec_product_interview.md`;
> see `LOOP_RECEIPTS.md` Receipts 69–70. The owner-intent quotes, loop
> protocol, and fences F-PEC-1..4 are carried forward into the successor; the
> ruled in-flight packets (D-PEC-30/31/35/36/37) execute on their own rulings
> and are carried as pointers there. This file is retained unedited below for
> the record.

> **Epistemic status: agent-authored plan — not authority.** Authored 2026-07-08
> at owner direction (Ryan Tufts, K-AUTH-1) as the owner-directed **synthesis of
> the two colocated CANDIDATE redesign proposals** in
> `_DomainEngines/proposals/pec/` (provenance below; synthesis reasoning in
> `LOOP_RECEIPTS.md` Receipt 57). It supersedes
> `.archive/WORKPLAN_2026-07-04_pec_loop.md` (retired into `.archive/` at owner
> direction 2026-07-08, Receipt 58) as the loop's standing plan (LOOP_INIT §2)
> and carries the **loop protocol, fences F-PEC-1..4, and the owner gate
> unchanged** from it. This plan never authorizes work: owner-adopted
> specifications and owner rulings/directions do — every roadmap tranche below
> is a future owner-ruled D-PEC source-tranche. Sources govern on any
> disagreement. This file is a PROTOCOL plus pointer indexes; it carries NO
> status, NO work history, and NO measurements — each loop iteration re-derives
> state from the live tree, and loop closes append a minimal receipt to
> `_DomainEngines/pec/LOOP_RECEIPTS.md` (rules live at the top of that file).

## Owner intent (the goal's single durable home — carried forward + current)

**The standing goal** (adopted via D-T0-15 O-A, 2026-07-04): *keep the pec
project surface governably aligned with the framework and move the pec standing
plan forward as far as live authority permits.* The founding direction of
record ("I want to create a new development loop to implement this plan," said
of `plans/pec_bridge_integration_plan_2026-07-04.md`) and the registration
history live in Receipts 0–3; that implementation goal is discharged.

**Addendum (2026-07-04, owner direction of record — verbatim in Receipt 4):**
the staged integration ladder is a core inherent goal of the project: *"That's
exactly the progression this needs to follow from L1, L2 to L3. It's one of the
core inherent goals of the project now."* The ladder has since been climbed at
owner ruling (D-T0-17 L1 acceptance; D-T0-18 + D-PEC-12 `OPERATION_PROPOSAL`);
the governing posture — advance only rung-by-rung at owner ruling — stands.

**Addendum (2026-07-07, owner direction of record — verbatim in Receipt 51):**
*"What I would say is that future refinement of the interface and importing
should be indefinitely postponed. My intention now is to simplify workflows and
reinforce only reporting on what is factual and has a clear basis."* — D-PEC-14
/15/19 remain indefinitely postponed; factual, clear-basis reporting remains a
standing value that selection weighs.

**Addendum (2026-07-08, owner direction of record — verbatim in Receipts 55/56;
the redesign phase's north star):**

> "The demo application is now over the minimum viable threshold. There remains
> lots of poor UI and UX design choices, particularly the Admin page. The
> Packages and Deliverables are well linked but it's not clear if the issues
> are. The Action & Hold Log has a good schema but isn't a well designed page it
> is a terrible task management interface - for now it should just be a good
> dashboard with comprehensive tools and an intuitive and contemporary
> interface. The Plan page has some good ideas but is a very poor implementation
> and needs to be redesigned to be an effective UI that utilizes the best
> practices and known patterns in this domain."

This steer reactivates UI/UX work (LOOP_INIT §7: a newer specific per-run steer
governs over the Receipt-51 postponement — the D-PEC-23 precedent), and this
plan's adoption makes the reactivation standing for the redesign phase. The
reconciliation is recorded, not silent: **the redesign is in service of the
2026-07-07 value, not against it** — its through-line is clarity and factual,
drill-to-source reporting (fixing wrongly-shown values, restoring the drill
spine, refusing invented data), and the Log becomes **a dashboard, not a
heavier task manager**. D-PEC-14/15/19 stay postponed; nothing here reopens
import-refinement or the tracker edit path as objectives.

*Reconciliation note (2026-07-08):* the 2026-07-07 direction that "importing
should be indefinitely postponed" (Receipt 51) is **selectively narrowed** by
the newer 2026-07-08 reporting-first direction (a newer specific steer governs
— LOOP_INIT §7, the D-PEC-23 precedent): the import lane reactivates **only**
as the agent-adaptive, proposal-gated document-upload path (the
D-PEC-08/D-PEC-22 pattern: agent maps → import proposal → human accept/apply;
no direct writes). The D-PEC-14/15/19 rulings otherwise stand — no
live-evidence obligation reopens, the FILE_DROP_RUNBOOK v1.2 step-5 interim
re-import rule stands, and the tracker stays import-owned/read-only.

**Synthesis direction (2026-07-08, owner launcher steer — this plan's mandate,
verbatim in Receipt 57):** the owner directed that the two candidate proposals
be read in full, the strongest of each be taken, and the result be authored as
the newest-sorting `WORKPLAN_*.md` superseding `WORKPLAN_2026-07-04_pec_loop.md`,
with protocol/fences/gate carried unchanged, conflicts decided on the merits
and recorded, and each source tranche remaining future owner-ruled.

**Addendum (2026-07-08, owner direction of record — verbatim in the adopting
receipt (Receipt 60); this phase's north star):**

> "Good.  Now My intention for this continuing development phase is to
> produce an effective reporting tool for project status, according to
> issues tracked at a package level and completeness tracked at a
> deliverable level.  I don't need this to be task management or planning
> or scheduling platform at this time.  It can possibly grow into those
> functions but to begin with I want to be able to upload documents that
> allow the issues and status to be updated, and the for the agent to
> produce reports (both standard reports and novel user-defined)."

With four same-day owner clarification selections: (1) defer D-PEC-28/28b,
keep the F2 fix on an earlier tranche; (2) upload = agent-adaptive
structured files via the proposal-gated D-PEC-08/22 pattern; (3) reporting
= drill-backed exported documents from Explain-shaped server data,
user-defined via agent prompt; (4) this landed as a reviewed amendment
(`_DomainEngines/proposals/pec/PLAN_AMENDMENT_2026-07-08_reporting_first.md`).
The UI/UX redesign continues **in service of** reporting-first: the drill
spine, factual-correctness fixes, and package/deliverable surfaces are what
make reports interrogable.

## Provenance (pointer index — the full design detail lives here)

- **Operator proposal:** `_DomainEngines/proposals/pec/PLAN_2026-07-08_pec_uiux_redesign.md`
  — diagnosis, per-surface target designs, tiers, tranche table, decision slate —
  with `PLAN_2026-07-08_pec_uiux_redesign.appendix.md` (**69-defect verified
  register**, every row cited `file:line`, adversarially verified).
- **Peer proposal:** `_DomainEngines/proposals/pec/WORKPLAN_2026-07-08_pec_ui_redesign.md`
  — standing-plan form, product design principles, target information
  architecture, design-spec-first tranche 0 — with screenshot evidence under
  `_DomainEngines/proposals/pec/PEC_2026-07-08_ui-redesign-planning/`
  (MANIFEST + 9 captures of the live TWD demo).
- **Synthesis decisions + verification:** `LOOP_RECEIPTS.md` Receipt 57. Both
  proposals remain unedited provenance; where either disagrees with the live
  tree, the live tree wins.

## Why the gate structure remains (the compelling reasons)

1. **Adoption, ruling, and direction are human acts** (K-AUTH-1; D-GOV-04): no
   agent fills a `HumanRuling`; deliverable work lands as CANDIDATE briefs or
   proposed decision packets terminating at the owner.
2. **Every redesign tranche is fenced work in pec source** — F-PEC-1 forbids
   `web/**`, `server/**`, `core/**` writes by default, so each roadmap item
   executes only under its own owner-ruled D-PEC source-tranche naming an exact
   file fence (the D-PEC-08 / D-PEC-17 / D-PEC-20..23 precedent).
3. **Fences F-PEC-1..4** (below) bound what any tranche may touch regardless of
   ambition (D-T0-15 ratified the standing set).

## The loop protocol (every iteration — carried unchanged in structure)

0. **Discover (mandatory core).** Clean `git` state and branch awareness (log
   since the last receipt; concurrent loops exist — keep write scopes disjoint
   from `_DomainEngines/bridge/**` and both sibling project subtrees); read the
   latest receipt(s) in `_DomainEngines/pec/LOOP_RECEIPTS.md`; check the tier-0
   decision register AND the pec project register for rulings newer than the
   last receipt — new rulings are how work unlocks, look every time.
   `PYTHONDONTWRITEBYTECODE=1` harness `self-check`; full harness pytest at
   discovery only if `tools/**` changed since the last receipt (always mandatory
   at closeout — step 4). **K-INVENT-1 note:** verify a harness command's pec
   citizenship live before invoking it (`self-check`, `coord-check`,
   `bridge-status`, and full pytest are the deterministic checks of record;
   never fabricate pec `status`/`drift`/`next`/`brief` rows). Verify any
   derivative statement — this plan, either proposal, and your own tasking —
   against the live tree before relying on it; on disagreement the live tree
   wins and the delta goes in the receipt.
1. **Select.** The widest lawful tranche(s) now, re-derived. Principles, in
   order: (a) work that discharges a gate prerequisite beats work that doesn't;
   (b) owner-directed items beat agent-inferred ones; (c) doc/design-level
   before any binding; (d) within the redesign phase, the roadmap's phase order
   below (foundation → owner's named pains → linkage/polish → owner-gated model
   work) is the default sequence; coordination/control artifacts beyond this
   plan's inventory take explicit owner direction.
2. **Brief / slate.** Deliverable-shaped redesign work is proposed as a **D-PEC
   decision packet** (continuing the numbered series from the live register)
   carrying: scope, exact write fence, dependencies, verification plan,
   rollback, and the owner gate — the D-PEC-23 vehicle. Non-source design/spec
   work (roadmap step T0) is proposed and executed as coordination-surface
   documents inside F-PEC-1's carve-out, still branch-first + PR.
3. **Gate.** STOP; adoption/ruling/direction is the owner's act (K-AUTH-1;
   D-GOV-04). Directions/rulings given in-session are quoted verbatim in the
   receipt and recorded in their governed artifact as part of execution. Record
   every gate outcome in the receipt — including no-ops and their reason.
4. **Execute + check.** Branch-first + PR unless the owner directs main-direct;
   never self-merge; mutually exclusive write scopes when parallel (and always
   disjoint from concurrent loops'). Inside fences + standing constraints.
   Checks per work type at the exact final commit SHA of each PR (any edit
   after a check run invalidates that run — re-run at the final SHA):
   - **always:** repo-wide `self-check` exit 0 with conscious live-pin updates
     riding the same PR; `coord-check` on the branch diff; `git diff --check`;
     adversarial review of citations + git-diff scope containment (⊆ fence).
   - **if `tools/**` changed:** FULL harness pytest including the live-baseline
     suite.
   - **if pec source changed:** pec belt-and-braces
     (`npm run typecheck && npm test && npm run build && npm run drill` green)
     PLUS a visual pass on every changed surface — browser screenshots at a
     ~1280px desktop viewport and one narrow/mobile viewport, keyboard
     operability of changed interactions, no blank pages/overflow/overlap.
   - **if the profile changed:** profile validator VALID.
   CI green; owner merges.
5. **Receipt.** Append a minimal receipt to `_DomainEngines/pec/LOOP_RECEIPTS.md`
   per its local rules — pointers, verbatim owner directions, gate outcomes,
   check pass/fail. No narrative here or anywhere else. Next iteration starts
   at 0.

## Session conventions — task-dependent subagent model selection

The convention's durable home is `LOOP_INIT.md` §7 (owner-revised 2026-07-05;
a per-run steer may override). This plan applies it to the redesign phase's
work types so each iteration selects the model by task, not by habit:

- **`opus`** — Step-0 discovery and register/receipt reads; codebase and
  contemporary-pattern research; summaries; running the deterministic checks
  (`self-check`, `coord-check`, pytest, pec belt-and-braces); breadth
  verification sweeps; screenshot/evidence capture drives.
- **`fable` at `high` reasoning effort** — planning work (the T0 design spec;
  D-PEC packet drafting); adversarial verification of anything that will be
  recorded as fact (defect claims, citations, receipt load-bearing lines,
  Explain-shape drill verification); and execution that touches governed
  artifacts, fences, or rulings — which includes every D-PEC-24..33 source
  tranche.
- **`fable` at `low` effort** — mechanical execution of fully specified
  changes only (e.g. applying an already-verified token rename across files).
- **Fallback:** model unavailability never blocks a tranche — complete the
  task on `opus` and record the salvage in the receipt (Receipts 54/56
  precedent).

## Standing constraints — fences F-PEC-1..4 (all iterations; D-T0-15 ratified)

- **F-PEC-1 (engine truth):** no writes under `projects/pec/**` except
  `execution/_Coordination/**`, `AGENTS.md`, and the one-time `docs/STATUS.md`
  pointer edit sanctioned in the registration packet; never `pec.db`/`-wal`/
  `-shm`, `backups/**`, `core/**`, `server/**`, `web/**`, `tools/**`,
  `fixtures/**`, or root manifests; never run the pec server or a mutating CLI
  against a non-scratch DB.
- **F-PEC-2 (lifecycle/status):** no invention or file-level mutation of pec
  record states — approvals, checks, decisions, holds exist only as app-created
  RBAC'd append-only records or cited owner statements; no pilot-readiness,
  go-live, or issuance claims.
- **F-PEC-3 (release/egress):** no `npm publish` or release/packaging act; no
  new pec runtime dependencies (ADR-002 zero-dep posture); no pec
  instance-content egress beyond the profile's ruled `data_residency` basis.
- **F-PEC-4 (tier-0 scope):** tier-0 writes only under `_DomainEngines/pec/**`
  and `_DomainEngines/proposals/pec/**`; never the ADOPTED
  `profiles/open_pipe_stress.yaml`, closed snapshots, sealed logs, other loops'
  surfaces, or the three owner-retained self-check fixtures.
  *Grant note (2026-07-06, owner D-T0-19 O-1A ruling — dated pointer, no fence
  rewrite):* the fence set gains the enumerated app-dev **decision/coordination
  packet** paths (`projects/chirality-app-dev/execution/_Coordination/_DECISIONS/**`
  rows authored as PROPOSALs by this loop); app-dev **source** stays behind
  D-APP rulings.
- **Redesign-phase corollaries (from the owner intent + ADR-002, binding on
  every tranche):** each tranche's ruling opens F-PEC-1 for exactly its named
  files, nothing more; **zero new runtime/web dependencies** (React 18 + Vite +
  react-router + the hand-written `styles.css` + inline SVG — no charting,
  component, or CSS-framework library; any proposed dependency is its own
  explicit owner decision); computed status is never hand-settable; monitoring
  surfaces never grow drag-to-mutate boards, editable status, or bulk state
  edits; export-what-is-displayed, verbatim intake statements (OM-3),
  unanchored-stays-visible (I-2), and append-only history are never regressed.

## Redesign basis (diagnosis — detail lives in the provenance, not here)

One root cause underlies most of the 69 verified defects: **the app's
signature drill-to-source spine (I-4) is unwired or broken exactly where it
matters most, and mouse-only where it is wired** — the package issues cockpit
misroutes issue types (`issueHref` vs `refRoute`), Log/My Week/detail/register
rows are inert, and `KpiCard`/rows/reflinks are keyboard-unreachable. Three
factual-correctness defects violate the standing "report only what is factual"
value outright (open interfaces all show Age 0 and mis-sort; Plan "raise risk"
fabricates 4×3 scores and dup-creates; thresholds accept warn > escalate and
negatives, silently corrupting computed severity). The screenshots add the
empirical state: an empty Plan page whose primary action is "Commit week" with
no planning intake, readiness, or use of the 127 imported schedule activities.
The **feasibility gift**: the server already composes most needed data (package
`issues[]`, deliverable `openItems`, `capacityView.planItemIds`, schedule WBS
rows), so the highest-value redesign is largely UI re-wiring and re-composition
— zero new dependencies, modest read-side server work.

## Vision

> PEC should read as **one honest instrument**: every surface answers its own
> headline question at a glance, every number is interrogable to the records
> that produced it, and every reference is one accessible click from its
> source. The redesign adds no invented data and no task-manager machinery — it
> makes what is already computed *legible, navigable, and trustworthy*, by
> mouse and keyboard.

## Design principles (govern every tranche)

1. **Drill or it doesn't ship.** Every badge, KPI, aging bar, and record ref is
   click-to-explain and/or routes through `refRoute` to its source; every count
   carries a rule/source basis. Aggregation never duplicates truth — issues
   remain typed source records (I-4).
2. **Compute on the server, render on the web.** No new rollups, thresholds, or
   status in React (SPEC §1). New aggregates are server views emitting the
   existing `Explain` shape `{value, ruleId, detail, contributing[]}`.
3. **Factual or absent.** Show only what records support: no fabricated scores,
   no critical path (PEC imports WBS parentage, not logic links), no
   hand-settable computed values (F-PEC-2). Fix wrongly-shown values first.
4. **Re-compose, don't re-import.** Build from the existing vocabulary — cards,
   `KpiCard`, `HealthBadge`, `Drawer`, `RegisterTable`, badges/state/itype
   tags, `WorkflowStages` — plus tiny hand-rolled inline-SVG marks. Zero new
   deps.
5. **Accessible by construction.** Real `<button>`/`<a href>` for actions,
   `:focus-visible` rings, `role`/`aria` on dialogs and tablists, keyboard
   operability, AA contrast. The drill spine must be reachable without a mouse.
6. **Dashboards, not task managers — one primary job per page.** Admin is
   operational control, Log is issue awareness + triage, Plan is weekly
   planning control, Packages are scope ownership, Deliverables are document
   workflow. Monitoring surfaces summarize "what is off-plan / falling
   through" first and never grow mutation machinery.
7. **High-risk actions are visually fenced.** Import apply, direct/force
   import, threshold changes, and destructive/demo-state actions are visually
   and structurally separated from read/export tasks, confirm-gated, and shown
   only to actors the server says can perform them (`can/:action` probe — never
   client-invented RBAC).
8. **Dense, contemporary, non-marketing UI.** Restrained dashboards, filters,
   tabs, sticky summary bars, status chips, drawers; no hero sections,
   decorative cards, or narrative onboarding copy.
9. **Theming through tokens only.** All color flows through a two-tier token
   layer (primitive palette + semantic roles); any theme work swaps semantic
   tokens, never per-component hex.
10. **Preserve the guarantees** enumerated in the fences corollary above; a
    redesign never regresses them.

*Scope note (2026-07-08 direction):* task management, planning, and
scheduling functions are **explicitly out of scope for this phase**. The
owner's direction allows that the tool "can possibly grow into those
functions" — that growth is a possible future phase behind its own owner
direction, and principle 6 ("Dashboards, not task managers") governs until
then.

## Data-readiness tiers (honest cost basis for sequencing)

- **Tier U — UI only** (zero new deps, no server change): drill re-wiring,
  accessibility, tokens, Admin/Log/Plan re-composition over existing payloads.
- **Tier S — read-side server** (still zero-dep `node:sqlite`): Explain-shaped
  `logSummaryView`; widen `logRegisterView` to decisions + risks; fix hold
  `packageId` + interface `ageWd`; join schedule WBS into `/plan`; expose link
  edges + unmerged threshold overrides; server threshold validation.
- **Tier M — schema/model migration (owner-gated):** `Risk.log` field;
  interface/decision deliverable FKs; widen `isInPackage`; deep-linkable
  drawer records.
- **Tier O — owner decisions (no default):** a `project_role` assignment route
  (none exists today); model-extension scope; dark mode; Log workbench depth;
  confirmation of the zero-new-dependency posture.

## Roadmap — fenced, phased candidate tranches

**T0 (design spec — doc-only, no source ruling needed, next lawful step on
adoption of this plan).** Author the redesign **design specification + data
contract inventory** under `projects/pec/execution/_Coordination/**` (F-PEC-1
carve-out): freeze each page's job, required metrics, drill paths, and
existing/new API needs, merging the per-surface target designs from BOTH
proposals (operator §5.1–5.8; peer "Target information architecture"). Exit
when every proposed dashboard count maps to an existing server field or a named
new read-only projection in the `Explain` shape. Branch-first + PR; owner
merges. Each subsequent D-PEC packet then cites the spec instead of re-deriving
design.

Each row below lands as its own proposed decision packet (numbered live from
the register — D-PEC-24.. as of authoring) with an exact write fence,
dependencies, verification plan, and the owner gate. Effort S/M/L/XL.

| Phase | Candidate packet | Scope (summary — spec detail in T0 + provenance) | Indicative fence | Deps | Tier | Effort |
|---|---|---|---|---|---|---|
| P0 | **D-PEC-24 · Design-system & a11y foundation** | Two-tier tokens (migrate ~30 hardcoded hex); global `:focus-visible`; AA badge contrast; `Drawer` → real dialog (role/aria/focus trap+restore); `KpiCard`/rows/reflinks keyboard-operable; sidebar grouping (six lenses vs Registers/Admin); breadcrumb primitive; project switcher keeps lens; Sign-out a real button. Dark-mode toggle only if slate item 6 says now. | `web/src/styles.css`, `web/src/shared.tsx`, `web/src/main.tsx` | T0 | U | M |
| P0 | **D-PEC-25 · Drill-to-source spine** | Shared `<RecordRef>` rendering `.reflink` + routing via `refRoute` with `?ref=`; fix `issueHref` misroute; wire Log rows, package cockpit + "Needs the lead", deliverable-detail cross-record tables, My Week waiting/notifications, Plan doc-nos, Registers reference cells; graceful null-route handling (`work_item`/drawer-only records — completed by D-PEC-33) | `web/src/shared.tsx`, `web/src/pages/*` | D-PEC-24 | U | M |
| P0 | **D-PEC-26 · Admin → operations console** | Route-tabbed Admin (Registers `registers/:tab` pattern): Import (proposals-first with import-history feed; direct/force import demoted behind a labeled, confirm-gated danger boundary) · Exports & data exchange (grouped, described) · Thresholds (grouped by signal family, warn/escalate adjacency, "drives: <signal>" links, validation in client AND server PUT, override-vs-default visibility) · People (real role pills + role→capability matrix; rename honestly to "People directory" unless slate item 2 rules the assignment route) · Activity/system evidence (audit trail via `HistoryTrail` + app/version/DB-basis notice). Gate write forms on server `can/:action` probes; replace `window.prompt` with Drawer forms | `web/src/pages/Admin.tsx`, `web/src/main.tsx`; `server/src/api.ts` (validation, overrides) | D-PEC-24/25 | U+S (role route = O) | L |
| P0 | **D-PEC-27 · Action & Hold Log → issue dashboard** | Server `logSummaryView` emitting `Explain`-shaped aggregates; KPI band (Open-by-type · Overdue · Aging>5wd · Untriaged intake + oldest · Active holds — each click-to-explain); pure-CSS aging strip (click-to-filter); group-by none/owner/package/cause over loaded rows; quick-view URL presets (Overdue · Aging>5 · Holds-by-cause · Untriaged · Mine — peer's saved-view vocabulary, zero-infra); color-typed Type column; render `state`, drop redundant Anchor column; default sort overdue-first; widen view to decisions + risks; fix hold `packageId` (via widened attribution as ruled) + interface `ageWd`; area filter becomes a select. Triage disposition workflow retained unchanged, surfaced as a queue KPI deep-link; split-pane row workbench only if slate item 3 rules it in. No board, no inline status edits, no bulk mutation | `server/src/services/views.ts`, `server/src/api.ts`, `web/src/pages/LogHome.tsx`, `web/src/shared.tsx` | D-PEC-24/25 | U+S | L |
| P0 | **D-PEC-34 · Plan factual-correctness fix (F2) — minimal** | Raise-risk stops fabricating `probability: 4, impact: 3` (Plan.tsx:65): create call sends no scores unless a human enters them (nullable per core/src/types.ts:474-475); confirm drawer previews the week/discipline/load basis verbatim and says "may create"; duplicate-guard per spec §12 F2 acceptance via the existing `GET /api/projects/:pid/risks` (api.ts:275, already client-consumed at Registers.tsx:629 — read, not a fence write). No other Plan change | `web/src/pages/Plan.tsx` | T0 | U | S |
| P1 | **D-PEC-29 · Packages/Deliverables issue linkage** | Risks surfaced on deliverable detail (server: add to `openItems` — data exists); register-level issue context (issue mix / worst-issue chips beside the count); breadcrumbs both detail pages; MDL Package cell → link/filter; cockpit group toggles + count chips; optional Related-records panel from server link edges | `server/src/services/views.ts`, `web/src/pages/{Packages,Deliverables}.tsx`, `web/src/shared.tsx` | D-PEC-25 | U+S | M |
| P2 | **D-PEC-30 · Registers consistency** | Unify row-actionability signal; `role="tablist"` + read-only tab grouping/marking; overflow container + sticky Ref column on wide registers; withdraw `window.prompt` → Drawer; Schedule tab parity (agent context, deep-link, highlight); optional per-tab summary strip; fresh docstring | `web/src/pages/Registers.tsx`, `web/src/shared.tsx` | D-PEC-24/25 | U | M |
| P2 | **D-PEC-31 · Overview & My Week polish** | Drill-fixes; affirmative all-clear empty states; consistent CSV export; sponsor-brief as a real labeled action, not a KPI look-alike; unify severity vocabulary (green/amber/red); remove dead import; (owner) decisions/approvals-owed on My Week | `web/src/pages/{Overview,MyWeek}.tsx` | D-PEC-25 | U | S–M |
| PR | **D-PEC-35 · Upload lane — agent-adaptive structured-file ingestion** | Extend D-PEC-08/22: agent accepts registers/MDLs/trackers in arbitrary structured schemas (CSV/XLSX-derived/tabular), proposes a schema mapping to the §16/tracker contracts (extending `IMPORT_MAPPING.md` per FILE_DROP_RUNBOOK step 2), files an import proposal; human accept/apply always; **no direct writes, ever**; unmappable rows are questions or rejects with reasons, never guesses. Runbook rules (RV-7 approval-follows-proposal, v1.2 step-5 re-import interim rule) carry unchanged | `projects/pec/agent-sidecar/**`, `execution/_Coordination/IMPORT_TEMPLATES/**`; `server/src/api.ts` only if a new upload endpoint is needed (else none) | D-PEC-08/22 (landed); D-PEC-26 improves the accept/apply surface but is not a hard dep | S | M |
| PR | **D-PEC-36 · Reporting lane — standard report set** | Agent composes drill-backed **exported documents** from Explain-shaped server data (spec E-rows + P1/P7/P6 as landed): weekly project status (overviewView basis), package issue summary (packageDetailView.issues[] / logSummaryView), deliverable completeness/MDL status (deliverablesView + openItems/facts) — the owner's three named examples. Every figure carries its rule-id/register basis per REPORT_BASIS.md ("names its basis by pointer"); **factual-or-absent** — reports contain only what records support; export-what-is-displayed / no-invented-data guarantees apply; export format/egress stays inside the profile's ruled `data_residency` basis (F-PEC-3) | `projects/pec/agent-sidecar/**`; `server/src/services/views.ts` + `server/src/api.ts` only for named read-only report payloads | D-PEC-25 (drill-backs); D-PEC-27 enriches the issue summary (soft) | S | M |
| PR | **D-PEC-37 · Reporting lane — user-defined reports** | Novel reports via a prompt to the agent (the D-PEC-21 agentic-turn-loop vehicle, already RULED O-A: read acts → compose → export); same factual-or-absent constraint — a figure the records don't support is absent and said to be absent, never synthesized; in-app viewing of reports is explicitly **optional later**, not in scope | `projects/pec/agent-sidecar/**` | D-PEC-36 (report composition conventions), D-PEC-21 (landed) | S+O (any new export egress route is an owner call) | M |
| P3 | **D-PEC-32 · Issue-model completeness (owner-gated)** | `Risk.log` field + migration + register/visibility parity; interface/decision deliverable FKs; widen `isInPackage` beyond 3 of 10 hold target types | `core/src/types.ts`, `server/src/*`, `web/src/*` | D-PEC-27/29 | M | L |
| P3 | **D-PEC-33 · Deep-linkable drawer records** | Stable URLs (e.g. `?open=check:123`) for check/work_item/comment/revision; completes the traceability the spine starts | `web/src/shared.tsx`, `web/src/pages/*` | D-PEC-25 | M | M |

**Sequencing rationale (reporting-first).** Default order:
**24 → 25 → 27 → 29 → 26 → 30/31 → upload/reporting lanes (35/36/37) as
their packets are ruled → deferred planning phase (28/28b) last**, with
**D-PEC-34** riding early in parallel (Plan.tsx only — no `shared.tsx`
contention) so no surface reports invented data. 24/25 stay first as
force-multipliers; 27 and 29 rise because issues-at-package-level and
completeness-at-deliverable-level are the direction's two named axes; 26
follows (Admin is the upload lane's accept/apply surface and carries F3);
30/31 inherit the spine cheaply and polish the report drill targets. The
`shared.tsx` constraint is unchanged: tranches touching it (24/25/27/29/30)
run sequentially, never in parallel. P3 (32/33) remains owner-gated where
it sits; F1 stays on 27, F3 on 26, F2 on 34. Each tranche is independently
shippable behind its own PR; the peer proposal's regression-evidence pass
rides every tranche as the step-4 visual check rather than landing as a
separate tranche.

**Deferred (planning-phase) — owner clarification 1, 2026-07-08.**
D-PEC-28 (Plan → planning control board) and D-PEC-28b (Schedule WBS view)
are deferred, not deleted: the direction of record needs a reporting tool,
not a planning/scheduling platform, "at this time." Their full scope stays
specified in the T0 design spec (§8, §11B P5/P9/P10) and reactivates only
by owner direction, as the last phase. The Plan page is otherwise left
as-is, except fix F2, which is re-homed to **D-PEC-34** (above) so no
surface reports invented data while D-PEC-28 sleeps. Spec projections P5
and P9/P10 sleep with their packets; spec §3 M3.11 and §5 M5.8 cell-explains
("once D-PEC-28 lands") defer accordingly.

## Open owner decisions (the redesign slate — rule any time; none defaulted)

1. **Zero-new-dependency posture** — confirm hand-rolled CSS + inline SVG (no
   charting/component/CSS-framework library). *Recommend: yes.*
2. **Admin role management** — build a `project_role` assignment route (new
   zero-dep server work, Tier O), or keep assignment instance-admin-only and
   rename the section "People directory"? *Recommend: rename in D-PEC-26,
   decide the route separately.*
3. **Log dashboard depth** — full band (KPI + aging + group-by + quick-views)
   in D-PEC-27 as specified, and does a split-pane row workbench (peer
   proposal) ride it or stay out as task-manager creep? *Recommend: full band,
   workbench out for now — drill-through covers it.*
4. **Plan schedule view (D-PEC-28b)** — ~~open~~ **ANSWERED 2026-07-08:
   effectively ruled "defer"** by owner clarification 1 ("Defer both; keep
   F2 fix") under the reporting-first direction; lives in the Deferred
   (planning-phase) section.
5. **Issue-model completeness (D-PEC-32)** — pursue the schema migration, or
   accept the documented under-counts? *The one item touching data shape —
   squarely an owner call.*
6. **Dark mode** — ride D-PEC-24 now, or defer the toggle (tokens land either
   way)?

## Risks & watch-items

- **`shared.tsx` contention** — sequence, never parallelize, the tranches that
  touch it (24/25/27/28/29/30); keep write scopes disjoint (loop rule).
- **Explain-shape discipline** — Log/Plan KPI tiles must emit real
  `contributing[]` refs or they silently break I-4; verify each tile drills at
  step 4.
- **Scope creep toward a task manager** — reject any board/bulk-mutate/
  editable-status request against principle 6 and the owner's framing.
- **Partial `refRoute` coverage** — `work_item` and drawer-only records return
  `null` today; D-PEC-25 must degrade gracefully (no dead links) until
  D-PEC-33 completes them.
- **Model-agent availability** — select per the session-conventions section
  above; tranche execution never blocks on fable (Opus salvage precedent,
  Receipts 54/56).

## Where live work is re-derived (pointer index — never a status surface)

- **Decision registers** (open rows are the owner-gated surface):
  `_DomainEngines/_DECISIONS/_REGISTER.md` ·
  `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md` (D-PEC-XX
  rows — never bare `D-XX`).
- **The profile:** `_DomainEngines/profiles/pec.yaml` (ADOPTED; Gate 2 ruled
  2026-07-05; `integration_level` and `data_residency` are read live from it,
  never from prose) + its `_validation/` report; registry row in
  `_DomainEngines/DOMAIN_ENGINE_INDEX.md`.
- **Redesign provenance:** the two proposals + appendix + screenshot evidence
  under `_DomainEngines/proposals/pec/` (Provenance section above); the T0
  design spec under `projects/pec/execution/_Coordination/` once authored.
- **pec's own track:** `projects/pec/docs/STATUS.md`,
  `projects/pec/docs/TRACEABILITY.md`, conventions in `projects/pec/AGENTS.md`;
  operating runbooks in `projects/pec/execution/_Coordination/`
  (`LAUNCH_RUNBOOK.md`, `IMPORT_TEMPLATES/FILE_DROP_RUNBOOK.md`,
  `REPORT_BASIS.md`).
- **Cross-loop awareness:** `_DomainEngines/bridge/LOOP_RECEIPTS.md` (scope
  dedup only — this loop never writes other loops' surfaces).
- **Queued harness work:** `tools/practitioner_harness/BACKLOG.md`.
- **Handoff context** (owner directions, gate outcomes, stale-map deltas):
  `_DomainEngines/pec/LOOP_RECEIPTS.md`.
- **Superseded predecessor:** `.archive/WORKPLAN_2026-07-04_pec_loop.md`
  (registration → ladder phase; retired into `.archive/` at owner direction
  2026-07-08; kept unedited for the record apart from its dated
  supersession/retirement pointer).
