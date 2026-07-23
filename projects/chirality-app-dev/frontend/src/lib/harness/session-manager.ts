import { randomUUID } from 'node:crypto';
import { mkdir, readdir, readFile, rm, stat, writeFile, access } from 'node:fs/promises';
import { constants as fsConstants } from 'node:fs';
import path from 'node:path';
import { HarnessError } from '@chirality/harness-contract/errors';
import { instructionRootContainsPath, resolveInstructionRootPath } from './instruction-root';
import { ISessionManager, SessionCreateRequest, SessionRecord } from '@chirality/harness-contract/types';

const DEFAULT_PERSONA = 'WORKING_ITEMS';
const DEFAULT_MODE = 'direct';
const CANONICAL_SESSION_FILE = 'session.json';

type RawSessionRecord = SessionRecord & Record<string, unknown>;

function getSessionStoreDirectory(): string {
  return process.env.CHIRALITY_SESSION_ROOT ?? path.join(process.cwd(), '.chirality', 'sessions');
}

async function ensureDirectoryExists(dirPath: string): Promise<void> {
  await mkdir(dirPath, { recursive: true });
}

export async function assertProjectRootAccessible(projectRoot: string): Promise<string> {
  if (!path.isAbsolute(projectRoot)) {
    throw new HarnessError(
      'INVALID_REQUEST',
      400,
      'projectRoot must be an absolute filesystem path',
      { projectRoot }
    );
  }

  const normalizedProjectRoot = path.resolve(projectRoot);
  const instructionRoot = resolveInstructionRootPath();
  if (instructionRootContainsPath(normalizedProjectRoot, instructionRoot)) {
    throw new HarnessError(
      'WORKING_ROOT_CONFLICT',
      409,
      'projectRoot cannot point inside instruction root',
      {
        projectRoot: normalizedProjectRoot,
        instructionRoot
      }
    );
  }

  try {
    const directoryStat = await stat(normalizedProjectRoot);
    if (!directoryStat.isDirectory()) {
      throw new HarnessError(
        'WORKING_ROOT_INACCESSIBLE',
        404,
        'projectRoot must point to an existing directory',
        { projectRoot: normalizedProjectRoot }
      );
    }
    await access(normalizedProjectRoot, fsConstants.R_OK | fsConstants.W_OK);
  } catch (error) {
    if (error instanceof HarnessError) {
      throw error;
    }
    throw new HarnessError('WORKING_ROOT_INACCESSIBLE', 404, 'projectRoot is not accessible', {
      projectRoot: normalizedProjectRoot
    });
  }

  return normalizedProjectRoot;
}

function assertSafeSessionId(sessionId: string): void {
  if (
    sessionId.trim().length === 0 ||
    sessionId === '.' ||
    sessionId === '..' ||
    sessionId.includes('/') ||
    sessionId.includes('\\')
  ) {
    throw new HarnessError('SESSION_NOT_FOUND', 404, `Session '${sessionId}' does not exist`, {
      sessionId
    });
  }
}

function getCanonicalSessionDirectoryPath(sessionId: string): string {
  assertSafeSessionId(sessionId);
  return path.join(getSessionStoreDirectory(), sessionId);
}

function getCanonicalSessionFilePath(sessionId: string): string {
  return path.join(getCanonicalSessionDirectoryPath(sessionId), CANONICAL_SESSION_FILE);
}

function getLegacySessionFilePath(sessionId: string): string {
  assertSafeSessionId(sessionId);
  return path.join(getSessionStoreDirectory(), `${sessionId}.json`);
}

async function readOptionalSessionFile(filePath: string): Promise<RawSessionRecord | undefined> {
  try {
    const raw = await readFile(filePath, 'utf8');
    const parsed = JSON.parse(raw) as unknown;
    if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) {
      return undefined;
    }
    return parsed as RawSessionRecord;
  } catch {
    return undefined;
  }
}

function mergeSessionRecords(
  sessionId: string,
  legacyRecord: RawSessionRecord | undefined,
  canonicalRecord: RawSessionRecord | undefined
): RawSessionRecord | undefined {
  if (!legacyRecord && !canonicalRecord) {
    return undefined;
  }

  const merged: Record<string, unknown> = legacyRecord ? { ...legacyRecord } : {};
  if (canonicalRecord) {
    for (const [key, value] of Object.entries(canonicalRecord)) {
      if (value !== undefined) {
        merged[key] = value;
      }
    }
  }
  merged.sessionId = sessionId;

  return synthesizeProviderNeutralMetadata(merged as RawSessionRecord);
}

function asRecord(value: unknown): Record<string, unknown> | undefined {
  return value && typeof value === 'object' && !Array.isArray(value)
    ? (value as Record<string, unknown>)
    : undefined;
}

function hasSdkAttribution(session: RawSessionRecord): boolean {
  return (
    [
      session.sdkSessionId,
      session.sdkTranscriptPath,
      session.sdkSessionStoreKey,
      session.sdkConfigDir,
      session.sdkClaudeCodeVersion
    ].some((value) => typeof value === 'string' && value.trim().length > 0) ||
    (Array.isArray(session.sdkSettingSources) && session.sdkSettingSources.length > 0)
  );
}

function inferLegacyClaudeAdapter(
  session: RawSessionRecord
): 'anthropic-direct' | 'claude-agent-sdk' | undefined {
  const explicitSelection = asRecord(session.engineSelection);
  if (explicitSelection?.providerId === 'anthropic') {
    if (explicitSelection.adapterId === 'anthropic-direct') {
      return 'anthropic-direct';
    }
    if (explicitSelection.adapterId === 'claude-agent-sdk') {
      return 'claude-agent-sdk';
    }
  }
  if (explicitSelection) {
    return undefined;
  }

  if (hasSdkAttribution(session)) {
    return 'claude-agent-sdk';
  }

  const adapterSession = asRecord(session.adapterSession);
  if (adapterSession?.packageName === '@anthropic-ai/claude-agent-sdk') {
    return 'claude-agent-sdk';
  }
  if (adapterSession?.packageName === '@anthropic-ai/sdk') {
    return 'anthropic-direct';
  }

  const runtimeFingerprint = asRecord(session.runtimeFingerprint);
  const engineAdapter = asRecord(runtimeFingerprint?.engineAdapter);
  if (engineAdapter?.providerId === 'anthropic') {
    if (engineAdapter.adapterId === 'anthropic-direct') {
      return 'anthropic-direct';
    }
    if (engineAdapter.adapterId === 'claude-agent-sdk') {
      return 'claude-agent-sdk';
    }
  }

  return undefined;
}

function synthesizeProviderNeutralMetadata(session: RawSessionRecord): RawSessionRecord {
  const legacyEngineSessionId = [
    session.engineSessionId,
    session.sdkSessionId,
    session.claudeSessionId
  ].find((value): value is string => typeof value === 'string' && value.trim().length > 0);
  const inferredAdapterId = inferLegacyClaudeAdapter(session);

  // A claudeSessionId by itself is ambiguous: historical stub sessions used the
  // same field. Keep it readable, but leave selection to the current key-aware
  // runtime default instead of silently pinning the record to Anthropic.
  if (!legacyEngineSessionId || !inferredAdapterId) {
    return session;
  }

  const existingAdapterSession = asRecord(session.adapterSession);
  const existingEngineSessionId = existingAdapterSession?.engineSessionId;

  return {
    ...session,
    ...(session.engineSelection
      ? {}
      : {
          engineSelection: {
            adapterId: inferredAdapterId,
            providerId: 'anthropic',
            model: typeof session.model === 'string' ? session.model : ''
          }
        }),
    adapterSession: {
      transcriptPath: session.sdkTranscriptPath,
      storeKey: session.sdkSessionStoreKey,
      configDir: session.sdkConfigDir,
      packageName:
        inferredAdapterId === 'claude-agent-sdk'
          ? '@anthropic-ai/claude-agent-sdk'
          : '@anthropic-ai/sdk',
      packageVersion: session.sdkPackageVersion,
      ...existingAdapterSession,
      engineSessionId:
        typeof existingEngineSessionId === 'string'
          ? existingEngineSessionId
          : legacyEngineSessionId
    }
  };
}

async function writeCanonicalSession(
  sessionId: string,
  session: SessionRecord | RawSessionRecord
): Promise<void> {
  const sessionDirectory = getCanonicalSessionDirectoryPath(sessionId);
  await ensureDirectoryExists(sessionDirectory);
  await writeFile(
    getCanonicalSessionFilePath(sessionId),
    `${JSON.stringify(session, null, 2)}\n`,
    'utf8'
  );
}

async function canonicalizeSessionRecord(sessionId: string): Promise<RawSessionRecord> {
  const legacyFilePath = getLegacySessionFilePath(sessionId);
  const canonicalFilePath = getCanonicalSessionFilePath(sessionId);
  const [legacyRecord, canonicalRecord] = await Promise.all([
    readOptionalSessionFile(legacyFilePath),
    readOptionalSessionFile(canonicalFilePath)
  ]);

  const merged = mergeSessionRecords(sessionId, legacyRecord, canonicalRecord);
  if (!merged) {
    throw new HarnessError('SESSION_NOT_FOUND', 404, `Session '${sessionId}' does not exist`, {
      sessionId
    });
  }

  if (legacyRecord || !canonicalRecord) {
    await writeCanonicalSession(sessionId, merged);
  }
  if (legacyRecord) {
    await rm(legacyFilePath, { force: true });
  }

  return merged;
}

export class FileSessionManager implements ISessionManager {
  async create(input: SessionCreateRequest): Promise<SessionRecord> {
    const projectRoot = await assertProjectRootAccessible(input.projectRoot);
    await ensureDirectoryExists(getSessionStoreDirectory());

    const now = new Date().toISOString();
    const session: SessionRecord = {
      sessionId: `sess_${randomUUID()}`,
      projectRoot,
      persona: input.persona?.trim() || DEFAULT_PERSONA,
      mode: input.mode?.trim() || DEFAULT_MODE,
      createdAt: now,
      updatedAt: now
    };

    await writeCanonicalSession(session.sessionId, session);
    return session;
  }

  async resume(sessionId: string): Promise<SessionRecord> {
    return this.getById(sessionId);
  }

  async getById(sessionId: string): Promise<SessionRecord> {
    await ensureDirectoryExists(getSessionStoreDirectory());
    return canonicalizeSessionRecord(sessionId);
  }

  async save(sessionId: string, updates: Partial<SessionRecord>): Promise<SessionRecord> {
    await ensureDirectoryExists(getSessionStoreDirectory());
    const existing = await canonicalizeSessionRecord(sessionId);
    const updated: SessionRecord = {
      ...existing,
      ...updates,
      sessionId: existing.sessionId,
      createdAt: existing.createdAt,
      updatedAt: new Date().toISOString()
    };

    await writeCanonicalSession(sessionId, updated);
    return updated;
  }

  async list(projectRoot: string): Promise<SessionRecord[]> {
    const normalizedProjectRoot = await assertProjectRootAccessible(projectRoot);
    await ensureDirectoryExists(getSessionStoreDirectory());

    const entries = await readdir(getSessionStoreDirectory(), { withFileTypes: true });
    const candidateSessionIds = new Set<string>();
    const sessions: SessionRecord[] = [];

    for (const entry of entries) {
      if (entry.isDirectory()) {
        candidateSessionIds.add(entry.name);
      } else if (entry.isFile() && entry.name.endsWith('.json')) {
        candidateSessionIds.add(entry.name.replace(/\.json$/, ''));
      }
    }

    for (const sessionId of [...candidateSessionIds].sort()) {
      try {
        const session = await canonicalizeSessionRecord(sessionId);
        if (path.resolve(session.projectRoot) === normalizedProjectRoot) {
          sessions.push(session);
        }
      } catch {
        // Ignore malformed or orphaned records during list traversal.
      }
    }

    sessions.sort((a, b) => a.createdAt.localeCompare(b.createdAt));
    return sessions;
  }

  async delete(sessionId: string): Promise<void> {
    await ensureDirectoryExists(getSessionStoreDirectory());

    await canonicalizeSessionRecord(sessionId);
    await rm(getCanonicalSessionDirectoryPath(sessionId), { recursive: true, force: true });
    await rm(getLegacySessionFilePath(sessionId), { force: true });
  }
}
