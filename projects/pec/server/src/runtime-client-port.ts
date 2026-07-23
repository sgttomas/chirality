/**
 * Structural seam to the root-owned Chirality runtime.
 *
 * This package deliberately does not import @chirality/runtime-client yet:
 * G1 owns that package and the workspace lockfiles. HELP_HUMAN binds the real
 * client to this port after G1 fan-in. Until then the default implementation
 * fails closed; it never falls back to the retired PEC agent loop.
 *
 * The public stream is the existing app harness UIEvent contract. Rich,
 * persisted HarnessEvent records ride provider-neutrally as `harness:event`.
 */

export const PEC_RUNTIME_PROJECT_ID = 'pec' as const
/** Authoritative PEC Agent 1 entry from projects/pec/AGENTS.md. */
export const PEC_AGENT_1_ID = 'WORKING_ITEMS' as const

export const PEC_UI_EVENT_TYPES = [
  'session:init',
  'chat:delta',
  'chat:complete',
  'tool:result',
  'session:complete',
  'turn:error',
  'process:exit',
  'harness:event',
] as const

export type PecUiEventType = (typeof PEC_UI_EVENT_TYPES)[number]

export const PEC_HARNESS_EVENT_TYPES = [
  'session.created',
  'session.resumed',
  'turn.accepted',
  'turn.started',
  'adapter.initialized',
  'message.accepted',
  'message.queued',
  'message.started',
  'message.delta',
  'message.completed',
  'model.request.started',
  'model.delta',
  'model.completed',
  'turn.completed',
  'turn.failed',
  'turn.cancelled',
  'turn.interrupted',
  'tool.queued',
  'tool.permission',
  'tool.started',
  'tool.progress',
  'tool.completed',
  'tool.failed',
  'hook.started',
  'hook.progress',
  'hook.completed',
  'hook.failed',
  'queue.enqueued',
  'queue.consumed',
  'queue.cleared',
  'branch.created',
  'branch.selected',
  'branch.summarized',
  'interruption.requested',
  'interruption.completed',
  'context.compaction.started',
  'context.compacted',
  'context.compaction.failed',
  'subagent.started',
  'subagent.progress',
  'subagent.completed',
  'subagent.failed',
  'coordination.notice',
  'coordination.update',
  'coordination.acknowledged',
  'runtime.mirror.error',
] as const

export type PecHarnessEventType = (typeof PEC_HARNESS_EVENT_TYPES)[number]

export interface PecHarnessEvent {
  schemaVersion: 1
  eventId: string
  sessionId: string
  turnId?: string
  parentEventId?: string
  timestamp: string
  type: PecHarnessEventType
  data: Record<string, unknown>
}

export interface PecUiEvent {
  type: PecUiEventType
  data: Record<string, unknown> | PecHarnessEvent
}

export interface PecRuntimeStatusRequest {
  projectId: typeof PEC_RUNTIME_PROJECT_ID
  pecProjectId: number
}

export interface PecRuntimeRunRequest {
  projectId: typeof PEC_RUNTIME_PROJECT_ID
  role: 'agent1'
  agentId: typeof PEC_AGENT_1_ID
  brief: string
  approvalReference: string
  requestedBy: {
    pecProjectId: number
    personId: number
  }
  localModel?: string
  readOnlyTool?: {
    name: 'read_file'
    relativePath: string
  }
}

export interface PecSharedRuntimeClientPort {
  status(request: PecRuntimeStatusRequest): Promise<unknown>
  runAgent1(request: PecRuntimeRunRequest, signal: AbortSignal): AsyncIterable<PecUiEvent>
}

export interface RuntimeClientFailure {
  status?: number
  code?: string
  message?: string
}

const UI_EVENT_TYPES = new Set<string>(PEC_UI_EVENT_TYPES)
const HARNESS_EVENT_TYPES = new Set<string>(PEC_HARNESS_EVENT_TYPES)

function isRecord(value: unknown): value is Record<string, unknown> {
  return value != null && typeof value === 'object' && !Array.isArray(value)
}

export function assertPecHarnessEvent(value: unknown): asserts value is PecHarnessEvent {
  if (!isRecord(value)) throw new Error('harness:event data is not an object')
  if (value.schemaVersion !== 1) throw new Error('HarnessEvent schemaVersion is not 1')
  if (typeof value.eventId !== 'string' || !value.eventId) throw new Error('HarnessEvent eventId is missing')
  if (typeof value.sessionId !== 'string' || !value.sessionId) throw new Error('HarnessEvent sessionId is missing')
  if (typeof value.timestamp !== 'string' || !value.timestamp) throw new Error('HarnessEvent timestamp is missing')
  if (!HARNESS_EVENT_TYPES.has(String(value.type ?? ''))) {
    throw new Error(`HarnessEvent type is unknown: ${String(value.type ?? '')}`)
  }
  if (!isRecord(value.data)) throw new Error('HarnessEvent data is not an object')
}

export function assertPecUiEvent(value: unknown): asserts value is PecUiEvent {
  if (!isRecord(value)) throw new Error('runtime emitted a non-object UIEvent')
  if (!UI_EVENT_TYPES.has(String(value.type ?? ''))) {
    throw new Error(`runtime emitted an unknown public UIEvent type: ${String(value.type ?? '')}`)
  }
  if (!isRecord(value.data)) throw new Error('runtime UIEvent data is not an object')
  if (value.type === 'harness:event') assertPecHarnessEvent(value.data)
  if (value.type === 'session:init') {
    const data = value.data
    if (
      typeof data.engineSessionId !== 'string'
      || typeof data.adapterId !== 'string'
      || typeof data.providerId !== 'string'
      || typeof data.model !== 'string'
    ) {
      throw new Error('session:init is missing provider-neutral engine/model attribution')
    }
  }
  if ((value.type === 'chat:delta' || value.type === 'chat:complete') && typeof value.data.text !== 'string') {
    throw new Error(`${value.type} data.text is missing`)
  }
  if (
    value.type === 'tool:result'
    && (
      typeof value.data.name !== 'string'
      || typeof value.data.ok !== 'boolean'
      || (value.data.output != null && typeof value.data.output !== 'string')
    )
  ) {
    throw new Error('tool:result data is invalid')
  }
  if (value.type === 'process:exit' && !Number.isInteger(value.data.exitCode)) {
    throw new Error('process:exit data.exitCode is invalid')
  }
}

export function unavailableRuntimeClient(): PecSharedRuntimeClientPort {
  const unavailable = (): never => {
    throw Object.assign(
      new Error('the Chirality runtime daemon client is not bound; install/start the daemon and complete runtime-client fan-in'),
      { status: 503, code: 'AGENT_UNAVAILABLE' },
    )
  }
  return {
    status: async () => unavailable(),
    runAgent1: () => ({
      async *[Symbol.asyncIterator]() {
        unavailable()
      },
    }),
  }
}
