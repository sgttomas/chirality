import { ipcMain } from 'electron';
import { isProviderCredentialId, type ProviderCredentialId } from './api-key-storage';

// Existing Anthropic-only channels remain stable for renderer compatibility.
export const API_KEY_STORE_CHANNEL = 'chirality:api-key-store';
export const API_KEY_REMOVE_CHANNEL = 'chirality:api-key-remove';
export const API_KEY_STATUS_CHANNEL = 'chirality:api-key-status';

export const PROVIDER_API_KEY_STORE_CHANNEL = 'chirality:provider-api-key-store';
export const PROVIDER_API_KEY_REMOVE_CHANNEL = 'chirality:provider-api-key-remove';
export const PROVIDER_API_KEY_STATUS_CHANNEL = 'chirality:provider-api-key-status';

export type ApiKeyStatusResult = {
  hasKey: boolean;
  encryptionAvailable: boolean;
  source: 'ui' | 'env' | 'none';
};

export type ApiKeyStoreResult = {
  ok: boolean;
  error?: string;
};

function hasEnvironmentKey(providerId: ProviderCredentialId): boolean {
  if (providerId === 'anthropic') {
    return Boolean(
      process.env.ANTHROPIC_API_KEY?.trim() || process.env.CHIRALITY_ANTHROPIC_API_KEY?.trim()
    );
  }
  return Boolean(process.env.CHIRALITY_OMLX_API_KEY?.trim());
}

export interface DaemonCredentialClient {
  credentialStatus(providerId: ProviderCredentialId): Promise<{ configured: boolean }>;
  storeCredential(
    providerId: ProviderCredentialId,
    credential: string
  ): Promise<{ configured: boolean }>;
  removeCredential(providerId: ProviderCredentialId): Promise<{ configured: boolean }>;
}

function invalidProviderResult(): ApiKeyStoreResult {
  return { ok: false, error: 'Unsupported credential provider' };
}

export function registerApiKeyHandlers(client: DaemonCredentialClient): void {
  unregisterApiKeyHandlers();

  ipcMain.handle(API_KEY_STORE_CHANNEL, async (_event, key: unknown): Promise<ApiKeyStoreResult> => {
    if (typeof key !== 'string' || key.trim().length === 0) {
      return { ok: false, error: 'Key must be a non-empty string' };
    }
    try {
      await client.storeCredential('anthropic', key.trim());
      return { ok: true };
    } catch (error) {
      return { ok: false, error: error instanceof Error ? error.message : 'Failed to store key' };
    }
  });

  ipcMain.handle(API_KEY_REMOVE_CHANNEL, async (): Promise<ApiKeyStoreResult> => {
    try {
      await client.removeCredential('anthropic');
      return { ok: true };
    } catch (error) {
      return { ok: false, error: error instanceof Error ? error.message : 'Failed to remove key' };
    }
  });

  ipcMain.handle(API_KEY_STATUS_CHANNEL, async (): Promise<ApiKeyStatusResult> => {
    const status = await client.credentialStatus('anthropic');
    const envKey = hasEnvironmentKey('anthropic');
    return {
      hasKey: status.configured,
      encryptionAvailable: true,
      source: status.configured ? (envKey ? 'env' : 'ui') : 'none'
    };
  });

  ipcMain.handle(
    PROVIDER_API_KEY_STORE_CHANNEL,
    async (_event, providerId: unknown, key: unknown): Promise<ApiKeyStoreResult> => {
      if (!isProviderCredentialId(providerId)) {
        return invalidProviderResult();
      }
      if (typeof key !== 'string' || key.trim().length === 0) {
        return { ok: false, error: 'Key must be a non-empty string' };
      }
      try {
        await client.storeCredential(providerId, key.trim());
        return { ok: true };
      } catch (error) {
        return { ok: false, error: error instanceof Error ? error.message : 'Failed to store key' };
      }
    }
  );

  ipcMain.handle(
    PROVIDER_API_KEY_REMOVE_CHANNEL,
    async (_event, providerId: unknown): Promise<ApiKeyStoreResult> => {
      if (!isProviderCredentialId(providerId)) {
        return invalidProviderResult();
      }
      try {
        await client.removeCredential(providerId);
        return { ok: true };
      } catch (error) {
        return { ok: false, error: error instanceof Error ? error.message : 'Failed to remove key' };
      }
    }
  );

  ipcMain.handle(
    PROVIDER_API_KEY_STATUS_CHANNEL,
    async (_event, providerId: unknown): Promise<ApiKeyStatusResult | ApiKeyStoreResult> => {
      if (!isProviderCredentialId(providerId)) {
        return invalidProviderResult();
      }
      const status = await client.credentialStatus(providerId);
      const envKey = hasEnvironmentKey(providerId);
      return {
        hasKey: status.configured,
        encryptionAvailable: true,
        source: status.configured ? (envKey ? 'env' : 'ui') : 'none'
      };
    }
  );
}

export function unregisterApiKeyHandlers(): void {
  for (const channel of [
    API_KEY_STORE_CHANNEL,
    API_KEY_REMOVE_CHANNEL,
    API_KEY_STATUS_CHANNEL,
    PROVIDER_API_KEY_STORE_CHANNEL,
    PROVIDER_API_KEY_REMOVE_CHANNEL,
    PROVIDER_API_KEY_STATUS_CHANNEL
  ]) {
    ipcMain.removeHandler(channel);
  }
}
