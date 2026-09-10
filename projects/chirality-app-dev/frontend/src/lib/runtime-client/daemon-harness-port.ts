import { resolve } from 'node:path';

import { HarnessError } from '@chirality/runtime-contracts/errors';
import type { HarnessEvent } from '@chirality/runtime-contracts/event-schema';
import type {
  InterruptRequest,
  ScaffoldExecutionRootRequest,
  ScaffoldExecutionRootResponse,
  SessionBootRequest,
  SessionBootResponse,
  SessionCreateRequest,
  SessionRecord,
  TurnRequest,
  UIEvent
} from '@chirality/runtime-contracts/types';
import type { TranscriptView } from '@chirality/runtime-contracts/transcript-replay';
import type {
  ChiralityRoleName,
  ExportNativePlanRequest,
  ExportNativePlanResponse,
  FrozenInstructionBasisV3,
  InstructionHistoryRecordV3,
  MethodInspectionResponse,
  MethodsResponse,
  NativePlanCapabilityResponse,
  NativePlanClarificationsResponse,
  NativePlanRevisionsResponse,
  ReplyNativePlanClarificationRequest,
  ReplyNativePlanClarificationResponse,
  ReplaceSelectedMethodsRequest,
  ReplaceSelectedMethodsResponse,
  ResolveSelectedContextRequest,
  ResolveSelectedContextResponse,
  RolesResponse
} from '@chirality/runtime-contracts/v3';
import type { ReadableRuntimeSessionRecord } from '@chirality/runtime-contracts';
import type {
  HostedBootstrapLoginStartResponse,
  HostedBootstrapStatus
} from '@chirality/runtime-contracts';
import {
  createRuntimeDaemonHarnessPortFromEnvironment,
  createRuntimeHostedBootstrapPortFromEnvironment
} from './runtime-daemon-harness-port';

export type AgentRosterEntry = {
  name: string;
  type: number | undefined;
  class: string | undefined;
};

export type PermissionDecisionRequest = {
  sessionId: string;
  toolUseId: string;
  verdict: 'allow' | 'deny';
};

export type HarnessReplayResponse = {
  events: HarnessEvent[];
  malformedLineCount: number;
  summary: {
    eventCount: number;
    malformedLineCount: number;
    eventTypeCounts: Record<string, number>;
    firstTimestamp?: string;
    lastTimestamp?: string;
  };
  session: SessionRecord | ReadableRuntimeSessionRecord;
  transcript: TranscriptView;
  instructionHistory: readonly InstructionHistoryRecordV3[];
  instructionBases: readonly FrozenInstructionBasisV3[];
};

export type RunningDaemonHarnessTurn = {
  events: AsyncIterable<UIEvent>;
  cancel(): Promise<void>;
};

export type DaemonRequestOptions = {
  signal?: AbortSignal;
};

export type HostedBootstrapStatusResponse =
  | { registration: 'required' }
  | {
      registration: 'registered';
      projectId: string;
      status: HostedBootstrapStatus;
    };

export interface HostedBootstrapPort {
  getStatus(
    projectRoot: string,
    options?: DaemonRequestOptions
  ): Promise<HostedBootstrapStatusResponse>;
  initializeProject(
    projectRoot: string,
    options?: DaemonRequestOptions
  ): Promise<Extract<HostedBootstrapStatusResponse, { registration: 'registered' }>>;
  grantProviderNetworkConsent(
    projectRoot: string,
    options?: DaemonRequestOptions
  ): Promise<HostedBootstrapStatus>;
  startLogin(
    projectRoot: string,
    options?: DaemonRequestOptions
  ): Promise<HostedBootstrapLoginStartResponse>;
  cancelLogin(
    projectRoot: string,
    options?: DaemonRequestOptions
  ): Promise<HostedBootstrapStatus>;
  signOut(
    projectRoot: string,
    options?: DaemonRequestOptions
  ): Promise<HostedBootstrapStatus>;
}

export type DaemonProjectBinding = {
  projectId: string;
  projectRoot: string;
};

export type V3SessionCreateRequest = SessionCreateRequest & {
  roleId?: ChiralityRoleName;
  interactionMode?: ResolveSelectedContextRequest['interactionMode'];
  permissionMode?: ResolveSelectedContextRequest['permissionMode'];
  selectedMethods?: ResolveSelectedContextRequest['methods'];
  declaredContext?: string[];
  allowedWriteTargets?: string[];
};

export type V3TurnRequest = TurnRequest & {
  interactionMode?: ResolveSelectedContextRequest['interactionMode'];
  permissionMode?: ResolveSelectedContextRequest['permissionMode'];
  methods?: ResolveSelectedContextRequest['methods'];
};

/**
 * Compatibility boundary between the existing Desktop renderer API and the
 * shared runtime daemon.
 *
 * The concrete runtime-client binder is responsible for resolving a
 * registered projectRoot to a projectId, resolving session ownership, mapping
 * canonical daemon events to the existing UI event names, and authenticating
 * over the Unix socket. Route handlers intentionally know none of those
 * details and have no in-process runtime fallback.
 */
export interface DaemonHarnessPort {
  createSession(
    request: V3SessionCreateRequest,
    options?: DaemonRequestOptions
  ): Promise<{ session: SessionRecord | ReadableRuntimeSessionRecord }>;
  listSessions(
    projectRoot: string,
    options?: DaemonRequestOptions
  ): Promise<{ sessions: Array<SessionRecord | ReadableRuntimeSessionRecord> }>;
  getSession(
    sessionId: string,
    options?: DaemonRequestOptions
  ): Promise<{ session: SessionRecord | ReadableRuntimeSessionRecord }>;
  deleteSession(
    sessionId: string,
    options?: DaemonRequestOptions
  ): Promise<{ ok: true }>;
  bootSession(
    request: SessionBootRequest,
    options?: DaemonRequestOptions
  ): Promise<SessionBootResponse>;
  replaySession(
    sessionId: string,
    options?: DaemonRequestOptions
  ): Promise<HarnessReplayResponse>;
  turn(
    request: V3TurnRequest,
    options?: DaemonRequestOptions
  ): Promise<RunningDaemonHarnessTurn>;
  interrupt(
    request: InterruptRequest,
    options?: DaemonRequestOptions
  ): Promise<{ ok: true }>;
  decidePermission(
    request: PermissionDecisionRequest,
    options?: DaemonRequestOptions
  ): Promise<{ ok: true; decided: boolean }>;
  listAgents(
    request: { directChatOnly: boolean },
    options?: DaemonRequestOptions
  ): Promise<{ agents: AgentRosterEntry[] }>;
  listRoles(
    projectRoot: string,
    options?: DaemonRequestOptions
  ): Promise<RolesResponse>;
  listMethods(
    request: { projectRoot: string; kind?: 'skill' | 'workflow'; query?: string },
    options?: DaemonRequestOptions
  ): Promise<MethodsResponse>;
  inspectMethod(
    request: { projectRoot: string; qualifiedId: string },
    options?: DaemonRequestOptions
  ): Promise<MethodInspectionResponse>;
  resolveSelectedContext(
    sessionId: string,
    request: ResolveSelectedContextRequest,
    options?: DaemonRequestOptions
  ): Promise<ResolveSelectedContextResponse>;
  replaceSelectedMethods(
    sessionId: string,
    request: ReplaceSelectedMethodsRequest,
    options?: DaemonRequestOptions
  ): Promise<ReplaceSelectedMethodsResponse>;
  getNativePlanCapability(
    sessionId: string,
    options?: DaemonRequestOptions
  ): Promise<NativePlanCapabilityResponse>;
  listNativePlanRevisions(
    sessionId: string,
    options?: DaemonRequestOptions
  ): Promise<NativePlanRevisionsResponse>;
  listNativePlanClarifications(
    sessionId: string,
    options?: DaemonRequestOptions
  ): Promise<NativePlanClarificationsResponse>;
  replyNativePlanClarification(
    sessionId: string,
    requestId: string | number,
    answers: ReplyNativePlanClarificationRequest['answers'],
    options?: DaemonRequestOptions
  ): Promise<ReplyNativePlanClarificationResponse>;
  exportNativePlan(
    sessionId: string,
    request: ExportNativePlanRequest,
    options?: DaemonRequestOptions
  ): Promise<ExportNativePlanResponse>;
  scaffold(
    request: ScaffoldExecutionRootRequest,
    options?: DaemonRequestOptions
  ): Promise<ScaffoldExecutionRootResponse>;
}

function daemonClientUnavailable(): never {
  throw new HarnessError(
    'ENGINE_UNAVAILABLE',
    503,
    'Chirality runtime daemon client is not configured'
  );
}

const unboundDaemonHarnessPort: DaemonHarnessPort = {
  createSession: daemonClientUnavailable,
  listSessions: daemonClientUnavailable,
  getSession: daemonClientUnavailable,
  deleteSession: daemonClientUnavailable,
  bootSession: daemonClientUnavailable,
  replaySession: daemonClientUnavailable,
  turn: daemonClientUnavailable,
  interrupt: daemonClientUnavailable,
  decidePermission: daemonClientUnavailable,
  listAgents: daemonClientUnavailable,
  listRoles: daemonClientUnavailable,
  listMethods: daemonClientUnavailable,
  inspectMethod: daemonClientUnavailable,
  resolveSelectedContext: daemonClientUnavailable,
  replaceSelectedMethods: daemonClientUnavailable,
  getNativePlanCapability: daemonClientUnavailable,
  listNativePlanRevisions: daemonClientUnavailable,
  listNativePlanClarifications: daemonClientUnavailable,
  replyNativePlanClarification: daemonClientUnavailable,
  exportNativePlan: daemonClientUnavailable,
  scaffold: daemonClientUnavailable
};

const unboundHostedBootstrapPort: HostedBootstrapPort = {
  getStatus: daemonClientUnavailable,
  initializeProject: daemonClientUnavailable,
  grantProviderNetworkConsent: daemonClientUnavailable,
  startLogin: daemonClientUnavailable,
  cancelLogin: daemonClientUnavailable,
  signOut: daemonClientUnavailable
};

type HarnessPortRegistry = {
  daemonPort?: DaemonHarnessPort;
  daemonBinding?: DaemonProjectBinding;
  daemonEnvironmentInitialized?: boolean;
  hostedBootstrapPort?: HostedBootstrapPort;
  hostedBootstrapEnvironmentInitialized?: boolean;
};

const HARNESS_PORT_REGISTRY = Symbol.for('chirality.app.harness-port-registry/v1');

function portRegistry(): HarnessPortRegistry {
  const target = globalThis as typeof globalThis & {
    [HARNESS_PORT_REGISTRY]?: HarnessPortRegistry;
  };
  return target[HARNESS_PORT_REGISTRY] ??= {};
}

export function getDaemonHarnessPort(): DaemonHarnessPort {
  const registry = portRegistry();
  if (registry.daemonPort === undefined && !registry.daemonEnvironmentInitialized) {
    // Loading is intentionally lazy: tests and alternate hosts may inject a
    // port, while production route evaluation never constructs an engine.
    registry.daemonPort = createRuntimeDaemonHarnessPortFromEnvironment();
    registry.daemonEnvironmentInitialized = true;
    const projectId = process.env.CHIRALITY_RUNTIME_PROJECT_ID?.trim();
    const projectRoot = process.env.CHIRALITY_RUNTIME_PROJECT_ROOT?.trim();
    if (projectId && projectRoot) {
      registry.daemonBinding = { projectId, projectRoot: resolve(projectRoot) };
    }
  }
  return registry.daemonPort ?? unboundDaemonHarnessPort;
}

export function getHostedBootstrapPort(): HostedBootstrapPort {
  const registry = portRegistry();
  if (
    registry.hostedBootstrapPort === undefined &&
    !registry.hostedBootstrapEnvironmentInitialized
  ) {
    registry.hostedBootstrapPort = createRuntimeHostedBootstrapPortFromEnvironment(
      process.env,
      installBoundDaemonHarnessPort
    );
    registry.hostedBootstrapEnvironmentInitialized = true;
  }
  return registry.hostedBootstrapPort ?? unboundHostedBootstrapPort;
}

/**
 * Installed by the Desktop runtime-client composition root after it has loaded
 * the authenticated daemon client. It is deliberately not initialized from a
 * route module, which prevents Next from owning a second runtime singleton.
 */
export function installDaemonHarnessPort(port: DaemonHarnessPort): void {
  const registry = portRegistry();
  registry.daemonEnvironmentInitialized = true;
  registry.daemonPort = port;
  registry.daemonBinding = undefined;
}

export function installBoundDaemonHarnessPort(
  port: DaemonHarnessPort,
  binding: DaemonProjectBinding,
  allowReplacement = false
): void {
  const registry = portRegistry();
  const current = registry.daemonBinding;
  if (
    registry.daemonPort !== undefined &&
    !allowReplacement &&
    (current === undefined ||
      current.projectId !== binding.projectId ||
      current.projectRoot !== binding.projectRoot)
  ) {
    throw new HarnessError(
      'WORKING_ROOT_CONFLICT',
      409,
      'A different project is already bound to the Desktop runtime client'
    );
  }
  registry.daemonEnvironmentInitialized = true;
  registry.daemonPort = port;
  registry.daemonBinding = binding;
}

export function installHostedBootstrapPort(port: HostedBootstrapPort): void {
  const registry = portRegistry();
  registry.hostedBootstrapEnvironmentInitialized = true;
  registry.hostedBootstrapPort = port;
}

export function resetDaemonHarnessPortForTests(): void {
  const registry = portRegistry();
  registry.daemonEnvironmentInitialized = false;
  registry.daemonPort = undefined;
  registry.daemonBinding = undefined;
  registry.hostedBootstrapEnvironmentInitialized = false;
  registry.hostedBootstrapPort = undefined;
}
