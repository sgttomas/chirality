/**
 * The sidecar's own loopback-only HTTP surface (D-PEC-17):
 *   GET  /agent/health   → { ok, engine, egress, configured, agent }
 *   POST /agent/messages → { events: AgentEvent[] }  (body: AgentTurnInput, ≤ 6 MiB)
 *
 * Bound to 127.0.0.1 only. Turn errors map to turn:error EVENTS, not 5xx —
 * transport errors stay transport errors. Unconfigured credentials → 503
 * AGENT_NOT_CONFIGURED (npm run dev works out of the box; scope item 8).
 */

import { createServer } from 'node:http'
import type { IncomingMessage, Server, ServerResponse } from 'node:http'
import type { SidecarConfig } from './config.ts'
import type { PecAgentClient } from './pec-client.ts'
import type { AgentEnginePort, AgentTurnInput } from './engine/port.ts'
import { bindActs } from './acts.ts'

const MAX_BODY_BYTES = 6 * 1024 * 1024
/** RV-14: CSV only, mirroring the server's proposal cap */
const MAX_ATTACHMENT_BYTES = 5 * 1024 * 1024

function sendJson(res: ServerResponse, status: number, data: unknown): void {
  const body = JSON.stringify(data)
  res.writeHead(status, {
    'content-type': 'application/json; charset=utf-8',
    'content-length': Buffer.byteLength(body),
    'x-content-type-options': 'nosniff',
  })
  res.end(body)
}

const errJson = (res: ServerResponse, status: number, code: string, message: string): void =>
  sendJson(res, status, { error: { code, message } })

async function readJsonBody(req: IncomingMessage): Promise<unknown> {
  const chunks: Buffer[] = []
  let size = 0
  for await (const chunk of req) {
    size += (chunk as Buffer).length
    if (size > MAX_BODY_BYTES) throw Object.assign(new Error('request body too large'), { code: 'PAYLOAD_TOO_LARGE' })
    chunks.push(chunk as Buffer)
  }
  if (chunks.length === 0) return null
  try {
    return JSON.parse(Buffer.concat(chunks).toString('utf8'))
  } catch {
    throw Object.assign(new Error('invalid JSON body'), { code: 'BAD_JSON' })
  }
}

/** validate an AgentTurnInput; throws {code:'BAD_REQUEST'} with a reason */
function validateTurn(body: unknown): AgentTurnInput {
  const bad = (message: string): never => {
    throw Object.assign(new Error(message), { code: 'BAD_REQUEST' })
  }
  if (body == null || typeof body !== 'object') bad('JSON body required')
  const b = body as Record<string, unknown>
  const pid = Number(b.pid)
  if (!Number.isInteger(pid) || pid <= 0) bad('pid (positive integer) required')
  if (typeof b.message !== 'string') bad('message (string) required')
  const turn: AgentTurnInput = { pid, message: b.message as string }
  if (b.context != null) {
    const c = b.context as Record<string, unknown>
    if (typeof c.route !== 'string' || !Array.isArray(c.records)) bad('context must be { route, records[] }')
    turn.context = {
      route: c.route as string,
      records: (c.records as Array<Record<string, unknown>>).map((r) => ({
        recordType: String(r.recordType ?? ''), ref: String(r.ref ?? ''), id: Number(r.id ?? 0),
      })),
    }
  }
  if (b.attachment != null) {
    const a = b.attachment as Record<string, unknown>
    if (typeof a.name !== 'string' || typeof a.text !== 'string') bad('attachment must be { name, text }')
    if (!/\.csv$/i.test(a.name as string)) bad('attachment must be a .csv file (RV-14: CSV-only v1)')
    if (Buffer.byteLength(a.text as string, 'utf8') > MAX_ATTACHMENT_BYTES) {
      bad('attachment exceeds the 5 MiB CSV cap (RV-14)')
    }
    turn.attachment = { name: a.name as string, text: a.text as string }
  }
  return turn
}

export interface SidecarHttpDeps {
  cfg: SidecarConfig
  engine: AgentEnginePort
  client: PecAgentClient
  /** whether credentials are configured AND login succeeded */
  configured: boolean
}

export function createSidecarHttpServer(deps: SidecarHttpDeps): Server {
  return createServer(async (req, res) => {
    const url = new URL(req.url ?? '/', 'http://localhost')
    try {
      if (req.method === 'GET' && url.pathname === '/agent/health') {
        const me = deps.client.whoami()
        sendJson(res, 200, {
          ok: true,
          engine: deps.engine.subject,
          egress: deps.engine.egress,
          // D-T0-21 O-B disclosure: the active access basis is always stated
          access: deps.cfg.access,
          configured: deps.configured,
          agent: me ? { name: me.name, email: me.email } : null,
        })
        return
      }
      if (req.method === 'POST' && url.pathname === '/agent/messages') {
        if (!deps.configured) {
          errJson(res, 503, 'AGENT_NOT_CONFIGURED',
            'set PEC_AGENT_EMAIL / PEC_AGENT_PASSWORD to the owner-provisioned agent person and restart')
          return
        }
        const body = await readJsonBody(req)
        const turn = validateTurn(body)
        const acts = bindActs({ pid: turn.pid, egress: deps.engine.egress, access: deps.cfg.access, client: deps.client })
        try {
          const events = await deps.engine.runTurn(turn, acts)
          sendJson(res, 200, { events })
        } catch (e) {
          // turn errors are events, not 5xx (transport errors stay transport errors)
          const code = (e as { code?: string }).code ?? 'TURN_FAILED'
          sendJson(res, 200, {
            events: [{ type: 'turn:error', code, message: e instanceof Error ? e.message : String(e) }],
          })
        }
        return
      }
      errJson(res, 404, 'NOT_FOUND', `no route: ${req.method} ${url.pathname}`)
    } catch (e) {
      const code = (e as { code?: string }).code
      if (code === 'PAYLOAD_TOO_LARGE') errJson(res, 413, code, (e as Error).message)
      else if (code === 'BAD_JSON' || code === 'BAD_REQUEST') errJson(res, 400, code, (e as Error).message)
      else errJson(res, 500, 'INTERNAL', 'internal sidecar error')
    }
  })
}
