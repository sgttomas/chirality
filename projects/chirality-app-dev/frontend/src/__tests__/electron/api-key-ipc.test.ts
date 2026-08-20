import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

const mocks = vi.hoisted(() => {
  const handlers = new Map<string, (...args: unknown[]) => Promise<unknown>>();
  const ipcMain = {
    handle: vi.fn((channel: string, handler: (...args: unknown[]) => Promise<unknown>) => {
      handlers.set(channel, handler);
    }),
    removeHandler: vi.fn((channel: string) => {
      handlers.delete(channel);
    })
  };

  return {
    handlers,
    ipcMain,
    isProviderCredentialId: vi.fn((value: unknown) => value === 'anthropic' || value === 'omlx'),
    credentialStatus: vi.fn<(providerId: 'anthropic' | 'omlx') => Promise<unknown>>(),
    removeCredential: vi.fn<(providerId: 'anthropic' | 'omlx') => Promise<{ configured: boolean }>>(),
    storeCredential: vi.fn<
      (providerId: 'anthropic' | 'omlx', key: string) => Promise<{ configured: boolean }>
    >()
  };
});

vi.mock('electron', () => ({
  ipcMain: mocks.ipcMain
}));

vi.mock('../../../electron/api-key-storage', () => ({
  isProviderCredentialId: mocks.isProviderCredentialId
}));

import {
  API_KEY_REMOVE_CHANNEL,
  API_KEY_STATUS_CHANNEL,
  API_KEY_STORE_CHANNEL,
  PROVIDER_API_KEY_REMOVE_CHANNEL,
  PROVIDER_API_KEY_STATUS_CHANNEL,
  PROVIDER_API_KEY_STORE_CHANNEL,
  registerApiKeyHandlers,
  unregisterApiKeyHandlers
} from '../../../electron/api-key-ipc';

function getHandler(channel: string): (...args: unknown[]) => Promise<unknown> {
  const handler = mocks.handlers.get(channel);
  if (!handler) {
    throw new Error(`Missing handler for ${channel}`);
  }
  return handler;
}

const credentialClient = {
  credentialStatus: mocks.credentialStatus,
  removeCredential: mocks.removeCredential,
  storeCredential: mocks.storeCredential
};

beforeEach(() => {
  mocks.handlers.clear();
  vi.clearAllMocks();
  mocks.credentialStatus.mockResolvedValue({ configured: false, source: 'none' });
  mocks.removeCredential.mockResolvedValue({ configured: false });
  mocks.storeCredential.mockResolvedValue({ configured: true });
  delete process.env.ANTHROPIC_API_KEY;
  delete process.env.CHIRALITY_ANTHROPIC_API_KEY;
  delete process.env.CHIRALITY_OMLX_API_KEY;
});

afterEach(() => {
  delete process.env.ANTHROPIC_API_KEY;
  delete process.env.CHIRALITY_ANTHROPIC_API_KEY;
  delete process.env.CHIRALITY_OMLX_API_KEY;
});

describe('electron/api-key-ipc', () => {
  it('registers all API key handlers and unregisters previous handlers first', () => {
    registerApiKeyHandlers(credentialClient);

    expect(mocks.ipcMain.removeHandler).toHaveBeenCalledWith(API_KEY_STORE_CHANNEL);
    expect(mocks.ipcMain.removeHandler).toHaveBeenCalledWith(API_KEY_REMOVE_CHANNEL);
    expect(mocks.ipcMain.removeHandler).toHaveBeenCalledWith(API_KEY_STATUS_CHANNEL);
    expect(mocks.ipcMain.removeHandler).toHaveBeenCalledWith(PROVIDER_API_KEY_STORE_CHANNEL);
    expect(mocks.ipcMain.removeHandler).toHaveBeenCalledWith(PROVIDER_API_KEY_REMOVE_CHANNEL);
    expect(mocks.ipcMain.removeHandler).toHaveBeenCalledWith(PROVIDER_API_KEY_STATUS_CHANNEL);
    expect(mocks.handlers.has(API_KEY_STORE_CHANNEL)).toBe(true);
    expect(mocks.handlers.has(API_KEY_REMOVE_CHANNEL)).toBe(true);
    expect(mocks.handlers.has(API_KEY_STATUS_CHANNEL)).toBe(true);
    expect(mocks.handlers.has(PROVIDER_API_KEY_STORE_CHANNEL)).toBe(true);
    expect(mocks.handlers.has(PROVIDER_API_KEY_REMOVE_CHANNEL)).toBe(true);
    expect(mocks.handlers.has(PROVIDER_API_KEY_STATUS_CHANNEL)).toBe(true);
  });

  it('trims and stores key material through the store channel', async () => {
    registerApiKeyHandlers(credentialClient);
    const handler = getHandler(API_KEY_STORE_CHANNEL);

    const result = await handler({}, '  sk-ant-test-key  ');

    expect(mocks.storeCredential).toHaveBeenCalledWith('anthropic', 'sk-ant-test-key');
    expect(result).toEqual({ ok: true });
  });

  it('rejects empty values on the store channel', async () => {
    registerApiKeyHandlers(credentialClient);
    const handler = getHandler(API_KEY_STORE_CHANNEL);

    const result = await handler({}, '   ');

    expect(mocks.storeCredential).not.toHaveBeenCalled();
    expect(result).toEqual({ ok: false, error: 'Key must be a non-empty string' });
  });

  it('consumes the daemon-owned source when UI and environment credentials coexist', async () => {
    registerApiKeyHandlers(credentialClient);
    const handler = getHandler(API_KEY_STATUS_CHANNEL);

    process.env.ANTHROPIC_API_KEY = 'canonical-environment-key';
    process.env.CHIRALITY_ANTHROPIC_API_KEY = 'compatibility-environment-key';
    mocks.credentialStatus.mockResolvedValue({ configured: true, source: 'ui' });

    await expect(handler({})).resolves.toEqual({
      hasKey: true,
      encryptionAvailable: true,
      source: 'ui'
    });
  });

  it.each([
    {
      caseName: 'canonical environment credential',
      environment: { ANTHROPIC_API_KEY: 'canonical-environment-key' },
      status: { configured: true, source: 'env' }
    },
    {
      caseName: 'compatibility-alias environment credential',
      environment: { CHIRALITY_ANTHROPIC_API_KEY: 'compatibility-environment-key' },
      status: { configured: true, source: 'env' }
    },
    {
      caseName: 'no credential',
      environment: {},
      status: { configured: false, source: 'none' }
    }
  ])('reports $caseName from the daemon status', async ({ environment, status }) => {
    registerApiKeyHandlers(credentialClient);
    const handler = getHandler(API_KEY_STATUS_CHANNEL);
    Object.assign(process.env, environment);
    mocks.credentialStatus.mockResolvedValue(status);

    await expect(handler({})).resolves.toEqual({
      hasKey: status.configured,
      encryptionAvailable: true,
      source: status.source
    });
  });

  it.each([
    { configured: true },
    { configured: true, source: 'other' },
    { configured: true, source: 'none' },
    { configured: false, source: 'ui' }
  ])('fails closed for an invalid daemon status %#', async (status) => {
    registerApiKeyHandlers(credentialClient);
    const handler = getHandler(API_KEY_STATUS_CHANNEL);
    process.env.ANTHROPIC_API_KEY = 'must-not-be-inferred-or-disclosed';
    mocks.credentialStatus.mockResolvedValue({
      ...status,
      credential: 'must-not-be-returned'
    });

    const result = await handler({});

    expect(result).toEqual({
      hasKey: false,
      encryptionAvailable: false,
      source: 'none',
      error: 'Runtime daemon returned an invalid credential status'
    });
    expect(JSON.stringify(result)).not.toContain('must-not');
  });

  it('handles remove channel failures without throwing', async () => {
    registerApiKeyHandlers(credentialClient);
    const handler = getHandler(API_KEY_REMOVE_CHANNEL);
    mocks.removeCredential.mockRejectedValue(new Error('remove-failed'));

    await expect(handler({})).resolves.toEqual({ ok: false, error: 'remove-failed' });
  });

  it('stores, reports, and removes an isolated oMLX credential', async () => {
    registerApiKeyHandlers(credentialClient);

    await expect(getHandler(PROVIDER_API_KEY_STORE_CHANNEL)({}, 'omlx', '  local-secret  '))
      .resolves.toEqual({ ok: true });
    expect(mocks.storeCredential).toHaveBeenCalledWith('omlx', 'local-secret');

    mocks.credentialStatus.mockResolvedValueOnce({ configured: true, source: 'ui' });
    await expect(getHandler(PROVIDER_API_KEY_STATUS_CHANNEL)({}, 'omlx')).resolves.toEqual({
      hasKey: true,
      encryptionAvailable: true,
      source: 'ui'
    });

    await expect(getHandler(PROVIDER_API_KEY_REMOVE_CHANNEL)({}, 'omlx')).resolves.toEqual({
      ok: true
    });
    expect(mocks.removeCredential).toHaveBeenCalledWith('omlx');
  });

  it('consumes the daemon-owned oMLX source and rejects unknown providers', async () => {
    registerApiKeyHandlers(credentialClient);
    process.env.ANTHROPIC_API_KEY = 'anthropic-only';
    process.env.CHIRALITY_OMLX_API_KEY = 'omlx-environment-key';

    await expect(getHandler(PROVIDER_API_KEY_STATUS_CHANNEL)({}, 'omlx')).resolves.toEqual({
      hasKey: false,
      encryptionAvailable: true,
      source: 'none'
    });

    mocks.credentialStatus.mockResolvedValue({ configured: true, source: 'env' });
    await expect(getHandler(PROVIDER_API_KEY_STATUS_CHANNEL)({}, 'omlx')).resolves.toEqual({
      hasKey: true,
      encryptionAvailable: true,
      source: 'env'
    });

    await expect(getHandler(PROVIDER_API_KEY_STATUS_CHANNEL)({}, 'other')).resolves.toEqual({
      ok: false,
      error: 'Unsupported credential provider'
    });
  });

  // A status query used to reject straight into the renderer whenever the daemon
  // was down: the client throws ENOENT on the operator token, which surfaced as an
  // unhandled "Error occurred in handler for ..." on every launch without a
  // running daemon. The state is reported as data instead.
  it('reports an unreachable daemon as a structured status rather than throwing', async () => {
    registerApiKeyHandlers(credentialClient);
    const failure = Object.assign(
      new Error("ENOENT: no such file or directory, open '/runtime/auth/tokens/operator.token'"),
      { code: 'ENOENT' }
    );
    mocks.credentialStatus.mockRejectedValue(failure);

    await expect(getHandler(API_KEY_STATUS_CHANNEL)({})).resolves.toEqual({
      hasKey: false,
      encryptionAvailable: false,
      source: 'none',
      unavailable: true,
      error: failure.message
    });
  });

  it('reports an unreachable daemon on the provider status channel too', async () => {
    registerApiKeyHandlers(credentialClient);
    mocks.credentialStatus.mockRejectedValue(new Error('connect ENOENT control.sock'));

    await expect(
      getHandler(PROVIDER_API_KEY_STATUS_CHANNEL)({}, 'omlx')
    ).resolves.toMatchObject({ unavailable: true, hasKey: false, source: 'none' });
  });

  it('does not mark a real answer as unavailable', async () => {
    registerApiKeyHandlers(credentialClient);
    mocks.credentialStatus.mockResolvedValue({ configured: true, source: 'ui' });

    const result = await getHandler(API_KEY_STATUS_CHANNEL)({});

    expect(result).not.toHaveProperty('unavailable');
    expect(result).toMatchObject({ hasKey: true, encryptionAvailable: true });
  });

  it('still rejects an unsupported provider before consulting the daemon', async () => {
    registerApiKeyHandlers(credentialClient);
    mocks.credentialStatus.mockRejectedValue(new Error('should not be called'));

    await expect(getHandler(PROVIDER_API_KEY_STATUS_CHANNEL)({}, 'nope')).resolves.toEqual({
      ok: false,
      error: 'Unsupported credential provider'
    });
    expect(mocks.credentialStatus).not.toHaveBeenCalled();
  });

  it('unregisters all handlers', () => {
    registerApiKeyHandlers(credentialClient);
    unregisterApiKeyHandlers();

    expect(mocks.ipcMain.removeHandler).toHaveBeenCalledWith(API_KEY_STORE_CHANNEL);
    expect(mocks.ipcMain.removeHandler).toHaveBeenCalledWith(API_KEY_REMOVE_CHANNEL);
    expect(mocks.ipcMain.removeHandler).toHaveBeenCalledWith(API_KEY_STATUS_CHANNEL);
    expect(mocks.ipcMain.removeHandler).toHaveBeenCalledWith(PROVIDER_API_KEY_STORE_CHANNEL);
    expect(mocks.ipcMain.removeHandler).toHaveBeenCalledWith(PROVIDER_API_KEY_REMOVE_CHANNEL);
    expect(mocks.ipcMain.removeHandler).toHaveBeenCalledWith(PROVIDER_API_KEY_STATUS_CHANNEL);
  });
});
