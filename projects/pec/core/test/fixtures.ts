/** Snapshot fixture builders for core tests. */

import type {
  ApprovalRecord, Check, Condition, Decision, Deliverable, Evidence, Hold, HoldLink,
  IntakeItem, InterfaceItem, Package, Project, ProjectSnapshot, ReviewComment, Revision,
  Risk, WorkItem,
} from '../src/types.ts'
import { DEFAULT_THRESHOLDS } from '../src/types.ts'

let nextId = 1000
export function id(): number { return ++nextId }

export const TODAY = '2026-07-15' // a Wednesday
export const TZ = 'UTC'

export function project(over: Partial<Project> = {}): Project {
  return {
    id: 1, code: 'PRJ', name: 'Test Project',
    calendar: { timezone: TZ, weekendDays: ['Sat', 'Sun'], holidays: [] },
    thresholds: { ...DEFAULT_THRESHOLDS },
    config: {
      holdCauses: [], issuePurposes: ['IFR', 'IFA', 'IFC'],
      logVisibility: {}, waiverRoles: {}, allowAnyoneRaiseIntake: true,
    },
    version: 1,
    ...over,
  }
}

export function snapshot(over: Partial<ProjectSnapshot> = {}): ProjectSnapshot {
  return {
    project: project(), packages: [], deliverables: [], revisions: [], workItems: [],
    holds: [], holdLinks: [], checks: [], reviewComments: [], approvalRecords: [],
    decisions: [], decisionLinks: [], risks: [], interfaces: [], intakeItems: [],
    conditions: [], issueEvents: [], evidence: [], today: TODAY,
    ...over,
  }
}

export function pkg(over: Partial<Package> = {}): Package {
  const n = id()
  return { id: n, projectId: 1, code: `PKG-${n}`, name: 'Package', leadId: null, description: null, milestone: null, version: 1, ...over }
}

export function deliverable(over: Partial<Deliverable> = {}): Deliverable {
  const n = id()
  return {
    id: n, projectId: 1, packageId: 0, docNo: `DOC-${n}`, title: 'Deliverable',
    discipline: null, deliverableType: null, ownerId: null, dcRef: null, clientNo: null,
    milestone: null, dueDate: null, issuePurposePlan: null, remarks: null, version: 1, ...over,
  }
}

export function revision(over: Partial<Revision> = {}): Revision {
  const n = id()
  return {
    id: n, projectId: 1, deliverableId: 0, revCode: 'A', state: 'in_work',
    createdAt: '2026-07-01T00:00:00Z', createdBy: 1, supersededByRevisionId: null, version: 1, ...over,
  }
}

export function workItem(over: Partial<WorkItem> = {}): WorkItem {
  const n = id()
  return {
    id: n, projectId: 1, ref: `WI-${n}`, title: 'Work item', statement: null, kind: 'action',
    log: 'internal', anchorType: 'deliverable', anchorId: 0, packageId: null, ownerId: 1,
    needBy: null, priority: null, priorityProvenance: null, state: 'open', committedWeek: null,
    sourceType: null, sourceId: null, closingStatement: null, closedBy: null, closedAt: null,
    cancelReason: null, createdBy: 1, createdAt: '2026-07-01T00:00:00Z', version: 1, ...over,
  }
}

export function hold(over: Partial<Hold> = {}): Hold {
  const n = id()
  return {
    id: n, projectId: 1, ref: `HLD-${n}`, title: 'Hold', cause: 'information', statement: null,
    ownerId: 1, needBy: null, raisedBy: 1, raisedAt: '2026-07-10T00:00:00Z', state: 'active',
    resolutionKind: null, resolutionNote: null, resolvedAt: null, resolvingRefType: null,
    resolvingRefId: null, log: 'internal', version: 1, ...over,
  }
}

export function holdLink(over: Partial<HoldLink> & Pick<HoldLink, 'holdId' | 'targetType' | 'targetId'>): HoldLink {
  return { id: id(), ...over }
}

export function check(over: Partial<Check> = {}): Check {
  const n = id()
  return {
    id: n, projectId: 1, ref: `CHK-${n}`, revisionId: 0, checkerId: 2, templateId: null,
    state: 'open', checklist: [], acceptedAt: null, independenceWarning: false,
    reopenReason: null, createdAt: '2026-07-05T00:00:00Z', version: 1, ...over,
  }
}

export function comment(over: Partial<ReviewComment> = {}): ReviewComment {
  const n = id()
  return {
    id: n, projectId: 1, ref: `CMT-${n}`, checkId: 0, revisionId: null, originatorId: 2, responderId: 1,
    text: 'Comment', response: null, disposition: 'open', closureEvidenceId: null,
    log: 'internal', createdAt: '2026-07-05T00:00:00Z', version: 1, ...over,
  }
}

export function approval(over: Partial<ApprovalRecord> = {}): ApprovalRecord {
  const n = id()
  return {
    id: n, projectId: 1, ref: `APR-${n}`, title: 'Approval', approvalType: 'issue_authorization',
    authoritySource: 'contract', appliesToType: 'revision', appliesToId: 0, authorityHolder: null,
    requiredDecisionType: 'approve', signatoryIds: [3], basisRef: null, dueDate: null,
    holdPoint: false, state: 'required', outcomeDecisionId: null, supersededById: null,
    readyAt: null, createdAt: '2026-07-01T00:00:00Z', version: 1, ...over,
  }
}

export function decision(over: Partial<Decision> = {}): Decision {
  const n = id()
  return {
    id: n, projectId: 1, ref: `DEC-${n}`, title: 'Decision', statement: 'Decide',
    preparerId: null, authorityId: 3, needBy: null, state: 'identified', outcome: null,
    rationale: null, optionsConsidered: null, recommendation: null, decidedAt: null,
    decidedBy: null, kind: 'standalone', approvalRecordId: null, conditionId: null,
    supersededById: null, packageId: null, log: 'internal',
    createdAt: '2026-07-01T00:00:00Z', version: 1, ...over,
  }
}

export function condition(over: Partial<Condition> = {}): Condition {
  const n = id()
  return {
    id: n, projectId: 1, ref: `COND-${n}`, parentType: 'revision', parentId: 0,
    gatedTransition: 'revision.issue', type: 'check', description: 'Condition',
    requiredRefType: null, requiredRefId: null, requiredArtifactName: null,
    source: 'template', sourceRef: null, severity: 'hard', ownerId: null, needBy: null,
    state: 'open', satisfiedByType: null, satisfiedById: null, satisfiedAt: null,
    waiverDecisionId: null, version: 1, ...over,
  }
}

export function risk(over: Partial<Risk> = {}): Risk {
  const n = id()
  return {
    id: n, projectId: 1, ref: `RSK-${n}`, title: 'Risk', cause: null, consequence: null,
    packageId: null, deliverableId: null, ownerId: null, probability: null, impact: null,
    mitigation: null, needBy: null, state: 'open', version: 1, ...over,
  }
}

export function interfaceItem(over: Partial<InterfaceItem> = {}): InterfaceItem {
  const n = id()
  return {
    id: n, projectId: 1, ref: `INT-${n}`, title: 'Interface', givingParty: 'A', receivingParty: 'B',
    givingPackageId: null, receivingPackageId: null, requiredInfo: null, needBy: null,
    state: 'open', log: 'internal', version: 1, ...over,
  }
}

export function intake(over: Partial<IntakeItem> = {}): IntakeItem {
  const n = id()
  return {
    id: n, projectId: 1, ref: `INTK-${n}`, statementVerbatim: 'Concern as raised',
    quickType: 'action', anchorSuggestion: null, needBy: null, suggestedOwnerId: null,
    log: 'internal', raisedBy: 1, raisedAt: '2026-07-10T00:00:00Z', state: 'raised',
    disposition: null, dispositionNote: null, mergedIntoIntakeId: null, version: 1, ...over,
  }
}

export function evidence(over: Partial<Evidence> = {}): Evidence {
  const n = id()
  return {
    id: n, projectId: 1, recordType: 'revision', recordId: 0, kind: 'attachment',
    label: 'artifact', urlOrPath: null, content: null, addedBy: 1,
    addedAt: '2026-07-10T00:00:00Z', ...over,
  }
}
