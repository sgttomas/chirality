import { spawn } from 'node:child_process';
import { createHash } from 'node:crypto';
import { PassThrough } from 'node:stream';
import { chmod, copyFile, mkdir, mkdtemp, readFile, realpath, rm, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { describe, expect, it } from 'vitest';
import { verifyExactSupply, createControlledSupplyVerifierForTests } from '../packages/core/src/exact-supply.js';
import { prepareCodexNativePolicy } from '../packages/daemon/src/codex-containment.js';
import { CodexTurnSession, type CodexDynamicTool } from '../packages/daemon/src/codex-session.js';
// This fixture substitutes the model endpoint, never the vendor App Server.
// @ts-ignore .mjs fixture is intentionally executable independently of TypeScript builds.
import { startResponseProvider, nativeSearch, discoveredTools } from './fixtures/response-provider.mjs';

it('discovers deferred native tools through source-shaped client search and only its completed output', () => {
  const issued = new Map();
  const request = nativeSearch([{ type: 'tool_search', execution: 'client' }], issued, 'primary', 'spawn', 3);
  expect(request).toEqual({ type: 'tool_search_call', call_id: 'fixture_search_3', execution: 'client', arguments: { query: 'spawn agent', limit: 1 } });
  expect(() => nativeSearch([{ type: 'tool_search', execution: 'client' }], issued, 'primary', 'spawn', 4)).toThrow();
  expect(() => nativeSearch([], new Map(), 'primary', 'spawn', 1)).toThrow();
  const namespace = { type: 'namespace', name: 'multi_agent_v1', tools: [{ type: 'function', name: 'spawn_agent', parameters: { type: 'object' } }] };
  const output = { type: 'tool_search_output', call_id: request.call_id, execution: 'client', status: 'completed', tools: [namespace] };
  expect(discoveredTools([output], issued)).toEqual([namespace]);
  expect(discoveredTools([{ ...output, call_id: 'unissued' }, { ...output, execution: 'server' }, { ...output, status: 'pending' }], issued)).toEqual([]);
});

it('bounds the local fake Responses peer and captures schemas without retaining prompts', async () => {
  const provider = await startResponseProvider({ projectRoot: '/fixture/project', foreignCanary: '/fixture/foreign', brokerCanary: '/fixture/broker', mode: 'discover' });
  try {
    const response = await fetch(`${provider.baseUrl}/responses`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ stream: true, input: [{ role: 'user', content: [{ type: 'input_text', text: 'PRIVATE_TEST_PROMPT' }] }], tools: [] }) });
    expect(response.status).toBe(200);
    expect(await response.text()).toContain('response.completed');
    expect(JSON.stringify(provider.records)).not.toContain('PRIVATE_TEST_PROMPT');
    const refused = await fetch(`${provider.baseUrl}/responses`, { method: 'POST', headers: { Authorization: 'fixture-must-not-be-used' }, body: '{}' });
    expect(refused.status).toBe(400);
  } finally { await provider.close(); }
});

it('uses observed namespace call fields and stages shell diagnostics before descendant dispatch', async () => {
  const provider = await startResponseProvider({ projectRoot: '/fixture/project', foreignCanary: '/fixture/foreign', brokerCanary: '/fixture/broker' });
  const fn = (name: string, properties: Record<string, unknown>, required: string[] = []) => ({ type: 'function', name, parameters: { type: 'object', properties, required } });
  const tools = [fn('exec_command', { cmd: { type: 'string' }, shell: { type: 'string' } }, ['cmd']), { type: 'namespace', name: 'multi_agent_v1', tools: [fn('spawn_agent', { message: { type: 'string' } }), fn('wait_agent', { targets: { type: 'array' } }, ['targets'])] }];
  const input: unknown[] = [{ role: 'user', content: 'DETERMINISTIC_PARENT_ONLY' }];
  try {
    for (const expected of ['baseline', 'shell', 'spawn', 'wait']) {
      const response = await fetch(`${provider.baseUrl}/responses`, { method: 'POST', body: JSON.stringify({ stream: true, tools, input }) });
      expect(response.status).toBe(200);
      const frames = (await response.text()).split('\n').filter(line => line.startsWith('data: ')).map(line => JSON.parse(line.slice(6)));
      const call = frames.find(frame => frame.type === 'response.output_item.done').item;
      if (expected === 'baseline') expect(JSON.parse(call.arguments).cmd).toContain('BASELINE_SHELL_OK');
      if (expected === 'spawn' || expected === 'wait') expect(call.namespace).toBe('multi_agent_v1');
      else expect(call.namespace).toBeUndefined();
      if (expected === 'wait') { expect(call.name).toBe('wait_agent'); expect(JSON.parse(call.arguments)).toEqual({ targets: ['fixture-child'] }); }
      input.push(call, { type: 'function_call_output', call_id: call.call_id, output: expected === 'spawn' ? JSON.stringify({ agent_id: 'fixture-child' }) : 'fixture-output' });
    }
    expect(provider.failures).toEqual([]);
  } finally { await provider.close(); }
});

it('selects only the advertised harmless dynamic review tool and verifies its result marker', async () => {
  const provider = await startResponseProvider({ projectRoot: '/fixture/project', foreignCanary: '/fixture/foreign', brokerCanary: '/fixture/broker', mode: 'dynamic' });
  const tools = [{ type: 'namespace', name: 'fixture_dynamic', tools: [{ type: 'function', name: 'review', parameters: { type: 'object', properties: { text: { type: 'string' } }, required: ['text'], additionalProperties: false } }] }];
  const input: unknown[] = [{ role: 'user', content: 'DETERMINISTIC_PARENT_ONLY' }];
  try {
    const response = await fetch(`${provider.baseUrl}/responses`, { method: 'POST', body: JSON.stringify({ stream: true, tools, input }) });
    expect(response.status).toBe(200);
    const frames = (await response.text()).split('\n').filter(line => line.startsWith('data: ')).map(line => JSON.parse(line.slice(6)));
    const call = frames.find(frame => frame.type === 'response.output_item.done').item;
    expect(call.name).toBe('review'); expect(call.namespace).toBe('fixture_dynamic'); expect(JSON.parse(call.arguments)).toEqual({ text: 'DETERMINISTIC_DYNAMIC_INPUT' });
    input.push(call, { type: 'function_call_output', call_id: call.call_id, output: 'DETERMINISTIC_DYNAMIC_REVIEWED' });
    const terminal = await fetch(`${provider.baseUrl}/responses`, { method: 'POST', body: JSON.stringify({ stream: true, tools, input }) });
    expect(terminal.status).toBe(200); expect(await terminal.text()).toContain('DETERMINISTIC_DYNAMIC_COMPLETE'); expect(provider.failures).toEqual([]);
  } finally { await provider.close(); }
});

it('sequences managed delegation and review using returned child identity and marker', async () => {
  const provider = await startResponseProvider({ projectRoot: '/fixture', mode: 'managed-pi' });
  const tools = [
    { type: 'function', name: 'delegate_agent', parameters: { type: 'object', properties: { sealedBrief: { type: 'string' } }, required: ['sealedBrief'] } },
    { type: 'function', name: 'review', parameters: { type: 'object', properties: { childSessionId: { type: 'string' }, decision: { type: 'string' }, rationale: { type: 'string' } }, required: ['childSessionId', 'decision', 'rationale'] } }
  ];
  const input: unknown[] = [{ role: 'user', content: 'fixture' }];
  try {
    for (const expected of ['delegate_agent', 'review', 'complete']) {
      const response = await fetch(`${provider.baseUrl}/responses`, { method: 'POST', body: JSON.stringify({ stream: true, tools, input }) });
      expect(response.status).toBe(200);
      const frames = (await response.text()).split('\n').filter(line => line.startsWith('data: ')).map(line => JSON.parse(line.slice(6)));
      const item = frames.find(frame => frame.type === 'response.output_item.done').item;
      if (expected === 'complete') { expect(JSON.stringify(item)).toContain('DETERMINISTIC_MANAGED_PI_COMPLETE'); continue; }
      expect(item.name).toBe(expected);
      if (expected === 'review') expect(JSON.parse(item.arguments)).toMatchObject({ childSessionId: 'real-returned-child', decision: 'accepted' });
      input.push(item, { type: 'function_call_output', call_id: item.call_id, output: JSON.stringify(expected === 'delegate_agent' ? { childSessionId: 'real-returned-child', returnText: 'CHIRALITY_PI_BOUNDED_READ_7D3E' } : { reviewed: true }) });
    }
    expect(provider.failures).toEqual([]);
  } finally { await provider.close(); }
});

const scrubStderr = (value: string): string => value
  .replace(/\bBearer\s+[^\s"']+/gi, 'Bearer [REDACTED]')
  .replace(/\bsk-[A-Za-z0-9_-]{8,}/g, '[REDACTED_KEY]')
  .replace(/((?:access_token|refresh_token|id_token|api[_-]?key|authorization)["']?\s*[:=]\s*)["']?[^\s,"'}]+["']?/gi, '$1[REDACTED]');
it('scrubs credential-shaped stderr while retaining launch diagnostics', () => {
  const scrubbed = scrubStderr('unknown subcommand; Bearer fixture-bearer-secret api_key=fixture-key refresh_token="fixture-refresh" sk-fixtureSecret0123');
  expect(scrubbed).toContain('unknown subcommand');
  for (const secret of ['fixture-bearer-secret', 'fixture-key', 'fixture-refresh', 'sk-fixtureSecret0123']) expect(scrubbed).not.toContain(secret);
});
function commandPosture(value: string | undefined): 'off' | 'ask-per-destination' | 'on' {
  if (value === undefined) return 'off';
  if (value === 'off' || value === 'ask-per-destination' || value === 'on') return value;
  throw new Error('CHIRALITY_EXACT_COMMAND_POSTURE must be off, ask-per-destination or on');
}
it('validates the trusted exact command posture without silently widening defaults', () => {
  expect(commandPosture(undefined)).toBe('off');
  for (const value of ['off', 'ask-per-destination', 'on'] as const) expect(commandPosture(value)).toBe(value);
  for (const value of ['', 'ON', 'ask', ' on', 'off\n', 'unrestricted']) expect(() => commandPosture(value)).toThrow();
});
function candidateIdentity(sha256: string | undefined, size: string | undefined): { sha256: string; size: number } | undefined {
  if (sha256 === undefined && size === undefined) return undefined;
  if (sha256 === undefined || size === undefined || sha256.length !== 64 || !/^[a-f0-9]{64}$/.test(sha256) || !/^[1-9][0-9]{0,10}$/.test(size) || String(Number(size)) !== size || !Number.isSafeInteger(Number(size)) || Number(size) > 4_294_967_296) throw new Error('Candidate SHA256 and positive bounded SIZE must be supplied together');
  return Object.freeze({ sha256, size: Number(size) });
}
it('requires a complete strict candidate identity and detects changed controlled bytes without executing them', async () => {
  expect(candidateIdentity(undefined, undefined)).toBeUndefined();
  for (const [sha, size] of [[undefined, '1'], ['a'.repeat(64), undefined], ['A'.repeat(64), '1'], ['a'.repeat(64), '01'], ['a'.repeat(64), '0'], ['a'.repeat(64), '4294967297'], ['a'.repeat(64), '2\n']]) expect(() => candidateIdentity(sha, size)).toThrow();
  const root = await realpath(await mkdtemp(join(await realpath(tmpdir()), 'candidate-identity-test-')));
  try {
    const path = join(root, 'inert-fixture'); await writeFile(path, 'abc');
    const profile = candidateIdentity(createHash('sha256').update('abc').digest('hex'), '3')!;
    const verifier = createControlledSupplyVerifierForTests({ ...profile, version: 'candidate-source-version-not-accepted-identity' });
    expect((await verifier.verify(path)).evidenceClass).toBe('controlled-fixture');
    await writeFile(path, 'abd'); await expect(verifier.verify(path)).rejects.toThrow();
    await writeFile(path, 'ab'); await expect(verifier.verify(path)).rejects.toThrow();
  } finally { await rm(root, { recursive: true, force: true }); }
});
const enabled = process.env.CHIRALITY_RUN_EXACT_CODEX_CONFORMANCE === '1';
describe.skipIf(!enabled)('opt-in accepted exact supplier or unaccepted candidate with deterministic local model', () => {
  it('runs actual primary and native descendant actions under the named policy', async () => {
    const supplied = process.env.CHIRALITY_EXACT_CODEX_PATH;
    const evidenceDirectory = process.env.CHIRALITY_EXACT_EVIDENCE_DIR;
    if (!supplied || !evidenceDirectory) throw new Error('Explicit exact binary and disposable evidence paths are required');
    if (process.platform !== 'darwin' || process.arch !== 'arm64') throw new Error('Exact conformance is darwin-arm64 only');
    const commandNetworkPosture = commandPosture(process.env.CHIRALITY_EXACT_COMMAND_POSTURE);
    const candidate = candidateIdentity(process.env.CHIRALITY_EXACT_CANDIDATE_SHA256, process.env.CHIRALITY_EXACT_CANDIDATE_SIZE);
    const controlled = candidate ? createControlledSupplyVerifierForTests({ ...candidate, version: 'candidate-source-version-not-accepted-identity' }) : undefined;
    const verifyPayload = (path: string) => controlled ? controlled.verify(path) : verifyExactSupply({ executablePath: path });
    const verified = await verifyPayload(supplied);
    const base = await realpath(await mkdtemp(join(await realpath(tmpdir()), 'exact-codex-conformance-')));
    const root = join(base, 'project'), broker = join(base, 'broker'), worker = join(broker, 'worker'), home = join(worker, 'home');
    const foreign = join(base, 'foreign.txt'), brokerCanary = join(broker, 'broker-control.txt');
    await mkdir(root, { mode: 0o700 }); await mkdir(broker, { mode: 0o700 }); await mkdir(worker, { mode: 0o700 }); await mkdir(home, { mode: 0o700 });
    await writeFile(foreign, 'DETERMINISTIC_FOREIGN_SENTINEL', { mode: 0o600 }); await writeFile(brokerCanary, 'DETERMINISTIC_BROKER_SENTINEL', { mode: 0o600 });
    const executable = join(worker, 'app-server'); await copyFile(verified.executablePath, executable); await chmod(executable, 0o700);
    await verifyPayload(executable);
    let policy: Awaited<ReturnType<typeof prepareCodexNativePolicy>> | undefined;
    let provider: Awaited<ReturnType<typeof startResponseProvider>> | undefined;
    let actor: CodexTurnSession | undefined;
    let closeChild: (() => Promise<void>) | undefined;
    let stderr = Buffer.alloc(0), stderrBytes = 0;
    const observations: Record<string, unknown> = { evidenceClass: candidate ? 'supplier-candidate-unaccepted' : 'exact-app-server-deterministic-model', supplierIdentity: candidate ? 'supplier-candidate-unaccepted' : 'accepted-supply', acceptedSupplierIdentityClaimed: candidate === undefined, sourceVersionIsAcceptedIdentity: false, accountUsed: false, providerEndpoint: 'loopback-only-configured', externalEgressEnforcement: 'NOT_ESTABLISHED_BY_THIS_TEST', supplySha256: verified.sha256, supplySize: Number(verified.identity.size) };
    const diagnosticRootsRaw = process.env.CHIRALITY_EXACT_DIAGNOSTIC_READ_ROOTS;
    const dynamicOnly = process.env.CHIRALITY_EXACT_DYNAMIC_ONLY === '1';
    const fileChangeOnly = process.env.CHIRALITY_EXACT_FILE_CHANGE_ONLY === '1';
    // Pinned source model catalog declares freeform apply_patch for gpt-5.4.
    // The fixture still requires the actual advertisement before emitting any call.
    const fixtureModel = fileChangeOnly ? 'gpt-5.4' : 'runtime-deterministic';
    observations.fileChangeOnly = fileChangeOnly; observations.fixtureModel = fixtureModel;
    observations.dynamicOnly = dynamicOnly;
    observations.commandNetworkPosture = commandNetworkPosture;
    observations.networkPostureEvidence = 'CONFIGURATION_TEXT_RESUME_ONLY_UNLESS_SEPARATELY_EXERCISED';
    observations.commandNetworkEnforcementProven = false;
    observations.phase = 'compile-native-policy';
    try {
      if ([dynamicOnly, fileChangeOnly, process.env.CHIRALITY_EXACT_DISCOVERY_ONLY === '1'].filter(Boolean).length > 1) throw new Error('Select either dynamic or discovery mode');
      const diagnosticRoots: unknown = diagnosticRootsRaw === undefined ? undefined : JSON.parse(diagnosticRootsRaw);
      if (diagnosticRoots !== undefined && (!Array.isArray(diagnosticRoots) || diagnosticRoots.length > 16 || !diagnosticRoots.every(value => typeof value === 'string' && value.length <= 1024))) throw new Error('Diagnostic read roots must be a bounded JSON string array');
      const immutableReadRoots = (diagnosticRoots as string[] | undefined) ?? ['/bin', '/usr/lib', '/System/Volumes/Preboot/Cryptexes/OS/System/Library/dyld'];
      observations.readRoots = immutableReadRoots; observations.diagnosticReadRootOverride = diagnosticRootsRaw !== undefined;
      policy = await prepareCodexNativePolicy({ canonicalRoot: root, codexHome: home, privateDirectory: worker,
        // Live Mach-O dependency inspection supports /bin shell/cat plus /usr/lib.
        // Additional runtime reads require observed exact-payload evidence, not blanket roots.
        immutableReadRoots, protectedPaths: [broker], commandNetworkPosture });
      provider = await startResponseProvider({ projectRoot: root, foreignCanary: foreign, brokerCanary, mode: fileChangeOnly ? 'file-change' : dynamicOnly ? 'dynamic' : process.env.CHIRALITY_EXACT_DISCOVERY_ONLY === '1' ? 'discover' : 'exercise' });
      const providerConfig = [
        'model_provider="runtime_deterministic"', `model=${JSON.stringify(fixtureModel)}`,
        'model_providers.runtime_deterministic.name="Runtime deterministic loopback"',
        `model_providers.runtime_deterministic.base_url=${JSON.stringify(provider.baseUrl)}`,
        'model_providers.runtime_deterministic.wire_api="responses"', 'model_providers.runtime_deterministic.requires_openai_auth=false',
        'model_providers.runtime_deterministic.supports_websockets=false', 'model_providers.runtime_deterministic.request_max_retries=0',
        'model_providers.runtime_deterministic.stream_max_retries=0', 'model_providers.runtime_deterministic.stream_idle_timeout_ms=10000',
        'features.multi_agent=true',
      ];
      observations.expectedPermissions = policy.expectedPermissions;
      observations.permissionProfile = policy.profileId;
      const startHost = async (generation: number) => {
      observations.phase = `host-${generation}-launch`;
      await verifyPayload(executable);
      const launch = await policy!.launchArguments(executable);
      const child = spawn(launch[0]!, [...launch.slice(1), ...providerConfig.flatMap(value => ['-c', value])], { cwd: root, env: policy!.environment, detached: true, stdio: 'pipe' });
      const closed = new Promise<void>(resolve => child.once('close', (exitCode, signal) => { observations.process = { generation, pid: child.pid, exitCode, signal }; observations.processes = [...((observations.processes as unknown[]) ?? []), observations.process]; resolve(); }));
      const kill = () => { if (child.pid) { try { process.kill(-child.pid, 'SIGKILL'); } catch { /* already exited */ } } };
      child.once('exit', kill); child.on('error', () => {});
      child.stderr.on('data', (bytes: Buffer) => { stderrBytes += bytes.length; stderr = Buffer.concat([stderr, bytes]).subarray(0, 65_536); if (stderrBytes > 65_536) kill(); });
      closeChild = async () => { if (child.exitCode === null && child.signalCode === null) observations.cleanupTerminationRequested = true; kill(); await closed; };
      // Correlate request IDs with method names only. Parameters are never retained.
      const transportInput = new PassThrough();
      transportInput.on('error', () => {});
      child.stdin.on('error', () => transportInput.destroy(new Error('App Server input closed')));
      const requestMethods = new Map<number, string>();
      let requestBuffer = Buffer.alloc(0), requestBytes = 0;
      transportInput.on('data', (bytes: Buffer) => {
        requestBytes += bytes.length;
        if (requestBytes > 2_000_000) { requestBuffer = Buffer.alloc(0); return; }
        requestBuffer = Buffer.concat([requestBuffer, bytes]);
        if (requestBuffer.length > 262_144) { requestBuffer = Buffer.alloc(0); return; }
        for (let newline = requestBuffer.indexOf(10); newline >= 0; newline = requestBuffer.indexOf(10)) {
          const line = requestBuffer.subarray(0, newline); requestBuffer = requestBuffer.subarray(newline + 1);
          try {
            const request = JSON.parse(line.toString());
            if (Number.isSafeInteger(request.id) && typeof request.method === 'string' && request.method.length <= 128 && requestMethods.size < 128) {
              requestMethods.set(request.id, request.method);
              observations.rpcRequests = [...((observations.rpcRequests as unknown[]) ?? []), { generation, id: request.id, method: request.method }];
            }
          } catch { /* Observation is not a protocol authority. */ }
        }
      });
      transportInput.pipe(child.stdin);
      // Read-only diagnostic observer; never retains full config, prompts or auth.
      let observedBytes = 0, observerBuffer = Buffer.alloc(0), observedConfigs = 0;
      const table = (value: unknown): value is Record<string, unknown> => Boolean(value && typeof value === 'object' && !Array.isArray(value));
      const boundedProfile = (value: unknown, depth = 0): unknown => {
        if (depth > 6) return '[DEPTH_BOUND]';
        if (typeof value === 'string') return value.slice(0, 1024);
        if (value === null || typeof value === 'number' || typeof value === 'boolean') return value;
        if (Array.isArray(value)) return value.slice(0, 64).map(item => boundedProfile(item, depth + 1));
        if (table(value)) return Object.fromEntries(Object.entries(value).slice(0, 64).map(([key, item]) => [key, /^(?:authorization|access_token|refresh_token|api_key|password|secret|credential)$/i.test(key) ? '[REDACTED]' : boundedProfile(item, depth + 1)]));
        return '[ABSENT]';
      };
      child.stdout.on('data', (bytes: Buffer) => {
        observedBytes += bytes.length;
        if (observedBytes > 2_000_000) { observerBuffer = Buffer.alloc(0); return; }
        observerBuffer = Buffer.concat([observerBuffer, bytes]);
        if (observerBuffer.length > 1_000_000) { observerBuffer = Buffer.alloc(0); return; }
        for (let newline = observerBuffer.indexOf(10); newline >= 0; newline = observerBuffer.indexOf(10)) {
          const line = observerBuffer.subarray(0, newline); observerBuffer = observerBuffer.subarray(newline + 1);
          try {
            const message = JSON.parse(line.toString());
            if (message.method === 'item/tool/call' && ((observations.dynamicCallbacks as unknown[]) ?? []).length < 16) {
              const params = table(message.params) ? message.params : {};
              const safeId = (value: unknown) => (typeof value === 'string' && /^[A-Za-z0-9._-]{1,256}$/.test(value)) || Number.isSafeInteger(value) ? value : null;
              observations.dynamicCallbacks = [...((observations.dynamicCallbacks as unknown[]) ?? []), {
                generation, requestId: safeId(message.id), parameterKeys: Object.keys(params).slice(0, 32), threadId: safeId(params.threadId), turnId: safeId(params.turnId), callId: safeId(params.callId),
                tool: params.tool === 'review' ? params.tool : '[OTHER]', argumentKeys: table(params.arguments) ? Object.keys(params.arguments).slice(0, 32) : null,
                argumentSha256: createHash('sha256').update(JSON.stringify(params.arguments ?? null)).digest('hex'),
              }];
            }
            if (typeof message.method === 'string' && message.method.length <= 128 && ((observations.nativeNotifications as unknown[]) ?? []).length < 256) {
              // Only identity metadata from native notifications; no text, prompts or arguments.
              const ids: Record<string, unknown> = {};
              const visit = (value: unknown, prefix: string, depth: number) => {
                if (!table(value) || depth > 4) return;
                for (const [key, child] of Object.entries(value).slice(0, 64)) {
                  if (/^(?:threadId|thread_id|turnId|turn_id|parentId|parent_id|parentThreadId|parent_thread_id|sourceId|source_id|sourceThreadId|source_thread_id|agentId|agent_id)$/.test(key) && typeof child === 'string' && child.length <= 256) ids[`${prefix}${key}`] = child;
                  else if (key === 'type' && prefix.endsWith('item.') && typeof child === 'string') ids[`${prefix}type`] = child.slice(0, 128);
                  else if (table(child)) visit(child, `${prefix}${key}.`, depth + 1);
                }
              };
              visit(message.params, '', 0);
              observations.nativeNotifications = [...((observations.nativeNotifications as unknown[]) ?? []), { generation, method: message.method, ...ids }];
            }
            if (table(message?.error) && ((observations.rpcErrors as unknown[]) ?? []).length < 32) {
              const error = message.error;
              const safe = { generation, id: Number.isSafeInteger(message.id) ? message.id : null, method: requestMethods.get(message.id) ?? 'UNMATCHED',
                code: typeof error.code === 'number' ? error.code : typeof error.code === 'string' ? scrubStderr(error.code).slice(0, 128) : null,
                message: typeof error.message === 'string' ? scrubStderr(error.message).slice(0, 2048) : '[NON_STRING_MESSAGE]', dataPresent: Object.hasOwn(error, 'data') };
              observations.rpcErrors = [...((observations.rpcErrors as unknown[]) ?? []), safe];
            }
            const config = message?.result?.config;
            if (!table(config) || observedConfigs >= 4) continue;
            observedConfigs++;
            const permissions = table(config.permissions) ? config.permissions : undefined;
            const profile = permissions?.[policy!.profileId];
            const featureValues = table(config.features) ? Object.fromEntries(Object.entries(config.features).slice(0, 64).filter(([, value]) => typeof value === 'boolean')) : {};
            const result = {
              generation, selectedProfile: boundedProfile(profile),
              permissionShape: { present: Object.hasOwn(config, 'permissions'), isTable: permissions !== undefined, keyCount: permissions ? Object.keys(permissions).length : 0, hasProfiles: Boolean(permissions && Object.hasOwn(permissions, 'profiles')), hasSelectedProfile: Boolean(permissions && Object.hasOwn(permissions, policy!.profileId)) },
              hostSettings: { allow_login_shell: typeof config.allow_login_shell === 'boolean' ? config.allow_login_shell : null, approval_policy: typeof config.approval_policy === 'string' ? config.approval_policy.slice(0, 64) : null, features: featureValues },
              otherConfigFieldCount: Object.keys(config).filter(key => !['permissions', 'allow_login_shell', 'approval_policy', 'features'].includes(key)).length,
            };
            observations.nativePolicyReadbacks = [...((observations.nativePolicyReadbacks as unknown[]) ?? []), result];
          } catch { /* The actor independently rejects malformed protocol. */ }
        }
      });

      const dynamicTools: CodexDynamicTool[] | undefined = dynamicOnly ? [{
        name: 'review', description: 'Return a harmless deterministic review marker for conformance; no external side effects.',
        inputSchema: { type: 'object', properties: { text: { type: 'string', enum: ['DETERMINISTIC_DYNAMIC_INPUT'] } }, required: ['text'], additionalProperties: false },
        async handler(input, context) {
          if (input.text !== 'DETERMINISTIC_DYNAMIC_INPUT' || context.signal.aborted) throw new Error('Unexpected controlled dynamic input');
          observations.dynamicHandlerInvocations = [...((observations.dynamicHandlerInvocations as unknown[]) ?? []), { generation, threadId: context.threadId, turnId: context.turnId, callId: context.callId, marker: 'DETERMINISTIC_DYNAMIC_REVIEWED' }];
          return { success: true, contentItems: [{ type: 'inputText', text: 'DETERMINISTIC_DYNAMIC_REVIEWED' }] };
        },
      }] : undefined;
      actor = new CodexTurnSession({ transport: { stdin: transportInput, stdout: child.stdout, close: closeChild }, permissionProfile: policy!.permissionProfile, policyDigest: policy!.policyDigest, requestTimeoutMs: 10_000, turnTimeoutMs: 90_000, dynamicTools, commandNetworkPosture });
      const currentActor = actor;
      void (async () => { for await (const _event of currentActor.events()) { /* bounded actor drain; fixture records only chosen tool results */ } })().catch(() => {});
      observations.phase = `host-${generation}-initialize`;
      await actor.initialize();
      observations.phase = `host-${generation}-effective-policy-readback`;
      await actor.verifyNativePolicy(policy!.expectedPermissions);
      observations.phase = `host-${generation}-account-read`;
      const account = await actor.accountRead(); expect(account.hasAccount).toBe(false); observations.account = account;
      return { actor, pid: child.pid };
      };
      const firstHost = await startHost(1);
      actor = firstHost.actor;
      observations.phase = 'thread-start';
      const threadId = await actor.startThread({ cwd: root, model: fixtureModel, continuityChecked: true });
      observations.phase = 'first-turn';
      const turnId = await actor.startTurn({ threadId, model: fixtureModel, text: 'DETERMINISTIC_PARENT_ONLY: follow the deterministic local provider exercise.' });
      const terminal = await actor.waitTurn(turnId);
      observations.terminal = terminal; observations.policy = { profile: policy.permissionProfile, digest: policy.policyDigest };
      expect(terminal.status).toBe('completed'); expect(provider.failures).toEqual([]);
      if (dynamicOnly) {
        expect(terminal.output).toContain('DETERMINISTIC_DYNAMIC_COMPLETE');
        expect((observations.dynamicHandlerInvocations as unknown[])?.length).toBe(1);
        expect((observations.dynamicCallbacks as unknown[])?.length).toBe(1);
        expect(provider.records.flatMap((record: any) => record.outputs).some((output: any) => output.issued.kind === 'dynamic' && output.output.includes('DETERMINISTIC_DYNAMIC_REVIEWED'))).toBe(true);
      }
      if (!dynamicOnly && !fileChangeOnly && process.env.CHIRALITY_EXACT_DISCOVERY_ONLY !== '1') {
        expect(await readFile(join(root, 'primary.txt'), 'utf8')).toBe('primary');
        expect(await readFile(join(root, 'child.txt'), 'utf8')).toBe('child');
        const outputs = provider.records.flatMap((record: any) => record.outputs);
        for (const who of ['primary', 'child']) {
          const result = outputs.find((output: any) => output.issued.who === who && output.issued.kind === 'shell');
          expect(result?.output).toContain('FOREIGN_DENIED'); expect(result?.output).toContain('BROKER_DENIED');
          expect(result?.output).not.toContain('_LEAK');
        }
        expect(outputs.some((output: any) => output.issued.kind === 'spawn')).toBe(true);
        expect(outputs.some((output: any) => output.issued.kind === 'wait' && output.output.includes('completed'))).toBe(true);
      }
      if (fileChangeOnly) {
        for (const who of ['primary', 'child']) expect((await readFile(join(root, `${who}-patch.txt`), 'utf8')).trim()).toBe(`${who}-patch-marker`);
        expect(await readFile(foreign, 'utf8')).toBe('DETERMINISTIC_FOREIGN_SENTINEL');
        expect(terminal.output).toContain('DETERMINISTIC_FILE_CHANGE_COMPLETE');
        const outputs = provider.records.flatMap((record: any) => record.outputs);
        for (const who of ['primary', 'child']) expect(outputs.some((output: any) => output.issued.who === who && output.issued.kind === 'patch-denied')).toBe(true);
        observations.fileChange = { primaryCreated: true, nativeChildCreated: true, foreignUnchanged: true, tool: 'actual-advertised-apply_patch' };
      }
      await actor.close(); await closeChild?.();
      const secondHost = await startHost(2); actor = secondHost.actor;
      expect(secondHost.pid).not.toBe(firstHost.pid);
      observations.phase = 'thread-resume';
      const resumedThreadId = await actor.resumeThread({ threadId, model: fixtureModel, continuityChecked: true });
      expect(resumedThreadId).toBe(threadId);
      observations.phase = 'resumed-turn';
      const resumedTurnId = await actor.startTurn({ threadId: resumedThreadId, model: fixtureModel, text: 'DETERMINISTIC_RESUME_ONLY: finish the resumed deterministic conversation.' });
      const resumedTerminal = await actor.waitTurn(resumedTurnId);
      observations.resume = { firstPid: firstHost.pid, secondPid: secondHost.pid, threadId, resumedThreadId, firstTurnId: turnId, resumedTurnId, terminal: resumedTerminal, samePrivateHome: true, nativePolicyVerifiedOnBothHosts: true };
      expect(resumedTurnId).not.toBe(turnId); expect(resumedTerminal.status).toBe('completed'); expect(provider.failures).toEqual([]);
      observations.phase = 'complete';
      observations.verdict = diagnosticRootsRaw !== undefined ? 'DIAGNOSTIC_ONLY' : fileChangeOnly ? 'FILE_CHANGE_PASS' : dynamicOnly ? 'DYNAMIC_TOOL_PASS' : process.env.CHIRALITY_EXACT_DISCOVERY_ONLY === '1' ? 'DISCOVERY_ONLY' : 'PASS';
    } catch (error) { observations.verdict = diagnosticRootsRaw !== undefined ? 'DIAGNOSTIC_ONLY' : 'FAIL'; observations.outcome = 'FAIL'; observations.error = error instanceof Error ? error.message : 'unknown'; throw error; }
    finally {
      await actor?.close(); await closeChild?.(); await provider?.close();
      try { await verifyPayload(supplied); await verifyPayload(executable); observations.supplyRevalidatedAfter = true; }
      catch { observations.supplyRevalidatedAfter = false; observations.verdict = 'FAIL'; observations.outcome = 'SUPPLY_IDENTITY_CHANGED'; }
      observations.projectFiles = {};
      for (const name of ['primary.txt', 'child.txt', 'primary-baseline.txt', 'child-baseline.txt', 'primary-patch.txt', 'child-patch.txt']) {
        try { (observations.projectFiles as Record<string, unknown>)[name] = (await readFile(join(root, name), 'utf8')).slice(0, 128); }
        catch { (observations.projectFiles as Record<string, unknown>)[name] = null; }
      }
      await mkdir(evidenceDirectory, { recursive: true, mode: 0o700 });
      await writeFile(join(evidenceDirectory, 'deterministic-conformance.json'), JSON.stringify({ ...observations, stderr: { text: scrubStderr(stderr.toString()), bytesObserved: stderrBytes, truncated: stderrBytes > 65_536, redaction: 'known bearer/key/token patterns; isolated empty home only' }, requests: provider?.records ?? [], providerFailures: provider?.failures ?? [] }, null, 2) + '\n', { mode: 0o600, flag: 'wx' });
      await policy?.cleanup(); await rm(base, { recursive: true, force: true });
      expect(observations.supplyRevalidatedAfter, 'Supplier identity must remain verified after execution').toBe(true);
    }
  }, 210_000);
});
