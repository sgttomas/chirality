/**
 * PEC core vocabulary — entity types per docs/SPEC.md §3, controlled vocabulary per PRD §4.4.
 * String-literal unions (not TS enums: erasable-syntax-only) with runtime const arrays for validation.
 */

// ---------- shared ----------

export const HEALTH = ['green', 'amber', 'red'] as const
export type Health = (typeof HEALTH)[number]

export const RECORD_TYPES = [
  'project', 'package', 'deliverable', 'revision',
  'intake_item', 'work_item', 'hold', 'check', 'review_comment',
  'approval_record', 'decision', 'risk', 'interface_item',
  'condition', 'issue_event', 'evidence', 'basis_reference', 'person',
  'plan_item', 'plan_shift', 'schedule_activity', // P2 planning (PRD §13.1)
  'import_proposal', // D-PEC-08: proposed imports (§16 contracts behind a human accept/apply gate)
  'package_tracker', // D-PEC-13: §16 tracker contract (import-owned register)
] as const
export type RecordType = (typeof RECORD_TYPES)[number]

/** Record types a work item may use as its primary anchor (SPEC §3.3, PRD §13.4). */
export const ANCHOR_TYPES = [
  'deliverable', 'revision', 'package', 'decision', 'approval_record', 'risk', 'interface_item',
] as const
export type AnchorType = (typeof ANCHOR_TYPES)[number]

export const LOGS = ['package', 'internal', 'client'] as const
export type Log = (typeof LOGS)[number]

export const ROLES = [
  'sponsor', 'pm', 'engineering_manager', 'package_lead', 'discipline_lead',
  'engineer_of_record', 'checker', 'approver', 'planner', 'coordinator',
  'contributor', 'document_controller', 'viewer', 'admin',
] as const
export type Role = (typeof ROLES)[number]

export interface ContributingRef {
  recordType: RecordType
  id: number
  ref: string
  why: string
}

/** Every derived value ships with its rule and contributors (I-4, ADR-004). */
export interface Explain<V = string> {
  value: V
  ruleId: string
  detail: string
  threshold?: string
  contributing: ContributingRef[]
}

// ---------- identity ----------

export interface Person {
  id: number
  name: string
  email: string
  isAdmin: boolean
  discipline: string | null
}

export interface ProjectCalendar {
  timezone: string
  /** e.g. ['Sat','Sun'] — short en weekday names */
  weekendDays: string[]
  /** local dates YYYY-MM-DD */
  holidays: string[]
}

/** §8.4 governance thresholds; all overridable per project (PEC-OV-007). */
export interface Thresholds {
  holdAgeWarnWd: number
  holdAgeRedWd: number
  decisionOverdueWarnD: number
  decisionOverdueRedD: number
  approvalLatencyWarnWd: number
  approvalLatencyRedWd: number
  commentAgeWarnWd: number
  commentAgeRedWd: number
  untriagedWarnWd: number
  untriagedRedWd: number
  unanchoredWarnCount: number
  unanchoredRedCount: number
  unanchoredRedAgeD: number
  forecastSlipAmberWd: number // deliverable amber: slip <= this; red beyond (§8.2: 5)
  schedulePressureWarnD: number
  schedulePressureRedD: number
  /** §8.3 "interface item overdue past escalation" — escalation threshold, working days (implementer default) */
  interfaceOverdueRedWd: number
  /** PEC-PKG-008 (P2): interface aging feeds package health below escalation — amber past this, working days */
  interfaceOverdueWarnWd: number
  /** §8.4 capacity row (P2): committed load as % of capacity — warn above, escalate above */
  capacityWarnPct: number
  capacityRedPct: number
}

export const DEFAULT_THRESHOLDS: Thresholds = {
  holdAgeWarnWd: 7, holdAgeRedWd: 14,
  decisionOverdueWarnD: 0, decisionOverdueRedD: 7,
  approvalLatencyWarnWd: 5, approvalLatencyRedWd: 10,
  commentAgeWarnWd: 5, commentAgeRedWd: 10,
  untriagedWarnWd: 2, untriagedRedWd: 5,
  unanchoredWarnCount: 0, unanchoredRedCount: 5, unanchoredRedAgeD: 5,
  forecastSlipAmberWd: 5,
  schedulePressureWarnD: 0, schedulePressureRedD: 10,
  interfaceOverdueRedWd: 7,
  interfaceOverdueWarnWd: 0,
  capacityWarnPct: 100, capacityRedPct: 110,
}

export interface ProjectConfig {
  holdCauses: string[]
  issuePurposes: string[] // D-07: default IFR/IFA/IFC, configurable labels
  /** role → logs that role may see (PEC-NFR-005, PEC-AHL-002) */
  logVisibility: Partial<Record<Role, Log[]>>
  /** condition type → roles that may waive (I-8; SPEC §2.2) */
  waiverRoles: Partial<Record<ConditionType, Role[]>>
  allowAnyoneRaiseIntake: boolean
}

export interface Project {
  id: number
  code: string
  name: string
  calendar: ProjectCalendar
  thresholds: Thresholds
  config: ProjectConfig
  version: number
}

// ---------- hierarchy ----------

export interface Package {
  id: number
  projectId: number
  code: string
  name: string
  leadId: number | null
  description: string | null
  milestone: string | null
  /** project area the package belongs to (§16 mdl optional column, D-PEC-23) */
  area: string | null
  /** package classification, e.g. Standard vs FEED (§16 mdl optional column, D-PEC-23) */
  packageType: string | null
  /** attested package discipline from contract v2 imports (D-PEC-41) */
  discipline: string | null
  /** complete distinct attested discipline set (D-PEC-51); never inferred */
  disciplines: string[]
  /** full-fidelity capture of unmapped source columns, verbatim JSON (D-PEC-41) */
  sourcePayload: Record<string, string> | null
  version: number
}

export interface Deliverable {
  id: number
  projectId: number
  packageId: number
  docNo: string
  title: string
  discipline: string | null
  deliverableType: string | null
  ownerId: number | null
  dcRef: string | null
  clientNo: string | null
  milestone: string | null
  dueDate: string | null // local date YYYY-MM-DD
  issuePurposePlan: string | null
  remarks: string | null
  /** Contract v2 (D-PEC-41) PE-attested import fields. Never in-app editable, never
   * derived in-app (workplan reconciliation 1) — import is their only writer. */
  projectPhase: string | null
  targetCompleteness: string | null
  workingStatus: string | null
  /** attested percent complete, integer 0..100; null when unattested or marker-valued */
  percentComplete: number | null
  /** attested non-numeric percent marker (e.g. "Next Phase"), verbatim; excluded from rollups */
  percentCompleteVerbatim: string | null
  /** full-fidelity capture of unmapped source columns, verbatim JSON (D-PEC-41) */
  sourcePayload: Record<string, string> | null
  version: number
}

/** Contract v2 attested working-status vocabulary (TWD template Lists sheet; D-PEC-41). */
export const MDL_WORKING_STATUSES = [
  'Not Set', 'Not Started', 'In Progress', 'On Hold', 'Complete', 'Cancelled',
] as const

/** Contract v2 RAIL issue-type vocabulary (TWD template Lists sheet; D-PEC-41). */
export const RAIL_V2_ISSUE_TYPES = [
  'Decision', 'Information', 'Clarification', 'Approval',
  'Action', 'Opportunity', 'Risk', 'Resources',
] as const

export const REVISION_STATES = [
  'in_work', 'in_check', 'check_accepted', 'ready_for_approval',
  'approved', 'issued', 'returned_with_comments', 'superseded',
] as const
export type RevisionState = (typeof REVISION_STATES)[number]

export interface Revision {
  id: number
  projectId: number
  deliverableId: number
  revCode: string
  state: RevisionState
  createdAt: string
  createdBy: number
  supersededByRevisionId: number | null
  version: number
}

// ---------- intake ----------

export const INTAKE_STATES = ['raised', 'in_triage', 'dispositioned'] as const
export type IntakeState = (typeof INTAKE_STATES)[number]

export const INTAKE_DISPOSITIONS = ['converted', 'merged', 'duplicate', 'rejected', 'parked'] as const
export type IntakeDisposition = (typeof INTAKE_DISPOSITIONS)[number]

/** PEC-AHL-003 quick types: daily-habit Needs + Risks of Change + action, hold, interface. */
export const INTAKE_QUICK_TYPES = [
  'need_information', 'need_decision', 'need_approval', 'need_resource',
  'risk_budget', 'risk_scope', 'risk_schedule',
  'action', 'hold', 'interface',
] as const
export type IntakeQuickType = (typeof INTAKE_QUICK_TYPES)[number]

export interface IntakeItem {
  id: number
  projectId: number
  ref: string
  statementVerbatim: string
  quickType: IntakeQuickType
  anchorSuggestion: string | null
  needBy: string | null
  suggestedOwnerId: number | null
  log: Log
  raisedBy: number
  raisedAt: string
  state: IntakeState
  disposition: IntakeDisposition | null
  dispositionNote: string | null
  mergedIntoIntakeId: number | null
  /** source-log area context (§16 rail optional column, D-PEC-23) */
  area: string | null
  version: number
}

// ---------- work ----------

export const WORK_ITEM_STATES = ['open', 'in_work', 'closed', 'cancelled'] as const
export type WorkItemState = (typeof WORK_ITEM_STATES)[number]

export const WORK_ITEM_KINDS = ['action', 'coordination', 'risk_treatment', 'rework', 'other'] as const
export type WorkItemKind = (typeof WORK_ITEM_KINDS)[number]

export const NEEDS_AUDIENCES = ['internal', 'client'] as const
export type NeedsAudience = (typeof NEEDS_AUDIENCES)[number]

export interface WorkItem {
  id: number
  projectId: number
  ref: string
  title: string
  statement: string | null
  kind: WorkItemKind
  log: Log
  anchorType: AnchorType
  anchorId: number
  packageId: number | null // derived from anchor at write time
  ownerId: number
  needBy: string | null
  priority: string | null
  priorityProvenance: string | null
  state: WorkItemState
  committedWeek: string | null // ISO week 'YYYY-Www' (PEC-MW-007)
  /** who set committedWeek: the owner's manual flag or the weekly planning commit (PEC-PLAN-007) */
  commitSource: 'manual' | 'plan' | null
  sourceType: RecordType | null
  sourceId: number | null
  closingStatement: string | null
  closedBy: number | null
  closedAt: string | null
  cancelReason: string | null
  /** source-log area context (§16 rail optional column, D-PEC-23) */
  area: string | null
  /** Explicit imported needs-side classification (D-PEC-47); null means unclassified, never inferred. */
  needsAudience: NeedsAudience | null
  /** attested responsible discipline/function, verbatim from RAIL v2 (D-PEC-41) */
  responsibleParty: string | null
  /** attested RAIL v2 issue type, verbatim (D-PEC-41) */
  sourceIssueType: string | null
  /** full-fidelity capture of unmapped source columns, verbatim JSON (D-PEC-41) */
  sourcePayload: Record<string, string> | null
  createdBy: number
  createdAt: string
  version: number
}

// ---------- holds ----------

export const HOLD_STATES = ['active', 'resolved', 'withdrawn'] as const
export type HoldState = (typeof HOLD_STATES)[number]

/** I-3 typed causes. */
export const HOLD_CAUSES = [
  'information', 'decision', 'approval', 'resource',
  'client_input', 'interface', 'vendor_data', 'other',
] as const
export type HoldCause = (typeof HOLD_CAUSES)[number]

export const HOLD_RESOLUTION_KINDS = [
  'decision_recorded', 'information_received', 'resource_assigned', 'approval_recorded', 'other',
] as const
export type HoldResolutionKind = (typeof HOLD_RESOLUTION_KINDS)[number]

export interface Hold {
  id: number
  projectId: number
  ref: string
  title: string
  cause: HoldCause
  statement: string | null
  ownerId: number
  needBy: string | null
  raisedBy: number
  raisedAt: string
  state: HoldState
  resolutionKind: HoldResolutionKind | null
  resolutionNote: string | null
  resolvedAt: string | null
  resolvingRefType: RecordType | null
  resolvingRefId: number | null
  log: Log
  /** Explicit imported needs-side classification (D-PEC-47); null means unclassified, never inferred. */
  needsAudience: NeedsAudience | null
  version: number
}

export const HOLD_TARGET_TYPES = [
  'work_item', 'revision', 'deliverable', 'condition', 'issue_event',
  'interface_item', 'decision', 'approval_record', 'check', 'risk',
] as const
export type HoldTargetType = (typeof HOLD_TARGET_TYPES)[number]

export interface HoldLink {
  id: number
  holdId: number
  targetType: HoldTargetType
  targetId: number
}

// ---------- checking ----------

export const CHECK_STATES = [
  'open', 'in_check', 'comments_open', 'comments_closed', 'accepted', 'reopened',
] as const
export type CheckState = (typeof CHECK_STATES)[number]

export interface ChecklistItem {
  text: string
  category: string | null
  done: boolean
  note: string | null
}

export interface Check {
  id: number
  projectId: number
  ref: string
  revisionId: number
  checkerId: number
  templateId: number | null
  state: CheckState
  checklist: ChecklistItem[]
  acceptedAt: string | null
  independenceWarning: boolean // PEC-CHK-004: warn when checker == revision owner (P1)
  reopenReason: string | null
  createdAt: string
  version: number
}

export const COMMENT_DISPOSITIONS = ['open', 'responded', 'accepted_closed', 'reopened'] as const
export type CommentDisposition = (typeof COMMENT_DISPOSITIONS)[number]

export interface ReviewComment {
  id: number
  projectId: number
  ref: string
  /** parent check (OM-5); null for client-return comment sheets attached to the revision (D-10) */
  checkId: number | null
  /** set when the comment attaches directly to a revision (client return, D-10) */
  revisionId: number | null
  originatorId: number
  responderId: number
  text: string
  response: string | null
  disposition: CommentDisposition
  closureEvidenceId: number | null
  log: Log
  createdAt: string
  version: number
}

/** A comment counts against closure unless individually accepted by the checker (PEC-CHK-002/003). */
export function commentIsOpen(c: ReviewComment): boolean {
  return c.disposition !== 'accepted_closed'
}

// ---------- approval & decisions ----------

export const APPROVAL_STATES = [
  'required', 'prereqs_incomplete', 'ready', 'decided', 'superseded',
] as const
export type ApprovalState = (typeof APPROVAL_STATES)[number]

export interface ApprovalRecord {
  id: number
  projectId: number
  ref: string
  title: string
  approvalType: string
  authoritySource: string | null // why approval is required (basis, PRD §12.7)
  appliesToType: RecordType
  appliesToId: number
  authorityHolder: string | null
  requiredDecisionType: string | null
  signatoryIds: number[] // named signatories, P1 (D-12)
  basisRef: string | null
  dueDate: string | null
  holdPoint: boolean
  state: ApprovalState
  outcomeDecisionId: number | null
  supersededById: number | null
  readyAt: string | null // for approval-latency signal
  createdAt: string
  version: number
}

export const DECISION_STATES = [
  'identified', 'in_progress', 'pending', 'decided', 'superseded',
] as const
export type DecisionState = (typeof DECISION_STATES)[number]

/** PEC-DEC-003 outcome vocabulary. */
export const DECISION_OUTCOMES = [
  'select', 'approve', 'reject', 'defer', 'conditionally_accept',
  'confirm_basis', 'waive', 'supersede',
] as const
export type DecisionOutcome = (typeof DECISION_OUTCOMES)[number]

export const DECISION_KINDS = ['standalone', 'approval_outcome', 'waiver'] as const
export type DecisionKind = (typeof DECISION_KINDS)[number]

export interface Decision {
  id: number
  projectId: number
  ref: string
  title: string
  statement: string
  preparerId: number | null
  authorityId: number
  needBy: string | null
  state: DecisionState
  outcome: DecisionOutcome | null
  rationale: string | null
  optionsConsidered: string | null
  recommendation: string | null
  decidedAt: string | null
  decidedBy: number | null
  kind: DecisionKind
  approvalRecordId: number | null // when kind=approval_outcome (OM-6)
  conditionId: number | null // when kind=waiver (I-8)
  supersededById: number | null
  packageId: number | null // decisions tracked at package level (PRD §4.2)
  log: Log
  /** date the decision was opened in the source log (§16 optional column, D-PEC-23) */
  openDate: string | null // YYYY-MM-DD
  /** project area context (§16 optional column, D-PEC-23) */
  area: string | null
  /** where the decision arose, e.g. a workshop or the client RAIL (§16 optional column, D-PEC-23) */
  source: string | null
  createdAt: string
  version: number
}

export const DECISION_LINK_RELATIONS = ['affects', 'blocks', 'follow_up', 'supersedes'] as const
export type DecisionLinkRelation = (typeof DECISION_LINK_RELATIONS)[number]

export interface DecisionLink {
  id: number
  decisionId: number
  recordType: RecordType
  recordId: number
  relation: DecisionLinkRelation
}

// ---------- registers ----------

export const RISK_STATES = ['open', 'mitigating', 'closed'] as const
export type RiskState = (typeof RISK_STATES)[number]

export interface Risk {
  id: number
  projectId: number
  ref: string
  title: string
  cause: string | null
  consequence: string | null
  packageId: number | null
  deliverableId: number | null
  ownerId: number | null
  probability: number | null // 1-5
  impact: number | null // 1-5
  mitigation: string | null
  needBy: string | null
  state: RiskState
  /** risk-log classification (§16 optional columns, D-PEC-23) */
  category: string | null
  riskType: string | null
  treatment: string | null
  /** post-mitigation residual scoring pair (§16 optional columns, D-PEC-23) */
  residualProbability: number | null // 1-5
  residualImpact: number | null // 1-5
  version: number
}

export const INTERFACE_STATES = ['open', 'agreed', 'delivered', 'closed', 'cancelled'] as const
export type InterfaceState = (typeof INTERFACE_STATES)[number]

export interface InterfaceItem {
  id: number
  projectId: number
  ref: string
  title: string
  givingParty: string
  receivingParty: string
  givingPackageId: number | null
  receivingPackageId: number | null
  requiredInfo: string | null
  needBy: string | null
  state: InterfaceState
  log: Log
  version: number
}

// ---------- conditions (§9) ----------

export const CONDITION_TYPES = [
  'check', 'decision', 'approval', 'evidence', 'interface',
  'document_control', 'resource', 'other',
] as const
export type ConditionType = (typeof CONDITION_TYPES)[number]

export const CONDITION_STATES = ['open', 'satisfied', 'waived', 'superseded'] as const
export type ConditionState = (typeof CONDITION_STATES)[number]

export const CONDITION_SEVERITIES = ['hard', 'warn'] as const
export type ConditionSeverity = (typeof CONDITION_SEVERITIES)[number]

export const CONDITION_SOURCES = ['template', 'checklist', 'decision', 'manual', 'route'] as const
export type ConditionSource = (typeof CONDITION_SOURCES)[number]

/** Transitions that conditions can gate: '<recordType>.<event>' */
export type GatedTransition = string

export interface Condition {
  id: number
  projectId: number
  ref: string
  parentType: RecordType
  parentId: number
  gatedTransition: GatedTransition // e.g. 'revision.issue', 'work_item.close', 'approval_record.ready'
  type: ConditionType
  description: string
  requiredRefType: RecordType | null // pinned satisfier, optional
  requiredRefId: number | null
  requiredArtifactName: string | null // evidence-type conditions
  source: ConditionSource
  sourceRef: string | null
  severity: ConditionSeverity
  ownerId: number | null
  needBy: string | null
  state: ConditionState
  satisfiedByType: RecordType | null
  satisfiedById: number | null
  satisfiedAt: string | null
  waiverDecisionId: number | null
  version: number
}

export interface ConditionTemplate {
  id: number
  projectId: number
  name: string
  deliverableType: string | null // null = any
  issuePurpose: string | null
  packageId: number | null
  transition: GatedTransition
  type: ConditionType
  severity: ConditionSeverity
  description: string
  requiredArtifactName: string | null
}

// ---------- document control ----------

export interface IssueEvent {
  id: number
  projectId: number
  ref: string
  revisionId: number
  purpose: string // configurable labels (D-07); defaults IFR/IFA/IFC/other
  transmittalRef: string
  recipients: string[]
  issuedAt: string
  issuedBy: number
  approvalRecordIds: number[]
  decisionIds: number[]
  archiveRef: string | null // P1 chain (PEC-ARC-002)
  version: number
}

export interface Evidence {
  id: number
  projectId: number
  recordType: RecordType
  recordId: number
  kind: 'attachment' | 'markup' | 'comment_sheet' | 'transmittal' | 'basis_ref' | 'link' | 'note'
  label: string
  urlOrPath: string | null
  content: string | null
  addedBy: number
  addedAt: string
}

export interface BasisReference {
  id: number
  projectId: number
  recordType: RecordType
  recordId: number
  basisKind: 'DBM' | 'SOW' | 'data_sheet' | 'standard' | 'client_direction' | 'other'
  reference: string
  note: string | null
  state: 'active' | 'superseded'
  supersededById: number | null
}

// ---------- history / audit / notifications ----------

export interface HistoryEntry {
  id: number
  projectId: number
  recordType: RecordType
  recordId: number
  at: string
  actorId: number
  kind: string // created | transition | transition_blocked | progress | field_change | ...
  summary: string
  payload: unknown
  authorityRef: string | null
}

export interface AuditEvent {
  id: number
  projectId: number
  at: string
  actorId: number
  action: string // approval_outcome | issue | waiver | permission_change | config_change
  recordType: RecordType
  recordId: number
  priorValue: unknown
  newValue: unknown
  authorityRef: string | null
}

/** PEC-NOT-001 event catalog; P2 adds the weekly-commit, plan-review, and digest events (PEC-NOT-002). */
export const NOTIFICATION_EVENTS = [
  'assigned', 'item_overdue', 'hold_blocks_your_record', 'decision_past_need_by',
  'approval_requires_you', 'check_requires_you', 'comment_requires_you',
  'raised_item_routed', 'raised_item_updated', 'raised_item_closed',
  'revision_ready_for_check', 'revision_ready_for_approval',
  'basis_superseded', 'hold_resolved_unblocked', 'condition_warn',
  'week_committed', 'plan_shift_review',
  'digest_planning', 'digest_package_review', 'digest_judgments', 'digest_holds', 'digest_comments',
] as const
export type NotificationEvent = (typeof NOTIFICATION_EVENTS)[number]

/** PEC-NOT-003: §8.4 escalation thresholds drive notification severity. */
export const NOTIFICATION_SEVERITIES = ['info', 'warn', 'red'] as const
export type NotificationSeverity = (typeof NOTIFICATION_SEVERITIES)[number]

export interface Notification {
  id: number
  projectId: number
  personId: number
  at: string
  event: NotificationEvent
  recordType: RecordType
  recordId: number
  recordRef: string
  reason: string
  nextAction: string
  due: string | null
  severity: NotificationSeverity
  readAt: string | null
}

// ---------- planning & capacity (P2 — PRD §12.4, §13.1) ----------

/** What may be placed on the plan and load capacity: work, checking, approving (I-9). */
export const PLAN_ITEM_TYPES = ['work_item', 'check', 'approval_record'] as const
export type PlanItemType = (typeof PLAN_ITEM_TYPES)[number]

export const PLAN_HORIZONS = ['now', 'next', 'later'] as const
export type PlanHorizon = (typeof PLAN_HORIZONS)[number]

/** One record's placement on the plan (the §13.1 Commitment entity). One placement per record. */
export interface PlanItem {
  id: number
  projectId: number
  ref: string
  itemType: PlanItemType
  itemId: number
  horizon: PlanHorizon
  /** ISO week 'YYYY-Www'; required for 'now'/'next', null for 'later' (backlog) */
  week: string | null
  /** capacity discipline this placement loads — snapshotted from the responsible person, editable (ADR-013) */
  discipline: string | null
  plannedHours: number
  createdBy: number
  createdAt: string
  version: number
}

export const PLAN_PERIOD_STATES = ['open', 'committed'] as const
export type PlanPeriodState = (typeof PLAN_PERIOD_STATES)[number]

/** A planning week; committing it generates the My Week sets (PEC-PLAN-007). */
export interface PlanPeriod {
  id: number
  projectId: number
  week: string // 'YYYY-Www'
  state: PlanPeriodState
  committedAt: string | null
  committedBy: number | null
  version: number
}

/** Available hours per discipline per week (PEC-PLAN-003). */
export interface CapacityEntry {
  id: number
  projectId: number
  week: string
  discipline: string
  hours: number
  version: number
}

/** Schedule row classification from the source export (§16 optional column, D-PEC-23);
 *  unrecognized values reject the row. */
export const SCHEDULE_ROW_TYPES = ['task', 'summary', 'milestone'] as const
export type ScheduleRowType = (typeof SCHEDULE_ROW_TYPES)[number]

/** Imported schedule row feeding the lookahead (§16 P2, D-04). */
export interface ScheduleActivity {
  id: number
  projectId: number
  activityId: string
  description: string
  startDate: string // YYYY-MM-DD
  finishDate: string
  packageId: number | null
  deliverableId: number | null
  /** WBS shape from the source schedule export (§16 optional columns, D-PEC-23) */
  rowType: ScheduleRowType | null
  outlineLevel: number | null
  parentActivityId: string | null
  percentComplete: number | null // 0-100
  durationDays: number | null
  baselineStart: string | null // YYYY-MM-DD
  baselineFinish: string | null // YYYY-MM-DD
  version: number
}

/** Procurement-stage vocabulary of the §16 tracker contract (D-PEC-13); unrecognized values reject the row. */
export const TRACKER_STAGE_STATES = [
  'not_started', 'in_progress', 'complete', 'issued', 'not_applicable',
] as const
export type TrackerStageState = (typeof TRACKER_STAGE_STATES)[number]

/** Imported Package Tracker row (§16 tracker contract, D-PEC-13 as amended). Import-owned:
 *  no in-app edit path. One row per package — the resolved package is the idempotency key. */
export interface PackageTracker {
  id: number
  projectId: number
  trackingNo: string | null // CoA number, kept verbatim; plain data, NOT the key (owner amendment)
  packageName: string
  discipline: string | null
  area: string | null
  packageTypeApproved: string | null
  packageTypeProposed: string | null
  lineItems: string | null
  vendorsEngaged: string | null
  vendorAwarded: string | null
  expectedDeliveryDate: string | null // YYYY-MM-DD
  costEstimateCad: string | null
  comments: string | null
  stageBudgetaryDatasheet: TrackerStageState | null
  stageCostEstimate: TrackerStageState | null
  stagePackageDatasheet: TrackerStageState | null
  stagePackage: TrackerStageState | null
  stageRfq: TrackerStageState | null
  stageReview: TrackerStageState | null
  stageVendorBids: TrackerStageState | null
  stageClarifications: TrackerStageState | null
  stageEvaluation: TrackerStageState | null
  stageEngReq: TrackerStageState | null
  stagePo: TrackerStageState | null
  stageDatabook: TrackerStageState | null
  packageId: number // the resolved package — the §16 idempotency key (owner amendment)
  version: number
}

export const PLAN_SHIFT_STATES = ['applied', 'proposed', 'rejected'] as const
export type PlanShiftState = (typeof PLAN_SHIFT_STATES)[number]

/** The plan-change log: every move records its reason (PEC-PLAN-005/006/008). */
export interface PlanShift {
  id: number
  projectId: number
  ref: string
  planItemId: number
  fromHorizon: PlanHorizon
  toHorizon: PlanHorizon
  fromWeek: string | null
  toWeek: string | null
  reason: string
  impactStatement: string | null
  /** impacts cross packages → requires review by affected leads (PEC-PLAN-005) */
  crossPackage: boolean
  affectedPackageIds: number[]
  state: PlanShiftState
  createdBy: number
  createdAt: string
  reviewedBy: number | null
  reviewedAt: string | null
  version: number
}

/** Links a shift to the conditions/holds/risks/schedule activities it affects (PEC-PLAN-008). */
export interface PlanShiftLink {
  id: number
  planShiftId: number
  recordType: RecordType
  recordId: number
}

/** Old basis → replacement, with the affected-record set (PEC-AUTH-005; §13.1 P2 link, P3 propagation). */
export interface SupersessionLink {
  id: number
  projectId: number
  recordType: 'approval_record' | 'decision' | 'revision' | 'basis_reference'
  oldId: number
  newId: number | null
  affected: Array<{ recordType: RecordType; id: number; ref: string }>
  createdBy: number
  createdAt: string
}

// ---------- snapshot ----------

/** Everything derived status needs for one project, loaded once per request (ADR-004). */
export interface ProjectSnapshot {
  project: Project
  packages: Package[]
  deliverables: Deliverable[]
  revisions: Revision[]
  workItems: WorkItem[]
  holds: Hold[]
  holdLinks: HoldLink[]
  checks: Check[]
  reviewComments: ReviewComment[]
  approvalRecords: ApprovalRecord[]
  decisions: Decision[]
  decisionLinks: DecisionLink[]
  risks: Risk[]
  interfaces: InterfaceItem[]
  intakeItems: IntakeItem[]
  conditions: Condition[]
  issueEvents: IssueEvent[]
  evidence: Evidence[]
  // P2 planning & capacity (PRD §13.1)
  planItems: PlanItem[]
  planPeriods: PlanPeriod[]
  capacityEntries: CapacityEntry[]
  scheduleActivities: ScheduleActivity[]
  planShifts: PlanShift[]
  /** today's local date in the project timezone, YYYY-MM-DD */
  today: string
}
