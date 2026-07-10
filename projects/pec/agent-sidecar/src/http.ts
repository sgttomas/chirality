/**
 * The sidecar's own loopback-only HTTP surface (D-PEC-17):
 *   GET  /agent/health   → { ok, engine, egress, configured, agent }
 *   POST /agent/messages → { events: AgentEvent[] }  (body: AgentTurnInput, ≤ 8 MiB)
 *
 * Bound to 127.0.0.1 only. Turn errors map to turn:error EVENTS, not 5xx —
 * transport errors stay transport errors. Unconfigured credentials → 503
 * AGENT_NOT_CONFIGURED (npm run dev works out of the box; scope item 8).
 */

import { createServer } from 'node:http'
import type { IncomingMessage, Server, ServerResponse } from 'node:http'
import type { SidecarConfig } from './config.ts'
import type { PecAgentClient } from './pec-client.ts'
import type { AgentEnginePort, AgentEvent, AgentStreamEvent, AgentTurnInput } from './engine/port.ts'
import { bindActs } from './acts.ts'

/** holds a 5 MiB attachment even base64-encoded (×4/3) plus JSON overhead */
const MAX_BODY_BYTES = 8 * 1024 * 1024
/**
 * D-PEC-35 O-A: CSV/TSV/plain tabular text, normalized to CSV before proposal
 * filing; D-PEC-42 O-A adds `.xlsx` workbooks as base64 bytes (decoded size
 * capped here), parsed zero-dep in the sidecar onto the same lane.
 */
const MAX_ATTACHMENT_BYTES = 5 * 1024 * 1024
/** D-PEC-21 item 2: request-borne conversation history caps */
const MAX_HISTORY_ENTRIES = 40
const MAX_HISTORY_ENTRY_BYTES = 8 * 1024

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

/** app-dev harness wire shape: event type + JSON data, one SSE frame. */
function sendSseEvent(res: ServerResponse, event: AgentStreamEvent): void {
  if (!res.destroyed && !res.writableEnded) {
    res.write(`event: ${event.type}\ndata: ${JSON.stringify(event.data)}\n\n`)
  }
}

function legacyStreamEvents(event: AgentEvent): AgentStreamEvent[] {
  switch (event.type) {
    case 'agent:reply':
      return [
        { type: 'model.completed', data: {} },
        { type: 'message.completed', data: { role: 'assistant', source: 'engine', text: event.text, streamed: false } },
      ]
    case 'act:result':
      return [{
        type: event.ok ? 'tool.completed' : 'tool.failed',
        data: { toolName: event.act, act: event.act, ok: event.ok, summary: event.summary, payload: event.payload },
      }]
    case 'act:refused':
      return [{ type: 'tool.failed', data: { toolName: event.act, act: event.act, refused: true, reason: event.reason } }]
    case 'turn:error':
      return [{ type: 'turn.failed', data: { code: event.code, message: event.message } }]
  }
}

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
  if (b.history != null) {
    if (!Array.isArray(b.history)) bad('history must be an array of { who, text }')
    const entries = b.history as Array<Record<string, unknown>>
    if (entries.length > MAX_HISTORY_ENTRIES) {
      bad(`history exceeds the ${MAX_HISTORY_ENTRIES}-entry cap (send the most recent turns only)`)
    }
    turn.history = entries.map((h) => {
      if (h == null || typeof h !== 'object' || (h.who !== 'you' && h.who !== 'agent') || typeof h.text !== 'string') {
        bad("each history entry must be { who: 'you'|'agent', text: string }")
      }
      if (Buffer.byteLength(h.text as string, 'utf8') > MAX_HISTORY_ENTRY_BYTES) {
        bad(`a history entry exceeds the ${MAX_HISTORY_ENTRY_BYTES}-byte cap`)
      }
      return { who: h.who as 'you' | 'agent', text: h.text as string }
    })
  }
  if (b.attachment != null) {
    const a = b.attachment as Record<string, unknown>
    if (typeof a.name !== 'string') bad('attachment must be { name, text } or { name, base64 }')
    const name = a.name as string
    if (/\.xlsx$/i.test(name)) {
      // D-PEC-42 O-A: .xlsx workbooks arrive as base64 bytes
      if (typeof a.base64 !== 'string' || (a.base64 as string).length === 0) {
        bad('a .xlsx attachment must be { name, base64 } (base64-encoded workbook bytes — D-PEC-42 O-A)')
      }
      const base64 = a.base64 as string
      const bytes = Buffer.from(base64, 'base64')
      if (bytes.length === 0 || bytes.toString('base64').replace(/=+$/, '') !== base64.replace(/[\r\n\s]/g, '').replace(/=+$/, '')) {
        bad('a .xlsx attachment carries invalid base64')
      }
      if (bytes.length > MAX_ATTACHMENT_BYTES) {
        bad('attachment exceeds the 5 MiB structured-file cap (D-PEC-35 O-A)')
      }
      turn.attachment = { name, base64 }
    } else {
      if (typeof a.text !== 'string') bad('attachment must be { name, text }')
      if (!/\.(csv|tsv|tab|txt)$/i.test(name)) {
        bad('attachment must be a CSV/TSV/plain text tabular file (D-PEC-35 O-A) or a .xlsx workbook (D-PEC-42 O-A)')
      }
      if (Buffer.byteLength(a.text as string, 'utf8') > MAX_ATTACHMENT_BYTES) {
        bad('attachment exceeds the 5 MiB structured-file cap (D-PEC-35 O-A)')
      }
      turn.attachment = { name, text: a.text as string }
    }
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
          // D-T0-22 disclosure: the active session profile is always stated
          session: deps.cfg.session,
          // exact SDK-resolved model appears after its init event; a configured
          // override is available before the first turn.
          model: deps.engine.resolvedModel?.() ?? null,
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
        const wantsStream = String(req.headers.accept ?? '').includes('text/event-stream')
        if (wantsStream) {
          res.writeHead(200, {
            'content-type': 'text/event-stream; charset=utf-8',
            'cache-control': 'no-cache, no-transform',
            connection: 'keep-alive',
            'x-accel-buffering': 'no',
            'x-content-type-options': 'nosniff',
          })
          res.flushHeaders()
          const startedAt = Date.now()
          sendSseEvent(res, { type: 'turn.accepted', data: { engine: deps.engine.subject } })
          sendSseEvent(res, { type: 'turn.started', data: { engine: deps.engine.subject, access: deps.cfg.access, session: deps.cfg.session } })
          if (deps.engine.subject !== 'sdk') {
            sendSseEvent(res, { type: 'adapter.initialized', data: { engine: deps.engine.subject, model: null } })
          }
          try {
            const events = await deps.engine.runTurn(turn, acts, (event) => sendSseEvent(res, event))
            // The deterministic engine still returns its bounded batch. Adapt
            // it at the boundary so both engines share one harness stream.
            if (deps.engine.subject !== 'sdk') {
              // Stub arrays historically place prose before act evidence;
              // harness order is tool evidence first, terminal message second.
              for (const event of events.filter((item) => item.type !== 'agent:reply')) {
                for (const live of legacyStreamEvents(event)) sendSseEvent(res, live)
              }
              const replies = events.filter((item) => item.type === 'agent:reply')
              for (const event of replies) {
                for (const live of legacyStreamEvents(event)) sendSseEvent(res, live)
              }
              if (replies.length === 0) {
                const last = [...events].reverse().find((item) => item.type === 'act:result' || item.type === 'act:refused')
                const text = last?.type === 'act:result' ? last.summary
                  : last?.type === 'act:refused' ? last.reason
                    : ''
                if (text) {
                  sendSseEvent(res, { type: 'model.completed', data: {} })
                  sendSseEvent(res, { type: 'message.completed', data: { role: 'assistant', source: 'engine', text, streamed: false } })
                }
              }
            } else {
              for (const event of events) {
                if (event.type === 'turn:error') for (const live of legacyStreamEvents(event)) sendSseEvent(res, live)
              }
            }
            const failed = events.some((event) => event.type === 'turn:error')
            if (!failed) sendSseEvent(res, { type: 'turn.completed', data: { durationMs: Date.now() - startedAt } })
          } catch (e) {
            const code = (e as { code?: string }).code ?? 'TURN_FAILED'
            sendSseEvent(res, { type: 'turn.failed', data: { code, message: e instanceof Error ? e.message : String(e) } })
          }
          res.end()
          return
        }
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
