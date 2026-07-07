/**
 * Panel client for the agent proxy routes (D-PEC-17): thin wrappers over the
 * existing web transport. The AgentEvent/AgentTurnInput types are hand-copied
 * from `agent-sidecar/src/engine/port.ts` (no cross-package import from web
 * to the sidecar — keep the two in step by hand).
 */

import { api, p } from '../api.ts'
import type { ScreenRecord } from './context.tsx'

// mirrors agent-sidecar/src/engine/port.ts AgentEvent
export type AgentEvent =
  | { type: 'agent:reply'; text: string }
  | { type: 'act:result'; act: string; ok: boolean; summary: string; payload?: unknown }
  | { type: 'act:refused'; act: string; reason: string }
  | { type: 'turn:error'; code: string; message: string }

export interface AgentStatus {
  ok: boolean
  engine: string
  egress: string
  /** D-T0-21 O-B disclosure: the launch-selected access basis (D-PEC-21 type cleanup) */
  access?: string
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
  attachment?: { name: string; text: string }
  history?: AgentHistoryEntry[]
}

export function agentStatus(pid: number): Promise<AgentStatus> {
  return api.get(p(pid, 'agent/status'))
}

export function agentMessage(pid: number, body: AgentMessageBody): Promise<{ events: AgentEvent[] }> {
  return api.post(p(pid, 'agent/messages'), body)
}
