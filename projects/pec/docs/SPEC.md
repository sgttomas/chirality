# PEC — Implementation Specification (P1 + P2)

**Basis:** `docs/PRD.md` (Project Execution Control PRD v0.4). This SPEC translates the PRD's P1 scope into
buildable contracts: data model, state machines, conditions engine, derived status, API, permissions, and
import/export. Where the PRD leaves an implementation choice open, the choice is recorded here or in
`docs/adr/`. Requirement IDs (`PEC-*`), invariants (`I-*`), object-model decisions (`OM-*`), and defaults
(`D-*`) refer to the PRD.

Phase scope: **P1** (controlled tracker replacement, PRD §21 Phase 1) in §1–§13, plus the **P2 planning
& capacity build** in §14 (2026-07-04; ADR-013). P3 headroom is noted where a schema choice would
otherwise foreclose it.

---

## 1 Architecture

Three layers, one record system (I-1):

| Layer | Package | Responsibility |
|---|---|---|
| Domain core | `core/` | Pure TypeScript, no I/O. Entity types, the seven lifecycles (§4), conditions engine (§5), derived status + explanations (§6), working-day calendar, permission rules. |
| Server | `server/` | Node 24, `node:sqlite`, zero runtime deps. Persistence with append-only history + audit events, optimistic concurrency, session auth, server-side RBAC, REST API, notifications, CSV import/export, static hosting of the built web app. |
| Web | `web/` | React + Vite SPA. Six role homes + registers, all rendering projections of the same records via the API. Holds **no** business rules: every guard, derivation, and permission is server-truth; the UI only displays explanations the server provides. |

Derived values (health, lifecycle state, blocked overlay, KPIs) are **computed on read, never stored**
(I-4). Every derived value is returned with an `explain` payload: the rule id that classified it, the
threshold used, and the contributing record refs (§6.4).

All timestamps are stored as UTC ISO-8601 strings. Each project has an IANA timezone and a working-day
calendar (weekend days + holiday dates) used for every "working days" computation (PEC-NFR-010).

Multi-project isolation (PEC-NFR-007): one SQLite database; every project-scoped table carries
`project_id`; the repository layer scopes **every** query by project id taken from the authenticated
route, never from the request body.

---

## 2 Identity, roles, permissions

### 2.1 Tables

- `person` — firm-level identity: `id, name, email UNIQUE, password_hash (scrypt), is_admin, discipline, created_at`.
- `project` — `id, code UNIQUE, name, timezone, weekend_days (JSON, default ["Sat","Sun"])`, holiday dates JSON, `thresholds` JSON (§6.3 overrides), `config` JSON (hold causes, issue purposes per D-07, log visibility map).
- `project_role_assignment` — `project_id, person_id, role`, uniqueness on the triple. A person may hold several roles in one project.

Roles (PRD §14): `sponsor, pm, engineering_manager, package_lead, discipline_lead, engineer_of_record,
checker, approver, planner, coordinator, contributor, document_controller, viewer, admin`.
`admin` here is project-admin; `person.is_admin` is instance admin.

### 2.2 Permission rules (P1)

Enforced server-side per route (PEC-NFR-005); the matrix lives in `core/src/permissions.ts` so the UI can
ask "can I?" through the API without duplicating rules.

| Action | Allowed |
|---|---|
| Raise intake item | any project member (configurable off per project) |
| Triage / disposition intake | coordinator, pm, admin |
| Create work item (anchored) directly | package_lead, discipline_lead, engineer_of_record, pm, coordinator, admin |
| Update / progress / close own work item | owner; plus package_lead of the item's package, coordinator (hygiene fields: anchor, log, priority), pm, admin |
| Raise hold | any member except viewer |
| Resolve / withdraw hold | hold owner, package_lead, pm, coordinator, admin |
| Create check, edit checklist | package_lead, discipline_lead, engineer_of_record, pm, admin |
| Work comments / respond | the comment's responder (any member may be assigned) |
| Accept comment closure, accept check | the check's checker only |
| Create approval record | package_lead, pm, engineering_manager, document_controller (metadata only), admin |
| Record approval outcome | a **named signatory** of that approval record only (D-12) |
| Create decision | package_lead, pm, engineering_manager, coordinator, admin |
| Record decision outcome | the decision's `authority` person only |
| Waive condition | per condition type, from project config; defaults: `check/approval/decision/document_control` types → pm or engineering_manager; others → package_lead or above. Always recorded as a Decision (I-8). |
| Revision transitions (work/check flow) | owner, package_lead, pm, admin — gated by conditions engine |
| Record issue event, revision metadata, transmittals | document_controller, pm, admin. Document controllers **cannot** accept checks or record approval/decision outcomes (PRD §14). |
| Create / update deliverable, package | package_lead, discipline_lead, engineer_of_record, document_controller, pm, admin |
| Create / update risk | package_lead, discipline_lead, engineering_manager, coordinator, engineer_of_record, pm, admin; plus the risk's owner |
| Create / update interface item | package_lead, discipline_lead, engineering_manager, coordinator, pm, admin |
| Add evidence / basis reference | any member except viewer |
| Manage config, templates, thresholds, roles | admin (writes an Audit Event) |
| Everything above | viewer: read-only everywhere |

Log visibility (PEC-AHL-002, PEC-NFR-005): items carry `log ∈ {package, internal, client}`. P1 default
config: all internal roles see all logs; `viewer` sees `client` + `package` only. Derived status is
computed on the **unfiltered** snapshot (one shared truth, §6); visibility is enforced when register rows
and list-endpoint responses are serialized. Contributing/explanation refs that point at records outside
the caller's visible logs are redacted to type + ref, title/statement omitted. Changing an item's log
writes history (never silent).

---

## 3 Data model

### 3.1 Conventions

- `id`: integer PK. `ref`: human display id per project + type, from `seq` table: `WI-0001`, `HLD-0002`,
  `CHK-0003`, `APR-0004`, `DEC-0005`, `RSK-0006`, `INT-0007`, `INTK-0008`, `COND-0009`, `CMT-0010`,
  `EVT-0011` (issue events), `DLV-…` uses doc_no instead.
- Controlled records carry `version INTEGER` (optimistic concurrency, PEC-NFR-004): writes must send the
  version they read; mismatch → HTTP 409 with the intervening history entries.
- **No hard delete** of controlled records (PEC-NFR-002): the repository layer exposes no delete for them;
  terminal outcomes are `cancelled / withdrawn / rejected / superseded` states with reason.
- `history_entry` — append-only (I-7): `id, project_id, record_type, record_id, at, actor_id, kind, summary, payload JSON, authority_ref`. Written inside the same transaction as the change. No UPDATE/DELETE on this table (enforced: the repo layer has insert-only methods **and** SQL triggers reject UPDATE/DELETE).
- `audit_event` (PEC-NFR-001): `id, project_id, at, actor_id, action, record_type, record_id, prior_value JSON, new_value JSON, authority_ref`. Written additionally for: approval outcome, issue event, waiver, permission/config change. Trigger-protected like history.
- `notification` — `id, project_id, person_id, at, event (PEC-NOT-001 catalog), record_type, record_id, reason, next_action, due, read_at`. Every notification names the record, why, next action, due date, and where to resolve (PRD §12.14) — `where` is derived client-side from record type.

### 3.2 Hierarchy

- `package` — `project_id, code, name, lead_id, description, version`.
- `deliverable` — `project_id, package_id, doc_no UNIQUE(project), title, discipline, deliverable_type, owner_id, dc_ref, client_no, milestone, due_date, issue_purpose_plan, remarks, version`. Document layer collapsed per OM-4/D-01. `deliverable_type` is populated from the optional MDL column `deliverable_type` or set in-app; it keys condition/checklist template matching (§5.2, PEC-CHK-001).
- `revision` — `project_id, deliverable_id, rev_code, state (§4.7), created_at, created_by, superseded_by_revision_id, version`. One `current` revision per deliverable = the latest non-superseded one.

### 3.3 Intake and work

- `intake_item` — OM-3: `project_id, ref, statement_verbatim, quick_type (need_information | need_decision | need_approval | need_resource | risk_budget | risk_scope | risk_schedule | action | hold | interface), anchor_suggestion, need_by, suggested_owner_id, log, raised_by, raised_at, state (raised | in_triage | dispositioned), disposition (converted | merged | duplicate | rejected | parked), disposition_note, merged_into_intake_id, version`. `statement_verbatim` is never updated after insert (trigger-enforced). Created records back-link via `intake_link (intake_id, record_type, record_id)` (PEC-AHL-005).
- `work_item` — OM-1, PRD §13.2: `project_id, ref, title, statement, kind (action | coordination | risk_treatment | rework | other), log, anchor_type, anchor_id, package_id (derived from anchor at write time), owner_id, need_by, priority, priority_provenance, state (open | in_work | closed | cancelled), committed_week (ISO week string; P1 manual commit, PEC-MW-007), source_type/source_id (intake, decision, comment, risk), created_by, created_at (PRD §13.2), closing_statement, closed_by, closed_at, cancel_reason, version`.
  - Anchor: exactly one primary anchor (`deliverable | revision | package | decision | approval_record | risk | interface_item`) — I-2, §13.4. `work_item_link` holds unlimited secondary links. Rollups use the primary anchor only.
  - An **unanchored** work item cannot exist; what can exist is an untriaged intake item. Direct creation requires an anchor (I-2).

### 3.4 Holds

- `hold` — OM-2: `project_id, ref, title, cause (information | decision | approval | resource | client_input | interface | vendor_data | other), statement, owner_id, need_by, raised_by, raised_at, state (active | resolved | withdrawn), resolution_kind (decision_recorded | information_received | resource_assigned | approval_recorded | other), resolution_note, resolved_at, resolving_ref_type/id, log, version`. Requires ≥1 blocking link at creation;
`owner_id` and `need_by` are likewise **required at creation** (I-3), enforced in the `POST holds` validation.
- `hold_link` — `hold_id, target_type (work_item | revision | deliverable | condition | issue_event | interface_item | decision | approval_record | check | risk), target_id`. A record's **blocked overlay** = it has ≥1 link from an `active` hold; never a stored state (§4 preamble).

### 3.5 Checking

- `checklist_template` — `project_id, name, discipline, deliverable_type, package_id (nullable — null matches any), items JSON [{text, category}]`, version. (PEC-CHK-001)
- `check` — §7.4: `project_id, ref, revision_id, checker_id, template_id, state (open | in_check | comments_open | comments_closed | accepted | reopened), checklist JSON [{text, category, done, note}], accepted_at, independence_warning (bool, set when checker == revision owner, PEC-CHK-004 P1 warn), reopen_reason, version`.
- `review_comment` — OM-5, child of check: `project_id, ref, check_id (nullable), revision_id, originator_id, responder_id, text, response, disposition (open | responded | accepted_closed | reopened), closure_evidence_id, log, created_at, version`. `check_id` is null only for client-return comment sheets logged directly against a revision via `revision_id` (D-10); `created_at` feeds the comment-age signal (§6.1 DH-A4, §6.3). Comments project into My Week for the responder; they are **not** duplicated as work items (a triage/convert action may create a linked work item explicitly, D-10).
- Three distinct facts, never merged (PEC-CHK-003): checklist completion (`checklist[].done` all true), comment closure (no comment in `open|responded|reopened`), checker acceptance (`state=accepted`). The API exposes all three separately.

### 3.6 Approval and decisions

- `approval_record` — §7.5, PEC-AUTH-001: `project_id, ref, title, approval_type, authority_source, applies_to_type/id, authority_holder, required_decision_type, signatory_ids JSON (named, P1 per D-12), basis_ref, due_date, hold_point, state (required | prereqs_incomplete | ready | decided | superseded), ready_at (stamped on entering `ready`; drives the approval-latency signal, §6.3), outcome_decision_id, superseded_by_id, version`.
- `decision` — §7.6, OM-6 (the **only** judgment record; approval outcomes and waivers are rows here): `project_id, ref, package_id (nullable — decisions are tracked at package level, PRD §4.2; drives PH-A2, PEC-OV-003, PEC-PKG-006), title, statement, preparer_id, authority_id, need_by, state (identified | in_progress | pending | decided | superseded), outcome (select | approve | reject | defer | conditionally_accept | confirm_basis | waive | supersede), rationale, options_considered, recommendation, decided_at, decided_by, kind (standalone | approval_outcome | waiver), approval_record_id (when approval_outcome), condition_id (when waiver), superseded_by_id, log, version`.
- `decision_link` — affected records: `decision_id, record_type, record_id, relation (affects | blocks | follow_up | supersedes)`. Follow-up work items are created linked with `relation=follow_up`.

### 3.7 Registers

- `risk` — PEC-RISK-001: `project_id, ref, title, cause, consequence, package_id, deliverable_id, owner_id, probability (1-5), impact (1-5), mitigation, need_by, state (open | mitigating | closed), version` + links via work_item anchor / decision_link.
- `interface_item` — PEC-PKG-007 / OM-7: `project_id, ref, title, giving_party, receiving_party, giving_package_id, receiving_package_id, required_info, need_by, state (open | agreed | delivered | closed | cancelled), log, version` + `interface_deliverable (interface_id, deliverable_id)` affected links.

### 3.8 Conditions (§5) and document control

- `condition_template` — `project_id, name, deliverable_type, issue_purpose, package_id (nullable), transition, type, severity, description, required_artifact_name`. Instantiated on revision creation (keyed by deliverable type + issue purpose + package, PRD §9).
- `condition` — PRD §13.3: `project_id, ref, parent_type, parent_id, gated_transition, type (check | decision | approval | evidence | interface | document_control | resource | other), required_ref_type/required_ref_id (optional pinned satisfier), required_artifact_name, source (template | checklist | decision | manual — with source_ref), severity (hard | warn), owner_id, need_by, state (open | satisfied | waived | superseded), satisfied_by_type/id, satisfied_at, waiver_decision_id, version`. `blocked` is an overlay (active hold linked), not a state.
- `issue_event` — PEC-DEL-008: `project_id, ref, revision_id, purpose (IFR | IFA | IFC | other, labels configurable per D-07), transmittal_ref, recipients JSON, issued_at, issued_by, approval_record_ids JSON, decision_ids JSON, archive_ref, version`. Every issue event's archive_ref makes the P1 chain of PEC-ARC-002.
- `evidence` — `project_id, record_type, record_id, kind (attachment | markup | comment_sheet | transmittal | basis_ref | link | note), label, url_or_path, content, added_by, added_at`. A status update and its history entry are the same record (PEC-DEL-005): progress updates write `history_entry` rows of kind `progress`, which the evidence trail renders inline.
- `basis_reference` — `project_id, record_type, record_id, basis_kind (DBM | SOW | data_sheet | standard | client_direction | other), reference, note, state (active | superseded), superseded_by_id`.

---

## 4 Lifecycles

State machines live in `core/src/lifecycles.ts` as data (state, event, guard, target, side-effects), so the
same tables drive server enforcement, UI affordances, and tests. "Blocked" never appears below: it is a
derived overlay (active hold linked to the record). The transition tables in `core/src/lifecycles.ts`
carry a per-transition `holdVeto` flag; while a record has an active hold, exactly these transitions are
vetoed until the hold is resolved/withdrawn: `work_item.close`, `check.accept`,
`approval_record.became_ready`, `approval_record.record_outcome`, `decision.record_outcome`,
`revision.issue`. §5.4's evaluation applies the veto only to transitions so marked.

Every transition: (1) checks actor permission; (2) checks hold veto; (3) evaluates hard conditions attached
to it (§5); (4) applies; (5) writes history; (6) fires side-effects (notifications, condition
satisfaction propagation, audit events where §3.1 requires). A refused transition (guard fail) writes a
`transition_blocked` history entry listing the open conditions (metric: prevented invalid closures).

Notification producers (PEC-NOT-001, §3.1): event-driven catalog rows are emitted by transition
side-effects — assignment (work item create / owner change; check create → checker; comment create →
responder), hold raise → owners of newly blocked records, decision pending → authority, approval ready →
signatories, intake routed/updated/closed → raiser, revision ready for approval → signatories,
supersession → affected-record owners. Time-driven catalog events (item overdue; decision past need-by)
are produced by a working-day-aware sweep (hourly timer + on login), idempotent per
(person, event, record, local day).

### 4.1 Intake Item
`raised → in_triage` (coordinator opens) → `dispositioned` (disposition enum recorded; `converted` creates
linked controlled records atomically; raiser notified at routing, at ownership assignment, and at closure
of each created record, PEC-AHL-007).

### 4.2 Work Item
`open → in_work` (owner logs activity/starts) · `in_work → open` (paused) · `in_work|open → closed` —
**guard:** all `hard` conditions on `work_item.close` satisfied/waived + closing statement if template
requires · `open|in_work → cancelled` (lead/coordinator, reason) · `closed → open` (reopen: checker
rejection or supersession; records reopen reason; history preserved).
Close-from-`open` and cancel-from-`in_work` deliberately deviate from the PRD §7.2 exit sets
(`open → closed` collapses an implicit start; cancel from `in_work` is allowed with reason) — ADR-009.

### 4.3 Hold
`active → resolved` (owner records resolution kind + resolving fact; unblocks targets; notifies owners of
previously blocked records) · `active → withdrawn` (reason). Terminal states keep links for history.

### 4.4 Check
`open → in_check` (checker starts) · `in_check → comments_open` (≥1 open comment auto) ·
`comments_open → comments_closed` (auto when every comment `accepted_closed`) · `comments_closed →
in_check` (checker reopens a comment) · `comments_closed|in_check → accepted` — **guard:** zero open
comments; checklist need not be 100% but incomplete items are listed in the acceptance history entry
(three-facts rule) · `accepted → reopened` (new revision or supersession; reason).
Comment sub-flow: `open → responded` (responder) → `accepted_closed` (checker only) · `responded →
reopened → open` (checker; counts as open) · `accepted_closed → reopened` (checker only, reason
recorded) — reopening drives the parent check back to `comments_open`/`in_check`.
On `accepted`: satisfy matching `check`-type conditions (§5.3); notify revision owner.

### 4.5 Approval Record
Creation instantiates the record's default prerequisite conditions on gate `approval_record.ready`: by
default one `check`-type condition (unpinned — resolves through the record's `applies_to` revision, §5.3)
plus any decision/evidence prerequisites named in the payload. Readiness is a pure re-evaluation: on
creation and on every condition state change the `approval_record.ready` gate is evaluated — all hard
prerequisites satisfied/waived (or none exist) → `ready` (stamps `ready_at`, signatories notified), else
`prereqs_incomplete`; `required → ready` directly when zero prerequisites exist.
`ready → decided` — only via **record-outcome**, which creates a
Decision (`kind=approval_outcome`, outcome ∈ approve | conditionally_accept | reject | defer) linked back
(OM-6). `approved with conditions` instantiates the stated conditions on the target record.
`reject` → creates rework work items (linked follow_up). `defer` → resets due_date, returns to `ready`.
· `decided → superseded` (replacement link; affected records flagged — P1 records the link + notification
to owners; propagation analysis is P3).
Closure guard PEC-AUTH-004: an approval record has no "closed by task completion" path — only
record-outcome reaches `decided`.

### 4.6 Decision
`identified → in_progress` (preparer assigned; preparer ≠ authority allowed and expected) ·
`in_progress → pending` (package ready; authority notified; appears in Waiting-on-you) ·
`pending → decided` (authority records outcome + rationale; conditions created/satisfied; follow-up items
generated) · `decided → superseded` (later decision links `relation=supersedes`; affected records flagged
via decision_link owners notified). `reconciled` is P3; schema keeps the state string open.

### 4.7 Deliverable Revision
`in_work → in_check` (a check is opened) · `in_check → in_work` (rework loop, no ceremony) ·
`in_check → check_accepted` (auto from check acceptance) · `check_accepted → ready_for_approval` (auto when
every linked approval record for this revision is `ready` or `decided`; explicit if none required) ·
`ready_for_approval → approved` (all required approval outcomes recorded as approve/conditionally_accept)
· `approved → issued` — **hard-gated** (D-11): every hard condition on `revision.issue` must be
satisfied/waived; recording the issue event (purpose, transmittal, recipients) is the transition ·
`issued → returned_with_comments` (client comments logged as review comments with log=client on a
re-opened check or new check, D-10; typically followed by creating the next revision) ·
`issued|any → superseded` (new revision created; chain preserved via `superseded_by_revision_id`).
Creating a revision instantiates conditions from templates (§5.2).

Derived deliverable state = current revision state; shown with the distinct facts of PEC-DEL-009, never a
merged flag.

---

## 5 Conditions engine

`core/src/conditions.ts`. Semantics per PRD §9:

### 5.1 Attachment & severity
A condition attaches to `(parent_type, parent_id, gated_transition)` — e.g. `(revision, 42, issue)`,
`(work_item, 7, close)`, `(approval_record, 3, ready)`. `hard` blocks the transition; `warn` logs a
history entry + notification but does not block. Defaults (D-11): templates for issue-affecting
transitions and approval-authority conditions ship `hard`; everything else `warn`. Severity configurable
per template.

### 5.2 Instantiation
On revision creation: all `condition_template` rows matching (deliverable_type, issue_purpose, package —
null matches any) instantiate onto the revision's transitions, `source=template` with template ref. On
approval-record creation: the default prerequisite set of §4.5 instantiates on `approval_record.ready`.
Other sources: `decision` ("approved with conditions" — created at outcome recording), `manual`
(authorized roles). The `checklist` source is **deferred to P2** — P1 keeps only the enum headroom (§11).
Source is recorded on each condition.

### 5.3 Satisfaction wiring
| Type | Satisfied when |
|---|---|
| check | a Check on the parent revision reaches `accepted` (pinned to `required_ref` if set, else any check on the parent); on `approval_record` parents an unpinned condition resolves through the record's `applies_to` revision |
| decision | the linked Decision (required_ref) reaches `decided`; unpinned: any Decision linked to the parent via `decision_link` reaching `decided` |
| approval | the linked Approval Record reaches `decided` with outcome approve/conditionally_accept; unpinned: any Approval Record with `applies_to` = parent reaching decided-approved |
| evidence | evidence with `label == required_artifact_name` attached to the parent |
| interface | the linked interface item reaches `delivered` or `closed` |
| document_control | transmittal prerequisites present on the pending issue event (transmittal_ref + recipients) |
| resource / other | manual satisfaction by an authorized role with note (recorded as satisfied_by=person + history) |

Satisfaction is **event-driven**: the satisfying record's transition side-effect finds matching open
conditions and marks them satisfied (satisfied_by + date + history). It is also **re-verified at
evaluation time** (defense in depth: the gate recomputes truth from the record graph, so a stale
`satisfied` cannot let an issue through if its satisfier was reopened — a reopened check flips its
conditions back to `open`).

### 5.4 Evaluation & waiver
A transition is permitted iff every `hard` condition on it is `satisfied | waived | superseded` **and** no
active hold vetoes it (the veto applies only to transitions marked `holdVeto`, §4 preamble). Failed attempts are recorded (`transition_blocked` history) with the open
condition refs. Waiver is **only** via a Decision (`kind=waiver`, outcome=waive) linked to the condition
(I-8, D-09), permission per §2.2; the condition shows `waived` with the decision ref in every explanation.

### 5.5 Explanation ("before this issues", PEC-DEL-004)
`explainTransition(record, transition)` returns each condition: ref, description, type, severity, state
(satisfied / open / blocked-by-hold / waived / superseded), owner, need_by, satisfying record ref or
waiver decision ref. This one payload backs the deliverable panel, the 409 response body, and the tests.

---

## 6 Derived status

`core/src/status.ts`. Pure functions over a `ProjectSnapshot` (all live records of one project, loaded by
the repo layer in a handful of indexed queries; 10k open items is well inside memory budget,
PEC-NFR-003).

### 6.1 Deliverable health (PRD §8.2) — rule ids
Evaluated on the current revision, worst rule wins:
`DH-R1` red: forecast slip > 5 working days · `DH-R2` red: hold older than escalation threshold ·
`DH-R3` red: breached milestone-linked condition (hard condition past need_by on a deliverable with a
milestone) · `DH-A1` amber: any active hold · `DH-A2` amber: overdue open item/condition ·
`DH-A3` amber: forecast slip 1–5 working days · `DH-A4` amber: check comment aging past threshold ·
`DH-G` green otherwise.
**Forecast (P1, no plan):** `forecast_date = max(due_date, need_by of open work items / open hard
conditions / active holds on the current revision)`; slip = working days from due_date to forecast_date.
(P2 replaces with plan-sourced forecast.)

### 6.2 Package health (§8.3)
`PH-R1` any red deliverable linked to a package milestone (P1 reading: red deliverable with a non-empty
milestone) · `PH-R2` interface item overdue past escalation (implementer default: > 7 working days
overdue, `thresholds.interfaceOverdueRedWd`, configurable — the PRD §8.4 table has no interface row) ·
`PH-A1` ≥ 20% of active deliverables amber/red · `PH-A2` package-level decision past need_by · `PH-G`
otherwise. (Capacity rules are P2.)
**Explanation carry-through (ADR-012):** DH-* is an internal aggregation stage — PH-R1/PH-A1 state
each pressured deliverable's pressure in plain terms and carry the underlying issue/schedule records
(holds, overdue items, conditions, aging comments; capped at 3 per deliverable) into `contributing`,
so drill-down always lands on a cockpit-visible record; KPI-ONPLAN whys carry the plain-language
detail at deliverable granularity. The Overview package rollup additionally reports the cockpit's
log-scoped `openIssues` count (PEC-NFR-005).

### 6.3 Project health & thresholds (§8.4)
Project health = worst package health, floored by governance signals breaching at project level: a
warn-tier signal breach ⇒ **amber** contribution (health floors at amber); an escalate-tier breach ⇒
**red** contribution (health = red). Signals with warn/escalate defaults (all per-project configurable
via `project.thresholds`, PEC-OV-007):
hold age 7/14 wd · decision past need-by 0/7 d (or blocking an issue transition → red) · approval latency
(ready, undecided; measured from `ready_at`) 5/10 wd · open check-comment age 5/10 wd · untriaged intake age 2/5 wd · unanchored
items >0 warn, >5 or any older than 5 days escalate (P1 reading of "unanchored": untriaged intake items,
since anchored-ness is mandatory on controlled work) · schedule pressure 0/10 d.

### 6.4 Explanations (I-4, PEC-OV-002)
Every computed value returns `{value, ruleId, threshold, contributing: [{record_type, id, ref, why}]}`.
The API never returns a bare health string. The UI drill-down renders `contributing` as links.

### 6.5 Waiting on you (PEC-OV-004)
For the current user: decisions where they are authority in `pending` (age/need-by annotated), approval
records where they are a signatory in `ready`, plus what each blocks (records linked via conditions on
gated transitions). Sorted by §6.3 breach severity. The API returns **all** pending-on-you items, each
annotated with its breach level; the Overview surface (PEC-OV-004) shows the threshold-breaching ones
prominently and the rest collapsed — the deliberate P1 interpretation of PEC-OV-004's threshold clause.

---

## 7 API

REST, JSON, session cookie auth (`POST /api/auth/login`, scrypt verify; SSO is P2). Errors:
`{error: {code, message, details}}`. Optimistic concurrency: mutating requests carry `version`; stale →
`409 VERSION_CONFLICT` with intervening history entries (PEC-NFR-004). Blocked transitions →
`409 CONDITIONS_OPEN` with the §5.5 explanation payload. Permission denial → `403` with required role.

Route groups (all under `/api/projects/:pid/`, RBAC per §2.2; viewer read-only):

| Group | Endpoints (summary) |
|---|---|
| overview | `GET overview` → KPIs + package rollup + waiting-on-you + top blockers, each with explain payloads (PEC-OV-001..005) |
| packages | `GET packages`, `GET packages/:id` (summary, deliverables by nearest commitment, needs-the-lead-this-week, decisions, interfaces) |
| deliverables | `GET deliverables?filters`, `POST deliverables`, `GET deliverables/:id` (metadata, revision chain, open items across record types, before-this-issues panel, evidence trail, distinct facts) |
| revisions | `POST deliverables/:id/revisions`, `POST revisions/:id/transition {to, issue_event?}`, `GET revisions/:id/explain?transition=` |
| work items | CRUD-without-delete + `POST work-items/:id/transition`, progress updates (history), commit-to-week flag |
| holds | `POST holds` (typed cause + links required), `POST holds/:id/resolve|withdraw`, `GET holds?cause=` |
| checks | `POST checks`, checklist item updates, `POST checks/:id/comments`, comment respond/accept/reopen, `POST checks/:id/accept` |
| approvals | `GET approval-register`, `POST approval-records`, `POST approval-records/:id/outcome` (creates Decision), supersede |
| decisions | `GET decisions`, `POST decisions`, state moves, `POST decisions/:id/outcome`, supersede |
| risks / interfaces | register CRUD-without-delete, link management |
| intake | `POST intake` (≤8 fields, PEC-AHL-003), `GET intake?state=`, `POST intake/:id/triage` (dispositions; converted → creates records atomically) |
| log | `GET log?log=&package=&owner=&type=&cause=&overdue=&anchored=` → the PEC-AHL-001 register: server-composed union of open work items, active holds, open interface items, and non-dispositioned intake items (flagged unanchored); each row: record type, ref, title, log, package, owner, age (working days), need-by, overdue flag, hold cause where applicable, anchor status. Derivation is server-side — the web layer holds no rules (§1) |
| conditions | `POST conditions` (manual, authorized), `POST conditions/:id/waive` (creates waiver Decision), `POST conditions/:id/satisfy` (resource/other only) |
| evidence / basis | `POST :recordType/:id/evidence` (any member except viewer, §2.2; attaching evidence fires evidence-type condition satisfaction, §5.3), `POST :recordType/:id/basis-refs` + supersede |
| my-week | `GET my-week` → committed items grouped by deliverable, checks/comments owed, waiting-on-others, each with "why in week" (PEC-MW-001..006) |
| notifications | `GET notifications`, `POST notifications/:id/read` |
| import/export | `POST import/:contract` (mdl, rail, decisions, risks; `?force=true` per §8) body = CSV text → per-row accept/reject report (§16); `GET export/:register.csv` mirrors import schemas — every register view (approvals, decisions, risks, interfaces, intake, log) exports exactly what is displayed; `GET export/commitments.csv` (individual weekly commitments, PRD §15); `GET reports/sponsor-brief` (print-HTML; PDF via browser print, ADR-010) |
| config | `GET/PUT config` (thresholds, causes, purposes, templates) — admin; audit-evented |

---

## 8 Import / export (PRD §16)

Importers in `server/src/import/`. Common behavior: parse CSV (RFC 4180, header row required), validate
row-by-row against the contract, return `{accepted: n, rejected: [{row, errors[]}]}` — never silently
drop. Imports are idempotent-by-key (doc_no, item_id, decision_id, risk_id). Re-import updates a matched
record only if its latest history entry is itself an import entry; rows edited in-app since the last
import are reported as per-row conflicts unless the import request carries `force=true` (which overwrites
and writes history). Unmatched keys create new records.

**Import state seeding.** An imported row is *created at* its imported lifecycle state — initial-state
seeding, not a transition, therefore outside the I-5 transition gates — with a history entry
`kind=import` recording the source file and the as-imported state. Conditions instantiate normally and
gate only *subsequent* transitions. No synthetic issue events are created for imported issued revisions
(the PEC-ARC-002 chain applies to in-system issues only). Rows with unrecognized state strings are
rejected per-row. MDL `state` values map to revision states, case/space tolerant: `in_work`/`in work`,
`in_check`/`in check`, `check_accepted`, `ready_for_approval`, `approved`, `issued`, `superseded`.

Contracts (required / optional columns) exactly as PRD §16. RAIL `type` mapping: `action | coordination |
risk_treatment | rework | other` → Work Item with `kind` = that value; `hold` → Hold with the typed
`hold_cause` column (required for hold rows, else the row is rejected) and a blocking link to the matched
deliverable's current revision; `interface` → Interface Item; unmatched/unknown `type` → reject the row
with reason. Rows with no matched `deliverable_ref` anchor — hold and interface rows included — land as
**intake items** flagged unanchored (I-2) rather than anchored records.

Exports use the same columns so a filtered register view round-trips; `GET export/rail.csv` includes
non-converted intake items as rows flagged unanchored, so import → export round-trips without losing
rows. Every register view exports exactly what is displayed (CSV, §7); `GET export/commitments.csv`
serves the individual weekly commitments report (PRD §15, ADR-010).

---

## 9 Web UI

React SPA, routes: `/login`, `/p/:pid/overview | packages | packages/:id | deliverables |
deliverables/:id | plan | log | my-week | registers/(approvals|decisions|risks|interfaces|intake) |
admin`. Shared components: `HealthBadge` (always click-to-explain, I-4), `ExplainDrawer`,
`ConditionsPanel` ("before this issues"), `RecordDrawer` (work item in place, PEC-MW-004), `RaiseItem`
dialog (global, every screen, ≤8 fields), `RegisterTable` (filter + CSV export of exactly what is
displayed), `HistoryTrail`. Plan is a P1 placeholder page stating the P2 scope (Now/Next/Later,
lookahead) and showing need-by-driven My Week source rules.

## 10 Testing

- `core/test/` — unit: every lifecycle transition table (legal + illegal moves), conditions engine
  (satisfaction wiring per type, hard vs warn, waiver-requires-decision, reopen flips satisfied→open),
  status rules (each rule id has a fixture), calendar math.
- `server/test/` — integration over a temp DB through the HTTP layer: **invariant suite** `invariants.test.ts`
  with named cases I-1..I-10 (e.g., I-5: issue transition with open hard condition → 409 + recorded
  attempt; I-7: UPDATE on history rejected by trigger; I-8: waive without decision impossible via API);
  RBAC matrix probes; optimistic concurrency; import round-trip; notification catalog.
- Traceability: `docs/TRACEABILITY.md` maps every P1 requirement id → module + test.

## 11 Exclusions (explicit)

Built in the P2 pass (2026-07-04, §14): Plan module, capacity, digests + notification severity,
dedicated interface register with aging, weekly package review packs, schedule import, supersession
links, plan-sourced forecast.

Still excluded: duplicate suggestion (P2 — wants pilot vocabulary to tune matching), SSO (P2 — wants an
IdP; auth stays pluggable behind `server/src/auth.ts`, ADR-007), checklist-sourced conditions (P2 —
§5.2 keeps the enum headroom only), EDMS live integration (P2+, import-only per D-03), supersession
propagation analysis (P3 — the P2 `supersession_link` rows are its substrate), routes/authority matrix
(P3), archive views (P3), lessons (P3), reconciliation (P3). Schema headroom kept: state strings not
DB-enums, condition `source` includes `checklist` (P2) and `route` (P3) strings.

## 12 Operations

Backup (PEC-NFR-009): a daily WAL-safe SQLite backup via `tools/backup.ts` meets the RPO ≤ 24 h. Restore
= replace the database file and restart the server. A **tested restore** is a pilot-readiness gate.

## 13 Security & invariant hardening

Two adversarial passes shaped the build: a design review against the PRD (§10 traceability) and a
red-team pass that attacked a running instance trying to violate every invariant. Confirmed defects and
their fixes (regression-tested in `server/test/hardening.test.ts`):

- **Input validation on writes (PEC-NFR-010, I-4).** Every date field is validated to `YYYY-MM-DD` at
  write time (`server/src/validate.ts`); a malformed date is rejected `400`, never stored. Defense in
  depth: the derived-status layer (`core/src/status.ts`, `core/src/calendar.ts`) treats any malformed
  stored date as absent rather than throwing, so no single record can 500 the role-home reads.
- **Import never bypasses the gate (I-5).** State-seeding on import applies only to *new* records
  (initial-state seeding, outside the transition gates). A re-import that names an existing in-system
  revision cannot advance its lifecycle state; the state field is reported as a conflict and ignored —
  issue-affecting transitions go through the gated workflow only.
- **Approval outcomes are a closed set (I-6).** `recordApprovalOutcome` accepts only
  `approve | conditionally_accept | reject | defer`; a free-form decision outcome is rejected `400`.
- **Instance admin is not break-glass for judgments (I-6).** Recording an approval outcome, a decision
  outcome, accepting a check, or accepting a comment requires the real signatory / authority / checker;
  `person.is_admin` grants config/taxonomy power only, never the authority to make an engineering judgment
  as itself (`PERSONAL_JUDGMENTS` in `core/src/permissions.ts`).
- **Supersession links a distinct live replacement (I-10).** A decision or approval record cannot
  supersede itself or a record that is itself superseded.
- **Log visibility on composed views (PEC-NFR-005).** Row lists that carry titles/details (top blockers,
  package decisions/interfaces/holds, "needs the lead") are visibility-filtered before serialization;
  derived counts and health still compute on the unfiltered snapshot (shared truth), and explanation refs
  outside the caller's visible logs are redacted to `type + ref` with the detail omitted.
- **Cross-view consistency (I-1).** A work item on any revision of a deliverable — including a superseded
  one — projects into the deliverable's open-items list and counts toward its health, so a deliverable
  never derives green while carrying an owned overdue item.

## 14 P2 — planning & capacity (PRD §12.4; ADR-013)

### 14.1 Data model (all project-scoped; PRD §13.1 P2 entities)
- `plan_item` (the Commitment): `ref (PLN-…), item_type (work_item | check | approval_record — I-9),
  item_id, horizon (now | next | later), week ('YYYY-Www', null = backlog), discipline (denormalized
  from the responsible person, editable), planned_hours, version`. UNIQUE(project, item_type, item_id).
- `plan_period`: `week UNIQUE(project, week), state (open | committed), committed_at/by`.
- `capacity_entry`: `week, discipline, hours`; UNIQUE(project, week, discipline) (PEC-PLAN-003).
- `schedule_activity` (imported, §16 P2): `activity_id UNIQUE(project), description, start_date,
  finish_date, package_id?, deliverable_id?`.
- `plan_shift` (the plan-change log; delete-trigger protected): `ref (PLS-…), plan_item_id,
  from/to horizon+week, reason (required), impact_statement, cross_package, affected_package_ids,
  state (applied | proposed | rejected), reviewed_by/at` + `plan_shift_link (record_type, record_id)`
  for conditions/holds/risks/interfaces/schedule activities (PEC-PLAN-008).
- `supersession_link` (PEC-AUTH-005; delete-trigger protected): `record_type, old_id, new_id,
  affected [{recordType, id, ref}]` — written by decision/approval supersession.
- P1 tables extended in place (`ensureColumn` migration): `work_item.commit_source (manual | plan)`,
  `notification.severity (info | warn | red)`.

### 14.2 Derivations (pure, `core/src/plan.ts`; consumed by status rules)
- `planHorizons(snap)` — Now/Next/Later with each placement resolved to its underlying record,
  responsible person, deliverable, and package (PEC-PLAN-001).
- `capacityView(snap, weeks)` — load vs capacity per (week, discipline); only open underlying records
  load; hours split by work/check/approval (I-9); `pct` and level (`warn > capacityWarnPct`,
  `red > capacityRedPct`, defaults 100/110 per §8.4). `capacityBreaches(snap)` = current-week cells.
- `lookahead(snap, weeks)` — rows deliverables, cells the derived weekly state with priority
  **Hold-by-cause > Issue (due week) > Approve > Check > Work**, sourced from plan items and schedule
  activities overlapping the week (PEC-PLAN-002). Holds show on the current week.
- Forecast (§6.1) gains plan-sourced candidates: Sunday of the latest planned week over the
  deliverable's sphere + mapped schedule-activity finishes (`planForecastCandidates`).
- New health rules: `PH-R3` red / `PH-A3` amber — current-week capacity breach in a discipline the
  package's planned records draw on (§8.3 P2, ADR-013 reading); `PH-A4` amber — interface overdue past
  `interfaceOverdueWarnWd` but under the PH-R2 escalation (PEC-PKG-008); `S-CAP` project signal
  (§8.4 capacity row). Amber order: PH-A1, PH-A2, PH-A3, PH-A4.
- `myWeek` committed-reason provenance: `commit_source='plan'` → "planning commitment — weekly commit".

### 14.3 Plan services & API (`server/src/services/plan.ts`)
`GET plan` (?weeks=1..12) → currentWeek, periods, horizons, lookahead, capacity, shifts (latest 50),
plannable (unplanned open work/checks/approvals) · `POST plan-items` (perm `plan.manage`: planner/pm/EM;
'now'/'next' require a week; 'now' requires a named responsible) · `PUT plan-items/:id` (hours/discipline
only — placement changes go through shifts) · `POST plan-items/:id/shift` (perm `plan.propose`: +leads;
reason required; cross-package → impact statement required, state `proposed`, affected leads notified
`plan_shift_review`) · `POST plan-shifts/:id/review` (perm `plan.review`; a package_lead must lead an
affected package; approve applies the move) · `POST plan/commit {week}` (perm `plan.commit`: planner/pm;
stamps `committed_week` + `commit_source='plan'` on the week's open planned work items, notifies
`week_committed`, idempotent; checks/approvals notify their responsible) · `PUT plan/capacity` (upsert).
`GET reports/package-pack/:id` — weekly review pack print-HTML (PEC-PKG-009). Interface register
(`GET interfaces`) gains `?giving=&receiving=&state=` filters + `overdueWd`/`aging` (PEC-INT-002).
Overview gains `schedulePressure` (six-week load vs capacity, PEC-OV-008) — the §8.4 signals grid
carries S-CAP. Permission additions: `plan.manage`, `plan.commit`, `plan.propose`, `plan.review`;
`risk.create` adds `planner` (PEC-PLAN-004/PEC-RISK-003).

### 14.4 Schedule import/export (§16 P2, D-04)
`POST import/schedule` — required `activity_id, description, start, finish`; optional
`package, deliverable_ref`. Rows upsert by `activity_id` and always refresh (import-owned data);
mapping columns update only when present in the CSV; a stated mapping that does not resolve rejects
the row. `GET export/schedule.csv` mirrors the schema; `GET export/lookahead.csv` exports the six-week
grid (PRD §15 P2).

### 14.5 Digests & severity (PEC-NOT-002/003)
The sweep additionally emits weekly digests — one notification per person per digest type per ISO week:
`digest_planning` (planner/pm: capacity breaches, uncommitted planned week), `digest_package_review`
(leads: holds/overdue decisions/late interfaces per package + pack pointer), `digest_judgments`
(authorities/signatories past threshold), `digest_holds` (hold owners), `digest_comments` (responders
past threshold). All time-driven notifications carry `severity` from the §8.4 thresholds; the web
notification inbox badges warn/red.

