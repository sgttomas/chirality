/**
 * The seven controlled lifecycles (PRD §7, SPEC §4) as data (ADR-006).
 *
 * The server executes these tables; the UI reads offered transitions from the API;
 * tests enumerate them exhaustively. "Blocked" is never a state here — it is the
 * derived hold overlay (OM-2), which vetoes transitions marked `holdVeto`.
 */

export const LIFECYCLE_RECORDS = [
  'intake_item', 'work_item', 'hold', 'check', 'approval_record', 'decision', 'revision',
] as const
export type LifecycleRecord = (typeof LIFECYCLE_RECORDS)[number]

export interface TransitionDef {
  record: LifecycleRecord
  event: string
  from: string[]
  to: string
  /** permission action key (core/src/permissions.ts) the actor must hold */
  permission: string
  /** conditions-engine gate evaluated on this transition (SPEC §5), or null */
  gate: string | null
  /** an active hold linked to the record vetoes this transition */
  holdVeto: boolean
  /** system-driven: not directly invokable by a user event */
  auto: boolean
  /** named server-side preconditions beyond conditions/holds */
  requires: string[]
  /** documented side effects the server must implement */
  sideEffects: string[]
}

function t(def: TransitionDef): TransitionDef {
  return def
}

export const TRANSITIONS: TransitionDef[] = [
  // ---------- Intake Item (§7.1) ----------
  t({
    record: 'intake_item', event: 'open_triage', from: ['raised'], to: 'in_triage',
    permission: 'intake.triage', gate: null, holdVeto: false, auto: false, requires: [],
    sideEffects: [],
  }),
  t({
    record: 'intake_item', event: 'disposition', from: ['in_triage'], to: 'dispositioned',
    permission: 'intake.triage', gate: null, holdVeto: false, auto: false,
    requires: ['disposition_recorded'], // enum + note; converted → records created atomically
    sideEffects: ['create_converted_records', 'notify_raiser_routed'],
  }),

  // ---------- Work Item (§7.2) ----------
  t({
    record: 'work_item', event: 'start', from: ['open'], to: 'in_work',
    permission: 'work_item.transition', gate: null, holdVeto: false, auto: false, requires: [],
    sideEffects: [],
  }),
  t({
    record: 'work_item', event: 'pause', from: ['in_work'], to: 'open',
    permission: 'work_item.transition', gate: null, holdVeto: false, auto: false, requires: [],
    sideEffects: [],
  }),
  t({
    record: 'work_item', event: 'close', from: ['open', 'in_work'], to: 'closed',
    permission: 'work_item.transition', gate: 'work_item.close', holdVeto: true, auto: false,
    requires: [], // closing statement requirement carried by evidence-type conditions where templated
    sideEffects: ['satisfy_matching_conditions', 'notify_raiser_closed'],
  }),
  t({
    record: 'work_item', event: 'cancel', from: ['open', 'in_work'], to: 'cancelled',
    permission: 'work_item.cancel', gate: null, holdVeto: false, auto: false,
    requires: ['reason'],
    sideEffects: ['notify_raiser_closed'],
  }),
  t({
    record: 'work_item', event: 'reopen', from: ['closed'], to: 'open',
    permission: 'work_item.transition', gate: null, holdVeto: false, auto: false,
    requires: ['reason'], // checker rejection or supersession (§7.2)
    sideEffects: ['unsatisfy_dependent_conditions'],
  }),

  // ---------- Hold (§7.3) ----------
  t({
    record: 'hold', event: 'resolve', from: ['active'], to: 'resolved',
    permission: 'hold.resolve', gate: null, holdVeto: false, auto: false,
    requires: ['resolution_kind'],
    sideEffects: ['notify_unblocked_owners'],
  }),
  t({
    record: 'hold', event: 'withdraw', from: ['active'], to: 'withdrawn',
    permission: 'hold.resolve', gate: null, holdVeto: false, auto: false,
    requires: ['reason'],
    sideEffects: ['notify_unblocked_owners'],
  }),

  // ---------- Check (§7.4) ----------
  t({
    record: 'check', event: 'start', from: ['open'], to: 'in_check',
    permission: 'check.work', gate: null, holdVeto: false, auto: false, requires: [],
    sideEffects: [],
  }),
  t({
    record: 'check', event: 'comments_opened', from: ['in_check'], to: 'comments_open',
    permission: 'check.work', gate: null, holdVeto: false, auto: true,
    requires: ['has_open_comment'], sideEffects: [],
  }),
  t({
    record: 'check', event: 'comments_closed', from: ['comments_open'], to: 'comments_closed',
    permission: 'check.work', gate: null, holdVeto: false, auto: true,
    requires: ['no_open_comment'], sideEffects: [],
  }),
  t({
    record: 'check', event: 'reopen_comments', from: ['comments_closed'], to: 'in_check',
    permission: 'comment.accept', gate: null, holdVeto: false, auto: false,
    requires: [], sideEffects: [],
  }),
  t({
    record: 'check', event: 'accept', from: ['in_check', 'comments_closed'], to: 'accepted',
    permission: 'check.accept', gate: null, holdVeto: true, auto: false,
    // Three distinct facts (PEC-CHK-003): acceptance requires zero open comments; incomplete
    // checklist items do not block but are listed in the acceptance history entry.
    requires: ['no_open_comment'],
    sideEffects: ['satisfy_check_conditions', 'sync_revision_state', 'notify_revision_owner', 'record_incomplete_checklist'],
  }),
  t({
    record: 'check', event: 'reopen', from: ['accepted'], to: 'reopened',
    permission: 'check.work', gate: null, holdVeto: false, auto: false,
    requires: ['reason'], // new revision or supersession (§7.4)
    sideEffects: ['unsatisfy_check_conditions', 'sync_revision_state'],
  }),

  // ---------- Approval Record (§7.5) ----------
  t({
    record: 'approval_record', event: 'prereqs_open', from: ['required'], to: 'prereqs_incomplete',
    permission: 'approval.auto', gate: null, holdVeto: false, auto: true,
    requires: ['has_open_prereq'], sideEffects: [],
  }),
  t({
    record: 'approval_record', event: 'became_ready', from: ['required', 'prereqs_incomplete'], to: 'ready',
    permission: 'approval.auto', gate: 'approval_record.ready', holdVeto: true, auto: true,
    requires: [],
    sideEffects: ['stamp_ready_at', 'notify_signatories', 'sync_revision_state'],
  }),
  t({
    record: 'approval_record', event: 'prereqs_reopened', from: ['ready'], to: 'prereqs_incomplete',
    permission: 'approval.auto', gate: null, holdVeto: false, auto: true,
    requires: ['has_open_prereq'], sideEffects: ['clear_ready_at', 'sync_revision_state'],
  }),
  t({
    record: 'approval_record', event: 'record_outcome', from: ['ready'], to: 'decided',
    permission: 'approval.outcome', gate: null, holdVeto: true, auto: false,
    // The ONLY path to decided: creates a Decision (kind=approval_outcome) linked back (OM-6, PEC-AUTH-004).
    requires: ['outcome_decision'],
    sideEffects: ['create_outcome_decision', 'instantiate_outcome_conditions', 'create_rework_items_on_reject',
      'reset_due_on_defer', 'satisfy_approval_conditions', 'sync_revision_state', 'audit_event'],
  }),
  t({
    record: 'approval_record', event: 'supersede', from: ['required', 'prereqs_incomplete', 'ready', 'decided'], to: 'superseded',
    permission: 'approval.supersede', gate: null, holdVeto: false, auto: false,
    requires: ['replacement_link'],
    sideEffects: ['flag_affected_records', 'notify_affected_owners', 'unsatisfy_approval_conditions'],
  }),

  // ---------- Decision (§7.6) ----------
  t({
    record: 'decision', event: 'assign_preparer', from: ['identified'], to: 'in_progress',
    permission: 'decision.progress', gate: null, holdVeto: false, auto: false,
    requires: ['preparer'], sideEffects: [],
  }),
  t({
    record: 'decision', event: 'mark_pending', from: ['in_progress'], to: 'pending',
    permission: 'decision.progress', gate: null, holdVeto: false, auto: false,
    requires: [],
    sideEffects: ['notify_authority'], // appears in blocking views and Waiting-on-you
  }),
  t({
    record: 'decision', event: 'record_outcome', from: ['pending'], to: 'decided',
    permission: 'decision.outcome', gate: null, holdVeto: true, auto: false,
    requires: ['outcome', 'rationale'],
    sideEffects: ['instantiate_outcome_conditions', 'create_follow_up_items',
      'satisfy_decision_conditions', 'notify_affected_owners', 'audit_event_if_waiver_or_approval'],
  }),
  t({
    record: 'decision', event: 'supersede', from: ['decided'], to: 'superseded',
    permission: 'decision.supersede', gate: null, holdVeto: false, auto: false,
    requires: ['replacement_link'],
    sideEffects: ['flag_affected_records', 'notify_affected_owners', 'unsatisfy_decision_conditions'],
  }),

  // ---------- Deliverable Revision (§7.7) ----------
  t({
    record: 'revision', event: 'open_check', from: ['in_work'], to: 'in_check',
    permission: 'revision.transition', gate: null, holdVeto: false, auto: true,
    requires: ['has_check'], sideEffects: [],
  }),
  t({
    record: 'revision', event: 'rework', from: ['in_check', 'check_accepted', 'ready_for_approval'], to: 'in_work',
    permission: 'revision.transition', gate: null, holdVeto: false, auto: false,
    requires: [], // loops are expected, no ceremony (§7.7)
    sideEffects: [],
  }),
  t({
    record: 'revision', event: 'check_accepted', from: ['in_check'], to: 'check_accepted',
    permission: 'revision.auto', gate: null, holdVeto: false, auto: true,
    requires: ['check_accepted'], sideEffects: [],
  }),
  t({
    record: 'revision', event: 'ready_for_approval', from: ['check_accepted'], to: 'ready_for_approval',
    permission: 'revision.auto', gate: null, holdVeto: false, auto: true,
    requires: ['approvals_ready_or_none'], sideEffects: ['notify_signatories'],
  }),
  t({
    record: 'revision', event: 'approved', from: ['ready_for_approval'], to: 'approved',
    permission: 'revision.auto', gate: null, holdVeto: false, auto: true,
    requires: ['approval_outcomes_approved'], sideEffects: [],
  }),
  t({
    record: 'revision', event: 'issue', from: ['approved'], to: 'issued',
    permission: 'issue.record', gate: 'revision.issue', holdVeto: true, auto: false,
    // Recording the issue event IS the transition (SPEC §4.7); hard-gated per D-11.
    requires: ['issue_event_payload'],
    sideEffects: ['create_issue_event', 'archive_ref', 'audit_event', 'satisfy_document_control_conditions'],
  }),
  t({
    record: 'revision', event: 'return_comments', from: ['issued'], to: 'returned_with_comments',
    permission: 'revision.transition', gate: null, holdVeto: false, auto: false,
    requires: [],
    sideEffects: ['log_client_comments'], // D-10: review comments with log=client
  }),
  t({
    record: 'revision', event: 'supersede', from: ['in_work', 'in_check', 'check_accepted', 'ready_for_approval', 'approved', 'issued', 'returned_with_comments'], to: 'superseded',
    permission: 'revision.create', gate: null, holdVeto: false, auto: true,
    requires: ['replacement_revision'], // superseding happens by creating the next revision
    sideEffects: ['chain_link', 'reopen_checks_note', 'notify_owner'],
  }),
]

/** All transitions leaving `state` for a record kind. */
export function transitionsFrom(record: LifecycleRecord, state: string): TransitionDef[] {
  return TRANSITIONS.filter((d) => d.record === record && d.from.includes(state))
}

/** Find a specific transition; undefined when illegal from this state. */
export function findTransition(
  record: LifecycleRecord, event: string, fromState: string,
): TransitionDef | undefined {
  return TRANSITIONS.find(
    (d) => d.record === record && d.event === event && d.from.includes(fromState),
  )
}

/** Every state named by a record's machine (for validation and tests). */
export function statesOf(record: LifecycleRecord): string[] {
  const s = new Set<string>()
  for (const d of TRANSITIONS) {
    if (d.record !== record) continue
    for (const f of d.from) s.add(f)
    s.add(d.to)
  }
  return [...s]
}
