import { spawn, type ChildProcess } from 'node:child_process';
import { createHash } from 'node:crypto';
import { chmod, copyFile, mkdir, mkdtemp, readFile, realpath, rm, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { describe, expect, it } from 'vitest';
import { verifyExactSupply, createControlledSupplyVerifierForTests } from '../packages/core/src/exact-supply.js';
import { DescendantTracker, censusProcesses } from '../packages/core/src/descendant-tracker.js';
import { prepareCodexNativePolicy } from '../packages/daemon/src/codex-containment.js';
import { CodexTurnSession } from '../packages/daemon/src/codex-session.js';
// @ts-ignore Executable fixture intentionally has no separate declaration package.
import { startProcessProvider, processProbe } from './fixtures/process-response-provider.mjs';
const delay = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));
async function until(check: () => Promise<boolean>, ms: number) {
  const deadline = Date.now() + ms;
  while (Date.now() < deadline) { if (await check()) return; await delay(25); }
  throw new Error('Bounded observation timed out');
}
it('constructs fixed owned-PID probes without accepting arbitrary target syntax', () => {
  expect(processProbe('/fixture', 123, 'primary')).toContain('kill -USR1 123');
  expect(processProbe('/fixture', 123, 'child', true)).toContain('/bin/sleep 7');
  for (const pid of [0, -1, 1.5, '123;kill']) expect(() => processProbe('/fixture', pid, 'primary')).toThrow();
});
const safeFailure = (error: unknown) => {
  const value = error as { name?: unknown; code?: unknown };
  return { name: typeof value?.name === 'string' && /^[A-Za-z0-9_]{1,64}$/.test(value.name) ? value.name : 'Error',
    code: typeof value?.code === 'string' && /^[A-Z0-9_]{1,64}$/.test(value.code) ? value.code : 'UNCLASSIFIED' };
};
it('keeps failure diagnostics bounded without raw error bodies', () => {
  expect(safeFailure({ name: 'Error', code: 'TIMEOUT', message: 'private payload' })).toEqual({ name: 'Error', code: 'TIMEOUT' });
  expect(safeFailure({ name: 'unsafe name', code: 'secret payload' })).toEqual({ name: 'Error', code: 'UNCLASSIFIED' });
});
it('rejects invalid provider scope before opening a local listener', async () => {
  await expect(startProcessProvider({ projectRoot: '/fixture', siblingPid: 123, scenario: 'unknown' })).rejects.toThrow();
  await expect(startProcessProvider({ projectRoot: '/fixture', siblingPid: -1, scenario: 'normal' })).rejects.toThrow();
});
const enabled = process.env.CHIRALITY_RUN_EXACT_PROCESS_CONFORMANCE === '1';
describe.skipIf(!enabled)('P2 actual exact App Server process boundary, deterministic local model', () => {
  it('checks the explicitly selected bounded process profile', async () => {
    const started = Date.now();
    const scenario = process.env.CHIRALITY_EXACT_PROCESS_SCENARIO ?? 'normal';
    if (!['normal', 'cancel-primary', 'cancel-child', 'timeout-primary', 'timeout-child'].includes(scenario)) throw new Error('Unknown process scenario');
    const supplied = process.env.CHIRALITY_EXACT_CODEX_PATH, evidence = process.env.CHIRALITY_EXACT_EVIDENCE_DIR;
    if (!supplied || !evidence || process.platform !== 'darwin' || process.arch !== 'arm64') throw new Error('Explicit darwin-arm64 supply and disposable evidence required');
    const sha = process.env.CHIRALITY_EXACT_CANDIDATE_SHA256, size = process.env.CHIRALITY_EXACT_CANDIDATE_SIZE;
    if ((sha !== undefined || size !== undefined) && (!sha || !/^[a-f0-9]{64}$/.test(sha) || !size || !/^[1-9][0-9]{0,9}$/.test(size) || Number(size) > 4294967296)) throw new Error('Complete strict candidate identity required');
    const controlled = sha && size ? createControlledSupplyVerifierForTests({ sha256: sha, size: Number(size), version: 'unaccepted-candidate' }) : undefined;
    const verify = (path: string) => controlled ? controlled.verify(path) : verifyExactSupply({ executablePath: path });
    const identity = await verify(supplied);
    const base = await realpath(await mkdtemp(join(await realpath(tmpdir()), 'exact-process-')));
    const root = join(base, 'project'), broker = join(base, 'broker'), worker = join(broker, 'worker'), home = join(worker, 'home');
    for (const path of [root, broker, worker, home]) await mkdir(path, { mode: 0o700 });
    const executable = join(worker, 'app-server'); await copyFile(supplied, executable); await chmod(executable, 0o700); await verify(executable);
    const sourceFiles = ['tests/exact-process-conformance.test.ts', 'tests/fixtures/process-response-provider.mjs', 'tests/fixtures/response-provider.mjs', 'packages/daemon/src/codex-containment.ts', 'packages/daemon/src/codex-session.ts', 'packages/core/src/descendant-tracker.ts'];
    const fingerprints = async () => Object.fromEntries(await Promise.all(sourceFiles.map(async path => [path, createHash('sha256').update(await readFile(path)).digest('hex')])));
    const observations: Record<string, any> = { scenario, evidenceClass: controlled ? 'supplier-candidate-unaccepted' : 'accepted-exact-supply-local-model', accountUsed: false, supplySha256: identity.sha256, sourceBefore: await fingerprints(), verdict: 'PROFILE_NOT_COMPLETED', publicRuntimeCancellationProven: false, processScope: 'observed actual tool lineage only; no all-orphans proof' };
    let sibling: ChildProcess | undefined, host: ChildProcess | undefined, actor: CodexTurnSession | undefined, tracker: DescendantTracker | undefined;
    let policy: Awaited<ReturnType<typeof prepareCodexNativePolicy>> | undefined, provider: Awaited<ReturnType<typeof startProcessProvider>> | undefined;
    let signals = 0, siblingReady = false, hostClosed: Promise<void> | undefined, siblingClosed: Promise<void> | undefined;
    let phase = 'sibling-setup';
    const cleanupHost = async () => {
      if (host?.pid && host.exitCode === null && host.signalCode === null) { try { process.kill(-host.pid, 'SIGKILL'); } catch (error: any) { if (error.code !== 'ESRCH') throw error; } }
      if (hostClosed) await Promise.race([hostClosed, delay(8000).then(() => { throw new Error('Owned vendor group close timed out'); })]);
    };
    const watchdog = setTimeout(() => { void cleanupHost().catch(() => {}); }, 55_000);
    try {
      sibling = spawn(process.execPath, ['-e', 'process.on("SIGUSR1",()=>process.send({signal:true}));process.send({ready:true});setTimeout(()=>process.exit(0),55000);'], { cwd: broker, env: { PATH: '/usr/bin:/bin' }, stdio: ['ignore', 'ignore', 'ignore', 'ipc'] });
      siblingClosed = new Promise(resolve => sibling!.once('close', () => resolve()));
      sibling.on('message', (message: any) => { if (message.ready) siblingReady = true; if (message.signal) signals++; });
      await until(async () => siblingReady, 2000);
      sibling.kill('SIGUSR1'); await until(async () => signals === 1, 2000);
      const siblingIdentity = (await censusProcesses()).find(row => row.pid === sibling!.pid);
      if (!siblingIdentity) throw new Error('Owned sibling positive-control identity absent');
      observations.sibling = { ...siblingIdentity, positiveControlCount: signals };
      phase = 'policy-compile';
      policy = await prepareCodexNativePolicy({ canonicalRoot: root, codexHome: home, privateDirectory: worker, immutableReadRoots: ['/bin', '/usr/lib', '/System/Volumes/Preboot/Cryptexes/OS/System/Library/dyld'], protectedPaths: [broker], commandNetworkPosture: 'off' });
      observations.policyDigest = policy.policyDigest; observations.expectedPermissions = policy.expectedPermissions;
      phase = 'provider-start';
      provider = await startProcessProvider({ projectRoot: root, siblingPid: sibling.pid!, scenario });
      const config = ['model_provider="process_fixture"', 'model="runtime-deterministic"', 'model_providers.process_fixture.name="P2 deterministic local model"', `model_providers.process_fixture.base_url=${JSON.stringify(provider.baseUrl)}`, 'model_providers.process_fixture.wire_api="responses"', 'model_providers.process_fixture.requires_openai_auth=false', 'model_providers.process_fixture.supports_websockets=false', 'model_providers.process_fixture.request_max_retries=0', 'model_providers.process_fixture.stream_max_retries=0', 'features.multi_agent=true'];
      const args = await policy.launchArguments(executable);
      phase = 'vendor-spawn';
      host = spawn(args[0]!, [...args.slice(1), ...config.flatMap(value => ['-c', value])], { cwd: root, env: policy.environment, detached: true, stdio: 'pipe' });
      hostClosed = new Promise(resolve => host!.once('close', () => resolve()));
      host.on('error', () => {}); host.stderr!.on('data', () => {});
      if (!host.pid) throw new Error('Vendor PID absent');
      tracker = new DescendantTracker({ leaderPid: host.pid, intervalMs: 25, maxDurationMs: 55000 }); await tracker.start();
      actor = new CodexTurnSession({ transport: { stdin: host.stdin!, stdout: host.stdout!, close: cleanupHost }, permissionProfile: policy.permissionProfile, policyDigest: policy.policyDigest, requestTimeoutMs: 8000, turnTimeoutMs: scenario.startsWith('timeout') ? 5000 : 30000, commandNetworkPosture: 'off' });
      phase = 'initialize-policy';
      await actor.initialize(); await actor.verifyNativePolicy(policy.expectedPermissions);
      const threadId = await actor.startThread({ cwd: root, model: 'runtime-deterministic', continuityChecked: true });
      phase = 'turn-start';
      const actionStarted = Date.now();
      const turnId = await actor.startTurn({ threadId, model: 'runtime-deterministic', text: 'PROCESS_PARENT_ONLY: follow bounded deterministic process probe.' });
      const terminalPromise = actor.waitTurn(turnId).then(value => ({ value }), error => ({ error: String(error) }));
      phase = 'process-observation';
      if (scenario === 'normal') {
        const result = await terminalPromise; observations.terminal = result; expect(result).toHaveProperty('value.status', 'completed');
        for (const who of ['primary', 'child']) {
          const returned = provider.records.flatMap((record: any) => record.outputs).filter((output: any) => output.issued.who === who && output.issued.kind === 'probe');
          expect(returned.length).toBeGreaterThan(0);
          for (const output of returned) { expect(output.output).toContain('PROCESS_STARTEDFOREGROUND_CHILD_DONESIGNAL_DENIEDPROCESS_FINISHED'); expect(output.output).not.toContain('SIGNAL_BREACH'); }
        }
      } else {
        const role = scenario.endsWith('-child') ? 'child' : 'primary'; let observedPid = 0;
        await until(async () => { try { const text = await readFile(join(root, `${role}.pid`), 'utf8'); if (!/^[1-9][0-9]*\n$/.test(text)) return false; observedPid = Number(text.trim()); return true; } catch { return false; } }, 4000);
        await tracker.sample();
        const lineage = await tracker.reconcile(); const observed = [...lineage.ownedGroup, ...lineage.detached].find(row => row.pid === observedPid);
        if (!observed || observed.pid === host.pid) throw new Error('Tool marker PID lacks independently observed owned lineage');
        observations.lifetimeIdentity = observed; observations.beforeInterruption = lineage;
        if (scenario.startsWith('cancel')) await actor.interrupt(turnId);
        const terminal = await terminalPromise; observations.terminal = terminal;
        if (scenario.startsWith('cancel')) expect(terminal).toHaveProperty('value.status', 'interrupted');
        else expect(terminal).toHaveProperty('error');
        const after = await tracker.reconcile(); observations.afterInterruptionBeforeFixtureCleanup = after;
        expect([...after.ownedGroup, ...after.detached].some(row => row.pid === observedPid && row.startIdentity === observed.startIdentity)).toBe(false);
      }
      observations.actionElapsedMs = Date.now() - actionStarted;
      // Each observed completed command has its own <=10s bound; whole native pair may include multiple probes.
      for (const record of provider.records) for (const output of record.outputs) if (output.issued.kind === 'probe') expect(record.receivedAt - output.issued.issuedAt).toBeLessThanOrEqual(10000);
      if (scenario !== 'normal') expect(observations.actionElapsedMs).toBeLessThanOrEqual(10000);
      expect(signals).toBe(1); expect(provider.failures).toEqual([]);
      const siblingAfter = (await censusProcesses()).find(row => row.pid === sibling!.pid);
      expect(sibling.exitCode).toBeNull(); expect(sibling.signalCode).toBeNull();
      expect(siblingAfter).toEqual(siblingIdentity); observations.siblingAfter = siblingAfter;
      if (scenario === 'normal') {
        sibling.kill('SIGUSR1'); await until(async () => signals === 2, 2000);
        observations.siblingPostProbePositiveControl = true;
      }
      observations.verdict = 'PROFILE_PASS_NOT_FULL_G_SBX';
    } catch (error) {
      observations.failurePhase = phase; observations.failure = safeFailure(error); throw error;
    } finally {
      observations.siblingSignalCount = signals; observations.providerRecords = provider?.records; observations.providerFailures = provider?.failures;
      observations.issuedCalls = provider?.issuedCalls;
      const cleanupFailures: { phase: string; failure: ReturnType<typeof safeFailure> }[] = [];
      const cleanup = async (name: string, action: () => Promise<unknown>) => {
        try { await action(); } catch (error) { cleanupFailures.push({ phase: name, failure: safeFailure(error) }); }
      };
      await cleanup('census-before', async () => { observations.beforeFixtureCleanup = await tracker?.reconcile(); });
      await cleanup('actor-close', async () => { await actor?.close(); });
      await cleanup('vendor-group-close', cleanupHost);
      await cleanup('sibling-close', async () => {
        if (sibling && sibling.exitCode === null && sibling.signalCode === null) sibling.kill('SIGTERM');
        if (siblingClosed) await Promise.race([siblingClosed, delay(2000).then(() => { throw new Error('Owned sibling close timed out'); })]);
      });
      // No individual model/census PID is signaled. Natural 7s fixture sleep bounds uncertain descendants.
      await cleanup('observed-lineage', async () => {
        if (!tracker) return;
        try { await until(async () => { const snapshot = await tracker!.reconcile(); return snapshot.ownedGroup.length === 0 && snapshot.detached.length === 0; }, 8000); }
        catch { observations.cleanupFailure = 'Observed owned lineage remains after bounded group/natural cleanup'; }
        observations.afterFixtureCleanup = await tracker.reconcile();
      });
      await cleanup('tracker-stop', async () => { await tracker?.stop(); });
      await cleanup('provider-close', async () => { await provider?.close(); });
      await cleanup('policy-close', async () => { await policy?.cleanup(); });
      clearTimeout(watchdog);
      await cleanup('source-fingerprint', async () => { observations.sourceAfter = await fingerprints(); });
      await cleanup('supply-revalidation', async () => { observations.supplyAfter = (await verify(supplied)).sha256; });
      observations.cleanupFailures = cleanupFailures;
      observations.elapsedMs = Date.now() - started;
      if (cleanupFailures.length || observations.cleanupFailure || observations.elapsedMs > 60000 || JSON.stringify(observations.sourceBefore) !== JSON.stringify(observations.sourceAfter)) observations.verdict = 'PROFILE_FAILED_CLEANUP_TIME_OR_SOURCE_DRIFT';
      await mkdir(evidence, { recursive: true }); await writeFile(join(evidence, 'process-conformance.json'), JSON.stringify(observations, null, 2) + '\n');
      if (!observations.cleanupFailure && cleanupFailures.length === 0) await rm(base, { recursive: true, force: true });
      expect(cleanupFailures).toEqual([]); expect(observations.cleanupFailure).toBeUndefined(); expect(observations.elapsedMs).toBeLessThanOrEqual(60000); expect(observations.sourceAfter).toEqual(observations.sourceBefore);
    }
  }, 70000);
});
