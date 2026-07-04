import { access, mkdir, mkdtemp, readFile, rm, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import { FileSessionManager } from '../../lib/harness/session-manager';
import { SessionRecord } from '@chirality/harness-contract/types';

type PersistedSessionRecord = SessionRecord & Record<string, unknown>;

let tmpRoot = '';
let projectRoot = '';
let sessionRoot = '';

function sessionRecord(
  sessionId: string,
  overrides: Partial<PersistedSessionRecord> = {}
): PersistedSessionRecord {
  return {
    sessionId,
    projectRoot,
    persona: 'WORKING_ITEMS',
    mode: 'WORKBENCH',
    createdAt: '2026-06-21T00:00:00.000Z',
    updatedAt: '2026-06-21T00:00:00.000Z',
    ...overrides
  };
}

function canonicalPath(sessionId: string): string {
  return path.join(sessionRoot, sessionId, 'session.json');
}

function legacyPath(sessionId: string): string {
  return path.join(sessionRoot, `${sessionId}.json`);
}

async function readPersistedSession(sessionId: string): Promise<PersistedSessionRecord> {
  return JSON.parse(await readFile(canonicalPath(sessionId), 'utf8')) as PersistedSessionRecord;
}

beforeEach(async () => {
  tmpRoot = await mkdtemp(path.join(os.tmpdir(), 'chirality-session-manager-'));
  projectRoot = path.join(tmpRoot, 'project-root');
  sessionRoot = path.join(tmpRoot, '.chirality', 'sessions');
  await mkdir(projectRoot, { recursive: true });
  process.env.CHIRALITY_SESSION_ROOT = sessionRoot;
});

afterEach(async () => {
  delete process.env.CHIRALITY_SESSION_ROOT;
  if (tmpRoot) {
    await rm(tmpRoot, { recursive: true, force: true });
    tmpRoot = '';
  }
});

describe('FileSessionManager canonical session storage', () => {
  it('creates new sessions as canonical folder records without writing legacy flat files', async () => {
    const manager = new FileSessionManager();

    const session = await manager.create({ projectRoot, persona: 'TASK', mode: 'PIPELINE' });

    await expect(access(canonicalPath(session.sessionId))).resolves.toBeUndefined();
    await expect(access(legacyPath(session.sessionId))).rejects.toThrow();
    await expect(readPersistedSession(session.sessionId)).resolves.toMatchObject({
      sessionId: session.sessionId,
      projectRoot,
      persona: 'TASK',
      mode: 'PIPELINE'
    });
  });

  it('migrates legacy flat records to canonical folders on resume', async () => {
    const manager = new FileSessionManager();
    const sessionId = 'sess_legacy';
    await mkdir(sessionRoot, { recursive: true });
    await writeFile(
      legacyPath(sessionId),
      `${JSON.stringify(
        sessionRecord(sessionId, {
          claudeSessionId: 'claude_legacy',
          sdkTranscriptPath: '/tmp/transcript.jsonl',
          legacyOnly: 'preserved'
        }),
        null,
        2
      )}\n`,
      'utf8'
    );

    const session = (await manager.resume(sessionId)) as PersistedSessionRecord;

    expect(session).toMatchObject({
      sessionId,
      claudeSessionId: 'claude_legacy',
      sdkTranscriptPath: '/tmp/transcript.jsonl',
      legacyOnly: 'preserved'
    });
    await expect(access(legacyPath(sessionId))).rejects.toThrow();
    await expect(readPersistedSession(sessionId)).resolves.toMatchObject({
      claudeSessionId: 'claude_legacy',
      sdkTranscriptPath: '/tmp/transcript.jsonl',
      legacyOnly: 'preserved'
    });
  });

  it('resolves duplicate canonical and flat records with canonical precedence and no legacy field loss', async () => {
    const manager = new FileSessionManager();
    const sessionId = 'sess_duplicate';
    await mkdir(path.dirname(canonicalPath(sessionId)), { recursive: true });
    await mkdir(sessionRoot, { recursive: true });
    await writeFile(
      legacyPath(sessionId),
      `${JSON.stringify(
        sessionRecord(sessionId, {
          engineSessionId: 'engine_legacy',
          claudeSessionId: 'claude_legacy',
          sdkPackageVersion: 'legacy-sdk',
          legacyOnly: { nested: true }
        }),
        null,
        2
      )}\n`,
      'utf8'
    );
    await writeFile(
      canonicalPath(sessionId),
      `${JSON.stringify(
        sessionRecord(sessionId, {
          engineSessionId: 'engine_canonical',
          sdkSessionId: 'sdk_canonical',
          updatedAt: '2026-06-21T01:00:00.000Z'
        }),
        null,
        2
      )}\n`,
      'utf8'
    );

    const session = (await manager.getById(sessionId)) as PersistedSessionRecord;

    expect(session).toMatchObject({
      sessionId,
      engineSessionId: 'engine_canonical',
      sdkSessionId: 'sdk_canonical',
      claudeSessionId: 'claude_legacy',
      sdkPackageVersion: 'legacy-sdk',
      legacyOnly: { nested: true }
    });
    await expect(access(legacyPath(sessionId))).rejects.toThrow();
    await expect(readPersistedSession(sessionId)).resolves.toMatchObject({
      engineSessionId: 'engine_canonical',
      sdkSessionId: 'sdk_canonical',
      claudeSessionId: 'claude_legacy',
      sdkPackageVersion: 'legacy-sdk',
      legacyOnly: { nested: true }
    });
  });

  it('canonicalizes legacy records during list traversal', async () => {
    const manager = new FileSessionManager();
    const sessionId = 'sess_listed';
    await mkdir(sessionRoot, { recursive: true });
    await writeFile(
      legacyPath(sessionId),
      `${JSON.stringify(sessionRecord(sessionId, { model: 'claude-sonnet-4' }), null, 2)}\n`,
      'utf8'
    );

    const sessions = await manager.list(projectRoot);

    expect(sessions.map((session) => session.sessionId)).toEqual([sessionId]);
    await expect(access(legacyPath(sessionId))).rejects.toThrow();
    await expect(readPersistedSession(sessionId)).resolves.toMatchObject({
      sessionId,
      model: 'claude-sonnet-4'
    });
  });

  it('canonicalizes legacy records before saving updates', async () => {
    const manager = new FileSessionManager();
    const sessionId = 'sess_save';
    await mkdir(sessionRoot, { recursive: true });
    await writeFile(
      legacyPath(sessionId),
      `${JSON.stringify(sessionRecord(sessionId, { claudeSessionId: 'claude_legacy' }), null, 2)}\n`,
      'utf8'
    );

    const saved = await manager.save(sessionId, { model: 'claude-opus-4' });

    expect(saved).toMatchObject({
      sessionId,
      claudeSessionId: 'claude_legacy',
      model: 'claude-opus-4'
    });
    await expect(access(legacyPath(sessionId))).rejects.toThrow();
    await expect(readPersistedSession(sessionId)).resolves.toMatchObject({
      claudeSessionId: 'claude_legacy',
      model: 'claude-opus-4'
    });
  });

  it('removes canonical folders and stray flat files when deleting a session', async () => {
    const manager = new FileSessionManager();
    const sessionId = 'sess_delete';
    await mkdir(path.dirname(canonicalPath(sessionId)), { recursive: true });
    await mkdir(sessionRoot, { recursive: true });
    await writeFile(
      canonicalPath(sessionId),
      `${JSON.stringify(sessionRecord(sessionId, { engineSessionId: 'engine_canonical' }), null, 2)}\n`,
      'utf8'
    );
    await writeFile(
      legacyPath(sessionId),
      `${JSON.stringify(sessionRecord(sessionId, { claudeSessionId: 'claude_legacy' }), null, 2)}\n`,
      'utf8'
    );

    await manager.delete(sessionId);

    await expect(access(path.dirname(canonicalPath(sessionId)))).rejects.toThrow();
    await expect(access(legacyPath(sessionId))).rejects.toThrow();
    await expect(manager.getById(sessionId)).rejects.toMatchObject({ type: 'SESSION_NOT_FOUND' });
  });
});
