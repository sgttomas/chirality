/**
 * The bounded agent client (D-PEC-17; the adopted UI brief's §4 contract as a
 * method surface, adopted via D-PEC-16). The method surface IS the contract:
 * there is deliberately no method for accept, apply, reject-of-others, `force`,
 * or approval/decision/check outcomes. pec RBAC remains the real gate
 * (K-DOMAIN-3); every guard here is defense in depth:
 *
 * - loopback-only base URL by construction (D-T0-19 O-2A);
 * - URL denylist in the single low-level request helper (accept/apply/outcome/
 *   supersede/waive paths, `force` in query or body) — AGENT_FORBIDDEN_ACT
 *   before any network call;
 * - disposition-payload guard (GOV MAJOR-1, engine-independent): any payload
 *   naming `approvalRecords` is refused BEFORE any network call — the one act
 *   pec RBAC does not stop (conversion runs under skipPermission, live at
 *   server/src/services/intake.ts:106-131) — test-pinned, non-negotiable;
 * - misprovisioning refusal: instance-admin session or an allowed
 *   `can/import.accept` probe is fatal;
 * - ruled failure semantics: 409 STALE_PROPOSAL and 403 come back as typed
 *   results (refresh→report / report-never-escalate), never retried around.
 */

import type { ProjectAdapterConfig, SidecarConfig } from './config.ts'
import { assertLoopbackBaseUrl } from './config.ts'

export class AgentClientError extends Error {
  code: string
  details: unknown

  constructor(code: string, message: string, details?: unknown) {
    super(message)
    this.code = code
    this.details = details ?? null
  }
}

export interface AgentIdentity {
  personId: number
  name: string
  email: string
}

/**
 * Typed outcome for API calls: 409 STALE_PROPOSAL is the ruled
 * refresh→human-re-accepts flow, not an exception to retry; 403 is
 * report-never-escalate. Everything else (bad request, 404, 5xx, network)
 * throws a typed AgentClientError — once, no retry storms.
 */
export type ApiResult<T> =
  | { ok: true; value: T }
  | { ok: false; kind: 'stale'; details: unknown }
  | { ok: false; kind: 'forbidden'; message: string }

/** proposal view as the server returns it (subset the sidecar relies on) */
export interface ProposalView {
  id: number
  ref: string
  contract: string
  state: string
  version: number
  createdBy: number
  sourceName: string | null
  sourceSha256: string
  coverageStart?: string | null
  coverageEnd?: string | null
  dryRunReport: {
    accepted?: number
    updated?: number
    conflicts?: unknown[]
    rejected?: unknown[]
    intakeCreated?: number
    error?: string
  } | null
  rejectReason?: string | null
}

export type ProposalSummary = Omit<ProposalView, 'dryRunReport'> & { dryRunReport: ProposalView['dryRunReport'] }

export interface IntakeItemView {
  id: number
  ref: string
  state: string
  version: number
  statementVerbatim: string
  quickType: string
  disposition: string | null
  dispositionNote: string | null
}

/**
 * GOV MAJOR-1 (type layer): the disposition body the client accepts is
 * CONSTRAINED — it cannot express approval-record creation (`approvalRecords`
 * is structurally absent). The runtime guard below backs the type against
 * structural typing / JSON passthrough.
 */
export interface AgentConversionRecords {
  workItems?: unknown[]
  holds?: unknown[]
  risks?: unknown[]
  decisions?: unknown[]
  interfaces?: unknown[]
}

export interface AgentDispositionBody {
  version: number
  disposition: 'parked' | 'duplicate' | 'rejected' | 'merged' | 'converted'
  /** grounds — required by acts.ts (D-PEC-10 rider: no groundless dispositions) */
  note: string
  mergedIntoIntakeId?: number
  records?: AgentConversionRecords
}

/** URL paths the agent must never call (rider 4; RBAC stays the real gate). */
const DENYLIST_PATH = [/\/accept$/, /\/apply$/, /\/outcome$/, /\/supersede$/, /\/waive$/]

/** any key, at any depth, that would create an approval record via conversion */
const FORBIDDEN_PAYLOAD_KEYS = ['approvalRecords', 'approval_records']

function payloadNamesForbiddenKey(value: unknown): string | null {
  if (value == null || typeof value !== 'object') return null
  if (Array.isArray(value)) {
    for (const v of value) {
      const hit = payloadNamesForbiddenKey(v)
      if (hit) return hit
    }
    return null
  }
  for (const [k, v] of Object.entries(value as Record<string, unknown>)) {
    if (FORBIDDEN_PAYLOAD_KEYS.includes(k)) return k
    const hit = payloadNamesForbiddenKey(v)
    if (hit) return hit
  }
  return null
}

export class PecAgentClient {
  private readonly cfg: ProjectAdapterConfig | SidecarConfig
  private cookie: string | null = null
  private identity: AgentIdentity | null = null
  private readonly acceptProbeDone = new Set<number>()

  constructor(cfg: ProjectAdapterConfig | SidecarConfig) {
    // refused by construction, independent of loadConfig (defense in depth)
    assertLoopbackBaseUrl(cfg.pecBaseUrl)
    this.cfg = cfg
  }

  whoami(): AgentIdentity | null {
    return this.identity
  }

  /** POST /api/auth/login as the provisioned agent person; cookie kept in memory only. */
  async login(): Promise<AgentIdentity> {
    if (!this.cfg.agentEmail || !this.cfg.agentPassword) {
      throw new AgentClientError('AGENT_NOT_CONFIGURED',
        'PEC_AGENT_EMAIL / PEC_AGENT_PASSWORD are not configured')
    }
    const res = await fetch(`${this.cfg.pecBaseUrl}/api/auth/login`, {
      method: 'POST',
      redirect: 'manual',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ email: this.cfg.agentEmail, password: this.cfg.agentPassword }),
    })
    if (res.status >= 300 && res.status < 400) {
      throw new AgentClientError(
        'AGENT_REDIRECT_REFUSED',
        'agent login refused an HTTP redirect',
      )
    }
    if (res.status !== 200) {
      // credentials never echoed into errors
      throw new AgentClientError('AGENT_LOGIN_FAILED', `agent login refused (HTTP ${res.status})`)
    }
    const setCookie = res.headers.get('set-cookie') ?? ''
    const pair = setCookie.split(';')[0] ?? ''
    if (!pair.startsWith('pec_session=')) {
      throw new AgentClientError('AGENT_LOGIN_FAILED', 'agent login returned no session cookie')
    }
    this.cookie = pair
    const body = await res.json() as { me: { personId: number; name: string; email: string; isAdmin: boolean } }
    if (body.me.isAdmin === true) {
      this.cookie = null
      throw new AgentClientError('AGENT_MISPROVISIONED',
        'the agent person is an instance admin — refusing to operate (rider 3)')
    }
    this.identity = { personId: body.me.personId, name: body.me.name, email: body.me.email }
    return this.identity
  }

  /**
   * The single low-level request helper. All guards live here:
   * denylist BEFORE any network call; 401 → one re-login then replay.
   */
  private async request(method: string, path: string, body?: unknown): Promise<{ status: number; body: unknown }> {
    const [pathname, query = ''] = path.split('?', 2) as [string, string?]
    for (const re of DENYLIST_PATH) {
      if (re.test(pathname)) {
        throw new AgentClientError('AGENT_FORBIDDEN_ACT',
          `the agent never calls ${pathname} — accept/apply/outcome/supersede/waive are human acts (rider 4)`)
      }
    }
    if (/(^|&)force=/.test(query)) {
      throw new AgentClientError('AGENT_FORBIDDEN_ACT', 'the agent never uses force (rider 4)')
    }
    if (body != null && typeof body === 'object' && (body as Record<string, unknown>).force === true) {
      throw new AgentClientError('AGENT_FORBIDDEN_ACT', 'the agent never uses force (rider 4)')
    }
    if (!this.cookie) throw new AgentClientError('AGENT_NOT_LOGGED_IN', 'login() first')

    const doFetch = async (): Promise<Response> => {
      try {
        return await fetch(`${this.cfg.pecBaseUrl}${path}`, {
          method,
          redirect: 'manual',
          headers: {
            cookie: this.cookie!,
            ...(body !== undefined
              ? { 'content-type': typeof body === 'string' ? 'text/csv' : 'application/json' }
              : {}),
          },
          body: body === undefined ? undefined : typeof body === 'string' ? body : JSON.stringify(body),
        })
      } catch (e) {
        throw new AgentClientError('AGENT_PEC_UNREACHABLE',
          `pec server unreachable at ${this.cfg.pecBaseUrl}: ${e instanceof Error ? e.message : String(e)}`)
      }
    }
    let res = await doFetch()
    if (res.status >= 300 && res.status < 400) {
      throw new AgentClientError(
        'AGENT_REDIRECT_REFUSED',
        'PEC request refused an HTTP redirect',
      )
    }
    if (res.status === 401) {
      // session expired: one re-login, then replay — never a retry loop
      await this.login()
      res = await doFetch()
      if (res.status >= 300 && res.status < 400) {
        throw new AgentClientError(
          'AGENT_REDIRECT_REFUSED',
          'PEC request refused an HTTP redirect',
        )
      }
    }
    const text = await res.text()
    let parsed: unknown = text
    try { parsed = JSON.parse(text) } catch { /* csv/html stays text */ }
    return { status: res.status, body: parsed }
  }

  private toResult<T>(r: { status: number; body: unknown }): ApiResult<T> {
    if (r.status >= 200 && r.status < 300) return { ok: true, value: r.body as T }
    const err = (r.body as { error?: { code?: string; message?: string; details?: unknown } })?.error
    if (r.status === 409 && err?.code === 'STALE_PROPOSAL') {
      return { ok: false, kind: 'stale', details: err.details ?? null }
    }
    if (r.status === 403) {
      return { ok: false, kind: 'forbidden', message: err?.message ?? 'forbidden' }
    }
    throw new AgentClientError(err?.code ?? `HTTP_${r.status}`,
      err?.message ?? `unexpected HTTP ${r.status}`, err?.details)
  }

  /**
   * Misprovisioning probe (rider 3): once per project, before the first
   * mutating act — an agent person that CAN import.accept is misprovisioned.
   */
  private async assertNotAcceptCapable(pid: number): Promise<void> {
    if (this.acceptProbeDone.has(pid)) return
    const probe = await this.can(pid, 'import.accept')
    if (probe.allowed) {
      throw new AgentClientError('AGENT_MISPROVISIONED',
        'the agent person may import.accept — refusing to operate (rider 3)')
    }
    this.acceptProbeDone.add(pid)
  }

  // ---------- proposal family (import.propose authority) ----------

  async propose(pid: number, contract: string, csv: string, filename?: string,
    coverage?: { start?: string; end?: string }, extras?: Record<string, unknown>): Promise<ApiResult<ProposalView>> {
    await this.assertNotAcceptCapable(pid)
    const qs = new URLSearchParams({ contract })
    if (filename) qs.set('filename', filename)
    // D-PEC-39: the PE's declared coverage rides the proposal verbatim; never inferred here
    if (coverage?.start) qs.set('coverage_start', coverage.start)
    if (coverage?.end) qs.set('coverage_end', coverage.end)
    // D-PEC-41 full-fidelity capture: verbatim non-tabular source content (e.g. every
    // workbook sheet) rides the proposal as JSON { csv, extras } → source_extras
    const body = extras && Object.keys(extras).length > 0 ? { csv, extras } : csv
    return this.toResult(await this.request('POST', `/api/projects/${pid}/import-proposals?${qs}`, body))
  }

  async refresh(pid: number, id: number, version: number): Promise<ApiResult<ProposalView>> {
    await this.assertNotAcceptCapable(pid)
    return this.toResult(await this.request('POST', `/api/projects/${pid}/import-proposals/${id}/refresh`, { version }))
  }

  /**
   * Withdraw = reject-of-OWN only: the client refuses before the network when
   * the proposal is not the agent's (server enforces the same via RV-16).
   */
  async withdrawOwn(pid: number, id: number, version: number, reason: string): Promise<ApiResult<ProposalView>> {
    await this.assertNotAcceptCapable(pid)
    const current = await this.getProposal(pid, id)
    if (!current.ok) return current
    const me = this.identity
    if (!me || current.value.createdBy !== me.personId) {
      throw new AgentClientError('AGENT_FORBIDDEN_ACT',
        'the agent withdraws only its own proposals — rejecting others\' is a human act (rider 4)')
    }
    return this.toResult(await this.request('POST', `/api/projects/${pid}/import-proposals/${id}/reject`, { version, reason }))
  }

  async listProposals(pid: number): Promise<ApiResult<ProposalSummary[]>> {
    return this.toResult(await this.request('GET', `/api/projects/${pid}/import-proposals`))
  }

  async getProposal(pid: number, id: number): Promise<ApiResult<ProposalView>> {
    return this.toResult(await this.request('GET', `/api/projects/${pid}/import-proposals/${id}`))
  }

  // ---------- intake family (intake.triage authority) ----------

  async listIntake(pid: number, state?: string): Promise<ApiResult<IntakeItemView[]>> {
    const qs = state ? `?state=${encodeURIComponent(state)}` : ''
    return this.toResult(await this.request('GET', `/api/projects/${pid}/intake${qs}`))
  }

  async openTriage(pid: number, id: number, version: number): Promise<ApiResult<IntakeItemView>> {
    await this.assertNotAcceptCapable(pid)
    return this.toResult(await this.request('POST', `/api/projects/${pid}/intake/${id}/open-triage`, { version }))
  }

  /**
   * GOV MAJOR-1 runtime guard (engine-independent, test-pinned, non-negotiable):
   * a disposition payload naming approval records is refused with the typed
   * AGENT_FORBIDDEN_ACT BEFORE any network call — this act rides the legitimate
   * triage route, so the URL denylist cannot catch it; conversion under
   * skipPermission could otherwise create approval records the D-PEC-10 rider
   * forbids the agent to create. The future SDK engine inherits this guard.
   */
  async disposition(pid: number, id: number, body: AgentDispositionBody): Promise<ApiResult<{ intake: IntakeItemView; created: unknown[] }>> {
    const forbidden = payloadNamesForbiddenKey(body)
    if (forbidden) {
      throw new AgentClientError('AGENT_FORBIDDEN_ACT',
        `disposition payload names ${forbidden} — the agent never creates approval records (GOV MAJOR-1; D-PEC-10 rider)`)
    }
    await this.assertNotAcceptCapable(pid)
    return this.toResult(await this.request('POST', `/api/projects/${pid}/intake/${id}/triage`, body))
  }

  // ---------- enumerated reads (D-T0-20 O-B; used by acts.ts under the clamp) ----------

  async historyFor(pid: number, recordType: string, id: number): Promise<ApiResult<unknown[]>> {
    return this.toResult(await this.request('GET', `/api/projects/${pid}/history/${recordType}/${id}`))
  }

  // ---------- broad-basis reads (D-PEC-20 item 3; D-T0-21 O-B) ----------
  // Every route below is an EXISTING RBAC'd GET on the pec server — zero
  // server change. acts.ts applies the basis gate BEFORE any of these run
  // for a model-provider engine; visibility stays the agent person's own RBAC.

  async overview(pid: number): Promise<ApiResult<unknown>> {
    return this.toResult(await this.request('GET', `/api/projects/${pid}/overview`))
  }

  /** register name → its existing GET route (read-only list views) */
  static readonly REGISTER_ROUTES: Record<string, string> = {
    deliverables: 'deliverables',
    packages: 'packages',
    plan: 'plan',
    'my-week': 'my-week',
    holds: 'holds',
    approvals: 'approval-register',
    decisions: 'decisions',
    risks: 'risks',
    tracker: 'tracker',
    interfaces: 'interfaces',
    log: 'log',
  }

  async readRegister(pid: number, register: string): Promise<ApiResult<unknown>> {
    const route = PecAgentClient.REGISTER_ROUTES[register]
    if (!route) {
      throw new AgentClientError('AGENT_UNMAPPED_READ',
        `no register read mapped for '${register}' (one of: ${Object.keys(PecAgentClient.REGISTER_ROUTES).join(', ')})`)
    }
    return this.toResult(await this.request('GET', `/api/projects/${pid}/${route}`))
  }

  async explainRevision(pid: number, id: number): Promise<ApiResult<unknown>> {
    return this.toResult(await this.request('GET', `/api/projects/${pid}/revisions/${id}/explain`))
  }

  async sponsorBrief(pid: number): Promise<ApiResult<unknown>> {
    return this.toResult(await this.request('GET', `/api/projects/${pid}/reports/sponsor-brief`))
  }

  async packagePack(pid: number, id: number): Promise<ApiResult<unknown>> {
    return this.toResult(await this.request('GET', `/api/projects/${pid}/reports/package-pack/${id}`))
  }

  async standardReport(pid: number, report: string, groupBy?: string, period?: { start: string; end: string }): Promise<ApiResult<unknown>> {
    const q = new URLSearchParams()
    if (groupBy) q.set('groupBy', groupBy)
    if (period) {
      q.set('period_start', period.start)
      q.set('period_end', period.end)
    }
    const qs = q.size > 0 ? `?${q}` : ''
    return this.toResult(await this.request('GET', `/api/projects/${pid}/reports/standard/${report}${qs}`))
  }

  async packages(pid: number): Promise<ApiResult<unknown[]>> {
    return this.toResult(await this.request('GET', `/api/projects/${pid}/packages`))
  }

  async packageDetail(pid: number, id: number): Promise<ApiResult<unknown>> {
    return this.toResult(await this.request('GET', `/api/projects/${pid}/packages/${id}`))
  }

  async disciplines(pid: number): Promise<ApiResult<unknown[]>> {
    return this.toResult(await this.request('GET', `/api/projects/${pid}/disciplines`))
  }

  async disciplineDetail(pid: number, name: string, period?: { start: string; end: string }): Promise<ApiResult<unknown>> {
    const q = new URLSearchParams()
    if (period) {
      q.set('period_start', period.start)
      q.set('period_end', period.end)
    }
    const qs = q.size > 0 ? `?${q}` : ''
    return this.toResult(await this.request('GET', `/api/projects/${pid}/disciplines/${encodeURIComponent(name)}${qs}`))
  }

  async can(pid: number, action: string): Promise<{ allowed: boolean; reason: string }> {
    const r = this.toResult<{ allowed: boolean; reason: string }>(
      await this.request('GET', `/api/projects/${pid}/can/${action}`))
    if (!r.ok) {
      // a refused probe read means "not allowed" — report, never escalate
      return { allowed: false, reason: r.kind === 'forbidden' ? r.message : 'stale' }
    }
    return r.value
  }

  /**
   * Screen-context record read (acts.ts applies the D-T0-20 clamp BEFORE this
   * is called). Only mapped GET views are reachable; everything the agent sees
   * remains bounded by its own RBAC visibility.
   */
  async screenRead(pid: number, recordType: string, id: number): Promise<ApiResult<unknown>> {
    const routes: Record<string, string> = {
      deliverable: `/api/projects/${pid}/deliverables/${id}`,
      package: `/api/projects/${pid}/packages/${id}`,
      work_item: `/api/projects/${pid}/work-items/${id}`,
      import_proposal: `/api/projects/${pid}/import-proposals/${id}`,
      check: `/api/projects/${pid}/checks/${id}`,
    }
    if (recordType === 'intake_item') {
      const all = await this.listIntake(pid)
      if (!all.ok) return all
      const item = all.value.find((i) => i.id === id)
      if (!item) throw new AgentClientError('NOT_FOUND', `intake item #${id} not visible`)
      return { ok: true, value: item }
    }
    // register-view record types have no per-id GET route; resolve the row out
    // of the existing register view (zero server change — D-PEC-20 item 3)
    const registerOf: Record<string, string> = {
      risk: 'risks',
      decision: 'decisions',
      hold: 'holds',
      approval_record: 'approvals',
      interface_item: 'interfaces',
      package_tracker: 'tracker',
    }
    const reg = registerOf[recordType]
    if (reg) {
      const view = await this.readRegister(pid, reg)
      if (!view.ok) return view
      const rows = Array.isArray(view.value)
        ? view.value
        : (view.value as { rows?: unknown[] })?.rows ?? []
      const row = (rows as Array<{ id?: number }>).find((r) => r?.id === id)
      if (!row) throw new AgentClientError('NOT_FOUND', `${recordType} #${id} not visible`)
      return { ok: true, value: row }
    }
    const route = routes[recordType]
    if (!route) {
      throw new AgentClientError('AGENT_UNMAPPED_READ',
        `no read route mapped for record type '${recordType}'`)
    }
    return this.toResult(await this.request('GET', route))
  }
}
