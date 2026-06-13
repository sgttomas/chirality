import { randomUUID } from 'node:crypto';

export const HARNESS_EVENT_TYPES = [
  'session.created',
  'session.resumed',
  'turn.accepted',
  'turn.started',
  'adapter.initialized',
  'model.request.started',
  'model.delta',
  'model.completed',
  'turn.completed',
  'turn.failed',
  'turn.cancelled',
  'tool.permission',
  'context.compacted',
  'runtime.mirror.error'
] as const;

export type HarnessEventType = (typeof HARNESS_EVENT_TYPES)[number];

export type HarnessEvent = {
  schemaVersion: 1;
  eventId: string;
  sessionId: string;
  turnId?: string;
  parentEventId?: string;
  timestamp: string;
  type: HarnessEventType;
  data: Record<string, unknown>;
};

export function createHarnessEvent(input: {
  sessionId: string;
  type: HarnessEventType;
  data?: Record<string, unknown>;
  turnId?: string;
  parentEventId?: string;
}): HarnessEvent {
  return {
    schemaVersion: 1,
    eventId: `evt_${randomUUID()}`,
    sessionId: input.sessionId,
    turnId: input.turnId,
    parentEventId: input.parentEventId,
    timestamp: new Date().toISOString(),
    type: input.type,
    data: input.data ?? {}
  };
}
