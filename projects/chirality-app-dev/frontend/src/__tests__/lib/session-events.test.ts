import { mkdtemp, rm } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';
import { createHarnessEvent } from '../../lib/harness/event-schema';
import { appendHarnessEvent, replayHarnessEvents } from '../../lib/harness/session-events';

let tmpDir = '';

afterEach(async () => {
  delete process.env.CHIRALITY_SESSION_ROOT;
  if (tmpDir) {
    await rm(tmpDir, { recursive: true, force: true });
    tmpDir = '';
  }
});

describe('session events', () => {
  it('appends and replays HarnessEvent JSONL records', async () => {
    tmpDir = await mkdtemp(path.join(os.tmpdir(), 'chirality-session-events-'));
    process.env.CHIRALITY_SESSION_ROOT = path.join(tmpDir, 'sessions');
    const event = createHarnessEvent({
      sessionId: 'sess_1',
      type: 'turn.accepted',
      data: {
        apiKey: 'not-a-real-key'
      }
    });

    const filePath = await appendHarnessEvent(event);
    const replay = await replayHarnessEvents('sess_1');

    expect(filePath).toContain(path.join('sessions', 'sess_1', 'events.jsonl'));
    expect(replay.malformedLineCount).toBe(0);
    expect(replay.events).toHaveLength(1);
    expect(replay.events[0]).toMatchObject({
      schemaVersion: 1,
      sessionId: 'sess_1',
      type: 'turn.accepted'
    });
  });
});
