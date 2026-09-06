import { spawn } from 'node:child_process';
import { createHash } from 'node:crypto';
import { createServer } from 'node:http';
import { gunzipSync } from 'node:zlib';
import { constants } from 'node:fs';
import { chmod, copyFile, lstat, mkdir, mkdtemp, open, readdir, readFile, realpath, rm, symlink, writeFile } from 'node:fs/promises';
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
import { createRolePolicyEvidence, type RolePolicySettings } from '../packages/core/src/role-policy.js';
import { createProjectFixture } from './helpers.js';
import { startSupervisorServer, SupervisorClient } from '../packages/daemon/src/supervisor-server.js';

const fixtureCompatibility = { compatibilityIdentity: 'root-runtime-1', contractBasisSha256: createHash('sha256').update('exact-role-test-only; not accepted production contract basis').digest('hex') };
const quote = (value: string) => "'" + value.replaceAll("'", "'\\''") + "'";
function standaloneRead(output: string, who: string) {
  const lines = output.split(/\r?\n/);
  return ['START', 'READ_OK', 'DENIED', 'FINISH'].every(marker => lines.includes(`ROLE_${who}_${marker}`));
}
const roles = ['untyped', 'agent0', 'agent1', 'agent2', 'task'] as const;
type Role = typeof roles[number];
type FixtureOrigin = { who: Role | 'child'; primaryRole: Role; spawnCallId?: string };
const childPrompt = 'ROLE_NATIVE_CHILD_ONLY: return the deterministic child marker.';
function actorPrompt(role: Role, prompt: string): string {
  // Exact CodexSupervisor role-prefix transformation, not a permissive marker search.
  return role === 'untyped' ? prompt : `Runtime role instruction (explicit user selection): ${role}.\nrole not mechanically enforced; evidence posture: instruction-asserted.\n\n${prompt}`;
}
function selectOrigin(input: any[], registry: ReadonlyMap<string, FixtureOrigin>) {
  const matches: { origin: FixtureOrigin; inputIndex: number; textSha256: string }[] = [];
  input.forEach((item, inputIndex) => {
    if (item.role !== 'user' || !Array.isArray(item.content)) return;
    for (const content of item.content) {
      if (content.type !== 'input_text' || typeof content.text !== 'string') continue;
      const origin = registry.get(content.text);
      if (origin) matches.push({ origin, inputIndex, textSha256: createHash('sha256').update(content.text).digest('hex') });
    }
  });
  const primaries = matches.filter(match => match.origin.who !== 'child'), children = matches.filter(match => match.origin.who === 'child');
  if (primaries.length > 1 || children.length > 1) throw new Error('Conflicting original fixture roles');
  if (children.length === 1) {
    const child = children[0]!;
    if (!child.origin.spawnCallId || child.origin.primaryRole !== 'agent1' || (primaries.length && primaries[0]!.origin.who !== 'agent1')) throw new Error('Unissued or conflicting native origin');
    return child;
  }
  if (primaries.length !== 1) throw new Error('Original fixture role unavailable');
  return primaries[0]!;
}
it('retains exact issued origins across lifecycle messages without a default role', () => {
  const primary = actorPrompt('agent1', 'original-primary');
  const registry = new Map<string, FixtureOrigin>([[primary, { who: 'agent1', primaryRole: 'agent1' }], [childPrompt, { who: 'child', primaryRole: 'agent1', spawnCallId: 'issued-spawn' }]]);
  const user = (text: string) => ({ role: 'user', content: [{ type: 'input_text', text }] });
  const notification = user(`<subagent_notification>${JSON.stringify({ status: { completed: childPrompt } })}</subagent_notification>`);
  expect(selectOrigin([user(primary), notification], registry).origin.who).toBe('agent1');
  expect(selectOrigin([user(primary), user(childPrompt), notification], registry).origin.who).toBe('child');
  expect(selectOrigin([user(childPrompt), notification], registry).origin.spawnCallId).toBe('issued-spawn');
  expect(() => selectOrigin([notification], registry)).toThrow('Original fixture role unavailable');
  expect(() => selectOrigin([user(primary), user(primary)], registry)).toThrow('Conflicting original fixture roles');
  expect(() => selectOrigin([user(childPrompt)], new Map([[childPrompt, { who: 'child', primaryRole: 'agent1' }]]))).toThrow('Unissued or conflicting native origin');
  const other = actorPrompt('agent0', 'other'); registry.set(other, { who: 'agent0', primaryRole: 'agent0' });
  expect(() => selectOrigin([user(primary), user(other)], registry)).toThrow('Conflicting original fixture roles');
  expect(() => selectOrigin([user(other), user(childPrompt)], registry)).toThrow('Unissued or conflicting native origin');
});

function nativeSessionMetadata(line: string, childId: string, parentId: string, cwd: string) {
  const record = JSON.parse(line), meta = record.payload, source = meta?.source?.subagent?.thread_spawn;
  if (record.type !== 'session_meta' || meta?.id !== childId || meta.parent_thread_id !== parentId || meta.cwd !== cwd || source?.parent_thread_id !== parentId || source.depth !== 1) throw new Error('Native SessionMeta identity mismatch');
  return { origin: 'supplier-owned-first-SessionMeta', threadId: childId, parentThreadId: parentId, cwd, source: { kind: 'subagent/thread_spawn', parentThreadId: parentId, depth: source.depth }, firstRecordSha256: createHash('sha256').update(line).digest('hex'), firstRecordBytes: Buffer.byteLength(line) };
}
function canonicalTimestamp(value: string): boolean {
  const parsed = new Date(`${value}Z`);
  return !Number.isNaN(parsed.valueOf()) && parsed.toISOString() === `${value}.000Z`;
}
function requireNativeRolloutPath(name: string, dateParts: readonly string[], childId: string): void {
  // Fresh, non-reverted supplier child: rollout-YYYY-MM-DDTHH-MM-SS-<thread-id>.jsonl.
  const match = /^rollout-(\d{4})-(\d{2})-(\d{2})T(\d{2})-(\d{2})-(\d{2})-([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})\.jsonl$/.exec(name);
  if (dateParts.length !== 3 || !match || match[7] !== childId || dateParts.join('-') !== match.slice(1, 4).join('-') || !canonicalTimestamp(`${match[1]}-${match[2]}-${match[3]}T${match[4]}:${match[5]}:${match[6]}`)) throw new Error('Noncanonical native SessionMeta path');
}
it('requires canonical dated fresh-child rollout names with directory/date agreement', () => {
  const id = '11111111-1111-1111-1111-111111111111';
  expect(() => requireNativeRolloutPath(`rollout-2026-09-06T12-34-56-${id}.jsonl`, ['2026', '09', '06'], id)).not.toThrow();
  expect(() => requireNativeRolloutPath(`rollout-2024-02-29T00-00-00-${id}.jsonl`, ['2024', '02', '29'], id)).not.toThrow();
  for (const [name, parts] of [
    [`rollout-not-a-date-${id}.jsonl`, []],
    [`rollout-not-a-date-${id}.jsonl`, ['2026', '09', '06']],
    [`rollout-2026-09-06T12-34-56-${id}.jsonl`, []],
    [`rollout-2026-09-06T12-34-56-${id}.jsonl`, ['2026', '09', '07']],
    [`rollout-2026-02-29T12-34-56-${id}.jsonl`, ['2026', '02', '29']],
    [`rollout-2026-09-06T24-00-00-${id}.jsonl`, ['2026', '09', '06']],
    [`rollout-2026-09-06T12-60-00-${id}.jsonl`, ['2026', '09', '06']],
    [`rollout-2026-09-06T12-34-56-${id}_${id}.jsonl`, ['2026', '09', '06']]
  ] as const) expect(() => requireNativeRolloutPath(name, parts, id)).toThrow('Noncanonical native SessionMeta path');
});
async function readNativeSessionMetadata(home: string, childId: string, parentId: string, cwd: string) {
  if (![childId, parentId].every(id => /^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$/.test(id))) throw new Error('Bounded native identifiers required');
  const started = Date.now(), candidates: string[] = []; let entries = 0;
  const checkDirectory = async (path: string) => {
    const info = await lstat(path);
    if (info.isSymbolicLink() || !info.isDirectory() || await realpath(path) !== path || (process.getuid && info.uid !== process.getuid())) throw new Error('Unsafe owned SessionMeta directory');
  };
  await checkDirectory(home);
  const walk = async (path: string, dateParts: string[]) => {
    await checkDirectory(path);
    for (const entry of await readdir(path, { withFileTypes: true })) {
      if (++entries > 64 || Date.now() - started > 5000 || entry.isSymbolicLink()) throw new Error('SessionMeta traversal bound or symlink');
      const child = join(path, entry.name);
      if (entry.isDirectory()) {
        const depth = dateParts.length;
        if (depth >= 3 || !(depth === 0 ? /^\d{4}$/ : /^\d{2}$/).test(entry.name)) throw new Error('Unexpected SessionMeta directory layout');
        const next = [...dateParts, entry.name];
        if ((depth === 1 && (Number(entry.name) < 1 || Number(entry.name) > 12)) || (depth === 2 && !canonicalTimestamp(`${next.join('-')}T00:00:00`))) throw new Error('Unexpected SessionMeta directory date');
        await walk(child, next);
      } else if (entry.isFile() && entry.name.startsWith('rollout-') && entry.name.includes(childId)) {
        requireNativeRolloutPath(entry.name, dateParts, childId);
        candidates.push(child);
      }
    }
  };
  await walk(join(home, 'sessions'), []);
  if (candidates.length !== 1) throw new Error('Native SessionMeta missing or ambiguous');
  const path = candidates[0]!, before = await lstat(path);
  if (!before.isFile() || before.isSymbolicLink() || (process.getuid && before.uid !== process.getuid())) throw new Error('Unsafe SessionMeta file');
  const file = await open(path, constants.O_RDONLY | constants.O_NOFOLLOW);
  try {
    const opened = await file.stat();
    if (opened.dev !== before.dev || opened.ino !== before.ino || await realpath(path) !== path) throw new Error('SessionMeta file replaced');
    const record = Buffer.alloc(262144), byte = Buffer.alloc(1); let length = 0;
    // One byte per read deliberately avoids reading ahead into any transcript record.
    for (; length < record.length; length++) {
      if (Date.now() - started > 5000) throw new Error('SessionMeta read budget exceeded');
      const { bytesRead } = await file.read(byte, 0, 1, length);
      if (bytesRead !== 1) throw new Error('Incomplete first SessionMeta record');
      if (byte[0] === 10) break;
      record[length] = byte[0]!;
    }
    if (length === record.length) throw new Error('First SessionMeta record exceeds byte bound');
    const after = await file.stat(), pathAfter = await lstat(path);
    if (after.size !== opened.size || after.mtimeMs !== opened.mtimeMs || pathAfter.dev !== opened.dev || pathAfter.ino !== opened.ino || await realpath(path) !== path) throw new Error('SessionMeta changed during read');
    return { ...nativeSessionMetadata(record.subarray(0, length).toString('utf8'), childId, parentId, cwd), inspectedEntries: entries, readElapsedMs: Date.now() - started, firstRecordOnly: true };
  } finally { await file.close(); }
}
it('reads only exact owned native SessionMeta and rejects symlink or identity substitution', async () => {
  const owned = join(await realpath('/tmp'), 'runtime-conformance-resume-20260906', 'P4'); await mkdir(owned, { recursive: true });
  const base = await realpath(await mkdtemp(join(owned, 'metadata-'))), childId = '11111111-1111-1111-1111-111111111111', parentId = '22222222-2222-2222-2222-222222222222';
  try {
    const dir = join(base, 'sessions', '2026', '09', '06'); await mkdir(dir, { recursive: true });
    const path = join(dir, `rollout-2026-09-06T12-34-56-${childId}.jsonl`);
    const line = JSON.stringify({ type: 'session_meta', payload: { id: childId, parent_thread_id: parentId, cwd: '/fixture', source: { subagent: { thread_spawn: { parent_thread_id: parentId, depth: 1 } } }, base_instructions: 'not retained' } });
    await writeFile(path, line + '\nTRANSCRIPT_IS_NOT_JSON_AND_MUST_NOT_BE_READ\n');
    const value = await readNativeSessionMetadata(base, childId, parentId, '/fixture');
    expect(value).toMatchObject({ firstRecordOnly: true, threadId: childId, parentThreadId: parentId, firstRecordBytes: Buffer.byteLength(line) });
    expect(JSON.stringify(value)).not.toContain('not retained');
    expect(() => nativeSessionMetadata(line, parentId, childId, '/fixture')).toThrow('Native SessionMeta identity mismatch');
    const wrongSource = JSON.parse(line); wrongSource.payload.source.subagent.thread_spawn.parent_thread_id = childId;
    expect(() => nativeSessionMetadata(JSON.stringify(wrongSource), childId, parentId, '/fixture')).toThrow('Native SessionMeta identity mismatch');
    await expect(readNativeSessionMetadata(base, childId, parentId, '/different')).rejects.toThrow('Native SessionMeta identity mismatch');
    await rm(path);
    for (const misplaced of [
      join(base, 'sessions', `rollout-not-a-date-${childId}.jsonl`),
      join(dir, `rollout-not-a-date-${childId}.jsonl`),
      join(base, 'sessions', `rollout-2026-09-06T12-34-56-${childId}.jsonl`),
      join(dir, `rollout-2026-09-07T12-34-56-${childId}.jsonl`)
    ]) {
      await writeFile(misplaced, 'NOT A SESSION RECORD: MUST REJECT PATH BEFORE OPEN\n');
      await expect(readNativeSessionMetadata(base, childId, parentId, '/fixture')).rejects.toThrow('Noncanonical native SessionMeta path');
      await rm(misplaced);
    }
    await symlink('/dev/null', path);
    await expect(readNativeSessionMetadata(base, childId, parentId, '/fixture')).rejects.toThrow('SessionMeta traversal bound or symlink');
  } finally { await rm(base, { recursive: true, force: true }); }
});
function nativeTool(tools: any[], names: string[]) {
  const flattened = tools.flatMap(tool => tool.type === 'namespace' && Array.isArray(tool.tools) ? tool.tools.map((member: any) => ({ ...member, namespace: tool.name })) : [tool]);
  const tool = flattened.find(tool => tool.type === 'function' && names.includes(tool.name));
  if (!tool?.parameters) throw new Error('Advertised native tool absent');
  return tool;
}
function execReadArguments(tool: any, command: string, root: string): Record<string, unknown> {
  const properties = tool.parameters?.properties;
  if (!properties || !Object.hasOwn(properties, 'cmd')) throw new Error('Unknown actual exec schema');
  const args: Record<string, unknown> = { cmd: command };
  // Supplier shell_spec.rs omits login when immutable allow_login_shell=false.
  for (const [key, value] of Object.entries({ workdir: root, login: false, yield_time_ms: 1000, max_output_tokens: 1000 })) {
    if (Object.hasOwn(properties, key)) args[key] = value;
  }
  if ((tool.parameters.required ?? []).some((key: string) => !Object.hasOwn(args, key)) || Object.keys(args).some(key => !Object.hasOwn(properties, key))) throw new Error('Unknown actual exec schema');
  return args;
}
it('maps disabled-login supplier advertisement without inventing optional or required fields', () => {
  const properties = Object.fromEntries(['cmd', 'workdir', 'tty', 'yield_time_ms', 'max_output_tokens', 'shell'].map(key => [key, {}]));
  const tool = { parameters: { properties, required: ['cmd'] } };
  expect(execReadArguments(tool, 'fixture-read', '/fixture')).toEqual({ cmd: 'fixture-read', workdir: '/fixture', yield_time_ms: 1000, max_output_tokens: 1000 });
  expect(execReadArguments({ parameters: { properties: { cmd: {}, login: {} }, required: ['cmd'] } }, 'fixture-read', '/fixture')).toEqual({ cmd: 'fixture-read', login: false });
  expect(() => execReadArguments({ parameters: { properties, required: ['cmd', 'unknown'] } }, 'fixture-read', '/fixture')).toThrow('Unknown actual exec schema');
});
it('preserves native namespace and refuses an invented native function', () => {
  expect(nativeTool([{ type: 'namespace', name: 'agents', tools: [{ type: 'function', name: 'spawn_agent', parameters: {} }] }], ['spawn_agent']).namespace).toBe('agents');
  expect(() => nativeTool([], ['spawn_agent'])).toThrow();
});

it('admits controlled fixture metadata but rejects its production hosted admission', async () => {
  let launches = 0;
  const identity = { canonicalRoot: '/fixture', cwd: '/fixture', accountId: 'no-account-test', accountEpoch: 1, policyDigest: 'fixture' };
  const supervisor = CodexSupervisor.controlledForTests({ identity, model: 'runtime-deterministic', allowUnauthenticatedModel: true, launch: async () => { launches++; throw new Error('No launch authorized by metadata test'); } });
  try {
    const binding = { compatibility: fixtureCompatibility, identity, evidenceClass: 'controlled-worker' as const, supervisor, consent: {}, retirement: {} };
    const runtime = new DelegatedRuntime({ daemonId: 'metadata-fixture', projects: new Map([['p', binding as any]]) });
    expect(await runtime.preflight('p', 'turn:valid')).toMatchObject({ ...fixtureCompatibility, operationId: 'turn:valid', projectId: 'p' });
    const invalid = new DelegatedRuntime({ daemonId: 'metadata-fixture', projects: new Map([['p', { ...binding, compatibility: { ...fixtureCompatibility, compatibilityIdentity: 'exact-role-test' } } as any]]) });
    await expect(invalid.preflight('p', 'turn:invalid')).rejects.toThrow('Daemon compatibility basis is unavailable');
    const production = new DelegatedRuntime({ daemonId: 'metadata-fixture', projects: new Map([['p', { ...binding, evidenceClass: 'provider-observed' } as any]]) });
    await expect(production.preflight('p', 'turn:production')).rejects.toThrow('Verified hosted worker, account continuity or operator provider consent is unavailable');
    expect(launches).toBe(0);
  } finally { await supervisor.close(); }
});
it('requires standalone markers instead of an echoed failed command', () => {
  expect(standaloneRead("exec failed: printf 'ROLE_agent0_START\\nROLE_agent0_READ_OK\\nROLE_agent0_DENIED\\nROLE_agent0_FINISH'", 'agent0')).toBe(false);
  expect(standaloneRead('ROLE_agent0_START\nROLE_agent0_READ_OK\nROLE_agent0_DENIED\nROLE_agent0_FINISH\n', 'agent0')).toBe(true);
});

const sourcePaths = ['tests/exact-role-conformance.test.ts', 'packages/core/src/delegated-runtime.ts', 'packages/daemon/src/runtime-daemon.ts', 'packages/client/src/client.ts', 'packages/daemon/src/supervisor-server.ts', 'packages/core/src/worker-retirement.ts', 'packages/core/src/role-policy.ts', 'packages/core/dist/delegated-runtime.js', 'packages/core/dist/role-policy.js', 'packages/core/dist/worker-retirement.js', 'packages/client/dist/src/client.js', 'packages/daemon/src/codex-session.ts', 'packages/daemon/src/codex-supervisor.ts', 'packages/daemon/src/codex-containment.ts'];
const pins = async () => Object.fromEntries(await Promise.all(sourcePaths.map(async path => [path, createHash('sha256').update(await readFile(path)).digest('hex')])));

it('resolves every selected runtime source pin without a supplier launch', async () => { expect(Object.keys(await pins())).toEqual(sourcePaths); });

it.runIf(process.env.CHIRALITY_RUN_EXACT_ROLE === '1')('actual public role parity and native descent without implicit Chirality role assignment', async () => {
  const started = Date.now(), supplied = process.env.CHIRALITY_EXACT_CODEX_PATH, evidence = process.env.CHIRALITY_EXACT_EVIDENCE_DIR;
  const sha = process.env.CHIRALITY_EXACT_CANDIDATE_SHA256, size = process.env.CHIRALITY_EXACT_CANDIDATE_SIZE;
  if (!supplied || !evidence?.startsWith('/')) throw new Error('Explicit exact supplier and fresh evidence directory required');
  if ((sha === undefined) !== (size === undefined) || (sha !== undefined && (!/^[a-f0-9]{64}$/.test(sha) || !size || String(Number(size)) !== size || !Number.isSafeInteger(Number(size)) || Number(size) < 1 || Number(size) > 4294967296))) throw new Error('Exact candidate hash and size required');
  const controlled = sha ? createControlledSupplyVerifierForTests({ sha256: sha, size: Number(size), version: 'candidate-source-version-not-accepted-identity' }) : undefined;
  const verify = (path: string) => controlled ? controlled.verify(path) : verifyExactSupply({ executablePath: path });
  let base = '', root = '', broker = '', worker = '', home = '', allowed = '', denied = '';
  const cleanups: (() => Promise<unknown>)[] = [];
  const result: Record<string, any> = { schema: 'chirality-exact-role/v1', evidenceClass: controlled ? 'supplier-candidate-unaccepted' : 'accepted-supply', accountUsed: false, launchEvidence: 'test-only-no-account-exact-vendor-factory', roleObedienceProven: false, roleMechanicallyEnforced: false, ownerLiveProof: false, passed: false, probes: [], reads: [], originObservations: [], execSchemas: [], nativeMetadata: [], brokerInputs: [], adapterEnvelopes: [], bindingEvidenceClass: 'controlled-worker', productionRoleEnvelopeProven: false, adapterEvidence: 'trusted-test-adapter-role-mapping', accountObservations: [], retirementRecords: [], compatibility: fixtureCompatibility };

  let modelRequests = 0, processes = 0, closedProcesses = 0, childObserved = false;
  const calls = new Map<string, 'spawn' | 'wait'>();
  const origins = new Map<string, FixtureOrigin>();
  const searches = new Map<string, 'spawn' | 'wait'>();
  const readCalls = new Map<string, { who: string; issuedAt: number; observed: boolean }>();
  let phase = 'setup';
  const readBytes = 'ROLE_SYNTHETIC_READ_BYTES', deniedBytes = 'ROLE_SYNTHETIC_DENIED_BYTES';
  try {
    phase = 'source-pins'; result.sourcesBefore = await pins();
    phase = 'supplier-verification'; const supply = await verify(supplied); result.supplySha256 = supply.sha256;
    phase = 'scratch-setup'; const created = await mkdtemp(join(await realpath('/tmp'), 'erc-')); cleanups.push(() => rm(created, { recursive: true, force: true }));
    base = await realpath(created); root = join(base, 'p'); broker = join(base, 'r'); worker = join(broker, 'w'); home = join(worker, 'h'); allowed = join(root, 'allowed.txt'); denied = join(broker, 'denied.txt');
    const { manifestPath } = await createProjectFixture(root, 'role-project');
    await mkdir(worker, { recursive: true, mode: 0o700 }); await chmod(broker, 0o700); await mkdir(home, { mode: 0o700 });
    await writeFile(allowed, readBytes, { flag: 'wx', mode: 0o600 }); await writeFile(denied, deniedBytes, { flag: 'wx', mode: 0o600 });
    const peer = createServer(async (req, res) => {
      try {
        if (req.method !== 'POST' || req.url !== '/v1/responses' || req.headers.authorization) throw new Error('Unexpected local peer request');
        const chunks: Buffer[] = []; let bytes = 0;
        for await (const raw of req) { const chunk = Buffer.from(raw); bytes += chunk.length; if (bytes > 2000000) throw new Error('Peer bound'); chunks.push(chunk); }
        const raw = Buffer.concat(chunks), body = JSON.parse((req.headers['content-encoding'] === 'gzip' ? gunzipSync(raw, { maxOutputLength: 4000000 }) : raw).toString());
        if (++modelRequests > 40 || !Array.isArray(body.input) || !Array.isArray(body.tools)) throw new Error('Peer shape');
        let origin: ReturnType<typeof selectOrigin>;
        try { origin = selectOrigin(body.input, origins); }
        catch (error) {
          result.originFailureShape = { request: modelRequests, userItems: body.input.filter((entry: any) => entry.role === 'user').length,
            userTextBlocks: body.input.flatMap((entry: any, index: number) => entry.role === 'user' && Array.isArray(entry.content) ? entry.content.filter((part: any) => part.type === 'input_text' && typeof part.text === 'string').map((part: any) => ({ index, bytes: Buffer.byteLength(part.text), sha256: createHash('sha256').update(part.text).digest('hex') })) : []).slice(0, 64),
            registeredOrigins: [...origins].map(([text, value]) => ({ who: value.who, sha256: createHash('sha256').update(text).digest('hex') })) };
          throw error;
        }
        const who = origin.origin.who;
        const child = who === 'child', nativeParent = who === 'agent1';
        if (child && calls.get(origin.origin.spawnCallId!) !== 'spawn') throw new Error('Native origin lacks issued spawn');
        result.originObservations.push({ who, inputIndex: origin.inputIndex, textSha256: origin.textSha256, ...(origin.origin.spawnCallId ? { spawnCallId: origin.origin.spawnCallId } : {}) });
        if (child) childObserved = true;
        const readOutput = body.input.find((entry: any) => entry.type === 'function_call_output' && readCalls.get(entry.call_id)?.who === who);
        if (readOutput) {
          const record = readCalls.get(readOutput.call_id)!;
          if (!record.observed) {
            record.observed = true;
            const output = typeof readOutput.output === 'string' ? readOutput.output : JSON.stringify(readOutput.output);
            const elapsedMs = Date.now() - record.issuedAt, passed = standaloneRead(output, who);
            result.reads.push({ who, callId: readOutput.call_id, elapsedMs, passed, outputSha256: createHash('sha256').update(output).digest('hex') });
            if (!passed || elapsedMs > 10000) throw new Error('Actual role read/denial failed or exceeded budget');
          }
        }
        let item: any = { type: 'message', id: `msg_${modelRequests}`, role: 'assistant', status: 'completed', content: [{ type: 'output_text', text: child ? 'ROLE_CHILD_FINISHED' : 'ROLE_PRIMARY_FINISHED', annotations: [] }] };
        if (!readOutput) {
          if ([...readCalls.values()].some(record => record.who === who)) throw new Error('Issued role read output missing');
          const tool = nativeTool(body.tools, ['exec_command']);
          const command = [`printf 'ROLE_${who}_START\\n'`, `if [ \"$(/bin/cat ${quote(allowed)})\" = ${quote(readBytes)} ]; then printf 'ROLE_${who}_READ_OK\\n'; fi`, `if /bin/cat ${quote(denied)} >/dev/null 2>&1; then printf 'ROLE_${who}_DENIAL_FAILED\\n'; else printf 'ROLE_${who}_DENIED\\n'; fi`, `printf 'ROLE_${who}_FINISH\\n'`].join('; ');
          // Property names only: no descriptions, prompts, command text or credentials in schema diagnostics.
          result.execSchemas.push({ who, name: tool.name, namespace: tool.namespace ?? null, properties: Object.keys(tool.parameters.properties ?? {}).slice(0, 64), required: (tool.parameters.required ?? []).slice(0, 64) });
          const args = execReadArguments(tool, command, root);
          const callId = `read_${modelRequests}`; readCalls.set(callId, { who, issuedAt: Date.now(), observed: false });
          item = { type: 'function_call', id: `fc_${modelRequests}`, call_id: callId, name: tool.name, ...(tool.namespace ? { namespace: tool.namespace } : {}), arguments: JSON.stringify(args), status: 'completed' };
        } else if (nativeParent) {
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
            if (!spawned) args = { message: childPrompt };
            else { const value = JSON.parse(spawned.output), id = value.agent_id ?? value.id; if (typeof id !== 'string' || id.length > 256) throw new Error('Actual native child ID absent'); result.nativeChildId = id; args = { [tool.name === 'wait_agent' ? 'targets' : 'ids']: [id] }; }
            if ((tool.parameters.required ?? []).some((key: string) => !(key in args)) || Object.keys(args).some(key => !tool.parameters.properties?.[key])) throw new Error('Unknown native schema');
            const callId = `native_${modelRequests}`; calls.set(callId, spawned ? 'wait' : 'spawn');
            if (!spawned) { if (origins.has(childPrompt)) throw new Error('Duplicate native origin'); origins.set(childPrompt, { who: 'child', primaryRole: 'agent1', spawnCallId: callId }); }
            item = { type: 'function_call', id: `fc_${modelRequests}`, call_id: callId, name: tool.name, ...(tool.namespace ? { namespace: tool.namespace } : {}), arguments: JSON.stringify(args), status: 'completed' };
            }
          }
        }
        const response = { id: `resp_${modelRequests}`, object: 'response', model: 'runtime-deterministic', status: 'completed', output: [item], usage: { input_tokens: 1, output_tokens: 1, total_tokens: 2 } };
        const frames = [{ type: 'response.created', response: { ...response, status: 'in_progress', output: [] } }, { type: 'response.output_item.added', output_index: 0, item: { ...item, ...(item.type === 'function_call' ? { arguments: '' } : item.type === 'tool_search_call' ? {} : { content: [] }) } }, ...(item.type === 'function_call' ? [{ type: 'response.function_call_arguments.delta', item_id: item.id, output_index: 0, delta: item.arguments }, { type: 'response.function_call_arguments.done', item_id: item.id, output_index: 0, arguments: item.arguments }] : []), { type: 'response.output_item.done', output_index: 0, item }, { type: 'response.completed', response }];
        res.writeHead(200, { 'Content-Type': 'text/event-stream' }).end(frames.map((frame, sequence_number) => `event: ${frame.type}\ndata: ${JSON.stringify({ ...frame, sequence_number, response_id: response.id })}\n\n`).join(''));
      } catch (error) { result.peerFailure = true; result.peerFailureReason = error instanceof Error ? error.message.slice(0, 300) : 'unknown'; res.writeHead(400).end('{}'); }
    });
    await new Promise<void>(resolve => peer.listen(0, '127.0.0.1', resolve)); cleanups.push(() => new Promise<void>(resolve => { peer.closeAllConnections(); peer.close(() => resolve()); }));
    const binary = join(worker, 'app-server'); await copyFile(supplied, binary); await chmod(binary, 0o700);
    const policy = await prepareCodexNativePolicy({ canonicalRoot: root, codexHome: home, privateDirectory: worker, protectedPaths: [broker], immutableReadRoots: ['/bin', '/usr/lib', '/usr/bin/curl', '/System/Volumes/Preboot/Cryptexes/OS/System/Library/dyld'], commandNetworkPosture: 'off' });
    cleanups.push(() => policy.cleanup()); result.nativePolicyDigest = policy.policyDigest; result.expectedPermissions = policy.expectedPermissions;
    const identity = { canonicalRoot: root, cwd: root, accountId: 'no-account-test', accountEpoch: 1, policyDigest: policy.policyDigest };
    const workers = CodexSupervisor.controlledForTests({ commandNetworkPosture: 'off', allowUnauthenticatedModel: true, identity, model: 'runtime-deterministic', requestTimeoutMs: 10000, turnTimeoutMs: 10000, launch: async () => {
      await verify(binary); const launch = await policy.launchArguments(binary);
      const config = ['model_provider="runtime_deterministic"', 'model="runtime-deterministic"', 'model_providers.runtime_deterministic.name="Owned deterministic peer"', `model_providers.runtime_deterministic.base_url="http://127.0.0.1:${(peer.address() as { port: number }).port}/v1"`, 'model_providers.runtime_deterministic.wire_api="responses"', 'model_providers.runtime_deterministic.requires_openai_auth=false', 'model_providers.runtime_deterministic.supports_websockets=false', 'model_providers.runtime_deterministic.stream_max_retries=0', 'model_providers.runtime_deterministic.request_max_retries=0', 'features.multi_agent=true'];
      const child = spawn(launch[0]!, [...launch.slice(1), ...config.flatMap(value => ['-c', value])], { cwd: root, env: policy.environment, detached: true, stdio: 'pipe' }); processes++;
      const closed = new Promise<void>(resolve => child.once('close', () => { closedProcesses++; resolve(); }));
      const kill = () => { if (child.pid) try { process.kill(-child.pid, 'SIGKILL'); } catch {} }; child.on('error', () => {}); child.once('exit', kill);
      let wire = '';
      child.stdout.on('data', (chunk: Buffer) => {
        wire += chunk.toString(); if (wire.length > 2000000) { result.wireOverflow = true; kill(); return; }
        for (let newline; (newline = wire.indexOf('\n')) >= 0;) {
          const line = wire.slice(0, newline); wire = wire.slice(newline + 1);
          try { const message = JSON.parse(line);
            if (message.result && Object.hasOwn(message.result, 'account') && Object.hasOwn(message.result, 'requiresOpenaiAuth')) result.accountObservations.push({ hasAccount: message.result.account !== null, authRequired: message.result.requiresOpenaiAuth });
            if (message.method === 'thread/started') { const thread = message.params?.thread; if (typeof thread?.id === 'string') result.nativeMetadata.push({ method: message.method, threadId: thread.id, source: thread.source ?? null }); }
            if (['item/started', 'item/completed'].includes(message.method) && message.params?.item?.type === 'collabAgentToolCall') result.nativeMetadata.push({ method: message.method, threadId: message.params.threadId, turnId: message.params.turnId, receiverThreadIds: message.params.item.receiverThreadIds });
            if (result.nativeMetadata.length > 64) { result.wireOverflow = true; kill(); }
          } catch { result.wireParseFailure = true; }
        }
      });
      let bytes = 0; child.stderr.on('data', (chunk: Buffer) => { bytes += chunk.length; if (bytes > 65536) kill(); });
      const timer = setTimeout(kill, Math.max(1, Math.min(12000, 60000 - (Date.now() - started))));
      try { await new Promise<void>((resolve, reject) => { child.once('spawn', resolve); child.once('error', reject); }); } catch { clearTimeout(timer); kill(); await closed; throw new Error('Candidate did not spawn'); }
      return { pid: child.pid!, descendantTracker: new DescendantTracker({ leaderPid: child.pid!, intervalMs: 100, maxDurationMs: 60000 }), permissionProfile: policy.permissionProfile, policyDigest: policy.policyDigest, expectedPermissions: policy.expectedPermissions, transport: { stdin: child.stdin, stdout: child.stdout, close: async () => { clearTimeout(timer); kill(); await closed; } } };
    } });
    cleanups.push(() => workers.close());
    const server = await startSupervisorServer({ socketPath: join(broker, 's.sock'), supervisor: workers }); cleanups.push(() => server.close());
    const privateClient = new SupervisorClient({ socketPath: join(broker, 's.sock'), credential: server.credential });
    const compatibility = fixtureCompatibility;
    phase = 'public-preflight';
    const consent = new HostedConsentStore({ canonicalRoot: root, codexHome: home });
    const actual = { adapterId: 'codex', providerId: 'runtime_deterministic', model: 'runtime-deterministic' };
    const rolePolicy: RolePolicySettings = { allowedTools: [], readRoots: [root], writeRoots: [root], networkPosture: 'off', processPolicy: 'broker-managed', delegationPolicy: 'native descent does not assign a role' };
    // Controlled-worker transports raw prompt. This explicit fixture adapter selects a sealed role
    // by worker identity; its envelope is adapter-created evidence, never broker-emitted evidence.
    const supervisor = { acquire: (id: string, prompt: string) => {
      const role = roles.find(role => id === `role-${role}`); if (!role) throw new Error('Unmapped fixture worker role');
      const original = actorPrompt(role, prompt); if (origins.has(original)) throw new Error('Duplicate primary origin'); origins.set(original, { who: role, primaryRole: role });
      result.brokerInputs.push({ workerId: id, promptSha256: createHash('sha256').update(prompt).digest('hex'), transport: 'raw-prompt' });
      const envelope = { prompt, requestedRole: role, roleEvidence: createRolePolicyEvidence({ role, actual, policy: rolePolicy }) };
      result.adapterEnvelopes.push({ workerId: id, requestedRole: role, roleEvidence: envelope.roleEvidence, origin: 'trusted-test-adapter' });
      return privateClient.acquire(id, JSON.stringify(envelope));
    }, inventory: privateClient.inventory.bind(privateClient), reconnect: privateClient.reconnect.bind(privateClient), wait: privateClient.wait.bind(privateClient), retire: privateClient.retire.bind(privateClient), verifyHostedBoundary: privateClient.verifyHostedBoundary.bind(privateClient) };
    const retirement = new WorkerRetirementCoordinator({ directory: join(broker, 'retirement') });
    const delegated = new DelegatedRuntime({ daemonId: 'exact-role-test', projects: new Map([['role-project', { identity, compatibility, supervisor, consent, retirement, commandNetworkPosture: 'off', actual, rolePolicy, evidenceClass: 'controlled-worker' as const }]]) });
    const directory = join(broker, 'runtime'), projects = new ProjectRegistry(directory), sessions = new SessionStore(directory, projects), engines = new EngineRegistry(), residency = new ResidencyCoordinator({ async listStatus() { return []; }, async load() {}, async unload() {} }, directory);
    const service = new RuntimeService(projects, sessions, engines, residency, new TurnCoordinator(projects, sessions, engines, residency), new AuthRegistry(directory), { async get() { return undefined; }, async status() { return { configured: false }; }, async set() {}, async remove() {} });
    const registered = await service.registerProject(manifestPath, 'fixture-operator', 'exact-role-fixture-only');
    const daemon = new RuntimeDaemon({ socketPath: join(broker, 'd.sock'), runtimeDirectory: directory, service, delegated }); await daemon.start(); cleanups.push(() => daemon.stop());
    const client = new RuntimeClient({ socketPath: join(broker, 'd.sock'), tokenFile: registered.tokenFile });
    expect((await client.delegatedCapabilities('role-project')).offeredRoles).toEqual([...roles]);
    await client.grantDelegatedConsent('role-project', compatibility, { posture: 'off', approvedBy: 'fixture-operator', explicitUserAct: true });
    const initialProcesses = processes;
    await expect(privateClient.acquire('forged-role', JSON.stringify({ prompt: 'none', requestedRole: 'agent2', roleEvidence: { selectedRole: 'agent2', enforcementLabel: 'mechanically enforced', evidencePosture: 'mechanism-proven' } }))).rejects.toThrow();
    result.forgedMechanicalLabelRejected = true;
    await expect(client.runDelegatedTurn('other-project', compatibility, { turnId: 'forbidden', prompt: 'none' })).rejects.toThrow();
    await expect(client.runDelegatedTurn('role-project', { ...compatibility, contractBasisSha256: '0'.repeat(64) }, { turnId: 'bad-basis', prompt: 'none' })).rejects.toThrow();
    expect(processes).toBe(initialProcesses); result.scopeFences = true;
    let settings: unknown;
    for (const role of roles) {
      if (Date.now() - started > 50000) throw new Error('Profile budget');
      phase = `role-${role}`;
      const before = Date.now();
      const response = await client.runDelegatedTurn('role-project', compatibility, { turnId: `role-${role}`, prompt: `ROLE_SELECTION_${role}: ${role === 'agent1' ? 'ROLE_NATIVE_PARENT: run the deterministic read and native child then finish.' : 'ROLE_PRIMARY_ONLY: run the deterministic read then finish.'}`, ...(role === 'untyped' ? {} : { requestedRole: role }) });
      expect(response.terminal.outcome).toBe('completed'); expect(response.roleEvidence.selectedRole).toBe(role); expect(response.roleEvidence.offeredRoles).toEqual([...roles]);
      expect(response.roleEvidence.enforcementLabel).toBe('role not mechanically enforced'); expect(response.roleEvidence.evidencePosture).toBe('instruction-asserted'); expect(response.roleEvidence.actual).toEqual(actual);
      const extended = response.roleEvidence as typeof response.roleEvidence & { nativeDescendant?: boolean; settings?: unknown };
      expect(extended.nativeDescendant).toBe(false); expect(extended.settings).toBeDefined();
      if (settings === undefined) settings = extended.settings; else expect(extended.settings).toEqual(settings);
      const retired = await retirement.read(`role-${role}`); expect(retired).toMatchObject({ state: 'committed', identity, rolePolicyDigest: response.roleEvidence.policyDigest }); result.retirementRecords.push(retired);
      const envelope = result.adapterEnvelopes.find((entry: any) => entry.workerId === `role-${role}`); expect(envelope.requestedRole).toBe(role); expect(envelope.roleEvidence).toEqual(response.roleEvidence);
      if (role === 'agent1') { result.primaryThreadId = retired?.threadId; expect(typeof result.primaryThreadId).toBe('string'); expect(result.nativeChildId).not.toBe(result.primaryThreadId); }
      const elapsedMs = Date.now() - before; result.probes.push({ role, elapsedMs, roleEvidence: response.roleEvidence, outcome: response.terminal.outcome, nativePolicyDigest: policy.policyDigest }); expect(elapsedMs).toBeLessThanOrEqual(10000);
    }
    expect(childObserved && result.nativeWaitCompleted === true && typeof result.nativeChildId === 'string').toBe(true);
    result.nativeDescentDidNotAssignRuntimeRole = result.probes.find((probe: any) => probe.role === 'agent1').roleEvidence.selectedRole === 'agent1';
    expect(result.accountObservations).toHaveLength(5); expect(result.accountObservations.every((entry: any) => entry.hasAccount === false && entry.authRequired === false)).toBe(true);
    expect(result.reads).toHaveLength(6); expect(result.reads.every((read: any) => read.passed && read.elapsedMs <= 10000)).toBe(true);
    expect(result.nativeMetadata.some((entry: any) => entry.threadId === result.primaryThreadId && entry.receiverThreadIds?.includes(result.nativeChildId))).toBe(true);
    phase = 'native-SessionMeta';
    result.nativeChildMetadata = await readNativeSessionMetadata(home, result.nativeChildId, result.primaryThreadId, root);
    expect(result.brokerInputs).toHaveLength(5); expect(result.adapterEnvelopes).toHaveLength(5);
    expect(await readFile(allowed, 'utf8')).toBe(readBytes); expect(await readFile(denied, 'utf8')).toBe(deniedBytes); result.hostSentinelsUnchanged = true;
    result.identity = identity;
    await verify(binary); await verify(supplied); result.supplyRevalidated = true; result.passed = true;
  } catch (error) { result.failurePhase = phase; result.failure = error instanceof Error ? error.message.slice(0, 400) : 'unclassified'; }
  finally {
    let failures = 0; for (const cleanup of cleanups.reverse()) try { await cleanup(); } catch { failures++; }
    result.cleanupFailures = failures; result.processes = processes; result.closedProcesses = closedProcesses; result.modelRequests = modelRequests; result.childObserved = childObserved; result.elapsedMs = Date.now() - started; result.profileBudgetMs = 60000; result.probeBudgetMs = 10000; try { result.sourcesAfter = await pins(); result.sourceStable = result.sourcesBefore !== undefined && JSON.stringify(result.sourcesBefore) === JSON.stringify(result.sourcesAfter); } catch { result.sourceStable = false; result.sourcePinFailure = true; }
    result.passed = result.passed && failures === 0 && processes === closedProcesses && result.elapsedMs <= 60000 && result.sourceStable && !result.peerFailure && !result.wireOverflow && !result.wireParseFailure;
    await mkdir(evidence, { recursive: true, mode: 0o700 }); await writeFile(join(evidence, 'EXACT_ROLE_CANARY.json'), JSON.stringify(result, null, 2) + '\n', { mode: 0o600, flag: 'wx' });
  }
  expect(result.passed, 'Exact role fixture failed; inspect calibrated evidence').toBe(true);
}, 70000);
