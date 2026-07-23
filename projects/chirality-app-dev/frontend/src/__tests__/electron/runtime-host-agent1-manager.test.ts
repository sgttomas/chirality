import { describe, expect, it, vi } from 'vitest';

vi.mock('electron', () => ({
  app: {
    getPath: vi.fn(() => '/tmp/chirality-runtime-host-test'),
    isPackaged: false
  },
  safeStorage: {
    isEncryptionAvailable: vi.fn(() => false)
  }
}));

import type { RuntimeSessionRecord, UIEvent } from '@chirality/runtime-contracts';
import type { Agent1ManagerHooks } from '@chirality/runtime-core';
import { EngineBackedAgent1Manager } from '../../../electron/runtime-host';

const session: RuntimeSessionRecord = {
  schemaVersion: 'chirality.session/v2',
  projectId: 'app-dev',
  projectRoot: '/tmp/project',
  sessionId: 'manager-session',
  persona: 'WORKING_ITEMS',
  mode: 'direct',
  role: 'agent1',
  engineSelection: {
    adapterId: 'stub',
    providerId: 'stub',
    model: 'stub'
  },
  status: 'idle',
  createdAt: '2026-07-22T00:00:00.000Z',
  updatedAt: '2026-07-22T00:00:00.000Z'
};

function harnessTerminal(
  type: 'turn.completed' | 'turn.failed' | 'turn.cancelled' | 'turn.interrupted'
): UIEvent {
  return {
    type: 'harness:event',
    data: {
      schemaVersion: 1,
      eventId: `event-${type}`,
      sessionId: session.sessionId,
      turnId: 'turn-1',
      timestamp: '2026-07-22T00:00:01.000Z',
      type,
      data: {}
    }
  };
}

function events(items: readonly UIEvent[]): AsyncIterable<UIEvent> {
  return {
    async *[Symbol.asyncIterator]() {
      yield* items;
    }
  };
}

async function consume(iterable: AsyncIterable<UIEvent>): Promise<UIEvent[]> {
  const received: UIEvent[] = [];
  for await (const event of iterable) received.push(event);
  return received;
}

function hooks(): Agent1ManagerHooks & {
  delegate: ReturnType<typeof vi.fn>;
  review: ReturnType<typeof vi.fn>;
} {
  return {
    delegate: vi.fn(async () => ({
      childSessionId: 'child-session',
      returnText: 'bounded evidence',
      model: 'Qwen-local',
      residencyEpoch: 'epoch-1'
    })),
    review: vi.fn(async () => undefined)
  };
}

describe('EngineBackedAgent1Manager terminal enforcement', () => {
  it('turns manager preparation into a direct, tool-mandatory child brief', async () => {
    let runNumber = 0;
    const turns = {
      run: vi.fn(() => {
        runNumber += 1;
        return runNumber === 1
          ? events([
              { type: 'chat:complete', data: { text: 'Check the configured project.' } },
              harnessTerminal('turn.completed'),
              { type: 'process:exit', data: { exitCode: 0 } }
            ])
          : events([
              { type: 'chat:complete', data: { text: 'ACCEPT: grounded return.' } },
              harnessTerminal('turn.completed'),
              { type: 'process:exit', data: { exitCode: 0 } }
            ]);
      }),
      interrupt: vi.fn(async () => undefined)
    };
    const manager = new EngineBackedAgent1Manager(turns as never);
    const managerHooks = hooks();

    await consume(
      manager.execute(
        session,
        {
          brief: 'Report the project schema version.',
          approvalReference: 'approval-direct',
          localModel: 'Qwen-local',
          readOnlyTool: { name: 'read_file', relativePath: 'chirality.project.json' }
        },
        managerHooks,
        new AbortController().signal
      )
    );

    expect(managerHooks.delegate).toHaveBeenCalledOnce();
    expect(managerHooks.delegate.mock.calls[0]?.[0].sealedBrief).toContain(
      'Call the available read_file tool exactly once'
    );
    expect(managerHooks.delegate.mock.calls[0]?.[0].sealedBrief).toContain(
      'bound to chirality.project.json'
    );
    expect(managerHooks.delegate.mock.calls[0]?.[0].sealedBrief).toContain(
      'Original request:\nReport the project schema version.'
    );
    expect(managerHooks.review).toHaveBeenCalledWith(
      expect.objectContaining({ decision: 'accepted' })
    );
  });

  it('does not delegate after a failed manager preparation turn', async () => {
    const turns = {
      run: vi.fn(() =>
        events([
          { type: 'chat:complete', data: { text: 'sealed brief' } },
          harnessTerminal('turn.failed'),
          {
            type: 'turn:error',
            data: {
              phase: 'mid-stream',
              errorType: 'SDK_FAILURE',
              message: 'preparation failed',
              status: 502,
              severity: 'error',
              fatal: true
            }
          },
          {
            type: 'process:exit',
            data: { exitCode: 1, error: 'preparation failed', status: 502 }
          }
        ])
      ),
      interrupt: vi.fn(async () => undefined)
    };
    const manager = new EngineBackedAgent1Manager(turns as never);
    const managerHooks = hooks();

    await expect(
      consume(
        manager.execute(
          session,
          {
            brief: 'Inspect the fixture',
            approvalReference: 'approval-1',
            localModel: 'Qwen-local',
            readOnlyTool: { name: 'read_file', relativePath: 'fixture.txt' }
          },
          managerHooks,
          new AbortController().signal
        )
      )
    ).rejects.toMatchObject({
      code: 'ENGINE_UNAVAILABLE',
      message: 'preparation failed'
    });
    expect(managerHooks.delegate).not.toHaveBeenCalled();
    expect(managerHooks.review).not.toHaveBeenCalled();
  });

  it('does not accept a child after the manager review turn fails', async () => {
    let runNumber = 0;
    const turns = {
      run: vi.fn(() => {
        runNumber += 1;
        return runNumber === 1
          ? events([
              { type: 'chat:complete', data: { text: 'sealed brief' } },
              harnessTerminal('turn.completed'),
              { type: 'process:exit', data: { exitCode: 0 } }
            ])
          : events([
              { type: 'chat:complete', data: { text: 'ACCEPT without evidence' } },
              harnessTerminal('turn.failed'),
              { type: 'process:exit', data: { exitCode: 1, error: 'review failed' } }
            ]);
      }),
      interrupt: vi.fn(async () => undefined)
    };
    const manager = new EngineBackedAgent1Manager(turns as never);
    const managerHooks = hooks();

    await expect(
      consume(
        manager.execute(
          session,
          {
            brief: 'Inspect the fixture',
            approvalReference: 'approval-2',
            localModel: 'Qwen-local',
            readOnlyTool: { name: 'read_file', relativePath: 'fixture.txt' }
          },
          managerHooks,
          new AbortController().signal
        )
      )
    ).rejects.toMatchObject({
      code: 'ENGINE_UNAVAILABLE',
      message: 'review failed'
    });
    expect(managerHooks.delegate).toHaveBeenCalledOnce();
    expect(managerHooks.review).not.toHaveBeenCalled();
  });

  it('rejects a manager turn missing process:exit', async () => {
    const turns = {
      run: vi.fn(() =>
        events([
          { type: 'chat:complete', data: { text: 'partial response' } },
          harnessTerminal('turn.completed')
        ])
      ),
      interrupt: vi.fn(async () => undefined)
    };
    const manager = new EngineBackedAgent1Manager(turns as never);
    const managerHooks = hooks();

    await expect(
      consume(
        manager.execute(
          session,
          {
            brief: 'Direct manager request',
            approvalReference: 'approval-3'
          },
          managerHooks,
          new AbortController().signal
        )
      )
    ).rejects.toMatchObject({
      code: 'ENGINE_UNAVAILABLE',
      message: expect.stringContaining('without process:exit')
    });
  });

  it('propagates interruption instead of delegating', async () => {
    const turns = {
      run: vi.fn(() =>
        events([
          harnessTerminal('turn.interrupted'),
          {
            type: 'process:exit',
            data: { exitCode: 130, interrupted: true }
          }
        ])
      ),
      interrupt: vi.fn(async () => undefined)
    };
    const manager = new EngineBackedAgent1Manager(turns as never);
    const managerHooks = hooks();

    await expect(
      consume(
        manager.execute(
          session,
          {
            brief: 'Inspect the fixture',
            approvalReference: 'approval-4',
            localModel: 'Qwen-local',
            readOnlyTool: { name: 'read_file', relativePath: 'fixture.txt' }
          },
          managerHooks,
          new AbortController().signal
        )
      )
    ).rejects.toMatchObject({ code: 'INTERRUPTED' });
    expect(managerHooks.delegate).not.toHaveBeenCalled();
  });
});
