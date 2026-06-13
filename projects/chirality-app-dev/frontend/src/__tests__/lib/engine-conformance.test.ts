import type { SDKMessage } from '@anthropic-ai/claude-agent-sdk';
import { mkdtemp, rm } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, describe, expect, it, vi } from 'vitest';
import type { AgentEnginePort, AgentEngineRunInput } from '../../lib/harness/agent-engine-port';
import { ClaudeAgentSdkManager } from '../../lib/harness/claude-agent-sdk-manager';
import {
  runEngineConformance,
  runEngineInterruptConformance
} from '../../lib/harness/engine-conformance';
import { replayHarnessEvents } from '../../lib/harness/session-events';
import type { ResolvedOpts, SessionRecord, UIEvent } from '../../lib/harness/types';

const session: SessionRecord = {
  sessionId: 'sess_engine_conformance',
  projectRoot: '/tmp/project',
  persona: 'WORKING_ITEMS',
  mode: 'direct',
  createdAt: '2026-06-13T00:00:00.000Z',
  updatedAt: '2026-06-13T00:00:00.000Z'
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

function createRunInput(overrides: Partial<AgentEngineRunInput> = {}): AgentEngineRunInput {
  return {
    session,
    message: 'hello',
    opts,
    ...overrides
  };
}

function sdkInit(sessionId = 'sdk_1'): SDKMessage {
  return {
    type: 'system',
    subtype: 'init',
    session_id: sessionId,
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
  };
}

function sdkDelta(sessionId = 'sdk_1', text = 'Hi'): SDKMessage {
  return {
    type: 'stream_event',
    event: {
      type: 'content_block_delta',
      index: 0,
      delta: { type: 'text_delta', text }
    },
    parent_tool_use_id: null,
    uuid: '00000000-0000-0000-0000-000000000002',
    session_id: sessionId
  };
}

function sdkSuccess(sessionId = 'sdk_1', text = 'Hi'): SDKMessage {
  return {
    type: 'result',
    subtype: 'success',
    duration_ms: 10,
    duration_api_ms: 9,
    is_error: false,
    num_turns: 1,
    result: text,
    stop_reason: 'end_turn',
    total_cost_usd: 0,
    usage: {} as never,
    modelUsage: {},
    permission_denials: [],
    uuid: '00000000-0000-0000-0000-000000000003',
    session_id: sessionId
  };
}

function sdkFailure(sessionId = 'sdk_1'): SDKMessage {
  return {
    type: 'result',
    subtype: 'error_during_execution',
    duration_ms: 10,
    duration_api_ms: 9,
    is_error: true,
    num_turns: 1,
    total_cost_usd: 0,
    usage: {} as never,
    modelUsage: {},
    permission_denials: [],
    errors: ['provider failed'],
    terminal_reason: 'provider_error',
    uuid: '00000000-0000-0000-0000-000000000004',
    session_id: sessionId
  } as never;
}

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

function createInterruptibleQuery(eventsBeforeInterrupt: SDKMessage[]) {
  let resolveInterrupt: () => void = () => undefined;
  const interrupted = new Promise<void>((resolve) => {
    resolveInterrupt = resolve;
  });
  const stream = (async function* (): AsyncGenerator<SDKMessage, void> {
    for (const event of eventsBeforeInterrupt) {
      yield event;
    }
    await interrupted;
    yield sdkDelta('sdk_interrupt', 'after interrupt');
  })() as AsyncGenerator<SDKMessage, void> & {
    interrupt: () => Promise<void>;
    close: () => void;
  };
  stream.interrupt = vi.fn(async () => {
    resolveInterrupt();
  });
  stream.close = vi.fn();
  return vi.fn(() => stream);
}

class ScriptedEnginePort implements AgentEnginePort {
  readonly subject = 'stub' as const;

  constructor(private readonly script: Array<UIEvent | { type: string; data: unknown }>) {}

  async *startTurn(_input: AgentEngineRunInput): AsyncIterable<UIEvent> {
    for (const event of this.script) {
      yield event as UIEvent;
    }
  }

  async interrupt(_sessionId: string): Promise<void> {
    return undefined;
  }
}

async function useTempSessionRoot(): Promise<void> {
  tmpDir = await mkdtemp(path.join(os.tmpdir(), 'chirality-engine-conformance-'));
  process.env.CHIRALITY_SESSION_ROOT = path.join(tmpDir, 'sessions');
}

describe('engine conformance fixtures', () => {
  it('passes a Claude Agent SDK success stream against the provider-neutral engine contract', async () => {
    await useTempSessionRoot();
    const query = createQuery([sdkInit(), sdkDelta(), sdkSuccess()]);
    const manager = new ClaudeAgentSdkManager(query as never, async () => 'persona prompt');

    const report = await runEngineConformance(manager, createRunInput(), {
      requireEngineSessionId: true
    });

    expect(report.passed).toBe(true);
    expect(report.issues).toEqual([]);
    expect(report.eventTypes).toEqual([
      'session:init',
      'chat:delta',
      'chat:complete',
      'session:complete',
      'process:exit'
    ]);
    expect(report.eventTypes.join(' ')).not.toMatch(/sdk|claude|anthropic/i);
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

    const replay = await replayHarnessEvents(session.sessionId);
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

  it('treats scripted provider failure as terminal public evidence instead of a provider-shaped UI event', async () => {
    await useTempSessionRoot();
    const manager = new ClaudeAgentSdkManager(
      createQuery([sdkInit(), sdkFailure()]) as never,
      async () => 'persona prompt'
    );

    const report = await runEngineConformance(manager, createRunInput(), {
      requireEngineSessionId: true
    });

    expect(report.passed).toBe(true);
    expect(report.eventTypes).toEqual(['session:init', 'process:exit']);
    expect(report.events.at(-1)).toMatchObject({
      type: 'process:exit',
      data: {
        exitCode: 1,
        errorType: 'SDK_FAILURE',
        fatal: true
      }
    });

    const replay = await replayHarnessEvents(session.sessionId);
    expect(replay.events.map((event) => event.type)).toEqual([
      'turn.accepted',
      'turn.started',
      'adapter.initialized',
      'turn.failed'
    ]);
  });

  it('requires interrupted adapter turns to emit cancellation terminal evidence', async () => {
    await useTempSessionRoot();
    const manager = new ClaudeAgentSdkManager(
      createInterruptibleQuery([sdkInit('sdk_interrupt')]) as never,
      async () => 'persona prompt'
    );

    const report = await runEngineInterruptConformance(manager, createRunInput(), {
      requireEngineSessionId: true
    });

    expect(report.passed).toBe(true);
    expect(report.eventTypes).toEqual(['session:init', 'process:exit']);
    expect(report.events.at(-1)).toMatchObject({
      type: 'process:exit',
      data: {
        exitCode: 130,
        interrupted: true
      }
    });

    const replay = await replayHarnessEvents(session.sessionId);
    expect(replay.events.map((event) => event.type)).toEqual([
      'turn.accepted',
      'turn.started',
      'adapter.initialized',
      'interruption.requested',
      'interruption.completed',
      'turn.cancelled'
    ]);
  });

  it('flags non-public event names from scripted adapters', async () => {
    const port = new ScriptedEnginePort([
      {
        type: 'session:init',
        data: {
          engineSessionId: 'engine_1',
          claudeSessionId: 'claude_1',
          model: 'claude-test'
        }
      },
      { type: 'sdk:delta', data: { text: 'provider-shaped event name' } },
      { type: 'process:exit', data: { exitCode: 0 } }
    ]);

    const report = await runEngineConformance(port, createRunInput(), {
      requireEngineSessionId: true
    });

    expect(report.passed).toBe(false);
    expect(report.issues).toEqual([
      expect.objectContaining({
        code: 'UNKNOWN_UI_EVENT',
        eventType: 'sdk:delta'
      })
    ]);
  });

  it('flags scripted adapters that finish without process:exit evidence', async () => {
    const port = new ScriptedEnginePort([
      {
        type: 'session:init',
        data: {
          engineSessionId: 'engine_1',
          claudeSessionId: 'claude_1',
          model: 'claude-test'
        }
      },
      { type: 'chat:complete', data: { text: 'done' } },
      { type: 'session:complete', data: {} }
    ]);

    const report = await runEngineConformance(port, createRunInput(), {
      requireEngineSessionId: true
    });

    expect(report.passed).toBe(false);
    expect(report.issues).toEqual([
      expect.objectContaining({
        code: 'MISSING_PROCESS_EXIT'
      })
    ]);
  });
});
