/**
 * Loopback deterministic tool service for the shared runtime.
 *
 * No model, engine selection, conversation, session, delegation, interruption,
 * credential-provider, or residency logic exists on this path.
 */

import { createServer } from 'node:http'
import { timingSafeEqual } from 'node:crypto'
import type { IncomingMessage, Server, ServerResponse } from 'node:http'
import type { ProjectAdapterConfig } from './config.ts'
import type { PecAgentClient } from './pec-client.ts'
import { bindActs } from './acts.ts'
import {
  PEC_ADAPTER_ACTS,
  executePecAdapterAct,
} from './project-adapter.ts'
import type { PecAdapterAct } from './project-adapter.ts'

const MAX_BODY_BYTES = 8 * 1024 * 1024

function sendJson(res: ServerResponse, status: number, data: unknown): void {
  const body = JSON.stringify(data)
  res.writeHead(status, {
    'content-type': 'application/json; charset=utf-8',
    'content-length': Buffer.byteLength(body),
    'x-content-type-options': 'nosniff',
  })
  res.end(body)
}

async function readBody(req: IncomingMessage): Promise<unknown> {
  const chunks: Buffer[] = []
  let bytes = 0
  for await (const chunk of req) {
    bytes += (chunk as Buffer).length
    if (bytes > MAX_BODY_BYTES) throw Object.assign(new Error('request body too large'), { code: 'PAYLOAD_TOO_LARGE' })
    chunks.push(chunk as Buffer)
  }
  if (chunks.length === 0) return null
  try {
    return JSON.parse(Buffer.concat(chunks).toString('utf8'))
  } catch {
    throw Object.assign(new Error('invalid JSON body'), { code: 'BAD_JSON' })
  }
}

export interface ProjectAdapterHttpDeps {
  cfg: ProjectAdapterConfig
  client: PecAgentClient
  configured: boolean
  adapterToken: string
}

function isAuthorized(req: IncomingMessage, expected: string): boolean {
  const raw = req.headers.authorization
  if (typeof raw !== 'string' || !raw.startsWith('Bearer ')) return false
  const received = Buffer.from(raw.slice('Bearer '.length), 'utf8')
  const wanted = Buffer.from(expected, 'utf8')
  return received.length === wanted.length && timingSafeEqual(received, wanted)
}

export function createProjectAdapterHttpServer(deps: ProjectAdapterHttpDeps): Server {
  return createServer(async (req, res) => {
    const url = new URL(req.url ?? '/', 'http://localhost')
    try {
      if (url.pathname.startsWith('/adapter/') && !isAuthorized(req, deps.adapterToken)) {
        sendJson(res, 401, {
          error: {
            code: 'ADAPTER_UNAUTHORIZED',
            message: 'valid project-adapter authorization is required',
          },
        })
        return
      }
      if (req.method === 'GET' && url.pathname === '/adapter/health') {
        const me = deps.client.whoami()
        sendJson(res, 200, {
          ok: true,
          service: 'pec-project-adapter',
          schemaVersion: 'pec.adapter/v1',
          access: deps.cfg.access,
          acts: PEC_ADAPTER_ACTS,
          configured: deps.configured,
          agent: me ? { name: me.name, email: me.email } : null,
        })
        return
      }
      if (url.pathname === '/agent/health' || url.pathname === '/agent/messages') {
        sendJson(res, 410, {
          error: {
            code: 'AGENT_RUNTIME_MIGRATED',
            message: 'PEC no longer owns an agent execution loop; use the root Chirality runtime daemon',
          },
        })
        return
      }
      if (req.method === 'POST' && url.pathname === '/adapter/execute') {
        if (!deps.configured) {
          sendJson(res, 503, {
            error: {
              code: 'ADAPTER_NOT_CONFIGURED',
              message: 'set PEC_AGENT_EMAIL / PEC_AGENT_PASSWORD to the owner-provisioned agent person and restart',
            },
          })
          return
        }
        const raw = await readBody(req)
        if (raw == null || typeof raw !== 'object') throw Object.assign(new Error('JSON body required'), { code: 'BAD_REQUEST' })
        const body = raw as Record<string, unknown>
        const pid = Number(body.pid)
        if (!Number.isInteger(pid) || pid <= 0) throw Object.assign(new Error('pid must be a positive integer'), { code: 'BAD_REQUEST' })
        if (typeof body.act !== 'string') throw Object.assign(new Error('act must be a string'), { code: 'BAD_REQUEST' })
        const acts = bindActs({
          pid,
          // Adapter results are intended for a governed model session. Keep
          // the conservative provider-egress clamp active.
          egress: 'model-provider',
          access: deps.cfg.access,
          client: deps.client,
        })
        const result = await executePecAdapterAct(acts, {
          pid,
          act: body.act as PecAdapterAct,
          input: body.input,
        })
        sendJson(res, 200, result)
        return
      }
      sendJson(res, 404, { error: { code: 'NOT_FOUND', message: `no route: ${req.method} ${url.pathname}` } })
    } catch (error) {
      const code = (error as { code?: string }).code ?? 'ADAPTER_FAILURE'
      const status = code === 'AGENT_FORBIDDEN_ACT' ? 403
        : code === 'PAYLOAD_TOO_LARGE' ? 413
          : code === 'BAD_JSON' || code === 'BAD_REQUEST' ? 400
            : 500
      sendJson(res, status, {
        error: {
          code,
          message: error instanceof Error ? error.message : String(error),
        },
      })
    }
  })
}
