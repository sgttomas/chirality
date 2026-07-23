# Architecture Decision Records — PEC

Format: context → decision → consequences. PRD decisions (OM-1..7, D-01..14) are taken as given; these
ADRs cover choices the PRD delegates to the implementer.

## ADR-001 Workspace placement and governance posture
**Context.** The chirality repo hosts software project workspaces under `projects/` (cf.
`projects/chirality-piping`). The PEC PRD v0.4 arrived at the repo root, untracked.
**Decision.** Build in `projects/pec/`, self-contained (PRD copied to `docs/PRD.md`). Scaffolded directly
from the PRD rather than through the full chirality decomposition loop; the workspace mirrors repo
conventions (docs/, plans-ready layout) so it can be adopted into governance (SOFTWARE_DECOMP, registers,
snapshots) without restructuring.
**Consequences.** No decomposition registers yet; if the project enters the governed loop, generate them
from `docs/SPEC.md` + `docs/TRACEABILITY.md`.

## ADR-002 TypeScript end-to-end; Node 24 native TS; zero server runtime deps
**Context.** The product's core is a rule engine (lifecycles, conditions, derived status) shared
conceptually by server enforcement and UI affordances. NFRs demand auditability and small deploy surface.
**Decision.** One language (TypeScript) across core/server/web. Server runs directly on Node ≥ 23.6
type-stripping (erasable syntax only: no enums/namespaces/param-properties; `import type` for types;
explicit `.ts` extensions). No server runtime dependencies: hand-rolled HTTP router over `node:http`,
`node:sqlite` for storage, `node:crypto` scrypt for passwords, `node:test` for tests.
**Consequences.** No build step server-side; tiny supply-chain surface; router/CSV code is ours to test.
Web keeps a conventional React + Vite toolchain (build-time deps only).

## ADR-003 SQLite, single DB, repository-enforced project scoping
**Context.** PEC-NFR-003 sets pilot scale (10k open items / 250k history rows); PEC-NFR-007 requires
project isolation, PEC-NFR-008 (P2) single-tenant deploys.
**Decision.** One SQLite database file; every project-scoped table carries `project_id`; the repository
layer is the only SQL surface and scopes every query by the route's project id. WAL mode. Append-only
tables (`history_entry`, `audit_event`) protected by SQL triggers that raise on UPDATE/DELETE, plus an
insert-only repo API. Controlled records get no delete path at all.
**Consequences.** Pilot scale is comfortably in-memory for derived status; Postgres migration is a repo-
layer swap (SQL kept vanilla). Backup = file copy (PEC-NFR-009: document + script `tools/backup.ts`).

## ADR-004 Derived values computed on read, returned only with explanations
**Context.** I-4 ("status is derived and explainable") is the anti-black-box invariant; storing derived
state invites drift.
**Decision.** Health, lifecycle rollups, KPIs, blocked overlays are pure functions in `core/` over a
`ProjectSnapshot`; the API returns `{value, ruleId, threshold, contributing[]}` — never a bare value.
Nothing derived is persisted.
**Consequences.** No cache invalidation class of bugs; recompute cost bounded by snapshot load (indexed,
one project). If P2 scale demands, add read-through caching keyed on project mutation counter — without
changing the contract.

## ADR-005 One write path for judgments (Decision service)
**Context.** OM-6 / I-6: approval outcomes and waivers must be Decisions; a generic "approved" flag is the
named failure mode (PRD §19).
**Decision.** A single `recordDecision()` service creates every judgment row. Approval outcome and
condition waiver endpoints call it internally; there is no code path that sets an approval/waiver effect
without creating a linked Decision. Check acceptance is deliberately *not* routed through it (checking
verifies; PEC-CHK-005).
**Consequences.** I-6/I-8 become structural properties testable by grepping one module's call sites.

## ADR-006 Transitions as data
**Context.** Seven lifecycles with guards, vetoes, and side-effects; UI must know what's offerable;
tests must enumerate legal/illegal moves.
**Decision.** Each lifecycle is a declarative transition table in `core/src/lifecycles.ts` (from-state,
event, to-state, permission key, guard refs, side-effect keys). Server executes it; UI reads offered
transitions from the API; tests iterate the tables exhaustively.
**Consequences.** New states (P3 `reconciled`) are table rows, not scattered conditionals.

## ADR-007 Sessions + scrypt for P1 auth
**Context.** SSO is P2 (PEC-NFR-006); pilots need multi-user auth day one.
**Decision.** Cookie sessions (httpOnly, SameSite=Lax), scrypt password hashes, seeded users, per-project
role assignments. Auth pluggable behind `server/src/auth.ts` for the P2 SAML/OIDC swap.
**Consequences.** No external IdP dependency for pilot; password reset is admin-driven in P1.

## ADR-008 Display refs per project + integer PKs
**Decision.** Every controlled record gets a human ref (`WI-0001`, `HLD-0002`, …) from a per-project,
per-type sequence, alongside integer PKs. Refs appear in every explanation, notification, and export.
**Consequences.** Stable cross-references in meetings/exports without exposing raw ids; sequences are
project-scoped so multi-project numbering never collides.

## ADR-009 Lifecycle convenience deviations
**Context.** PRD §7.2 gives the Work Item exit sets Open → {In work, Cancelled} and In work → {Closed,
Open}. Field practice closes trivial items without a logged start and cancels items already started;
forcing the PRD exit sets adds ceremony without record value.
**Decision.** SPEC §4.2 keeps two shortcuts: `open → closed` (collapses an implicit start; the closure
guard still applies in full) and cancel from `in_work` as well as `open` (lead/coordinator, reason
required).
**Consequences.** The exhaustive legal/illegal-move tests (SPEC §10) treat both as legal; the deviation
from the PRD exit sets is deliberate and recorded here, not drift to reconcile.

## ADR-010 Export and report pragmatics
**Context.** PRD §15 requires CSV export for every register, an individual-weekly-commitments report, and
"PDF and print-friendly HTML" for briefs — but the P1 server has no PDF pipeline and wants none (ADR-002:
zero runtime deps).
**Decision.** Register CSV export = exactly what is displayed: the current filtered view of every
register (approvals, decisions, risks, interfaces, intake, log) serializes to CSV, and
`GET export/commitments.csv` serves individual weekly commitments (PRD §15). The sponsor brief ships as
print-friendly HTML; P1 satisfies the PDF format via the browser rendering that page to PDF — a
deliberate reading of §15, revisited only if a pilot demands generated PDFs.
**Consequences.** No PDF dependency server-side; brief formatting is CSS print styles; export coverage is
testable per register, and round-trip fidelity (§16) is preserved because register exports mirror the
import schemas.

## ADR-011 Deliverable status is workflow completeness; issues live at the package
**Context.** P1 shipped a single issue-driven RAG (`deliverableStatus`, DH-*) as a deliverable's
"health" and surfaced holds/overdue counts on the Deliverables register. Pilot direction (2026-07-04)
drew a sharper line: a deliverable is a document moving through a production workflow, so its *status*
is workflow completeness — which gates (drafted → checked → approved → issued) it has closed. Issues
(holds, interfaces, decisions, risks, action items) are coordination records that belong to the
package: they are what a Package Lead manages, not what a deliverable *is*.
**Decision.** Add a pure `workflowCompleteness(snap, deliverable)` derivation over the revision
lifecycle (independent of issues) and make it the deliverable summary status on the Deliverables page
and the deliverable-detail header. Reorient the Packages page into an issues cockpit: a unified,
urgency-sorted list of the package's holds, interfaces, decisions, risks, and rolled-up open
action/coordination work items, with an `openIssues` count on the register. Deliverable-level issues
are removed from the deliverables summary; they remain visible on drill-down (deliverable detail) as
tied context. The existing issue-driven `deliverableStatus` (DH-*) is retained — it still feeds package
and project health rollups (PH-*/PJ-*) and the Overview, which are legitimately issue/schedule signals.
**Consequences.** `deliverablesView` returns `workflow` instead of `health`/`openItems`/`holds`; the
hold-cause filter leaves the Deliverables page (issues are a package lens). `packageDetailView` gains
`issues`, `risks`, action-item roll-up, and richer counts; `packagesView` gains `openIssues`. The
register `openIssues` count is log-visibility-scoped so it matches the drill-down cockpit and never
reveals the existence of records the caller cannot see (PEC-NFR-005). I-4 is preserved: workflow status
is derived-on-read and never stored; health continues to carry Explain payloads for the rollups. The
deviation from the P1 "deliverable health" presentation is deliberate and recorded here, not drift.

## ADR-012 Package/project health derivation stands; explanations carry through to issue records
**Context.** ADR-011 left a seam open: package health (PH-R1/PH-A1) and project health still derive from
the issue-driven per-deliverable RAG (DH-*), a concept the UI no longer surfaces as "deliverable health"
since a deliverable's status became workflow completeness. Should package/overview health be reframed
around package-level issue signals (hold age, overdue decisions, late interfaces, risks) instead?
**Decision.** The derivation stands, rule for rule. PRD §8.3 specifies the package rules — including
"≥ 20% of active deliverables amber/red" — as the shipped defaults; the pilot has not run, and deviating
from the basis document ahead of pilot evidence would invert the pilot-driven posture. The rules are also
not redundant with an issue-count reframing: PH-R1/PH-A1 weight issues by schedule impact (forecast slip,
milestone linkage) that flat issue aggregation cannot express; §8.3 already contains the direct
package-level issue rules (PH-R2 interfaces, PH-A2 decisions); and hold-age/decision-latency pressure
already escalates through the §8.4 project signals — a parallel per-package copy would be rule sprawl.
P2 extends §8.3 in kind (capacity load rules), confirming the frame. What was actually broken is the
*explanation*: PH-R1/PH-A1 drill-downs bottomed out at "AUR-M-001 amber (DH-A1)" — an internal label
pointing at nothing a user can open. Fixed in the presentation layer: (1) the contributing refs of
PH-R1/PH-A1 now state each deliverable's pressure in plain terms and carry through the underlying
records themselves — the same holds, overdue items, conditions, and aging comments the package cockpit
lists (capped at 3 per deliverable) — so every drill-down lands on a cockpit-visible record; KPI-ONPLAN
whys gain the same plain-language detail (its contributing list stays at deliverable granularity — it
counts deliverables, and carrying records through at project scale would flood the drawer); (2) the
Overview package rollup (PEC-OV-003) adopts the cockpit's log-scoped `openIssues` count, so Overview and
Packages speak the same issues language (PEC-NFR-005 preserved via the same scoping).
**Consequences.** No health value changes anywhere; only Explain payloads and the Overview rollup gain
information. DH-* remains an internal aggregation stage, legitimate as derivation, invisible as
presentation. Revisit the derivation itself only if the pilot demonstrates the §8.3 defaults mislead —
that is what PEC-OV-007 threshold configurability and this ADR's paper trail are for.

## ADR-013 P2 planning & capacity — implementer choices
**Context.** PRD §12.4 specifies the P2 requirements but leaves the planning data model and several
rule scopes to the implementer: what a "Commitment" is, how capacity attaches to people, what the §8.3
package capacity rule means when capacity is defined by discipline (PEC-PLAN-003), and how the
plan-shift review works.
**Decision.**
1. **One plan placement per record** (`plan_item`, UNIQUE on the underlying record): a work item,
   check, or approval record is placed once — horizon (now/next/later) + ISO week + planned hours.
   Checks and approvals are plan items exactly like work (I-9): their hours load the same capacity
   cells and are reported per type. `later` is the unscheduled backlog (no week).
2. **Discipline is denormalized onto the plan item**, snapshotted from the responsible person (owner /
   checker / first signatory) at planning time and editable. Capacity math stays a pure function of
   the snapshot without loading persons; a planner can re-bucket a placement without touching people.
3. **Package capacity rule (PH-R3/PH-A3) reads through disciplines**: capacity exists per
   discipline/week (PEC-PLAN-003), so the only well-defined package reading of §8.3's "committed load
   vs capacity" is exposure — the package breaches when the current week's load in a discipline its
   planned records draw on exceeds the threshold, with those plan items as the contributing records.
   S-CAP applies the same cells at project level (current week; §8.3 says "in the current week").
4. **Plan shifts are the plan-change log** (append-only table, no delete trigger exception): every
   move records reason (PEC-PLAN-006) and links (PEC-PLAN-008). A shift whose linked/own packages
   differ is cross-package: it requires an impact statement, lands `proposed`, notifies the affected
   leads, and applies only on review (PEC-PLAN-005); within-package shifts apply immediately.
5. **The weekly commit writes the durable fact onto the work item** (`committed_week` +
   `commit_source='plan'`) rather than deriving My Week from plan rows at read time — the committed
   week must survive later plan edits (a commitment is a record, not a view), and the P1 manual flag
   coexists (`commit_source='manual'`). Commit is idempotent; checks/approvals notify their
   responsible person instead (their My Week obligations already project via PEC-MW-002).
6. **Schedule import is import-owned** (D-04): rows upsert by `activity_id` and always refresh —
   there is no in-app edit path to protect — but mapping columns update only when present in the CSV,
   and a stated mapping that does not resolve rejects the row (§16: nothing silently dropped/wiped).
7. **Digests are notifications** (PEC-NOT-002): one per person per digest type per ISO week, produced
   by the existing sweep (hourly + login), idempotent the same way the daily overdue events are.
   Severity on all time-driven notifications comes from the §8.4 thresholds (PEC-NOT-003); a
   `severity` column was added rather than a parallel channel.
8. **Supersession links are first-class rows** (`supersession_link`, PEC-AUTH-005): old → replacement
   with the affected-record set (JSON of refs) captured at supersession time from decision links /
   applies-to / satisfied conditions. P3 propagation gets a stable substrate; nothing is recomputed
   retroactively.
**Consequences.** Plan tables are additive; P1 behavior is unchanged until records are planned
(capacity rules and S-CAP are silent with no plan/capacity rows). Plan resolution is indexed per
snapshot (`core/src/plan.ts` planIndex, WeakMap-memoized like snapshot-index.ts) so the health rules
stay off O(n²) paths at PEC-NFR-003 scale; the perf guard now seeds 2k plan items. `plan_shift` loads
fully into the snapshot like the other controlled registers — bounded by human planning actions, the
same class as decisions/holds. An adversarial review pass (2026-07-04) additionally hardened: plan-view
and package-pack log visibility (PEC-NFR-005), cross-package review integrity (foreign-lead-only,
no self-approval, stale proposals refuse to apply), per-package digest idempotency, raw-ratio capacity
classification incl. zero-hour baselines, phantom-W53 rejection, schedule-forecast gating on issued
deliverables, capacity-change audit events, and served-merged threshold defaults. `interfaceOverdueWarnWd`,
`capacityWarnPct`, `capacityRedPct` join the configurable thresholds (PEC-OV-007). Existing databases
migrate in place via `ensureColumn` (notification.severity, work_item.commit_source). PEC-AHL-008
(duplicate suggestion) and PEC-NFR-006 (SSO) remain the P2 items deliberately not built here: the
first wants pilot vocabulary to tune matching against, the second an IdP to integrate with.

### ADR-014 — Shared runtime agent ownership (2026-07-22)

**Decision:** Under D-T0-23/D-PEC-56, root daemon owns LLM, credentials,
sessions, delegation, interruption, and residency. PEC retains deterministic
acts, RBAC, reporting, human-only acts, visibility, and data boundaries in a
project adapter. The legacy endpoint is a one-cycle proxy; no production dual
loop. Validation is scratch/demo-only.
