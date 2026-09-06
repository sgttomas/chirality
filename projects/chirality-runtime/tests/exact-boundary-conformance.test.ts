import { spawn } from 'node:child_process';
import { createHash } from 'node:crypto';
import { chmod, copyFile, lstat, mkdir, mkdtemp, readFile, realpath, rm, symlink, writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import { expect, it } from 'vitest';
import { verifyExactSupply, createControlledSupplyVerifierForTests } from '../packages/core/src/exact-supply.js';
import { prepareCodexNativePolicy } from '../packages/daemon/src/codex-containment.js';
import { CodexTurnSession } from '../packages/daemon/src/codex-session.js';
// @ts-ignore Standalone test peer is intentionally plain executable JavaScript.
import { startBoundaryResponseProvider, summarizeBoundaryOutput } from './fixtures/boundary-response-provider.mjs';
const quote = (value: string) => "'" + value.replaceAll("'", "'\\''") + "'";
// Persist only bounded facts. Exception messages/stacks may contain supplier commands or ambient data.
function safeFailure(error: unknown) {
  return { kind: error instanceof Error ? 'Error' : 'non-Error', code: ['ENOENT', 'EACCES', 'EPERM', 'ETIMEDOUT'].includes(String((error as any)?.code)) ? String((error as any).code) : 'OTHER' };
}
function assertBoundary(observation: Record<string, unknown>, name: string, passed: boolean) {
  const assertions = (observation.assertions ??= []) as { name: string; passed: boolean }[];
  assertions.push({ name, passed });
  if (!passed) { observation.failureAssertion = name; throw new Error('BOUNDARY_ASSERTION_FAILED'); }
}
function terminalFacts(output: string) {
  return { bytes: Buffer.byteLength(output), sha256: createHash('sha256').update(output).digest('hex'), primaryCompleteMarker: /^BOUNDARY_PRIMARY_COMPLETE\r?$/m.test(output) };
}
it('retains the failed assertion and safe terminal facts without raw error/output', () => {
  const observation: Record<string, unknown> = {};
  assertBoundary(observation, 'terminal-status', true);
  expect(() => assertBoundary(observation, 'terminal-output-marker', false)).toThrow('BOUNDARY_ASSERTION_FAILED');
  expect(observation).toEqual({ assertions: [{ name: 'terminal-status', passed: true }, { name: 'terminal-output-marker', passed: false }], failureAssertion: 'terminal-output-marker' });
  expect(terminalFacts('rejected command BOUNDARY_PRIMARY_COMPLETE').primaryCompleteMarker).toBe(false);
  expect(terminalFacts('BOUNDARY_PRIMARY_COMPLETE\n').primaryCompleteMarker).toBe(true);
  expect(JSON.stringify(safeFailure(new Error('SYNTHETIC_SECRET')))).not.toContain('SYNTHETIC_SECRET');
});
it('rejects echoed command markers as primary or native execution evidence', () => {
  expect(summarizeBoundaryOutput('exec_command failed for printf BOUNDARY_primary_START', 'primary').started).toBe(false);
  expect(summarizeBoundaryOutput('BOUNDARY_child_START\nBOUNDARY_ALLOWED:PASS\nBOUNDARY_child_FINISH', 'child')).toEqual({ started: true, finished: true, values: { ALLOWED: 'PASS' } });
});
it.runIf(process.env.CHIRALITY_RUN_EXACT_BOUNDARY === '1')('P1 actual primary and native read/environment boundary', async () => {
  const started = Date.now(), supplied = process.env.CHIRALITY_EXACT_CODEX_PATH, evidenceDirectory = process.env.CHIRALITY_EXACT_EVIDENCE_DIR;
  const sha = process.env.CHIRALITY_EXACT_CANDIDATE_SHA256, size = process.env.CHIRALITY_EXACT_CANDIDATE_SIZE;
  if (!supplied || !evidenceDirectory?.startsWith('/')) throw new Error('Explicit supplier and private evidence path required');
  if ((sha === undefined) !== (size === undefined) || (sha !== undefined && (sha.length !== 64 || !/^[a-f0-9]{64}$/.test(sha) || !size || String(Number(size)) !== size || !Number.isSafeInteger(Number(size)) || Number(size) < 1 || Number(size) > 4294967296))) throw new Error('Complete bounded candidate identity required');
  const fixtureVerifier = sha ? createControlledSupplyVerifierForTests({ sha256: sha, size: Number(size), version: 'candidate-source-version-not-accepted-identity' }) : undefined;
  const verify = (path: string) => fixtureVerifier ? fixtureVerifier.verify(path) : verifyExactSupply({ executablePath: path });
  const supply = await verify(supplied);
  const base = await realpath(await mkdtemp(join(await realpath('/tmp'), 'ebc-'))), root = join(base, 'p'), broker = join(base, 'b'), worker = join(broker, 'w'), home = join(worker, 'h');
  const cleanup: (() => Promise<unknown>)[] = [() => rm(base, { recursive: true, force: true })];
  const observation: Record<string, unknown> = { schema: 'chirality-exact-boundary/v1', suite: 'P1-read-environment', evidenceClass: fixtureVerifier ? 'supplier-candidate-unaccepted' : 'accepted-supply', supplySha256: supply.sha256, supplySize: Number(supply.identity.size), accountUsed: false, modelEvidence: 'deterministic-loopback-only', passed: false, processBoundaryProven: false, roleBoundaryProven: false };
  const sourcePaths = ['tests/exact-boundary-conformance.test.ts', 'tests/fixtures/boundary-response-provider.mjs', 'tests/fixtures/response-provider.mjs', 'packages/daemon/src/codex-session.ts', 'packages/daemon/src/codex-containment.ts', 'packages/core/src/exact-supply.ts'];
  const pins = async () => Object.fromEntries(await Promise.all(sourcePaths.map(async path => [path, createHash('sha256').update(await readFile(path)).digest('hex')])));
  observation.sourcesBefore = await pins();
  let phase = 'setup';
  const assert = (name: string, passed: boolean) => { phase = `assert:${name}`; assertBoundary(observation, name, passed); };
  let inspectHost: (() => Promise<void>) | undefined;
  const ambientPrior = process.env.CHIRALITY_AMBIENT_CANARY;
  process.env.CHIRALITY_AMBIENT_CANARY = 'SYNTHETIC_PARENT_ONLY';
  try {
    await mkdir(root, { mode: 0o700 }); await mkdir(worker, { recursive: true, mode: 0o700 }); await chmod(broker, 0o700); await mkdir(home, { mode: 0o700 }); await mkdir(join(root, '.codex'), { mode: 0o700 });
    const allowed = join(root, 'allowed.txt'), foreign = join(base, 'foreign.txt'), control = join(broker, 'control.txt'), literal = join(root, 'protected.txt'), config = join(root, '.codex', 'private.txt'), alias = join(root, 'foreign-alias');
    await writeFile(allowed, 'BOUNDARY_ALLOWED_BYTES', { mode: 0o600 });
    for (const path of [foreign, control, literal, config]) await writeFile(path, 'SYNTHETIC_DENIED_BYTES', { mode: 0o600 });
    await symlink(foreign, alias);
    const startupMarker = join(root, 'startup-ran');
    await writeFile(join(worker, '.zshenv'), `printf STARTUP_RAN > ${quote(startupMarker)}\n`, { mode: 0o600 });
    const sentinelPaths = { ALLOWED: allowed, FOREIGN: foreign, BROKER: control, LITERAL: literal, CONFIG: config, ALIAS: alias, STARTUP_FILE: join(worker, '.zshenv') };
    const hostHashes = async () => Object.fromEntries(await Promise.all(Object.entries(sentinelPaths).map(async ([name, path]) => [name, createHash('sha256').update(await readFile(path)).digest('hex')])));
    observation.hostSentinelsBefore = await hostHashes();
    inspectHost = async () => {
      observation.hostSentinelsAfter = await hostHashes();
      observation.hostSentinelsUnchanged = JSON.stringify(observation.hostSentinelsBefore) === JSON.stringify(observation.hostSentinelsAfter);
      try {
        const marker = await lstat(startupMarker);
        const knownBytes = marker.isFile() && marker.size === Buffer.byteLength('STARTUP_RAN') ? (await readFile(startupMarker)).equals(Buffer.from('STARTUP_RAN')) : false;
        observation.startupMarker = { present: true, regularFile: marker.isFile(), size: marker.size, expectedSyntheticBytes: knownBytes };
        observation.startupFileExecuted = true; // Marker appearance fails closed; bytes are not disclosed.
      } catch (error) {
        if ((error as any)?.code !== 'ENOENT') throw error;
        observation.startupMarker = { present: false }; observation.startupFileExecuted = false;
      }
    };
    // Reverse-order cleanup inspects after vendor/peer closure and before base removal.
    cleanup.splice(1, 0, async () => { try { await inspectHost!(); } catch (error) { observation.hostInspectionFailure = safeFailure(error); throw error; } });
    const binary = join(worker, 'app-server'); await copyFile(supplied, binary); await chmod(binary, 0o700); await verify(binary);
    cleanup.push(async () => { await verify(binary); await verify(supplied); observation.supplyRevalidated = true; });
    const policy = await prepareCodexNativePolicy({ canonicalRoot: root, codexHome: home, privateDirectory: worker, protectedPaths: [broker, literal], immutableReadRoots: ['/bin', '/usr/lib', '/usr/bin/curl', '/private/etc/ssl/openssl.cnf', '/System/Volumes/Preboot/Cryptexes/OS/System/Library/dyld'], commandNetworkPosture: 'off' });
    cleanup.push(() => policy.cleanup()); observation.policyDigest = policy.policyDigest; observation.expectedPermissions = policy.expectedPermissions;
    const commandFor = (who: string) => [
      `printf 'BOUNDARY_${who}_START\\n'`,
      `if [ "$(/bin/cat ${quote(allowed)})" = BOUNDARY_ALLOWED_BYTES ]; then printf 'BOUNDARY_ALLOWED:PASS\\n'; else printf 'BOUNDARY_ALLOWED:FAIL\\n'; fi`,
      ...Object.entries({ FOREIGN: foreign, BROKER: control, LITERAL: literal, CONFIG: config, ALIAS: alias }).map(([name, path]) => `/bin/cat ${quote(path)} >/dev/null 2>&1; printf 'BOUNDARY_${name}:%s\\n' "$?"`),
      `if [ -z "\${CHIRALITY_AMBIENT_CANARY+x}" ]; then printf 'BOUNDARY_AMBIENT:ABSENT\\n'; else printf 'BOUNDARY_AMBIENT:PRESENT\\n'; fi`,
      `if [ -z "\${SSH_AUTH_SOCK+x}" ] && [ -z "\${OPENAI_API_KEY+x}" ]; then printf 'BOUNDARY_CREDENTIAL_ENV:ABSENT\\n'; else printf 'BOUNDARY_CREDENTIAL_ENV:PRESENT\\n'; fi`,
      `if [ "$PWD" = ${quote(root)} ]; then printf 'BOUNDARY_CWD:PASS\\n'; else printf 'BOUNDARY_CWD:FAIL\\n'; fi`,
      `if [ "$HOME" = ${quote(worker)} ]; then printf 'BOUNDARY_HOME:PASS\\n'; else printf 'BOUNDARY_HOME:FAIL\\n'; fi`,
      `if [ "$CODEX_HOME" = ${quote(home)} ]; then printf 'BOUNDARY_CODEX_HOME:PASS\\n'; else printf 'BOUNDARY_CODEX_HOME:FAIL\\n'; fi`,
      `if [ "$TMPDIR" = ${quote(policy.scratchDirectory)} ]; then printf 'BOUNDARY_TMPDIR:PASS\\n'; else printf 'BOUNDARY_TMPDIR:FAIL\\n'; fi`,
      `printf 'BOUNDARY_${who}_FINISH\\n'`
    ].join('; ');
    const peer = await startBoundaryResponseProvider({ root, commandFor }); cleanup.push(async () => { observation.probes = peer.records; observation.peerFailures = peer.failures; await peer.close(); });
    phase = 'launch'; await verify(binary);
    const launch = await policy.launchArguments(binary);
    const configOverrides = ['model_provider="runtime_deterministic"', 'model="runtime-deterministic"', 'model_providers.runtime_deterministic.name="Boundary deterministic fixture"', `model_providers.runtime_deterministic.base_url=${JSON.stringify(peer.baseUrl)}`, 'model_providers.runtime_deterministic.wire_api="responses"', 'model_providers.runtime_deterministic.requires_openai_auth=false', 'model_providers.runtime_deterministic.supports_websockets=false', 'model_providers.runtime_deterministic.request_max_retries=0', 'model_providers.runtime_deterministic.stream_max_retries=0', 'features.multi_agent=true'];
    const child = spawn(launch[0]!, [...launch.slice(1), ...configOverrides.flatMap(value => ['-c', value])], { cwd: root, env: policy.environment, detached: true, stdio: 'pipe' });
    const closed = new Promise<void>(resolve => child.once('close', () => resolve()));
    const kill = () => { if (child.pid) try { process.kill(-child.pid, 'SIGKILL'); } catch { /* owned group gone */ } };
    child.on('error', () => {}); child.once('exit', kill);
    let stderrBytes = 0; child.stderr.on('data', (bytes: Buffer) => { stderrBytes += bytes.length; if (stderrBytes > 65536) kill(); });
    const timer = setTimeout(kill, 55000);
    const close = async () => { clearTimeout(timer); kill(); await closed; observation.vendorProcessClosed = true; };
    cleanup.push(close);
    await new Promise<void>((resolve, reject) => { child.once('spawn', resolve); child.once('error', reject); });
    const actor = new CodexTurnSession({ transport: { stdin: child.stdin, stdout: child.stdout, close }, permissionProfile: policy.permissionProfile, policyDigest: policy.policyDigest, commandNetworkPosture: 'off', requestTimeoutMs: 10000, turnTimeoutMs: 45000 });
    cleanup.push(() => actor.close());
    void (async () => { for await (const _event of actor.events()) { /* bounded actor drain */ } })().catch(() => {});
    phase = 'initialize-and-policy'; await actor.initialize(); await actor.verifyNativePolicy(policy.expectedPermissions);
    const account = await actor.accountRead(); assert('account-absent', account.hasAccount === false);
    phase = 'primary-and-native-probes'; const threadId = await actor.startThread({ cwd: root, model: 'runtime-deterministic', continuityChecked: true });
    const turnId = await actor.startTurn({ threadId, model: 'runtime-deterministic', text: 'Perform the deterministic boundary probe once, then delegate the matching native child probe and finish.' });
    const terminal = await actor.waitTurn(turnId); observation.terminalStatus = terminal.status; observation.nativeChildren = actor.nativeChildren();
    observation.probes = peer.records; observation.peerFailures = peer.failures;
    observation.terminalOutput = terminalFacts(terminal.output);
    phase = 'observe-host-after-turn'; await inspectHost();
    assert('terminal-status', terminal.status === 'completed');
    assert('terminal-output-marker', (observation.terminalOutput as ReturnType<typeof terminalFacts>).primaryCompleteMarker);
    assert('peer-failures-empty', peer.failures.length === 0);
    assert('probe-count', peer.records.length === 2);
    for (const who of ['primary', 'child']) {
      const record = peer.records.find((row: any) => row.who === who);
      assert(`${who}:record`, record !== undefined);
      assert(`${who}:standalone-start-finish`, record.summary.started === true && record.summary.finished === true);
      for (const [name, value] of Object.entries({ ALLOWED: 'PASS', AMBIENT: 'ABSENT', CREDENTIAL_ENV: 'ABSENT', CWD: 'PASS', HOME: 'PASS', CODEX_HOME: 'PASS', TMPDIR: 'PASS' })) assert(`${who}:${name}`, record.summary.values[name] === value);
      for (const name of ['FOREIGN', 'BROKER', 'LITERAL', 'CONFIG', 'ALIAS']) assert(`${who}:${name}:denied`, Number(record.summary.values[name]) > 0);
      assert(`${who}:probe-budget`, record.elapsedMs <= 10000);
    }
    assert('native-child-present', actor.nativeChildren().length > 0);
    assert('startup-marker-absent', observation.startupFileExecuted === false);
    assert('host-sentinels-unchanged', observation.hostSentinelsUnchanged === true);
    observation.passed = true;
  } catch (error) { observation.failurePhase = phase; observation.failure = safeFailure(error); }
  finally {
    if (ambientPrior === undefined) delete process.env.CHIRALITY_AMBIENT_CANARY; else process.env.CHIRALITY_AMBIENT_CANARY = ambientPrior;
    let failures = 0;
    for (const fn of cleanup.reverse()) try { await fn(); } catch { failures++; }
    observation.cleanupFailures = failures; observation.sourcesAfter = await pins(); observation.sourceStable = JSON.stringify(observation.sourcesBefore) === JSON.stringify(observation.sourcesAfter);
    observation.elapsedMs = Date.now() - started; observation.profileBudgetMs = 60000; observation.probeBudgetMs = 10000;
    observation.finalizationChecks = { hostSentinelsUnchanged: observation.hostSentinelsUnchanged === true, startupMarkerAbsent: observation.startupFileExecuted === false, cleanup: failures === 0, vendorProcessClosed: observation.vendorProcessClosed === true, sourceStable: observation.sourceStable === true, supplyRevalidated: observation.supplyRevalidated === true, profileBudget: Number(observation.elapsedMs) <= 60000 };
    observation.passed = observation.passed === true && Object.values(observation.finalizationChecks as Record<string, boolean>).every(Boolean);
    await mkdir(evidenceDirectory, { recursive: true, mode: 0o700 }); await writeFile(join(evidenceDirectory, 'EXACT_BOUNDARY_P1.json'), JSON.stringify(observation, null, 2) + '\n', { mode: 0o600, flag: 'wx' });
  }
  expect(observation.passed, 'See exact bounded read/environment evidence; no aggregate conformance claim').toBe(true);
}, 75000);
