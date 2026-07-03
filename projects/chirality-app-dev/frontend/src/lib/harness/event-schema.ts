import { randomUUID } from 'node:crypto';

export { HARNESS_EVENT_TYPES } from '@chirality/harness-contract/event-schema';
export type { HarnessEvent, HarnessEventType } from '@chirality/harness-contract/event-schema';

import type { HarnessEvent, HarnessEventType } from '@chirality/harness-contract/event-schema';

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
