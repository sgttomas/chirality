import { spawn } from 'node:child_process';
import { createHash } from 'node:crypto';
import { chmod, copyFile, mkdir, mkdtemp, readFile, readdir, realpath, rm, writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import { expect, it } from 'vitest';
import { AuthRegistry, ProjectRegistry, DescendantTracker, verifyExactSupply } from '@chirality/runtime-core';
import { RuntimeClient } from '@chirality/runtime-client';
import { CodexSupervisor } from '../packages/daemon/src/codex-supervisor.js';
import { prepareCodexNativePolicy } from '../packages/daemon/src/codex-containment.js';
import { startSupervisorServer } from '../packages/daemon/src/supervisor-server.js';
import { startLocalDaemon, type LocalStandaloneConfig } from '../packages/daemon/src/standalone.js';
import { createProjectFixture } from './helpers.js';
// @ts-ignore Executable fixture intentionally has no generated declarations.
import { startResponseProvider } from './fixtures/response-provider.mjs';

const enabled = process.env.CHIRALITY_RUN_EXACT_MANAGED_PI === '1';
it.runIf(enabled)('exact vendor manager, real private broker/coordinator, actual Pi and resident oMLX bounded read', async () => {
  const key = process.env.CHIRALITY_OMLX_API_KEY, supplied = process.env.CHIRALITY_EXACT_CODEX_PATH, evidenceDirectory = process.env.CHIRALITY_EXACT_EVIDENCE_DIR;
  if (!key || !supplied || !evidenceDirectory?.startsWith('/')) throw new Error('Explicit parent-only memory credential, exact binary and evidence directory required');
  const accepted = await verifyExactSupply({ executablePath: supplied });
  const base = await realpath(await mkdtemp(join(await realpath('/tmp'), 'empi-')));
  const root = join(base, 'p'), broker = join(base, 'r'), worker = join(broker, 'w'), home = join(worker, 'h');
  const cleanups: (() => Promise<unknown>)[] = [() => rm(base, { recursive: true, force: true })];
  const marker = 'CHIRALITY_PI_BOUNDED_READ_7D3E', projectId = 'exact-managed-pi', model = 'Qwen3.6-35B-A3B-8bit';
  const observations: Record<string, unknown> = { schema: 'chirality-exact-managed-pi/v1', launchEvidence: 'test-only-exact-vendor-factory', managerModelEvidence: 'deterministic-loopback-Responses', hostedManagerProviderObserved: false, hostedAccountBoundaryProven: false, credentialStorage: 'memory-only', supplySha256: accepted.sha256, passed: false };
  const sourcePaths = ['packages/daemon/src/codex-supervisor.ts', 'packages/daemon/src/codex-session.ts', 'packages/daemon/src/codex-manager.ts', 'packages/daemon/src/supervisor-server.ts', 'packages/daemon/src/standalone.ts', 'packages/core/src/agent1-run-coordinator.ts', 'tests/exact-managed-pi-integration.test.ts', 'tests/fixtures/response-provider.mjs'];
  const pins = async () => Object.fromEntries(await Promise.all(sourcePaths.map(async path => [path, createHash('sha256').update(await readFile(path)).digest('hex')])));
  observations.sourcesBefore = await pins();
  let phase = 'fixture-setup';
  try {
    await mkdir(worker, { recursive: true, mode: 0o700 }); await chmod(broker, 0o700); await mkdir(home, { mode: 0o700 });
    const { manifest, manifestPath } = await createProjectFixture(root, projectId);
    manifest.enabledAdapterIds.push('codex-app-server'); await writeFile(manifestPath, JSON.stringify(manifest));
    await writeFile(join(root, 'evidence.txt'), marker, { mode: 0o600 });
    const binary = join(worker, 'app-server'); await copyFile(accepted.executablePath, binary); await chmod(binary, 0o700);
    await verifyExactSupply({ executablePath: binary });
    const policy = await prepareCodexNativePolicy({ canonicalRoot: root, codexHome: home, privateDirectory: worker, immutableReadRoots: ['/bin', '/usr/lib', '/System/Volumes/Preboot/Cryptexes/OS/System/Library/dyld'], protectedPaths: [broker] });
    cleanups.push(() => policy.cleanup());
    const provider = await startResponseProvider({ projectRoot: root, mode: 'managed-pi', managedMarker: marker }); cleanups.push(async () => {
      observations.responseRequests = provider.records.length;
      observations.modelFixtureFailureCount = provider.failures.length;
      observations.modelCallbackKinds = [...new Set(provider.records.flatMap((record: { outputs: { issued: { kind: string } }[] }) => record.outputs.map(output => output.issued.kind)))];
      await provider.close();
    });
    const identity = { canonicalRoot: root, cwd: root, accountId: 'test-only-no-account', accountEpoch: 1, policyDigest: policy.policyDigest };
    const providerConfig = ['model_provider="runtime_deterministic"', 'model="runtime-deterministic"', 'model_providers.runtime_deterministic.name="Runtime deterministic loopback"', `model_providers.runtime_deterministic.base_url=${JSON.stringify(provider.baseUrl)}`, 'model_providers.runtime_deterministic.wire_api="responses"', 'model_providers.runtime_deterministic.requires_openai_auth=false', 'model_providers.runtime_deterministic.supports_websockets=false', 'model_providers.runtime_deterministic.request_max_retries=0', 'model_providers.runtime_deterministic.stream_max_retries=0', 'model_providers.runtime_deterministic.stream_idle_timeout_ms=10000'];
    const workers = CodexSupervisor.controlledForTests({ identity, model: 'runtime-deterministic', allowUnauthenticatedModel: true, turnTimeoutMs: 210000, requestTimeoutMs: 10000, launch: async () => {
      await verifyExactSupply({ executablePath: binary });
      const launch = await policy.launchArguments(binary);
      const child = spawn(launch[0]!, [...launch.slice(1), ...providerConfig.flatMap(value => ['-c', value])], { cwd: root, env: policy.environment, detached: true, stdio: 'pipe' });
      const closed = new Promise<void>(resolve => child.once('close', () => resolve()));
      const kill = () => { if (child.pid) try { process.kill(-child.pid, 'SIGKILL'); } catch { /* already closed */ } };
      child.on('error', () => {}); child.once('exit', kill);
      let stderrBytes = 0; child.stderr.on('data', (bytes: Buffer) => { stderrBytes += bytes.length; if (stderrBytes > 65536) kill(); });
      const lifetime = setTimeout(kill, 240000);
      await new Promise<void>((resolve, reject) => { child.once('spawn', resolve); child.once('error', reject); });
      observations.vendorPid = child.pid;
      return { pid: child.pid!, permissionProfile: policy.permissionProfile, policyDigest: policy.policyDigest, expectedPermissions: policy.expectedPermissions,
        descendantTracker: new DescendantTracker({ leaderPid: child.pid!, intervalMs: 100, maxDurationMs: 300000 }),
        transport: { stdin: child.stdin, stdout: child.stdout, close: async () => { kill(); await closed; clearTimeout(lifetime); observations.vendorProcessClosed = true; } } };
    } });
    cleanups.push(() => workers.close());
    phase = 'private-supervisor';
    const server = await startSupervisorServer({ socketPath: join(broker, 's.sock'), supervisor: workers }); cleanups.push(() => server.close());
    const bindingDigest = createHash('sha256').update('test-only-exact-vendor-private-channel').digest('hex');
    await writeFile(join(broker, 's.json'), JSON.stringify({ schema: 'chirality-supervisor-credential/v1', socketPath: join(broker, 's.sock'), bindingDigest, credential: server.credential }), { mode: 0o600 });
    await new ProjectRegistry(broker, {}).register(manifestPath, { approvedBy: 'parent-authorized-fixture', approvalReference: 'AM11-exact-managed-Pi' }, 'fixture');
    const tokenFile = (await new AuthRegistry(broker).issueClient('fixture', ['runtime:read', 'sessions:read', 'sessions:write'], projectId)).tokenFile;
    const config: LocalStandaloneConfig = { schema: 'chirality-standalone/v1', mode: 'local-engine-only', runtimeDirectory: broker, daemonSocket: 'd.sock', project: { projectId, canonicalRoot: root }, manager: { kind: 'codex-supervisor', supervisorSocket: 's.sock', supervisorCredential: 's.json', bindingDigest, model: 'runtime-deterministic' }, engine: { baseUrl: 'http://127.0.0.1:8000/v1', model: { id: model, contextWindow: 32768, maxTokens: 2048 }, credentialFile: 'unused-memory.json', approvalReference: 'parent-authorized-AM11-live-Pi', turnTimeoutMs: 180000 } };
    phase = 'local-daemon-residency';
    const daemon = await startLocalDaemon(config, { async get(id) { return id === 'omlx' ? key : undefined; }, async status() { return { configured: true }; } }); cleanups.push(() => daemon.close());
    const client = new RuntimeClient({ socketPath: daemon.socketPath, tokenFile });
    phase = 'governed-manager-run';
    const stream = await client.runAgent1(projectId, { brief: 'Delegate the authorized file read and review its returned marker.', approvalReference: 'parent-authorized-AM11-full-composition', localModel: model, readOnlyTool: { name: 'read_file', relativePath: 'evidence.txt' } });
    let markerObserved = false;
    for await (const frame of stream) {
      if (JSON.stringify(frame).includes(marker)) markerObserved = true;
      const event = frame as unknown as { type?: string; data?: Record<string, unknown> };
      if (event.type === 'turn:error') observations.turnError = { type: typeof event.data?.errorType === 'string' && /^[A-Z_]{1,64}$/.test(event.data.errorType) ? event.data.errorType : 'OTHER', phase: event.data?.phase === 'pre-stream' ? 'pre-stream' : 'mid-stream' };
    }
    const sessions = await client.listSessions(projectId), parent = sessions.find(s => s.role === 'agent1'), child = sessions.find(s => s.role === 'agent2');
    const replay = child ? JSON.stringify(await client.replaySession(projectId, child.sessionId)) : '';
    const boundedReadObserved = replay.includes('"tool.completed"') && replay.includes('read_file');
    const runRoot = join(root, 'execution/_Coordination/AgentRuns/runtime'), names = await readdir(runRoot);
    const record = names.length === 1 ? JSON.parse(await readFile(join(runRoot, names[0]!, 'run.json'), 'utf8')) : undefined;
    const reviewed = record?.review?.decision === 'accepted' && child?.parentSessionId === parent?.sessionId;
    Object.assign(observations, { markerObserved, boundedReadObserved, reviewed, parentStatus: parent?.status, childStatus: child?.status, responseRequests: provider.records.length, modelFixtureFailureCount: provider.failures.length });
    observations.passed = markerObserved && boundedReadObserved && reviewed && parent?.status === 'completed' && child?.status === 'completed' && provider.failures.length === 0;
    await expect(readFile(join(broker, 'unused-memory.json'))).rejects.toMatchObject({ code: 'ENOENT' });
    await verifyExactSupply({ executablePath: supplied }); observations.supplyRevalidated = true;
  } catch { observations.failurePhase = phase; }
  finally {
    let cleanupFailures = 0;
    for (const cleanup of cleanups.reverse()) try { await cleanup(); } catch { cleanupFailures++; }
    observations.cleanupFailures = cleanupFailures;
    observations.sourcesAfter = await pins();
    observations.sourceStable = JSON.stringify(observations.sourcesBefore) === JSON.stringify(observations.sourcesAfter);
    observations.passed = observations.passed === true && cleanupFailures === 0 && observations.sourceStable === true && observations.vendorProcessClosed === true;
    await mkdir(evidenceDirectory, { recursive: true, mode: 0o700 });
    await writeFile(join(evidenceDirectory, 'EXACT_MANAGED_PI.json'), JSON.stringify(observations, null, 2) + '\n', { mode: 0o600, flag: 'wx' });
  }
  expect(observations.passed, 'See sanitized EXACT_MANAGED_PI.json; this is not hosted-manager model or account proof').toBe(true);
}, 270000);
