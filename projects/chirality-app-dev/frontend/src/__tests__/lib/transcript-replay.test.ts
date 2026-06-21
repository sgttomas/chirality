import { describe, expect, it } from 'vitest';
import type { HarnessEvent, HarnessEventType } from '../../lib/harness/event-schema';
import { deriveTranscriptView } from '../../lib/harness/transcript-replay';
import type { SessionRecord } from '../../lib/harness/types';

let counter = 0;

function event(
  type: HarnessEventType,
  data: Record<string, unknown>,
  turnId = 'turn_1'
): HarnessEvent {
  counter += 1;
  return {
    schemaVersion: 1,
    eventId: `evt_${counter}`,
    sessionId: 'sess_transcript',
    turnId,
    timestamp: `2026-06-21T00:00:0${counter}.000Z`,
    type,
    data
  };
}

describe('deriveTranscriptView', () => {
  it('projects messages, tool artifacts, and terminal events from replay data', () => {
    const events = [
      event('message.completed', { role: 'user', text: 'Summarize the file.' }),
      event('message.delta', { role: 'assistant', text: 'Partial ' }),
      event('message.delta', { role: 'assistant', text: 'answer' }),
      event('message.completed', { role: 'assistant', text: 'Final answer.' }),
      event('tool.completed', {
        toolName: 'Read',
        resultMetadata: {
          contentItemCount: 2,
          contentTypes: ['text'],
          resultByteLength: 128,
          outputPersisted: true
        },
        artifactMetadata: {
          artifactRelativePath: 'artifacts/tools/read.json',
          artifactByteLength: 128,
          redacted: true,
          truncated: false
        }
      }),
      event('turn.completed', { stopReason: 'end_turn' })
    ];

    const transcript = deriveTranscriptView(events);

    expect(transcript.sessionId).toBe('sess_transcript');
    expect(transcript.terminalStatus).toBe('completed');
    expect(transcript.items.map((item) => item.kind)).toEqual([
      'message',
      'message',
      'tool',
      'terminal'
    ]);
    expect(transcript.items[0]).toMatchObject({
      role: 'user',
      text: 'Summarize the file.',
      status: 'completed'
    });
    expect(transcript.items[1]).toMatchObject({
      role: 'assistant',
      text: 'Final answer.',
      status: 'completed'
    });
    expect(transcript.items[2]).toMatchObject({
      kind: 'tool',
      toolName: 'Read',
      summary: '2 content items / text / 128 bytes / artifact saved',
      artifact: {
        artifactRelativePath: 'artifacts/tools/read.json',
        artifactByteLength: 128,
        redacted: true,
        truncated: false
      }
    });
  });

  it('uses accumulated assistant deltas when no completed assistant message exists', () => {
    const transcript = deriveTranscriptView([
      event('message.delta', { role: 'assistant', text: 'streamed ' }, 'turn_stream'),
      event('message.delta', { role: 'assistant', text: 'answer' }, 'turn_stream')
    ]);

    expect(transcript.items).toHaveLength(1);
    expect(transcript.items[0]).toMatchObject({
      kind: 'message',
      role: 'assistant',
      status: 'started',
      text: 'streamed answer'
    });
  });

  it('includes SDK linkage from the canonical session record', () => {
    const session: SessionRecord = {
      sessionId: 'sess_transcript',
      projectRoot: '/tmp/project',
      persona: 'WORKING_ITEMS',
      mode: 'CHAT',
      createdAt: '2026-06-21T00:00:00.000Z',
      updatedAt: '2026-06-21T00:00:00.000Z',
      engineSessionId: 'engine_1',
      claudeSessionId: 'claude_legacy',
      sdkSessionId: 'sdk_1',
      sdkTranscriptPath: '/tmp/project/.chirality/sessions/sess_transcript/sdk/transcript.jsonl',
      sdkSessionStoreKey: 'store-key',
      sdkConfigDir: '/tmp/config',
      sdkSettingSources: ['env', 'ui'],
      sdkPackageVersion: '0.3.150',
      sdkClaudeCodeVersion: '1.0.0',
      model: 'claude-test'
    };

    const transcript = deriveTranscriptView([], session);

    expect(transcript.sessionId).toBe('sess_transcript');
    expect(transcript.sdkLinkage).toMatchObject({
      engineSessionId: 'engine_1',
      claudeSessionId: 'claude_legacy',
      sdkSessionId: 'sdk_1',
      sdkTranscriptPath: expect.stringContaining('transcript.jsonl'),
      sdkSessionStoreKey: 'store-key',
      sdkConfigDir: '/tmp/config',
      sdkSettingSources: ['env', 'ui'],
      sdkPackageVersion: '0.3.150',
      sdkClaudeCodeVersion: '1.0.0',
      model: 'claude-test'
    });
  });
});
