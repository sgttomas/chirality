/**
 * Provider credential storage.
 *
 * Credentials are encrypted with Electron safeStorage and persisted under the
 * app userData directory. The Anthropic filename and process-global are kept
 * for compatibility with existing installations and server-side consumers.
 */

import { app, safeStorage } from 'electron';
import { mkdir, readFile, rm, writeFile } from 'node:fs/promises';
import path from 'node:path';

export const PROVIDER_CREDENTIAL_IDS = ['anthropic', 'omlx'] as const;
export type ProviderCredentialId = (typeof PROVIDER_CREDENTIAL_IDS)[number];

const LEGACY_ANTHROPIC_STORAGE_FILENAME = 'api-key.enc';
const PROVIDER_STORAGE_FILENAMES: Record<ProviderCredentialId, string> = {
  anthropic: LEGACY_ANTHROPIC_STORAGE_FILENAME,
  omlx: 'api-key.omlx.enc'
};
const LEGACY_ANTHROPIC_GLOBAL_KEY = '__CHIRALITY_UI_API_KEY__';
const PROVIDER_GLOBAL_KEY = '__CHIRALITY_PROVIDER_API_KEYS__';

type ApiKeyGlobal = typeof globalThis & {
  [LEGACY_ANTHROPIC_GLOBAL_KEY]?: string;
  [PROVIDER_GLOBAL_KEY]?: Partial<Record<ProviderCredentialId, string>>;
};

const apiKeyGlobal = globalThis as ApiKeyGlobal;

export function isProviderCredentialId(value: unknown): value is ProviderCredentialId {
  return typeof value === 'string' && PROVIDER_CREDENTIAL_IDS.includes(value as ProviderCredentialId);
}

function getStoragePath(providerId: ProviderCredentialId): string {
  return path.join(app.getPath('userData'), 'credentials', PROVIDER_STORAGE_FILENAMES[providerId]);
}

async function ensureStorageDir(providerId: ProviderCredentialId): Promise<void> {
  await mkdir(path.dirname(getStoragePath(providerId)), { recursive: true });
}

function setProviderGlobal(providerId: ProviderCredentialId, key: string | undefined): void {
  const providerKeys = apiKeyGlobal[PROVIDER_GLOBAL_KEY] ?? {};
  if (key) {
    providerKeys[providerId] = key;
  } else {
    delete providerKeys[providerId];
  }
  apiKeyGlobal[PROVIDER_GLOBAL_KEY] = providerKeys;

  if (providerId === 'anthropic') {
    apiKeyGlobal[LEGACY_ANTHROPIC_GLOBAL_KEY] = key;
  }
}

export async function storeProviderApiKey(
  providerId: ProviderCredentialId,
  key: string
): Promise<void> {
  if (!safeStorage.isEncryptionAvailable()) {
    throw new Error('Secure storage is not available on this platform');
  }

  const encrypted = safeStorage.encryptString(key);
  await ensureStorageDir(providerId);
  await writeFile(getStoragePath(providerId), encrypted);
  setProviderGlobal(providerId, key);
}

export async function retrieveProviderApiKey(
  providerId: ProviderCredentialId
): Promise<string | null> {
  if (!safeStorage.isEncryptionAvailable()) {
    return null;
  }

  let encrypted: Buffer;
  try {
    encrypted = await readFile(getStoragePath(providerId));
  } catch {
    return null;
  }

  try {
    return safeStorage.decryptString(encrypted);
  } catch {
    // Preserve corrupted blobs for operator investigation.
    return null;
  }
}

export async function removeProviderApiKey(providerId: ProviderCredentialId): Promise<void> {
  setProviderGlobal(providerId, undefined);
  try {
    await rm(getStoragePath(providerId));
  } catch {
    // Missing files are already in the desired state.
  }
}

export async function hasStoredProviderApiKey(providerId: ProviderCredentialId): Promise<boolean> {
  if (getProviderUiApiKey(providerId)) {
    return true;
  }

  try {
    await readFile(getStoragePath(providerId));
    return true;
  } catch {
    return false;
  }
}

export function isEncryptionAvailable(): boolean {
  return safeStorage.isEncryptionAvailable();
}

/** Load every supported provider credential during Electron startup. */
export async function loadStoredKeyIntoGlobal(): Promise<void> {
  await Promise.all(
    PROVIDER_CREDENTIAL_IDS.map(async (providerId) => {
      const key = await retrieveProviderApiKey(providerId);
      if (key) {
        setProviderGlobal(providerId, key);
      }
    })
  );
}

export function getProviderUiApiKey(providerId: ProviderCredentialId): string | undefined {
  const providerValue = apiKeyGlobal[PROVIDER_GLOBAL_KEY]?.[providerId];
  if (typeof providerValue === 'string' && providerValue.trim().length > 0) {
    return providerValue;
  }
  if (providerId === 'anthropic') {
    return apiKeyGlobal[LEGACY_ANTHROPIC_GLOBAL_KEY];
  }
  return undefined;
}

// Anthropic compatibility API. These deliberately retain the original
// filename, global, signatures, and behavior.
export const storeApiKey = (key: string): Promise<void> => storeProviderApiKey('anthropic', key);
export const retrieveApiKey = (): Promise<string | null> => retrieveProviderApiKey('anthropic');
export const removeApiKey = (): Promise<void> => removeProviderApiKey('anthropic');
export const hasStoredApiKey = (): Promise<boolean> => hasStoredProviderApiKey('anthropic');
export const getUiApiKey = (): string | undefined => getProviderUiApiKey('anthropic');
