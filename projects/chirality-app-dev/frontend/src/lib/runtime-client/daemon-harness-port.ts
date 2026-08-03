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
  session: SessionRecord;
  transcript: TranscriptView;
};

export type RunningDaemonHarnessTurn = {
  events: AsyncIterable<UIEvent>;
  cancel(): Promise<void>;
};

export type DaemonRequestOptions = {
  signal?: AbortSignal;
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
    request: SessionCreateRequest,
    options?: DaemonRequestOptions
  ): Promise<{ session: SessionRecord }>;
  listSessions(
    projectRoot: string,
    options?: DaemonRequestOptions
  ): Promise<{ sessions: SessionRecord[] }>;
  getSession(
    sessionId: string,
    options?: DaemonRequestOptions
  ): Promise<{ session: SessionRecord }>;
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
    request: TurnRequest,
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
