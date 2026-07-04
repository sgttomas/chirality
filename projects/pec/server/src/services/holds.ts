/**
 * Hold services (§4.3, OM-2, I-3). A hold is a first-class blocking record with typed
 * cause, owner, and need-by — all REQUIRED at creation — plus ≥1 blocking link.
 * "Blocked" on targets is derived, never stored.
 */

import type { Hold, HoldTargetType, RecordType } from '@pec/core'
import { HOLD_CAUSES, HOLD_RESOLUTION_KINDS, HOLD_TARGET_TYPES, findTransition } from '@pec/core'
import { badRequest, notFound } from '../errors.ts'
import { TABLE, nowIso } from '../repo.ts'
import { reqDate } from '../validate.ts'
import type { Sx } from './shared.ts'
import { requireCan } from './shared.ts'

export interface HoldTarget { targetType: HoldTargetType; targetId: number }

export interface RaiseHoldInput {
  title: string
  cause: Hold['cause']
  statement?: string
  ownerId: number
  needBy: string
  log?: Hold['log']
  targets: HoldTarget[]
}

function ownerOfTarget(sx: Sx, t: HoldTarget): number | null {
  const table = TABLE[t.targetType]
  if (!table) return null
  const rec = sx.repo.maybeGet<Record<string, unknown>>(table, sx.projectId, t.targetId)
  if (!rec) throw notFound(`${t.targetType}#${t.targetId}`)
  return (rec.ownerId ?? rec.checkerId ?? rec.authorityId ?? null) as number | null
}

function refOfTarget(sx: Sx, t: HoldTarget): string {
  const table = TABLE[t.targetType]!
  const rec = sx.repo.get<Record<string, unknown>>(table, sx.projectId, t.targetId)
  return (rec.ref ?? rec.docNo ?? rec.revCode ?? `#${t.targetId}`) as string
}

export function raiseHold(sx: Sx, input: RaiseHoldInput, opts?: { skipPermission?: boolean }): Hold {
  if (!opts?.skipPermission) requireCan(sx, 'hold.raise')
  if (!input.title) throw badRequest('title required')
  if (!HOLD_CAUSES.includes(input.cause)) throw badRequest(`hold cause must be typed (I-3): ${HOLD_CAUSES.join(', ')}`)
  if (!input.ownerId) throw badRequest('hold owner required (I-3)')
  const needBy = reqDate(input.needBy, 'hold need-by')
  if (!input.targets || input.targets.length === 0) throw badRequest('a hold blocks ≥1 record (§7.3)')
  for (const t of input.targets) {
    if (!HOLD_TARGET_TYPES.includes(t.targetType)) throw badRequest(`invalid hold target type: ${t.targetType}`)
  }

  const ref = sx.repo.nextRef(sx.projectId, 'hold')
  const id = sx.repo.insert('hold', {
    projectId: sx.projectId, ref, title: input.title, cause: input.cause,
    statement: input.statement ?? null, ownerId: input.ownerId, needBy,
    raisedBy: sx.session.personId, raisedAt: nowIso(), state: 'active',
    log: input.log ?? 'internal',
  })
  for (const t of input.targets) {
    // validates target existence + resolves owner for notification
    const targetOwner = ownerOfTarget(sx, t)
    const targetRef = refOfTarget(sx, t)
    sx.repo.insert('hold_link', { holdId: id, targetType: t.targetType, targetId: t.targetId })
    sx.repo.history({
      projectId: sx.projectId, recordType: t.targetType as RecordType, recordId: t.targetId,
      actorId: sx.session.personId, kind: 'hold_applied',
      summary: `${ref} (${input.cause}) blocks ${targetRef}`, payload: { holdId: id }, authorityRef: null,
    })
    if (targetOwner && targetOwner !== sx.session.personId) {
      sx.repo.notify({
        projectId: sx.projectId, personId: targetOwner, event: 'hold_blocks_your_record',
        recordType: t.targetType, recordId: t.targetId, recordRef: targetRef,
        reason: `${ref} (${input.cause}) blocks your record`, nextAction: `chase ${ref} owner`, due: input.needBy,
      })
    }
  }
  sx.repo.history({
    projectId: sx.projectId, recordType: 'hold', recordId: id,
    actorId: sx.session.personId, kind: 'created',
    summary: `${ref} raised: ${input.cause}, owner #${input.ownerId}, need-by ${input.needBy}, blocks ${input.targets.length} record(s)`,
    payload: { input }, authorityRef: null,
  })
  return sx.repo.get<Hold>('hold', sx.projectId, id)
}

export function resolveHold(
  sx: Sx, id: number, event: 'resolve' | 'withdraw',
  payload: {
    version: number
    resolutionKind?: Hold['resolutionKind']
    note?: string
    resolvingRefType?: RecordType
    resolvingRefId?: number
    reason?: string
  },
): Hold {
  const hold = sx.repo.get<Hold>('hold', sx.projectId, id)
  const def = findTransition('hold', event, hold.state)
  if (!def) throw badRequest(`illegal transition: ${event} from ${hold.state}`)
  requireCan(sx, 'hold.resolve', { isHoldOwner: hold.ownerId === sx.session.personId })
  if (event === 'resolve') {
    if (!payload.resolutionKind || !HOLD_RESOLUTION_KINDS.includes(payload.resolutionKind)) {
      throw badRequest('resolve requires the resolving fact (§7.3): ' + HOLD_RESOLUTION_KINDS.join(', '))
    }
  }
  if (event === 'withdraw' && !payload.reason) throw badRequest('withdraw requires a reason')

  sx.repo.update('hold', sx.projectId, id, payload.version, {
    state: def.to,
    resolutionKind: payload.resolutionKind ?? null,
    resolutionNote: payload.note ?? payload.reason ?? null,
    resolvedAt: nowIso(),
    resolvingRefType: payload.resolvingRefType ?? null,
    resolvingRefId: payload.resolvingRefId ?? null,
  })
  sx.repo.history({
    projectId: sx.projectId, recordType: 'hold', recordId: id,
    actorId: sx.session.personId, kind: 'transition',
    summary: `${hold.ref}: active → ${def.to}${payload.resolutionKind ? ` (${payload.resolutionKind})` : ''}${payload.reason ? ` (${payload.reason})` : ''}`,
    payload, authorityRef: null,
  })

  // Blocked records become available; their owners are notified (§7.3).
  const links = sx.repo.db.prepare('SELECT target_type, target_id FROM hold_link WHERE hold_id = ?')
    .all(id) as Array<{ target_type: HoldTargetType; target_id: number }>
  for (const l of links) {
    const t = { targetType: l.target_type, targetId: l.target_id }
    try {
      const owner = ownerOfTarget(sx, t)
      const targetRef = refOfTarget(sx, t)
      sx.repo.history({
        projectId: sx.projectId, recordType: t.targetType as RecordType, recordId: t.targetId,
        actorId: sx.session.personId, kind: 'hold_lifted',
        summary: `${hold.ref} ${def.to}; ${targetRef} no longer blocked by it`, payload: { holdId: id }, authorityRef: null,
      })
      if (owner) {
        sx.repo.notify({
          projectId: sx.projectId, personId: owner, event: 'hold_resolved_unblocked',
          recordType: t.targetType, recordId: t.targetId, recordRef: targetRef,
          reason: `${hold.ref} was ${def.to}`, nextAction: 'your record is available again', due: null,
        })
      }
    } catch {
      // target gone from view — keep resolving the rest
    }
  }
  return sx.repo.get<Hold>('hold', sx.projectId, id)
}
