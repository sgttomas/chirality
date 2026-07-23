import { readFile, stat } from 'node:fs/promises'
import { resolve } from 'node:path'

const DEFAULT_ADAPTER_URL = 'http://127.0.0.1:4812'
const MAX_ADAPTER_RESPONSE_BYTES = 4 * 1024 * 1024

export interface PecAdapterContextEvidence {
  source: 'pec-project-adapter'
  act: 'screen.read' | 'read.overview'
  result: unknown
}

export interface PecProjectAdapterClientPort {
  status(): Promise<unknown>
  readContext(pecProjectId: number, context: unknown): Promise<PecAdapterContextEvidence>
}

function adapterFailure(message: string, status = 503, code = 'PROJECT_ADAPTER_UNAVAILABLE'): Error {
  return Object.assign(new Error(message), { status, code })
}

function adapterBaseUrl(env: NodeJS.ProcessEnv): string {
  const raw = (env.PEC_PROJECT_ADAPTER_URL ?? DEFAULT_ADAPTER_URL).trim()
  let url: URL
  try {
    url = new URL(raw)
  } catch {
    throw adapterFailure('PEC project adapter URL is invalid')
  }
  if (
    url.protocol !== 'http:'
    || url.hostname !== '127.0.0.1'
    || url.username
    || url.password
    || url.search
    || url.hash
    || (url.pathname !== '/' && url.pathname !== '')
  ) {
    throw adapterFailure('PEC project adapter must use literal loopback with no URL credentials')
  }
  return url.origin
}

async function adapterToken(env: NodeJS.ProcessEnv): Promise<string> {
  const configured = env.PEC_PROJECT_ADAPTER_TOKEN_FILE?.trim()
  if (!configured) {
    throw adapterFailure('PEC_PROJECT_ADAPTER_TOKEN_FILE is required')
  }
  const path = resolve(configured)
  const info = await stat(path).catch(() => undefined)
  if (!info?.isFile() || (info.mode & 0o077) !== 0) {
    throw adapterFailure('PEC project adapter token file must be a regular mode-0600 file')
  }
  const token = (await readFile(path, 'utf8')).trim()
  if (token.length < 32) {
    throw adapterFailure('PEC project adapter token is invalid')
  }
  return token
}

function screenContext(value: unknown):
  | { route: string; records: Array<{ recordType: string; ref: string; id: number }> }
  | undefined {
  if (!value || typeof value !== 'object' || Array.isArray(value)) return undefined
  const input = value as Record<string, unknown>
  if (typeof input.route !== 'string' || !Array.isArray(input.records)) return undefined
  const records = input.records.map((record) => {
    if (!record || typeof record !== 'object' || Array.isArray(record)) return undefined
    const row = record as Record<string, unknown>
    if (
      typeof row.recordType !== 'string'
      || typeof row.ref !== 'string'
      || !Number.isInteger(row.id)
      || Number(row.id) <= 0
    ) return undefined
    return {
      recordType: row.recordType,
      ref: row.ref,
      id: Number(row.id),
    }
  })
  if (records.some((record) => record === undefined)) return undefined
  return {
    route: input.route,
    records: records as Array<{ recordType: string; ref: string; id: number }>,
  }
}

export function createPecProjectAdapterClient(
  env: NodeJS.ProcessEnv = process.env,
): PecProjectAdapterClientPort {
  const baseUrl = adapterBaseUrl(env)

  const request = async (path: string, init: RequestInit): Promise<unknown> => {
    const token = await adapterToken(env)
    let response: Response
    try {
      response = await fetch(`${baseUrl}${path}`, {
        ...init,
        redirect: 'manual',
        signal: AbortSignal.timeout(15_000),
        headers: {
          accept: 'application/json',
          authorization: `Bearer ${token}`,
          ...(init.body === undefined ? {} : { 'content-type': 'application/json' }),
        },
      })
    } catch {
      throw adapterFailure('PEC project adapter is unavailable on loopback')
    }
    if (response.status >= 300 && response.status < 400) {
      throw adapterFailure('PEC project adapter redirects are forbidden', 502, 'PROJECT_ADAPTER_PROTOCOL')
    }
    if (response.status === 401 || response.status === 403) {
      throw adapterFailure('PEC project adapter authentication failed', 503, 'PROJECT_ADAPTER_AUTH')
    }
    const text = await response.text()
    if (Buffer.byteLength(text, 'utf8') > MAX_ADAPTER_RESPONSE_BYTES) {
      throw adapterFailure('PEC project adapter response exceeded its byte cap', 502, 'PROJECT_ADAPTER_PROTOCOL')
    }
    let payload: unknown
    try {
      payload = text ? JSON.parse(text) : {}
    } catch {
      throw adapterFailure('PEC project adapter returned malformed JSON', 502, 'PROJECT_ADAPTER_PROTOCOL')
    }
    if (!response.ok) {
      const detail = payload as { error?: { message?: unknown; code?: unknown } }
      throw adapterFailure(
        typeof detail.error?.message === 'string'
          ? detail.error.message
          : `PEC project adapter failed with HTTP ${response.status}`,
        response.status,
        typeof detail.error?.code === 'string' ? detail.error.code : 'PROJECT_ADAPTER_FAILURE',
      )
    }
    return payload
  }

  return {
    status() {
      return request('/adapter/health', { method: 'GET' })
    },
    async readContext(pecProjectId, context) {
      const screen = screenContext(context)
      const act = screen === undefined ? 'read.overview' : 'screen.read'
      const result = await request('/adapter/execute', {
        method: 'POST',
        body: JSON.stringify({
          pid: pecProjectId,
          act,
          input: screen ?? {},
        }),
      })
      return {
        source: 'pec-project-adapter',
        act,
        result,
      }
    },
  }
}

export function unavailableProjectAdapterClient(): PecProjectAdapterClientPort {
  const unavailable = (): never => {
    throw adapterFailure('PEC project adapter is not configured')
  }
  return {
    async status() {
      return unavailable()
    },
    async readContext() {
      return unavailable()
    },
  }
}
