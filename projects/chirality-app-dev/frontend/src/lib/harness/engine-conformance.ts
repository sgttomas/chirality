import {
  AgentEnginePort,
  AgentEngineRunInput,
  EngineAdapterSubject,
  PUBLIC_UI_EVENT_NAMES
} from './agent-engine-port';
import { UIEvent } from './types';

export type EngineConformanceIssueCode =
  | 'STREAM_THREW'
  | 'UNKNOWN_UI_EVENT'
  | 'MISSING_SESSION_INIT'
  | 'MISSING_ENGINE_SESSION_ID'
  | 'MISSING_SESSION_INIT_MODEL'
  | 'MISSING_PROCESS_EXIT'
  | 'PROCESS_EXIT_NOT_TERMINAL'
  | 'MISSING_INTERRUPTED_PROCESS_EXIT';

export type EngineConformanceIssue = {
  code: EngineConformanceIssueCode;
  message: string;
  eventIndex?: number;
  eventType?: string;
};

export type EngineConformanceOptions = {
  requireSessionInit?: boolean;
  requireEngineSessionId?: boolean;
  requireInterruptedProcessExit?: boolean;
};

export type EngineConformanceReport = {
  subject: EngineAdapterSubject;
  passed: boolean;
  events: UIEvent[];
  eventTypes: string[];
  issues: EngineConformanceIssue[];
};

const PUBLIC_UI_EVENT_NAME_SET = new Set<string>(PUBLIC_UI_EVENT_NAMES);

function summarizeThrownError(error: unknown): string {
  return error instanceof Error ? error.message : String(error);
}

function readEventType(event: unknown): string | undefined {
  return event && typeof event === 'object' && 'type' in event
    ? String((event as { type: unknown }).type)
    : undefined;
}

function isSessionInitEvent(event: UIEvent): event is Extract<UIEvent, { type: 'session:init' }> {
  return event.type === 'session:init';
}

function isProcessExitEvent(event: UIEvent): event is Extract<UIEvent, { type: 'process:exit' }> {
  return event.type === 'process:exit';
}

function evaluateEventStream(
  subject: EngineAdapterSubject,
  events: UIEvent[],
  options: EngineConformanceOptions,
  thrownError?: unknown
): EngineConformanceReport {
  const issues: EngineConformanceIssue[] = [];
  const eventTypes = events.map((event) => readEventType(event) ?? '<missing>');

  if (thrownError !== undefined) {
    issues.push({
      code: 'STREAM_THREW',
      message: `Engine stream threw before terminal evidence: ${summarizeThrownError(thrownError)}`
    });
  }

  events.forEach((event, eventIndex) => {
    const eventType = readEventType(event);
    if (!eventType || !PUBLIC_UI_EVENT_NAME_SET.has(eventType)) {
      issues.push({
        code: 'UNKNOWN_UI_EVENT',
        message: `Engine emitted non-public UI event '${eventType ?? '<missing>'}'`,
        eventIndex,
        eventType
      });
    }
  });

  const sessionInitCount = events.filter(isSessionInitEvent).length;
  if (options.requireSessionInit !== false && sessionInitCount === 0) {
    issues.push({
      code: 'MISSING_SESSION_INIT',
      message: 'Engine did not emit session:init metadata'
    });
  }

  events.forEach((event, eventIndex) => {
    if (!isSessionInitEvent(event)) {
      return;
    }

    if (options.requireEngineSessionId && !event.data.engineSessionId) {
      issues.push({
        code: 'MISSING_ENGINE_SESSION_ID',
        message: 'session:init did not include provider-neutral engineSessionId metadata',
        eventIndex,
        eventType: event.type
      });
    }
    if (!event.data.model) {
      issues.push({
        code: 'MISSING_SESSION_INIT_MODEL',
        message: 'session:init did not include model metadata',
        eventIndex,
        eventType: event.type
      });
    }
  });

  const processExitIndex = events.findIndex(isProcessExitEvent);
  if (processExitIndex < 0) {
    issues.push({
      code: 'MISSING_PROCESS_EXIT',
      message: 'Engine did not emit terminal process:exit evidence'
    });
  } else if (processExitIndex !== events.length - 1) {
    issues.push({
      code: 'PROCESS_EXIT_NOT_TERMINAL',
      message: 'process:exit must be the final public UI event',
      eventIndex: processExitIndex,
      eventType: 'process:exit'
    });
  }

  if (
    options.requireInterruptedProcessExit &&
    !events.some(
      (event) =>
        isProcessExitEvent(event) && event.data.exitCode === 130 && event.data.interrupted === true
    )
  ) {
    issues.push({
      code: 'MISSING_INTERRUPTED_PROCESS_EXIT',
      message: 'Interrupted turn did not emit process:exit with exitCode 130 and interrupted=true'
    });
  }

  return {
    subject,
    passed: issues.length === 0,
    events,
    eventTypes,
    issues
  };
}

export async function runEngineConformance(
  port: AgentEnginePort,
  input: AgentEngineRunInput,
  options: EngineConformanceOptions = {}
): Promise<EngineConformanceReport> {
  const events: UIEvent[] = [];
  let thrownError: unknown;

  try {
    for await (const event of port.startTurn(input)) {
      events.push(event);
    }
  } catch (error) {
    thrownError = error;
  }

  return evaluateEventStream(port.subject, events, options, thrownError);
}

export async function runEngineInterruptConformance(
  port: AgentEnginePort,
  input: AgentEngineRunInput,
  options: EngineConformanceOptions = {}
): Promise<EngineConformanceReport> {
  const events: UIEvent[] = [];
  let thrownError: unknown;
  const iterator = port.startTurn(input)[Symbol.asyncIterator]();

  try {
    const first = await iterator.next();
    if (!first.done) {
      events.push(first.value);
    }

    await port.interrupt(input.session.sessionId);

    while (true) {
      const next = await iterator.next();
      if (next.done) {
        break;
      }
      events.push(next.value);
    }
  } catch (error) {
    thrownError = error;
  }

  return evaluateEventStream(
    port.subject,
    events,
    {
      ...options,
      requireInterruptedProcessExit: true
    },
    thrownError
  );
}
