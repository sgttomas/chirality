import { spawn } from 'node:child_process';
import { createHash } from 'node:crypto';
import { createServer } from 'node:http';
import { gunzipSync } from 'node:zlib';
import { chmod, copyFile, mkdir, mkdtemp, readFile, realpath, rm, writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import { expect, it } from 'vitest';
import { createControlledSupplyVerifierForTests, verifyExactSupply } from '../packages/core/src/exact-supply.js';
import { CodexSupervisor } from '../packages/daemon/src/codex-supervisor.js';
import { prepareCodexNativePolicy } from '../packages/daemon/src/codex-containment.js';
import { AuthRegistry, EngineRegistry, ProjectRegistry, ResidencyCoordinator, RuntimeService, SessionStore, TurnCoordinator, DescendantTracker } from '@chirality/runtime-core';
import { RuntimeClient } from '@chirality/runtime-client';
import { RuntimeDaemon } from '../packages/daemon/src/runtime-daemon.js';
import { DelegatedRuntime } from '@chirality/runtime-core';
import { HostedConsentStore } from '@chirality/runtime-core';
import { WorkerRetirementCoordinator } from '@chirality/runtime-core';
import { createProjectFixture } from './helpers.js';
import { startSupervisorServer, SupervisorClient } from '../packages/daemon/src/supervisor-server.js';

const roles = ['untyped', 'agent0', 'agent1', 'agent2', 'task'] as const;
function nativeTool(tools: any[], names: string[]) {
  const flattened = tools.flatMap(tool => tool.type === 'namespace' && Array.isArray(tool.tools) ? tool.tools.map((member: any) => ({ ...member, namespace: tool.name })) : [tool]);
  const tool = flattened.find(tool => tool.type === 'function' && names.includes(tool.name));
  if (!tool?.parameters) throw new Error('Advertised native tool absent');
  return tool;
}
it('preserves native namespace and refuses an invented native function', () => {
  expect(nativeTool([{ type: 'namespace', name: 'agents', tools: [{ type: 'function', name: 'spawn_agent', parameters: {} }] }], ['spawn_agent']).namespace).toBe('agents');
  expect(() => nativeTool([], ['spawn_agent'])).toThrow();
});

it.runIf(process.env.CHIRALITY_RUN_EXACT_ROLE === '1')('actual public role parity and native descent without implicit Chirality role assignment', async () => {
  const started = Date.now(), supplied = process.env.CHIRALITY_EXACT_CODEX_PATH, evidence = process.env.CHIRALITY_EXACT_EVIDENCE_DIR;
  const sha = process.env.CHIRALITY_EXACT_CANDIDATE_SHA256, size = process.env.CHIRALITY_EXACT_CANDIDATE_SIZE;
  if (!supplied || !evidence?.startsWith('/')) throw new Error('Explicit exact supplier and fresh evidence directory required');
  if ((sha === undefined) !== (size === undefined) || (sha !== undefined && (!/^[a-f0-9]{64}$/.test(sha) || !size || String(Number(size)) !== size || !Number.isSafeInteger(Number(size)) || Number(size) < 1 || Number(size) > 4294967296))) throw new Error('Exact candidate hash and size required');
  const controlled = sha ? createControlledSupplyVerifierForTests({ sha256: sha, size: Number(size), version: 'candidate-source-version-not-accepted-identity' }) : undefined;
  const verify = (path: string) => controlled ? controlled.verify(path) : verifyExactSupply({ executablePath: path });
  const supply = await verify(supplied);
  const base = await realpath(await mkdtemp(join(await realpath('/tmp'), 'erc-'))), root = join(base, 'p'), broker = join(base, 'r'), worker = join(broker, 'w'), home = join(worker, 'h');
  const cleanups: (() => Promise<unknown>)[] = [() => rm(base, { recursive: true, force: true })];
  const result: Record<string, any> = { schema: 'chirality-exact-role/v1', evidenceClass: controlled ? 'supplier-candidate-unaccepted' : 'accepted-supply', supplySha256: supply.sha256, accountUsed: false, launchEvidence: 'test-only-no-account-exact-vendor-factory', roleObedienceProven: false, roleMechanicallyEnforced: false, ownerLiveProof: false, passed: false, probes: [] };
  const sourcePaths = ['tests/exact-role-conformance.test.ts', 'packages/core/src/delegated-runtime.ts', 'packages/core/src/role-policy.ts', 'packages/daemon/src/codex-session.ts', 'packages/daemon/src/codex-supervisor.ts', 'packages/daemon/src/codex-containment.ts'];
  const pins = async () => Object.fromEntries(await Promise.all(sourcePaths.map(async path => [path, createHash('sha256').update(await readFile(path)).digest('hex')])));
  result.sourcesBefore = await pins();
  let modelRequests = 0, processes = 0, closedProcesses = 0, childObserved = false;
  const calls = new Map<string, 'spawn' | 'wait'>();
  const searches = new Map<string, 'spawn' | 'wait'>();
  try {
    const { manifestPath } = await createProjectFixture(root, 'role-project');
    await mkdir(worker, { recursive: true, mode: 0o700 }); await chmod(broker, 0o700); await mkdir(home, { mode: 0o700 });
    const peer = createServer(async (req, res) => {
      try {
        if (req.method !== 'POST' || req.url !== '/v1/responses' || req.headers.authorization) throw new Error('Unexpected local peer request');
        const chunks: Buffer[] = []; let bytes = 0;
        for await (const raw of req) { const chunk = Buffer.from(raw); bytes += chunk.length; if (bytes > 2000000) throw new Error('Peer bound'); chunks.push(chunk); }
        const raw = Buffer.concat(chunks), body = JSON.parse((req.headers['content-encoding'] === 'gzip' ? gunzipSync(raw, { maxOutputLength: 4000000 }) : raw).toString());
        if (++modelRequests > 20 || !Array.isArray(body.input) || !Array.isArray(body.tools)) throw new Error('Peer shape');
        const userText = JSON.stringify(body.input.filter((item: any) => item.role === 'user').at(-1)?.content ?? '');
        const child = userText.includes('ROLE_NATIVE_CHILD_ONLY'), nativeParent = !child && userText.includes('ROLE_NATIVE_PARENT');
        if (child) childObserved = true;
        let item: any = { type: 'message', id: `msg_${modelRequests}`, role: 'assistant', status: 'completed', content: [{ type: 'output_text', text: child ? 'ROLE_CHILD_FINISHED' : 'ROLE_PRIMARY_FINISHED', annotations: [] }] };
        if (nativeParent) {
          const outputs = body.input.filter((entry: any) => entry.type === 'function_call_output' && calls.has(entry.call_id));
          const spawned = outputs.find((entry: any) => calls.get(entry.call_id) === 'spawn'), waited = outputs.find((entry: any) => calls.get(entry.call_id) === 'wait');
          if (waited) { if (!JSON.stringify(waited.output).includes('ROLE_CHILD_FINISHED')) throw new Error('Actual native child did not finish'); result.nativeWaitCompleted = true; }
          else {
            const kind = spawned ? 'wait' : 'spawn';
            const discovered = body.input.filter((entry: any) => entry.type === 'tool_search_output' && searches.has(entry.call_id) && entry.execution === 'client' && entry.status === 'completed' && Array.isArray(entry.tools)).flatMap((entry: any) => entry.tools).slice(0, 64);
            let tool: any;
            try { tool = nativeTool([...body.tools, ...discovered], spawned ? ['wait_agent', 'wait'] : ['spawn_agent']); } catch {
              if (!body.tools.some((entry: any) => entry.type === 'tool_search' && entry.execution === 'client') || [...searches.values()].includes(kind)) throw new Error('Native function absent after bounded search');
              const call_id = `search_${modelRequests}`; searches.set(call_id, kind);
              item = { type: 'tool_search_call', call_id, execution: 'client', arguments: { query: `${kind} agent`, limit: 1 } };
            }
            if (tool) {
            let args: Record<string, unknown>;
            if (!spawned) args = { message: 'ROLE_NATIVE_CHILD_ONLY: return the deterministic child marker.' };
            else { const value = JSON.parse(spawned.output), id = value.agent_id ?? value.id; if (typeof id !== 'string' || id.length > 256) throw new Error('Actual native child ID absent'); result.nativeChildId = id; args = { [tool.name === 'wait_agent' ? 'targets' : 'ids']: [id] }; }
            if ((tool.parameters.required ?? []).some((key: string) => !(key in args)) || Object.keys(args).some(key => !tool.parameters.properties?.[key])) throw new Error('Unknown native schema');
            const callId = `native_${modelRequests}`; calls.set(callId, spawned ? 'wait' : 'spawn');
            item = { type: 'function_call', id: `fc_${modelRequests}`, call_id: callId, name: tool.name, ...(tool.namespace ? { namespace: tool.namespace } : {}), arguments: JSON.stringify(args), status: 'completed' };
            }
          }
        }
        const response = { id: `resp_${modelRequests}`, object: 'response', model: 'runtime-deterministic', status: 'completed', output: [item], usage: { input_tokens: 1, output_tokens: 1, total_tokens: 2 } };
        const frames = [{ type: 'response.created', response: { ...response, status: 'in_progress', output: [] } }, { type: 'response.output_item.added', output_index: 0, item: { ...item, ...(item.type === 'function_call' ? { arguments: '' } : item.type === 'tool_search_call' ? {} : { content: [] }) } }, ...(item.type === 'function_call' ? [{ type: 'response.function_call_arguments.delta', item_id: item.id, output_index: 0, delta: item.arguments }, { type: 'response.function_call_arguments.done', item_id: item.id, output_index: 0, arguments: item.arguments }] : []), { type: 'response.output_item.done', output_index: 0, item }, { type: 'response.completed', response }];
        res.writeHead(200, { 'Content-Type': 'text/event-stream' }).end(frames.map((frame, sequence_number) => `event: ${frame.type}\ndata: ${JSON.stringify({ ...frame, sequence_number, response_id: response.id })}\n\n`).join(''));
      } catch { result.peerFailure = true; res.writeHead(400).end('{}'); }
    });
    await new Promise<void>(resolve => peer.listen(0, '127.0.0.1', resolve)); cleanups.push(() => new Promise<void>(resolve => { peer.closeAllConnections(); peer.close(() => resolve()); }));
    const binary = join(worker, 'app-server'); await copyFile(supplied, binary); await chmod(binary, 0o700);
    const policy = await prepareCodexNativePolicy({ canonicalRoot: root, codexHome: home, privateDirectory: worker, protectedPaths: [broker], immutableReadRoots: ['/bin', '/usr/lib', '/usr/bin/curl', '/System/Volumes/Preboot/Cryptexes/OS/System/Library/dyld'], commandNetworkPosture: 'off' });
    cleanups.push(() => policy.cleanup()); result.nativePolicyDigest = policy.policyDigest;
    const identity = { canonicalRoot: root, cwd: root, accountId: 'no-account-test', accountEpoch: 1, policyDigest: policy.policyDigest };
    const workers = CodexSupervisor.controlledForTests({ commandNetworkPosture: 'off', allowUnauthenticatedModel: true, identity, model: 'runtime-deterministic', requestTimeoutMs: 10000, turnTimeoutMs: 10000, launch: async () => {
      await verify(binary); const launch = await policy.launchArguments(binary);
      const config = ['model_provider="runtime_deterministic"', 'model="runtime-deterministic"', 'model_providers.runtime_deterministic.name="Owned deterministic peer"', `model_providers.runtime_deterministic.base_url="http://127.0.0.1:${(peer.address() as { port: number }).port}/v1"`, 'model_providers.runtime_deterministic.wire_api="responses"', 'model_providers.runtime_deterministic.requires_openai_auth=false', 'model_providers.runtime_deterministic.supports_websockets=false', 'model_providers.runtime_deterministic.stream_max_retries=0', 'model_providers.runtime_deterministic.request_max_retries=0', 'features.multi_agent=true'];
      const child = spawn(launch[0]!, [...launch.slice(1), ...config.flatMap(value => ['-c', value])], { cwd: root, env: policy.environment, detached: true, stdio: 'pipe' }); processes++;
      const closed = new Promise<void>(resolve => child.once('close', () => { closedProcesses++; resolve(); }));
      const kill = () => { if (child.pid) try { process.kill(-child.pid, 'SIGKILL'); } catch {} }; child.on('error', () => {}); child.once('exit', kill);
      let bytes = 0; child.stderr.on('data', (chunk: Buffer) => { bytes += chunk.length; if (bytes > 65536) kill(); });
      const timer = setTimeout(kill, Math.max(1, Math.min(12000, 60000 - (Date.now() - started))));
      try { await new Promise<void>((resolve, reject) => { child.once('spawn', resolve); child.once('error', reject); }); } catch { clearTimeout(timer); kill(); await closed; throw new Error('Candidate did not spawn'); }
      return { pid: child.pid!, descendantTracker: new DescendantTracker({ leaderPid: child.pid!, intervalMs: 100, maxDurationMs: 60000 }), permissionProfile: policy.permissionProfile, policyDigest: policy.policyDigest, expectedPermissions: policy.expectedPermissions, transport: { stdin: child.stdin, stdout: child.stdout, close: async () => { clearTimeout(timer); kill(); await closed; } } };
    } });
    cleanups.push(() => workers.close());
    const server = await startSupervisorServer({ socketPath: join(broker, 's.sock'), supervisor: workers }); cleanups.push(() => server.close());
    const supervisor = new SupervisorClient({ socketPath: join(broker, 's.sock'), credential: server.credential });
    const compatibility = { compatibilityIdentity: 'exact-role-test', contractBasisSha256: createHash('sha256').update('exact-role-test-only').digest('hex') };
    const consent = new HostedConsentStore({ canonicalRoot: root, codexHome: home });
    const actual = { adapterId: 'codex', providerId: 'runtime_deterministic', model: 'runtime-deterministic' };
    const delegated = new DelegatedRuntime({ daemonId: 'exact-role-test', projects: new Map([['role-project', { identity, compatibility, supervisor, consent, retirement: new WorkerRetirementCoordinator({ directory: join(broker, 'retirement') }), commandNetworkPosture: 'off', actual, evidenceClass: 'provider-observed' as const }]]) });
    const directory = join(broker, 'runtime'), projects = new ProjectRegistry(directory), sessions = new SessionStore(directory, projects), engines = new EngineRegistry(), residency = new ResidencyCoordinator({ async listStatus() { return []; }, async load() {}, async unload() {} }, directory);
    const service = new RuntimeService(projects, sessions, engines, residency, new TurnCoordinator(projects, sessions, engines, residency), new AuthRegistry(directory), { async get() { return undefined; }, async status() { return { configured: false }; }, async set() {}, async remove() {} });
    const registered = await service.registerProject(manifestPath, 'fixture-operator', 'exact-role-fixture-only');
    const daemon = new RuntimeDaemon({ socketPath: join(broker, 'd.sock'), runtimeDirectory: directory, service, delegated }); await daemon.start(); cleanups.push(() => daemon.stop());
    const client = new RuntimeClient({ socketPath: join(broker, 'd.sock'), tokenFile: registered.tokenFile });
    expect((await client.delegatedCapabilities('role-project')).offeredRoles).toEqual([...roles]);
    await client.grantDelegatedConsent('role-project', compatibility, { posture: 'off', approvedBy: 'fixture-operator', explicitUserAct: true });
    const initialProcesses = processes;
    await expect(client.runDelegatedTurn('other-project', compatibility, { turnId: 'forbidden', prompt: 'none' })).rejects.toThrow();
    await expect(client.runDelegatedTurn('role-project', { ...compatibility, contractBasisSha256: '0'.repeat(64) }, { turnId: 'bad-basis', prompt: 'none' })).rejects.toThrow();
    expect(processes).toBe(initialProcesses); result.scopeFences = true;
    let settings: unknown;
    for (const role of roles) {
      if (Date.now() - started > 50000) throw new Error('Profile budget');
      const before = Date.now();
      const response = await client.runDelegatedTurn('role-project', compatibility, { turnId: `role-${role}`, prompt: role === 'agent1' ? 'ROLE_NATIVE_PARENT: run the deterministic native child then finish.' : 'ROLE_PRIMARY_ONLY: return the deterministic primary marker.', ...(role === 'untyped' ? {} : { requestedRole: role }) });
      expect(response.terminal.outcome).toBe('completed'); expect(response.roleEvidence.selectedRole).toBe(role); expect(response.roleEvidence.offeredRoles).toEqual([...roles]);
      expect(response.roleEvidence.enforcementLabel).toBe('role not mechanically enforced'); expect(response.roleEvidence.evidencePosture).toBe('instruction-asserted'); expect(response.roleEvidence.actual).toEqual(actual);
      const extended = response.roleEvidence as typeof response.roleEvidence & { nativeDescendant?: boolean; settings?: unknown };
      expect(extended.nativeDescendant).toBe(false); expect(extended.settings).toBeDefined();
      if (settings === undefined) settings = extended.settings; else expect(extended.settings).toEqual(settings);
      if (role === 'agent1') { result.primaryThreadId = response.terminal.threadId; expect(typeof result.primaryThreadId).toBe('string'); expect(result.nativeChildId).not.toBe(result.primaryThreadId); }
      const elapsedMs = Date.now() - before; result.probes.push({ role, elapsedMs, roleEvidence: response.roleEvidence, outcome: response.terminal.outcome, nativePolicyDigest: policy.policyDigest }); expect(elapsedMs).toBeLessThanOrEqual(10000);
    }
    expect(childObserved && result.nativeWaitCompleted === true && typeof result.nativeChildId === 'string').toBe(true);
    result.nativeDescentDidNotAssignRuntimeRole = result.probes.find((probe: any) => probe.role === 'agent1').roleEvidence.selectedRole === 'agent1';
    await verify(binary); await verify(supplied); result.supplyRevalidated = true; result.passed = true;
  } catch (error) { result.failure = error instanceof Error ? error.message.slice(0, 400) : 'unclassified'; }
  finally {
    let failures = 0; for (const cleanup of cleanups.reverse()) try { await cleanup(); } catch { failures++; }
    result.cleanupFailures = failures; result.processes = processes; result.closedProcesses = closedProcesses; result.modelRequests = modelRequests; result.childObserved = childObserved; result.elapsedMs = Date.now() - started; result.profileBudgetMs = 60000; result.probeBudgetMs = 10000; result.sourcesAfter = await pins(); result.sourceStable = JSON.stringify(result.sourcesBefore) === JSON.stringify(result.sourcesAfter);
    result.passed = result.passed && failures === 0 && processes === closedProcesses && result.elapsedMs <= 60000 && result.sourceStable && !result.peerFailure;
    await mkdir(evidence, { recursive: true, mode: 0o700 }); await writeFile(join(evidence, 'EXACT_ROLE_CANARY.json'), JSON.stringify(result, null, 2) + '\n', { mode: 0o600, flag: 'wx' });
  }
  expect(result.passed, 'Exact role fixture failed; inspect calibrated evidence').toBe(true);
}, 70000);
