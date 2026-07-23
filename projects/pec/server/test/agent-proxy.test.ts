/**
 * D-PEC-56 shared-runtime compatibility proxy.
 *
 * Pins: PEC RBAC + same-origin boundary, one injected runtime-client path,
 * scratch/demo-only execution, canonical SSE preservation and attribution,
 * server-owned project/actor routing, and fail-closed daemon failures with no
 * PEC state mutation or retired-sidecar fallback.
 */

import { after, before, test } from 'node:test'
import assert from 'node:assert/strict'
import { createTestEnv } from './harness.ts'
import type { TestEnv } from './harness.ts'
import {
  isScratchOrDemoDatabasePath,
  runtimeRunRequest,
} from '../src/agent-proxy.ts'
import { toDaemonAgent1RunRequest } from '../src/shared-runtime-client.ts'
import type {
  PecHarnessEvent,
  PecHarnessEventType,
  PecUiEvent,
  PecRuntimeRunRequest,
  PecRuntimeStatusRequest,
  PecSharedRuntimeClientPort,
} from '../src/runtime-client-port.ts'
import type { PecProjectAdapterClientPort } from '../src/project-adapter-client.ts'
import { AppError } from '../src/errors.ts'

const runtimeCalls: Array<
  | { kind: 'status'; request: PecRuntimeStatusRequest }
  | { kind: 'run'; request: PecRuntimeRunRequest }
> = []
let runtimeFailure: Error & { status?: number; code?: string } | null = null
let emitted: PecUiEvent[] = []
const adapterCalls: Array<{ kind: 'status' } | { kind: 'read'; projectId: number; context: unknown }> = []

const runtimeClient: PecSharedRuntimeClientPort = {
  async status(request) {
    runtimeCalls.push({ kind: 'status', request })
    if (runtimeFailure) throw runtimeFailure
    return {
      ok: true,
      configured: true,
      projectId: request.projectId,
      daemon: { status: 'ready' },
      engine: 'shared-runtime',
      model: 'manager-model',
    }
  },
  runAgent1(request, signal) {
    runtimeCalls.push({ kind: 'run', request })
    return {
      async *[Symbol.asyncIterator]() {
        if (runtimeFailure) throw runtimeFailure
        for (const event of emitted) {
          if (signal.aborted) return
          yield event
        }
      },
    }
  },
}

const projectAdapterClient: PecProjectAdapterClientPort = {
  async status() {
    adapterCalls.push({ kind: 'status' })
    return {
      ok: true,
      service: 'pec-project-adapter',
      schemaVersion: 'pec.adapter/v1',
      configured: true,
      agent: { name: 'PEC Agent', email: 'agent@t.co' },
    }
  },
  async readContext(projectId, context) {
    adapterCalls.push({ kind: 'read', projectId, context })
    return {
      source: 'pec-project-adapter',
      act: 'read.overview',
      result: { kind: 'result', act: 'read.overview', payload: { projectId } },
    }
  },
}

let env: TestEnv
let P = ''

function event(type: PecUiEvent['type'], data: Record<string, unknown> | PecHarnessEvent): PecUiEvent {
  return {
    type,
    data,
  }
}

function harnessEvent(
  eventId: string,
  type: PecHarnessEventType,
  data: Record<string, unknown>,
): PecHarnessEvent {
  return {
    schemaVersion: 1,
    eventId,
    sessionId: 'session-a1',
    turnId: 'turn-1',
    timestamp: '2026-07-22T00:00:00.000Z',
    type,
    data,
  }
}

before(async () => {
  env = await createTestEnv({ runtimeClient, projectAdapterClient })
  P = `/api/projects/${env.projectId}`
})

after(async () => {
  await env.close()
})

test('401 unauthenticated and 403 without agent.direct never reach the daemon client', async () => {
  runtimeCalls.length = 0
  adapterCalls.length = 0
  const unauthenticated = await fetch(`${env.base}${P}/agent/status`)
  assert.equal(unauthenticated.status, 401)

  const contributor = await env.as('ic@t.co')
  assert.equal((await contributor.get(`${P}/agent/status`)).status, 403)
  assert.equal((await contributor.post(`${P}/agent/messages`, { message: 'hi' })).status, 403)

  const documentController = await env.as('dc@t.co')
  const dc = await documentController.get(`${P}/agent/status`)
  assert.equal(dc.status, 403)
  assert.match(dc.body.error.message, /agent.direct/)
  assert.equal(runtimeCalls.length, 0)
  assert.equal(adapterCalls.length, 0)
})

test('404 wrong PEC project never reaches the daemon client', async () => {
  runtimeCalls.length = 0
  adapterCalls.length = 0
  const admin = await env.as('admin@t.co')
  const response = await admin.get('/api/projects/9999/agent/status')
  assert.equal(response.status, 404)
  assert.equal(runtimeCalls.length, 0)
  assert.equal(adapterCalls.length, 0)
})

test('cross-origin POST is refused before runtime invocation', async () => {
  runtimeCalls.length = 0
  adapterCalls.length = 0
  const login = await fetch(`${env.base}/api/auth/login`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ email: 'pm@t.co', password: 'pilot' }),
  })
  const cookie = (login.headers.get('set-cookie') ?? '').split(';')[0]!
  const response = await fetch(`${env.base}${P}/agent/messages`, {
    method: 'POST',
    headers: {
      cookie,
      origin: 'https://evil.example.com',
      'content-type': 'application/json',
    },
    body: JSON.stringify({ message: 'hi' }),
  })
  assert.equal(response.status, 403)
  assert.equal((await response.json() as { error: { code: string } }).error.code, 'CROSS_ORIGIN')
  assert.equal(runtimeCalls.length, 0)
  assert.equal(adapterCalls.length, 0)
})

test('status and execution use one injected runtime-client path and stable project registration', async () => {
  runtimeFailure = null
  runtimeCalls.length = 0
  adapterCalls.length = 0
  const coordinator = await env.as('coord@t.co')
  const status = await coordinator.get(`${P}/agent/status`)
  assert.equal(status.status, 200)
  assert.equal(status.body.projectId, 'pec')
  assert.equal(status.body.projectAdapter.service, 'pec-project-adapter')
  assert.equal(status.body.configured, true)
  assert.deepEqual(status.body.agent, { name: 'PEC Agent', email: 'agent@t.co' })

  emitted = [
    event('session:init', {
      engineSessionId: 'manager-engine-session',
      adapterId: 'claude-agent-sdk',
      providerId: 'anthropic',
      model: 'manager-model',
    }),
    event('harness:event', harnessEvent('evt-accepted', 'turn.accepted', { role: 'agent1' })),
    event('harness:event', harnessEvent('evt-started', 'turn.started', { role: 'agent1' })),
    event('chat:delta', { text: 'reviewed' }),
    event('chat:complete', { text: 'reviewed' }),
    event('session:complete', {}),
    event('process:exit', { exitCode: 0 }),
  ]
  const response = await coordinator.post(`${P}/agent/messages`, {
    message: 'Review the scratch PEC state',
    pid: 424242,
    context: { route: `/p/${env.projectId}/overview`, records: [] },
    history: [{ who: 'you', text: 'Earlier context' }],
  })
  assert.equal(response.status, 200)

  assert.equal(runtimeCalls.length, 2)
  assert.deepEqual(adapterCalls, [
    { kind: 'status' },
    { kind: 'read', projectId: env.projectId, context: { route: `/p/${env.projectId}/overview`, records: [] } },
  ])
  assert.deepEqual(runtimeCalls[0], {
    kind: 'status',
    request: { projectId: 'pec', pecProjectId: env.projectId },
  })
  const run = runtimeCalls[1]
  assert.equal(run?.kind, 'run')
  if (run?.kind !== 'run') throw new Error('expected run')
  assert.equal(run.request.projectId, 'pec')
  assert.equal(run.request.role, 'agent1')
  assert.equal(run.request.agentId, 'WORKING_ITEMS')
  assert.deepEqual(run.request.requestedBy, {
    pecProjectId: env.projectId,
    personId: env.people['coord@t.co'],
  })
  assert.match(run.request.approvalReference, new RegExp(`^pec-ui-agent-direct:${env.projectId}:`))
  assert.match(run.request.brief, /Review the scratch PEC state/)
  assert.match(run.request.brief, /pec-project-adapter/)
  assert.doesNotMatch(run.request.brief, /424242/, 'client-supplied pid is not authority')
})

test('canonical UIEvent SSE names/data and rich harness:event payloads are preserved byte-for-byte', async () => {
  runtimeFailure = null
  runtimeCalls.length = 0
  emitted = [
    event('session:init', {
      engineSessionId: 'manager-engine-session',
      adapterId: 'claude-agent-sdk',
      providerId: 'anthropic',
      model: 'manager-model',
    }),
    event('harness:event', harnessEvent('evt-accepted', 'turn.accepted', { role: 'agent1' })),
    event('harness:event', harnessEvent('evt-child', 'subagent.started', {
      childRole: 'agent2',
      adapterId: 'pi',
      providerId: 'omlx',
      model: 'mlx-community/Qwen3.6-35B-A3B-8bit',
      residencyEpoch: 'epoch-35b',
    })),
    event('harness:event', harnessEvent('evt-tool-start', 'tool.started', {
      toolName: 'read_file',
      toolUseId: 'tool-1',
    })),
    event('tool:result', { name: 'read_file', ok: true, output: 'fixture' }),
    event('harness:event', harnessEvent('evt-tool-done', 'tool.completed', {
      toolName: 'read_file',
      toolUseId: 'tool-1',
      ok: true,
    })),
    event('harness:event', harnessEvent('evt-reviewed', 'coordination.acknowledged', {
      acceptance: 'accepted',
    })),
    event('chat:complete', { text: 'accepted after review' }),
    event('harness:event', harnessEvent('evt-completed', 'turn.completed', {
      managerText: 'accepted after review',
    })),
    event('session:complete', {}),
    event('process:exit', { exitCode: 0 }),
  ]
  const pm = await env.as('pm@t.co')
  const login = await fetch(`${env.base}/api/auth/login`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ email: 'pm@t.co', password: 'pilot' }),
  })
  const cookie = (login.headers.get('set-cookie') ?? '').split(';')[0]!
  const response = await fetch(`${env.base}${P}/agent/messages`, {
    method: 'POST',
    headers: {
      cookie,
      origin: env.base,
      accept: 'text/event-stream',
      'content-type': 'application/json',
    },
    body: JSON.stringify({ message: 'run the governed read-only pilot' }),
  })
  assert.equal(response.status, 200)
  assert.match(response.headers.get('content-type') ?? '', /^text\/event-stream/)
  const stream = await response.text()

  const frames = stream.trim().split('\n\n')
  assert.equal(frames.length, emitted.length)
  for (let index = 0; index < emitted.length; index++) {
    assert.equal(frames[index], `event: ${emitted[index]!.type}\ndata: ${JSON.stringify(emitted[index]!.data)}`)
  }
  assert.match(stream, /"providerId":"omlx"/)
  assert.match(stream, /"residencyEpoch":"epoch-35b"/)
})

test('buffers process exit until exhaustion and never exposes a premature success', async () => {
  runtimeFailure = null
  runtimeCalls.length = 0
  emitted = [
    event('session:init', {
      engineSessionId: 'manager-engine-session',
      adapterId: 'stub',
      providerId: 'stub',
      model: 'manager',
    }),
    event('process:exit', { exitCode: 0 }),
    event('chat:complete', { text: 'illegal late event' }),
  ]
  const pm = await env.as('pm@t.co')
  const response = await pm.post(`${P}/agent/messages`, {
    message: 'exercise terminal buffering',
  })
  assert.equal(response.status, 200)
  const stream = String(response.body)
  assert.doesNotMatch(stream, /event: process:exit/)
  assert.doesNotMatch(stream, /illegal late event/)
})

test('daemon failure fails closed with no PEC state mutation and no sidecar fallback', async () => {
  runtimeCalls.length = 0
  runtimeFailure = Object.assign(new Error('control socket refused'), {
    status: 503,
    code: 'AGENT_UNAVAILABLE',
  })
  const beforeHistory = Number((env.db.prepare('SELECT COUNT(*) AS n FROM history_entry').get() as { n: number }).n)
  const beforeAudit = Number((env.db.prepare('SELECT COUNT(*) AS n FROM audit_event').get() as { n: number }).n)
  const beforeProposals = Number((env.db.prepare('SELECT COUNT(*) AS n FROM import_proposal').get() as { n: number }).n)

  const pm = await env.as('pm@t.co')
  const response = await pm.post(`${P}/agent/messages`, { message: 'status' })
  assert.equal(response.status, 503)
  assert.equal(response.body.error.code, 'AGENT_UNAVAILABLE')
  assert.match(response.body.error.message, /control socket refused/)
  assert.equal(runtimeCalls.filter((call) => call.kind === 'run').length, 1)

  assert.equal(Number((env.db.prepare('SELECT COUNT(*) AS n FROM history_entry').get() as { n: number }).n), beforeHistory)
  assert.equal(Number((env.db.prepare('SELECT COUNT(*) AS n FROM audit_event').get() as { n: number }).n), beforeAudit)
  assert.equal(Number((env.db.prepare('SELECT COUNT(*) AS n FROM import_proposal').get() as { n: number }).n), beforeProposals)
  runtimeFailure = null
})

test('file proposal attachments fail closed in the read-only shared-runtime pilot', async () => {
  runtimeCalls.length = 0
  const pm = await env.as('pm@t.co')
  const response = await pm.post(`${P}/agent/messages`, {
    message: 'file this',
    attachment: { name: 'mdl.csv', text: 'doc_no,title\nD-1,Test' },
  })
  assert.equal(response.status, 400)
  assert.equal(response.body.error.code, 'AGENT_ATTACHMENT_UNSUPPORTED')
  assert.equal(runtimeCalls.length, 0)
})

test('raw browser requests cannot select a local model or repository path', async () => {
  runtimeCalls.length = 0
  adapterCalls.length = 0
  const pm = await env.as('pm@t.co')
  const response = await pm.post(`${P}/agent/messages`, {
    message: 'attempt hidden routing',
    localModel: 'Qwen3.6-35B-A3B-8bit',
    readOnlyTool: { name: 'read_file', relativePath: 'server/.env' },
  })
  assert.equal(response.status, 403)
  assert.equal(response.body.error.code, 'AGENT_RUNTIME_ROUTING_FORBIDDEN')
  assert.equal(runtimeCalls.length, 0)
  assert.equal(adapterCalls.length, 0)
})

test('scratch/demo routing accepts OS temp and explicit demo paths but rejects production paths', () => {
  assert.equal(isScratchOrDemoDatabasePath('/private/tmp/pec-test.db', '/private/tmp'), true)
  assert.equal(isScratchOrDemoDatabasePath('/srv/pec/demo/pec.db', '/private/tmp'), true)
  assert.equal(isScratchOrDemoDatabasePath('/srv/pec/pec-demo.db', '/private/tmp'), true)
  assert.equal(isScratchOrDemoDatabasePath('/srv/pec/production/pec.db', '/private/tmp'), false)
})

test('compatibility request pins Agent 1 and rejects browser-selected runtime routing', () => {
  const request = runtimeRunRequest({ message: 'read governed PEC context' }, 7, 11)
  assert.equal(request.role, 'agent1')
  assert.equal(request.agentId, 'WORKING_ITEMS')
  assert.deepEqual(toDaemonAgent1RunRequest(request), {
    brief: request.brief,
    agentId: 'WORKING_ITEMS',
    approvalReference: 'pec-ui-agent-direct:7:11',
  })
  assert.throws(
    () => runtimeRunRequest({
      message: 'read arbitrary checkout file',
      localModel: 'mlx-community/Qwen3.6-35B-A3B-8bit',
      readOnlyTool: { name: 'read_file', relativePath: '../../secret' },
    }, 7, 11),
    (error: unknown) =>
      error instanceof AppError && error.code === 'AGENT_RUNTIME_ROUTING_FORBIDDEN',
  )
})
