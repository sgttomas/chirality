import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

const mocks = vi.hoisted(() => {
  const handlers = new Map<string, (...args: unknown[]) => Promise<unknown>>();
  return {
    handlers,
    ipcMain: {
      handle: vi.fn((channel: string, handler: (...args: unknown[]) => Promise<unknown>) => {
        handlers.set(channel, handler);
      }),
      removeHandler: vi.fn((channel: string) => {
        handlers.delete(channel);
      })
    }
  };
});

vi.mock('electron', () => ({
  app: {
    getPath: vi.fn((name: string) =>
      name === 'home' ? '/Users/tester' : '/Users/tester/Library/Application Support/Chirality'
    )
  },
  ipcMain: mocks.ipcMain
}));

// Only the manager is replaced. The package's env-name and default-label
// constants stay real, so this asserts against the contract the shipped code
// reads rather than against a restatement of it.
vi.mock('@chirality/runtime-cli', async (importOriginal) => ({
  ...(await importOriginal<typeof import('@chirality/runtime-cli')>()),
  LaunchAgentManager: vi.fn()
}));

import { LaunchAgentManager } from '@chirality/runtime-cli';
import {
  RUNTIME_DAEMON_CONTROL_CHANNEL,
  RUNTIME_MODEL_ACTIVATE_CHANNEL,
  RUNTIME_MODEL_STATUS_CHANNEL,
  createDesktopDaemonLifecycle,
  registerRuntimeControlHandlers,
  unregisterRuntimeControlHandlers
} from '../../../electron/runtime-control-ipc';

function getHandler(channel: string): (...args: unknown[]) => Promise<unknown> {
  const handler = mocks.handlers.get(channel);
  if (!handler) throw new Error(`Missing handler for ${channel}`);
  return handler;
}

function residency(managedModelId?: string) {
  return {
    phase: managedModelId ? ('READY' as const) : ('NO_MODEL' as const),
    ...(managedModelId ? { managedModelId } : {}),
    activeTurns: 0,
    acceptingLocalTurns: Boolean(managedModelId),
    models: [
      {
        id: 'Qwen-local-exact',
        kind: 'llm' as const,
        loaded: Boolean(managedModelId),
        loading: false
      }
    ]
  };
}

const lifecycle = {
  install: vi.fn<() => Promise<void>>(),
  start: vi.fn<() => Promise<void>>(),
  stop: vi.fn<() => Promise<void>>(),
  status: vi.fn(),
  uninstall: vi.fn<() => Promise<void>>()
};

const client = {
  daemonStatus: vi.fn(),
  listModels: vi.fn(),
  activateModel: vi.fn()
};

const trustedEvent = {
  senderFrame: { url: 'http://127.0.0.1:3000/settings' }
};

const dependencies = {
  lifecycle,
  client,
  daemonExecutable:
    '/Applications/Chirality.app/Contents/Library/LoginItems/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service',
  packaged: true,
  rendererOrigin: 'http://127.0.0.1:3000'
};

beforeEach(() => {
  mocks.handlers.clear();
  vi.clearAllMocks();
  lifecycle.install.mockResolvedValue();
  lifecycle.start.mockResolvedValue();
  lifecycle.stop.mockResolvedValue();
  lifecycle.uninstall.mockResolvedValue();
  lifecycle.status.mockResolvedValue({ installed: true, loaded: true });
  client.daemonStatus.mockResolvedValue({
    apiVersion: 'v1',
    status: 'ok',
    daemonId: 'daemon-test',
    pid: 4242,
    startedAt: '2026-07-22T00:00:00.000Z',
    socketPath: '/private/runtime.sock',
    engines: []
  });
  client.listModels.mockResolvedValue(residency());
  client.activateModel.mockResolvedValue(residency('Qwen-local-exact'));
});

describe('electron/runtime-control-ipc', () => {
  it('registers only fixed daemon and model control channels', () => {
    registerRuntimeControlHandlers(dependencies);

    expect(mocks.handlers.has(RUNTIME_DAEMON_CONTROL_CHANNEL)).toBe(true);
    expect(mocks.handlers.has(RUNTIME_MODEL_STATUS_CHANNEL)).toBe(true);
    expect(mocks.handlers.has(RUNTIME_MODEL_ACTIVATE_CHANNEL)).toBe(true);
    expect(mocks.handlers.size).toBe(3);
  });

  it('does not let the renderer choose an executable or invoke an unknown daemon action', async () => {
    registerRuntimeControlHandlers(dependencies);
    const handler = getHandler(RUNTIME_DAEMON_CONTROL_CHANNEL);

    await expect(handler(trustedEvent, 'arbitrary-command', '/tmp/evil')).resolves.toEqual({
      ok: false,
      error: 'Unsupported runtime daemon action'
    });
    expect(lifecycle.install).not.toHaveBeenCalled();

    await handler(trustedEvent, 'install');
    expect(lifecycle.install).toHaveBeenCalledWith(
      '/Applications/Chirality.app/Contents/Library/LoginItems/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service'
    );
  });

  it('rejects development-build installation while retaining read-only status', async () => {
    registerRuntimeControlHandlers({
      lifecycle,
      client,
      daemonExecutable: '/Applications/Electron.app/Contents/MacOS/Electron',
      packaged: false,
      rendererOrigin: 'http://127.0.0.1:3000'
    });
    const handler = getHandler(RUNTIME_DAEMON_CONTROL_CHANNEL);

    await expect(handler(trustedEvent, 'install')).resolves.toMatchObject({
      ok: false,
      error: expect.stringContaining('packaged Chirality')
    });
    expect(lifecycle.install).not.toHaveBeenCalled();

    await expect(handler(trustedEvent, 'status')).resolves.toMatchObject({
      ok: true,
      launchAgent: { installed: true, loaded: true },
      daemon: { running: true, pid: 4242 }
    });
  });

  it('reports installed state without exposing launchctl detail or failing on a stopped daemon', async () => {
    lifecycle.status.mockResolvedValue({
      installed: true,
      loaded: false,
      detail: 'sensitive launchctl environment'
    });
    client.daemonStatus.mockRejectedValue(new Error('socket contains private path'));
    registerRuntimeControlHandlers(dependencies);

    await expect(
      getHandler(RUNTIME_DAEMON_CONTROL_CHANNEL)(trustedEvent, 'status')
    ).resolves.toEqual({
      ok: true,
      launchAgent: { installed: true, loaded: false },
      daemon: { running: false }
    });
  });

  it('requires a model reported by oMLX and supplies a main-process approval reference', async () => {
    registerRuntimeControlHandlers(dependencies);
    const handler = getHandler(RUNTIME_MODEL_ACTIVATE_CHANNEL);

    await expect(handler(trustedEvent, ' unknown ')).resolves.toEqual({
      ok: false,
      error: 'An exact valid oMLX model ID is required'
    });
    await expect(handler(trustedEvent, 'not-reported')).resolves.toEqual({
      ok: false,
      error: 'The selected model is not reported by oMLX'
    });
    expect(client.activateModel).not.toHaveBeenCalled();

    await expect(handler(trustedEvent, 'Qwen-local-exact')).resolves.toMatchObject({
      ok: true,
      residency: { managedModelId: 'Qwen-local-exact' }
    });
    expect(client.activateModel).toHaveBeenCalledWith(
      'Qwen-local-exact',
      'desktop-explicit-model-activation'
    );
  });

  it('unregisters every runtime control handler', () => {
    registerRuntimeControlHandlers(dependencies);
    unregisterRuntimeControlHandlers();

    expect(mocks.handlers.size).toBe(0);
    expect(mocks.ipcMain.removeHandler).toHaveBeenCalledWith(RUNTIME_DAEMON_CONTROL_CHANNEL);
    expect(mocks.ipcMain.removeHandler).toHaveBeenCalledWith(RUNTIME_MODEL_STATUS_CHANNEL);
    expect(mocks.ipcMain.removeHandler).toHaveBeenCalledWith(RUNTIME_MODEL_ACTIVATE_CHANNEL);
  });

  it('rejects runtime controls from a renderer outside the configured origin', async () => {
    registerRuntimeControlHandlers(dependencies);

    await expect(
      getHandler(RUNTIME_DAEMON_CONTROL_CHANNEL)(
        { senderFrame: { url: 'https://attacker.example/' } },
        'start'
      )
    ).resolves.toEqual({
      ok: false,
      error: 'Runtime control request was denied'
    });
    await expect(
      getHandler(RUNTIME_MODEL_STATUS_CHANNEL)({
        senderFrame: { url: 'https://attacker.example/' }
      })
    ).resolves.toEqual({
      ok: false,
      error: 'Runtime control request was denied'
    });
    expect(lifecycle.start).not.toHaveBeenCalled();
    expect(client.listModels).not.toHaveBeenCalled();
  });
});

describe('createDesktopDaemonLifecycle', () => {
  const previousLabel = process.env.CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL;

  afterEach(() => {
    if (previousLabel === undefined) {
      delete process.env.CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL;
    } else {
      process.env.CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL = previousLabel;
    }
  });

  it('pins the whole posture, not just the runtime directory, into the LaunchAgent', () => {
    delete process.env.CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL;

    createDesktopDaemonLifecycle();

    expect(LaunchAgentManager).toHaveBeenCalledOnce();
    const [paths, runner, userId, options] = vi.mocked(LaunchAgentManager).mock.calls[0] ?? [];
    expect(paths).toEqual({
      launchAgentsDirectory: '/Users/tester/Library/LaunchAgents',
      runtimeDirectory: '/Users/tester/Library/Application Support/Chirality/runtime'
    });
    // The generic package keeps its own defaults for the runner and uid.
    expect(runner).toBeUndefined();
    expect(userId).toBeUndefined();
    // 'always', not the crash-only default: the observed daemon termination was a
    // clean exit(0), which a SuccessfulExit=false semaphore never restarts. With
    // the quit veto gone this restart contract is the whole of the stay-dead fix.
    // The label is pinned into the job environment too, so a GUI the daemon spawns
    // addresses the same job — the mechanism that keeps an isolated run isolated.
    expect(options).toEqual({
      label: 'com.chirality.runtime',
      keepAlive: 'always',
      runAtLoad: true,
      environmentVariables: {
        CHIRALITY_USER_DATA: '/Users/tester/Library/Application Support/Chirality',
        CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL: 'com.chirality.runtime',
        CHIRALITY_RUNTIME_KEEP_ALIVE: 'always'
      }
    });
  });

  it('honors a label override so an isolated run cannot touch the real agent', () => {
    process.env.CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL = 'com.chirality.runtime.tranchetest';

    createDesktopDaemonLifecycle();

    const options = vi.mocked(LaunchAgentManager).mock.calls[0]?.[3];
    expect(options).toMatchObject({
      label: 'com.chirality.runtime.tranchetest',
      environmentVariables: {
        CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL: 'com.chirality.runtime.tranchetest'
      }
    });
  });

  it('falls back to the package default label when the override is blank', () => {
    process.env.CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL = '   ';

    createDesktopDaemonLifecycle();

    expect(vi.mocked(LaunchAgentManager).mock.calls[0]?.[3]).toMatchObject({
      label: 'com.chirality.runtime'
    });
  });
});
