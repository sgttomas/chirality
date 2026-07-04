# PEC — P1 Traceability

Requirement → implementation → test map promised by SPEC §10. Covers every P1-tagged
requirement in PRD §12, the P1 rows of §13 (data model), §15 (reporting), §16 (imports),
§17 (NFRs), and the product invariants I-1..I-10 (PRD §5).

How to read the **Test** column:

- `core:` = `core/test/*.test.ts` (unit, pure functions) · `server:` = `server/test/invariants.test.ts`,
  `server/test/integration.test.ts`, and `server/test/hardening.test.ts` (integration through the real
  HTTP layer against a temp DB, via `server/test/harness.ts`). `hardening.test.ts` closes the confirmed
  findings from the adversarial red-team pass (SPEC §13). Test names are quoted as they appear.
- `manual: <how>` = verified by hand, no automated test.
- `gap` = P1-implemented but not covered by an automated test (listed again under *Known P1 gaps*).

Paths are repo-relative. Where a requirement spans layers, the rule/derivation home is
listed first (the web layer holds no business rules — SPEC §1).

---

## PRD §12.1 Overview (PEC-OV)

| Requirement | Where implemented | Test |
|---|---|---|
| PEC-OV-001 KPIs computed per §8 | `core/src/status.ts` `projectStatus()` (kpis: pctOnPlan, holdsByCause, openDecisions, approvalsInFlight, scheduleForecastWd); served by `server/src/services/views.ts` `overviewView()`; rendered by `web/src/pages/Overview.tsx` | core: status.test.ts 'KPIs carry explanations with contributing records (PEC-OV-001/002)'; server: 'I-4: overview KPIs and health carry ruleId + contributing records, never bare values' |
| PEC-OV-002 every KPI/health drills down (I-4) | `Explain<T>` payload shape in `core/src/status.ts` (`mk()`); redaction in `views.ts` `redact()`; drill-down UI `web/src/shared.tsx` `HealthBadge`/`KpiCard`/`useExplain` | same two tests as PEC-OV-001 |
| PEC-OV-003 package rollup table, rows open the package | `views.ts` `overviewView()` `packageRollup` (incl. the cockpit's log-scoped `openIssues`, ADR-012); health rules `core/src/status.ts` `packageStatus()` (drill-downs carry the underlying issue records, ADR-012); `web/src/pages/Overview.tsx` rollup table (row → `/p/:pid/packages/:id`) | core: status.test.ts PH-* cases + 'ADR-012: PH-A1/PH-R1 drill-down …'; server: coverage-adr-012.test.ts (openIssues parity + log scoping); row navigation: manual — open Overview, click a rollup row |
| PEC-OV-004 waiting-on-you with threshold breach + what each blocks | `core/src/status.ts` `waitingOnYou()`; split into `breaching`/`other` in `views.ts` `overviewView()`; `web/src/pages/Overview.tsx` (breaching prominent, rest collapsed — SPEC §6.5 interpretation) | core: status.test.ts 'waitingOnYou: pending decisions for authority + ready approvals for signatory, with blocks (PEC-OV-004)' |
| PEC-OV-005 blocking items typed by cause everywhere | typed `hold.cause` (I-3) carried through: `views.ts` `overviewView()` `topBlockers`, `logRegisterView()` `holdCause` column, 409 payloads (`core/src/conditions.ts` `explainTransition()` includes hold cause), `web/src/shared.tsx` `ErrorBox`/`ConditionsPanel` | server: 'OM-2: an active hold vetoes closure … and shows in the 409' (typed hold in 409); register/blocker columns: manual |
| PEC-OV-006 export sponsor brief | `server/src/reports/sponsor-brief.ts` `sponsorBrief()`; route `GET reports/sponsor-brief` in `server/src/api.ts`; buttons in `web/src/pages/Overview.tsx` and `web/src/pages/Admin.tsx` (print-HTML → PDF via browser print, ADR-010) | gap — no automated test renders the brief; manual: Overview → "sponsor brief" |
| PEC-OV-007 thresholds configurable per project | `core/src/types.ts` `Thresholds` + defaults; stored in `project.thresholds` (`server/src/db.ts`); read in `core/src/status.ts`; written via `PUT config` in `server/src/api.ts` (audit-evented); editor in `web/src/pages/Admin.tsx` | core: status.test.ts DH-R2/DH-A4/PH-* fixtures exercise threshold values; config write path: manual — Admin → thresholds → save, verify audit event |

## PRD §12.2 Packages (PEC-PKG, P1 rows)

| Requirement | Where implemented | Test |
|---|---|---|
| PEC-PKG-001 package list with derived health | `core/src/status.ts` `packageStatus()` (PH-R1/R2/A1/A2/G); `views.ts` `packagesView()`; `web/src/pages/Packages.tsx` register | core: status.test.ts 'PH-A1: >= 20% amber/red deliverables → amber package (§8.3)', 'PH-R1: red deliverable with milestone → red package; PH-R2 late interface → red' |
| PEC-PKG-002 package summary + issues cockpit (ADR-011) | `views.ts` `packageDetailView()` — unified urgency-sorted `issues` (holds + interfaces + decisions + risks + rolled-up action items), `summary` counts (openIssues/overdue/holds/interfaces/decisions/risks/actions), `risks` group, and a deliverable rollup carrying workflow status; register `openIssues` count is log-scoped (`openIssueCount()` in `views.ts`); `web/src/pages/Packages.tsx` leads with the cockpit | server: issues-orientation.test.ts 'the issues cockpit unifies record types, urgency-first, with a workflow deliverable rollup', 'PEC-NFR-005: the register openIssues count is log-scoped and matches the cockpit'; browser-verified 2026-07-04 (PKG-P: 6 issues, 2 overdue) |
| PEC-PKG-004 deliverables by nearest commitment / need-by | `views.ts` `packageDetailView()` `deliverables` (server-side sort by due date); `web/src/pages/Packages.tsx` | manual: package detail ordering |
| PEC-PKG-005 "needs the lead this week" | `views.ts` `packageDetailView()` `needsLead` (sign-offs due, decisions to rule, holds to resolve, interface obligations); `web/src/pages/Packages.tsx` | manual: assign the lead as signatory/authority/hold owner and confirm the four kinds appear |
| PEC-PKG-006 package-level decisions linked to affected records | `decision.package_id` (`server/src/db.ts`, SPEC §3.6); `decision_link` rows via `server/src/services/decisions.ts`; surfaced in `views.ts` `packageDetailView()` `decisions` (+ affected counts); feeds PH-A2 in `core/src/status.ts` | server: 'I-10: superseding a decision …' creates and checks `decision_link` affected records; PH-A2 rule: gap (no dedicated fixture) |
| PEC-PKG-007 interface item fields (OM-7) | `core/src/types.ts` `InterfaceItem`; validation in `server/src/services/registers.ts` `createInterface()` (giving/receiving party required); blocking impact + aging in `views.ts` `packageDetailView()` `interfaces` | gap — no automated interface test; manual: Registers → interfaces → create/update |

## PRD §12.3 Deliverables (PEC-DEL)

| Requirement | Where implemented | Test |
|---|---|---|
| PEC-DEL-001 filterable list; master + issued views | `views.ts` `deliverablesView()` (package/discipline/state/due filters; `view=active\|master\|issued`); `web/src/pages/Deliverables.tsx` register | server: '§16: MDL import …' reads `?view=master`; filters: manual |
| PEC-DEL status = workflow completeness (ADR-011) | `core/src/status.ts` `workflowCompleteness()` — pure over the revision lifecycle (drafted → checked → approved → issued), independent of issues; surfaced as the summary status by `deliverablesView()` and on the deliverable-detail header; `web/src/shared.tsx` `WorkflowStages`. The issue-driven `deliverableStatus` (DH-*) is retained for package/overview rollups only | core: status.test.ts 'workflowCompleteness: maps each revision state to closed gates …', '… issued is 100% …', '… independent of holds and overdue items …'; server: issues-orientation.test.ts 'summary status is workflow completeness, not issue health'; browser-verified 2026-07-04 |
| PEC-DEL-002 deliverable metadata | `deliverable` table `server/src/db.ts`; `server/src/services/registers.ts` `createDeliverable()`/`updateDeliverable()`; header block in `web/src/pages/Deliverables.tsx` | server: creation exercised throughout invariants.test.ts (e.g. I-6, D-11); field-level: manual |
| PEC-DEL-003 open items across all record types | `views.ts` `deliverableDetailView()` `openItems` (work items, checks + comments, holds, approval records, decision dependencies) | server: 'I-1: a work item created once appears in My Week, the log register, and the deliverable view' |
| PEC-DEL-004 "before this issues" panel | `core/src/conditions.ts` `explainTransition()` (§5.5 payload); `views.ts` `deliverableDetailView()` `beforeIssue`; route `GET revisions/:id/explain` (`server/src/api.ts`); `web/src/shared.tsx` `ConditionsPanel` | core: conditions.test.ts 'explainTransition renders the before-this-issues panel payload (PEC-DEL-004)'; server: 'D-11/I-5 …' asserts the explain endpoint post-issue |
| PEC-DEL-005 evidence trail; status update = history entry | `server/src/services/work.ts` `addProgress()` (history kind `progress`); `evidence` table + `work.ts` `addEvidence()`; one merged stream in `views.ts` `deliverableDetailView()` (`evidence` + `history`); `web/src/pages/Deliverables.tsx` history section, `web/src/pages/MyWeek.tsx` drawer progress box | server: I-5 asserts history entries via the API; the progress-note round-trip itself: manual — add a progress note, see it in the deliverable history |
| PEC-DEL-006 state at revision level; chain visible | `revision` table; `server/src/services/revisions.ts` `createRevision()` (supersedes prior, chain via `superseded_by_revision_id`); `views.ts` `deliverableDetailView()` `revisionChain`; `web/src/pages/Deliverables.tsx` chain section | core: lifecycles.test.ts 'PRD §7.7 revision: issue is hard-gated and only from approved (D-11, I-5)'; server: 'D-11/I-5 …' walks the chain |
| PEC-DEL-007 hard conditions block; attempt recorded; waiver per I-8 | `core/src/conditions.ts` `evaluateGate()`; `server/src/services/shared.ts` `gateOrThrow()`; blocked-attempt persistence in `server/src/api.ts` `tx()` wrapper (`transition_blocked` history); waiver `server/src/services/decisions.ts` `waiveCondition()` | server: 'I-5: … cannot close; the blocked attempt is recorded …', 'D-11/I-5 …', 'I-8: waiving a condition creates a linked waiver Decision'; core: conditions.test.ts 'hard blocks, warn does not (D-11)' |
| PEC-DEL-008 issue events with purpose/transmittal/recipients + links | `server/src/services/revisions.ts` `transitionRevision()` issue path (payload required; recording the event IS the transition, D-11); `issue_event` table; issue drawer `web/src/pages/Deliverables.tsx` | server: 'D-11/I-5: revision cannot issue with open hard conditions; full chain check→approve→issue works; audit + archive ref written' |
| PEC-DEL-009 distinct visible facts, never one merged flag | `views.ts` `deliverableDetailView()` `facts` (workComplete / checkAccepted / approvalRecorded / authorizedForIssue / issued / returnedWithComments / superseded / archived-P3); facts strip in `web/src/pages/Deliverables.tsx` | server: 'I-6: …' asserts `facts.checkAccepted/approvalRecorded/issued` independently |

## PRD §12.5 Action & Hold Log and intake (PEC-AHL)

| Requirement | Where implemented | Test |
|---|---|---|
| PEC-AHL-001 unified open-items register | `views.ts` `logRegisterView()` (server-composed union: open work items, active holds, open interfaces, untriaged intake; age/overdue/cause/anchor columns; all filters server-side); `web/src/pages/LogHome.tsx` tab 1 | server: 'I-1 …' (work item in log), 'I-2 …' (intake row flagged unanchored) |
| PEC-AHL-002 three logs; visibility; never silent log change | `core/src/permissions.ts` `visibleLogs()`; filtering + explanation redaction in `views.ts` (`logsFor()`/`redact()`); log-change history in `server/src/services/work.ts` `updateWorkItem()` (kind `log_change`) | core: permissions.test.ts 'log visibility: viewer sees package+client by default; config overrides (PEC-NFR-005)'; log-change history entry: gap |
| PEC-AHL-003 raise-an-item everywhere, ≤ 8 fields | `server/src/services/intake.ts` `RaiseIntakeInput` (8 fields incl. the quick-type set); `web/src/RaiseItem.tsx` (global dialog, mounted in `web/src/main.tsx` shell) | core: permissions.test.ts 'anyone on the project may raise intake (PEC-AHL-003); config can restrict'; server: 'I-2 …' raises intake through the API |
| PEC-AHL-004 intake verbatim; disposition enum | `statement_verbatim` freeze trigger in `server/src/db.ts`; `INTAKE_DISPOSITIONS` enforced in `server/src/services/intake.ts` `dispositionIntake()` | server: 'I-7: … intake statement is frozen' |
| PEC-AHL-005 one intake → many records, back-linked | `server/src/services/intake.ts` `dispositionIntake()` converted path (creates work items/holds/risks/decisions/approvals/interfaces atomically); `intake_link` table; links shown in `views.ts` `intakeQueueView()` | gap — conversion is not exercised by an automated test; manual: triage an intake to `converted` with ≥2 records, check back-links in the queue |
| PEC-AHL-006 triage queue with untriaged age; unanchored flagged + excluded | `views.ts` `intakeQueueView()` (`untriagedAgeWd`); `web/src/pages/LogHome.tsx` tab 2; exclusion from rollups is structural (rollups in `core/src/status.ts` read controlled records only); S-INTAKE/S-ANCHOR signals in `core/src/status.ts` | server: 'I-2 …' (flagged unanchored, work item creation without anchor rejected); queue UI: manual |
| PEC-AHL-007 raiser notified at routing / ownership / closure | `server/src/services/intake.ts` (routing notification on disposition); `server/src/services/work.ts` `notifyIntakeRaiser()` (ownership change, closure) | gap — no automated assertion on raiser notifications |

## PRD §12.6 My Week (PEC-MW)

| Requirement | Where implemented | Test |
|---|---|---|
| PEC-MW-001 committed items grouped by deliverable | `core/src/status.ts` `myWeek()` (`committed`); `views.ts` `myWeekView()`; grouping in `web/src/pages/MyWeek.tsx` | core: status.test.ts 'myWeek: manual commit, need-by, overdue reasons; checks and comments owed; waiting on others (PEC-MW-*)'; server: 'I-1 …' |
| PEC-MW-002 checks/comments owed, distinct from own items | `core/src/status.ts` `myWeek()` (`checksOwed`, `commentsOwed`); own section in `web/src/pages/MyWeek.tsx`; respond flow posts `comments/:id/respond` | core: same status.test.ts myWeek case |
| PEC-MW-003 waiting-on-others: visible, chase-able, not commitments | `core/src/status.ts` `myWeek()` (`waitingOnOthers` — holds/decisions gating the user's work); `web/src/pages/MyWeek.tsx` | core: same status.test.ts myWeek case |
| PEC-MW-004 work-item panel in place | `views.ts` `workItemDetailView()` (anchor, blockedBy, closure conditions explain, offered transitions, history, evidence); drawer in `web/src/pages/MyWeek.tsx` (progress + attachments without navigation) | manual: open a My Week row, progress + close from the drawer (endpoint pieces covered by server I-5 via the same services) |
| PEC-MW-005 why-in-week on every item | `core/src/status.ts` `MyWeekItem.whyInWeek` (manual commitment / need-by / overdue); rendered per row in `web/src/pages/MyWeek.tsx` | core: status.test.ts myWeek case asserts the three reasons |
| PEC-MW-006 overdue flagged; owed-to-others flagged equally | `core/src/status.ts` `myWeek()` overdue flags on both `committed` and `checksOwed`/`commentsOwed`; equal badges in `web/src/pages/MyWeek.tsx` | core: status.test.ts myWeek case (overdue reason); owed-side flag: manual |
| PEC-MW-007 (P2; P1 interim) need-by + manual commit flag | `work_item.committed_week` column; editable via `updateWorkItem()` (`server/src/services/work.ts`); commit toggle in `web/src/pages/MyWeek.tsx` drawer; `web/src/pages/Plan.tsx` + `GET plan` (`server/src/api.ts`) state the P2 scope | core: status.test.ts myWeek case ('manual' reason from `committedWeek`) |

## PRD §12.7 Approval Register (PEC-AUTH, P1 rows)

| Requirement | Where implemented | Test |
|---|---|---|
| PEC-AUTH-001 register with authority fields | `approval_record` table (SPEC §3.6) in `server/src/db.ts`; `server/src/services/decisions.ts` `createApprovalRecord()`; `views.ts` `approvalRegisterView()` (latency, outcome decision ref, prerequisites); `web/src/pages/Registers.tsx` approvals tab; drawer in `web/src/pages/Deliverables.tsx` | server: 'I-6: check acceptance, approval basis, and approval outcome are three records …' |
| PEC-AUTH-002 requirement / readiness / outcome distinct; outcome is a Decision (OM-6) | states `required → prereqs_incomplete → ready → decided` in `core/src/lifecycles.ts`; readiness re-evaluation `server/src/services/shared.ts` `syncApprovalState()`; outcome via `decisions.ts` `recordApprovalOutcome()` → Decision `kind=approval_outcome` | server: 'I-6 …' (ready gating, linked Decision); core: lifecycles.test.ts 'PRD §7.5 approval record: decided only via record_outcome from ready (PEC-AUTH-004)' |
| PEC-AUTH-003 approval may compel records via conditions | `approval`-type condition satisfaction in `core/src/conditions.ts` (§5.3); prerequisite instantiation on creation + "approved with conditions" instantiates conditions on the target (`server/src/services/decisions.ts` post-outcome effects) | core: conditions.test.ts 'approval-type condition: only approve/conditionally_accept outcomes satisfy (§5.3)' |
| PEC-AUTH-004 no closure by task completion | `core/src/lifecycles.ts` approval table has no other path to `decided`; signatory-only permission in `core/src/permissions.ts` (`approval.outcome`); early-outcome rejection in `decisions.ts` | core: lifecycles.test.ts '§7.5 …(PEC-AUTH-004)'; server: 'I-6 …' ('no outcome before ready' 400; document controller 403) |

## PRD §12.8 Checks (PEC-CHK, P1 rows)

| Requirement | Where implemented | Test |
|---|---|---|
| PEC-CHK-001 checklist templates instantiated per check | `checklist_template` table (discipline / deliverable_type / package keys) in `server/src/db.ts`; instantiation in `server/src/services/checks.ts` `createCheck()` (template items → checklist instance); templates seeded via `tools/seed.ts` | gap — no automated template test, and no API surface for template CRUD in P1 (seed/DB only); manual: create a check with a `templateId`, checklist appears |
| PEC-CHK-002 check + child comments per §7.4 | `server/src/services/checks.ts` (comment add/respond/accept/reopen, checker-only closure); `review_comment` table; check drawer in `web/src/pages/Deliverables.tsx`; respond flow in `web/src/pages/MyWeek.tsx` | core: lifecycles.test.ts 'PRD §7.4 check: acceptance requires no open comments …'; permissions.test.ts 'only the assigned checker accepts checks and comment closures (I-6, PEC-CHK-002)'; server: RBAC test (pm cannot accept) |
| PEC-CHK-003 three distinct facts, never merged | `checks.ts` `acceptCheck()` (accepts with incomplete checklist, records the incomplete items; refuses with open comments); `views.ts` `checkDetailView()` `facts` (checklistComplete / commentsClosed / checkerAccepted); three-facts strip in `web/src/pages/Deliverables.tsx` | core: lifecycles.test.ts §7.4 case; server: harness `acceptCheckOn()` exercises the full flow in I-6/D-11; the three-facts view payload itself: manual |
| PEC-CHK-004 independence warn (P1 warn; hard block P3) | `server/src/services/checks.ts` `createCheck()` sets `independence_warning` when checker = revision owner; badge + banner in `web/src/pages/Deliverables.tsx` | gap — no automated test creates an owner-checker check |
| PEC-CHK-005 acceptance may satisfy conditions but is not approval | `checks.ts` `acceptCheck()` → `satisfyConditions()` for `check`-type conditions only; no Decision written (single outcome write-path is `decisions.ts` `recordDecisionRow()`, which check acceptance never calls) | core: conditions.test.ts 'check-type condition: satisfied by accepted check on parent revision (§5.3)'; server: 'I-6 …' (acceptance ≠ approval) |

## PRD §12.9 Decisions (PEC-DEC, P1 rows)

| Requirement | Where implemented | Test |
|---|---|---|
| PEC-DEC-001 decision log per §7.6 | `decision` table (SPEC §3.6); `server/src/services/decisions.ts` `createDecision()`/`progressDecision()`/`recordDecisionOutcome()`; `views.ts` `decisionRegisterView()`; `web/src/pages/Registers.tsx` decisions tab | server: 'I-10 …' walks identified → preparer → pending → decided through the API |
| PEC-DEC-002 linkable to holds/deliverables; overdue surfaces in Overview/Packages/Deliverables | `decision_link` (affects/blocks/follow_up/supersedes); hold resolution kind `decision_recorded` (`server/src/services/holds.ts`); overdue surfacing: S-DEC signal + `openDecisions` KPI (`core/src/status.ts`), `packageDetailView()` `decisions.overdueDays` + PH-A2, `deliverableDetailView()` `openItems.decisionDependencies` | core: status.test.ts 'S-DEC: overdue decision blocking an issue transition is red regardless of days (§8.4)'; server: 'I-10 …' (affected links) |
| PEC-DEC-003 outcome vocabulary (8 values) | `core/src/types.ts` `DECISION_OUTCOMES` (select, approve, reject, defer, conditionally_accept, confirm_basis, waive, supersede); validated in `decisions.ts` | server tests exercise select / approve / waive (I-10, I-6, I-8); remaining values: enum-validated, manual |

## PRD §12.10 Risk log (PEC-RISK, P1 rows)

| Requirement | Where implemented | Test |
|---|---|---|
| PEC-RISK-001 risk log fields + links | `risk` table (SPEC §3.7); `server/src/services/registers.ts` `createRisk()`/`updateRisk()`; `views.ts` `riskRegisterView()`; `web/src/pages/Registers.tsx` risks tab; links via work-item anchor `risk` and `decision_link` | gap — no automated risk test; manual: Registers → risks → create/update; risks CSV import/export |
| PEC-RISK-002 risk-treatment work items appear in Packages/Deliverables/My Week | `work_item.kind = risk_treatment` + anchor type `risk` (`core/src/types.ts` `ANCHOR_TYPES`, `server/src/services/work.ts` `derivePackageId()`); projections are the generic work-item projections | server: 'I-1 …' proves the generic projection (deliverable-anchored); risk-anchored variant: gap |

## PRD §12.11 Interfaces (PEC-INT, P1 rows)

| Requirement | Where implemented | Test |
|---|---|---|
| PEC-INT-001 interface record; raised via intake or directly; surfaces in Log + Packages | `server/src/services/registers.ts` `createInterface()`; intake quick type `interface` → conversion in `services/intake.ts`; `views.ts` `logRegisterView()` interface rows + `packageDetailView()` `interfaces`; P1 register view (ahead of the P2 dedicated view) in `web/src/pages/Registers.tsx` | gap — no automated interface test; RAIL `interface` rows import via `server/src/import/index.ts` (untested); manual: raise → triage → appears in Log and package |

## PRD §12.12 Archive (PEC-ARC, P1 part)

| Requirement | Where implemented | Test |
|---|---|---|
| PEC-ARC-002 controlled chain per issued revision (P1 chain; views P3) | `server/src/services/revisions.ts` issue path: `issue_event` written with purpose, transmittal, recipients, generated `archive_ref`, linked approval-record + decision ids; chain readable via `views.ts` `deliverableDetailView()` `revisionChain[].issueEvents` | server: 'D-11/I-5 …' asserts `issueEvents[0].archiveRef` matches `^ARC-` |

## PRD §12.13 Reconciliation (PEC-REC)

No P1 rows — PEC-REC-001..003 are all P3 (SPEC §11). Schema headroom only: decision state
strings are not DB-enums, so `reconciled` can be added without migration.

## PRD §12.14 Notifications (PEC-NOT)

| Requirement | Where implemented | Test |
|---|---|---|
| PEC-NOT-001 event notification catalog | event-driven producers as transition side-effects: assignment (`services/work.ts`, `services/checks.ts` checker/responder), hold raise/resolve (`services/holds.ts`), decision pending + approval ready + supersession (`services/decisions.ts`, `services/shared.ts` `syncApprovalState()`), intake routed/updated/closed (`services/intake.ts`, `services/work.ts`), revision ready for approval (`services/shared.ts` `syncRevisionState()`); time-driven sweep `server/src/services/sweep.ts` (hourly in `server/src/index.ts`, on login in `api.ts`), idempotent per (person, event, record, local day); read via `GET notifications` + bell in `web/src/main.tsx`; every row carries record, reason, next_action, due (`server/src/repo.ts` `notify()`) | server: 'OM-2 …' asserts `hold_resolved_unblocked` reaches the owner; rest of the catalog + sweep idempotency: gap |
| PEC-NOT-002 / PEC-NOT-003 | P2 — not implemented (by design, SPEC §11) | n/a |

## PRD §13 Data model (P1 rows)

| Requirement | Where implemented | Test |
|---|---|---|
| §13.1 P1 entities (hierarchy, intake, work item, hold, check/checklist/comment, approval record, decision, risk, interface, condition + template, issue event, evidence/history/basis, person/role/assignment, audit event) | schema: `server/src/db.ts` (all P1 tables incl. `basis_reference`, `evidence`, `audit_event`); domain types: `core/src/types.ts`; repository row-mapping: `server/src/repo.ts` | core: lifecycles.test.ts 'every lifecycle state named in types is reachable in the transition tables'; table-level behavior covered by the server suite throughout |
| §13.2 work item required fields at creation / closure | creation validation (title, anchor I-2, owner, need-by, package derived from anchor) in `server/src/services/work.ts` `createWorkItem()`; closure via gated `close` transition (conditions satisfied/waived, closing statement, closed-by/date) in `work.ts` `transitionWorkItem()` | server: 'I-2 …' (anchor required), 'I-5 …' (closure conditions + close) |
| §13.3 condition fields | `condition_record` table in `server/src/db.ts`; `core/src/types.ts` `Condition` (parent + gated transition, type, required ref/artifact, source, severity, owner, need-by, state, satisfied-by, waiver decision link) | core: conditions.test.ts (all satisfaction types, waiver link, severity); server: 'I-8 …' (waiver_decision_id populated) |

## PRD §15 Reporting and exports (P1 rows)

| Requirement | Where implemented | Test |
|---|---|---|
| Sponsor brief | `server/src/reports/sponsor-brief.ts` (print-HTML; PDF via browser print, ADR-010) | gap (see PEC-OV-006) |
| Register exports: action & hold log, deliverables status, decision log, risk log, approval register | server CSV: `server/src/import/index.ts` `exportRegister()` (`mdl`, `rail`, `decisions`, `risks`, `approvals`, `interfaces`, `intake`); any *filtered view* exports exactly what is displayed via the client-side `web/src/shared.tsx` `RegisterTable` export button (note: the unified Log register exports client-side only — there is no server `export/log.csv`) | server: '§16: MDL import … export round-trips', '§16: RAIL import … unanchored intake row round-trips in the export'; decisions/risks exports round-trip in pilot-hardening.test.ts; approvals/interfaces/intake exports: gap |
| Individual weekly commitments | `exportRegister('commitments')` in `server/src/import/index.ts` (`GET export/commitments.csv`, ADR-010) | gap — manual: export and compare against My Week |

## PRD §16 Import contracts (P1)

| Requirement | Where implemented | Test |
|---|---|---|
| MDL import (required/optional columns, per-row rejects, state seeding) | `server/src/import/index.ts` `importMdl()`; RFC 4180 parser `server/src/import/csv.ts`; idempotent-by-key + `force=true` conflict rule; history `kind=import` | server: '§16: MDL import validates row-by-row, seeds state, rejects bad rows with reasons; export round-trips' |
| RAIL import (type mapping, hold_cause required for holds, unanchored → intake) | `importRail()` in `server/src/import/index.ts` | server: '§16: RAIL import anchors on doc_no match, else lands as unanchored intake; holds require cause' |
| Decision log import | `importDecisions()` in `server/src/import/index.ts` (external `decision_id` stored as the `ref` idempotency key — fixed 2026-07-04) | server: pilot-hardening.test.ts 'decisions import: happy path, decided-requires-outcome, bad status/authority rejected', '… external decision_id is preserved as the ref and re-import is idempotent', '… affected_refs links … export round-trips' |
| Risk log import | `importRisks()` in `server/src/import/index.ts` (external `risk_id` stored as the `ref` idempotency key — fixed 2026-07-04) | server: pilot-hardening.test.ts 'risks import: happy path + linking + bounds/status validation; re-import is idempotent' |

## PRD §17 Non-functional requirements (P1 rows)

| Requirement | Where implemented | Test |
|---|---|---|
| PEC-NFR-001 append-only history + audit events | UPDATE/DELETE-rejecting triggers on `history_entry`/`audit_event` (`server/src/db.ts`); insert-only repo methods (`server/src/repo.ts` `history()`/`audit()`); audit writes at approval outcome + waiver (`services/decisions.ts`), issue (`services/revisions.ts`), config change (`api.ts` `PUT config`) | server: 'I-7: UPDATE/DELETE on history and audit tables are rejected by triggers …', 'I-8 …' (waiver audit), 'D-11/I-5 …' (issue audit) |
| PEC-NFR-002 no hard delete of controlled records | delete-rejecting triggers on all controlled tables (`server/src/db.ts` `CONTROLLED_TABLES`); repo exposes no delete; terminal states with reason (cancel/withdraw/supersede) in lifecycles | server: 'I-7/PEC-NFR-002: controlled records cannot be hard-deleted' |
| PEC-NFR-003 ≤ 2 s at 10k open items / 250k history | per-project `ProjectSnapshot` loaded in a handful of indexed queries (`server/src/repo.ts` `snapshot()`, ~300 ms at 10k; history never loaded into the snapshot); derivation de-quadratic-ized by a memoized per-snapshot index (`core/src/snapshot-index.ts`) consulted by `activeHoldsFor()`/`openWorkItemsFor()`, turning the O(deliverables × work-items) rescans into O(1) map hits — measured 2026-07-04: overview 628 ms, packages 551 ms, deliverables 543 ms at 10k (was 11–13 s) | server: pilot-hardening.test.ts 'PEC-NFR-003: derived views render within 2s at 10k deliverables/work-items', '… snapshot load is bounded and history-independent' |
| PEC-NFR-004 optimistic concurrency | version-checked `update()` in `server/src/repo.ts`; 409 `VERSION_CONFLICT` with intervening history (`server/src/errors.ts`); every web mutation sends `version` and `web/src/shared.tsx` `ErrorBox` tells the user to reload | server: 'PEC-NFR-004: stale version writes are rejected with the intervening history' |
| PEC-NFR-005 server-side RBAC + log visibility at the query layer | rules matrix `core/src/permissions.ts` (`can()`), enforced per route/service via `requireCan()` (`server/src/services/shared.ts`); log visibility `visibleLogs()` applied at serialization in `views.ts`; UI probe `GET can/:action` | core: permissions.test.ts (whole file); server: 'RBAC: viewer is read-only; checker acceptance is checker-only …' |
| PEC-NFR-007 multi-project isolation | every project-scoped repo query takes `project_id` from the authenticated route (`server/src/api.ts` `authed()` → `Sx.projectId`; `server/src/repo.ts` `get/list/update` are project-scoped), never from the body; `historyFor()` now takes `project_id` as its leading argument and filters on it (fixes a confirmed leak where the history endpoint returned another project's `history_entry` rows by record id — fixed 2026-07-04); snapshot link scans (`hold_link`/`decision_link`) are bounded to the project via a join on the parent's `project_id` | server: pilot-hardening.test.ts 'PEC-NFR-007: the history endpoint does not leak another project\'s history rows' (probed across every id-taking endpoint; only history leaked, now closed) |
| PEC-NFR-009 backup/restore, RPO ≤ 24 h, tested restore | `tools/backup.ts` — `backup`: WAL-safe `VACUUM INTO` snapshot to `backups/pec-YYYYMMDD-HHMMSS.db`, prunes to newest 14; `restore <file>`: integrity-checks the backup, moves the live db (+wal/shm) aside to `pec.db.pre-restore*`, copies the backup into place, prints restart instructions; honors `PEC_DB` like the server (SPEC §12: run daily for RPO ≤ 24 h); operational procedure + rehearsal recipe in `docs/PILOT.md` §4–5 | server: coverage-backup-restore.test.ts 'PEC-NFR-009: backup → mutate → restore round-trip; prior database preserved aside', '… restore refuses a corrupt backup …', '… unknown backup name fails …', 'backup prunes to the newest 14'; also rehearsed end-to-end by `npm run drill` (`tools/pilot-drill.ts` §4). The pilot-readiness gate additionally requires one rehearsal against the real pilot DB (PILOT.md §5) |
| PEC-NFR-010 UTC storage; project timezone + working-day calendar | all timestamps UTC ISO-8601 (`server/src/repo.ts` `nowIso()`); `core/src/calendar.ts` (localDate, working-day math over project weekend/holiday config); thresholds computed in working days (`core/src/status.ts`) | core: calendar.test.ts 'localDate respects timezone (PEC-NFR-010)' + the whole file |

## PRD §5 Invariants I-1..I-10

| Invariant | Where enforced | Test |
|---|---|---|
| I-1 one record, many views | single `work_item` row projected by `views.ts` (log, my-week, deliverable detail) and `core/src/status.ts` — no view-owned copies anywhere | server: 'I-1: a work item created once appears in My Week, the log register, and the deliverable view — same ref, no copies' |
| I-2 no unanchored planned work | `createWorkItem()` requires an anchor (`server/src/services/work.ts`); unanchored concerns exist only as intake, flagged in `logRegisterView()`; rollups read controlled records only | server: 'I-2: direct work-item creation without an anchor is rejected; untriaged intake is visible and flagged unanchored' |
| I-3 holds are typed | `raiseHold()` requires cause + owner + need-by + ≥1 blocking link (`server/src/services/holds.ts`) | server: 'I-3: hold requires typed cause, owner, need-by, and ≥1 blocking link' |
| I-4 status derived + explainable | `core/src/status.ts` — pure, never persisted (SPEC §6); every value an `Explain` with ruleId/threshold/contributing | server: 'I-4: overview KPIs and health carry ruleId + contributing records, never bare values'; core: status.test.ts (every DH-*/PH-* rule has a fixture) |
| I-5 transitions condition-gated; no generic done | gates declared per transition in `core/src/lifecycles.ts`; evaluated by `core/src/conditions.ts` `evaluateGate()` via `gateOrThrow()` (`server/src/services/shared.ts`) | server: 'I-5: …', 'D-11/I-5: …'; core: lifecycles.test.ts 'there is no generic "done" event on any record (I-5)' |
| I-6 approval ≠ check ≠ decide | three record types (check / approval_record / decision); single outcome write-path `recordDecisionRow()` (`server/src/services/decisions.ts`); no merged flag anywhere (`facts` in `views.ts`) | server: 'I-6: check acceptance, approval basis, and approval outcome are three records; outcome is a linked Decision (OM-6)' |
| I-7 controlled records append-only | history/audit triggers + insert-only repo (`server/src/db.ts`, `server/src/repo.ts`); intake verbatim trigger | server: 'I-7: UPDATE/DELETE on history and audit tables are rejected by triggers; intake statement is frozen' |
| I-8 waivers are Decisions | the only waive path is `waiveCondition()` → Decision `kind=waiver` linked via `waiver_decision_id` (`server/src/services/decisions.ts`); permission per condition type (`core/src/permissions.ts`) | server: 'I-8: waiving a condition creates a linked waiver Decision + audit event; unauthorized roles cannot waive'; core: conditions.test.ts 'waived stands as stored with waiver decision ref (I-8) …', permissions.test.ts 'waivers: strict types need pm/EM …' |
| I-9 checking/approving consume capacity | P2+ by its own wording ("wherever the plan exists") — no P1 obligation; headroom noted in `web/src/pages/Plan.tsx` / SPEC §11 | n/a in P1 |
| I-10 supersession never deletes | supersede transitions keep the record with `superseded_by_id` links (`server/src/services/decisions.ts` `supersedeDecision()`/`supersedeApproval()`, `revisions.ts` chain); affected records flagged via `basis_superseded` history + owner notifications | server: 'I-10: superseding a decision keeps it visible, links the replacement, and flags affected records'; core: conditions.test.ts '… superseded passes gate (I-10)' |

---

## Known P1 gaps

Honest list of what is implemented but not automatically tested (or deliberately thin), as of 2026-07-04:

1. **Closed by the 2026-07-04 pilot-hardening pass** (`server/test/pilot-hardening.test.ts`,
   driven by a live adversarial probe): PEC-NFR-007 cross-project isolation (a confirmed
   history-endpoint leak, now fixed and regression-tested); the decisions/risks importers +
   exports and RAIL re-import idempotency (§16) — three importers were discarding the external
   id and duplicating on re-import, now fixed; PEC-NFR-003 load at 10k items — the derived views
   were O(deliverables × work-items) (11–13 s), now de-quadratic-ized to ~0.6 s and guarded by a
   budget test; and intake conversion fan-out with back-links (PEC-AHL-005). Intake conversion +
   check three-facts/comment reopen (PEC-CHK-002/003) + decision-gated issue (§9) are also
   exercised by `server/test/integration.test.ts`.
2. **Closed by the 2026-07-04 P1-coverage pass** (`server/test/coverage-*.test.ts` +
   `core/test/coverage-ph-a2.test.ts`, 32 tests): sponsor-brief render (PEC-OV-006); independence
   warning (PEC-CHK-004); risk + interface registers incl. version-conflict handling and the
   risk-treatment work-item projection (PEC-RISK-001/002, PEC-INT-001, PEC-PKG-007); the §15
   exports — approvals/interfaces/intake/commitments/log, with log-visibility on the log export;
   the PH-A2 package-health rule; the log-change history entry (PEC-AHL-002); notification
   producers + sweep idempotency (PEC-NOT-001); and PEC-NFR-003 at 250k history rows (snapshot
   proven history-independent). The pass also fixed a real defect: the risk API
   (`createRisk`/`updateRisk`) did not enforce the probability/impact **1–5** range that the CSV
   importer does — now validated (`server/src/services/registers.ts` `validateRiskScore()`).
3. **Server `export/log.csv` implemented** (2026-07-04): a `log` case in `exportRegister`
   (`server/src/import/index.ts`) mirrors the displayed Action & Hold Log with log-visibility
   filtering (§7, PEC-NFR-005); the client-side `RegisterTable` export remains for filtered views.
5. **Checklist/condition template management has no API/UI**: templates are seeded via
   `tools/seed.ts` or direct DB in P1 (PEC-CHK-001 instantiation itself works and SPEC §7
   names templates under config — CRUD deferred).
6. **Backup/restore now automated** (2026-07-04, item B): the round-trip, corrupt-backup
   refusal, and retention pruning run in CI (`server/test/coverage-backup-restore.test.ts`), and
   `npm run drill` (`tools/pilot-drill.ts`) rehearses the whole pilot pipeline — §16 imports with
   reject reporting + MDL re-import idempotency, coordinator triage over unanchored intake,
   derived-view rendering, backup → mutate → restore — against a scratch DB (fixtures under
   `tools/fixtures/`, or the real pilot CSVs via `--mdl/--rail/--decisions/--risks`). What remains
   is inherently manual: one rehearsal against the **real pilot database** before go-live
   (recipe: `docs/PILOT.md` §5) — record its date in STATUS when done.
7. **PEC-NOT-002/003, PEC-CHK-004 hard block, PEC-REC-\*, dedicated interface register** are
   P2/P3 by design (SPEC §11), not gaps.
