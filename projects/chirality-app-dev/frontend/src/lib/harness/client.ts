import type { AgentRosterEntry } from './agent-roster';
import type { HarnessEvent } from './event-schema';
import type { HarnessReplaySummary } from './session-events';
import type { TranscriptView } from './transcript-replay';
import type {
  CoordinationMode,
  HarnessErrorResponse,
  InterruptRequest,
  ScaffoldExecutionRootResponse,
  SessionBootRequest,
  SessionBootResponse,
  SessionCreateRequest,
  SessionRecord,
  TurnRequest
} from './types';

export type SessionEventsReplay = {
  events: HarnessEvent[];
  malformedLineCount: number;
  summary: HarnessReplaySummary;
  session?: SessionRecord;
  transcript?: TranscriptView;
};

type JsonLike = Record<string, unknown>;

export type HarnessTurnStreamEvent = {
  event: string;
  data: unknown;
};

export class HarnessApiClientError extends Error {
  readonly status: number;
  readonly code: string;
  readonly details?: unknown;

  constructor(status: number, code: string, message: string, details?: unknown) {
    super(message);
    this.name = 'HarnessApiClientError';
    this.status = status;
    this.code = code;
    this.details = details;
  }
}

async function readJson<T>(response: Response): Promise<T | undefined> {
  try {
    return (await response.json()) as T;
  } catch {
    return undefined;
  }
}

function fromHarnessErrorPayload(
  status: number,
  payload: HarnessErrorResponse | undefined,
  fallbackMessage: string
): HarnessApiClientError {
  const code = payload?.error?.type ?? 'HARNESS_API_ERROR';
  const message = payload?.error?.message ?? fallbackMessage;
  return new HarnessApiClientError(status, code, message, payload?.error?.details);
}

async function requestHarnessJson<T>(
  input: RequestInfo | URL,
  init: RequestInit,
  fallbackMessage: string
): Promise<T> {
  const response = await fetch(input, init);
  const payload = await readJson<T & HarnessErrorResponse>(response);

  if (!response.ok) {
    throw fromHarnessErrorPayload(response.status, payload, fallbackMessage);
  }

  if (!payload) {
    throw new HarnessApiClientError(
      response.status,
      'INVALID_RESPONSE',
      'Harness API returned an empty response body'
    );
  }

  return payload;
}

function parseSseFrame(frame: string): HarnessTurnStreamEvent | null {
  const lines = frame.split('\n');
  let event = '';
  const dataLines: string[] = [];

  for (const line of lines) {
    if (line.startsWith('event:')) {
      event = line.slice('event:'.length).trim();
      continue;
    }

    if (line.startsWith('data:')) {
      dataLines.push(line.slice('data:'.length).trimStart());
    }
  }

  if (!event || dataLines.length === 0) {
    return null;
  }

  const rawData = dataLines.join('\n');

  try {
    return {
      event,
      data: JSON.parse(rawData) as JsonLike
    };
  } catch {
    return {
      event,
      data: rawData
    };
  }
}

async function openTurnStream(input: TurnRequest): Promise<Response> {
  const response = await fetch('/api/harness/turn', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(input)
  });

  if (response.ok) {
    return response;
  }

  const payload = await readJson<HarnessErrorResponse>(response);
  throw fromHarnessErrorPayload(response.status, payload, 'Unable to start harness turn');
}

export function harnessApiErrorMessage(error: unknown): string {
  if (error instanceof HarnessApiClientError) {
    return `${error.code}: ${error.message}`;
  }

  if (error instanceof Error) {
    return error.message;
  }

  return 'Unexpected harness API failure';
}

/**
 * Fetch the direct-chat persona roster (Type-0/Type-1 only, server-filtered via
 * `?directChat=1`) for the persona picker. D-APP-24 restricts direct chat to
 * conversational personas; Type-2 task agents run only via orchestration.
 */
export async function listDirectChatPersonas(): Promise<AgentRosterEntry[]> {
  const payload = await requestHarnessJson<{ agents: AgentRosterEntry[] }>(
    '/api/harness/agents?directChat=1',
    { method: 'GET' },
    'Unable to load direct-chat personas'
  );

  return payload.agents;
}

/**
 * List the harness sessions recorded for a Working Root (most-recent ordering
 * is whatever the server returns). Feeds the Phase 5 session-list UI (D-APP-22).
 */
export async function listHarnessSessions(projectRoot: string): Promise<SessionRecord[]> {
  const payload = await requestHarnessJson<{ sessions: SessionRecord[] }>(
    `/api/harness/session/list?projectRoot=${encodeURIComponent(projectRoot)}`,
    { method: 'GET' },
    'Unable to list harness sessions'
  );

  return payload.sessions;
}

/**
 * Replay a session's persisted harness events (D-APP-22 hydrate-on-open). The
 * caller seeds the live buffer with `events`; `malformedLineCount` is surfaced
 * so a corrupt log is reported, not silently dropped.
 */
export async function replaySessionEvents(sessionId: string): Promise<SessionEventsReplay> {
  return requestHarnessJson<SessionEventsReplay>(
    `/api/harness/session/${encodeURIComponent(sessionId)}/events`,
    { method: 'GET' },
    'Unable to load session events'
  );
}

export async function createHarnessSession(input: SessionCreateRequest): Promise<SessionRecord> {
  const payload = await requestHarnessJson<{ session: SessionRecord }>(
    '/api/harness/session/create',
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(input)
    },
    'Unable to create harness session'
  );

  return payload.session;
}

export async function bootHarnessSession(input: SessionBootRequest): Promise<SessionBootResponse> {
  return requestHarnessJson<SessionBootResponse>(
    '/api/harness/session/boot',
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(input)
    },
    'Unable to boot harness session'
  );
}

export async function decideHarnessPermission(input: {
  sessionId: string;
  toolUseId: string;
  verdict: 'allow' | 'deny';
}): Promise<{ ok: boolean; decided: boolean }> {
  return requestHarnessJson<{ ok: boolean; decided: boolean }>(
    '/api/harness/permission',
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(input)
    },
    'Unable to submit permission decision'
  );
}

export async function interruptHarnessSession(input: InterruptRequest): Promise<void> {
  await requestHarnessJson<{ ok: boolean }>(
    '/api/harness/interrupt',
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(input)
    },
    'Unable to interrupt harness session'
  );
}

export async function scaffoldHarnessExecutionRoot(input: {
  executionRoot: string;
  decompositionPath: string;
  projectName?: string;
  coordinationMode?: CoordinationMode;
}): Promise<ScaffoldExecutionRootResponse> {
  return requestHarnessJson<ScaffoldExecutionRootResponse>(
    '/api/harness/scaffold',
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(input)
    },
    'Unable to scaffold execution root'
  );
}

export async function streamHarnessTurn(
  input: TurnRequest,
  onEvent: (event: HarnessTurnStreamEvent) => void
): Promise<void> {
  const response = await openTurnStream(input);
  if (!response.body) {
    throw new HarnessApiClientError(
      response.status,
      'INVALID_RESPONSE',
      'Harness turn response did not include a stream body'
    );
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let buffer = '';

  while (true) {
    const { done, value } = await reader.read();
    if (done) {
      break;
    }

    if (value) {
      buffer += decoder.decode(value, { stream: true });
    }

    while (true) {
      const boundaryIndex = buffer.indexOf('\n\n');
      if (boundaryIndex < 0) {
        break;
      }

      const frame = buffer.slice(0, boundaryIndex);
      buffer = buffer.slice(boundaryIndex + 2);
      const parsed = parseSseFrame(frame);
      if (parsed) {
        onEvent(parsed);
      }
    }
  }

  buffer += decoder.decode();
  const trailingFrame = buffer.trim();
  if (trailingFrame) {
    const parsed = parseSseFrame(trailingFrame);
    if (parsed) {
      onEvent(parsed);
    }
  }
}
