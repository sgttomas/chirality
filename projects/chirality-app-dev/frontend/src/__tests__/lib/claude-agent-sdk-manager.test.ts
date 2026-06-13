import type { SDKMessage } from '@anthropic-ai/claude-agent-sdk';
import { mkdtemp, rm } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { ClaudeAgentSdkManager } from '../../lib/harness/claude-agent-sdk-manager';
import { replayHarnessEvents } from '../../lib/harness/session-events';
import type { ResolvedOpts, SessionRecord } from '../../lib/harness/types';

async function* createSdkStream(events: SDKMessage[]): AsyncGenerator<SDKMessage, void> {
  for (const event of events) {
    yield event;
  }
}

function createQuery(events: SDKMessage[]) {
  const stream = createSdkStream(events) as AsyncGenerator<SDKMessage, void> & {
    interrupt: () => Promise<void>;
    close: () => void;
  };
  stream.interrupt = vi.fn(async () => undefined);
  stream.close = vi.fn();
  return vi.fn(() => stream);
}

const session: SessionRecord = {
  sessionId: 'sess_sdk',
  projectRoot: '/tmp/project',
  persona: 'WORKING_ITEMS',
  mode: 'direct',
  createdAt: '2026-02-23T00:00:00.000Z',
  updatedAt: '2026-02-23T00:00:00.000Z'
};

const opts: ResolvedOpts = {
  model: 'claude-test',
  tools: [],
  maxTurns: 2,
  persona: 'WORKING_ITEMS',
  mode: 'direct'
};

let tmpDir = '';

afterEach(async () => {
  delete process.env.CHIRALITY_SESSION_ROOT;
  if (tmpDir) {
    await rm(tmpDir, { recursive: true, force: true });
    tmpDir = '';
  }
});

describe('ClaudeAgentSdkManager', () => {
  it('maps SDK stream messages to existing UI events and appends HarnessEvent evidence', async () => {
    tmpDir = await mkdtemp(path.join(os.tmpdir(), 'chirality-sdk-manager-'));
    process.env.CHIRALITY_SESSION_ROOT = path.join(tmpDir, 'sessions');
    const query = createQuery([
      {
        type: 'system',
        subtype: 'init',
        session_id: 'sdk_1',
        uuid: '00000000-0000-0000-0000-000000000001',
        apiKeySource: 'temporary',
        claude_code_version: '1.2.3',
        cwd: '/tmp/project',
        tools: [],
        mcp_servers: [],
        model: 'claude-test',
        permissionMode: 'default',
        slash_commands: [],
        output_style: 'default',
        skills: [],
        plugins: []
      },
      {
        type: 'stream_event',
        event: {
          type: 'content_block_delta',
          index: 0,
          delta: { type: 'text_delta', text: 'Hi' }
        },
        parent_tool_use_id: null,
        uuid: '00000000-0000-0000-0000-000000000002',
        session_id: 'sdk_1'
      },
      {
        type: 'result',
        subtype: 'success',
        duration_ms: 10,
        duration_api_ms: 9,
        is_error: false,
        num_turns: 1,
        result: 'Hi',
        stop_reason: 'end_turn',
        total_cost_usd: 0,
        usage: {} as never,
        modelUsage: {},
        permission_denials: [],
        uuid: '00000000-0000-0000-0000-000000000003',
        session_id: 'sdk_1'
      }
    ]);
    const manager = new ClaudeAgentSdkManager(query as never, async () => 'persona prompt');
    const events = [];

    for await (const event of manager.startTurn(session, 'hello', opts)) {
      events.push(event);
    }

    expect(events.map((event) => event.type)).toEqual([
      'session:init',
      'chat:delta',
      'chat:complete',
      'session:complete',
      'process:exit'
    ]);
    expect(query).toHaveBeenCalledWith(
      expect.objectContaining({
        prompt: 'hello',
        options: expect.objectContaining({
          settingSources: [],
          tools: [],
          allowedTools: []
        })
      })
    );
    const replay = await replayHarnessEvents('sess_sdk');
    expect(replay.events.map((event) => event.type)).toEqual([
      'turn.accepted',
      'turn.started',
      'adapter.initialized',
      'model.delta',
      'message.delta',
      'model.completed',
      'turn.completed'
    ]);
  });
});
