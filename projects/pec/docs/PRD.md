# 9-Domains: Project Execution Control

**PRODUCT REQUIREMENTS DOCUMENT**

# 1 Product summary

9-Domains: Project Execution Control is a **software application**: a web-based, multi-user system of record with role-based
screens, controlled records, and derived status, for multidisciplinary engineering firms — initially focused on oil
and gas FEED and detailed-design projects.

It implements the operating model described in "The 9 Domains of Task Management," "12 Rules for Project Management,"
and "Managing Work at Scale." Those documents define the hierarchy, habits, and governance; the software is the shared
state those habits maintain.

It is not a generic task app, Kanban board, document repository, or scheduling tool. It is the execution-control layer
that connects individual action to deliverables, packages, project controls, decisions, approval records, checks, risks,
interfaces, document-control events, and governance. The product does not merely display status; it maintains the
controlled record from which status is derived.

The concept defines six role homes — Overview, Packages, Deliverables, Plan, Action & Hold Log, My Week — over one
record system: every work item is a projection of the same record, seen around a deliverable, in a register, or in time.

**Core claim.** Task management becomes strategic when every task is anchored to a deliverable, every deliverable
belongs to a package, every package rolls up into project controls, and every decision, hold, approval record, check,
risk, and issue event is visible in shared execution state.

# 2 Problem statement

Engineering projects fail at scale not because competent people cannot complete tasks, but because distributed work
creates unmanaged dependencies, assumptions, handoffs, and collisions. Capacity grows linearly with headcount; the
dependency web grows much faster. The primary failure modes are bottlenecks, distribution failure (the many-to-many
problem), turnover, and basis drift.

Generic tools fail here because they treat tasks as isolated units. They do not represent deliverable lifecycle, holds
by cause, required checks, approval basis, decision dependencies, interface obligations, lookahead commitments, or the
difference between "work done" and "ready to issue."

**Basis drift is the defining risk.** Work proceeds on an assumption, authority, design basis, or decision that later
changes, is superseded, or turns out to have been informal. The product must preserve not only what people are doing but
the recorded basis under which they are doing it — and identify what is affected when that basis changes.

# 3 Product vision — six questions, six homes

| **Role**                   | **Governing question**                   | **Home**          |
|----------------------------|------------------------------------------|-------------------|
| Sponsor / Project Manager  | Is the project coherent?                 | Overview          |
| Discipline / Package Lead  | How is my scope?                         | Packages          |
| Engineer of Record         | What does this document need?            | Deliverables      |
| Planner / Project Controls | What is committed, and can we do it?     | Plan              |
| Coordinator                | Is anything falling through?             | Action & Hold Log |
| Individual Contributor     | What do I owe, and what am I waiting on? | My Week           |

# 4 Conceptual foundation

## 4.1 The 9 Domains — tacit, not exposed

The product is grounded in the nine domains of task management: Action Item, Assign, Prioritize, Status & Documentation,
Work, PLAN!, Approval, Check, Decide. They are product primitives, not UI modules. The interface expresses them through
ordinary engineering controls — assignments, priorities, conditions, registers, checks, approval records, decisions,
planning commitments, evidence, and history. The source document arranges the nine domains as a 3 × 3 ontology — rows
What / How / Why crossed with columns Data / Information / Knowledge — and then frames that grid successively within
project controls (logs, registers, MDL, schedule, lookahead, checklists) and project governance (scope, charter,
archive, lessons learned). The ontology remains the design rationale for one boundary the product must never blur:
Approval, Check, and Decide constitute the Why row — the judgment tier. The system structures, gates, and records
these acts; it never performs them.

## 4.2 Hierarchy (per "12 Rules", with one MVP simplification)

Project → Package → Deliverable → Revision. Tasks are tracked at the level of deliverables; decisions are tracked at the
level of packages. The 12 Rules hierarchy includes a Document layer between Deliverable and Task; for MVP the Document
collapses into the Deliverable, and controlled work happens on the Deliverable Revision (decision D-01). A Document
grouping entity is added later only if a pilot master deliverables list requires deliverables composed of multiple
separately-revisioned documents.

## 4.3 The operating model (per "Managing Work at Scale")

Reduce coordination demand through package definition; eliminate recurring coordination through standards, templates,
and checklists; externalize the remaining coordination into shared state (logs, registers, basis documents); govern the
shared state so it can be trusted; maintain the habits that keep it current under load. The product is the shared state
plus the governance plus the habit support — §10 maps the habits to surfaces.

## 4.4 Controlled vocabulary

| **Term**           | **Definition**                                                                                                                                                                                            |
|-------------------------|-----------------------------------------------------------------------------------------------|
| Intake Item        | A raised concern before triage. Preserves the statement as raised; resolves into controlled records at triage.                                                                                            |
| Work Item          | The single assignable unit of controlled work (UI labels: action item, task). Always anchored; always owned.                                                                                              |
| Hold               | A first-class blocking record with a typed cause, owner, and need-by. Blocks other records via links; "on hold" is a derived state of the blocked record, never set directly.                             |
| Deliverable        | An engineering output on the master deliverables list, managed through controlled lifecycle states via its revisions.                                                                                     |
| Revision           | A specific revision of a deliverable — the surface on which work, check, approval, issue, and archive occur.                                                                                            |
| Approval Record    | The recorded authorization basis: the authority, requirement, route, hold point, or issue authorization that explains why work may proceed or why formal approval is required. Distinct from its outcome. |
| Approval (outcome) | The recorded consequence of a decision to approve — always a Decision linked back to the Approval Record.                                                                                               |
| Check              | Verification of a revision against defined criteria by a named checker, carrying review comments to closure and checker acceptance.                                                                       |
| Decision           | A recorded judgment: select, approve, reject, defer, conditionally accept, confirm basis, waive, or supersede — with rationale, authority, and affected records.                                        |
| Condition          | A requirement attached to a transition that must be satisfied, waived (by Decision), or superseded before the transition may occur.                                                                       |
| Issue Event        | A formal document-control event (IFR, IFA, IFC, transmittal, issued record) recorded against a revision.                                                                                                  |
| Interface Item     | A controlled obligation between packages, disciplines, vendors, or client: giving party, receiving party, required information, need-by.                                                                  |
| Evidence           | Attachment, markup, comment sheet, transmittal, basis reference, or history entry supporting a record.                                                                                                    |
| Basis Reference    | A pointer to the governing basis (DBM section, SOW, data sheet, standard, client direction) under which work proceeds.                                                                                    |
| Lesson Learned     | Reviewed project learning linked to originating records, with a disposition lifecycle.                                                                                                                    |

# 5 Product invariants

These hold across all phases. Every requirement in §12 must be implementable without violating them; any conflict is a
defect in the requirement.

| **\#** | **Invariant**                                                                                                                                                                                                                                          |
|-----------|-------------------------------------------------------------------------------------------------------------|
| I-1    | **One record, many views.** A work item exists once and is projected into My Week, Deliverables, Packages, the Log, Plan, and registers. No view owns a private copy.                                                                                  |
| I-2    | **No unanchored planned work.** An item cannot enter a plan, a rollup, or a report until anchored to a project object. Unanchored items remain visible and flagged until triaged.                                                                      |
| I-3    | **Holds are typed.** Every hold carries a cause (information, decision, approval requirement, resource, client input, interface, vendor data, other-configured), an owner, and a need-by.                                                              |
| I-4    | **Status is derived and explainable.** Health and lifecycle states are computed from records per §8. Every derived value drills down to its contributing records and the rule that classified it.                                                      |
| I-5    | **Transitions are condition-gated.** Issue-affecting transitions cannot occur while hard conditions are open. There is no generic "done" that bypasses conditions.                                                                                     |
| I-6    | **Approval ≠ Check ≠ Decide.** Checking verifies; the approval record is the authorization basis; approving is a decision whose outcome links to that basis. The system never stores a generic approval flag that hides which of these is outstanding. |
| I-7    | **Controlled records are append-only.** History on controlled records is immutable: who, what, when, why, under what authority. Correction is by superseding entry, never deletion.                                                                    |
| I-8    | **Waivers are Decisions.** Any waiver or override of a condition is recorded as a Decision linked to the condition, with authority and rationale.                                                                                                      |
| I-9    | **Checking and approving consume capacity.** Wherever the plan exists (P2+), check and approval effort loads capacity like any other work.                                                                                                             |
| I-10   | **Supersession never deletes.** A superseded basis, decision, or approval record remains visible as superseded, linked to its replacement, with affected records identified.                                                                           |

# 6 Object model decisions

v0.2 left seven ambiguities that would have been resolved differently by each implementer. They are resolved here;
rationale is recorded so the choices can be revisited deliberately.

| **\#** | **Decision**                                                                                                                                                                                                                                  | **Rationale**                                                                                                                                       |
|-----------|-------------------------------------------------------|-------------------------------------------------------|
| OM-1   | There is exactly **one assignable entity: Work Item**, with a kind field (action, coordination, risk-treatment, rework, other-configured). "Task" and "action item" are UI labels.                                                            | v0.2 listed Work Item, Task, and Action Item as separate entities; three tables for one concept guarantees drift.                                   |
| OM-2   | **Hold is a first-class record**, not a status value. It blocks one or more target records (work item, revision, deliverable, condition, issue event) through blocking links. "Blocked / on hold" is derived on the target from active holds. | One hold (e.g., missing vendor data) typically blocks several records; modeling it as a status on each target loses the single cause and its owner. |
| OM-3   | **Intake Item is a separate record** from the controlled records it becomes. It preserves the statement as raised, carries the triage disposition, and links to every record created from it.                                                 | Preserving the concern-as-raised (v0.2 PEC-AHL-011) is incompatible with editing the intake into the controlled item.                               |
| OM-4   | **Document collapses into Deliverable for MVP**; controlled work happens on the Revision. (Decision D-01.)                                                                                                                                    | In FEED practice most MDL rows are single documents. The extra layer costs every screen and import; add it only when a real MDL demands it.         |
| OM-5   | **Review Comments are child records of a Check**, each with an assigned responder. They project into My Week as obligations; they are not duplicated as work items.                                                                           | v0.2 allowed "work items or sub-items"; duplication creates double entry and reconciliation bugs.                                                   |
| OM-6   | **Approval outcomes are Decisions.** The register row (Approval Record) is the basis; the outcome is a Decision of type approval linked to it. No third object type.                                                                          | Preserves v0.2\'s explicit invariant while giving implementers one write path for all judgments.                                                    |
| OM-7   | **Interface Items are their own record type from P1**, but the dedicated register view arrives in P2; in P1 they surface through the Log and Packages. (Decision D-06.)                                                                       | Interfaces drive basis drift and cannot wait, but a dedicated view is not needed to capture and track them.                                         |

# 7 Lifecycles

The seven controlled lifecycles. Guards refer to the conditions engine (§9). "Blocked" is not a state in any machine ---
it is a derived overlay present whenever an active Hold links to the record (OM-2).

## 7.1 Intake Item

| **State**     | **Enters when**                                                                                                                                          | **Exits to**             |
|----------------------|--------------------------------------------------------------|------------------------------------|
| Raised        | Any authorized user submits the raise-an-item dialog (≤8 fields).                                                                                        | In triage                |
| In triage     | Coordinator opens it. Untriaged age is visible from Raised.                                                                                              | Dispositioned            |
| Dispositioned | Coordinator records: converted (→ controlled records created and linked), merged, duplicate, rejected, or parked. Original statement preserved verbatim. | Terminal (links live on) |

## 7.2 Work Item

| **State** | **Enters when**                                                                                                                                               | **Exits to**                                    |
|----------------------|--------------------------------------------------------------|------------------------------------|
| Open      | Created by triage conversion, by a lead/owner directly (anchored at creation), or by another record (decision follow-up, risk treatment, comment conversion). | In work, Cancelled                              |
| In work   | Owner starts or logs activity.                                                                                                                                | Closed, Open                                    |
| Closed    | Owner marks complete AND all closure conditions are satisfied/waived (guard). Otherwise the attempt is blocked with the open conditions listed.               | Reopened (by supersession or checker rejection) |
| Cancelled | Lead or coordinator cancels with reason; history retained.                                                                                                    | Terminal                                        |

## 7.3 Hold

| **State** | **Enters when**                                                                                                                                                                              | **Exits to**        |
|----------------------|--------------------------------------------------------------|------------------------------------|
| Active    | Raised with typed cause, owner, need-by, and ≥1 blocking link. Appears in Overview, Packages, Deliverables, Log, and blocked owners\' My Week.                                               | Resolved, Withdrawn |
| Resolved  | Owner records the resolving fact (decision recorded, information received with evidence, resource assigned, approval recorded). Blocked records become available; their owners are notified. | Terminal            |
| Withdrawn | Raised in error; reason recorded.                                                                                                                                                            | Terminal            |

## 7.4 Check

| **State**       | **Enters when**                                                                                                                                              | **Exits to**                      |
|----------------------|--------------------------------------------------------------|------------------------------------|
| Open            | Check created on a revision with checker and checklist template. Independence warning if checker = originator (block configurable, P3).                      | In check                          |
| In check        | Checker working the checklist; comments raised as child records (originator, responder, response, disposition, evidence, reopen).                            | Comments open                     |
| Comments open   | ≥1 comment unresolved. Responder obligations project into My Week.                                                                                           | Comments closed                   |
| Comments closed | All comments dispositioned and accepted by the checker individually.                                                                                         | Accepted, In check (reopen)       |
| Accepted        | Checker records acceptance of the revision. Satisfies check-type conditions. Checklist completion, comment closure, and acceptance are three distinct facts. | Reopened (new rev / supersession) |

## 7.5 Approval Record

| **State**                | **Enters when**                                                                                                                                                                                               | **Exits to**             |
|----------------------|--------------------------------------------------------------|------------------------------------|
| Required                 | Requirement identified: type, source of authority, applicable object, required decision type, named signatories (P1) or route template (P3).                                                                  | Prerequisites incomplete |
| Prerequisites incomplete | Any prerequisite condition open (typically: check accepted, required decisions made, evidence attached).                                                                                                      | Ready                    |
| Ready                    | All prerequisite conditions satisfied/waived (guard). Signatories notified.                                                                                                                                   | Decided                  |
| Decided                  | Outcome recorded as a linked Decision: approved, approved with conditions (conditions instantiated), rejected (→ rework items), or deferred (need-by reset). Record shows outcome but remains a basis record. | Superseded               |
| Superseded               | Basis changes; replacement linked; affected records identified for review (P2 link, P3 propagation).                                                                                                          | Terminal                 |

## 7.6 Decision

| **State**        | **Enters when**                                                                                                      | **Exits to**           |
|----------------------|--------------------------------------------------------------|------------------------------------|
| Identified       | Need for decision recorded: statement, affected objects, need-by.                                                    | In progress            |
| In progress      | Preparer assigned (distinct from decision authority); options and recommendation assembled.                          | Pending decision       |
| Pending decision | Package ready; authority notified; appears in blocking views and Waiting-on-you.                                     | Decided                |
| Decided          | Authority records outcome, rationale, conditions created/satisfied, follow-up work items generated.                  | Reconciled, Superseded |
| Reconciled (P3)  | Decision incorporated into governing basis (DBM, SOW, data sheet) with document reference — the monthly loop, §10. | Terminal               |
| Superseded       | Later decision supersedes; affected records flagged for review.                                                      | Terminal               |

## 7.7 Deliverable Revision

| **State**                       | **Enters when**                                                                                                                          | **Exits to**            |
|----------------------|--------------------------------------------------------------|------------------------------------|
| In work                         | Revision created (from template conditions, §9). Open work items live here.                                                              | In check                |
| In check                        | Check opened. May return to In work on rework without ceremony — loops are expected.                                                   | Check accepted, In work |
| Check accepted                  | Per 7.4. Guard for approval readiness.                                                                                                   | Ready for approval      |
| Ready for approval              | All approval prerequisites met on linked Approval Record(s).                                                                             | Approved                |
| Approved / Authorized for issue | Approval outcome(s) recorded as Decisions; issue authorization confirmed where required.                                                 | Issued                  |
| Issued                          | Issue Event recorded: purpose (IFR/IFA/IFC/other, D-07), transmittal reference, recipients. Archive reference created (P3 full archive). | Returned, Superseded    |
| Returned with comments          | Client/external comments logged as review comments on the revision (D-10); next revision typically opens.                                | → new revision In work  |
| Superseded                      | Replaced by later revision; chain preserved.                                                                                             | Archived (P3)           |

# 8 Derived status — default rules and thresholds

All rules are project-configurable; these defaults ship enabled so the product works on day one (v0.2 risk: "derived
status may become a black box"; the corresponding invariant is I-4 — every value drills down).

## 8.1 Revision lifecycle state

Derived per §7.7 from the record graph: open work items, check state, approval record states, conditions, and issue
events. A manual state override does not exist; what exists is waiver of specific conditions (I-8).

## 8.2 Deliverable health

-   **Green — on plan.** No active hold, no overdue conditions, forecast (from plan where present, else need-by dates)
    does not breach the due date.

-   **Amber — pressure.** Any active hold; or any overdue open item/condition; or forecast slip ≤ 5 working days; or
    check comments aging past threshold.

-   **Red — schedule risk.** Forecast slip \> 5 working days, or a hold older than its escalation threshold, or a
    breached milestone-linked condition.

## 8.3 Package health

-   **Red** if any red deliverable is linked to a package milestone, or any interface item is overdue past escalation,
    or (P2) committed load \> 110% of capacity in the current week.

-   **Amber** if ≥ 20% of active deliverables are amber/red, or any decision owned at package level is past need-by, or
    (P2) load \> 100%.

-   **Green** otherwise.

## 8.4 Project health and default thresholds

Project health is the worst package state, escalated one level if any governance threshold below is breached at project
level. Every threshold is configurable per project (v0.2 PEC-OV-007 preserved).

| **Signal**                                 | **Warn (amber contribution)** | **Escalate (red contribution)**            |
|--------------------------------------------|-------------------------------|--------------------------------------------|
| Hold age                                   | \> 7 working days             | \> 14 working days                         |
| Decision past need-by                      | \> 0 days                     | \> 7 days, or blocking an issue transition |
| Approval latency (record Ready, undecided) | \> 5 working days             | \> 10 working days                         |
| Check comment age (open)                   | \> 5 working days             | \> 10 working days                         |
| Untriaged intake age                       | \> 2 working days             | \> 5 working days                          |
| Unanchored items                           | \> 0                          | \> 5, or any older than 5 days             |
| Capacity (P2)                              | \> 100% committed             | \> 110% committed                          |
| Schedule forecast vs gate                  | \> 0 days pressure            | \> 10 days pressure                        |

# 9 Conditions engine

Conditions are the mechanism behind I-5 and the deliverable\'s "before this issues" panel. Semantics:

-   **Attachment.** A condition attaches to a transition of a parent record (e.g., Revision → Issued; Work Item →
    Closed; Approval Record → Ready), not loosely to the record.

-   **Type** determines what satisfies it: check (a Check reaches Accepted), decision (a linked Decision reaches
    Decided), approval (a linked Approval Record reaches Decided-approved), evidence (a named artifact attached),
    interface (interface item resolved), document-control (transmittal/issue prerequisites), resource, other.

-   **Instantiation.** Conditions are instantiated when a revision (or record) is created, from condition templates
    keyed by deliverable type + issue purpose + package, plus any added by decisions ("approved with conditions"),
    routes (P3), checklists, or manually by authorized roles. Source is recorded on each condition.

-   **Severity.** Hard conditions block the transition; warning conditions log and notify but do not block. Default
    (D-11): hard = issue-affecting transitions and approval recording without authority; everything else warns. Severity
    is configurable per template.

-   **Evaluation.** A transition is permitted when every hard condition on it is satisfied, waived, or superseded.
    Failed attempts are recorded with the open conditions listed (metric: prevented invalid closures).

-   **Waiver.** Always a Decision linked to the condition, with authority and rationale (I-8, D-09). Waivers appear in
    the issue-readiness explanation.

-   **Explanation.** Any record with conditions can render an issue-readiness explanation: each condition with state
    (satisfied / open / blocked-by-hold / waived / superseded), owner, and satisfying record.

# 10 Operating cadence

The product exists to support habits, not replace them ("Managing Work at Scale"). Each cadence maps to surfaces; the
monthly loop is new in v0.3.

| **Cadence**            | **Habit (source model)**                                                                                                                                                            | **Product surface**                                                                                                                                                              |
|--------------------|-----------------------------------------------------|------------------------------------------------|
| Daily — individual   | Update touched items; surface Needs (information, decisions, approvals, resources) and Risks of Change (budget, scope, schedule).                                                   | My Week updates; raise-an-item dialog available on every screen with those quick types (P1).                                                                                     |
| Weekly — team        | Consolidate cross-cutting items to the project log; triage; Now / Next / Later and 6-week lookahead planning; package review; close-out feedback per RACI / interface register.     | Coordinator triage queue (P1); Plan module and commitment generation (P2); Packages review + weekly pack (P2); closure notifications to raiser and affected parties (P1).        |
| Monthly — governance | Reconcile decisions into DBM, SOWs, package data sheets; lifecycle Identified → In Progress → Pending Approval → Approved → Reconciled; re-issue soft revisions of basis documents. | Reconciliation queue of Decided-but-unreconciled decisions; Reconciled state with governing-document reference; monthly reconciliation report; supersession review (P3, §12.13). |

# 11 Users and role homes

Personas are unchanged from v0.2 §7 and are summarized by the table in §3. One addition for clarity: the **Document
Controller** works primarily in Deliverables (revision metadata, issue events, transmittal references) and Archive (P3),
and owns document-control data quality without owning engineering content. The **Coordinator** owns tracker hygiene ---
triage, anchoring, routing, disposition — while accountable work always belongs to named owners (12 Rules, rule 11).

# 12 Functional requirements

Phase key: **P1** = MVP (controlled tracker replacement) · **P2** = planning and capacity · **P3** = governance,
archive, reconciliation. IDs are stable with v0.2 where the requirement survives; merged or dropped v0.2 IDs are noted.

## 12.1 Overview (wireframe sheet 01)

| **ID**     | **Requirement**                                                                                                                                                                     | **Ph.** |
|--------------------|------------------------------------------------------------------------------------------|-----------|
| PEC-OV-001 | Display project KPIs — health, % deliverables on plan, holds by cause, open decisions, approvals in flight, schedule forecast — each computed per §8. (Merges v0.2 OV-001/002.) | P1      |
| PEC-OV-002 | Every KPI and health value drills down to its contributing records and the rule/threshold that classified it (I-4).                                                                 | P1      |
| PEC-OV-003 | Package rollup table: package, lead, deliverables on plan, holds, checks/approvals due, open decisions, health; rows open the package.                                              | P1      |
| PEC-OV-004 | "Waiting on you": decisions and approvals where the current user is the authority and age or need-by breaches a §8.4 threshold, with what each blocks.                              | P1      |
| PEC-OV-005 | Blocking items are typed by cause (information, decision, approval requirement, risk, resource, interface) wherever they appear.                                                    | P1      |
| PEC-OV-006 | Export sponsor brief (per §15).                                                                                                                                                     | P1      |
| PEC-OV-007 | Thresholds configurable per project; defaults per §8.4.                                                                                                                             | P1      |
| PEC-OV-008 | Schedule-pressure view derived from lookahead load vs capacity.                                                                                                                     | P2      |

Acceptance: a PM sees the top blockers without opening a deliverable; sponsor-required decisions/approvals are separated
from noise; every rollup traces to records.

## 12.2 Packages (sheet 02)

| **ID**      | **Requirement**                                                                                                                                                                | **Ph.** |
|--------------------|------------------------------------------------------------------------------------------|-----------|
| PEC-PKG-001 | Package list with derived health (§8.3).                                                                                                                                       | P1      |
| PEC-PKG-002 | Package summary: deliverables on plan, holds by cause, open interfaces, open decisions.                                                                                        | P1      |
| PEC-PKG-003 | Package capacity/discipline load for the current planning period.                                                                                                              | P2      |
| PEC-PKG-004 | Deliverables in the package ordered by nearest commitment or need-by.                                                                                                          | P1      |
| PEC-PKG-005 | "Needs the lead this week": items where the accountable role is the package lead — sign-offs due, decisions to rule, holds to resolve, reassignments, interface obligations. | P1      |
| PEC-PKG-006 | Package-level decisions linked to affected deliverables and interfaces (12 Rules: decisions tracked at package level).                                                         | P1      |
| PEC-PKG-007 | Interface items carry giving party, receiving party, affected deliverables, required information, need-by, state, blocking impact (OM-7).                                      | P1      |
| PEC-PKG-008 | Interface aging feeds package health.                                                                                                                                          | P2      |
| PEC-PKG-009 | Generate weekly package review pack.                                                                                                                                           | P2      |

Acceptance: a lead determines what needs their action this week on one screen and can navigate from any item to the
affected deliverable, hold, decision, risk, interface, or approval record.

## 12.3 Deliverables (sheet 03)

| **ID**      | **Requirement**                                                                                                                                                                       | **Ph.** |
|--------------------|------------------------------------------------------------------------------------------|-----------|
| PEC-DEL-001 | Active deliverables list with filters (package, discipline, state, due, hold cause); master list and issued records under the same filters.                                           | P1      |
| PEC-DEL-002 | Deliverable metadata: doc number, title, revision, package, discipline, owner, document-control reference, milestone, due, derived state.                                             | P1      |
| PEC-DEL-003 | Open items on a deliverable across all record types: work items, checks and their comments, holds blocking it, approval records, decision dependencies.                               | P1      |
| PEC-DEL-004 | "Before this issues" panel: the conditions on the next transition with state, owner, and satisfying record (§9 explanation).                                                          | P1      |
| PEC-DEL-005 | Evidence trail: updates, attachments, markups, comment sheets, transmittals, basis references. A status update and its history entry are the same record (v0.2 DEL-006).              | P1      |
| PEC-DEL-006 | State managed at revision level per §7.7; revision chain visible.                                                                                                                     | P1      |
| PEC-DEL-007 | Hard conditions block invalid transitions; the attempt is recorded with open conditions listed; waiver path per I-8.                                                                  | P1      |
| PEC-DEL-008 | Issue events recorded with purpose, transmittal reference, recipients; linked to revision, approval record, decision, and archive reference.                                          | P1      |
| PEC-DEL-009 | Distinct visible facts: work complete, check accepted, approval recorded, authorized for issue, issued, returned with comments, superseded, archived — never one merged flag (I-6). | P1      |

Acceptance: the responsible engineer sees exactly what prevents issue; a revision cannot be treated as issued with open
hard conditions; every state is explainable from records.

## 12.4 Plan (sheet 04)

| **ID**       | **Requirement**                                                                                                                                                                   | **Ph.** |
|--------------------|------------------------------------------------------------------------------------------|-----------|
| PEC-PLAN-001 | Now / Next / Later planning horizons; "Now" items carry named owner and confirmed capacity.                                                                                       | P2      |
| PEC-PLAN-002 | Six-week lookahead: rows are deliverables, cells are the derived weekly state (Work, Check, Approve, Hold-by-cause, Issue), sourced from the plan and integrated-schedule import. | P2      |
| PEC-PLAN-003 | Capacity by discipline/role for each week; check and approval hours load capacity (I-9).                                                                                          | P2      |
| PEC-PLAN-004 | Overcapacity flagged per §8.4; may create or link a Risk.                                                                                                                         | P2      |
| PEC-PLAN-005 | Proposed plan shifts carry an impact statement (milestones, capacity, affected deliverables) and require review by affected leads when impacts cross packages.                    | P2      |
| PEC-PLAN-006 | Every plan shift records its reason; the plan-change log is visible at weekly review.                                                                                             | P2      |
| PEC-PLAN-007 | Weekly commit generates the My Week set for each person (see PEC-MW-007).                                                                                                         | P2      |
| PEC-PLAN-008 | Plan shifts link to affected conditions, holds, risks, and schedule activities.                                                                                                   | P2      |

Acceptance: a planner can identify overloaded checking resources; every plan change traces to a reason and its affected
leads; check/approval work consumes capacity.

## 12.5 Action & Hold Log and intake (sheet 05)

| **ID**      | **Requirement**                                                                                                                                                                                                                                                                                 | **Ph.** |
|--------------------|------------------------------------------------------------------------------------------|-----------|
| PEC-AHL-001 | All open items across logs and packages in one filterable register: log, package, owner, age, type, hold cause, overdue, anchor status.                                                                                                                                                         | P1      |
| PEC-AHL-002 | Three logs minimum: Package, Internal, Client/Project; log determines visibility and formality; items never change log silently.                                                                                                                                                                | P1      |
| PEC-AHL-003 | Raise-an-item available on every screen; ≤ 8 fields: type, statement, anchor suggestion, need-by, suggested owner, log. Quick types include the daily-habit set: Needs (information, decision, approval, resource) and Risks of Change (budget, scope, schedule), plus action, hold, interface. | P1      |
| PEC-AHL-004 | Intake preserved verbatim after triage (OM-3); disposition enum: converted, merged, duplicate, rejected, parked.                                                                                                                                                                                | P1      |
| PEC-AHL-005 | One intake may resolve into multiple controlled records (work item, hold, risk, decision, approval record, interface item, review comment), each back-linked.                                                                                                                                   | P1      |
| PEC-AHL-006 | Triage queue with untriaged age; anchoring, owner, priority, and log confirmed at triage; unanchored items flagged and excluded from plans and rollups (I-2).                                                                                                                                   | P1      |
| PEC-AHL-007 | Raiser is notified at routing, ownership, and closure of records created from their intake.                                                                                                                                                                                                     | P1      |
| PEC-AHL-008 | Duplicate/similar-item suggestion at intake and triage.                                                                                                                                                                                                                                         | P2      |

Acceptance: anyone can raise a concern without knowing the routing; the coordinator can route, anchor, assign, and
disposition; nothing disappears between raised and dispositioned.

## 12.6 My Week (sheet 06)

| **ID**     | **Requirement**                                                                                                                                                                      | **Ph.** |
|--------------------|------------------------------------------------------------------------------------------|-----------|
| PEC-MW-001 | The user\'s committed items for the current week, grouped by deliverable.                                                                                                            | P1      |
| PEC-MW-002 | Checks and comment responses the user owes others, shown as booked work, distinct from their own deliverable items.                                                                  | P1      |
| PEC-MW-003 | "Waiting on others" section: holds and decisions gating the user\'s work — visible, chase-able, not counted as personal commitments.                                               | P1      |
| PEC-MW-004 | Work-item panel opens in place: anchor, owner, priority with provenance, closure conditions, activity + evidence, path/history; progress updates and attachments without navigation. | P1      |
| PEC-MW-005 | Every item shows why it is in the week: planning commitment (P2), need-by date, escalation rule, or manual commitment.                                                               | P1      |
| PEC-MW-006 | Overdue items flagged; overdue-to-someone-else (checks owed) flagged equally.                                                                                                        | P1      |
| PEC-MW-007 | Week set generated by the weekly planning commit; P1 interim: need-by dates plus a manual "commit to this week" flag.                                                                | P2      |

## 12.7 Approval Register (authorization basis)

The register is not a signature list. It records the authority, requirement, permission, route, hold point, or issue
authorization that compels action — and links the eventual outcome back to it.

| **ID**       | **Requirement**                                                                                                                                                                                                                                                                                  | **Ph.** |
|--------------------|------------------------------------------------------------------------------------------|-----------|
| PEC-AUTH-001 | Register of approval records with: ID, type, source of authority, applicable object(s), authority holder, required decision type, named signatories, governing basis reference, due date / hold point, state per §7.5, related checks / decisions / risks, evidence. (Merges v0.2 AUTH-001/002.) | P1      |
| PEC-AUTH-002 | Requirement, readiness, and outcome are distinct visible states (§7.5); outcome is a linked Decision (OM-6, I-6). (Merges v0.2 AUTH-003/007/008/012.)                                                                                                                                            | P1      |
| PEC-AUTH-003 | An approval record may compel work items, checks, decisions, or revision transitions via conditions.                                                                                                                                                                                             | P1      |
| PEC-AUTH-004 | Closure guard: a required approval record cannot close on task completion alone — the decision must be recorded, required checks accepted, affected records updated (v0.2 AUTH-005).                                                                                                           | P1      |
| PEC-AUTH-005 | Supersession: superseded state with replacement link.                                                                                                                                                                                                                                            | P2      |
| PEC-AUTH-006 | Supersession impact: affected deliverables, work items, checks, decisions, holds, and issue events identified and flagged for owner review (basis-drift response).                                                                                                                               | P3      |
| PEC-AUTH-007 | Configurable approval route templates by project, package, discipline, deliverable type, issue purpose, lifecycle state.                                                                                                                                                                         | P3      |
| PEC-AUTH-008 | Authority matrix: who may approve/decide by role, organization, package, threshold, delegation (with recorded basis and expiry).                                                                                                                                                                 | P3      |

Acceptance: a user can determine why an approval is required, not only who signs; requirement vs pending vs result are
distinguishable; issue cannot proceed on work completion alone.

## 12.8 Checks and checking

| **ID**      | **Requirement**                                                                                                                                                                               | **Ph.** |
|--------------------|------------------------------------------------------------------------------------------|-----------|
| PEC-CHK-001 | Checklist templates by discipline, package, deliverable type, or project standard; instantiated per check.                                                                                    | P1      |
| PEC-CHK-002 | Check record per §7.4 with child review comments: originator, responder, response, disposition, closure evidence, reopened flag, individual checker acceptance (merges v0.2 CHK-002/003/006). | P1      |
| PEC-CHK-003 | Three distinct facts, never merged: checklist completion, comment closure, checker acceptance (v0.2 CHK-005).                                                                                 | P1      |
| PEC-CHK-004 | Independence: warn when owner and checker are the same person; hard block configurable.                                                                                                       | P1 / P3 |
| PEC-CHK-005 | Checker acceptance may satisfy conditions but is not approval unless the route explicitly grants it and the outcome is recorded as a Decision (v0.2 CHK-008).                                 | P1      |
| PEC-CHK-006 | Checking effort available to Plan for capacity loading (I-9).                                                                                                                                 | P2      |

## 12.9 Decisions register

| **ID**      | **Requirement**                                                                                                                                                                                                                                                                                                               | **Ph.** |
|--------------------|------------------------------------------------------------------------------------------|-----------|
| PEC-DEC-001 | Decision log per §7.6 with: ID, title, decision-needed statement, preparer, decision authority (distinct roles), need-by, affected packages/deliverables/interfaces/risks, options considered, recommendation, outcome, rationale, date, follow-up items, conditions created or satisfied. (Merges v0.2 DEC-001/002/005/006.) | P1      |
| PEC-DEC-002 | Decisions linkable to blocking holds and deliverables; overdue decisions surface in Overview, Packages, and Deliverables.                                                                                                                                                                                                     | P1      |
| PEC-DEC-003 | Outcome vocabulary: select, approve, reject, defer, conditionally accept, confirm basis, waive, supersede (v0.2 DEC-007).                                                                                                                                                                                                     | P1      |
| PEC-DEC-004 | Supersession flags affected deliverables, checks, approval records, risks, holds, and plan commitments for review.                                                                                                                                                                                                            | P3      |
| PEC-DEC-005 | Reconciled state with governing-document reference (§10 monthly loop).                                                                                                                                                                                                                                                        | P3      |

## 12.10 Risk log

| **ID**       | **Requirement**                                                                                                                                                            | **Ph.** |
|--------------------|------------------------------------------------------------------------------------------|-----------|
| PEC-RISK-001 | Risk log: ID, title, cause, consequence, affected package/deliverable, owner, probability, impact, mitigation, need-by, status, linked actions/decisions/holds/conditions. | P1      |
| PEC-RISK-002 | Risk treatment work items appear in Packages, Deliverables, and My Week when assigned.                                                                                     | P1      |
| PEC-RISK-003 | Capacity overload can create or link a risk (with PEC-PLAN-004).                                                                                                           | P2      |

## 12.11 Interfaces

| **ID**      | **Requirement**                                                                                                  | **Ph.** |
|--------------------|------------------------------------------------------------------------------------------|-----------|
| PEC-INT-001 | Interface item record per PEC-PKG-007; raised via intake or directly by leads; surfaces in the Log and Packages. | P1      |
| PEC-INT-002 | Dedicated interface register view with aging and giving/receiving filters.                                       | P2      |

## 12.12 Archive and lessons learned

| **ID**      | **Requirement**                                                                                                                                                                                                                                                                                                                      | **Ph.**             |
|--------------------|------------------------------------------------------------------------------------------|-----------|
| PEC-ARC-001 | Issued revisions carry archive references from P1 (issue event chain); full archive views of issued deliverables, closed decisions, closed risks, and approval chains.                                                                                                                                                               | P3                  |
| PEC-ARC-002 | Controlled chain preserved for every issued revision: revision, issue purpose, transmittal, checks, approval record, decision(s), conditions (incl. waivers), evidence (v0.2 ARC-004).                                                                                                                                               | P1 chain / P3 views |
| PEC-ARC-003 | Lessons learned records linked to originating records; proposed from reopened items, late decisions, recurring holds, rejected approvals, comment patterns, interface failures, basis-drift events; disposition lifecycle: candidate → reviewed → accepted/rejected → assigned to standard/template update → implemented → archived. | P3                  |
| PEC-ARC-004 | Accepted lessons can update checklist and condition templates (closing the loop into "eliminate recurring coordination").                                                                                                                                                                                                            | P3                  |

## 12.13 Reconciliation (new in v0.3)

| **ID**      | **Requirement**                                                                                                                                                | **Ph.** |
|--------------------|------------------------------------------------------------------------------------------|-----------|
| PEC-REC-001 | Reconciliation queue: decisions in Decided state not yet Reconciled, ordered by age and scope impact.                                                          | P3      |
| PEC-REC-002 | Reconciling a decision records the governing document updated (DBM section, SOW, package data sheet), the soft-revision reference, and the reconciling person. | P3      |
| PEC-REC-003 | Monthly reconciliation report: decisions reconciled, outstanding, and basis documents touched.                                                                 | P3      |

## 12.14 Notifications

Principle (kept from v0.2): notifications direct users to the relevant role home or record — never to detached
threads. Every notification identifies the record, why the user is notified, the required next action, the due date or
threshold, and where to resolve it.

| **ID**      | **Requirement**                                                                                                                                                                                                                                           | **Ph.** |
|--------------------|------------------------------------------------------------------------------------------|-----------|
| PEC-NOT-001 | Event notifications: assignment; item overdue; hold blocks your record; decision you own past need-by; approval or check requires you; item you raised routed/updated/closed; revision ready for check or approval; basis affecting your work superseded. | P1      |
| PEC-NOT-002 | Role digests: weekly planning, package review, overdue decisions/approvals, open holds, comment aging.                                                                                                                                                    | P2      |
| PEC-NOT-003 | Escalation thresholds per §8.4 drive notification severity and Waiting-on-you placement.                                                                                                                                                                  | P2      |

# 13 Data model

## 13.1 Entities by phase

| **Entity**                                                            | **Purpose**                                                                                 | **Ph.**                  |
|------------------------------------|-------------------------------------------------------------------------|-----------|
| Project, Package, Deliverable, Revision                               | Hierarchy per §4.2 (Document deferred, D-01).                                               | P1                       |
| Intake Item                                                           | Concern as raised + disposition (OM-3).                                                     | P1                       |
| Work Item                                                             | Single assignable unit (OM-1).                                                              | P1                       |
| Hold                                                                  | Typed blocking record with blocking links (OM-2).                                           | P1                       |
| Check, Checklist (template + instance), Review Comment                | Verification per §7.4 (OM-5).                                                               | P1                       |
| Approval Record                                                       | Authorization basis per §7.5.                                                               | P1                       |
| Decision                                                              | Judgment record per §7.6; also carries approval outcomes (OM-6).                            | P1                       |
| Risk, Interface Item                                                  | Registers per §12.10--11.                                                                   | P1                       |
| Condition (+ Condition Template)                                      | Transition gates per §9.                                                                    | P1                       |
| Issue Event                                                           | Document-control event with transmittal reference.                                          | P1                       |
| Evidence / Attachment, History Entry, Basis Reference                 | Record support; history is append-only (I-7).                                               | P1                       |
| Person, Role, Project Role Assignment                                 | Identity and permissions (§14).                                                             | P1                       |
| Plan Period, Commitment, Capacity Entry, Schedule Activity (imported) | Planning per §12.4.                                                                         | P2                       |
| Supersession Link                                                     | Old basis → replacement, with affected-record set.                                          | P2 link / P3 propagation |
| Approval Route Template, Authority Matrix Entry, Delegation           | Governed approval routing.                                                                  | P3                       |
| Archive Record, Lesson Learned, Reconciliation Entry                  | Governance memory per §12.12--13.                                                           | P3                       |
| Audit Event                                                           | Critical-change trail beyond history entries (approval, issue, waiver, permission changes). | P1                       |

## 13.2 Work Item — required fields

| **At creation**                                                                                                                                                                                | **At closure**                                                                                                                                                                                                                         |
|------------------------------------------------------------|------------------------------------------------------------|
| ID (system); title; statement; kind; log; anchor object (I-2); package (derived from anchor); owner; need-by; created-by/date; source link (intake, decision, comment, risk) where applicable. | Closure conditions satisfied or waived-by-Decision; closing statement or evidence where the template requires it; closed-by/date (system). Optional throughout: support roles, priority provenance, plan period (P2), related records. |

## 13.3 Condition — fields

Condition ID; parent record and gated transition; type (§9); required object/event; source (template, checklist, route,
decision, manual — with reference); severity (hard / warn); owner; need-by; state (open, satisfied, waived,
superseded, blocked); satisfied-by record and date; waiver Decision link where applicable; history.

## 13.4 Relationship notes

-   Work Item anchors to exactly one primary object (deliverable, revision, package, decision, approval record, risk,
    interface); secondary links are unlimited. Rollups use the primary anchor to avoid double counting.

-   Hold blocks 1..n records; a record\'s blocked overlay is the union of its active holds.

-   Issue Event links revision → transmittal reference, purpose, recipients, approval record(s), decision(s), archive
    reference.

-   Every register row (decision, risk, approval record, interface) can own work items; those items appear in My Week
    like any other.

# 14 Permissions and roles

Role types unchanged from v0.2 §13.1 (Sponsor, PM, Engineering Manager, Package Lead, Discipline Lead, Engineer of
Record, Checker, Approver, Planner, Coordinator, Individual Contributor, Document Controller, Viewer, Administrator).
Principles, sharpened:

-   Anyone on the project may raise an intake item (configurable).

-   Coordinators triage, anchor, route, and disposition; they do not own accountable work by default (12 Rules, rule
    11).

-   Owners update their items; leads manage package items and propose plan changes; planners commit plans (P2).

-   Approvers record approval outcomes only within named-signatory scope (P1) or authority matrix scope (P3); delegation
    requires recorded basis, scope, and expiry (P3).

-   Preparing a decision or approval package requires no authority to decide it (v0.2 preserved).

-   Condition waivers: only roles configured per condition type, always recorded as Decisions (I-8).

-   Document Controllers manage revision metadata, issue events, and transmittal references; they cannot accept checks
    or record approvals.

-   Administrators configure taxonomy, templates, thresholds, routes, and the authority matrix; configuration changes
    are audit events.

# 15 Reporting and exports

| **Report**                                                                                                       | **Ph.** |
|----------------------------------------------------------------------------------------------------|--------------------|
| Sponsor brief (Overview snapshot: KPIs, package rollup, waiting-on items, top holds/risks)                       | P1      |
| Action & hold log; deliverables status; decision log; risk log; approval register; individual weekly commitments | P1      |
| Weekly package review pack; six-week lookahead; interface log                                                    | P2      |
| Issued deliverables summary; archive package; lessons learned summary; monthly reconciliation report             | P3      |

Formats: Excel/CSV for every register (round-trip per §16), PDF and print-friendly HTML for briefs and packs. Any
filtered register view exports exactly what is displayed.

# 16 Integrations and import contracts

MVP integration is import/export, not live sync (D-02, D-03). Every import validates against the schemas below, reports
rejects row-by-row, and never silently drops data. Exports use the same schemas so existing spreadsheets can round-trip
during adoption.

| **Import (P1)**          | **Required columns**                                                          | **Optional columns**                                                                                 |
|---------------------------|------------------------------------------------|----------------------------------------------|
| Master deliverables list | doc_no; title; package; discipline; owner; current_rev; state; due_date       | milestone; issue_purpose_plan; edms_ref; client_no; remarks                                          |
| Action / hold log (RAIL) | item_id; statement; type; log; owner; need_by; status; raised_by; raised_date | package; deliverable_ref (anchors on match, else flagged unanchored); hold_cause; closed_date; notes |
| Decision log             | decision_id; title; statement; authority; need_by; status                     | preparer; outcome; rationale; decided_date; affected_refs                                            |
| Risk log                 | risk_id; title; cause; consequence; owner; status                             | package; deliverable_ref; probability; impact; mitigation; need_by                                   |

P2 adds schedule-activity import (CSV or XER-derived: activity_id, description, start, finish, package/deliverable
mapping) feeding the lookahead, and EDMS revision/transmittal metadata import where available. Live EDMS and scheduling
integrations remain future scope.

# 17 Non-functional requirements

| **ID**      | **Requirement**                                                                                                                                                                           | **Ph.** |
|------------------|--------------------------------------------------------------------------------------------|-----------|
| PEC-NFR-001 | Append-only history on controlled records; approval, issue, waiver, and permission changes additionally write Audit Events with actor, timestamp, prior value, authority reference (I-7). | P1      |
| PEC-NFR-002 | No hard delete of controlled records; cancel/withdraw/supersede with reason (I-10).                                                                                                       | P1      |
| PEC-NFR-003 | Registers and role homes render ≤ 2 s at 10,000 open items / 250,000 history entries per project.                                                                                         | P1      |
| PEC-NFR-004 | Optimistic concurrency: conflicting saves warn and show the intervening change; no silent last-write-wins on controlled records.                                                          | P1      |
| PEC-NFR-005 | Role-based access enforced server-side; log visibility (Package / Internal / Client) enforced at the query layer.                                                                         | P1      |
| PEC-NFR-006 | SSO (SAML/OIDC) for firm identity.                                                                                                                                                        | P2      |
| PEC-NFR-007 | Multi-project data isolation from P1; portfolio views out of scope for MVP.                                                                                                               | P1      |
| PEC-NFR-008 | Deployable single-tenant / private-cloud for client-confidential projects.                                                                                                                | P2      |
| PEC-NFR-009 | Backup and restore, RPO ≤ 24 h, tested restore before pilot.                                                                                                                              | P1      |
| PEC-NFR-010 | All dates stored UTC with project timezone for display and threshold calculation; working-day thresholds respect the project calendar.                                                    | P1      |

# 18 Success metrics

## 18.1 Primary (pilot targets, measured at 8 weeks)

| **Metric**                                                                             | **Target**                 |
|----------------------------------------------------------------------------------------|----------------------------|
| Active deliverables represented in the system                                          | ≥ 90%                      |
| Open items anchored to a project object                                                | ≥ 95%                      |
| Median untriaged intake age                                                            | ≤ 2 working days           |
| Issued revisions with complete condition chain (checks, approval, decisions, evidence) | 100%                       |
| Issue transitions bypassing hard conditions without a recorded waiver Decision         | 0                          |
| Deliverables with status current within the weekly cadence                             | ≥ 85%                      |
| Overdue decisions older than 7 days                                                    | Downward trend from week 3 |
| Meeting time spent discovering status (survey, PM + leads)                             | −30% vs pre-pilot baseline |

## 18.2 Secondary (tracked, no hard target in MVP)

Hold age by cause; approval latency by type; check-comment aging by discipline; prevented invalid closures; reopened
items from superseded basis; % check/approval hours in plan (P2); plan reliability — committed items closed in week
(P2); % decisions reconciled within the monthly cycle (P3); lessons converted to template updates (P3).

# 19 Risks

| **Risk**                                                             | **Mitigation**                                                                                                                                        |
|----------------------------------------------|--------------------------------------------------------------------------|
| Seen as "another tracker."                                           | Role homes, deliverable anchoring, derived status, and generated packs are the visible difference; pilot messaging leads with the six questions (§3). |
| Data-entry burden reduces adoption.                                  | ≤ 8-field intake; coordinator triage absorbs classification; imports round-trip existing spreadsheets; templates and defaults everywhere.             |
| Weak document-control tie loses reality.                             | Revision and Issue Event are P1 entities even while EDMS integration is import-only.                                                                  |
| Shallow planning loses project controls\' trust.                     | P2 is a dedicated phase: lookahead, capacity, check/approval load, shift reasons — not a bolt-on.                                                   |
| Closure without conditions reproduces the old problem in a nicer UI. | Conditions engine (§9) is P1; hard blocks on issue transitions; waiver = Decision; prevented-closure metric.                                          |
| Approval terminology collapses in implementation.                    | OM-6 gives one write path; I-6 is a testable invariant; §7.5 is the state machine to build.                                                           |
| Derived status becomes a black box.                                  | I-4 + §8 defaults + drill-down on every value.                                                                                                        |
| The log becomes a dumping ground.                                    | Untriaged age is a project-health signal (§8.4); unanchored items are excluded from plans and rollups (I-2).                                          |

# 20 Decision log (formerly "open questions")

Each v0.2 open question restated as a decision with a default assumption. The build proceeds on the default unless the
decision authority rules otherwise by the decide-by point.

| **ID** | **Question**                                                 | **Default assumption**                                                                                                                        | **Decide by / authority**                 |
|-----------|-------------------------------|--------------------------------------------------|-----------------------------|
| D-01   | Model a Document layer between Deliverable and Revision?     | No for MVP; Revision hangs on Deliverable. Add Document grouping only if a pilot MDL requires multi-document deliverables.                    | Phase 0 exit / Product + Document Control |
| D-02   | Standalone database or layer over Excel?                     | Standalone system with round-trip Excel import/export (§16) as the adoption bridge.                                                           | Phase 0 / Product                         |
| D-03   | Which EDMS first?                                            | None in P1 — import/export only. Select per pilot client in P2.                                                                             | Phase 1 exit / Product + pilot DC         |
| D-04   | Which schedule system?                                       | CSV/XER-derived activity import in P2; no live sync.                                                                                          | Phase 2 / Project Controls                |
| D-05   | Client access to the Client log?                             | Export-only in MVP; no client portal.                                                                                                         | Phase 0 / PM + Sponsor                    |
| D-06   | Interface register in MVP?                                   | Interface Item record P1; dedicated register view P2.                                                                                         | Set (OM-7)                                |
| D-07   | Document lifecycle states?                                   | Default IFR → IFA → IFC with configurable labels and additional purposes per client standard; confirm on pilot.                               | Phase 0 / Document Control                |
| D-08   | How formal is e-signoff?                                     | In-system recorded action with full audit trail; no qualified e-signature in MVP.                                                             | Phase 0 / PM + QA                         |
| D-09   | Does waiving a condition always require a Decision?          | Yes, always (I-8).                                                                                                                            | Set                                       |
| D-10   | How are client comments modeled?                             | Review Comments on the revision with log = Client; convertible to work items / decisions at triage.                                           | Phase 1 / Coordinator + DC                |
| D-11   | Block vs warn ratio?                                         | Hard block: issue-affecting transitions and recording approval without authority. Everything else warns. Configurable per condition template. | Set; tune in pilot                        |
| D-12   | Approval routes: contractual vs project-standard?            | P1 uses named signatories per record; route templates captured in P3 from pilot observation.                                                  | Phase 2 exit / EM                         |
| D-13   | Is the existing authority matrix formal enough to configure? | Assume no; P1 named approvers, P3 matrix built from recorded pilot behavior.                                                                  | Phase 2 exit / EM + PM                    |
| D-14   | Minimum audit trail for approvals and issue?                 | Append-only history plus Audit Events per PEC-NFR-001.                                                                                        | Set                                       |

# 21 Release plan

Phases now bind exactly to requirement tags; a phase exits when its tagged requirements pass acceptance on the pilot
project.

**Phase 0 — Prototype validation (no build)**

Validate the six Rev C screens with a sponsor, PM, package lead, planner, coordinator, engineer of record, and document
controller on one representative FEED project. Exit criteria: terminology confirmed (package, deliverable, revision,
issue purpose, hold, log, check, approval, decision); the six role homes match observed weekly behavior; decisions D-01,
D-02, D-05, D-07, D-08 ruled or defaults confirmed.

**Phase 1 — Controlled tracker replacement (all P1 requirements)**

Overview, Packages, Deliverables, Action & Hold Log + intake, My Week (need-by + manual commit), all P1 registers,
conditions engine with hard blocks on issue transitions, typed holds, import/export contracts, notifications, NFRs.
Value: one shared record replaces fragmented spreadsheets — with closure discipline the spreadsheets never had.

**Phase 2 — Planning and capacity (all P2)**

Now / Next / Later, six-week lookahead, capacity with check/approval load, plan-shift workflow with reasons and lead
review, My Week generated from the weekly commit, digests, review packs, schedule import, supersession links, SSO.
Value: task management drives project controls.

**Phase 3 — Governance and memory (all P3)**

Approval routes and authority matrix, supersession impact propagation, archive views, lessons learned with template
feedback, reconciliation loop, EDMS metadata integration. Value: execution connects to governance and organizational
memory; the basis-drift response is complete.

# 22 Product thesis for sponsor presentation

*Project Execution Control is the controlled execution layer between engineering work, project controls, and project
governance. It does not replace engineers, EDMS, or scheduling tools. It connects the work people do each week to the
deliverables, packages, decisions, checks, approvals, risks, interfaces, and records that determine whether the project
is actually ready to move forward. Its purpose is to reduce coordination burden, expose holds early, preserve the basis
for action, and make project execution visible enough to govern.*

End of PRD v0.4 · Confidential concept draft · Basis: Rev C wireframes + PRD v0.2 + source theory documents
