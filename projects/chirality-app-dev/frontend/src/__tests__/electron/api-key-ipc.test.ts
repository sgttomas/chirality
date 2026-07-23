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
    credentialStatus: vi.fn<(providerId: 'anthropic' | 'omlx') => Promise<{ configured: boolean }>>(),
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
  mocks.credentialStatus.mockResolvedValue({ configured: false });
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

  it('returns status source precedence as ui > env > none', async () => {
    registerApiKeyHandlers(credentialClient);
    const handler = getHandler(API_KEY_STATUS_CHANNEL);

    mocks.credentialStatus.mockResolvedValue({ configured: true });
    process.env.ANTHROPIC_API_KEY = 'env-key';
    await expect(handler({})).resolves.toEqual({
      hasKey: true,
      encryptionAvailable: true,
      source: 'env'
    });

    mocks.credentialStatus.mockResolvedValue({ configured: true });
    await expect(handler({})).resolves.toEqual({
      hasKey: true,
      encryptionAvailable: true,
      source: 'env'
    });

    delete process.env.ANTHROPIC_API_KEY;
    mocks.credentialStatus.mockResolvedValue({ configured: false });
    await expect(handler({})).resolves.toEqual({
      hasKey: false,
      encryptionAvailable: true,
      source: 'none'
    });
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

    mocks.credentialStatus.mockResolvedValueOnce({ configured: true });
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

  it('uses only CHIRALITY_OMLX_API_KEY for oMLX status and rejects unknown providers', async () => {
    registerApiKeyHandlers(credentialClient);
    process.env.ANTHROPIC_API_KEY = 'anthropic-only';

    await expect(getHandler(PROVIDER_API_KEY_STATUS_CHANNEL)({}, 'omlx')).resolves.toEqual({
      hasKey: false,
      encryptionAvailable: true,
      source: 'none'
    });

    process.env.CHIRALITY_OMLX_API_KEY = 'omlx-env';
    mocks.credentialStatus.mockResolvedValue({ configured: true });
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
