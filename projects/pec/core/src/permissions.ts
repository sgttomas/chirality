/**
 * Permission rules (PRD §14, SPEC §2.2). Pure: the server builds a PermissionContext
 * from the session + record, the UI asks through the API. Enforced server-side only
 * (PEC-NFR-005); the client never decides.
 */

import type { ConditionType, Log, Role } from './types.ts'

export type PermissionAction =
  | 'project.read'
  | 'intake.raise' | 'intake.triage'
  | 'work_item.create' | 'work_item.update' | 'work_item.transition' | 'work_item.cancel'
  | 'hold.raise' | 'hold.resolve'
  | 'check.create' | 'check.work' | 'check.accept'
  | 'comment.create' | 'comment.respond' | 'comment.accept'
  | 'approval.create' | 'approval.outcome' | 'approval.supersede' | 'approval.auto'
  | 'decision.create' | 'decision.progress' | 'decision.outcome' | 'decision.supersede'
  | 'condition.create' | 'condition.waive' | 'condition.satisfy_manual'
  | 'revision.create' | 'revision.transition' | 'revision.auto'
  | 'issue.record'
  | 'deliverable.create' | 'deliverable.update'
  | 'risk.create' | 'risk.update'
  | 'interface.create' | 'interface.update'
  | 'evidence.add'
  | 'config.manage'
  | 'import.propose' | 'import.accept'
  | 'plan.manage' | 'plan.commit' | 'plan.propose' | 'plan.review'

export interface PermissionContext {
  roles: Role[]
  isInstanceAdmin: boolean
  /** relational facts about the acting user vs the record */
  isOwner?: boolean
  isChecker?: boolean
  isResponder?: boolean
  isSignatory?: boolean
  isAuthority?: boolean
  isPackageLead?: boolean
  isHoldOwner?: boolean
  isPreparer?: boolean
  /** for condition.waive: the condition's type, resolved against project config */
  conditionType?: ConditionType
  waiverRoles?: Partial<Record<ConditionType, Role[]>>
  allowAnyoneRaiseIntake?: boolean
}

const LEADS: Role[] = ['package_lead', 'discipline_lead', 'engineering_manager', 'pm', 'admin']
const CREATORS: Role[] = ['package_lead', 'discipline_lead', 'engineer_of_record', 'pm', 'coordinator', 'admin']
const DEFAULT_WAIVER: Record<'strict' | 'lead', Role[]> = {
  strict: ['pm', 'engineering_manager', 'admin'],
  lead: ['package_lead', 'pm', 'engineering_manager', 'admin'],
}
const STRICT_WAIVER_TYPES: ConditionType[] = ['check', 'approval', 'decision', 'document_control']

function hasAny(ctx: PermissionContext, roles: Role[]): boolean {
  return ctx.roles.some((r) => roles.includes(r))
}

export interface PermissionResult {
  allowed: boolean
  reason: string
}

/**
 * Judgments that must come from the actual signatory / authority / checker — never
 * from a break-glass admin. Instance admin governs config and taxonomy (PRD §14); it
 * does not get to record an engineering judgment as itself and call it the authority's
 * (I-6: the system never hides which of check/approve/decide is outstanding, and by whom).
 */
const PERSONAL_JUDGMENTS: PermissionAction[] = [
  'approval.outcome', 'decision.outcome', 'check.accept', 'comment.accept',
]

export function can(action: PermissionAction, ctx: PermissionContext): PermissionResult {
  const yes = (reason: string): PermissionResult => ({ allowed: true, reason })
  const no = (reason: string): PermissionResult => ({ allowed: false, reason })

  // Instance admin is break-glass for everything EXCEPT personal judgments (I-6).
  if (ctx.isInstanceAdmin && !PERSONAL_JUDGMENTS.includes(action)) return yes('instance admin')
  const viewerOnly = ctx.roles.length > 0 && ctx.roles.every((r) => r === 'viewer')
  if (viewerOnly && action !== 'project.read') return no('viewer is read-only')
  if (ctx.roles.length === 0) return no('not a member of this project')

  switch (action) {
    case 'project.read':
      return yes('project member')

    case 'intake.raise':
      return ctx.allowAnyoneRaiseIntake === false && !hasAny(ctx, [...CREATORS, 'coordinator'])
        ? no('intake raising restricted by project config')
        : yes('any project member may raise (PEC-AHL-003)')

    case 'intake.triage':
      return hasAny(ctx, ['coordinator', 'pm', 'admin'])
        ? yes('coordinator/pm') : no('triage requires coordinator, pm, or admin')

    case 'work_item.create':
      return hasAny(ctx, CREATORS) ? yes('lead/owner role') : no('direct creation requires a lead/owner role; raise an intake item instead')

    case 'work_item.update':
    case 'work_item.transition':
      if (ctx.isOwner) return yes('item owner')
      if (hasAny(ctx, LEADS)) return yes('lead role')
      if (hasAny(ctx, ['coordinator'])) return yes('coordinator (tracker hygiene)')
      return no('requires item owner, a lead role, or coordinator')

    case 'work_item.cancel':
      return hasAny(ctx, [...LEADS, 'coordinator']) ? yes('lead or coordinator') : no('cancel requires a lead or coordinator')

    case 'hold.raise':
      return yes('any project member except viewer (SPEC §2.2)')

    case 'hold.resolve':
      if (ctx.isHoldOwner) return yes('hold owner')
      if (hasAny(ctx, [...LEADS, 'coordinator'])) return yes('lead or coordinator')
      return no('requires hold owner, a lead, or coordinator')

    case 'check.create':
      return hasAny(ctx, ['package_lead', 'discipline_lead', 'engineer_of_record', 'pm', 'admin'])
        ? yes('lead/EOR') : no('check creation requires lead or engineer of record')

    case 'check.work':
      if (ctx.isChecker) return yes('assigned checker')
      if (hasAny(ctx, LEADS)) return yes('lead role')
      return no('requires the assigned checker or a lead')

    case 'check.accept':
      return ctx.isChecker ? yes('assigned checker') : no('only the assigned checker may accept (I-6, PEC-CHK-002)')

    case 'comment.create':
      if (ctx.isChecker) return yes('checker raises comments')
      if (hasAny(ctx, LEADS)) return yes('lead role')
      return no('comments are raised by the checker (or a lead)')

    case 'comment.respond':
      if (ctx.isResponder) return yes('assigned responder')
      if (hasAny(ctx, LEADS)) return yes('lead role')
      return no('requires the assigned responder')

    case 'comment.accept':
      return ctx.isChecker ? yes('assigned checker') : no('comment closure is accepted by the checker individually (PEC-CHK-002)')

    case 'approval.create':
      return hasAny(ctx, ['package_lead', 'pm', 'engineering_manager', 'document_controller', 'admin'])
        ? yes('lead/EM/DC') : no('approval records are created by leads, EM, or document control')

    case 'approval.outcome':
      // Document controllers can never record outcomes, even if also signatory-listed by error (PRD §14).
      if (ctx.roles.length === 1 && ctx.roles[0] === 'document_controller') return no('document controllers cannot record approvals (PRD §14)')
      return ctx.isSignatory ? yes('named signatory (D-12)') : no('only named signatories may record the outcome (PEC-AUTH-002)')

    case 'approval.supersede':
      return hasAny(ctx, ['pm', 'engineering_manager', 'admin']) ? yes('pm/EM') : no('supersession requires pm or EM')

    case 'decision.create':
      return hasAny(ctx, ['package_lead', 'pm', 'engineering_manager', 'coordinator', 'admin'])
        ? yes('lead/EM/coordinator') : no('decision records are created by leads, EM, or coordinator')

    case 'decision.progress':
      // Preparing requires no authority to decide (PRD §14).
      if (ctx.isPreparer || ctx.isAuthority) return yes('preparer or authority')
      if (hasAny(ctx, [...LEADS, 'coordinator'])) return yes('lead or coordinator')
      return no('requires preparer, authority, a lead, or coordinator')

    case 'decision.outcome':
      if (ctx.roles.length === 1 && ctx.roles[0] === 'document_controller') return no('document controllers cannot record decisions (PRD §14)')
      return ctx.isAuthority ? yes('decision authority') : no('only the decision authority records the outcome (§7.6)')

    case 'decision.supersede':
      return hasAny(ctx, ['pm', 'engineering_manager', 'admin']) ? yes('pm/EM') : no('supersession requires pm or EM')

    case 'condition.create':
      return hasAny(ctx, [...LEADS, 'coordinator']) ? yes('lead or coordinator') : no('manual conditions require a lead or coordinator')

    case 'condition.waive': {
      const type = ctx.conditionType ?? 'other'
      const configured = ctx.waiverRoles?.[type]
      const allowed = configured ?? (STRICT_WAIVER_TYPES.includes(type) ? DEFAULT_WAIVER.strict : DEFAULT_WAIVER.lead)
      return hasAny(ctx, allowed)
        ? yes(`waiver role for ${type}-type conditions`)
        : no(`waiving ${type}-type conditions requires: ${allowed.join(', ')} (I-8)`)
    }

    case 'condition.satisfy_manual':
      return hasAny(ctx, [...LEADS, 'coordinator']) ? yes('lead or coordinator') : no('manual satisfaction requires a lead or coordinator')

    case 'revision.create':
    case 'deliverable.create':
    case 'deliverable.update':
      return hasAny(ctx, ['package_lead', 'discipline_lead', 'engineer_of_record', 'pm', 'document_controller', 'admin'])
        ? yes('lead/EOR/DC') : no('requires lead, engineer of record, or document controller')

    case 'revision.transition':
      if (ctx.isOwner) return yes('deliverable owner')
      return hasAny(ctx, [...LEADS]) ? yes('lead role') : no('requires deliverable owner or a lead')

    case 'revision.auto':
    case 'approval.auto':
      return no('system-driven transition; not user-invokable')

    case 'issue.record':
      return hasAny(ctx, ['document_controller', 'pm', 'admin'])
        ? yes('document control') : no('issue events are recorded by document control or pm')

    case 'risk.create':
    case 'risk.update':
      // planner included in P2: overcapacity may create or link a risk (PEC-PLAN-004, PEC-RISK-003)
      return hasAny(ctx, [...LEADS, 'coordinator', 'engineer_of_record', 'planner']) || ctx.isOwner === true
        ? yes('lead/coordinator/planner/owner') : no('requires a lead, coordinator, planner, or the risk owner')

    case 'interface.create':
    case 'interface.update':
      return hasAny(ctx, [...LEADS, 'coordinator']) ? yes('lead or coordinator') : no('interface items are managed by leads or coordinator')

    case 'evidence.add':
      return yes('any project member except viewer')

    case 'config.manage':
      return hasAny(ctx, ['admin']) ? yes('project admin (audit-evented)') : no('configuration requires admin')

    // D-PEC-08: proposed imports. Proposing is register-handling work; accept/apply carries
    // the same power as direct import, so it keeps parity with the config.manage gate.
    // Deliberately NOT a personal judgment (I-6): no engineering authority is recorded.
    case 'import.propose':
      return hasAny(ctx, ['admin', 'pm', 'coordinator', 'document_controller'])
        ? yes('register-handling role (D-PEC-08)') : no('proposing an import requires admin, pm, coordinator, or document control')

    case 'import.accept':
      return hasAny(ctx, ['admin'])
        ? yes('project admin (parity with direct import)') : no('accepting/applying an import proposal requires admin')

    // P2 planning (PRD §14: planners commit plans; leads propose plan changes)
    case 'plan.manage':
      return hasAny(ctx, ['planner', 'pm', 'engineering_manager', 'admin'])
        ? yes('planner/pm/EM') : no('plan items and capacity are managed by the planner, pm, or EM')

    case 'plan.commit':
      return hasAny(ctx, ['planner', 'pm', 'admin'])
        ? yes('planner/pm (PEC-PLAN-007)') : no('the weekly commit is recorded by the planner or pm')

    case 'plan.propose':
      return hasAny(ctx, ['package_lead', 'discipline_lead', 'planner', 'pm', 'engineering_manager', 'admin'])
        ? yes('lead or planner (PEC-PLAN-005)') : no('plan shifts are proposed by leads or the planner')

    case 'plan.review':
      return hasAny(ctx, ['package_lead', 'discipline_lead', 'pm', 'engineering_manager', 'admin'])
        ? yes('affected lead (PEC-PLAN-005)') : no('cross-package shifts are reviewed by affected leads')
  }
}

/** Logs a role may see (PEC-AHL-002 / PEC-NFR-005); applied in the repository query layer. */
export function visibleLogs(
  roles: Role[],
  configured: Partial<Record<Role, Log[]>> | undefined,
): Log[] {
  const all: Log[] = ['package', 'internal', 'client']
  if (roles.length === 0) return []
  const sets = roles.map((r) => configured?.[r] ?? (r === 'viewer' ? (['package', 'client'] as Log[]) : all))
  const union = new Set<Log>()
  for (const s of sets) for (const l of s) union.add(l)
  return all.filter((l) => union.has(l))
}
