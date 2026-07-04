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
PH-R1/PH-A1 (and KPI-ONPLAN) now state the pressure in plain terms and carry through the underlying
records themselves — the same holds, overdue items, conditions, and aging comments the package cockpit
lists (capped at 3 per deliverable) — so every drill-down lands on a cockpit-visible record; (2) the
Overview package rollup (PEC-OV-003) adopts the cockpit's log-scoped `openIssues` count, so Overview and
Packages speak the same issues language (PEC-NFR-005 preserved via the same scoping).
**Consequences.** No health value changes anywhere; only Explain payloads and the Overview rollup gain
information. DH-* remains an internal aggregation stage, legitimate as derivation, invisible as
presentation. Revisit the derivation itself only if the pilot demonstrates the §8.3 defaults mislead —
that is what PEC-OV-007 threshold configurability and this ADR's paper trail are for.
