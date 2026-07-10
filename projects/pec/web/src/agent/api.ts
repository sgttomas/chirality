/**
 * Panel client for the agent proxy routes (D-PEC-17): thin wrappers over the
 * existing web transport. The AgentEvent/AgentTurnInput types are hand-copied
 * from `agent-sidecar/src/engine/port.ts` (no cross-package import from web
 * to the sidecar — keep the two in step by hand).
 */

import { api, p } from '../api.ts'
import type { ScreenRecord } from './context.tsx'

/** app-dev harness-compatible SSE event subset emitted by PEC (D-PEC-53). */
export type AgentStreamEvent = {
  type:
    | 'turn.accepted' | 'turn.started' | 'turn.completed' | 'turn.failed'
    | 'adapter.initialized'
    | 'model.request.started' | 'model.delta' | 'model.completed'
    | 'message.completed'
    | 'tool.started' | 'tool.completed' | 'tool.failed'
  data: Record<string, unknown>
}

export interface AgentStatus {
  ok: boolean
  engine: string
  egress: string
  /** D-T0-21 O-B disclosure: the launch-selected access basis (D-PEC-21 type cleanup) */
  access?: string
  session?: string
  /** null until SDK init resolves the default model (or an override is configured) */
  model?: string | null
  configured: boolean
  agent: { name: string; email: string } | null
}

// mirrors agent-sidecar/src/engine/port.ts HistoryEntry (D-PEC-21: the
// transcript rides the request; the sidecar stores nothing between requests)
export interface AgentHistoryEntry {
  who: 'you' | 'agent'
  text: string
}

export interface AgentMessageBody {
  message: string
  context?: { route: string; records: ScreenRecord[] }
  attachment?: { name: string; text: string } | { name: string; base64: string }
  history?: AgentHistoryEntry[]
}

export function agentStatus(pid: number): Promise<AgentStatus> {
  return api.get(p(pid, 'agent/status'))
}

function parseSseFrame(frame: string): AgentStreamEvent | null {
  let event = ''
  const dataLines: string[] = []
  for (const line of frame.split('\n')) {
    if (line.startsWith('event:')) event = line.slice('event:'.length).trim()
    else if (line.startsWith('data:')) dataLines.push(line.slice('data:'.length).trimStart())
  }
  if (!event || dataLines.length === 0) return null
  return { type: event as AgentStreamEvent['type'], data: JSON.parse(dataLines.join('\n')) as Record<string, unknown> }
}

/** Derived directly from app-dev's streamHarnessTurn client loop. */
export async function agentMessage(
  pid: number,
  body: AgentMessageBody,
  onEvent: (event: AgentStreamEvent) => void,
): Promise<void> {
  const response = await fetch(p(pid, 'agent/messages'), {
    method: 'POST',
    headers: { 'content-type': 'application/json', accept: 'text/event-stream' },
    body: JSON.stringify(body),
  })
  if (!response.ok) {
    let payload: { error?: { code?: string; message?: string } } = {}
    try { payload = await response.json() as typeof payload } catch { /* use fallback */ }
    const error = new Error(payload.error?.message ?? `agent request failed (${response.status})`) as Error & { code?: string }
    error.code = payload.error?.code ?? 'AGENT_ERROR'
    throw error
  }
  if (!response.body) throw new Error('agent response did not include a stream body')
  const reader = response.body.getReader()
  const decoder = new TextDecoder()
  let buffer = ''
  let terminal = false
  const publish = (event: AgentStreamEvent): void => {
    if (event.type === 'turn.completed' || event.type === 'turn.failed') terminal = true
    onEvent(event)
  }
  while (true) {
    const { done, value } = await reader.read()
    if (done) break
    if (value) buffer += decoder.decode(value, { stream: true })
    while (true) {
      const boundary = buffer.indexOf('\n\n')
      if (boundary < 0) break
      const parsed = parseSseFrame(buffer.slice(0, boundary))
      buffer = buffer.slice(boundary + 2)
      if (parsed) publish(parsed)
    }
  }
  buffer += decoder.decode()
  if (buffer.trim()) {
    const parsed = parseSseFrame(buffer.trim())
    if (parsed) publish(parsed)
  }
  if (!terminal) {
    const error = new Error('agent stream ended before a terminal turn event') as Error & { code?: string }
    error.code = 'AGENT_STREAM_INCOMPLETE'
    throw error
  }
}
