/**
 * Minimal HTTP router over node:http (ADR-002: zero runtime deps).
 * JSON bodies, cookie parsing, path params, centralized error mapping.
 */

import type { IncomingMessage, ServerResponse } from 'node:http'
import { AppError } from './errors.ts'

export interface ReqCtx {
  req: IncomingMessage
  res: ServerResponse
  method: string
  path: string
  params: Record<string, string>
  query: URLSearchParams
  body: unknown
  cookies: Record<string, string>
  /** attached by auth middleware */
  personId?: number
  isInstanceAdmin?: boolean
}

export type Handler = (ctx: ReqCtx) => unknown | Promise<unknown>

interface Route {
  method: string
  segments: string[]
  handler: Handler
}

export class Router {
  private routes: Route[] = []

  on(method: string, pattern: string, handler: Handler): void {
    this.routes.push({ method, segments: pattern.split('/').filter(Boolean), handler })
  }

  get(p: string, h: Handler): void { this.on('GET', p, h) }
  post(p: string, h: Handler): void { this.on('POST', p, h) }
  put(p: string, h: Handler): void { this.on('PUT', p, h) }

  match(method: string, path: string): { handler: Handler; params: Record<string, string> } | null {
    const parts = path.split('/').filter(Boolean)
    outer: for (const r of this.routes) {
      if (r.method !== method || r.segments.length !== parts.length) continue
      const params: Record<string, string> = {}
      for (let i = 0; i < parts.length; i++) {
        const seg = r.segments[i]!
        const part = decodeURIComponent(parts[i]!)
        if (seg.startsWith(':')) params[seg.slice(1)] = part
        else if (seg !== part) continue outer
      }
      return { handler: r.handler, params }
    }
    return null
  }
}

export function parseCookies(header: string | undefined): Record<string, string> {
  const out: Record<string, string> = {}
  if (!header) return out
  for (const pair of header.split(';')) {
    const idx = pair.indexOf('=')
    if (idx > 0) out[pair.slice(0, idx).trim()] = decodeURIComponent(pair.slice(idx + 1).trim())
  }
  return out
}

export async function readBody(req: IncomingMessage, maxBytes = 25 * 1024 * 1024): Promise<unknown> {
  const chunks: Buffer[] = []
  let size = 0
  for await (const chunk of req) {
    size += (chunk as Buffer).length
    if (size > maxBytes) throw new AppError(413, 'PAYLOAD_TOO_LARGE', 'request body too large')
    chunks.push(chunk as Buffer)
  }
  if (chunks.length === 0) return null
  const text = Buffer.concat(chunks).toString('utf8')
  const type = req.headers['content-type'] ?? ''
  if (type.includes('application/json')) {
    try { return JSON.parse(text) } catch { throw new AppError(400, 'BAD_JSON', 'invalid JSON body') }
  }
  return text
}

export function sendJson(res: ServerResponse, status: number, data: unknown): void {
  const body = JSON.stringify(data)
  res.writeHead(status, {
    'content-type': 'application/json; charset=utf-8',
    'content-length': Buffer.byteLength(body),
    'x-content-type-options': 'nosniff',
  })
  res.end(body)
}

export function errorPayload(e: unknown): { status: number; body: unknown } {
  if (e instanceof AppError) {
    return { status: e.status, body: { error: { code: e.code, message: e.message, details: e.details } } }
  }
  console.error(e)
  return { status: 500, body: { error: { code: 'INTERNAL', message: 'internal server error', details: null } } }
}
