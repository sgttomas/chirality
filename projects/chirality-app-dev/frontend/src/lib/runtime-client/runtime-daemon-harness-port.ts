import { basename, isAbsolute, relative, resolve } from 'node:path';

import {
  RuntimeClient,
  RuntimeTransportError,
  type RuntimeStream
} from '@chirality/runtime-client';
import {
  RuntimeError,
  type ProjectStatus,
  type RegisteredProject,
  type RuntimeSessionRecord
} from '@chirality/runtime-contracts';
import { HarnessError } from '@chirality/harness-contract/errors';
import type {
  HarnessErrorType,
  SessionRecord,
  UIEvent
} from '@chirality/harness-contract/types';

import type {
  DaemonHarnessPort,
  DaemonRequestOptions,
  RunningDaemonHarnessTurn
} from './daemon-harness-port';

const APP_DEV_PROJECT_ID = 'chirality-app-dev';

export interface RuntimeDaemonHarnessPortOptions {
  client: RuntimeClient;
  projectId?: string;
  projectRoot?: string;
}

export interface RuntimeDaemonHarnessEnvironment {
  [name: string]: string | undefined;
  CHIRALITY_RUNTIME_SOCKET_PATH?: string;
  CHIRALITY_RUNTIME_TOKEN_FILE?: string;
  CHIRALITY_RUNTIME_PROJECT_ID?: string;
  CHIRALITY_RUNTIME_PROJECT_ROOT?: string;
}

function asLegacySession(
  session: RuntimeSessionRecord,
  projectId = APP_DEV_PROJECT_ID
): SessionRecord {
  if (session.projectId !== projectId) {
    throw new RuntimeError(
      'FORBIDDEN',
      'The daemon returned a session outside the configured app-dev project',
      403
    );
  }
  return session;
}

function harnessErrorType(error: RuntimeError): HarnessErrorType {
  switch (error.code) {
    case 'INVALID_REQUEST':
      return 'INVALID_REQUEST';
    case 'SESSION_NOT_FOUND':
    case 'NOT_FOUND':
      return 'SESSION_NOT_FOUND';
    case 'SESSION_TURN_IN_PROGRESS':
      return 'TURN_IN_PROGRESS';
    case 'MODEL_UNAVAILABLE':
    case 'MODEL_NOT_RESIDENT':
    case 'RESIDENCY_TRANSITION_IN_PROGRESS':
    case 'RESIDENCY_DRAIN_TIMEOUT':
    case 'RESIDENCY_UNMANAGED_CONFLICT':
      return 'MODEL_UNAVAILABLE';
    case 'OMLX_AUTHENTICATION_FAILED':
    case 'UNAUTHORIZED':
    case 'FORBIDDEN':
      return 'PROVIDER_AUTH_FAILURE';
    case 'OMLX_PROTOCOL_FAILURE':
      return 'PROVIDER_PROTOCOL_FAILURE';
    case 'PROJECT_NOT_FOUND':
      return 'WORKING_ROOT_INACCESSIBLE';
    case 'PROJECT_MANIFEST_INVALID':
    case 'PROJECT_MANIFEST_DRIFT':
      return 'WORKING_ROOT_CONFLICT';
    case 'ENGINE_UNAVAILABLE':
    case 'OMLX_UNAVAILABLE':
      return 'ENGINE_UNAVAILABLE';
    default:
      return 'SDK_FAILURE';
  }
}

function translateDaemonError(error: unknown): HarnessError {
  if (error instanceof HarnessError) return error;
  if (error instanceof RuntimeError) {
    return new HarnessError(
      harnessErrorType(error),
      error.status,
      error.message,
      error.details
    );
  }
  if (error instanceof RuntimeTransportError) {
    return new HarnessError(
      'ENGINE_UNAVAILABLE',
      503,
      'Chirality runtime daemon is unavailable'
    );
  }
  if (error instanceof Error) {
    return new HarnessError('SDK_FAILURE', 500, error.message);
  }
  return new HarnessError('SDK_FAILURE', 500, 'Unexpected runtime daemon failure');
}

async function mapped<T>(operation: () => Promise<T>): Promise<T> {
  try {
    return await operation();
  } catch (error) {
    throw translateDaemonError(error);
  }
}

function containsPath(root: string, candidate: string): boolean {
  const child = relative(resolve(root), resolve(candidate));
  return child === '' || (!child.startsWith('..') && !isAbsolute(child));
}

function authorizedProject(status: ProjectStatus): RegisteredProject {
  if (status.manifestDrift || !status.adaptersEnabled) {
    throw new RuntimeError(
      'PROJECT_MANIFEST_DRIFT',
      'Project manifest changed after registration',
      409,
      { projectId: status.project.projectId }
    );
  }
  return status.project;
}

/**
 * Adapts the pre-daemon Desktop API to the versioned shared-runtime API.
 *
 * RuntimeClient supplies the authenticated Unix-socket transport. This class
 * owns only compatibility mappings; it does not construct an engine, session
 * store, permission broker, or other runtime singleton.
 */
export class RuntimeDaemonHarnessPort implements DaemonHarnessPort {
  private readonly projectId: string;
  private readonly projectRoot?: string;

  constructor(
    private readonly client: RuntimeClient,
    projectId = APP_DEV_PROJECT_ID,
    projectRoot?: string
  ) {
    if (projectId !== APP_DEV_PROJECT_ID) {
      throw new HarnessError(
        'WORKING_ROOT_CONFLICT',
        409,
        'Chirality Desktop is scoped only to the app-dev project'
      );
    }
    this.projectId = projectId;
    this.projectRoot = projectRoot === undefined ? undefined : resolve(projectRoot);
  }

  async createSession(
    request: Parameters<DaemonHarnessPort['createSession']>[0],
    options?: DaemonRequestOptions
  ): ReturnType<DaemonHarnessPort['createSession']> {
    return mapped(async () => {
      const project = await this.requirePathInConfiguredProject(
        request.projectRoot,
        options?.signal
      );
      const session = await this.client.createSession(
        this.projectId,
        {
          projectId: this.projectId,
          ...(request.persona === undefined ? {} : { persona: request.persona }),
          ...(request.mode === undefined ? {} : { mode: request.mode })
        },
        options?.signal
      );
      return { session: asLegacySession(session, this.projectId) };
    });
  }

  async listSessions(
    projectRoot: string,
    options?: DaemonRequestOptions
  ): ReturnType<DaemonHarnessPort['listSessions']> {
    return mapped(async () => {
      await this.requirePathInConfiguredProject(projectRoot, options?.signal);
      const sessions = await this.client.listSessions(this.projectId, options?.signal);
      return {
        sessions: sessions.map((session) => asLegacySession(session, this.projectId))
      };
    });
  }

  async getSession(
    sessionId: string,
    options?: DaemonRequestOptions
  ): ReturnType<DaemonHarnessPort['getSession']> {
    return mapped(async () => {
      await this.requireConfiguredProject(options?.signal);
      const session = await this.client.getSession(
        this.projectId,
        sessionId,
        options?.signal
      );
      return { session: asLegacySession(session, this.projectId) };
    });
  }

  async deleteSession(
    sessionId: string,
    options?: DaemonRequestOptions
  ): ReturnType<DaemonHarnessPort['deleteSession']> {
    return mapped(async () => {
      await this.requireConfiguredProject(options?.signal);
      await this.client.deleteSession(this.projectId, sessionId, options?.signal);
      return { ok: true };
    });
  }

  async bootSession(
    request: Parameters<DaemonHarnessPort['bootSession']>[0],
    options?: DaemonRequestOptions
  ): ReturnType<DaemonHarnessPort['bootSession']> {
    return mapped(async () => {
      await this.requireConfiguredProject(options?.signal);
      return this.client.bootSession(
        this.projectId,
        request.sessionId,
        { opts: request.opts },
        options?.signal
      );
    });
  }

  async replaySession(
    sessionId: string,
    options?: DaemonRequestOptions
  ): ReturnType<DaemonHarnessPort['replaySession']> {
    return mapped(async () => {
      await this.requireConfiguredProject(options?.signal);
      const replay = await this.client.replaySession(
        this.projectId,
        sessionId,
        options?.signal
      );
      return {
        ...replay,
        session: asLegacySession(replay.session, this.projectId),
        events: [...replay.events]
      };
    });
  }

  async turn(
    request: Parameters<DaemonHarnessPort['turn']>[0],
    options?: DaemonRequestOptions
  ): ReturnType<DaemonHarnessPort['turn']> {
    return mapped(async () => {
      await this.requireConfiguredProject(options?.signal);
      const stream = await this.client.turnSession(
        this.projectId,
        request.sessionId,
        {
          message: request.message,
          ...(request.opts === undefined ? {} : { opts: request.opts }),
          ...(request.attachments === undefined
            ? {}
            : { attachments: request.attachments })
        },
        options?.signal
      );
      return this.runningTurn(
        stream,
        this.projectId,
        request.sessionId
      );
    });
  }

  async interrupt(
    request: Parameters<DaemonHarnessPort['interrupt']>[0],
    options?: DaemonRequestOptions
  ): ReturnType<DaemonHarnessPort['interrupt']> {
    return mapped(async () => {
      await this.requireConfiguredProject(options?.signal);
      await this.client.interruptSession(
        this.projectId,
        request.sessionId,
        options?.signal
      );
      return { ok: true };
    });
  }

  async decidePermission(
    request: Parameters<DaemonHarnessPort['decidePermission']>[0],
    options?: DaemonRequestOptions
  ): ReturnType<DaemonHarnessPort['decidePermission']> {
    return mapped(async () => {
      await this.requireConfiguredProject(options?.signal);
      const response = await this.client.decidePermission(
        this.projectId,
        request.sessionId,
        {
          requestId: request.toolUseId,
          decision: request.verdict
        },
        options?.signal
      );
      const compatibility = response as typeof response & { decided?: boolean };
      return {
        ok: true,
        decided: compatibility.decided ?? compatibility.accepted
      };
    });
  }

  async listAgents(
    request: Parameters<DaemonHarnessPort['listAgents']>[0],
    options?: DaemonRequestOptions
  ): ReturnType<DaemonHarnessPort['listAgents']> {
    return mapped(async () => {
      await this.requireConfiguredProject(options?.signal);
      const agents = await this.client.listAgents(this.projectId, options?.signal);
      return {
        agents: agents
          .filter((agent) => !request.directChatOnly || agent.type === 0 || agent.type === 1)
          .map((agent) => ({
            name: agent.name,
            type: agent.type,
            class: agent.class
          }))
      };
    });
  }

  async scaffold(
    request: Parameters<DaemonHarnessPort['scaffold']>[0],
    options?: DaemonRequestOptions
  ): ReturnType<DaemonHarnessPort['scaffold']> {
    return mapped(async () => {
      const project = await this.requireConfiguredProject(options?.signal);
      for (const candidate of [request.executionRoot, request.decompositionPath]) {
        if (!containsPath(project.canonicalRoot, candidate)) {
          throw new RuntimeError(
            'PROJECT_NOT_FOUND',
            'The requested path is outside the configured app-dev project',
            404
          );
        }
      }
      return this.client.scaffold(this.projectId, request, options?.signal);
    });
  }

  private runningTurn(
    stream: RuntimeStream,
    projectId: string,
    sessionId: string
  ): RunningDaemonHarnessTurn {
    let cancelled = false;
    return {
      events: stream as AsyncIterable<UIEvent>,
      cancel: async (): Promise<void> => {
        if (cancelled) return;
        cancelled = true;
        stream.cancel();
        await mapped(async () => {
          // The inbound HTTP request signal may already be aborted when the
          // browser cancels its SSE reader. Use a fresh control request so the
          // daemon receives the interruption and releases the shared turn lock.
          await this.client.interruptSession(projectId, sessionId);
        });
      }
    };
  }

  private async requireConfiguredProject(signal?: AbortSignal): Promise<RegisteredProject> {
    const project = authorizedProject(await this.client.projectStatus(this.projectId, signal));
    if (
      project.projectId !== APP_DEV_PROJECT_ID ||
      (this.projectRoot !== undefined &&
        resolve(project.canonicalRoot) !== this.projectRoot)
    ) {
      throw new RuntimeError(
        'PROJECT_MANIFEST_DRIFT',
        'The daemon project registration does not match the Desktop project binding',
        409,
        { projectId: this.projectId }
      );
    }
    return project;
  }

  private async requirePathInConfiguredProject(
    candidate: string,
    signal?: AbortSignal
  ): Promise<RegisteredProject> {
    const project = await this.requireConfiguredProject(signal);
    if (!containsPath(project.canonicalRoot, candidate)) {
      throw new RuntimeError(
        'PROJECT_NOT_FOUND',
        'The requested path is outside the configured app-dev project',
        404
      );
    }
    return project;
  }
}

export function createRuntimeDaemonHarnessPort(
  options: RuntimeDaemonHarnessPortOptions
): DaemonHarnessPort {
  return new RuntimeDaemonHarnessPort(
    options.client,
    options.projectId,
    options.projectRoot
  );
}

/**
 * The Desktop composition root provides these paths to its Next child.
 * Credentials are read by RuntimeClient from a private file and never cross
 * the renderer boundary.
 */
export function createRuntimeDaemonHarnessPortFromEnvironment(
  environment: RuntimeDaemonHarnessEnvironment = process.env
): DaemonHarnessPort {
  const socketPath = environment.CHIRALITY_RUNTIME_SOCKET_PATH?.trim();
  const tokenFile = environment.CHIRALITY_RUNTIME_TOKEN_FILE?.trim();
  const projectId = environment.CHIRALITY_RUNTIME_PROJECT_ID?.trim();
  const projectRoot = environment.CHIRALITY_RUNTIME_PROJECT_ROOT?.trim();
  if (
    !socketPath ||
    !tokenFile ||
    !/^project-[A-Za-z0-9_-]+\.token$/u.test(basename(tokenFile)) ||
    projectId !== APP_DEV_PROJECT_ID ||
    !projectRoot
  ) {
    throw new HarnessError(
      'ENGINE_UNAVAILABLE',
      503,
      'Chirality runtime daemon client is not configured'
    );
  }
  return new RuntimeDaemonHarnessPort(
    new RuntimeClient({
      socketPath: resolve(socketPath),
      tokenFile: resolve(tokenFile)
    }),
    APP_DEV_PROJECT_ID,
    resolve(projectRoot)
  );
}
