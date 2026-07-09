# PEC Work Loop — standing plan (reporting-product phase)

> **Epistemic status: agent-authored plan — not authority.** Authored
> 2026-07-09 at owner direction (Ryan Tufts, K-AUTH-1; direction of record in
> Receipt 70) as the successor standing plan for the reporting-product phase.
> It supersedes `.archive/WORKPLAN_2026-07-08_pec_uiux_redesign.md` (retired
> into `.archive/` at the same direction, Receipt 70) and carries the **loop
> protocol, fences F-PEC-1..4, and the owner gate unchanged** from it. This
> plan never authorizes work: owner-adopted specifications and owner
> rulings/directions do — every roadmap tranche below is a future owner-ruled
> D-PEC packet, and the carried in-flight packets execute on their own
> already-recorded rulings. Sources govern on any disagreement. This file is a
> PROTOCOL plus pointer indexes; it carries NO status, NO work history, and NO
> measurements — each loop iteration re-derives state from the live tree, and
> loop closes append a minimal receipt to
> `_DomainEngines/pec/LOOP_RECEIPTS.md` (rules live at the top of that file).

## Owner intent (the goal's single durable home — carried forward + current)

**The standing goal** (adopted via D-T0-15 O-A, 2026-07-04): *keep the pec
project surface governably aligned with the framework and move the pec
standing plan forward as far as live authority permits.* Registration history:
Receipts 0–3. The staged L1→L2→L3 integration ladder remains a core inherent
goal, advanced only rung-by-rung at owner ruling (Receipt 4; D-T0-17/18,
D-PEC-12).

**Carried addendum (2026-07-07, owner direction of record — verbatim in
Receipt 51):** *"My intention now is to simplify workflows and reinforce only
reporting on what is factual and has a clear basis."* Factual, clear-basis
reporting is a standing value that selection weighs. D-PEC-14/15/19 remain
indefinitely postponed; the import lane is reactivated **only** as the
agent-adaptive, proposal-gated path (the D-PEC-08/22 pattern), per the
Receipt-60-era reconciliation carried from the predecessor plan.

**Carried addendum (2026-07-08, owner direction of record — verbatim in
Receipt 60; the phase's north star):**

> "My intention for this continuing development phase is to produce an
> effective reporting tool for project status, according to issues tracked at
> a package level and completeness tracked at a deliverable level. I don't
> need this to be task management or planning or scheduling platform at this
> time. It can possibly grow into those functions but to begin with I want to
> be able to upload documents that allow the issues and status to be updated,
> and the for the agent to produce reports (both standard reports and novel
> user-defined)."

**New addendum (2026-07-08 product-direction interview; recorded 2026-07-09 —
this plan's mandate).** The owner elaborated the north star in a
product-direction interview. The findings and requirements of record live in
`_DomainEngines/proposals/pec/FINDINGS_2026-07-09_pec_product_interview.md`
(the detail home; receipt anchor Receipt 69, plus Receipt 70 for this plan's
authoring). The load-bearing intent, quoted or tightly paraphrased from that
record:

- **Operating model:** a PE/PD pair. The PE curates, vets, uploads, and
  prepares reporting with the sidecar agent; the agent maintains the database
  and drafts reports, resolving application-level issues with the PE
  (*"either automatically or in response to the human (configurable)"*); the
  Admin panel is *"optional manual way"*; the PD *"just uses this app as the
  interface to receive the information and have the ability to drill down
  into matters as they see fit."* Reports are edited and issued **outside the
  app** (*"The report lives outside this app in terms of the workflow. It may
  be saved in the app as a convenience"*).
- **The recurring deliverable** is a weekly status report organized **by
  discipline** per the owner-provided template (Activities with % complete ·
  Issuances this period · Needs, internal vs client · Risks); *"The 'monthly'
  report will be any aggregate of any number of weeks more than 1."*
- **Periods:** *"I will need to specify the dates being covered when I upload
  data"* — declared **per document uploaded**; overlaps/corrections are
  caught by in-app tools and resolved by the agent with the PE, not prevented
  by schema.
- **% complete** arrives as a PE-attested MDL integer (0–100) computed from
  externally maintained rules of credit. Discipline rollup: each deliverable
  type ("document kind" = the existing deliverable-type column) contributes
  equally, split across its document count; no hours-weighted rollup until
  hours exist.
- **Consistency:** MDL "on hold" status and RAIL hold-issues must agree;
  *"Discrepancies between the two should flag a review by the agent and a
  report to the human,"* caught by the intake/triage machinery.
- **A first-class discipline view** — the live, drillable mirror of the
  weekly report with a small derived-metric band (findings §5).
- **Prerequisites the owner will provide:** revised MDL/RAIL XLSX templates
  (hard prerequisite for contract v2, % complete, status vocabulary, and the
  D-PEC-35 XLSX follow-on); the interfaces document format; optionally the
  rules-of-credit table (reporting explanation only).

**Reconciliations (recorded, not silent):**

1. *% complete vs "computed status is never hand-settable" (F-PEC-2 and the
   fences corollary).* % complete is classified as a **PE-attested source
   fact arriving via import** — attested outside the app against external
   rules of credit — not an in-app derivation and not an in-app editable
   value. F-PEC-2 stands unchanged; no future tranche converts % complete
   into an in-app derivation or an in-app hand-set field.
2. *Reporting vocabulary of "issues."* The owner's client-facing vocabulary
   ("issues" = action items and risks, by package, with status and %
   complete) is **narrower** than the ADR-011 five-type package union. This
   is a display/reporting-vocabulary decision for report and dashboard
   surfaces; it does not reopen ADR-011, the cockpit's union, or the issue
   derivations. Holds, decisions, risks, and actions arrive via the RAIL/MDL
   uploads; interfaces via a separately uploaded document.

**Scope note (carried):** task management, planning, and scheduling functions
remain **out of scope for this phase** (Receipt 60; reaffirmed in the
D-PEC-31 ruling's rejection of O-B as "task-management gravity"). Growth into
those functions is a possible future phase behind its own owner direction;
"Dashboards, not task managers" governs until then. D-PEC-28/28b stay
deferred; D-PEC-32/33 stay owner-gated where the predecessor left them.

## Provenance (pointer index — the full design detail lives here)

- **Interview findings and requirements of record:**
  `_DomainEngines/proposals/pec/FINDINGS_2026-07-09_pec_product_interview.md`
  — operating model, report-template structure and data mapping, period/%
  semantics, discipline-view spec, prerequisites register, gap analysis.
- **The owner's discipline report template:**
  `2026-07-08-Disciplines_Status_Report.docx` — owner-held; its home in the
  tree is gitignored `projects/pec/pilot-scratch/` per the D-PEC-01
  convention; structure recorded in the findings §3.
- **Receipt anchors:** Receipts 60 (north star), 69 (interview context +
  riders on D-PEC-30/31/35/36/37), 70 (this plan's authoring direction).
- **Carried redesign provenance** (still cited by the in-flight packets): the
  two 2026-07-08 proposals + appendix + screenshot evidence under
  `_DomainEngines/proposals/pec/`, and the T0 design spec
  `projects/pec/execution/_Coordination/DESIGN_SPEC_2026-07-08_uiux_redesign.md`.
- **Reporting conventions:**
  `projects/pec/execution/_Coordination/REPORT_BASIS.md`; import runbook
  `projects/pec/execution/_Coordination/IMPORT_TEMPLATES/FILE_DROP_RUNBOOK.md`.

## Why the gate structure remains (the compelling reasons — carried unchanged)

1. **Adoption, ruling, and direction are human acts** (K-AUTH-1; D-GOV-04): no
   agent fills a `HumanRuling`; deliverable work lands as CANDIDATE briefs or
   proposed decision packets terminating at the owner.
2. **Every tranche is fenced work in pec source** — F-PEC-1 forbids
   `web/**`, `server/**`, `core/**` writes by default, so each roadmap item
   executes only under its own owner-ruled D-PEC packet naming an exact file
   fence (the D-PEC-08 / D-PEC-17 / D-PEC-20..38 precedent).
3. **Fences F-PEC-1..4** (below) bound what any tranche may touch regardless
   of ambition (D-T0-15 ratified the standing set).

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
   derivative statement — this plan, the findings document, and your own
   tasking — against the live tree before relying on it; on disagreement the
   live tree wins and the delta goes in the receipt.
1. **Select.** The widest lawful tranche(s) now, re-derived. Principles, in
   order: (a) work that discharges a gate prerequisite beats work that doesn't;
   (b) owner-directed items beat agent-inferred ones; (c) doc/design-level
   before any binding; (d) within this phase, the roadmap's default sequence
   below governs, and **owner-prerequisite-blocked rows are parked, never
   improvised around** — a blocked row unparks only when its named input
   exists in the tree or the owner provides it; coordination/control artifacts
   beyond this plan's inventory take explicit owner direction.
2. **Brief / slate.** Deliverable-shaped work is proposed as a **D-PEC
   decision packet** (continuing the numbered series from the live register)
   carrying: scope, exact write fence, dependencies, verification plan,
   rollback, and the owner gate. Non-source design/spec work is proposed and
   executed as coordination-surface documents inside F-PEC-1's carve-out,
   still branch-first + PR.
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

## Session conventions — task-dependent subagent model selection (carried)

The convention's durable home is `LOOP_INIT.md` §7 (owner-revised 2026-07-05;
a per-run steer may override). Applied to this phase's work types:

- **`opus`** — Step-0 discovery and register/receipt reads; codebase and
  report-format research; summaries; running the deterministic checks
  (`self-check`, `coord-check`, pytest, pec belt-and-braces); breadth
  verification sweeps; screenshot/evidence capture drives.
- **`fable` at `high` reasoning effort** — planning work (D-PEC packet
  drafting; contract/period-semantics design); adversarial verification of
  anything that will be recorded as fact (report payload correctness against
  REPORT_BASIS.md, template-conformance claims, citations, receipt
  load-bearing lines); and execution that touches governed artifacts, fences,
  or rulings — which includes every source tranche below.
- **`fable` at `low` effort** — mechanical execution of fully specified
  changes only.
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
- **Phase corollaries (binding on every tranche; carried and extended):**
  - each tranche's ruling opens F-PEC-1 for exactly its named files, nothing
    more;
  - **zero new pec runtime/web dependencies** (React 18 + Vite + react-router
    + hand-written `styles.css` + inline SVG). Two dependency decisions are
    **explicitly reserved to their own future rulings**, never defaulted: the
    XLSX/workbook parsing approach (the D-PEC-35 rider's follow-on) and the
    `.docx` generation approach for the discipline report (candidate row
    below) — each names its approach and any dependency, and where it runs
    (sidecar vs server), in its own packet;
  - computed status is never hand-settable; **PE-attested import data (e.g.
    % complete) is never in-app editable and never converted to an in-app
    derivation** (reconciliation 1 above);
  - monitoring surfaces never grow drag-to-mutate boards, editable status, or
    bulk state edits; export-what-is-displayed, verbatim intake statements
    (OM-3), unanchored-stays-visible (I-2), and append-only history are never
    regressed;
  - **factual-or-absent + period honesty:** every report figure carries its
    rule-id/register basis (REPORT_BASIS.md), and every period-scoped figure
    names the coverage declaration(s) it is computed from; a figure the
    records don't support is absent and said to be absent;
  - upload stays proposal-gated (agent maps → import proposal → human
    accept/apply; no direct writes, ever); the D-PEC-14/15/19 postponements
    and the tracker import-owned/read-only posture stand.

## Phase basis (pointer — detail lives in the findings, not here)

The reporting-product phase closes the distance between the ruled reporting
machinery (D-PEC-35/36/37 and the landed foundation) and the owner's actual
recurring deliverable and operating model. The authoritative statement of
that distance is the findings document's gap analysis (§7) — periods,
% complete, discipline view, `.docx` conformance, interfaces contract,
consistency checks, needs typing, vocabulary — verified against the live tree
at authoring. Re-verify against the live tree before relying on it.

## Vision

> PEC should let the PE run the weekly cycle end-to-end with the agent —
> upload vetted documents with declared coverage, resolve caught
> discrepancies, and produce a template-conformant discipline status report —
> while the PD reads the same story live: a discipline view whose every
> number is period-honest, drill-backed, and factual-or-absent. The app
> remains **one honest instrument**: reporting, never task management; no
> invented data; nothing shown that the records don't support.

## Design principles (govern every tranche; carried, with reporting additions)

1. **Drill or it doesn't ship.** Every badge, KPI, and record ref is
   click-to-explain and/or routes to source; every count carries a rule/source
   basis (I-4).
2. **Compute on the server, render on the web.** New aggregates are server
   views emitting the existing `Explain` shape (SPEC §1).
3. **Factual or absent.** No fabricated values; attested import data is
   labeled as attested, derived values as derived; wrongly-shown values are
   fixed before new surfaces are added.
4. **Period honesty.** Period-scoped figures name their coverage basis;
   periods come from per-document declarations, never inferred silently.
5. **Re-compose, don't re-import.** Build from the existing UI vocabulary;
   zero new pec runtime deps (corollary above governs the two reserved
   dependency decisions).
6. **Accessible by construction.** Keyboard-operable drill spine, real
   buttons/links, AA contrast.
7. **Dashboards, not task managers — one primary job per page.** The
   discipline view answers "what is this discipline's status story this
   period?"; it never grows mutation machinery.
8. **High-risk actions are visually fenced** and server-authorized
   (`can/:action` probe — never client-invented RBAC).
9. **Agent proposes, human disposes.** The sidecar lane maps, files
   proposals, drafts reports, and flags discrepancies; accept/apply/issue are
   human acts. Agent auto-response, where offered, is configurable and
   scoped to caught application-level matters (findings §2).
10. **Theming through tokens only**; dense, contemporary, non-marketing UI.

## Data-readiness tiers (honest cost basis for sequencing)

- **Tier U — UI only:** discipline-view composition over existing payloads;
  vocabulary/display alignment.
- **Tier S — read-side server (zero-dep `node:sqlite`):** discipline
  rollup/report projections in the `Explain` shape; period-scoped read
  queries once the period model exists.
- **Tier M — schema/model migration (owner-gated):** coverage declarations +
  period snapshots; % complete column; needs internal/client typing; status
  vocabulary; interfaces contract keys.
- **Tier O — owner decisions (no default):** XLSX parsing approach +
  dependency; `.docx` generation approach + dependency; agent auto-response
  configuration surface; carried slate items below.
- **Tier P — owner-provided inputs (hard prerequisites, park until present):**
  revised MDL/RAIL templates; interfaces document format; report template
  file placement; (optional) rules-of-credit table.

## Roadmap

### Carried in-flight (already ruled — execution authority is their rulings,
### not this plan; riders verbatim in Receipt 69 and the register)

- **D-PEC-30** Registers consistency (O-A) — `shared.tsx` sequencing rule
  applies.
- **D-PEC-31** Overview & My Week polish (O-A).
- **D-PEC-35** Upload lane, CSV/TSV adaptive mapping (O-A; interim — XLSX
  follow-on expected after the revised templates, its own ruling).
- **D-PEC-36** Standard report set (O-A; weekly status payload groups by
  discipline as well as package; no `.docx`/%/periods).
- **D-PEC-37** User-defined reports (O-A; execution gated on D-PEC-36).

### Candidate packets (each lands as its own proposed D-PEC decision packet,
### numbered live from the register — D-PEC-39.. as of authoring — with an
### exact write fence, dependencies, verification plan, and the owner gate)

| Phase | Candidate packet | Scope (summary — detail in findings §§3–7) | Indicative fence | Deps / prerequisites | Tier | Effort |
|---|---|---|---|---|---|---|
| R0 | **Reporting periods & coverage declarations** | Per-document declared coverage date range on the import-proposal lane; period model + snapshots enabling "issued this period", week-over-week deltas, and stalled detection; overlaps/gaps/corrections are *caught* (surfaced to the agent/PE), not schema-prevented; period-scoped read queries in the `Explain` shape | `core/src/**`, `server/src/**`, `server/test/**`, upload-lane surfaces as named in the packet | none hard (semantics designed now; templates refine, don't gate) | M+S | L |
| R0 | **Discipline view v1** | First-class per-discipline page: the four report sections over existing data (Activities grouped by deliverable type; Issuances; Needs; Risks) + the findings §5 metric band; % complete and period-scoped tiles degrade honestly ("absent and said to be absent") until their tranches land | `web/src/**`, `server/src/services/views.ts`, `server/src/api.ts` (read-only projections), `server/test/**` | D-PEC-25/38 landed spine; periods packet enriches (soft); % packet enriches (soft) | U+S | L |
| R1 | **MDL/RAIL contract v2** | §16 contract extensions from the revised templates: % complete (0–100 int, PE-attested), full status vocabulary, coverage columns, any additive fields; export round-trip parity | `server/src/import/**`, `core/src/**`, `fixtures/**`, `server/test/**`, IMPORT_TEMPLATES docs | **Tier P: revised MDL/RAIL templates** | M | M |
| R1 | **XLSX upload follow-on (the D-PEC-35 rider)** | Workbook parsing for the agent-adaptive lane; parsing approach and any dependency named explicitly in the packet; proposal-gated only, no direct writes | `projects/pec/agent-sidecar/**` (+ only what the ruling names) | **Tier P: revised templates**; D-PEC-35 landed | O | M |
| R1 | **Discipline status report (.docx)** | Template-conformant Word draft of the weekly/aggregate discipline report (structure per findings §3) composed from the D-PEC-36 payloads + periods + %; generation approach and any dependency named explicitly; drafts are PE-vetted, issued outside the app; in-app storage at most a convenience | `projects/pec/agent-sidecar/**`, `server/src/reports/**` as named | D-PEC-36 landed; periods packet; contract v2 (%); **Tier P: template file accessible** | O+S | M–L |
| R2 | **MDL↔RAIL consistency checks** | Intake/triage machinery catches MDL-status vs RAIL-issue disagreements (starting with "on hold"); caught items carry a disposition trail; agent response automatic or human-prompted, **configurable** | `server/src/services/intake.ts` + named services, `server/test/**`, sidecar policy surface as named | contract v2 (status vocabulary) | S+M | M |
| R2 | **Needs internal/client typing** | Typed requester-side triage on needs-shaped records (RAIL-borne actions/holds); feeds the discipline view's Needs split and aging | `core/src/**`, `server/src/**`, `web/src/**` as named | contract v2 (RAIL carries the triage) | M | S–M |
| R2 | **Interfaces import contract** | §16-style import contract + round-trip export for the owner's periodically uploaded interfaces document | `server/src/import/**`, `fixtures/**`, `server/test/**`, IMPORT_TEMPLATES docs | **Tier P: interfaces document format** | M | M |
| R3 | **Reporting-vocabulary alignment** | Display-layer alignment of report/dashboard surfaces to the owner's client-facing vocabulary (findings §4.5) without reopening ADR-011 or the cockpit union | `web/src/**` as named | discipline view landed; contract v2 vocabulary | U | S |

### Carried owner-gated / deferred (unchanged from the predecessor)

- **D-PEC-32** issue-model completeness and **D-PEC-33** deep-linkable drawer
  records — P3, owner-gated where they sat.
- **D-PEC-28/28b** planning-phase redesign — deferred; reactivates only by
  owner direction, as the last phase. Spec projections sleep with their
  packets.

**Sequencing rationale (default order, re-derived each iteration).** Finish
the carried in-flight packets first — they are already authorized and the
reporting lanes (35/36/37) are direct prerequisites for the `.docx` tranche.
`shared.tsx` tranches never run in parallel with each other; sidecar/server
fences may run alongside web-only fences where write scopes are disjoint;
D-PEC-37 waits on D-PEC-36. Then R0 (periods; discipline view v1) — both are
specifiable **now** without the owner templates and are the
force-multipliers every later row composes over. R1 rows unpark as their
Tier-P inputs arrive (templates → contract v2 → XLSX follow-on and the
`.docx` report). R2 rows follow contract v2. R3 is cheap polish once the
surfaces exist. Blocked rows are parked and named in receipts — never
improvised around (protocol step 1d).

## Open owner decisions (rule any time; none defaulted)

1. **Carried slate items** still open from the predecessor plan (Receipt 68
   parked lanes): zero-new-dependency posture confirmation; Admin
   role-assignment route; Log workbench depth; issue-model completeness
   (D-PEC-32); dark mode.
2. **Periods schema approach** — the R0 periods packet is a Tier-M model
   change; its packet carries the options.
3. **XLSX parsing approach + dependency** (reserved by the D-PEC-35 rider).
4. **`.docx` generation approach + dependency** (reserved by the corollary).
5. **Agent auto-response configuration** — where the automatic-vs-prompted
   policy for caught discrepancies lives and who may change it.

## Risks & watch-items

- **Template dependency drift** — R1 rows are designed against templates that
  do not exist in the tree yet; park them, never guess column shapes
  (K-INVENT-1). The findings' prerequisites table (§6) is the checklist.
- **Period semantics creep** — periods are declarations plus caught
  exceptions; resist schema rigidity that blocks the PE's real workflow
  (retro-corrections are normal, per the owner).
- **Attested-vs-derived confusion** — % complete must never silently become a
  derivation or an editable field (reconciliation 1); verify at review on
  every % -touching tranche.
- **`shared.tsx` contention** — sequence, never parallelize, tranches that
  touch it; keep write scopes disjoint (loop rule; concurrent sessions have
  collided before — Receipts 55/56/67 precedent).
- **Explain-shape discipline** — discipline-view tiles must emit real
  `contributing[]` refs or they silently break I-4; verify each tile drills
  at step 4.
- **Scope creep toward a task manager** — reject any board/bulk-mutate/
  editable-status request against principle 7 and the standing direction.
- **Report egress** — `.docx` outputs and any report storage stay inside the
  profile's ruled `data_residency` basis (F-PEC-3); the report's project
  content never lands in this coordination repo (D-PEC-01 pilot-scratch
  convention).

## Where live work is re-derived (pointer index — never a status surface)

- **Decision registers** (open rows are the owner-gated surface):
  `_DomainEngines/_DECISIONS/_REGISTER.md` ·
  `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md` (D-PEC-XX
  rows — never bare `D-XX`).
- **The profile:** `_DomainEngines/profiles/pec.yaml` (ADOPTED;
  `integration_level` and `data_residency` are read live from it, never from
  prose) + its `_validation/` report; registry row in
  `_DomainEngines/DOMAIN_ENGINE_INDEX.md`.
- **This phase's provenance:** the findings document + carried redesign
  provenance (Provenance section above).
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
- **Superseded predecessors:** `.archive/WORKPLAN_2026-07-04_pec_loop.md` and
  `.archive/WORKPLAN_2026-07-08_pec_uiux_redesign.md` (each retired at owner
  direction with a dated supersession pointer; kept otherwise unedited for
  the record).
