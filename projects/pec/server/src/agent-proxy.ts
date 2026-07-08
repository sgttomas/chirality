/**
 * Agent sidecar proxy (D-PEC-17): a narrow hand-rolled node:http forwarder —
 * zero new server dependencies (ADR-002 by construction). It NEVER forwards
 * inbound headers: every outbound request is fresh with a JSON body only, so
 * the human's pec_session cookie cannot reach the sidecar (the sidecar acts
 * under its own agent-person session, never the human's). Sidecar down →
 * 503 AGENT_UNAVAILABLE; sidecar non-2xx JSON is relayed with its status.
 */

import { request as httpRequest } from 'node:http'
import { AppError } from './errors.ts'

export interface AgentProxyTarget {
  host: '127.0.0.1'
  port: number
}

/** 6 MiB payload cap (attachment ≤ the 5 MiB RV-14 proposal cap rides inside) */
const MAX_PAYLOAD_BYTES = 6 * 1024 * 1024
const STATUS_TIMEOUT_MS = 800
/** D-PEC-21 item 4: agentic multi-act turns outlive the old 60 s constant */
const DEFAULT_MESSAGE_TIMEOUT_MS = 300_000

/**
 * Message timeout: PEC_AGENT_MESSAGE_TIMEOUT_MS (default 300 000). Read
 * per-request like agentTargetFromEnv, so tests can repoint it.
 */
export function messageTimeoutFromEnv(env: Record<string, string | undefined> = process.env): number {
  const raw = env.PEC_AGENT_MESSAGE_TIMEOUT_MS?.trim()
  if (!raw) return DEFAULT_MESSAGE_TIMEOUT_MS
  const ms = Number(raw)
  if (!Number.isInteger(ms) || ms <= 0) {
    throw new AppError(500, 'AGENT_MISCONFIGURED', 'PEC_AGENT_MESSAGE_TIMEOUT_MS must be a positive integer (milliseconds)')
  }
  return ms
}

/**
 * Where the proxy finds the sidecar: PEC_AGENT_URL (must be loopback) or
 * PEC_AGENT_PORT, default 4812. Read per-request so tests can repoint it.
 */
export function agentTargetFromEnv(env: Record<string, string | undefined> = process.env): AgentProxyTarget {
  const raw = env.PEC_AGENT_URL?.trim()
  if (raw) {
    let url: URL
    try {
      url = new URL(raw)
    } catch {
      throw new AppError(500, 'AGENT_MISCONFIGURED', `PEC_AGENT_URL is not a valid URL`)
    }
    if (!['127.0.0.1', 'localhost', '::1', '[::1]'].includes(url.hostname.toLowerCase())) {
      throw new AppError(500, 'AGENT_MISCONFIGURED', 'PEC_AGENT_URL must be loopback (D-T0-19 O-2A)')
    }
    return { host: '127.0.0.1', port: Number(url.port || 4812) }
  }
  return { host: '127.0.0.1', port: Number(env.PEC_AGENT_PORT ?? 4812) }
}

function forward(
  target: AgentProxyTarget,
  method: 'GET' | 'POST',
  path: string,
  payload: unknown,
  timeoutMs: number,
): Promise<unknown> {
  return new Promise((resolve, reject) => {
    const body = payload === undefined ? undefined : JSON.stringify(payload)
    if (body !== undefined && Buffer.byteLength(body, 'utf8') > MAX_PAYLOAD_BYTES) {
      reject(new AppError(413, 'PAYLOAD_TOO_LARGE', 'agent message exceeds the 6 MiB cap'))
      return
    }
    const unavailable = (why: string): AppError =>
      new AppError(503, 'AGENT_UNAVAILABLE', `the agent sidecar is not reachable (${why}); start it with npm run dev:agent`)
    // a FRESH request: no inbound header is ever forwarded (cookie-stripping by construction)
    const req = httpRequest({
      host: target.host,
      port: target.port,
      method,
      path,
      headers: body === undefined ? {} : {
        'content-type': 'application/json',
        'content-length': Buffer.byteLength(body, 'utf8'),
      },
      timeout: timeoutMs,
    }, (res) => {
      const chunks: Buffer[] = []
      res.on('data', (c: Buffer) => chunks.push(c))
      res.on('end', () => {
        const text = Buffer.concat(chunks).toString('utf8')
        let parsed: unknown = text
        try { parsed = JSON.parse(text) } catch { /* relay as text */ }
        const status = res.statusCode ?? 502
        if (status >= 200 && status < 300) {
          resolve(parsed)
          return
        }
        // relay the sidecar's own error with its status
        const err = (parsed as { error?: { code?: string; message?: string } })?.error
        reject(new AppError(status, err?.code ?? 'AGENT_ERROR', err?.message ?? `agent sidecar returned HTTP ${status}`))
      })
    })
    req.on('timeout', () => {
      req.destroy(new Error('timeout'))
    })
    req.on('error', (e) => {
      reject(e instanceof AppError ? e : unavailable(e.message))
    })
    if (body !== undefined) req.write(body)
    req.end()
  })
}

/** GET /agent/health (800 ms timeout) */
export function agentStatus(target: AgentProxyTarget): Promise<unknown> {
  return forward(target, 'GET', '/agent/health', undefined, STATUS_TIMEOUT_MS)
}

/** POST /agent/messages — JSON body only; the caller injects the server-side pid */
export function agentMessage(target: AgentProxyTarget, payload: unknown): Promise<unknown> {
  return forward(target, 'POST', '/agent/messages', payload, messageTimeoutFromEnv())
}
