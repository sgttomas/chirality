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
  /**
   * Set when the daemon could not be reached at all, so the renderer can tell
   * "no key stored" apart from "cannot currently tell". Absent on a real answer.
   */
  unavailable?: true;
  error?: string;
};

export type ApiKeyStoreResult = {
  ok: boolean;
  error?: string;
};

export interface DaemonCredentialClient {
  credentialStatus(providerId: ProviderCredentialId): Promise<unknown>;
  storeCredential(
    providerId: ProviderCredentialId,
    credential: string
  ): Promise<{ configured: boolean }>;
  removeCredential(providerId: ProviderCredentialId): Promise<{ configured: boolean }>;
}

function invalidProviderResult(): ApiKeyStoreResult {
  return { ok: false, error: 'Unsupported credential provider' };
}

/**
 * Credential status when the daemon cannot be reached.
 *
 * A status *query* must not reject into the renderer. When the daemon is down the
 * client throws (`ENOENT` on the operator token or the control socket), which
 * surfaced as an unhandled `Error occurred in handler for …` on the IPC channel
 * every time the app started without a running daemon. The connectivity
 * indicator already reports that state; this returns it as data instead.
 */
function unavailableStatusResult(error: unknown): ApiKeyStatusResult {
  return {
    hasKey: false,
    encryptionAvailable: false,
    source: 'none',
    unavailable: true,
    error: error instanceof Error ? error.message : 'Runtime daemon unavailable'
  };
}

function parseCredentialStatus(status: unknown): Pick<ApiKeyStatusResult, 'hasKey' | 'source'> | null {
  if (!status || typeof status !== 'object') {
    return null;
  }
  const { configured, source } = status as { configured?: unknown; source?: unknown };
  if (
    typeof configured !== 'boolean' ||
    (source !== 'ui' && source !== 'env' && source !== 'none') ||
    configured !== (source !== 'none')
  ) {
    return null;
  }
  return { hasKey: configured, source };
}

function invalidStatusResult(): ApiKeyStatusResult {
  return {
    hasKey: false,
    encryptionAvailable: false,
    source: 'none',
    error: 'Runtime daemon returned an invalid credential status'
  };
}

async function credentialStatusResult(
  client: DaemonCredentialClient,
  providerId: ProviderCredentialId
): Promise<ApiKeyStatusResult> {
  let status: unknown;
  try {
    status = await client.credentialStatus(providerId);
  } catch (error) {
    return unavailableStatusResult(error);
  }
  const parsed = parseCredentialStatus(status);
  if (!parsed) {
    return invalidStatusResult();
  }
  return {
    hasKey: parsed.hasKey,
    encryptionAvailable: true,
    source: parsed.source
  };
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

  ipcMain.handle(
    API_KEY_STATUS_CHANNEL,
    async (): Promise<ApiKeyStatusResult> => credentialStatusResult(client, 'anthropic')
  );

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
      return credentialStatusResult(client, providerId);
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
