/**
 * Route registrations (SPEC §7). Auth + project membership at the boundary; fine-grained
 * permissions inside services. Every mutation runs in a transaction. Errors:
 * 400 BAD_REQUEST · 401 · 403 FORBIDDEN · 404 · 409 VERSION_CONFLICT / CONDITIONS_OPEN.
 */

import type { Db } from './db.ts'
import { withTx } from './db.ts'
import { Router } from './http.ts'
import type { ReqCtx } from './http.ts'
import { Repo } from './repo.ts'
import { COOKIE_NAME, destroySession, login, requireSession, rolesFor } from './auth.ts'
import { badRequest, forbidden, notFound, unauthorized } from './errors.ts'
import type { Sx } from './services/shared.ts'
import { requireCan } from './services/shared.ts'
import * as work from './services/work.ts'
import * as holds from './services/holds.ts'
import * as checks from './services/checks.ts'
import * as decisions from './services/decisions.ts'
import * as intake from './services/intake.ts'
import * as registers from './services/registers.ts'
import * as revisions from './services/revisions.ts'
import * as views from './services/views.ts'
import { sweepProject } from './services/sweep.ts'
import { exportRegister, importContract } from './import/index.ts'
import { sponsorBrief } from './reports/sponsor-brief.ts'
import { can, explainTransition } from '@pec/core'
import type { PermissionAction } from '@pec/core'
import { pctx } from './services/shared.ts'

interface AuthedCtx extends ReqCtx {
  sx: Sx
}

export function buildRouter(db: Db): Router {
  const r = new Router()
  const repo = new Repo(db)

  const authed = (fn: (ctx: AuthedCtx) => unknown) => (ctx: ReqCtx) => {
    const session = requireSession(db, ctx.cookies[COOKIE_NAME])
    const pid = Number(ctx.params.pid)
    if (!Number.isInteger(pid) || pid <= 0) throw badRequest('invalid project id')
    const roles = rolesFor(db, pid, session.personId)
    if (roles.length === 0 && !session.isAdmin) throw forbidden('not a member of this project')
    if (!repo.maybeGet('project', null, pid)) throw notFound(`project #${pid}`)
    const sx: Sx = { db, repo, projectId: pid, session, roles }
    return fn(Object.assign(ctx, { sx }))
  }
  const tx = (fn: (ctx: AuthedCtx) => unknown) => authed((ctx) => {
    try {
      return withTx(db, () => fn(ctx))
    } catch (e) {
      // A refused gated transition rolled back — persist the recorded attempt (§9)
      const attempt = (e as { blockedAttempt?: import('./services/shared.ts').BlockedAttempt }).blockedAttempt
      if (attempt) {
        withTx(db, () => repo.history({
          projectId: attempt.projectId, recordType: attempt.recordType, recordId: attempt.recordId,
          actorId: attempt.actorId, kind: 'transition_blocked',
          summary: attempt.summary, payload: attempt.payload, authorityRef: null,
        }))
      }
      throw e
    }
  })
  const body = (ctx: ReqCtx): Record<string, unknown> => {
    if (ctx.body == null || typeof ctx.body !== 'object') throw badRequest('JSON body required')
    return ctx.body as Record<string, unknown>
  }
  const idOf = (ctx: ReqCtx, name = 'id'): number => {
    const n = Number(ctx.params[name])
    if (!Number.isInteger(n) || n <= 0) throw badRequest(`invalid ${name}`)
    return n
  }

  // ---------- auth ----------
  r.post('/api/auth/login', async (ctx) => {
    const b = body(ctx)
    const result = login(db, String(b.email ?? ''), String(b.password ?? ''))
    if (!result) throw unauthorized('invalid credentials')
    ctx.res.setHeader('set-cookie',
      `${COOKIE_NAME}=${result.token}; HttpOnly; SameSite=Lax; Path=/; Max-Age=${7 * 24 * 3600}`)
    // login-time sweep (SPEC §4 notification producers)
    const memberships = db.prepare('SELECT DISTINCT project_id FROM project_role WHERE person_id = ?')
      .all(result.session.personId) as Array<{ project_id: number }>
    for (const m of memberships) {
      try { withTx(db, () => sweepProject(db, m.project_id)) } catch { /* sweep must never block login */ }
    }
    return { me: result.session }
  })
  r.post('/api/auth/logout', (ctx) => {
    const token = ctx.cookies[COOKIE_NAME]
    if (token) destroySession(db, token)
    ctx.res.setHeader('set-cookie', `${COOKIE_NAME}=; HttpOnly; SameSite=Lax; Path=/; Max-Age=0`)
    return { ok: true }
  })
  r.get('/api/auth/me', (ctx) => {
    const s = requireSession(db, ctx.cookies[COOKIE_NAME])
    const projects = db.prepare(
      `SELECT p.id, p.code, p.name, GROUP_CONCAT(pr.role) AS roles
       FROM project p JOIN project_role pr ON pr.project_id = p.id
       WHERE pr.person_id = ? GROUP BY p.id`,
    ).all(s.personId) as Array<{ id: number; code: string; name: string; roles: string }>
    const allProjects = s.isAdmin
      ? db.prepare('SELECT id, code, name FROM project').all() as Array<{ id: number; code: string; name: string }>
      : []
    return { me: s, projects, allProjects }
  })
  r.get('/api/people', (ctx) => {
    requireSession(db, ctx.cookies[COOKIE_NAME])
    return db.prepare('SELECT id, name, email, discipline FROM person ORDER BY name').all()
  })

  // ---------- role homes ----------
  r.get('/api/projects/:pid/overview', authed((c) => views.overviewView(c.sx)))
  r.get('/api/projects/:pid/packages', authed((c) => views.packagesView(c.sx)))
  r.get('/api/projects/:pid/packages/:id', authed((c) => views.packageDetailView(c.sx, idOf(c))))
  r.get('/api/projects/:pid/deliverables', authed((c) => views.deliverablesView(c.sx, {
    packageId: c.query.get('package') ? Number(c.query.get('package')) : undefined,
    discipline: c.query.get('discipline') ?? undefined,
    state: c.query.get('state') ?? undefined,
    holdCause: c.query.get('hold_cause') ?? undefined,
    dueBefore: c.query.get('due_before') ?? undefined,
    view: (c.query.get('view') as never) ?? undefined,
  })))
  r.get('/api/projects/:pid/deliverables/:id', authed((c) => views.deliverableDetailView(c.sx, idOf(c))))
  r.get('/api/projects/:pid/log', authed((c) => views.logRegisterView(c.sx, {
    log: (c.query.get('log') as never) ?? undefined,
    packageId: c.query.get('package') ? Number(c.query.get('package')) : undefined,
    ownerId: c.query.get('owner') ? Number(c.query.get('owner')) : undefined,
    type: (c.query.get('type') as never) ?? undefined,
    cause: c.query.get('cause') ?? undefined,
    overdue: c.query.get('overdue') != null ? c.query.get('overdue') === 'true' : undefined,
    anchored: c.query.get('anchored') != null ? c.query.get('anchored') === 'true' : undefined,
  })))
  r.get('/api/projects/:pid/my-week', authed((c) => views.myWeekView(c.sx)))
  r.get('/api/projects/:pid/plan', authed(() => ({
    phase: 'P2',
    note: 'Now/Next/Later, six-week lookahead, and capacity arrive in Phase 2 (PRD §12.4). '
      + 'P1 My Week is driven by need-by dates plus the manual commit-to-week flag (PEC-MW-007).',
  })))

  // permission probe for the UI ("can I?" — rules stay server-side)
  r.get('/api/projects/:pid/can/:action', authed((c) => {
    const action = c.params.action as PermissionAction
    return can(action, pctx(c.sx))
  }))

  // ---------- deliverables & revisions ----------
  r.post('/api/projects/:pid/deliverables', tx((c) => registers.createDeliverable(c.sx, body(c) as never)))
  r.put('/api/projects/:pid/deliverables/:id', tx((c) => {
    const b = body(c)
    return registers.updateDeliverable(c.sx, idOf(c), Number(b.version), b as never)
  }))
  r.post('/api/projects/:pid/deliverables/:id/revisions', tx((c) => {
    const b = body(c)
    return revisions.createRevision(c.sx, {
      deliverableId: idOf(c), revCode: String(b.revCode ?? ''), issuePurpose: b.issuePurpose as string | undefined,
    })
  }))
  r.post('/api/projects/:pid/revisions/:id/transition', tx((c) => {
    const b = body(c)
    return revisions.transitionRevision(c.sx, idOf(c), String(b.event ?? ''), {
      version: Number(b.version),
      issueEvent: b.issueEvent as never,
      clientComments: b.clientComments as never,
    })
  }))
  r.get('/api/projects/:pid/revisions/:id/explain', authed((c) => {
    const snap = c.sx.repo.snapshot(c.sx.projectId)
    const gate = c.query.get('transition') ?? 'revision.issue'
    return explainTransition(snap, 'revision', idOf(c), gate, { holdVeto: true })
  }))

  // ---------- packages ----------
  r.post('/api/projects/:pid/packages', tx((c) => registers.createPackage(c.sx, body(c) as never)))

  // ---------- work items ----------
  r.post('/api/projects/:pid/work-items', tx((c) => work.createWorkItem(c.sx, body(c) as never)))
  r.get('/api/projects/:pid/work-items/:id', authed((c) => views.workItemDetailView(c.sx, idOf(c))))
  r.put('/api/projects/:pid/work-items/:id', tx((c) => {
    const b = body(c)
    return work.updateWorkItem(c.sx, idOf(c), Number(b.version), b as never)
  }))
  r.post('/api/projects/:pid/work-items/:id/transition', tx((c) => {
    const b = body(c)
    return work.transitionWorkItem(c.sx, idOf(c), String(b.event ?? ''), {
      version: Number(b.version), reason: b.reason as string | undefined,
      closingStatement: b.closingStatement as string | undefined,
    })
  }))
  r.post('/api/projects/:pid/work-items/:id/progress', tx((c) => {
    work.addProgress(c.sx, idOf(c), String(body(c).note ?? ''))
    return { ok: true }
  }))

  // ---------- holds ----------
  r.get('/api/projects/:pid/holds', authed((c) => views.holdRegisterView(c.sx, c.query.get('cause') ?? undefined)))
  r.post('/api/projects/:pid/holds', tx((c) => holds.raiseHold(c.sx, body(c) as never)))
  r.post('/api/projects/:pid/holds/:id/resolve', tx((c) => {
    const b = body(c)
    return holds.resolveHold(c.sx, idOf(c), 'resolve', b as never)
  }))
  r.post('/api/projects/:pid/holds/:id/withdraw', tx((c) => {
    const b = body(c)
    return holds.resolveHold(c.sx, idOf(c), 'withdraw', b as never)
  }))

  // ---------- checks & comments ----------
  r.post('/api/projects/:pid/checks', tx((c) => checks.createCheck(c.sx, body(c) as never)))
  r.get('/api/projects/:pid/checks/:id', authed((c) => views.checkDetailView(c.sx, idOf(c))))
  r.post('/api/projects/:pid/checks/:id/start', tx((c) => checks.startCheck(c.sx, idOf(c), Number(body(c).version))))
  r.put('/api/projects/:pid/checks/:id/checklist', tx((c) => {
    const b = body(c)
    return checks.updateChecklist(c.sx, idOf(c), Number(b.version), b.checklist as never)
  }))
  r.post('/api/projects/:pid/checks/:id/comments', tx((c) => {
    const b = body(c)
    return checks.addComment(c.sx, { ...(b as object), checkId: idOf(c) } as never)
  }))
  r.post('/api/projects/:pid/comments/:id/respond', tx((c) => {
    const b = body(c)
    return checks.respondComment(c.sx, idOf(c), Number(b.version), String(b.response ?? ''))
  }))
  r.post('/api/projects/:pid/comments/:id/accept', tx((c) => {
    const b = body(c)
    return checks.acceptComment(c.sx, idOf(c), Number(b.version), b.closureEvidenceId as number | undefined)
  }))
  r.post('/api/projects/:pid/comments/:id/reopen', tx((c) => {
    const b = body(c)
    return checks.reopenComment(c.sx, idOf(c), Number(b.version), String(b.reason ?? ''))
  }))
  r.post('/api/projects/:pid/checks/:id/accept', tx((c) => checks.acceptCheck(c.sx, idOf(c), Number(body(c).version))))
  r.post('/api/projects/:pid/checks/:id/reopen', tx((c) => {
    const b = body(c)
    return checks.reopenCheck(c.sx, idOf(c), Number(b.version), String(b.reason ?? ''))
  }))

  // ---------- approvals ----------
  r.get('/api/projects/:pid/approval-register', authed((c) => views.approvalRegisterView(c.sx)))
  r.post('/api/projects/:pid/approval-records', tx((c) => decisions.createApprovalRecord(c.sx, body(c) as never)))
  r.post('/api/projects/:pid/approval-records/:id/outcome', tx((c) => decisions.recordApprovalOutcome(c.sx, idOf(c), body(c) as never)))
  r.post('/api/projects/:pid/approval-records/:id/supersede', tx((c) => decisions.supersedeApproval(c.sx, idOf(c), body(c) as never)))

  // ---------- decisions ----------
  r.get('/api/projects/:pid/decisions', authed((c) => views.decisionRegisterView(c.sx)))
  r.post('/api/projects/:pid/decisions', tx((c) => decisions.createDecision(c.sx, body(c) as never)))
  r.post('/api/projects/:pid/decisions/:id/progress', tx((c) => {
    const b = body(c)
    return decisions.progressDecision(c.sx, idOf(c), String(b.event ?? '') as never, b as never)
  }))
  r.post('/api/projects/:pid/decisions/:id/outcome', tx((c) => decisions.recordDecisionOutcome(c.sx, idOf(c), body(c) as never)))
  r.post('/api/projects/:pid/decisions/:id/supersede', tx((c) => decisions.supersedeDecision(c.sx, idOf(c), body(c) as never)))

  // ---------- conditions ----------
  r.post('/api/projects/:pid/conditions', tx((c) => decisions.createCondition(c.sx, body(c) as never)))
  r.post('/api/projects/:pid/conditions/:id/waive', tx((c) => decisions.waiveCondition(c.sx, idOf(c), body(c) as never)))
  r.post('/api/projects/:pid/conditions/:id/satisfy', tx((c) => {
    const b = body(c)
    return decisions.satisfyConditionManual(c.sx, idOf(c), Number(b.version), String(b.note ?? ''))
  }))

  // ---------- risks & interfaces ----------
  r.get('/api/projects/:pid/risks', authed((c) => views.riskRegisterView(c.sx)))
  r.post('/api/projects/:pid/risks', tx((c) => registers.createRisk(c.sx, body(c) as never)))
  r.put('/api/projects/:pid/risks/:id', tx((c) => {
    const b = body(c)
    return registers.updateRisk(c.sx, idOf(c), Number(b.version), b as never)
  }))
  r.get('/api/projects/:pid/interfaces', authed((c) => views.interfaceRegisterView(c.sx)))
  r.post('/api/projects/:pid/interfaces', tx((c) => registers.createInterface(c.sx, body(c) as never)))
  r.put('/api/projects/:pid/interfaces/:id', tx((c) => {
    const b = body(c)
    return registers.updateInterface(c.sx, idOf(c), Number(b.version), b as never)
  }))

  // ---------- intake ----------
  r.get('/api/projects/:pid/intake', authed((c) => views.intakeQueueView(c.sx, c.query.get('state') ?? undefined)))
  r.post('/api/projects/:pid/intake', tx((c) => intake.raiseIntake(c.sx, body(c) as never)))
  r.post('/api/projects/:pid/intake/:id/open-triage', tx((c) => intake.openTriage(c.sx, idOf(c), Number(body(c).version))))
  r.post('/api/projects/:pid/intake/:id/triage', tx((c) => intake.dispositionIntake(c.sx, idOf(c), body(c) as never)))

  // ---------- evidence & basis ----------
  r.post('/api/projects/:pid/records/:recordType/:id/evidence', tx((c) => {
    const b = body(c)
    const id = work.addEvidence(c.sx, String(c.params.recordType), idOf(c), b as never)
    return { id }
  }))

  // ---------- notifications ----------
  r.get('/api/projects/:pid/notifications', authed((c) =>
    c.sx.repo.notificationsFor(c.sx.projectId, c.sx.session.personId, c.query.get('unread') === 'true')))
  r.post('/api/projects/:pid/notifications/:id/read', tx((c) => {
    const n = c.sx.repo.maybeGet<{ personId: number }>('notification', c.sx.projectId, idOf(c))
    if (!n || n.personId !== c.sx.session.personId) throw notFound('notification')
    c.sx.db.prepare('UPDATE notification SET read_at = ? WHERE id = ?').run(new Date().toISOString(), idOf(c))
    return { ok: true }
  }))

  // ---------- history ----------
  r.get('/api/projects/:pid/history/:recordType/:id', authed((c) =>
    c.sx.repo.historyFor(String(c.params.recordType), idOf(c), 200)))

  // ---------- import / export / reports ----------
  r.post('/api/projects/:pid/import/:contract', tx((c) => {
    requireCan(c.sx, 'config.manage', {})
    const csv = typeof c.body === 'string' ? c.body : String((c.body as Record<string, unknown>)?.csv ?? '')
    if (!csv.trim()) throw badRequest('CSV body required')
    return importContract(c.sx, String(c.params.contract), csv, c.query.get('force') === 'true')
  }))
  r.get('/api/projects/:pid/export/:register', authed((c) => {
    const csv = exportRegister(c.sx, String(c.params.register).replace(/\.csv$/, ''))
    c.res.setHeader('content-type', 'text/csv; charset=utf-8')
    c.res.setHeader('content-disposition', `attachment; filename="${c.params.register}"`)
    return csv
  }))
  r.get('/api/projects/:pid/reports/sponsor-brief', authed((c) => {
    c.res.setHeader('content-type', 'text/html; charset=utf-8')
    return sponsorBrief(c.sx)
  }))

  // ---------- config ----------
  r.get('/api/projects/:pid/config', authed((c) => c.sx.repo.get('project', null, c.sx.projectId)))
  r.put('/api/projects/:pid/config', tx((c) => {
    requireCan(c.sx, 'config.manage', {})
    const b = body(c)
    const prior = c.sx.repo.get<Record<string, unknown>>('project', null, c.sx.projectId)
    // project has no project_id column: direct optimistic update
    const jsonCols = new Set(['weekendDays', 'holidays', 'thresholds', 'config'])
    const sets: string[] = []
    const vals: unknown[] = []
    for (const k of ['name', 'timezone', 'weekendDays', 'holidays', 'thresholds', 'config'] as const) {
      if (!(k in b)) continue
      sets.push(`${k === 'weekendDays' ? 'weekend_days' : k} = ?`)
      vals.push(jsonCols.has(k) ? JSON.stringify(b[k]) : b[k])
    }
    if (sets.length === 0) throw badRequest('nothing to update')
    const res = c.sx.db.prepare(
      `UPDATE project SET ${sets.join(', ')}, version = version + 1 WHERE id = ? AND version = ?`,
    ).run(...(vals as never[]), c.sx.projectId, Number(b.version))
    if (res.changes === 0) throw badRequest('version conflict on project config (PEC-NFR-004)')
    const patch: Record<string, unknown> = {}
    for (const k of ['name', 'timezone', 'weekendDays', 'holidays', 'thresholds', 'config'] as const) {
      if (k in b) patch[k] = b[k]
    }
    c.sx.repo.audit({
      projectId: c.sx.projectId, actorId: c.sx.session.personId, action: 'config_change',
      recordType: 'project', recordId: c.sx.projectId,
      priorValue: { thresholds: prior.thresholds, config: prior.config },
      newValue: patch,
    })
    return c.sx.repo.get('project', null, c.sx.projectId)
  }))

  return r
}
