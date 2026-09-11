import { mkdtemp, realpath, rm } from 'node:fs/promises';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { RuntimeError } from '@chirality/runtime-contracts';

const electron = vi.hoisted(() => {
  const handlers = new Map<string, (...arguments_: unknown[]) => Promise<unknown>>();
  return {
    handlers,
    ipcMain: {
      handle: vi.fn((channel: string, handler: (...arguments_: unknown[]) => Promise<unknown>) => handlers.set(channel, handler)),
      removeHandler: vi.fn((channel: string) => handlers.delete(channel))
    }
  };
});
vi.mock('electron', () => ({ ipcMain: electron.ipcMain }));

import { HOST_ACCOUNT_CHANNEL } from '../../../electron/host-account-ipc-contract';
import { createHostAccountConnection } from '../../../electron/host-account-connection';
import { performHostAccountOperation, registerHostAccountHandler } from '../../../electron/host-account-ipc';

const RENDERER_ORIGIN = 'http://127.0.0.1:3000';
const account = {
  start: vi.fn(async () => undefined), close: vi.fn(async () => undefined), status: vi.fn(),
  grantProviderNetworkConsent: vi.fn(), startLogin: vi.fn(), cancelLogin: vi.fn(), signOut: vi.fn()
};
let root: string;
let project: { projectId: string; displayName: string; canonicalRoot: string; manifestPath: string; manifestHash: string; registeredAt: string; approval: { approvedBy: string; approvalReference: string }; clientId: string; enabledAdapterIds: readonly string[]; legacySessionRoots: readonly string[] };

function projectStatus() { return { project, manifestDrift: false, adaptersEnabled: true }; }

function deferred() {
  let resolve!: () => void;
  const promise = new Promise<void>((done) => { resolve = done; });
  return { promise, resolve };
}

function deferredResult<T>() {
  let resolve!: (value: T) => void;
  let reject!: (error: unknown) => void;
  const promise = new Promise<T>((done, fail) => { resolve = done; reject = fail; });
  return { promise, resolve, reject };
}

beforeEach(async () => {
  root = await realpath(await mkdtemp('/tmp/host-account-ipc-'));
  project = { projectId: 'registered-project', displayName: 'Registered project', canonicalRoot: root, manifestPath: `${root}/.chirality/project.json`, manifestHash: 'a'.repeat(64), registeredAt: '2026-09-10T00:00:00.000Z', approval: { approvedBy: 'owner', approvalReference: 'decision' }, clientId: 'client', enabledAdapterIds: ['codex-app-server'], legacySessionRoots: [] };
  electron.handlers.clear(); vi.clearAllMocks();
  account.status.mockResolvedValue({ schema: 'chirality-hosted-bootstrap-status/v1', projectId: project.projectId, ceremony: 'consent-required', admission: 'unavailable', canStartLogin: false });
});
afterEach(async () => rm(root, { recursive: true, force: true }));

describe('host account main-process IPC', () => {
  it('maps a canonical registered root to the daemon-owned project id', async () => {
    const runtimeClient = { listProjects: vi.fn(async () => [projectStatus()]), projectStatus: vi.fn(async () => projectStatus()) };
    const result = await performHostAccountOperation({ operation: 'status', projectRoot: root }, { runtimeClient, accountClient: () => account });
    expect(result).toMatchObject({ ok: true, value: { registration: 'registered', projectId: project.projectId } });
    expect(runtimeClient.projectStatus).toHaveBeenCalledWith(project.projectId);
    expect(account.status).toHaveBeenCalledWith(project.projectId);
  });

  it('forwards a ready status with the model catalog and selection verbatim', async () => {
    const ready = {
      schema: 'chirality-hosted-bootstrap-status/v1', projectId: project.projectId, ceremony: 'signed-in', admission: 'ready', canStartLogin: false,
      models: [
        { model: 'gpt-default', isDefault: true, defaultReasoningEffort: 'high', supportedReasoningEfforts: ['low', 'medium', 'high'] },
        { model: 'gpt-alt', isDefault: false, defaultReasoningEffort: 'medium', supportedReasoningEfforts: ['medium', 'low'] }
      ],
      selection: { model: 'gpt-default', reasoningEffort: 'high' }
    };
    account.status.mockResolvedValue(ready);
    const runtimeClient = { listProjects: vi.fn(async () => [projectStatus()]), projectStatus: vi.fn(async () => projectStatus()) };
    const result = await performHostAccountOperation({ operation: 'status', projectRoot: root }, { runtimeClient, accountClient: () => account });
    expect(result).toEqual({ ok: true, value: { registration: 'registered', projectId: project.projectId, status: ready } });
  });

  it('rejects malformed and noncanonical roots before registry or account effects', async () => {
    const runtimeClient = { listProjects: vi.fn(), projectStatus: vi.fn() };
    for (const request of [{ operation: 'status', projectRoot: 'relative' }, { operation: 'status', projectRoot: `${root}/..` }, { operation: 'status', projectRoot: root, projectId: 'renderer-choice' }]) {
      await expect(performHostAccountOperation(request, { runtimeClient, accountClient: () => account })).resolves.toEqual({ ok: false, error: 'Hosted account service is unavailable.' });
    }
    expect(runtimeClient.listProjects).not.toHaveBeenCalled();
    expect(account.status).not.toHaveBeenCalled();
  });

  it('preserves registration-required status and rejects ambiguous registry ownership', async () => {
    const runtimeClient = { listProjects: vi.fn(async () => [projectStatus(), projectStatus()]), projectStatus: vi.fn() };
    await expect(performHostAccountOperation({ operation: 'status', projectRoot: root }, { runtimeClient, accountClient: () => account })).resolves.toEqual({ ok: true, value: { registration: 'required' } });
    expect(runtimeClient.projectStatus).not.toHaveBeenCalled();
    expect(account.status).not.toHaveBeenCalled();
  });

  it('rejects foreign origins and reduces account failures to one coarse error', async () => {
    const runtimeClient = { listProjects: vi.fn(async () => [projectStatus()]), projectStatus: vi.fn(async () => projectStatus()) };
    account.signOut.mockRejectedValue(new Error('Bearer secret-token x-chirality-account-proof signature-value'));
    registerHostAccountHandler({ runtimeClient, accountClient: () => account, rendererOrigin: RENDERER_ORIGIN });
    const handler = electron.handlers.get(HOST_ACCOUNT_CHANNEL);
    expect(handler).toBeDefined();
    expect(handler?.({ senderFrame: { url: 'https://attacker.example/settings' } }, { operation: 'status', projectRoot: root })).toEqual({ ok: false, error: 'Hosted account service is unavailable.' });
    expect(runtimeClient.listProjects).not.toHaveBeenCalled();
    await expect(handler?.({ senderFrame: { url: `${RENDERER_ORIGIN}/settings` } }, { operation: 'sign-out', projectRoot: root })).resolves.toEqual({ ok: false, error: 'Hosted account service is unavailable.' });
  });

  it('cannot call a stale account client once disconnect retirement begins', async () => {
    const closeGate = deferred();
    const lifecycleClient = { ...account, close: vi.fn(() => closeGate.promise) };
    const connection = createHostAccountConnection({
      connect: async () => lifecycleClient,
      log: vi.fn()
    });
    await connection.update(true);
    account.status.mockClear();
    const disconnecting = connection.update(false);
    expect(connection.client()).toBeUndefined();
    const runtimeClient = {
      listProjects: vi.fn(async () => [projectStatus()]),
      projectStatus: vi.fn(async () => projectStatus())
    };
    await expect(performHostAccountOperation(
      { operation: 'status', projectRoot: root },
      { runtimeClient, accountClient: () => connection.client() }
    )).resolves.toEqual({ ok: false, error: 'Hosted account service is unavailable.' });
    expect(account.status).not.toHaveBeenCalled();
    closeGate.resolve();
    await disconnecting;
  });

  it('retires a client after an operation failure and connects a fresh replacement without replaying the effect', async () => {
    const failedStatus = deferredResult<never>();
    const first = { ...account, status: vi.fn(() => failedStatus.promise), close: vi.fn(async () => undefined) };
    const second = { ...account, status: vi.fn(), close: vi.fn(async () => undefined) };
    const connection = createHostAccountConnection({
      connect: vi.fn().mockResolvedValueOnce(first).mockResolvedValueOnce(second),
      log: vi.fn()
    });
    await connection.update(true);
    const runtimeClient = {
      listProjects: vi.fn(async () => [projectStatus()]),
      projectStatus: vi.fn(async () => projectStatus())
    };
    let unpublishedOnInvalidate = false;
    const operation = performHostAccountOperation(
      { operation: 'status', projectRoot: root },
      {
        runtimeClient,
        accountClient: () => connection.client(),
        invalidateAccountClient: (client) => {
          void connection.invalidate(client);
          unpublishedOnInvalidate = connection.client() === undefined;
        }
      }
    );
    await vi.waitFor(() => expect(first.status).toHaveBeenCalledOnce());
    failedStatus.reject(new Error('x-chirality-account-proof sensitive-value'));
    await expect(operation).resolves.toEqual({ ok: false, error: 'Hosted account service is unavailable.' });
    expect(unpublishedOnInvalidate).toBe(true);
    await vi.waitFor(() => expect(connection.client()).toBe(second));
    expect(second.status).not.toHaveBeenCalled();
    await connection.close();
  });

  it('does not let a late failure from client A retire replacement B', async () => {
    const lateStatus = deferredResult<never>();
    const first = { ...account, status: vi.fn(() => lateStatus.promise), close: vi.fn(async () => undefined) };
    const second = { ...account, status: vi.fn(), close: vi.fn(async () => undefined) };
    const connection = createHostAccountConnection({
      connect: vi.fn().mockResolvedValueOnce(first).mockResolvedValueOnce(second),
      log: vi.fn()
    });
    await connection.update(true);
    const runtimeClient = {
      listProjects: vi.fn(async () => [projectStatus()]),
      projectStatus: vi.fn(async () => projectStatus())
    };
    const operation = performHostAccountOperation(
      { operation: 'status', projectRoot: root },
      {
        runtimeClient,
        accountClient: () => connection.client(),
        invalidateAccountClient: (client) => { void connection.invalidate(client); }
      }
    );
    await vi.waitFor(() => expect(first.status).toHaveBeenCalledOnce());
    await connection.update(false);
    await connection.update(true);
    expect(connection.client()).toBe(second);
    lateStatus.reject(new Error('late failure'));
    await expect(operation).resolves.toEqual({ ok: false, error: 'Hosted account service is unavailable.' });
    expect(connection.client()).toBe(second);
    await connection.close();
  });

  describe('daemon operation rejections', () => {
    const rejected = (details: Record<string, unknown>) =>
      new RuntimeError('ENGINE_UNAVAILABLE', 'Account operation was rejected', 409, details);
    const runtime = () => ({ listProjects: vi.fn(async () => [projectStatus()]), projectStatus: vi.fn(async () => projectStatus()) });

    it('keeps the signed client, returns the reason, and logs the rejection without request material', async () => {
      account.startLogin.mockRejectedValue(rejected({
        kind: 'operation-rejected', operation: 'start-login', status: 409,
        daemonCode: 'ENGINE_UNAVAILABLE', reason: 'CODEX_REQUEST_REJECTED', daemonMessage: 'Codex refused the login request'
      }));
      const invalidateAccountClient = vi.fn();
      const log = vi.fn();
      await expect(performHostAccountOperation(
        { operation: 'start-login', projectRoot: root },
        { runtimeClient: runtime(), accountClient: () => account, invalidateAccountClient, log }
      )).resolves.toEqual({ ok: false, error: 'Sign-in could not start (CODEX_REQUEST_REJECTED).', reason: 'CODEX_REQUEST_REJECTED' });
      expect(invalidateAccountClient).not.toHaveBeenCalled();
      expect(log).toHaveBeenCalledOnce();
      expect(log).toHaveBeenCalledWith('warn', 'runtime.account_host.operation_rejected', expect.objectContaining({
        operation: 'start-login', projectId: project.projectId, code: 'ENGINE_UNAVAILABLE', status: 409,
        message: 'Account operation was rejected', daemonCode: 'ENGINE_UNAVAILABLE', reason: 'CODEX_REQUEST_REJECTED',
        daemonMessage: 'Codex refused the login request'
      }));
      expect(JSON.stringify(log.mock.calls)).not.toMatch(/authUrl|Bearer|proof|counter|https?:/i);
    });

    it('falls back to the daemon code as the reason and words each operation for the operator', async () => {
      const details = { kind: 'operation-rejected', operation: 'x', status: 400, daemonCode: 'INVALID_REQUEST' };
      account.grantProviderNetworkConsent.mockRejectedValue(rejected(details));
      account.cancelLogin.mockRejectedValue(rejected(details));
      account.signOut.mockRejectedValue(rejected(details));
      account.status.mockRejectedValue(rejected({ kind: 'operation-rejected', operation: 'status', status: 404 }));
      const invalidateAccountClient = vi.fn();
      const options = { runtimeClient: runtime(), accountClient: () => account, invalidateAccountClient };
      await expect(performHostAccountOperation({ operation: 'grant-provider-network-consent', projectRoot: root }, options))
        .resolves.toEqual({ ok: false, error: 'Provider network consent could not be recorded (INVALID_REQUEST).', reason: 'INVALID_REQUEST' });
      await expect(performHostAccountOperation({ operation: 'cancel-login', projectRoot: root }, options))
        .resolves.toEqual({ ok: false, error: 'Sign-in could not be cancelled (INVALID_REQUEST).', reason: 'INVALID_REQUEST' });
      await expect(performHostAccountOperation({ operation: 'sign-out', projectRoot: root }, options))
        .resolves.toEqual({ ok: false, error: 'Sign-out could not complete (INVALID_REQUEST).', reason: 'INVALID_REQUEST' });
      await expect(performHostAccountOperation({ operation: 'status', projectRoot: root }, options))
        .resolves.toEqual({ ok: false, error: 'Account status could not be read.' });
      expect(invalidateAccountClient).not.toHaveBeenCalled();
    });

    it.each([
      ['no details', new RuntimeError('ENGINE_UNAVAILABLE', 'Account host authority was revoked during request', 503)],
      ['a different kind', rejected({ kind: 'transport', operation: 'start-login', status: 503 })],
      ['a malformed reason', rejected({ kind: 'operation-rejected', operation: 'start-login', status: 409, reason: 'not a code' })],
      ['an oversized daemon message', rejected({ kind: 'operation-rejected', operation: 'start-login', status: 409, daemonMessage: 'x'.repeat(201) })],
      ['a plain transport error', new Error('Bearer secret-token x-chirality-account-proof signature-value')]
    ])('treats %s as a transport failure: retires the client and logs without the raw message', async (_label, failure) => {
      account.startLogin.mockRejectedValue(failure);
      const invalidateAccountClient = vi.fn();
      const log = vi.fn();
      await expect(performHostAccountOperation(
        { operation: 'start-login', projectRoot: root },
        { runtimeClient: runtime(), accountClient: () => account, invalidateAccountClient, log }
      )).resolves.toEqual({ ok: false, error: 'Hosted account service is unavailable.' });
      expect(invalidateAccountClient).toHaveBeenCalledWith(account);
      expect(log).toHaveBeenCalledWith('error', 'runtime.account_host.operation_failed', expect.objectContaining({
        operation: 'start-login', projectId: project.projectId, clientSelected: true
      }));
      expect(JSON.stringify(log.mock.calls)).not.toMatch(/secret-token|signature-value|not a code|xxxx/);
    });

    it('logs an invalid request and a missing account client without retiring anything', async () => {
      const invalidateAccountClient = vi.fn();
      const log = vi.fn();
      await expect(performHostAccountOperation(
        { operation: 'nope', projectRoot: root },
        { runtimeClient: runtime(), accountClient: () => account, invalidateAccountClient, log }
      )).resolves.toEqual({ ok: false, error: 'Hosted account service is unavailable.' });
      expect(log).toHaveBeenCalledWith('error', 'runtime.account_host.operation_failed', expect.objectContaining({ clientSelected: false }));
      await expect(performHostAccountOperation(
        { operation: 'status', projectRoot: root },
        { runtimeClient: runtime(), accountClient: () => undefined, invalidateAccountClient, log }
      )).resolves.toEqual({ ok: false, error: 'Hosted account service is unavailable.' });
      expect(invalidateAccountClient).not.toHaveBeenCalled();
    });
  });
});
