/**
 * Conditions engine (PRD §9, SPEC §5).
 *
 * Pure functions over a ProjectSnapshot. Satisfaction is event-driven in the server
 * (transition side-effects mark conditions satisfied), but the gate here RE-VERIFIES
 * graph-checkable types at evaluation time, so a stale `satisfied` cannot let an
 * issue through after its satisfier was reopened (SPEC §5.3, defense in depth).
 */

import type {
  Condition, ContributingRef, Hold, HoldTargetType, ProjectSnapshot, RecordType,
} from './types.ts'

// ---------- hold overlay (OM-2) ----------

/** Active holds linked to a record: the record's "blocked" overlay. */
export function activeHoldsFor(
  snap: ProjectSnapshot, targetType: HoldTargetType, targetId: number,
): Hold[] {
  const holdById = new Map(snap.holds.map((h) => [h.id, h]))
  const out: Hold[] = []
  for (const link of snap.holdLinks) {
    if (link.targetType !== targetType || link.targetId !== targetId) continue
    const hold = holdById.get(link.holdId)
    if (hold && hold.state === 'active') out.push(hold)
  }
  return out
}

export function isBlocked(snap: ProjectSnapshot, targetType: HoldTargetType, targetId: number): boolean {
  return activeHoldsFor(snap, targetType, targetId).length > 0
}

// ---------- effective condition state ----------

export type EffectiveConditionState =
  | 'satisfied' | 'open' | 'waived' | 'superseded' | 'blocked_by_hold'

export interface ConditionEval {
  condition: Condition
  /** state used for gating and shown in explanations (§5.5) */
  effectiveState: EffectiveConditionState
  /** what satisfies / would satisfy it */
  satisfier: ContributingRef | null
  waiverDecisionRef: string | null
  note: string | null
}

/** Optional evaluation context for facts not yet in the graph (e.g. the issue event being recorded). */
export interface EvalContext {
  pendingIssueEvent?: { transmittalRef?: string; recipients?: string[] }
}

function ref(recordType: RecordType, id: number, refStr: string, why: string): ContributingRef {
  return { recordType, id, ref: refStr, why }
}

/**
 * Recompute a condition's satisfaction from the record graph where the type allows it.
 * Returns null when the graph has no qualifying satisfier (=> effectively open),
 * or a ContributingRef describing the satisfier.
 */
export function graphSatisfier(
  snap: ProjectSnapshot, cond: Condition, ctx?: EvalContext,
): ContributingRef | null {
  switch (cond.type) {
    case 'check': {
      // Pinned check, else any accepted check on the parent revision.
      if (cond.requiredRefType === 'check' && cond.requiredRefId != null) {
        const c = snap.checks.find((x) => x.id === cond.requiredRefId)
        return c && c.state === 'accepted' ? ref('check', c.id, c.ref, 'check accepted') : null
      }
      if (cond.parentType === 'revision') {
        const c = snap.checks.find((x) => x.revisionId === cond.parentId && x.state === 'accepted')
        return c ? ref('check', c.id, c.ref, 'check accepted') : null
      }
      // Prerequisite on an approval record resolves through its appliesTo revision (SPEC §4.5).
      if (cond.parentType === 'approval_record') {
        const a = snap.approvalRecords.find((x) => x.id === cond.parentId)
        if (a && a.appliesToType === 'revision') {
          const c = snap.checks.find((x) => x.revisionId === a.appliesToId && x.state === 'accepted')
          return c ? ref('check', c.id, c.ref, 'check accepted') : null
        }
      }
      return null
    }
    case 'decision': {
      if (cond.requiredRefType === 'decision' && cond.requiredRefId != null) {
        const d = snap.decisions.find((x) => x.id === cond.requiredRefId)
        return d && (d.state === 'decided') ? ref('decision', d.id, d.ref, `decision ${d.outcome ?? 'decided'}`) : null
      }
      // Unpinned fallback: any decided Decision linked to the parent record via decision_link.
      for (const l of snap.decisionLinks) {
        if (l.recordType !== cond.parentType || l.recordId !== cond.parentId) continue
        const d = snap.decisions.find((x) => x.id === l.decisionId)
        if (d && d.state === 'decided') return ref('decision', d.id, d.ref, `decision ${d.outcome ?? 'decided'} (linked)`)
      }
      return null
    }
    case 'approval': {
      const satisfies = (a: (typeof snap.approvalRecords)[number]): ContributingRef | null => {
        if (a.state !== 'decided' || a.outcomeDecisionId == null) return null
        const d = snap.decisions.find((x) => x.id === a.outcomeDecisionId)
        return d && (d.outcome === 'approve' || d.outcome === 'conditionally_accept')
          ? ref('approval_record', a.id, a.ref, `approval outcome: ${d.outcome} (${d.ref})`)
          : null
      }
      if (cond.requiredRefType === 'approval_record' && cond.requiredRefId != null) {
        const a = snap.approvalRecords.find((x) => x.id === cond.requiredRefId)
        return a ? satisfies(a) : null
      }
      // Unpinned fallback: any approval record applying to the parent, decided-approved.
      for (const a of snap.approvalRecords) {
        if (a.appliesToType !== cond.parentType || a.appliesToId !== cond.parentId) continue
        const s = satisfies(a)
        if (s) return s
      }
      return null
    }
    case 'evidence': {
      if (!cond.requiredArtifactName) return null
      const e = snap.evidence.find(
        (x) => x.recordType === cond.parentType && x.recordId === cond.parentId
          && x.label === cond.requiredArtifactName,
      )
      return e ? ref('evidence', e.id, e.label, 'artifact attached') : null
    }
    case 'interface': {
      if (cond.requiredRefType === 'interface_item' && cond.requiredRefId != null) {
        const i = snap.interfaces.find((x) => x.id === cond.requiredRefId)
        return i && (i.state === 'delivered' || i.state === 'closed')
          ? ref('interface_item', i.id, i.ref, `interface ${i.state}`)
          : null
      }
      return null
    }
    case 'document_control': {
      // Transmittal prerequisites live on the issue event being recorded (SPEC §5.3).
      const p = ctx?.pendingIssueEvent
      if (p?.transmittalRef && p.recipients && p.recipients.length > 0) {
        return ref(cond.parentType, cond.parentId, cond.ref, 'transmittal reference and recipients present')
      }
      // Already-issued parents satisfy through their recorded issue event.
      if (cond.parentType === 'revision') {
        const ev = snap.issueEvents.find((x) => x.revisionId === cond.parentId && x.transmittalRef)
        return ev ? ref('issue_event', ev.id, ev.ref, 'issue event recorded') : null
      }
      return null
    }
    case 'resource':
    case 'other':
      // Not graph-checkable: manual satisfaction only (stored state governs).
      return null
  }
}

const GRAPH_CHECKABLE = new Set(['check', 'decision', 'approval', 'evidence', 'interface', 'document_control'])

/** Evaluate one condition to its effective (gating) state. */
export function evaluateCondition(
  snap: ProjectSnapshot, cond: Condition, ctx?: EvalContext,
): ConditionEval {
  const waiverDecision = cond.waiverDecisionId != null
    ? snap.decisions.find((d) => d.id === cond.waiverDecisionId) ?? null
    : null

  // Waived / superseded are judgments and stand as stored (I-8, I-10).
  if (cond.state === 'waived') {
    return {
      condition: cond, effectiveState: 'waived', satisfier: null,
      waiverDecisionRef: waiverDecision?.ref ?? null,
      note: waiverDecision ? `waived by ${waiverDecision.ref}` : 'waived',
    }
  }
  if (cond.state === 'superseded') {
    return { condition: cond, effectiveState: 'superseded', satisfier: null, waiverDecisionRef: null, note: null }
  }

  let satisfier: ContributingRef | null = null
  if (GRAPH_CHECKABLE.has(cond.type)) {
    // Re-verify from the graph regardless of stored state.
    satisfier = graphSatisfier(snap, cond, ctx)
  } else if (cond.state === 'satisfied') {
    satisfier = cond.satisfiedByType != null && cond.satisfiedById != null
      ? ref(cond.satisfiedByType, cond.satisfiedById, cond.ref, 'manually satisfied (recorded)')
      : ref(cond.parentType, cond.parentId, cond.ref, 'manually satisfied (recorded)')
  }

  if (satisfier) {
    return { condition: cond, effectiveState: 'satisfied', satisfier, waiverDecisionRef: null, note: null }
  }

  // Open — annotate when the condition itself is held (display distinction, §5.5).
  const held = activeHoldsFor(snap, 'condition', cond.id)
  if (held.length > 0) {
    const h = held[0]!
    return {
      condition: cond, effectiveState: 'blocked_by_hold', satisfier: null, waiverDecisionRef: null,
      note: `blocked by ${h.ref} (${h.cause})`,
    }
  }
  const staleNote = cond.state === 'satisfied'
    ? 'previously satisfied, but the satisfying record is no longer valid (reopened or superseded)'
    : null
  return { condition: cond, effectiveState: 'open', satisfier: null, waiverDecisionRef: null, note: staleNote }
}

// ---------- transition gate ----------

export interface GateResult {
  permitted: boolean
  /** open (or hold-blocked) HARD conditions preventing the transition */
  hardOpen: ConditionEval[]
  /** open WARN conditions — logged and notified, never blocking (D-11) */
  warnOpen: ConditionEval[]
  /** all conditions on the gate, for the full §5.5 explanation */
  all: ConditionEval[]
  /** active holds vetoing the parent record itself (when the transition is holdVeto) */
  holdVeto: Hold[]
}

function passes(state: EffectiveConditionState): boolean {
  return state === 'satisfied' || state === 'waived' || state === 'superseded'
}

/**
 * Evaluate a gated transition (SPEC §5.4): permitted iff every hard condition attached to
 * (parentType, parentId, gate) passes AND (when vetoed) no active hold links the parent.
 */
export function evaluateGate(
  snap: ProjectSnapshot,
  parentType: RecordType,
  parentId: number,
  gate: string,
  opts?: { holdVeto?: boolean; ctx?: EvalContext },
): GateResult {
  const conds = snap.conditions.filter(
    (c) => c.parentType === parentType && c.parentId === parentId && c.gatedTransition === gate,
  )
  const all = conds.map((c) => evaluateCondition(snap, c, opts?.ctx))
  const hardOpen = all.filter((e) => e.condition.severity === 'hard' && !passes(e.effectiveState))
  const warnOpen = all.filter((e) => e.condition.severity === 'warn' && !passes(e.effectiveState))
  const holdVeto = opts?.holdVeto
    ? activeHoldsFor(snap, parentType as HoldTargetType, parentId)
    : []
  return {
    permitted: hardOpen.length === 0 && holdVeto.length === 0,
    hardOpen, warnOpen, all, holdVeto,
  }
}

/**
 * The "before this issues" explanation (PEC-DEL-004, §5.5): every condition on the
 * transition with state, owner, need-by, and satisfying/waiving record. This same
 * payload backs the deliverable panel, 409 bodies, and tests.
 */
export interface TransitionExplanation {
  gate: string
  permitted: boolean
  holdVeto: Array<{ ref: string; cause: string; title: string; ownerId: number }>
  conditions: Array<{
    ref: string
    description: string
    type: Condition['type']
    severity: Condition['severity']
    state: EffectiveConditionState
    ownerId: number | null
    needBy: string | null
    satisfiedBy: ContributingRef | null
    waiverDecisionRef: string | null
    note: string | null
  }>
}

export function explainTransition(
  snap: ProjectSnapshot,
  parentType: RecordType,
  parentId: number,
  gate: string,
  opts?: { holdVeto?: boolean; ctx?: EvalContext },
): TransitionExplanation {
  const r = evaluateGate(snap, parentType, parentId, gate, opts)
  return {
    gate,
    permitted: r.permitted,
    holdVeto: r.holdVeto.map((h) => ({ ref: h.ref, cause: h.cause, title: h.title, ownerId: h.ownerId })),
    conditions: r.all.map((e) => ({
      ref: e.condition.ref,
      description: e.condition.description,
      type: e.condition.type,
      severity: e.condition.severity,
      state: e.effectiveState,
      ownerId: e.condition.ownerId,
      needBy: e.condition.needBy,
      satisfiedBy: e.satisfier,
      waiverDecisionRef: e.waiverDecisionRef,
      note: e.note,
    })),
  }
}
