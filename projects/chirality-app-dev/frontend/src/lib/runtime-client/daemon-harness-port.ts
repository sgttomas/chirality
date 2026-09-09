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
  NativePlanRevisionsResponse,
  ReplaceSelectedMethodsRequest,
  ReplaceSelectedMethodsResponse,
  ResolveSelectedContextRequest,
  ResolveSelectedContextResponse,
  RolesResponse
} from '@chirality/runtime-contracts/v3';
import type { ReadableRuntimeSessionRecord } from '@chirality/runtime-contracts';
import { createRuntimeDaemonHarnessPortFromEnvironment } from './runtime-daemon-harness-port';

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
  exportNativePlan: daemonClientUnavailable,
  scaffold: daemonClientUnavailable
};

let daemonHarnessPort: DaemonHarnessPort = unboundDaemonHarnessPort;
let environmentPortInitialized = false;

export function getDaemonHarnessPort(): DaemonHarnessPort {
  if (daemonHarnessPort === unboundDaemonHarnessPort && !environmentPortInitialized) {
    // Loading is intentionally lazy: tests and alternate hosts may inject a
    // port, while production route evaluation never constructs an engine.
    daemonHarnessPort = createRuntimeDaemonHarnessPortFromEnvironment();
    environmentPortInitialized = true;
  }
  return daemonHarnessPort;
}

/**
 * Installed by the Desktop runtime-client composition root after it has loaded
 * the authenticated daemon client. It is deliberately not initialized from a
 * route module, which prevents Next from owning a second runtime singleton.
 */
export function installDaemonHarnessPort(port: DaemonHarnessPort): void {
  environmentPortInitialized = true;
  daemonHarnessPort = port;
}

export function resetDaemonHarnessPortForTests(): void {
  environmentPortInitialized = false;
  daemonHarnessPort = unboundDaemonHarnessPort;
}
