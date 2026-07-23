import { afterEach, describe, expect, it, vi } from 'vitest';
import type {
  DaemonHarnessPort,
  RunningDaemonHarnessTurn
} from '../../../lib/runtime-client/daemon-harness-port';
import {
  installDaemonHarnessPort,
  resetDaemonHarnessPortForTests
} from '../../../lib/runtime-client/daemon-harness-port';
import * as createRoute from '../../../app/api/harness/session/create/route';
import * as turnRoute from '../../../app/api/harness/turn/route';

function unimplemented(): never {
  throw new Error('Unexpected fake daemon-port method');
}

function daemonPort(
  overrides: Partial<DaemonHarnessPort>
): DaemonHarnessPort {
  return {
    createSession: unimplemented,
    listSessions: unimplemented,
    getSession: unimplemented,
    deleteSession: unimplemented,
    bootSession: unimplemented,
    replaySession: unimplemented,
    turn: unimplemented,
    interrupt: unimplemented,
    decidePermission: unimplemented,
    listAgents: unimplemented,
    scaffold: unimplemented,
    ...overrides
  };
}

afterEach(() => {
  resetDaemonHarnessPortForTests();
  vi.restoreAllMocks();
});

describe('Desktop daemon harness proxy boundary', () => {
  it('fails closed when the Desktop composition root has not installed a daemon client', async () => {
    const response = await createRoute.POST(
      new Request('http://localhost/api/harness/session/create', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ projectRoot: '/registered/project' })
      })
    );

    expect(response.status).toBe(503);
    await expect(response.json()).resolves.toMatchObject({
      error: {
        type: 'ENGINE_UNAVAILABLE',
        message: 'Chirality runtime daemon client is not configured'
      }
    });
  });

  it('forwards the legacy session-create shape and request cancellation signal', async () => {
    const session = {
      sessionId: 'sess_proxy_1',
      projectRoot: '/registered/project',
      persona: 'WORKING_ITEMS',
      mode: 'direct',
      createdAt: '2026-07-22T00:00:00.000Z',
      updatedAt: '2026-07-22T00:00:00.000Z'
    };
    const createSession = vi.fn(async () => ({ session }));
    installDaemonHarnessPort(daemonPort({ createSession }));
    const abortController = new AbortController();

    const response = await createRoute.POST(
      new Request('http://localhost/api/harness/session/create', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          projectRoot: '/registered/project',
          persona: 'WORKING_ITEMS',
          mode: 'direct'
        }),
        signal: abortController.signal
      })
    );

    expect(response.status).toBe(200);
    await expect(response.json()).resolves.toEqual({ session });
    expect(createSession).toHaveBeenCalledWith(
      {
        projectRoot: '/registered/project',
        persona: 'WORKING_ITEMS',
        mode: 'direct'
      },
      { signal: expect.any(AbortSignal) }
    );
  });

  it('preserves legacy SSE event names and propagates reader cancellation to the daemon turn', async () => {
    let release: (() => void) | undefined;
    const cancelled = vi.fn(async () => {
      release?.();
    });
    const runningTurn: RunningDaemonHarnessTurn = {
      events: (async function* () {
        yield {
          type: 'chat:delta' as const,
          data: { text: 'daemon text' }
        };
        await new Promise<void>((resolve) => {
          release = resolve;
        });
      })(),
      cancel: cancelled
    };
    const turn = vi.fn(async () => runningTurn);
    installDaemonHarnessPort(daemonPort({ turn }));

    const response = await turnRoute.POST(
      new Request('http://localhost/api/harness/turn', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          sessionId: 'sess_proxy_1',
          message: 'hello daemon'
        })
      })
    );
    const reader = response.body?.getReader();
    const first = await reader?.read();

    expect(response.headers.get('content-type')).toContain('text/event-stream');
    expect(new TextDecoder().decode(first?.value)).toBe(
      'event: chat:delta\ndata: {"text":"daemon text"}\n\n'
    );

    await reader?.cancel();
    expect(cancelled).toHaveBeenCalledOnce();
    expect(turn).toHaveBeenCalledWith(
      { sessionId: 'sess_proxy_1', message: 'hello daemon' },
      { signal: expect.any(AbortSignal) }
    );
  });
});
