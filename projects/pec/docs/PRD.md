# PEC — Project Execution Control

**Product Requirements Document — team information hub**

| Field | Value |
|---|---|
| Version | 1.0 |
| Date | 2026-07-09 |
| Status | Candidate for owner review; product direction is owner-provided, exact requirements not yet adopted |
| Product stage | Working demo exists; team product is not yet implemented |
| Intended supersession | PRD v0.4 product framing upon adoption |
| Conceptual basis | Chirality thesis and the owner clarifications recorded in this PRD |

This document proposes the product PEC is to become. It intentionally resets the
centre of gravity of PRD v0.4. The existing application remains useful prototype
evidence, but task management, planning, and report generation are supporting
capabilities rather than the product thesis.

The historical v0.4 requirement catalogue remains available in Git at commit
`7e8312172`. `SPEC.md` and `TRACEABILITY.md` describe that implemented prototype
baseline. They do not establish conformance to this candidate, and remain the
implementation basis unless and until v1.0 is adopted and rebaselined.

---

## 1. Product definition

PEC is a multi-user project information-control application for multidisciplinary
engineering teams. It gathers the same structured declaration from each discipline
on a regular cadence, reconciles those declarations with project records and source
documents, and maintains a sufficiently current, relevant, and detailed shared
project state that project leadership and downstream participants can rely upon it.

The application exists to reduce avoidable many-to-many coordination. Instead of
every discipline repeatedly contacting every other discipline to discover what
changed, what is at risk, what is needed, and what is about to be issued, each
discipline maintains its part of a common information contract. PEC makes the
resulting state visible, interrogable, and actionable across the project.

PEC's distinctive value is not that it can summarize uploaded files. A general
chatbot can do that. PEC adds value by preserving identity, coverage, provenance,
history, relationships, decision authority, verification results, and the closure
path from a decision to the documentation on which other people rely.

### 1.1 Product thesis

> PEC is the hub for critical project information flow. It helps project leadership
> maintain a shared project state that others can rely upon without requiring
> recurring N x N coordination events.

That thesis has four parts:

1. Each discipline makes a small, explicit, recurring declaration about change,
   risk, needs, deliverable events, and development state.
2. PEC reconciles those declarations into one current project state while
   preserving sources, gaps, conflicts, and honest absences.
3. Leadership uses that state to identify where decisions are required and what
   consequences follow from decisions already made.
4. Consequential change is triaged and assigned to the right relied-upon project
   documentation, such as a scope of work, design basis memorandum, master
   deliverables list, schedule basis, register, or controlled deliverable.

### 1.2 Chirality interpretation

PEC applies the Chirality thesis to project execution. Claims are not trustworthy
merely because a person, import routine, or language model stated them. The product
must expose the claim, its basis, its coverage, any conflict, and the human act that
authorizes a consequential change.

The gap between the recorded state and the state needed to proceed is where a
decision occurs. A decision is not complete merely because its outcome was entered.
Its consequences must be identified, assigned to the appropriate relied-upon
artifact, reflected there by an authorized owner, and made visible to affected
participants.

This PRD uses the thesis as a product-design basis, not as a claim that every thesis
document is binding project governance. See `../../../docs/thesis/README.md`,
`../../../docs/thesis/05_epistemic_architecture.md`, and
`../../../docs/thesis/bigger-picture/CHIRALITY_PRD_Amendment_Domain_Engine_Integration.md`.

---

## 2. Problem

Multidisciplinary projects generate more coordination paths than project leadership
can continuously service. Important changes often remain local to a discipline until
they cause rework, delay, scope disagreement, budget pressure, or an avoidable review
cycle. Meanwhile, status reports are assembled from inconsistent files and verbal
updates, and their polished prose can conceal stale coverage or unresolved
contradictions.

The recurring leadership problem is not a lack of data. It is the inability to know,
with reasonable confidence:

- whether every relevant discipline has reported for the same period;
- what materially changed and who else may be affected;
- where budget, scope, or schedule exposure is emerging;
- what information, resources, decisions, approvals, or clarifications are needed;
- what will be issued or checked soon;
- whether reported progress follows an agreed rule of credit;
- which statements conflict with other sources or prior state;
- what decisions are required; and
- whether the consequences of past decisions have reached the documents and people
  that depend upon them.

Current tools divide this problem across spreadsheets, email, meetings, document
systems, schedules, action logs, and individual memory. A report summarizes some of
those surfaces but does not maintain their relationships or prove that the state is
complete and current.

---

## 3. Product outcomes

PEC shall produce the following outcomes for a project team:

1. **A current shared state.** Team members can determine the latest attested state
   for each active discipline, package, and deliverable, including the reporting
   period and source basis.
2. **Exception-focused coordination.** Routine no-change declarations remain cheap;
   material changes, risks, needs, conflicts, decisions, and unreflected consequences
   become prominent.
3. **Leadership decision support.** Leadership sees decision gaps with enough context
   to assign authority, obtain missing information, and record a decision without
   treating an AI summary as the decision.
4. **Consequence placement.** Decisions and material changes are connected to the
   specific relied-upon artifacts that must change, their owners, and the affected
   consumers.
5. **Verification and validation.** The system checks completeness, consistency,
   identity, rules of credit, source alignment, and change closure without silently
   rewriting attested facts.
6. **Reliable projections.** Dashboards, discipline views, package views, registers,
   and reports are projections of the same governed state and drill to their basis.
7. **Reduced coordination load.** The shared state replaces status-discovery meetings
   and repeated bilateral queries while escalating the human conversations that
   actually require judgment.

---

## 4. Product boundary

### 4.1 PEC is

- a recurring discipline-declaration system;
- a maintained project-state database with provenance and history;
- a reconciliation and verification surface;
- a leadership information and decision-support surface;
- a change-consequence routing surface tied to relied-upon documentation;
- a generator of role-appropriate, drillable views and editable draft reports; and
- a platform on which later project-execution workflows can be built.

### 4.2 PEC is not

- a chatbot wrapper whose only durable output is a summary;
- a generic task manager, Kanban board, or personal to-do list;
- the engineering document management system or authoring environment;
- the authoritative schedule, cost ledger, or estimating system;
- an autonomous decision maker, checker, approver, or issuer;
- a replacement for engineering conversation when judgment or negotiation is needed;
- a system that invents missing facts, progress, issue classifications, or document
  impacts; or
- a demand that every informal conversation be captured.

Task, notification, and scheduling features may support an information obligation,
but they are not the core object or value proposition. Closing a task does not, by
itself, close a decision consequence or prove that a relied-upon artifact was updated.

---

## 5. Core information contract

### 5.1 Weekly discipline declaration

For each reporting period, PEC asks every active discipline the same five questions:

1. **Change and cross-discipline impact.** Has anything changed that would affect
   another discipline?
2. **Budget, scope, or schedule risk.** Is there a change or a risk of change to the
   budget, scope, or schedule?
3. **Needs.** Is any information, resource, decision, approval, or clarification
   needed?
4. **Deliverable events.** Has the discipline issued, or will it soon issue, an
   internal or external deliverable or request a squad check?
5. **Development state and progress.** What is the current development state of the
   discipline's deliverables, and what is their percent complete under the applicable
   rules of credit?

The declaration is the product's minimum recurring information contract. It is not a
free-form status essay. Each question supports either an explicit `none` response or
one or more structured observations with optional explanatory prose and evidence.

### 5.2 Declaration header

Every declaration shall identify:

- project;
- discipline;
- reporting period;
- covered packages and deliverables, or an explicit statement that the declaration
  covers the discipline's full active scope;
- declaring person and accountable discipline lead;
- submission and attestation timestamps;
- source files or records used, when applicable; and
- whether it is an original, amendment, or superseding declaration.

PEC shall never infer the reporting period or scope coverage from a filename alone.

### 5.3 Minimum observation fields

| Declaration area | Minimum structured content |
|---|---|
| Change / impact | Statement; affected scope; known or potentially affected disciplines; effective date or horizon; source/evidence |
| Budget / scope / schedule risk | Dimension(s); cause; potential consequence; affected scope; owner if known; need-by or decision horizon |
| Need | Need type; statement; requested party or authority if known; need-by; affected/blocked scope; internal/client/unclassified audience |
| Deliverable event | Deliverable and revision; event type; internal/external/squad check; actual or forecast date; source/evidence |
| Development state | Deliverable; controlled state; as-of date; source/evidence |
| Percent complete | Deliverable; percent; applicable rule-of-credit version; earned milestones/credits; as-of date; attesting person |

The product may make additional fields configurable, but shall not make declaration
completion onerous. Existing MDL, RAIL, document-control, schedule, and other source
files may supply the fields through a reviewable import proposal.

### 5.4 No-change declarations

An explicit no-change response is meaningful project information. PEC shall retain
who made it, the covered scope, and the period. Blank, missing, late, and explicit
`none` responses are distinct states and shall never be collapsed.

### 5.5 Attestation and amendment

The discipline lead or a delegated person attests that a declaration accurately
represents the stated scope and period to the best of their knowledge. Attestation is
not independent verification, approval, or professional sign-off.

After attestation, correction occurs by amendment or supersession. The original
declaration remains in history, and every downstream snapshot or report identifies
which version it used.

---

## 6. Operating model

PEC specifies a small information lifecycle rather than a prescriptive meeting
workflow:

1. **Collect.** A person enters a declaration directly or submits source documents.
2. **Review.** Mapped data remains a proposal until a human reviews and applies it;
   direct declarations remain draft until attested.
3. **Reconcile.** PEC compares the new observations with project identity,
   prior state, other current sources, and configured rules.
4. **Publish state.** Accepted observations form a period-bounded, immutable project
   state snapshot and update the live current-state projection.
5. **Triage exceptions.** Leadership and coordinators examine material changes,
   needs, conflicts, decision gaps, and stale or incomplete coverage.
6. **Record decisions and consequences.** Authorized humans record decisions and
   identify what project state, obligations, and relied-upon artifacts they change.
7. **Place change.** Consequences are assigned to the owners of the documents or
   systems that others rely upon.
8. **Verify propagation.** PEC records evidence that the change was reflected and
   identifies affected participants who still need the updated basis.
9. **Project.** Role views and reports summarize the same state without becoming a
   second source of truth.

Teams may perform these acts continuously, in a weekly review, or through existing
project-control meetings. PEC shall not require a new ceremony when the information
contract can be satisfied within the team's current cadence.

---

## 7. Product invariants

| ID | Invariant |
|---|---|
| PEC-I-01 | **Factual or absent.** Unsupported facts are shown as absent, unknown, stale, or conflicting; they are not inferred for presentation quality. |
| PEC-I-02 | **One state, many views.** Dashboards, registers, reports, exports, and agent responses project the same accepted records and snapshot basis. |
| PEC-I-03 | **Coverage is explicit.** Every periodic claim names its period and scope. Missing, late, partial, and no-change declarations remain distinguishable. |
| PEC-I-04 | **Source and authority are visible.** Every material claim drills to its declaration, imported row, source reference, decision, or configured derivation rule. |
| PEC-I-05 | **Attestation, verification, decision, approval, and issuance are distinct acts.** No status or label may merge them. |
| PEC-I-06 | **Decisions remain human.** An agent may identify a gap, assemble context, and draft a proposal; only the authorized person records the decision outcome. |
| PEC-I-07 | **A decision carries consequences.** A material decision identifies affected scope and either creates change obligations against relied-upon artifacts or records why no artifact change is required. |
| PEC-I-08 | **Consequence closure requires placement.** A task completion or notification is insufficient; closure requires evidence that the assigned authoritative artifact or system reflects the decision, or an authorized supersession/cancellation. |
| PEC-I-09 | **Authority is defined by data class.** PEC shall not silently replace the authority of a source workbook, controlled document, EDMS, schedule, cost system, or external decision register. |
| PEC-I-10 | **Rules of credit are versioned.** Percent complete is attested or calculated only against an identifiable rule set; an LLM never guesses it. |
| PEC-I-11 | **Accepted history is immutable.** Corrections supersede; they do not erase the prior declaration, decision, source basis, or snapshot. |
| PEC-I-12 | **Verification does not rewrite truth.** Automated checks create findings; a human disposition or accepted source change resolves them. |
| PEC-I-13 | **Agent work is bounded and observable.** Model, access basis, reads, proposals, refusals, and human gates are visible during and after a turn. |
| PEC-I-14 | **Shared state reduces, not suppresses, communication.** PEC escalates exceptions and judgment; it does not treat lack of a recorded issue as proof that no conversation is needed. |

---

## 8. Users and responsibilities

| Role | Primary responsibility in PEC |
|---|---|
| Discipline contributor | Supplies observations and evidence for assigned scope; responds to clarification requests |
| Discipline lead | Owns declaration coverage and attestation; confirms development state and rules-of-credit basis |
| Package lead | Reviews package-level impacts, needs, interfaces, and consequences across contributing disciplines |
| Project coordinator / information manager | Monitors coverage and freshness; routes exceptions; maintains identity and source alignment; does not make technical decisions by default |
| Project leadership | Prioritizes exceptions, identifies decision authority, records or obtains decisions, and assigns consequential change |
| Decision authority | Makes and records the authorized decision with rationale, affected scope, and consequences |
| Artifact owner | Reflects an assigned consequence in the applicable SOW, DBM, MDL, schedule basis, register, controlled deliverable, or other relied-upon artifact |
| Document controller | Maintains revision/issue references and verifies that controlled-document events are represented accurately |
| Project controls | Supplies or verifies schedule, cost, progress, and rules-of-credit bases where those systems remain authoritative |
| Sponsor / client viewer | Reads a restricted, role-appropriate state and follows permitted drill paths; cannot mutate project state |
| Project administrator | Configures membership, roles, disciplines, calendars, vocabularies, rules, integrations, and retention controls |
| Agent | Reads only authorized surfaces; maps inputs, finds gaps/conflicts, drafts summaries and proposals; never attests, decides, approves, applies, or issues |

A person may hold several roles. Permissions are evaluated against the project and the
specific act, not merely the screen being displayed.

---

## 9. Information model

### 9.1 Core entities

| Entity | Purpose |
|---|---|
| Project / team / discipline | Membership, responsibility, configuration, and scope |
| Package | Coordination boundary and package-level impact/need context |
| Deliverable / revision | Development-state, progress, check, and issue context |
| Reporting period | Declared time boundary and deadline for a recurring information cycle |
| Discipline declaration | Attested response for one discipline, period, and coverage scope |
| Observation | A structured change, risk, need, deliverable event, state, or progress claim within a declaration |
| Source document | Uploaded or linked file plus hash, metadata, declared coverage, and authority classification |
| Import proposal | Reviewable mapping from source content to proposed PEC changes |
| Decision gap | A recorded gap whose resolution requires an authorized judgment rather than more deterministic processing |
| Decision | Human judgment, authority, rationale, outcome, affected scope, and effective date |
| Consequence | A material result of a decision or accepted change for project scope, basis, deliverables, interfaces, schedule, cost, or obligations |
| Change obligation | Assignment to reflect a consequence in a named relied-upon artifact or authoritative external system |
| Artifact reference | Identity, owner, authority, location, revision, and state of a relied-upon document or external record |
| Validation finding | Deterministic or human finding about completeness, consistency, identity, currency, or closure |
| Project-state snapshot | Immutable period-bounded manifest of accepted records, sources, findings, gaps, and supersession pointers |
| History / audit event | Actor, act, time, before/after state, reason, and authority reference |

### 9.2 Consequence and change-obligation states

PEC shall distinguish at least the following facts:

- a consequence has been identified;
- the affected project scope is known or still incomplete;
- an artifact change is required, not required, or not yet determined;
- the target artifact and owner are assigned or missing;
- the artifact owner has acknowledged the obligation;
- a proposed artifact revision/reference exists;
- the change has been reflected in the authoritative artifact;
- the reflection has been verified against the decision; and
- affected consumers have been notified or have acknowledged the new basis where
  project policy requires it.

These may be implemented as a state machine or derived states, but the facts shall not
be collapsed into a single generic `done` flag.

### 9.3 Authority by data class

| Data class | Authority |
|---|---|
| A discipline's periodic declaration | The attested PEC declaration and its cited sources |
| Imported workbook facts | The accepted import proposal bound to the hashed source and declared coverage |
| Controlled document content/revision | The configured EDMS, repository, or controlled file; PEC stores a reference and verification evidence |
| Schedule or cost values | The configured schedule/cost system or an explicitly attested imported snapshot |
| Decision outcome | The authorized decision record in PEC or a linked authoritative external decision register |
| Live cross-project projection | PEC's database, derived from accepted records and explicit authority mappings |
| Period close | The immutable PEC project-state snapshot and its source manifest |
| Report, dashboard, export, or agent response | A derivative projection; never a substitute for the underlying accepted state |
| Agent-created content | Proposal or draft until the designated human act occurs |

The relational database supports concurrent team use and live queries. Source hashes,
immutable snapshots, audit exports, and backup/restore evidence shall make accepted
state independently inspectable and recoverable. Database mutability must not make
the project's basis opaque.

---

## 10. Functional requirements

### 10.1 Team and project setup

| ID | Requirement |
|---|---|
| PEC-TEAM-001 | Administrators can create projects, disciplines, teams, packages, deliverables, artifact types, reporting cadences, and project vocabularies without code changes. |
| PEC-TEAM-002 | Users can belong to multiple projects and hold multiple project roles; every query and mutation is project-scoped. |
| PEC-TEAM-003 | The product supports invite, deactivate, substitute/delegate, and temporary coverage without rewriting historical actor identity. |
| PEC-TEAM-004 | Project setup identifies active disciplines, accountable leads, expected declaration scope, declaration due date, and escalation path. |
| PEC-TEAM-005 | A responsibility view shows declaration ownership, decision authority, artifact ownership, and unassigned obligations. |

### 10.2 Declaration capture

| ID | Requirement |
|---|---|
| PEC-DECL-001 | PEC provides a concise form for the five-question weekly discipline declaration in §5.1. |
| PEC-DECL-002 | Each question supports explicit `none`, structured entries, explanatory text, links, and attachments. |
| PEC-DECL-003 | Users can save drafts, request input from other contributors, preview the covered scope, and submit for lead attestation. |
| PEC-DECL-004 | The discipline lead can attest, return for clarification, amend, or supersede a declaration; each act writes history. |
| PEC-DECL-005 | PEC distinguishes not started, draft, submitted, returned, attested, amended, late, partial, and superseded declarations. |
| PEC-DECL-006 | A discipline may declare once for its full scope or combine contributor submissions, without double-counting overlapping packages or deliverables. |
| PEC-DECL-007 | Current declarations and prior periods are viewable side by side with added, changed, removed, and unchanged observations. |
| PEC-DECL-008 | Reminders and escalation are configurable by role, deadline, and project calendar and never imply attestation. |

### 10.3 Source ingestion and proposals

| ID | Requirement |
|---|---|
| PEC-ING-001 | Users can attach XLSX, CSV/TSV, DOCX, PDF, and configured machine-readable exports where authorized. |
| PEC-ING-002 | Every source receives a hash, uploader, upload time, declared reporting coverage, scope, source type, and authority classification. |
| PEC-ING-003 | Mapping produces a reviewable proposal showing creates, updates, unchanged rows, conflicts, rejects, unsupported fields, and omitted content. |
| PEC-ING-004 | No importer or agent may silently drop a populated field or invent an identity, date, status, discipline, issue type, percent complete, or audience. |
| PEC-ING-005 | Acceptance and apply are distinct authorized human acts; accepted proposals are hash-bound and stale if the source or target state changes. |
| PEC-ING-006 | Re-import is idempotent, correction-aware, and capable of preserving source-specific observations without erasing other accepted sources. |
| PEC-ING-007 | Round-trip exports preserve source identifiers and every supported imported field. |

### 10.4 Reconciliation, verification, and validation

| ID | Requirement |
|---|---|
| PEC-VV-001 | PEC checks declaration completeness and overlap against the configured active-discipline and scope expectations for the period. |
| PEC-VV-002 | PEC checks referential integrity among disciplines, packages, deliverables, issues, decisions, events, and artifacts. |
| PEC-VV-003 | PEC compares current declarations with prior accepted state and flags unexplained regressions, discontinuities, additions, removals, and stale observations. |
| PEC-VV-004 | PEC can run configurable cross-source rules, including state/issue consistency, duplicated identity, issuance/date alignment, and decision/artifact closure. |
| PEC-VV-005 | Percent-complete checks identify the rule-of-credit version, earned components, manual attestation, and any arithmetic or state inconsistency. |
| PEC-VV-006 | Every finding states the rule, records examined, result, severity, and what human disposition or source correction would resolve it. |
| PEC-VV-007 | Findings can be acknowledged, assigned for clarification, accepted with rationale, corrected by a superseding source, or escalated to a decision gap. |
| PEC-VV-008 | Validation status shall not be presented as engineering correctness, professional approval, or proof that all relevant facts were supplied. |

### 10.5 Leadership current-state view

| ID | Requirement |
|---|---|
| PEC-LEAD-001 | The leadership home shows declaration coverage, freshness, amendments, and explicit no-change responses for the active period. |
| PEC-LEAD-002 | It foregrounds new material changes, cross-discipline impacts, budget/scope/schedule risks, needs, upcoming/actual deliverable events, and development progress. |
| PEC-LEAD-003 | It separately shows conflicts, validation findings, decision gaps, unassigned consequences, and overdue artifact change obligations. |
| PEC-LEAD-004 | Every count, status, and summary drills to contributing records, source, period, and derivation rule. |
| PEC-LEAD-005 | Users can filter, sort, search, group, resize columns, export the displayed rows, and retain shareable role-safe views. |
| PEC-LEAD-006 | Sponsor/client views are strictly read-only and expose only configured information classes and drill paths. |
| PEC-LEAD-007 | Package, discipline, and deliverable views project the same current state using the terminology appropriate to each scope. |

### 10.6 Planning: decision consequences and change placement

The Planning surface is not primarily a task board, capacity planner, or schedule.
Its foreground is the flow from material project information to decisions and from
decisions to the documentation on which others rely.

| ID | Requirement |
|---|---|
| PEC-PLAN-001 | Planning shows unresolved material changes and decision gaps with their affected scope, basis, missing information, need-by, and identified authority. |
| PEC-PLAN-002 | An authorized user can record a decision outcome, rationale, effective date, affected scope, and explicit consequences. |
| PEC-PLAN-003 | Each consequence is classified as requiring an artifact/system change, requiring communication only, having no downstream change, or still needing impact determination. |
| PEC-PLAN-004 | A required change is assigned to a named target artifact/system, owner, required-by date, affected consumers, and verification method. |
| PEC-PLAN-005 | PEC exposes consequences with no target, no owner, conflicting targets, unacknowledged ownership, or overdue reflection. |
| PEC-PLAN-006 | Artifact owners can acknowledge, cite a proposed/current revision, record reflection evidence, and request verification without altering the original decision. |
| PEC-PLAN-007 | Verification compares the reflected change with the decision consequence and records satisfied, partial, conflicting, superseded, or rejected results. |
| PEC-PLAN-008 | Optional actions, reminders, or schedule activities may be linked to a change obligation, but cannot substitute for its artifact-reflection evidence. |
| PEC-PLAN-009 | Affected disciplines and packages can acknowledge receipt of a changed basis where project policy requires it. |

### 10.7 Relied-upon artifacts

| ID | Requirement |
|---|---|
| PEC-ART-001 | Teams can register artifact types and instances, including SOW, DBM, MDL, schedule/cost basis, execution plan, design criteria, interface register, controlled deliverable, and client direction. |
| PEC-ART-002 | Each artifact reference records authority, location, owner, current revision/as-of date, status, and access classification. |
| PEC-ART-003 | PEC can link project claims, risks, needs, decisions, consequences, deliverables, packages, and validation findings to the artifact sections or records they depend upon. |
| PEC-ART-004 | Supersession preserves the prior artifact reference, replacement, effective date, affected dependencies, and unresolved propagation obligations. |
| PEC-ART-005 | PEC shall link to or exchange metadata with the authoritative document system rather than silently treating an uploaded convenience copy as the current controlled document. |

### 10.8 Collaboration and notifications

| ID | Requirement |
|---|---|
| PEC-COL-001 | Users can request clarification on a specific declaration entry, finding, decision gap, consequence, or change obligation without creating a parallel private record. |
| PEC-COL-002 | Mentions, assignments, acknowledgements, and comments retain record context and appear in a role-appropriate inbox. |
| PEC-COL-003 | Notifications state what changed, why the recipient is involved, the requested act, the due date, and the authoritative record link. |
| PEC-COL-004 | Digest and event notifications are configurable; urgent judgment requests remain distinguishable from routine status reminders. |
| PEC-COL-005 | Team members can see who is editing or has changed a controlled record; conflicting saves never silently overwrite one another. |

### 10.9 Reports and projections

| ID | Requirement |
|---|---|
| PEC-REP-001 | PEC generates a concise weekly project-status draft from a selected immutable period snapshot, following a configurable organization template. |
| PEC-REP-002 | The report summarizes rather than dumps rows and covers discipline activities/progress, package needs/issues, decisions, interfaces, and period deliverable events as supported by the selected state. |
| PEC-REP-003 | Every reported figure and material statement has a drillable or machine-auditable basis; unsupported sections state an honest absence. |
| PEC-REP-004 | Draft reports are available as editable DOCX and browser preview; issue/approval remains an external or separately authorized human act. |
| PEC-REP-005 | A regenerated report from the same snapshot and template version is materially reproducible. |
| PEC-REP-006 | Reports record project, period, snapshot, source coverage, template version, generation time, and draft/issued status without implying issue. |
| PEC-REP-007 | User-defined reports and agent answers are limited to authorized project state and preserve the same provenance and absence rules. |

### 10.10 Agent assistance

| ID | Requirement |
|---|---|
| PEC-AGENT-001 | The agent can explain the project, locate records, compare periods, summarize current state, identify gaps/conflicts, and draft import/report/change proposals within the user's access. |
| PEC-AGENT-002 | The agent can perform bounded multi-step reads and show the resolved model, turn state, tool activity, access basis, budget, refusals, and final response live. |
| PEC-AGENT-003 | Agent output distinguishes quoted/attested facts, deterministic derivations, model inferences, proposals, and absences. |
| PEC-AGENT-004 | The agent cannot attest declarations, accept/apply imports, record decisions, approve, verify professionally, issue documents, change access, or close consequences. |
| PEC-AGENT-005 | Every proposed mutation previews the affected records and requires the configured human authority act. |

### 10.11 Administration and audit

| ID | Requirement |
|---|---|
| PEC-ADM-001 | Administrators manage project roles, visibility classes, cadence, vocabularies, rules of credit, validation rules, artifact types, templates, and integrations. |
| PEC-ADM-002 | Configuration changes are versioned, effective-dated, auditable, and never retroactively change a historical snapshot. |
| PEC-ADM-003 | Audit views and exports show actor, act, time, prior/new state, source, authority, and related snapshot without exposing content outside the viewer's permissions. |
| PEC-ADM-004 | Backup, restore, retention, archive, and legal/project-closeout exports are operable and tested. |

---

## 11. User experience requirements

### 11.1 Navigation model

The primary navigation should reflect the information flow:

| Surface | Governing question |
|---|---|
| Current state | What is current, what changed, and how complete is the reporting basis? |
| Disciplines | What has each discipline declared, and what does its evidence show? |
| Packages | What package-level impacts, needs, issues, decisions, interfaces, and changes exist? |
| Deliverables | What is each deliverable's development state, progress basis, and upcoming/actual event? |
| Planning | What requires a decision, and where must the consequences be reflected? |
| Verification | What is missing, conflicting, stale, inconsistent, or not yet propagated? |
| Reports | What derivative view is needed from a selected state snapshot? |
| Admin | How is the information contract, authority, access, and integration basis configured? |

Personal assignment and notification views may exist, but they are entry points into
shared records rather than a separate private work system.

### 11.2 Interaction principles

- **Exception first.** Show material changes, decision gaps, conflicts, and overdue
  propagation before stable detail.
- **Low declaration burden.** Reuse existing sources, defaults, and prior scope; make
  an honest no-change declaration fast.
- **Progressive disclosure.** Leadership summaries stay concise; users can drill to
  discipline, package, deliverable, observation, source row, and history.
- **Basis before polish.** Unknown or partial information remains visibly so.
- **Role-safe by construction.** Hiding a navigation item is not a substitute for
  server-side authorization and filtered drill payloads.
- **Direct data control.** Every register supports search, filtering, sorting,
  resizable columns, local horizontal scrolling, and displayed-view export.
- **Stable identity.** Human-readable references and source IDs remain visible across
  imports, links, reports, and exports.
- **Accessible and responsive.** All critical acts are keyboard operable and usable
  at desktop and narrow viewports without page-level overflow.

---

## 12. Permissions and human authority

1. Authorization is enforced server-side for every read and act.
2. Project isolation applies to records, history, reports, agent tools, search, and
   exports.
3. Visibility is configurable for internal, client, confidential, and other project
   classifications.
4. Only a named or role-authorized person may attest a declaration, accept/apply an
   import, record a decision outcome, approve, accept verification, change access, or
   issue a controlled output.
5. Delegation records delegator, delegate, scope, effective dates, and authority
   basis; it does not rewrite historical identity.
6. Agent service identities are non-administrative and cannot acquire a user's human
   authority through prompting.
7. Sponsor/client users are read-only unless the project deliberately establishes a
   separate external-contribution workflow.

---

## 13. Integrations

### 13.1 Required integration classes

- firm identity and SSO;
- XLSX/CSV and document upload;
- MDL and action/issue register exchange;
- controlled-document/EDMS metadata and links;
- schedule and cost/progress snapshot import where those systems are authoritative;
- notifications through email or an enterprise collaboration system; and
- complete project-state, history, and audit export for archive or migration.

The product shall use adapter contracts so a project can choose SharePoint, an EDMS,
a scheduling system, or another controlled repository without changing the core
information model.

### 13.2 Integration rules

- Every integration declares which data classes it reads, proposes, or writes.
- Live synchronization is not required for the first team release; reliable,
  reviewable snapshots are acceptable.
- External writes require a separately authorized operation and shall never be a
  hidden side effect of report generation or agent conversation.
- Source-system identifiers and revision/as-of metadata are retained.
- Integration failure leaves the last accepted state visible with a stale warning;
  it never presents cached data as current without qualification.

---

## 14. Non-functional requirements

| ID | Requirement |
|---|---|
| PEC-NFR-001 | Append-only history and tamper-evident audit evidence for accepted declarations, imports, decisions, consequences, artifact references, permissions, configuration, and snapshots. |
| PEC-NFR-002 | No hard delete of controlled records; cancel, retract, amend, or supersede with reason and authority. |
| PEC-NFR-003 | Common views render within 2 seconds at the provisional team target of 100 named users, 25 concurrent users, 25,000 deliverables, and 1,000,000 history entries per project. |
| PEC-NFR-004 | Optimistic concurrency and transactional writes prevent silent last-write-wins or partially applied proposals. |
| PEC-NFR-005 | Role-based and record-class access is enforced at the query and mutation layers, including agent and export paths. |
| PEC-NFR-006 | SAML or OIDC SSO, configurable session controls, MFA inheritance, and centralized user deactivation are required for production team use. |
| PEC-NFR-007 | Multi-project isolation is verified by automated cross-project access tests. |
| PEC-NFR-008 | The application is deployable single-tenant or in a private cloud suitable for client-confidential engineering projects. |
| PEC-NFR-009 | Encrypted backup/restore provides an RPO no greater than 24 hours and an RTO no greater than 4 hours; restore is rehearsed before production use and quarterly thereafter. |
| PEC-NFR-010 | UTC storage, project-local display, reporting calendars, and working-day calculations are consistent across UI, reports, reminders, and APIs. |
| PEC-NFR-011 | All state-changing APIs are idempotent where retried, validate complete payloads, and return stable conflict/error taxonomies. |
| PEC-NFR-012 | Availability target is 99.5% during configured project working hours for the first production release. |
| PEC-NFR-013 | WCAG 2.2 AA is the accessibility target; critical workflows require keyboard and screen-reader verification. |
| PEC-NFR-014 | Logs and telemetry expose import, reconciliation, report, notification, and agent failures without recording unauthorized project content or secrets. |
| PEC-NFR-015 | Data retention, residency, encryption in transit/at rest, and deletion policies are configurable to firm and client requirements. |
| PEC-NFR-016 | The system can export a complete, documented, non-proprietary project package sufficient to reconstruct accepted records, relationships, snapshots, and history. |
| PEC-NFR-017 | Model providers, model IDs, access basis, and data sent to a model are configurable and observable; no unapproved training or retention assumption is made. |

The sizing and service-level values above are provisional release targets and shall be
confirmed with the sponsor before architecture commitments that materially depend on
them.

---

## 15. Success metrics

Pilot baselines shall be measured before rollout. The first eight-week team pilot
targets are:

| Outcome metric | Target |
|---|---|
| Active disciplines with an attested declaration or explicit no-change declaration by the reporting deadline | at least 95% |
| Attested declarations with explicit period and coverage | 100% |
| Material cross-discipline impacts with a triage disposition and accountable owner | at least 95% within 2 working days |
| Decision outcomes with explicit affected scope and consequences | 100% |
| Consequences requiring authoritative change that have a named target artifact and owner | at least 95% within 2 working days of decision |
| Change obligations closed without artifact-reflection evidence or an authorized no-change/supersession basis | 0 |
| Reported percent-complete values with an identifiable rule-of-credit basis | 100% |
| Generated weekly reports whose figures reconcile to the selected snapshot | 100% |
| Time spent assembling the recurring status report | at least 75% below pilot baseline |
| Meeting time spent discovering status rather than resolving exceptions | at least 30% below pilot baseline |
| Material validation findings resolved before the affected artifact is issued | upward trend from week 2; establish numeric target from pilot baseline |
| Team members who agree that PEC state is current enough to rely upon for their role | at least 80% |

Usage volume alone is not a success metric. More tasks, comments, notifications, or
agent turns do not demonstrate better project control.

---

## 16. Release strategy

### Phase 0 — information-contract validation

Observe one real weekly cycle with project leadership, discipline leads, project
controls, and document control. Confirm the five-question declaration, active-scope
rules, rules of credit, decision authorities, relied-upon artifact classes, visibility
classes, and current coordination baseline.

**Exit:** the team can answer what must be declared, by whom, for what scope, against
which sources, and which artifacts must receive consequential change.

### Phase 1 — team current-state foundation

Deliver team identity/roles, project setup, direct declarations, source proposals,
attestation, completeness/currentness, discipline/package/deliverable views,
leadership current-state view, report snapshots, concise DOCX generation, audit,
notifications, and production backup/security fundamentals.

**Value:** one weekly information contract and one dependable state replace manual
status assembly.

### Phase 2 — decisions and consequence placement

Deliver decision gaps, authorized decisions, affected-scope capture, consequence
classification, artifact registry, change obligations, owner acknowledgement,
reflection evidence, propagation verification, and the reoriented Planning page.

**Value:** critical information leads to decisions, and decisions reliably reach the
documents and people that depend upon them.

### Phase 3 — longitudinal verification and validation

Deliver period comparison, configurable cross-source rules, rules-of-credit engines,
staleness and regression detection, conflict disposition, supersession impact, and
project-state archive/export.

**Value:** PEC detects basis drift and incomplete propagation before they become
downstream rework.

### Phase 4 — integrations and spin-off workflows

Add selected EDMS, schedule, cost, collaboration, portfolio, assurance, interface,
review, and task-support workflows only where the shared information spine provides a
clear basis and avoids duplicate authority.

**Value:** PEC becomes a broader execution-control platform without losing the
information contract that justifies the application.

---

## 17. Acceptance scenarios

The target product is acceptable for team use when the following scenarios pass:

1. **Complete weekly cycle.** Every configured discipline either attests entries or
   explicitly declares no change for a common period; leadership sees complete and
   incomplete coverage without manual reconciliation.
2. **Source-assisted declaration.** A discipline attaches current MDL and issue files;
   the agent proposes a lossless mapping; a human reviews/applies it; the discipline
   attests the resulting declaration; all views and the report agree.
3. **Cross-discipline change.** A discipline declares a change affecting two other
   disciplines. Those impacts appear in leadership and recipient views with source
   basis, and the recipients can acknowledge or raise a conflict.
4. **Decision and documentation consequence.** Leadership records a decision that
   changes scope. PEC captures the consequences, assigns the SOW and DBM changes to
   their owners, retains revision evidence, and refuses to call the consequence
   closed merely because an action item was completed.
5. **Conflict caught.** A deliverable is declared on hold while the current issue
   source contains no corresponding need/issue. PEC raises a finding, preserves both
   source claims, and records the human disposition or corrected source.
6. **Rules-of-credit progress.** Percent complete traces to the applicable rule set
   and earned components; an unexplained regression or invalid credit combination is
   visible before report generation.
7. **Read-only sponsor.** A sponsor sees only permitted current-state and drill
   surfaces and cannot reach a mutating endpoint through URL, API, export, or agent.
8. **Concurrent team use.** Two users changing the same controlled record receive an
   explicit conflict and no accepted state is silently lost.
9. **Auditable report.** A concise editable report is generated from a named snapshot;
   every figure reconciles to the UI and missing data is stated honestly.
10. **Recoverability.** The production-like database is restored from backup, and its
    accepted records, history, source manifests, and snapshots pass integrity checks.

---

## 18. Risks and safeguards

| Risk | Safeguard |
|---|---|
| PEC becomes a more elaborate weekly report generator | Measure maintained-state, decision, propagation, and verification outcomes; keep reports derivative |
| Declaration burden causes non-adoption | Five stable questions, explicit none, source reuse, prior-scope defaults, short direct form, role-specific reminders |
| Task-management gravity returns | Keep tasks optional and subordinate to information gaps, decisions, and artifact change obligations |
| Leadership treats a polished summary as verified truth | Show coverage, currency, sources, conflicts, and snapshot basis; separate attestation from verification |
| Database becomes an opaque competing authority | Define authority by data class; preserve source hashes, immutable snapshots, exports, and artifact references |
| Decisions are recorded but not propagated | Require consequence classification and artifact placement; measure unassigned and unverified obligations |
| Artificially complete AI output conceals gaps | Factual-or-absent rule, bounded agent authority, observable acts, proposals, and explicit refusals |
| Too much workflow is designed before observing the team | Phase 0 validates the information contract and authority map; later workflow remains configurable |
| Notifications recreate N x N noise | Exception-focused routing, digests, explicit recipient basis, and configurable escalation |
| Integrations duplicate or overwrite authoritative systems | Adapter authority declarations, proposal gates, idempotency, and no hidden external writes |

---

## 19. Current prototype disposition

The demo already proves several useful components:

- multi-project membership and role-tailored navigation;
- populated and blank workflow-demo projects;
- XLSX upload, proposal, human accept/apply, and source-fidelity controls;
- discipline, package, deliverable, action/hold, and report projections;
- multi-discipline package relationships;
- direct table filtering, sorting, resizing, exporting, and drill paths;
- concise draft DOCX generation; and
- a live, observable, bounded LLM sidecar.

Those components should be retained where they satisfy this PRD. The current Plan,
My Week, generic work-item, capacity, condition, and lifecycle machinery should be
evaluated as supporting infrastructure, not assumed to define the future product.

Before further feature implementation, `SPEC.md`, `TRACEABILITY.md`, `STATUS.md`, the
information model, and the delivery plan shall be rebaselined against this PRD. That
rebaseline must identify what is retained, repurposed, retired, or newly required;
the existence of prototype code is not, by itself, a reason to preserve a product
concept.

---

## 20. Product decisions still requiring confirmation

These questions materially affect implementation and should be answered through
pilot observation or explicit owner/sponsor direction rather than guessed:

1. Which artifacts are relied upon for the first team pilot, and which systems are
   authoritative for each?
2. Who may attest on behalf of a discipline, and what delegation is acceptable?
3. Which rules-of-credit sets apply by discipline and deliverable type, and who owns
   their versions?
4. Which decisions must be recorded in PEC versus linked from an existing decision
   register?
5. What constitutes adequate evidence that a consequence has been reflected in an
   artifact, and who verifies it?
6. Which information classes may sponsors, clients, vendors, and subconsultants see?
7. What team size, data volume, availability window, residency, and recovery targets
   apply to the first production deployment?
8. Which enterprise identity, document, schedule, cost, and collaboration systems
   are required for the pilot?

None of these questions prevents the product definition in this PRD. They are the
remaining configuration and authority decisions needed to turn it into an
implementation specification.

---

## 21. Sponsor statement

*PEC gives every discipline a simple, repeatable way to declare what changed, what is
at risk, what is needed, what is being issued, and how the work is progressing. It
turns those declarations into a shared project state that leadership can interrogate
and the team can rely upon. When a gap requires a decision, PEC makes the basis and
authority visible; when that decision changes the project, PEC ensures the
consequence is assigned to the scope, design basis, deliverable, register, or other
documentation that must carry it. Reports are useful outputs of that system, but the
product is the trusted information flow underneath them.*

End of PRD v1.0
