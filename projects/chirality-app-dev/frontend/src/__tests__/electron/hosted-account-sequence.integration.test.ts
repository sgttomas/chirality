/**
 * Complete hosted-account sequence through production code against a real
 * controlled Runtime daemon that owns an account host.
 *
 * Production limbs exercised (nothing under test is mocked):
 *   renderer client (`hosted-bootstrap-client.ts`)
 *     -> Next route handlers (`app/api/harness/hosted-bootstrap/**`)
 *     -> `RuntimeHostedBootstrapPort` built from the Desktop environment
 *     -> real daemon (`startControlledHostedBootstrapRuntimeHostForTests`)
 *   renderer client
 *     -> account bridge (preload's unwrap, replicated verbatim)
 *     -> `performHostAccountOperation` (`electron/host-account-ipc.ts`)
 *     -> real signed `HostAccountClient` (`createHostAccountClient`)
 *     -> real daemon with a real `HostAccountAuthority`
 *
 * Native-only limbs (not exercised here): the Electron IPC transport itself
 * (`ipcRenderer.invoke` / `ipcMain.handle` / `contextBridge`), the Next HTTP
 * server between renderer `fetch` and the route handlers, and the XPC
 * transport plus codesign peer verification that `createVerifiedHostAccountClient`
 * and `createVerifiedHostAccountAuthority` add on top of the same client and
 * authority classes used here. The XPC ceremony is replaced by an in-process
 * seam that carries the same challenge/nonce/proof bytes, so the daemon's
 * proof verification, counter/replay guard, and scope checks run for real.
 */
import { mkdir, mkdtemp, realpath, rm } from 'node:fs/promises';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { hostedModelCatalog, type AgentEnginePort, type HostedModelCatalogEntry } from '@chirality/runtime-contracts';
import { RuntimeClient } from '@chirality/runtime-client';
import {
  HostAccountAuthority,
  createHostAccountClient,
  resolveHostedProjectTokenFile,
  startControlledHostedBootstrapRuntimeHostForTests,
  type HostAccountClient,
  type HostAccountClientNativeAdmission,
  type HostAccountNativeAdmission,
  type HostedBootstrapPrivateBindings,
  type TrustedHostedLoginCeremony
} from '@chirality/runtime-daemon';

import { performHostAccountOperation } from '../../../electron/host-account-ipc';
import type {
  HostAccountDesktopOperation,
  HostAccountDesktopResult,
  HostAccountDesktopValue
} from '../../../electron/host-account-ipc-contract';
import {
  getDaemonHarnessPort,
  resetDaemonHarnessPortForTests
} from '../../lib/runtime-client/daemon-harness-port';
import * as initializeRoute from '../../app/api/harness/hosted-bootstrap/project/initialize/route';
import * as bindRoute from '../../app/api/harness/hosted-bootstrap/project/bind/route';
import * as statusRoute from '../../app/api/harness/hosted-bootstrap/status/route';
import {
  cancelHostedBootstrapLogin,
  getHostedBootstrapStatusWithRetry,
  grantHostedProviderNetworkConsent,
  hydrateHostedBootstrapProject,
  initializeHostedBootstrapProject,
  signOutHostedBootstrapProject,
  startHostedBootstrapLogin
} from '../../lib/harness/hosted-bootstrap-client';

const REPO_ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..', '..', '..', '..', '..', '..');

const SIGNING_PREDICATE = {
  schema: 'chirality.host-account-signing-predicate/v1',
  serviceName: 'com.chirality.app.runtime.account-host',
  bundleId: 'com.chirality.app',
  teamId: 'TESTTEAM01',
  peerRequirement: 'identifier "com.chirality.app" and anchor apple generic and certificate leaf[subject.OU] = TESTTEAM01'
} as const;

const cleanup: Array<() => Promise<void>> = [];
afterEach(async () => {
  for (const close of cleanup.splice(0).reverse()) await close().catch(() => undefined);
  resetDaemonHarnessPortForTests();
  vi.unstubAllGlobals();
  vi.unstubAllEnvs();
});

/**
 * In-process stand-in for the XPC transport between the App main process and
 * the daemon's account host. It forwards the exact ceremony bytes both sides
 * produce; it never fabricates a challenge, nonce, bearer, or proof.
 */
function inProcessAccountHostSeam(): {
  server: HostAccountNativeAdmission;
  client: HostAccountClientNativeAdmission;
} {
  let callbacks: Parameters<HostAccountNativeAdmission['createHostXpcServer']>[0] | undefined;
  return {
    server: {
      createHostXpcServer(input) {
        callbacks = input;
        return {
          async ping(_connectionId, ping) { return ping; },
          async closeConnection() {},
          async close() {}
        };
      }
    },
    client: {
      createHostXpcClient() {
        return {
          async provision({ requestId, onChallenge }) {
            if (!callbacks) throw new Error('account host listener is not running');
            const connectionId = `connection:${requestId}`;
            const challenge = await callbacks.onCeremonyOpen({ connectionId, requestId });
            const answer = await onChallenge({
              requestId: challenge.requestId,
              challenge: challenge.challenge,
              generation: challenge.generation
            });
            return callbacks.onCeremonyFinish({
              connectionId,
              requestId: answer.requestId,
              hostNonce: answer.hostNonce,
              proof: answer.proof
            });
          },
          async close() {}
        };
      }
    }
  };
}

type ControlledCeremony = TrustedHostedLoginCeremony & { complete(): void };

function controlledCeremony(projectId: string): ControlledCeremony {
  let state: 'pending' | 'completed' | 'failed' = 'pending';
  return {
    async start() { return { loginId: `login-${projectId}`, authUrl: `https://auth.example.test/${projectId}` }; },
    async status() { return state === 'completed' ? { state, hasAccount: true } : { state }; },
    async cancel() { state = 'failed'; },
    async close() {},
    complete() { state = 'completed'; }
  };
}

/**
 * The non-hidden catalog the controlled admission retains. Its default is the
 * fixture engine's model, as the daemon requires of a materialized catalog.
 */
const CATALOG_ENTRIES: readonly HostedModelCatalogEntry[] = [
  { model: 'fixture-model', isDefault: true, defaultReasoningEffort: 'high', supportedReasoningEfforts: ['low', 'medium', 'high'] },
  { model: 'fixture-alt', isDefault: false, defaultReasoningEffort: 'medium', supportedReasoningEfforts: ['medium', 'low'] }
];

function fixtureEngine(projectId: string): AgentEnginePort {
  const descriptor = {
    adapterId: 'codex-app-server',
    providerId: 'openai',
    capabilities: { credentials: false, tools: true, attachments: false, interruption: true, durableResume: true, compaction: false, runtimeControlTools: true }
  } as const;
  return {
    descriptor,
    subject: descriptor.adapterId,
    async preflight() {},
    async *startTurn() {
      yield { type: 'session:init', data: { engineSessionId: `${projectId}-provider`, adapterId: descriptor.adapterId, providerId: descriptor.providerId, model: 'fixture-model' } };
      yield { type: 'chat:complete', data: { text: projectId } };
      yield { type: 'process:exit', data: { exitCode: 0, interrupted: false } };
    },
    async interrupt() {}
  };
}

/** Routes renderer `fetch` calls to the production Next route handlers. */
function routeFetch(): typeof fetch {
  const handlers: Record<string, (request: Request) => Promise<Response>> = {
    'POST /api/harness/hosted-bootstrap/project/initialize': initializeRoute.POST,
    'POST /api/harness/hosted-bootstrap/project/bind': bindRoute.POST,
    'GET /api/harness/hosted-bootstrap/status': statusRoute.GET
  };
  return (async (input: string | URL | Request, init?: RequestInit) => {
    const url = new URL(String(input), 'http://localhost');
    const request = new Request(url, init);
    const handler = handlers[`${request.method} ${url.pathname}`];
    if (!handler) throw new Error(`Unrouted renderer request: ${request.method} ${url.pathname}`);
    return handler(request);
  }) as typeof fetch;
}

/** Preload's `invokeHostAccount` unwrap, with `ipcRenderer.invoke` replaced by the main-process handler body. */
function rendererAccountBridge(
  options: Parameters<typeof performHostAccountOperation>[1]
): NonNullable<NonNullable<Window['chirality']>['runtime']>['hostedAccount'] {
  // Preload returns the untyped union across the context bridge; the renderer
  // contract narrows it per operation, which the generic here mirrors.
  const invoke = async <T extends HostAccountDesktopValue>(operation: HostAccountDesktopOperation, projectRoot: string): Promise<T> => {
    const result: HostAccountDesktopResult = await performHostAccountOperation({ operation, projectRoot }, options);
    if (!result.ok) throw new Error(result.error);
    return result.value as T;
  };
  return {
    status: (projectRoot) => invoke('status', projectRoot),
    grantProviderNetworkConsent: (projectRoot) => invoke('grant-provider-network-consent', projectRoot),
    startLogin: (projectRoot) => invoke('start-login', projectRoot),
    cancelLogin: (projectRoot) => invoke('cancel-login', projectRoot),
    signOut: (projectRoot) => invoke('sign-out', projectRoot)
  };
}

describe('hosted account sequence through production code against a real daemon with an account host', () => {
  it('initializes through Next, then runs every account action through the signed account-host path', async () => {
    const root = await realpath(await mkdtemp('/tmp/app-account-sequence-'));
    cleanup.push(() => rm(root, { recursive: true, force: true }));
    const runtimeDirectory = join(root, 'runtime');
    const projectRoot = join(root, 'project');
    await mkdir(runtimeDirectory, { mode: 0o700 });
    await mkdir(projectRoot);

    const seam = inProcessAccountHostSeam();
    const ceremonies: ControlledCeremony[] = [];
    const retired: string[] = [];
    const signedOut: string[] = [];
    const bindings: HostedBootstrapPrivateBindings = {
      async createAccountHost(auth) {
        return new HostAccountAuthority({
          runtimeDirectory,
          auth,
          signingPredicate: SIGNING_PREDICATE,
          expectedEuid: process.geteuid?.() ?? 0,
          nativeAdmission: seam.server
        });
      },
      async createCeremony(input) {
        const ceremony = controlledCeremony(input.projectId);
        ceremonies.push(ceremony);
        return ceremony;
      },
      async establishAdmission(input) {
        return {
          continuity: { canonicalRoot: input.canonicalRoot, cwd: input.canonicalRoot, accountId: `private-${input.projectId}`, accountEpoch: 1, policyDigest: `policy-${input.projectId}` },
          authority: { supplierGeneration: 'supplier', identityGeneration: 'identity', snapshotDigest: 'c'.repeat(64) },
          async retire() { retired.push(input.projectId); }
        };
      },
      async materializeAdmission(input) {
        const catalog = hostedModelCatalog(CATALOG_ENTRIES);
        return { engine: fixtureEngine(input.projectId), selection: { adapterId: 'codex-app-server', providerId: 'openai', model: catalog.default.model }, catalog };
      },
      async signOut(input) { signedOut.push(input.projectId); }
    };
    const host = await startControlledHostedBootstrapRuntimeHostForTests(
      { enabled: true, runtimeDirectory, daemonSocket: 'runtime.sock', instructionRoot: await realpath(REPO_ROOT) },
      bindings
    );
    cleanup.push(() => host.stop());

    // The Desktop composition root supplies exactly these paths to its Next child.
    vi.stubEnv('CHIRALITY_RUNTIME_SOCKET_PATH', host.socketPath);
    vi.stubEnv('CHIRALITY_RUNTIME_BOOTSTRAP_TOKEN_FILE', host.bootstrapTokenFile);
    vi.stubEnv('CHIRALITY_RUNTIME_DIRECTORY', runtimeDirectory);
    resetDaemonHarnessPortForTests();

    // The main process's daemon client (registry lookups) and its verified account client.
    const mainRuntimeClient = new RuntimeClient({ socketPath: host.socketPath, tokenFile: host.bootstrapTokenFile });
    const accountClient: HostAccountClient = createHostAccountClient({
      socketPath: host.socketPath,
      signingPredicate: SIGNING_PREDICATE,
      expectedEuid: process.geteuid?.() ?? 0,
      nativeAdmission: seam.client
    });
    await accountClient.start();
    cleanup.push(() => accountClient.close());
    const ipcOptions = { runtimeClient: mainRuntimeClient, accountClient: () => accountClient };

    vi.stubGlobal('fetch', routeFetch());
    vi.stubGlobal('window', { chirality: { runtime: { hostedAccount: rendererAccountBridge(ipcOptions) } } });

    // 1. Hydration of an unregistered folder: bind says required; the signed status path says required.
    const onBoundBeforeSetup = vi.fn();
    await expect(hydrateHostedBootstrapProject(projectRoot, onBoundBeforeSetup)).resolves.toEqual({ registration: 'required' });
    expect(onBoundBeforeSetup).not.toHaveBeenCalled();

    // 2. Explicit setup through Next returns only the verified binding.
    const initialized = await initializeHostedBootstrapProject(projectRoot);
    expect(initialized).toEqual({ registration: 'registered', projectId: expect.stringMatching(/^[0-9a-f-]{36}$/u) });
    expect(initialized).not.toHaveProperty('status');
    const { projectId } = initialized;

    // The verified normal daemon port is now bound to this project.
    await expect(getDaemonHarnessPort().listRoles(projectRoot)).resolves.toMatchObject({ schemaVersion: 'chirality.roles/v3' });

    // A repeated explicit setup (manual retry after a failed status read, or a
    // re-selection) re-registers the same folder to the same project.
    await expect(initializeHostedBootstrapProject(projectRoot)).resolves.toEqual({ registration: 'registered', projectId });

    // 3. The daemon's account-proof guard is live: the ordinary clients (the exact
    //    scoped client the old port used, and the bootstrap client) are rejected.
    const scopedClient = new RuntimeClient({ socketPath: host.socketPath, tokenFile: resolveHostedProjectTokenFile(runtimeDirectory, projectId) });
    await expect(scopedClient.hostedBootstrapStatus(projectId)).rejects.toMatchObject({
      code: 'UNAUTHORIZED', status: 401, message: 'Complete App account host proof is required'
    });
    await expect(mainRuntimeClient.hostedBootstrapStatus(projectId)).rejects.toMatchObject({ code: 'UNAUTHORIZED', status: 401 });
    await expect(mainRuntimeClient.grantHostedProviderNetworkConsent(projectId)).rejects.toMatchObject({ code: 'UNAUTHORIZED', status: 401 });

    // The Next status route can only report the binding.
    const nextStatus = await (await fetch(`/api/harness/hosted-bootstrap/status?projectRoot=${encodeURIComponent(projectRoot)}`)).json();
    expect(nextStatus).toEqual({ registration: 'registered', projectId });
    expect(nextStatus).not.toHaveProperty('status');

    // 4. Status after setup goes through the signed account-host path.
    await expect(getHostedBootstrapStatusWithRetry(projectRoot)).resolves.toEqual({
      registration: 'registered', projectId,
      status: { schema: 'chirality-hosted-bootstrap-status/v1', projectId, ceremony: 'consent-required', admission: 'unavailable', canStartLogin: false }
    });

    // 5. Re-hydration (restart path) revalidates the binding and reads status the same way.
    const onBound = vi.fn();
    await expect(hydrateHostedBootstrapProject(projectRoot, onBound)).resolves.toMatchObject({
      registration: 'registered', projectId, status: { ceremony: 'consent-required', admission: 'unavailable' }
    });
    expect(onBound).toHaveBeenCalledWith({ registration: 'registered', projectId });

    // 6. Consent, login start, pending, cancel.
    await expect(grantHostedProviderNetworkConsent(projectRoot)).resolves.toMatchObject({ ceremony: 'ready-to-start', admission: 'unavailable', canStartLogin: true });
    await expect(startHostedBootstrapLogin(projectRoot)).resolves.toEqual({ loginId: `login-${projectId}`, authUrl: `https://auth.example.test/${projectId}` });
    expect(ceremonies).toHaveLength(1);
    await expect(getHostedBootstrapStatusWithRetry(projectRoot)).resolves.toMatchObject({
      registration: 'registered', projectId, status: { ceremony: 'pending', admission: 'unavailable', canStartLogin: false }
    });
    await expect(cancelHostedBootstrapLogin(projectRoot)).resolves.toMatchObject({ ceremony: 'cancelled', admission: 'unavailable', canStartLogin: true });
    await expect(getHostedBootstrapStatusWithRetry(projectRoot)).resolves.toMatchObject({
      registration: 'registered', projectId, status: { ceremony: 'cancelled', admission: 'unavailable', canStartLogin: true }
    });

    // 7. A fresh login completed through the controlled ceremony reaches signed-in and admits the engine.
    await expect(startHostedBootstrapLogin(projectRoot)).resolves.toMatchObject({ loginId: `login-${projectId}` });
    expect(ceremonies).toHaveLength(2);
    await expect(getHostedBootstrapStatusWithRetry(projectRoot)).resolves.toMatchObject({ status: { ceremony: 'pending' } });
    ceremonies[1]!.complete();
    // The ready status carries the retained catalog and its default selection
    // across the real proof-bearing path (HostAccountClient -> account host).
    await expect(getHostedBootstrapStatusWithRetry(projectRoot)).resolves.toEqual({
      registration: 'registered', projectId,
      status: {
        schema: 'chirality-hosted-bootstrap-status/v1', projectId, ceremony: 'signed-in', admission: 'ready', canStartLogin: false,
        models: CATALOG_ENTRIES.map(entry => ({ ...entry, supportedReasoningEfforts: [...entry.supportedReasoningEfforts] })),
        selection: { model: 'fixture-model', reasoningEffort: 'high' }
      }
    });

    // 8. Project-local sign-out, then status: the catalog leaves with the admission.
    await expect(signOutHostedBootstrapProject(projectRoot)).resolves.toMatchObject({ ceremony: 'consent-required', admission: 'unavailable', canStartLogin: false });
    expect(signedOut).toEqual([projectId]);
    expect(retired).toEqual([projectId]);
    await expect(getHostedBootstrapStatusWithRetry(projectRoot)).resolves.toEqual({
      registration: 'registered', projectId,
      status: { schema: 'chirality-hosted-bootstrap-status/v1', projectId, ceremony: 'consent-required', admission: 'unavailable', canStartLogin: false }
    });

    // The ordinary path stays closed for the whole sequence.
    await expect(scopedClient.hostedBootstrapStatus(projectId)).rejects.toMatchObject({ code: 'UNAUTHORIZED', status: 401 });
  }, 20_000);
});
