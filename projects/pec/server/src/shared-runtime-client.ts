import { homedir } from 'node:os'
import { lstatSync, realpathSync } from 'node:fs'
import { basename, dirname, join, relative, resolve } from 'node:path'
import { RuntimeClient } from '@chirality/runtime-client'
import type { Agent1RunRequest, RuntimeSseFrame } from '@chirality/runtime-contracts'
import {
  PEC_AGENT_1_ID,
  PEC_RUNTIME_PROJECT_ID,
  assertPecUiEvent,
  type PecRuntimeRunRequest,
  type PecRuntimeStatusRequest,
  type PecSharedRuntimeClientPort,
  type PecUiEvent,
} from './runtime-client-port.ts'

function requiredProjectTokenFile(env: NodeJS.ProcessEnv, socketPath: string): string {
  const configured = env.CHIRALITY_PEC_RUNTIME_TOKEN_FILE?.trim()
  if (!configured) {
    throw Object.assign(
      new Error(
        'CHIRALITY_PEC_RUNTIME_TOKEN_FILE must name the project-scoped token returned by `chirality project register`',
      ),
      { status: 503, code: 'AGENT_UNAVAILABLE' },
    )
  }
  const tokensDirectory = resolve(dirname(socketPath), 'auth', 'tokens')
  const tokenFile = resolve(configured)
  const tokenName = basename(tokenFile)
  if (!/^project-[A-Za-z0-9_-]+\.token$/u.test(tokenName) || tokenName === 'operator.token') {
    throw Object.assign(new Error('PEC requires a project-scoped runtime token'), {
      status: 503,
      code: 'AGENT_UNAVAILABLE',
    })
  }
  const metadata = lstatSync(tokenFile)
  const canonical = realpathSync(tokenFile)
  const child = relative(tokensDirectory, canonical)
  if (
    !metadata.isFile()
    || metadata.isSymbolicLink()
    || (metadata.mode & 0o077) !== 0
    || (process.getuid !== undefined && metadata.uid !== process.getuid())
    || child.startsWith('..')
    || resolve(child) === child
  ) {
    throw Object.assign(new Error('PEC runtime token must be private and runtime-owned'), {
      status: 503,
      code: 'AGENT_UNAVAILABLE',
    })
  }
  return canonical
}

function runtimeSocketPath(env: NodeJS.ProcessEnv): string {
  return resolve(
    env.CHIRALITY_RUNTIME_SOCKET_PATH
      ?? join(
        homedir(),
        'Library',
        'Application Support',
        'Chirality',
        'runtime',
        'control.sock',
      ),
  )
}

function asPecUiEvent(event: RuntimeSseFrame): PecUiEvent {
  assertPecUiEvent(event)
  return event as PecUiEvent
}

/** Server-owned mapping; browser input can never select the PEC manager role. */
export function toDaemonAgent1RunRequest(request: PecRuntimeRunRequest): Agent1RunRequest {
  return {
    brief: request.brief,
    agentId: request.agentId,
    approvalReference: request.approvalReference,
    ...(request.localModel === undefined ? {} : { localModel: request.localModel }),
    ...(request.readOnlyTool === undefined
      ? {}
      : { readOnlyTool: request.readOnlyTool }),
  }
}

/**
 * Bind PEC to one project-scoped daemon principal. The server never falls back
 * to the historical sidecar LLM loop and never reads the operator token.
 */
export function createPecSharedRuntimeClient(
  env: NodeJS.ProcessEnv = process.env,
): PecSharedRuntimeClientPort {
  const socketPath = runtimeSocketPath(env)
  const tokenFile = requiredProjectTokenFile(env, socketPath)
  const client = new RuntimeClient({
    socketPath,
    tokenFile,
  })
  const expectedClientId = basename(tokenFile, '.token')
  const requirePecBinding = async (): Promise<void> => {
    const status = await client.projectStatus(PEC_RUNTIME_PROJECT_ID)
    if (
      status.project.projectId !== PEC_RUNTIME_PROJECT_ID
      || status.project.clientId !== expectedClientId
      || status.manifestDrift
      || !status.adaptersEnabled
    ) {
      throw Object.assign(new Error('PEC runtime token does not match the active registration'), {
        status: 403,
        code: 'FORBIDDEN',
      })
    }
  }

  return {
    async status(request: PecRuntimeStatusRequest): Promise<unknown> {
      if (request.projectId !== PEC_RUNTIME_PROJECT_ID) {
        throw Object.assign(new Error('PEC runtime project identity mismatch'), {
          status: 403,
          code: 'FORBIDDEN',
        })
      }
      await requirePecBinding()
      const [project, daemon, residency] = await Promise.all([
        client.projectStatus(PEC_RUNTIME_PROJECT_ID),
        client.daemonStatus(),
        client.listModels(),
      ])
      if (project.manifestDrift || !project.adaptersEnabled) {
        throw Object.assign(
          new Error('PEC project manifest changed; explicit re-registration is required'),
          { status: 409, code: 'PROJECT_MANIFEST_DRIFT' },
        )
      }
      return {
        ok: true,
        engine: 'chirality-runtime',
        egress: 'model-provider',
        access: env.PEC_AGENT_ACCESS === 'broad' ? 'broad' : 'enumerated',
        session: `daemon:${daemon.daemonId}`,
        model: residency.managedModelId ?? null,
        configured: true,
        managerAgentId: PEC_AGENT_1_ID,
      }
    },

    runAgent1(request: PecRuntimeRunRequest, signal: AbortSignal): AsyncIterable<PecUiEvent> {
      if (request.projectId !== PEC_RUNTIME_PROJECT_ID || request.role !== 'agent1') {
        throw Object.assign(new Error('PEC may invoke only its registered Agent 1 runtime'), {
          status: 403,
          code: 'FORBIDDEN',
        })
      }
      return {
        async *[Symbol.asyncIterator](): AsyncIterator<PecUiEvent> {
          await requirePecBinding()
          const stream = await client.runAgent1(
            PEC_RUNTIME_PROJECT_ID,
            toDaemonAgent1RunRequest(request),
            signal,
          )
          try {
            for await (const event of stream) {
              yield asPecUiEvent(event)
            }
          } finally {
            stream.cancel()
          }
        },
      }
    },
  }
}
