import { describe, expect, it, vi } from 'vitest';
import { TurnEngine } from '../../lib/harness/turn-engine';
import type {
  HarnessOpts,
  IAgentSdkManager,
  IAttachmentResolver,
  IPersonaManager,
  ISessionManager,
  ContentBlock,
  ResolvedOpts,
  SessionRecord,
  UIEvent
} from '@chirality/harness-contract/types';

const session: SessionRecord = {
  sessionId: 'sess_turn_engine',
  projectRoot: '/tmp/project',
  persona: 'WORKING_ITEMS',
  mode: 'direct',
  createdAt: '2026-06-13T00:00:00.000Z',
  updatedAt: '2026-06-13T00:00:00.000Z'
};

const resolvedOpts: ResolvedOpts = {
  model: 'claude-test',
  tools: [],
  maxTurns: 2,
  persona: 'WORKING_ITEMS',
  mode: 'direct'
};

async function collectEvents(events: AsyncIterable<UIEvent>): Promise<UIEvent[]> {
  const collected: UIEvent[] = [];
  for await (const event of events) {
    collected.push(event);
  }
  return collected;
}

function createSessionManager(): ISessionManager {
  return {
    create: vi.fn(async () => session),
    resume: vi.fn(async () => session),
    getById: vi.fn(async () => session),
    save: vi.fn(async (_sessionId: string, updates: Partial<SessionRecord>) => ({
      ...session,
      ...updates,
      updatedAt: '2026-06-13T00:00:01.000Z'
    })),
    list: vi.fn(async () => [session]),
    delete: vi.fn(async () => undefined)
  };
}

function createPersonaManager(): IPersonaManager {
  return {
    buildSystemPrompt: vi.fn(async () => 'system prompt'),
    getBootFingerprint: vi.fn(() => 'boot-fingerprint')
  };
}

function createAttachmentResolver(): IAttachmentResolver {
  return {
    resolveAttachmentsToContentBlocks: vi.fn(async (message: string) => {
      const contentBlocks: ContentBlock[] = message.trim() ? [{ type: 'text', text: message }] : [];
      return {
        contentBlocks,
        errors: []
      };
    })
  };
}

function createAgentSdkManager(startTurnImpl?: IAgentSdkManager['startTurn']): IAgentSdkManager {
  const defaultStartTurn: IAgentSdkManager['startTurn'] = async function* (_session, message, opts) {
    const initEvent: UIEvent = {
      type: 'session:init',
      data: {
        engineSessionId: 'engine_1',
        claudeSessionId: 'claude_1',
        model: opts.model
      }
    };
    yield initEvent;
    const completeEvent: UIEvent = {
      type: 'chat:complete',
      data: {
        text: message
      }
    };
    yield completeEvent;
    const sessionCompleteEvent: UIEvent = {
      type: 'session:complete',
      data: {}
    };
    yield sessionCompleteEvent;
    const processExitEvent: UIEvent = {
      type: 'process:exit',
      data: {
        exitCode: 0
      }
    };
    yield processExitEvent;
  };

  return {
    startTurn: vi.fn(startTurnImpl ?? defaultStartTurn),
    interrupt: vi.fn(async (_sessionId: string) => undefined)
  };
}

function createTurnEngine(
  startTurnImpl?: IAgentSdkManager['startTurn'],
  options?: {
    providerMode?: 'stub' | 'anthropic' | 'agentSdk';
  }
): {
  engine: TurnEngine;
  sessionManager: ISessionManager;
  personaManager: IPersonaManager;
  attachmentResolver: IAttachmentResolver;
  agentSdkManager: IAgentSdkManager;
} {
  const sessionManager = createSessionManager();
  const personaManager = createPersonaManager();
  const attachmentResolver = createAttachmentResolver();
  const agentSdkManager = createAgentSdkManager(startTurnImpl);
  const engine = new TurnEngine({
    sessionManager,
    personaManager,
    attachmentResolver,
    agentSdkManager,
    resolveProviderMode: () => options?.providerMode ?? 'stub',
    hasUiApiKey: () => options?.providerMode === 'agentSdk',
    resolveRuntimeOptions: async (_session: SessionRecord, opts?: HarnessOpts) => ({
      ...resolvedOpts,
      model: opts?.model ?? resolvedOpts.model,
      tools: opts?.tools ?? resolvedOpts.tools,
      mode: opts?.mode ?? resolvedOpts.mode
    }),
    evaluateSubagentGovernance: async () => ({
      allowed: false,
      gate: 'ENVIRONMENT',
      reason: 'subagents disabled',
      evaluationMs: 0,
      allowlistedSubagents: [],
      delegatedSubagents: []
    })
  });

  return {
    engine,
    sessionManager,
    personaManager,
    attachmentResolver,
    agentSdkManager
  };
}

describe('TurnEngine', () => {
  it('runs the turn lifecycle without HTTP and persists engine session metadata', async () => {
    const { engine, sessionManager, personaManager, attachmentResolver, agentSdkManager } =
      createTurnEngine();

    const runningTurn = await engine.runTurn({
      sessionId: session.sessionId,
      message: 'hello from engine',
      opts: { model: 'claude-engine-test' }
    });
    const events = await collectEvents(runningTurn.events);

    expect(events.map((event) => event.type)).toEqual([
      'session:init',
      'chat:complete',
      'session:complete',
      'process:exit'
    ]);
    expect(personaManager.buildSystemPrompt).toHaveBeenCalledWith(
      session.projectRoot,
      'WORKING_ITEMS',
      'direct',
      []
    );
    expect(attachmentResolver.resolveAttachmentsToContentBlocks).toHaveBeenCalledWith(
      'hello from engine',
      []
    );
    expect(agentSdkManager.startTurn).toHaveBeenCalledWith(
      session,
      'hello from engine',
      expect.objectContaining({
        model: 'claude-engine-test',
        delegatedSubagents: []
      }),
      undefined
    );
    expect(sessionManager.save).toHaveBeenCalledWith(
      session.sessionId,
      expect.objectContaining({
        engineSessionId: 'engine_1',
        claudeSessionId: 'claude_1',
        model: 'claude-engine-test'
      })
    );
  });

  it('owns same-session turn locking outside the route', async () => {
    const { engine } = createTurnEngine();

    const runningTurn = await engine.runTurn({
      sessionId: session.sessionId,
      message: 'leave the stream unconsumed'
    });

    await expect(
      engine.runTurn({
        sessionId: session.sessionId,
        message: 'overlap'
      })
    ).rejects.toMatchObject({
      type: 'TURN_IN_PROGRESS',
      status: 409
    });

    await runningTurn.cancel();
    const recoveryTurn = await engine.runTurn({
      sessionId: session.sessionId,
      message: 'after cancel'
    });
    await recoveryTurn.cancel();
  });

  it('rejects unknown agentSdk tools before starting the adapter stream', async () => {
    const { engine, agentSdkManager } = createTurnEngine(undefined, {
      providerMode: 'agentSdk'
    });

    await expect(
      engine.runTurn({
        sessionId: session.sessionId,
        message: 'hello',
        opts: {
          tools: ['read', 'mystery-tool']
        }
      })
    ).rejects.toMatchObject({
      type: 'INVALID_REQUEST',
      status: 400,
      message: expect.stringContaining('Unknown harness tool(s): mystery-tool')
    });

    expect(agentSdkManager.startTurn).not.toHaveBeenCalled();
  });
});
