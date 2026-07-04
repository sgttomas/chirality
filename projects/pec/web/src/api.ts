/**
 * API client. The server is the only source of rules (SPEC §1): this module transports;
 * 409 CONDITIONS_OPEN / VERSION_CONFLICT payloads are surfaced to the UI intact.
 */

export interface ApiError {
  status: number
  code: string
  message: string
  details: any
}

export class PecApiError extends Error {
  status: number
  code: string
  details: any

  constructor(e: ApiError) {
    super(e.message)
    this.status = e.status
    this.code = e.code
    this.details = e.details
  }
}

async function call<T>(method: string, path: string, body?: unknown): Promise<T> {
  const res = await fetch(path, {
    method,
    headers: body !== undefined ? { 'content-type': 'application/json' } : undefined,
    body: body !== undefined ? JSON.stringify(body) : undefined,
    credentials: 'same-origin',
  })
  const text = await res.text()
  let parsed: any = text
  try { parsed = JSON.parse(text) } catch { /* text/csv/html */ }
  if (!res.ok) {
    const err = parsed?.error ?? { code: 'HTTP_' + res.status, message: text || res.statusText, details: null }
    throw new PecApiError({ status: res.status, ...err })
  }
  return parsed as T
}

export const api = {
  get: <T = any>(path: string) => call<T>('GET', path),
  post: <T = any>(path: string, body?: unknown) => call<T>('POST', path, body),
  put: <T = any>(path: string, body?: unknown) => call<T>('PUT', path, body),
}

export interface Me {
  personId: number
  name: string
  email: string
  isAdmin: boolean
}

export interface ProjectRef {
  id: number
  code: string
  name: string
  roles?: string
}

export interface Explain<V = any> {
  value: V
  ruleId: string
  detail: string
  threshold?: string
  contributing: Array<{ recordType: string; id: number; ref: string; why: string }>
}

export type Health = 'green' | 'amber' | 'red'

/** Project-scoped path helper. */
export function p(pid: number | string, rest: string): string {
  return `/api/projects/${pid}/${rest}`
}
