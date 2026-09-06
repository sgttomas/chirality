import { spawn } from 'node:child_process';
import { constants } from 'node:fs';
import { createHash } from 'node:crypto';
import { createServer } from 'node:http';
import { gunzipSync } from 'node:zlib';
import { chmod, copyFile, lstat, mkdir, mkdtemp, open, readFile, realpath, rm, symlink, writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import { expect, it } from 'vitest';
import { createControlledSupplyVerifierForTests, verifyExactSupply } from '../packages/core/src/exact-supply.js';
import { CodexSupervisor } from '../packages/daemon/src/codex-supervisor.js';
import { prepareCodexNativePolicy } from '../packages/daemon/src/codex-containment.js';
import { AuthRegistry, EngineRegistry, ProjectRegistry, ResidencyCoordinator, RuntimeService, SessionStore, TurnCoordinator, DescendantTracker } from '@chirality/runtime-core';
import { RuntimeClient } from '@chirality/runtime-client';
import { RuntimeDaemon } from '../packages/daemon/src/runtime-daemon.js';
import { DelegatedRuntime } from '@chirality/runtime-core';
import { ApprovalStore } from '@chirality/runtime-core';
import { HostedConsentStore } from '@chirality/runtime-core';
import { WorkerRetirementCoordinator } from '@chirality/runtime-core';
import { createProjectFixture } from './helpers.js';
import { startSupervisorServer, SupervisorClient } from '../packages/daemon/src/supervisor-server.js';

// Fixture grammar is real; the digest remains explicitly test-only, never accepted production authority.
const fixtureCompatibility = { compatibilityIdentity: 'root-runtime-1', contractBasisSha256: createHash('sha256').update('test-only-exact-network-binding').digest('hex') };
it('uses valid fixture compatibility without relaxing broker preflight', async () => {
  const binding = { compatibility: fixtureCompatibility, evidenceClass: 'controlled-worker', identity: {}, supervisor: {}, consent: {} };
  const runtime = new DelegatedRuntime({ daemonId: 'network-metadata-fixture', projects: new Map([['p', binding as any]]) });
  expect(await runtime.preflight('p', 'turn:network')).toMatchObject({ ...fixtureCompatibility, projectId: 'p', operationId: 'turn:network' });
  const malformed = new DelegatedRuntime({ daemonId: 'network-metadata-fixture', projects: new Map([['p', { ...binding, compatibility: { ...fixtureCompatibility, compatibilityIdentity: 'exact-network-test' } } as any]]) });
  await expect(malformed.preflight('p', 'turn:network')).rejects.toThrow('Daemon compatibility basis is unavailable');
});

// Diagnostics are observational only: no callback values become approval authority.
function diagnosticRecord(value: unknown): Record<string, unknown> | undefined {
  return value !== null && typeof value === 'object' && !Array.isArray(value) ? value as Record<string, unknown> : undefined;
}
function diagnosticMetadata(value: unknown) {
  const serialized = JSON.stringify(value) ?? 'undefined';
  return { type: value === null ? 'null' : Array.isArray(value) ? 'array' : typeof value, bytes: Buffer.byteLength(serialized), sha256: createHash('sha256').update(serialized).digest('hex') };
}
function diagnosticId(value: unknown, expected?: unknown) {
  return { ...diagnosticMetadata(value), stringLength: typeof value === 'string' ? value.length : null, stringBytes: typeof value === 'string' ? Buffer.byteLength(value) : null,
    matchesCurrentIdentifier: typeof value === 'string' && /^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/.test(value),
    hasControlCharacters: typeof value === 'string' && /[\x00-\x1f\x7f]/.test(value),
    matchesObservedPrimary: typeof expected === 'string' && typeof value === 'string' ? value === expected : null,
    supplierNetworkShape: typeof value === 'string' && value.length <= 1024 && /^network#[^#\x00-\x20\x7f]+#(?:http|https|socks5_tcp|socks5_udp)#[^#\x00-\x20\x7f]+#[0-9]{1,5}#[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i.test(value) };
}
function diagnosticChoice(value: unknown, expectedHost: string) {
  const unknown = () => ({ tag: 'UNKNOWN', ...diagnosticMetadata(value) });
  if (typeof value === 'string' && ['accept', 'acceptForSession', 'decline', 'cancel'].includes(value)) return { tag: value };
  const object = diagnosticRecord(value);
  if (!object || Object.keys(object).length !== 1) return unknown();
  const network = diagnosticRecord(object.applyNetworkPolicyAmendment);
  const amendment = diagnosticRecord(network?.network_policy_amendment);
  if (network && Object.keys(network).join(',') === 'network_policy_amendment' && amendment && Object.keys(amendment).sort().join(',') === 'action,host' && typeof amendment.host === 'string' && amendment.host.length <= 253 && (amendment.action === 'allow' || amendment.action === 'deny')) {
    return { tag: 'applyNetworkPolicyAmendment', action: amendment.action, hostMatchesExpected: amendment.host === expectedHost };
  }
  const exec = diagnosticRecord(object.acceptWithExecpolicyAmendment);
  if (exec && Object.keys(exec).join(',') === 'execpolicy_amendment' && Array.isArray(exec.execpolicy_amendment) && exec.execpolicy_amendment.length <= 16 && exec.execpolicy_amendment.every(part => typeof part === 'string' && part.length <= 4096)) {
    return { tag: 'acceptWithExecpolicyAmendment', argumentCount: exec.execpolicy_amendment.length, ...diagnosticMetadata(exec.execpolicy_amendment) };
  }
  return unknown();
}
function diagnosticCallback(message: Record<string, unknown>, expectedHost: string, primary: { threadId?: unknown; turnId?: unknown }) {
  const params = diagnosticRecord(message.params) ?? {};
  const context = diagnosticRecord(params.networkApprovalContext);
  const choices = params.availableDecisions;
  const knownKeys = ['threadId', 'turnId', 'itemId', 'startedAtMs', 'environmentId', 'reason', 'networkApprovalContext', 'proposedNetworkPolicyAmendments', 'availableDecisions', 'approvalId', 'additionalPermissions', 'proposedExecpolicyAmendment', 'command', 'cwd', 'commandActions'];
  return { method: message.method === 'item/commandExecution/requestApproval' ? message.method : 'OTHER', parameterKeys: Object.keys(params).filter(key => knownKeys.includes(key)), unknownParameterKeys: diagnosticMetadata(Object.keys(params).filter(key => !knownKeys.includes(key))),
    requestId: diagnosticId(message.id), threadId: diagnosticId(params.threadId, primary.threadId), turnId: diagnosticId(params.turnId, primary.turnId), itemId: diagnosticId(params.itemId), environmentId: diagnosticId(params.environmentId),
    startedAtMsValid: Number.isSafeInteger(params.startedAtMs) && Number(params.startedAtMs) >= 0,
    networkContext: context ? { host: context.host === expectedHost ? expectedHost : 'OTHER', protocol: context.protocol === 'http' ? 'http' : 'OTHER', exactKeys: Object.keys(context).sort().join(',') === 'host,protocol' } : undefined,
    availableDecisions: { type: diagnosticMetadata(choices).type, count: Array.isArray(choices) ? choices.length : null, withinBound: Array.isArray(choices) && choices.length <= 16,
      duplicates: Array.isArray(choices) && choices.length <= 16 ? new Set(choices.map(value => diagnosticMetadata(value).sha256)).size !== choices.length : null,
      choices: Array.isArray(choices) ? choices.slice(0, 16).map(value => diagnosticChoice(value, expectedHost)) : [], ...(Array.isArray(choices) ? {} : { unknown: diagnosticMetadata(choices) }) } };
}
function diagnosticFailure(error: unknown) {
  const value = diagnosticRecord(error);
  const messages: Record<string, string> = {
    'Invalid Codex identifier': 'INVALID_CODEX_IDENTIFIER', 'Network request is outside the active primary turn': 'FOREIGN_PRIMARY_TURN',
    'Invalid network request ID': 'INVALID_NETWORK_REQUEST_ID', 'Invalid network approval timestamp': 'INVALID_NETWORK_TIMESTAMP',
    'Unsupported combined approval request': 'COMBINED_APPROVAL', 'Invalid network destination context': 'INVALID_NETWORK_CONTEXT',
    'Exact available approval decisions required': 'MISSING_EXACT_CHOICES', 'Unknown approval decision': 'UNKNOWN_CHOICE',
    'No valid exact network choices': 'NO_VALID_EXACT_CHOICES', 'Conflicting or stale network approval request': 'CONFLICTING_APPROVAL',
    'Server request ID reused across capability classes': 'REUSED_REQUEST_ID', 'Network approval inventory bound exceeded': 'APPROVAL_INVENTORY_BOUND',
    'Network approval requires trusted ask posture': 'WRONG_NETWORK_POSTURE', 'supervisor request rejected': 'BROKER_REJECTED',
  };
  return { classification: typeof value?.message === 'string' && Object.hasOwn(messages, value.message) ? messages[value.message] : 'UNCLASSIFIED',
    code: value?.code === 'ENGINE_UNAVAILABLE' || value?.code === 'INVALID_REQUEST' ? value.code : 'UNCLASSIFIED',
    reason: diagnosticRecord(value?.details)?.reason === 'CODEX_PROTOCOL_FAILURE' ? 'CODEX_PROTOCOL_FAILURE' : 'UNCLASSIFIED' };
}
function observeDiagnosticFailure<A extends unknown[], R>(original: (...args: A) => Promise<R>, record: (failure: ReturnType<typeof diagnosticFailure>) => void): (...args: A) => Promise<R> {
  return async (...args) => { try { return await original(...args); } catch (error) { try { record(diagnosticFailure(error)); } catch { /* diagnostics cannot replace the original rejection */ } throw error; } };
}
it('records closed callback diagnostics without raw IDs, unknown values or command data', () => {
  const secret = 'Bearer fixture-secret-not-for-output';
  const itemId = 'network#local#http#example.com#80#00000000-0000-4000-8000-000000000000';
  const observed = diagnosticCallback({ id: 1, method: 'item/commandExecution/requestApproval', params: { threadId: secret, turnId: 'turn', itemId, startedAtMs: 1, reason: secret, command: secret, [secret]: secret, networkApprovalContext: { host: 'example.com', protocol: 'http' }, availableDecisions: ['accept', 'acceptForSession', { applyNetworkPolicyAmendment: { network_policy_amendment: { host: 'example.com', action: 'allow' } } }, 'cancel', secret, { [secret]: secret }, { applyNetworkPolicyAmendment: { network_policy_amendment: { host: secret, action: secret } } }] } }, 'example.com', { threadId: secret, turnId: 'turn' });
  expect(JSON.stringify(observed)).not.toContain(secret); expect(JSON.stringify(observed)).not.toContain(itemId);
  expect(observed.itemId).toMatchObject({ supplierNetworkShape: true, matchesCurrentIdentifier: false });
  expect(observed.threadId.matchesObservedPrimary).toBe(true); expect(observed.turnId.matchesObservedPrimary).toBe(true);
  expect(observed.availableDecisions.choices.map(value => value.tag)).toEqual(['accept', 'acceptForSession', 'applyNetworkPolicyAmendment', 'cancel', 'UNKNOWN', 'UNKNOWN', 'UNKNOWN']);
  expect(observed.availableDecisions.choices).not.toContainEqual({ tag: 'decline' });
  expect(diagnosticId('wrong', 'expected').matchesObservedPrimary).toBe(false); expect(diagnosticId('unknown').matchesObservedPrimary).toBeNull();
  for (const value of [null, {}, [], 'x'.repeat(4096), 'network#bad\ncontrol']) { const metadata = diagnosticId(value); expect(metadata.matchesCurrentIdentifier).toBe(false); expect(metadata.supplierNetworkShape).toBe(false); }
  expect(diagnosticId('network#bad\ncontrol').hasControlCharacters).toBe(true);
  const bounded = diagnosticCallback({ params: { availableDecisions: Array(17).fill(secret) } }, 'example.com', {});
  expect(bounded.availableDecisions.withinBound).toBe(false); expect(bounded.availableDecisions.choices).toHaveLength(16); expect(JSON.stringify(bounded)).not.toContain(secret);
});
it('observes only allowlisted failure classes and preserves the original failure and terminal outcome', async () => {
  const error = Object.assign(new Error('Invalid Codex identifier'), { code: 'ENGINE_UNAVAILABLE', details: { reason: 'CODEX_PROTOCOL_FAILURE', secret: 'not-retained' } });
  const failures: unknown[] = [];
  const wrapped = observeDiagnosticFailure(async (_worker: string) => { throw error; }, value => failures.push(value));
  await expect(wrapped('worker')).rejects.toBe(error);
  expect(failures).toEqual([{ classification: 'INVALID_CODEX_IDENTIFIER', code: 'ENGINE_UNAVAILABLE', reason: 'CODEX_PROTOCOL_FAILURE' }]);
  let successfulTerminal = false;
  await wrapped('worker').then(() => { successfulTerminal = true; }, () => {});
  expect(successfulTerminal).toBe(false);
  await expect(observeDiagnosticFailure(async () => { throw error; }, () => { throw new Error('observer failure'); })()).rejects.toBe(error);
  const success = { exitCode: 0 }; expect(await observeDiagnosticFailure(async () => success, () => { throw new Error('must not run'); })()).toBe(success);
  expect(diagnosticFailure(new Error('Bearer fixture-secret-not-for-output'))).toEqual({ classification: 'UNCLASSIFIED', code: 'UNCLASSIFIED', reason: 'UNCLASSIFIED' });
  expect(diagnosticFailure(new Error('toString')).classification).toBe('UNCLASSIFIED');
});

// Read-only host audit of isolated fixture evidence; never an approval API or liveness override.
const auditDigest = (value: unknown) => createHash('sha256').update(JSON.stringify(value)).digest('hex');
const auditUuid = /^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/;
async function readCancellationAuditRecord(directory: string, basename: string): Promise<unknown | undefined> {
  if (/[^A-Za-z0-9._-]/.test(basename) || !/^(?:[0-9a-f-]{36}\.(?:request|decision|resolution)|[A-Za-z0-9][A-Za-z0-9._-]{0,127}\.(?:prepared|terminal|thread))\.json$/.test(basename)) throw new Error('Unsafe cancellation audit basename');
  if (await realpath(directory) !== directory) throw new Error('Noncanonical cancellation audit directory');
  const parent = await lstat(directory);
  if (!parent.isDirectory() || parent.isSymbolicLink() || (parent.mode & 0o077) !== 0 || (process.getuid && parent.uid !== process.getuid())) throw new Error('Unsafe cancellation audit directory');
  let handle;
  try { handle = await open(join(directory, basename), constants.O_RDONLY | constants.O_NOFOLLOW); }
  catch (error) { if ((error as NodeJS.ErrnoException).code === 'ENOENT') return undefined; throw error; }
  try {
    const before = await handle.stat(), bound = 65536;
    if (!before.isFile() || (before.mode & 0o077) !== 0 || (process.getuid && before.uid !== process.getuid()) || before.size > bound) throw new Error('Unsafe cancellation audit record');
    const bytes = Buffer.alloc(bound + 1); let length = 0;
    while (length <= bound) { const read = await handle.read(bytes, length, bytes.length - length, null); if (read.bytesRead === 0) break; length += read.bytesRead; }
    const after = await handle.stat();
    if (length > bound || length !== before.size || before.size !== after.size || before.mtimeMs !== after.mtimeMs || before.ctimeMs !== after.ctimeMs || before.ino !== after.ino || before.dev !== after.dev) throw new Error('Cancellation audit record changed or exceeded bound');
    return JSON.parse(bytes.subarray(0, length).toString('utf8'));
  } finally { await handle.close(); }
}
function verifyInterruptAcknowledgement(value: unknown, turnId: string, generation: string) {
  const ack = diagnosticRecord(value);
  if (!ack || Object.keys(ack).sort().join(',') !== 'interrupted,turnId,workerGeneration' || ack.interrupted !== true || ack.turnId !== turnId || ack.workerGeneration !== generation) throw new Error('Uncorrelated interrupt acknowledgement');
  return { interrupted: true, turnMatched: true, generationMatched: true };
}
it('requires the actual interrupt acknowledgement to match this turn and worker generation', () => {
  const ack = { interrupted: true, turnId: 'network-turn', workerGeneration: 'generation' };
  expect(verifyInterruptAcknowledgement(ack, 'network-turn', 'generation')).toEqual({ interrupted: true, turnMatched: true, generationMatched: true });
  for (const value of [null, {}, { ...ack, interrupted: false }, { ...ack, turnId: 'foreign' }, { ...ack, workerGeneration: 'stale' }, { ...ack, extra: true }]) expect(() => verifyInterruptAcknowledgement(value, 'network-turn', 'generation')).toThrow();
});
async function auditInterruptedApproval(broker: string, expected: Awaited<ReturnType<ApprovalStore['read']>>['request']) {
  const requestId = expected.requestId, turnId = expected.binding.turnId;
  if (!auditUuid.test(requestId) || /[^A-Za-z0-9._-]/.test(turnId) || !/^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/.test(turnId)) throw new Error('Unsafe cancellation audit identity');
  const approvalDirectory = join(broker, 'approvals'), retirementDirectory = join(broker, 'retirement');
  const request = diagnosticRecord(await readCancellationAuditRecord(approvalDirectory, `${requestId}.request.json`));
  const decision = await readCancellationAuditRecord(approvalDirectory, `${requestId}.decision.json`);
  const rawResolution = await readCancellationAuditRecord(approvalDirectory, `${requestId}.resolution.json`), resolution = diagnosticRecord(rawResolution);
  const prepared = diagnosticRecord(await readCancellationAuditRecord(retirementDirectory, `${turnId}.prepared.json`));
  const committed = diagnosticRecord(await readCancellationAuditRecord(retirementDirectory, `${turnId}.terminal.json`));
  const terminal = diagnosticRecord(committed?.terminal), identity = diagnosticRecord(prepared?.identity), binding = diagnosticRecord(request?.binding);
  const continuityKeys = ['canonicalRoot', 'cwd', 'accountId', 'accountEpoch', 'policyDigest'] as const;
  const fullBindingKeys = [...continuityKeys, 'sessionId', 'turnId', 'workerGeneration', 'scopeDigest'] as const;
  const requestDigestMatches = request !== undefined && auditDigest(request) === auditDigest(expected);
  const fullBindingMatches = binding !== undefined && fullBindingKeys.every(key => binding[key] === expected.binding[key]);
  const attributedRequest = requestDigestMatches && fullBindingMatches && request?.requestedBy === 'trusted-codex-supervisor';
  const providerResolutionPresent = rawResolution !== undefined;
  const providerResolutionValid = !providerResolutionPresent || (resolution !== undefined && Object.keys(resolution).sort().join(',') === 'reason,requestDigest,requestId,resolvedAt,resolvedBy' && resolution.requestId === requestId && resolution.requestDigest === auditDigest(expected) && resolution.reason === 'provider-resolved' && resolution.resolvedBy === 'trusted-codex-supervisor' && typeof resolution.resolvedAt === 'string' && Number.isFinite(Date.parse(resolution.resolvedAt)));
  const preparedMatches = prepared?.turnId === turnId && prepared.state === 'prepared' && prepared.terminal === undefined && (prepared.rolePolicyDigest === undefined || (typeof prepared.rolePolicyDigest === 'string' && /^[a-f0-9]{64}$/.test(prepared.rolePolicyDigest))) && (prepared.threadId === undefined || (typeof prepared.threadId === 'string' && /^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/.test(prepared.threadId))) && identity !== undefined && continuityKeys.every(key => identity[key] === expected.binding[key]);
  const interruptedRetirement = preparedMatches && committed?.basisDigest === auditDigest(prepared) && terminal?.turnId === turnId && terminal.workerId === turnId && terminal.generation === expected.binding.workerGeneration && terminal.outcome === 'interrupted' && typeof terminal.recordedAt === 'string' && Number.isFinite(Date.parse(terminal.recordedAt));
  let committedThreadValid = true;
  if (committed?.threadDigest !== undefined) {
    const thread = diagnosticRecord(await readCancellationAuditRecord(retirementDirectory, `${turnId}.thread.json`));
    committedThreadValid = thread !== undefined && Object.keys(thread).sort().join(',') === 'basisDigest,threadId' && thread.basisDigest === auditDigest(prepared) && typeof thread.threadId === 'string' && /^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/.test(thread.threadId) && committed.threadDigest === auditDigest(thread) && (prepared?.threadId === undefined || prepared.threadId === thread.threadId);
  }
  return { attributedRequest, requestDigestMatches, fullBindingMatches, decisionAbsent: decision === undefined, providerResolutionPresent, providerResolutionValid, interruptedRetirement, committedThreadValid,
    complete: attributedRequest && decision === undefined && providerResolutionValid && interruptedRetirement && committedThreadValid };
}
it('audits host interruption evidence without inventing provider resolution or a decision', async () => {
  const base = await realpath(await mkdtemp(join(await realpath('/tmp'), 'cancel-audit-'))), broker = join(base, 'broker');
  const approvalDirectory = join(broker, 'approvals'), retirementDirectory = join(broker, 'retirement');
  await mkdir(approvalDirectory, { recursive: true, mode: 0o700 }); await mkdir(retirementDirectory, { mode: 0o700 });
  const requestId = '00000000-0000-4000-8000-000000000001', turnId = 'network-turn';
  const binding = { canonicalRoot: join(base, 'project'), cwd: join(base, 'project'), accountId: 'fixture', accountEpoch: 1, policyDigest: 'fixture-policy', sessionId: turnId, turnId, workerGeneration: 'fixture-generation' };
  const request = { requestId, binding, networkApprovalContext: { host: 'example.com', protocol: 'http' }, requestedBy: 'trusted-codex-supervisor', requestedAt: '2026-09-06T00:00:00Z', consentDigest: 'fixture-consent', caveat: 'fixture' };
  const prepared = { turnId, identity: Object.fromEntries(['canonicalRoot', 'cwd', 'accountId', 'accountEpoch', 'policyDigest'].map(key => [key, binding[key as keyof typeof binding]])), state: 'prepared' };
  const committed = { basisDigest: auditDigest(prepared), terminal: { turnId, workerId: turnId, generation: binding.workerGeneration, outcome: 'interrupted', recordedAt: '2026-09-06T00:00:01Z' } };
  const save = async (directory: string, name: string, value: unknown) => writeFile(join(directory, name), JSON.stringify(value), { mode: 0o600 });
  const requestName = `${requestId}.request.json`, decisionName = `${requestId}.decision.json`, resolutionName = `${requestId}.resolution.json`, terminalName = `${turnId}.terminal.json`;
  try {
    await save(approvalDirectory, requestName, request); await save(retirementDirectory, `${turnId}.prepared.json`, prepared); await save(retirementDirectory, terminalName, committed);
    expect(await auditInterruptedApproval(broker, request)).toMatchObject({ complete: true, attributedRequest: true, decisionAbsent: true, providerResolutionPresent: false, interruptedRetirement: true });
    for (const field of ['canonicalRoot', 'cwd', 'accountId', 'accountEpoch', 'policyDigest', 'sessionId', 'turnId', 'workerGeneration'] as const) {
      await save(approvalDirectory, requestName, { ...request, binding: { ...binding, [field]: field === 'accountEpoch' ? 2 : 'wrong' } });
      expect((await auditInterruptedApproval(broker, request)).complete).toBe(false);
    }
    await save(approvalDirectory, requestName, request);
    await save(approvalDirectory, decisionName, { decision: 'allow' }); expect((await auditInterruptedApproval(broker, request)).complete).toBe(false); await rm(join(approvalDirectory, decisionName));
    for (const change of [{ outcome: 'completed' }, { outcome: 'failed' }, { generation: 'wrong' }, { turnId: 'wrong' }, { workerId: 'wrong' }]) {
      await save(retirementDirectory, terminalName, { ...committed, terminal: { ...committed.terminal, ...change } }); expect((await auditInterruptedApproval(broker, request)).complete).toBe(false);
    }
    await save(retirementDirectory, terminalName, { ...committed, basisDigest: 'wrong' }); expect((await auditInterruptedApproval(broker, request)).complete).toBe(false);
    await save(retirementDirectory, terminalName, committed);
    for (const change of [{ terminal: { outcome: 'failed' } }, { rolePolicyDigest: 'bad' }, { rolePolicyDigest: null }, { threadId: '../foreign' }, { threadId: null }]) {
      const changedPrepared = { ...prepared, ...change };
      await save(retirementDirectory, `${turnId}.prepared.json`, changedPrepared);
      await save(retirementDirectory, terminalName, { ...committed, basisDigest: auditDigest(changedPrepared) });
      expect((await auditInterruptedApproval(broker, request)).complete).toBe(false);
    }
    await save(retirementDirectory, `${turnId}.prepared.json`, prepared); await save(retirementDirectory, terminalName, committed);
    const resolution = { requestId, requestDigest: auditDigest(request), resolvedBy: 'trusted-codex-supervisor', resolvedAt: '2026-09-06T00:00:01Z', reason: 'provider-resolved' };
    await save(approvalDirectory, resolutionName, resolution); expect(await auditInterruptedApproval(broker, request)).toMatchObject({ complete: true, providerResolutionPresent: true, providerResolutionValid: true });
    await save(approvalDirectory, resolutionName, { ...resolution, reason: 'host-interrupted' }); expect((await auditInterruptedApproval(broker, request)).complete).toBe(false); await rm(join(approvalDirectory, resolutionName));
    await rm(join(retirementDirectory, terminalName)); expect((await auditInterruptedApproval(broker, request)).complete).toBe(false); await save(retirementDirectory, terminalName, committed);
    await rm(join(approvalDirectory, requestName)); expect((await auditInterruptedApproval(broker, request)).complete).toBe(false);
    await symlink(join(retirementDirectory, terminalName), join(approvalDirectory, requestName)); await expect(auditInterruptedApproval(broker, request)).rejects.toThrow(); await rm(join(approvalDirectory, requestName));
    await writeFile(join(approvalDirectory, requestName), 'x'.repeat(65537), { mode: 0o600 }); await expect(auditInterruptedApproval(broker, request)).rejects.toThrow('Unsafe cancellation audit record');
    for (const unsafe of ['../outside', '/outside', requestName + '\n']) await expect(readCancellationAuditRecord(approvalDirectory, unsafe)).rejects.toThrow('Unsafe');
    await expect(auditInterruptedApproval(broker, { ...request, requestId: '../outside' })).rejects.toThrow('Unsafe');
  } finally { await rm(base, { recursive: true, force: true }); }
});

const marker = 'OWNED_DESTINATION_REACHED_731A';
function commandEvidence(output: string) {
  const status = /^NETWORK_COMMAND_FINISHED:([0-9]{1,3})\r?$/m.exec(output);
  return { started: /^NETWORK_COMMAND_STARTED\r?$/m.test(output), finished: status !== null, curlStatus: status ? Number(status[1]) : undefined };
}
it('does not count shell abort as command-level denial', () => {
  expect(commandEvidence('exec_command failed: Rejected(printf NETWORK_COMMAND_STARTED)')).toEqual({ started: false, finished: false, curlStatus: undefined });
  expect(commandEvidence('Process exited with code 134')).toEqual({ started: false, finished: false, curlStatus: undefined });
  expect(commandEvidence('NETWORK_COMMAND_STARTED\nNETWORK_COMMAND_FINISHED:7')).toEqual({ started: true, finished: true, curlStatus: 7 });
});
function supplierErrorText(value: string): string {
  return /^(?:exec_command failed(?::| for )|Error parsing function call:|Error executing tool:|Tool execution failed:)/.test(value) ? value.slice(0, 2048) : '';
}
it('retains the actual supplier failed-for diagnostic but discards command response body', () => {
  const actualPrior = "exec_command failed for `/bin/zsh -c \"printf 'NETWORK_COMMAND_STARTED\n'; /usr/bin/curl --silent --show-error --max-time 8 --noproxy '' 'http://127.0.0.1:64122/canary'; curl_status=\"'$?; printf '\"'\nNETWORK_COMMAND_FINISHED:%s\n' \\\"\"'$curl_status\"'`: ProcessFailed { message: \"Network access to \\\"127.0.0.1\\\" was blocked: local/private network addresses are blocked by the sandbox policy.\" }";
  expect(supplierErrorText(actualPrior)).toContain('local/private network addresses are blocked by the sandbox policy');
  expect(commandEvidence(actualPrior).started).toBe(false);
  expect(supplierErrorText('Chunk ID: fixture\nOutput:\nexec_command failed for public body')).toBe('');
});
function commandFor(url: string): string {
  const parsed = new URL(url);
  if (url !== 'http://example.com/' && !(url === parsed.href && parsed.protocol === 'http:' && parsed.hostname === '127.0.0.1' && parsed.pathname === '/canary' && parsed.port && !parsed.username && !parsed.password && !parsed.search && !parsed.hash)) throw new Error('Unapproved network target');
  return `printf 'NETWORK_COMMAND_STARTED\n'; /usr/bin/curl --disable --request GET --silent --show-error --max-time 8 --max-redirs 0 --max-filesize 16384 --noproxy '' --write-out '\nNETWORK_HTTP_STATUS:%{http_code}\n' '${url}'; curl_status=$?; printf '\nNETWORK_COMMAND_FINISHED:%s\n' "$curl_status"`;
}
it('limits public canary to the explicit GET target with ambient curl config and redirects disabled', () => {
  const command = commandFor('http://example.com/');
  expect(command).toContain('/usr/bin/curl --disable --request GET');
  expect(command).toContain('--max-redirs 0 --max-filesize 16384');
  expect(command).not.toContain('--location');
  for (const url of ['https://example.com/', 'http://example.com/?x=1', 'http://example.com/path', 'http://user@example.com/', 'http://unapproved.test/']) expect(() => commandFor(url)).toThrow();
});
type Scenario = 'off' | 'on' | 'ask-allow' | 'ask-deny' | 'ask-cancel';
function scenario(value: string | undefined): Scenario {
  if (value === 'off' || value === 'on' || value === 'ask-allow' || value === 'ask-deny' || value === 'ask-cancel') return value;
  throw new Error('Explicit CHIRALITY_EXACT_NETWORK_SCENARIO required');
}
it('requires a closed explicit network scenario', () => {
  for (const value of ['off', 'on', 'ask-allow', 'ask-deny', 'ask-cancel'] as const) expect(scenario(value)).toBe(value);
  for (const value of [undefined, '', 'allow', 'ask', 'ON']) expect(() => scenario(value)).toThrow();
});

const sources = ['tests/exact-network-runtime-conformance.test.ts', 'packages/core/src/delegated-runtime.ts', 'packages/core/src/approval-store.ts', 'packages/core/src/hosted-consent.ts', 'packages/daemon/src/codex-session.ts', 'packages/daemon/src/codex-supervisor.ts', 'packages/daemon/src/codex-containment.ts', 'packages/daemon/src/supervisor-server.ts'];
const pins = async () => Object.fromEntries(await Promise.all(sources.map(async path => [path, createHash('sha256').update(await readFile(path)).digest('hex')])));

it('resolves each selected network source pin before supplier work', async () => { expect(Object.keys(await pins())).toEqual(sources); });

it.runIf(process.env.CHIRALITY_RUN_EXACT_NETWORK_RUNTIME === '1')('actual command network via public API and durable approval attribution', async () => {
  const nativeChild = process.env.CHIRALITY_EXACT_NETWORK_ROLE === 'native-child';
  if (process.env.CHIRALITY_EXACT_NETWORK_ROLE !== undefined && !['primary', 'native-child'].includes(process.env.CHIRALITY_EXACT_NETWORK_ROLE)) throw new Error('Closed network role required');
  const profileStartedAt = Date.now();
  const publicTarget = process.env.CHIRALITY_EXACT_NETWORK_TARGET === 'example-domain';
  if (process.env.CHIRALITY_EXACT_NETWORK_TARGET !== undefined && !['loopback', 'example-domain'].includes(process.env.CHIRALITY_EXACT_NETWORK_TARGET)) throw new Error('Closed authorized target selection required');
  const expectedHost = publicTarget ? 'example.com' : '127.0.0.1';
  const expectedMarker = publicTarget ? 'Example Domain' : marker;
  const selected = scenario(process.env.CHIRALITY_EXACT_NETWORK_SCENARIO);
  const posture = selected.startsWith('ask-') ? 'ask-per-destination' as const : selected as 'off' | 'on';
  const supplied = process.env.CHIRALITY_EXACT_CODEX_PATH, evidenceDirectory = process.env.CHIRALITY_EXACT_EVIDENCE_DIR;
  const sha = process.env.CHIRALITY_EXACT_CANDIDATE_SHA256, size = process.env.CHIRALITY_EXACT_CANDIDATE_SIZE;
  if (!supplied || !evidenceDirectory?.startsWith('/')) throw new Error('Explicit supplier and fresh private evidence path required');
  if ((sha === undefined) !== (size === undefined) || (sha !== undefined && (sha.length !== 64 || !/^[a-f0-9]{64}$/.test(sha) || !size || String(Number(size)) !== size || !Number.isSafeInteger(Number(size)) || Number(size) < 1 || Number(size) > 4294967296))) throw new Error('Complete candidate hash and size required');
  const controlled = sha ? createControlledSupplyVerifierForTests({ sha256: sha, size: Number(size), version: 'candidate-source-version-not-accepted-identity' }) : undefined;
  const verify = (path: string) => controlled ? controlled.verify(path) : verifyExactSupply({ executablePath: path });
  let root = '', broker = '', worker = '', home = '';
  const cleanups: (() => Promise<unknown>)[] = [];
  const result: Record<string, unknown> = { schema: 'chirality-exact-runtime-network/v1', evidenceClass: controlled ? 'supplier-candidate-unaccepted' : 'accepted-supply', scenario: selected, commandNetworkPosture: posture, launchEvidence: 'test-only-no-account-exact-vendor-factory', managerModel: 'owned-loopback-deterministic-Responses', target: publicTarget ? 'http://example.com/' : 'owned-loopback-HTTP', targetAuthorization: publicTarget ? 'IMPLEMENTATION_AMENDMENT_13' : 'owned-fixture', publicZeroNetworkTrafficProven: false, approvalEvidence: 'public-api-durable-store-candidate', storedAttributionProven: false, commandRole: nativeChild ? 'native-child' : 'primary', nativeDescendantNetworkProven: false, accountUsed: false, passed: false };
  let phase = 'setup', destinationHits = 0, commandReturnedMarker = false, commandStarted = false, commandFinished = false, curlStatus: number | undefined, approvalCount = 0;
  const safeRequests: unknown[] = [];
  const observedPrimary: { threadId?: unknown; turnId?: unknown } = {};

  try {
    phase = 'source-pins'; result.sourcesBefore = await pins();
    phase = 'supplier-verification'; const supply = await verify(supplied); result.supplySha256 = supply.sha256; result.supplySize = Number(supply.identity.size);
    phase = 'scratch-setup'; const created = await mkdtemp(join(await realpath('/tmp'), 'enc-')); cleanups.push(() => rm(created, { recursive: true, force: true }));
    const base = await realpath(created); root = join(base, 'p'); broker = join(base, 'r'); worker = join(broker, 'w'); home = join(worker, 'h');
    const { manifestPath } = await createProjectFixture(root, 'network-project');
    await mkdir(worker, { recursive: true, mode: 0o700 }); await chmod(broker, 0o700); await mkdir(home, { mode: 0o700 });
    const destination = createServer((req, res) => { if (req.method !== 'GET' || req.url !== '/canary') { res.writeHead(404).end(); return; } destinationHits++; res.writeHead(200, { 'Content-Type': 'text/plain' }).end(marker); });
    await new Promise<void>(resolve => destination.listen(0, '127.0.0.1', resolve));
    cleanups.push(() => new Promise<void>(resolve => { destination.closeAllConnections(); destination.close(() => resolve()); }));
    const destinationUrl = publicTarget ? 'http://example.com/' : `http://127.0.0.1:${(destination.address() as { port: number }).port}/canary`;
    let modelRequests = 0, issuedCallId: string | undefined;
    let commandIssuedAt: number | undefined;
    const nativeCalls = new Map<string, 'spawn' | 'wait'>();
    const peer = createServer(async (req, res) => {
      try {
        if (req.method !== 'POST' || req.url !== '/v1/responses' || req.headers.authorization) throw new Error('Unexpected model request');
        const chunks: Buffer[] = []; let bytes = 0;
        for await (const raw of req) { const chunk = Buffer.from(raw); bytes += chunk.length; if (bytes > 2000000) throw new Error('Model request bound'); chunks.push(chunk); }
        const raw = Buffer.concat(chunks), body = JSON.parse((req.headers['content-encoding'] === 'gzip' ? gunzipSync(raw, { maxOutputLength: 4000000 }) : raw).toString());
        if (++modelRequests > 16 || !Array.isArray(body.tools) || !Array.isArray(body.input)) throw new Error('Unexpected model shape');
        const childRequest = JSON.stringify(body.input.filter((item: any) => item.role === 'user').at(-1)?.content ?? '').includes('NETWORK_NATIVE_CHILD_ONLY');
        const nativePrimary = nativeChild && !childRequest;
        const output = body.input.find((item: any) => item.type === 'function_call_output' && item.call_id === issuedCallId);
        let item: Record<string, unknown>;
        if (nativePrimary) {
          const outputs = body.input.filter((entry: any) => entry.type === 'function_call_output' && nativeCalls.has(entry.call_id));
          const spawned = outputs.find((entry: any) => nativeCalls.get(entry.call_id) === 'spawn');
          const waited = outputs.find((entry: any) => nativeCalls.get(entry.call_id) === 'wait');
          if (waited) item = { type: 'message', id: `msg_${modelRequests}`, role: 'assistant', status: 'completed', content: [{ type: 'output_text', text: 'NATIVE_NETWORK_CANARY_FINISHED', annotations: [] }] };
          else {
            const names = spawned ? ['wait_agent', 'wait'] : ['spawn_agent'];
            const tools = body.tools.flatMap((tool: any) => tool.type === 'namespace' && Array.isArray(tool.tools) ? tool.tools.map((member: any) => ({ ...member, namespace: tool.name })) : [tool]);
            const tool = tools.find((tool: any) => tool.type === 'function' && names.includes(tool.name));
            if (!tool?.parameters) throw new Error('Actual native namespace function absent');
            let args: Record<string, unknown>;
            if (!spawned) args = { message: 'NETWORK_NATIVE_CHILD_ONLY: run the one deterministic authorized destination command and finish.' };
            else {
              const returned = JSON.parse(spawned.output), childId = returned.agent_id ?? returned.id;
              if (typeof childId !== 'string') throw new Error('Actual child ID absent');
              result.nativeChildId = childId;
              args = { [tool.name === 'wait_agent' ? 'targets' : 'ids']: [childId] };
            }
            if ((tool.parameters.required ?? []).some((key: string) => !(key in args))) throw new Error('Unknown native required argument');
            const callId = `native_${modelRequests}`; nativeCalls.set(callId, spawned ? 'wait' : 'spawn');
            item = { type: 'function_call', id: `fc_${modelRequests}`, call_id: callId, name: tool.name, ...(tool.namespace ? { namespace: tool.namespace } : {}), arguments: JSON.stringify(args), status: 'completed' };
          }
        } else if (output) {
          result.commandElapsedMs = commandIssuedAt === undefined ? null : Date.now() - commandIssuedAt;
          result.commandBudgetMs = 10000; result.commandWithinBudget = typeof result.commandElapsedMs === 'number' && result.commandElapsedMs <= 10000;
          const commandOutput = typeof output.output === 'string' ? output.output : JSON.stringify(output.output);
          commandReturnedMarker = commandOutput.includes(expectedMarker);
          const statusMatch = /NETWORK_HTTP_STATUS:([0-9]{3})/.exec(commandOutput); result.httpStatus = statusMatch ? Number(statusMatch[1]) : null;
          const evidence = commandEvidence(commandOutput); commandStarted = evidence.started; commandFinished = evidence.finished; curlStatus = evidence.curlStatus;
          // A vendor rejection begins at the top-level tool output, unlike HTTP bytes within a command transcript.
          const supplierError = supplierErrorText(commandOutput);
          result.supplierPolicyDiagnostic = supplierError || null;
          const retainedOutput = publicTarget ? supplierError || commandOutput.split('\n').filter((line: string) => /^(?:NETWORK_COMMAND_STARTED|NETWORK_COMMAND_FINISHED:[0-9]{1,3}|NETWORK_HTTP_STATUS:[0-9]{3}|curl: )/.test(line)).join('\n') : commandOutput;
          const safeOutput = retainedOutput.replace(/\bBearer\s+[^\s"']+/gi, 'Bearer [REDACTED]').replace(/\bsk-[A-Za-z0-9_-]{8,}/g, '[REDACTED_KEY]').replace(/((?:access_token|refresh_token|id_token|api[_-]?key|authorization)["']?\s*[:=]\s*)["']?[^\s,"'}]+["']?/gi, '$1[REDACTED]');
          result.supplierPolicyDiagnostic = supplierError ? safeOutput.slice(0, 2048) : null;
          result.syntheticCommandOutput = { text: safeOutput.slice(0, 8192), truncated: safeOutput.length > 8192, scope: publicTarget ? 'AM13 status and curl diagnostic lines only; public response body discarded' : 'owned-loopback curl command; isolated no-account worker; known credential patterns scrubbed', stream: 'vendor tool combined output' };
          result.commandDiagnostic = { classification: !commandStarted ? 'markers-not-observed' : !commandFinished ? 'command-incomplete' : curlStatus === 0 ? 'curl-completed' : 'curl-error', reportedCurlError: /curl: \(([0-9]{1,3})\)/.exec(commandOutput)?.[1] ?? null, shellExitCode: /Process exited with code ([0-9]{1,3})/.exec(commandOutput)?.[1] ?? null, outputBytes: Buffer.byteLength(commandOutput), started: commandStarted, finished: commandFinished, curlStatus };
          item = { type: 'message', id: `msg_${modelRequests}`, role: 'assistant', status: 'completed', content: [{ type: 'output_text', text: 'NETWORK_CANARY_COMMAND_RETURNED', annotations: [] }] };
        } else {
          if (issuedCallId) throw new Error('Command output absent; no resend');
          const tool = body.tools.find((value: any) => value.type === 'function' && value.name === 'exec_command');
          if (!tool?.parameters?.properties?.cmd) throw new Error('Advertised exec_command absent');
          const props = tool.parameters.properties;
          // Explicitly clear curl loopback proxy bypass, but never add a native network grant.
          const args: Record<string, unknown> = { cmd: commandFor(destinationUrl), ...(props.workdir ? { workdir: root } : {}), ...(props.login ? { login: false } : {}), ...(props.yield_time_ms ? { yield_time_ms: 10000 } : {}) };
          if ((tool.parameters.required ?? []).some((key: string) => !(key in args))) throw new Error('Unmapped advertised command field');
          result.commandEmittedFor = childRequest ? 'native-child' : 'primary';
          commandIssuedAt = Date.now();
          issuedCallId = 'network_fixture_call_1'; item = { type: 'function_call', id: 'fc_network_1', call_id: issuedCallId, name: tool.name, arguments: JSON.stringify(args), status: 'completed' };
        }
        const response = { id: `resp_${modelRequests}`, object: 'response', model: 'runtime-deterministic', status: 'completed', output: [item], usage: { input_tokens: 1, output_tokens: 1, total_tokens: 2 } };
        const frames = [{ type: 'response.created', response: { ...response, status: 'in_progress', output: [] } }, { type: 'response.output_item.added', output_index: 0, item: { ...item, ...(item.type === 'function_call' ? { arguments: '' } : { content: [] }) } }, ...(item.type === 'function_call' ? [{ type: 'response.function_call_arguments.delta', item_id: item.id, output_index: 0, delta: item.arguments }, { type: 'response.function_call_arguments.done', item_id: item.id, output_index: 0, arguments: item.arguments }] : []), { type: 'response.output_item.done', output_index: 0, item }, { type: 'response.completed', response }];
        res.writeHead(200, { 'Content-Type': 'text/event-stream' }).end(frames.map((frame, sequence_number) => `event: ${frame.type}\ndata: ${JSON.stringify({ ...frame, sequence_number, response_id: response.id })}\n\n`).join(''));
      } catch { result.modelPeerFailure = true; res.writeHead(400).end('{}'); }
    });
    await new Promise<void>(resolve => peer.listen(0, '127.0.0.1', resolve));
    cleanups.push(() => new Promise<void>(resolve => { peer.closeAllConnections(); peer.close(() => resolve()); }));
    const binary = join(worker, 'app-server'); await copyFile(supplied, binary); await chmod(binary, 0o700); await verify(binary);
    const policy = await prepareCodexNativePolicy({ canonicalRoot: root, codexHome: home, privateDirectory: worker, protectedPaths: [broker], immutableReadRoots: ['/bin', '/usr/lib', '/usr/bin/curl', '/private/etc/ssl/openssl.cnf', '/System/Volumes/Preboot/Cryptexes/OS/System/Library/dyld'], commandNetworkPosture: posture });
    cleanups.push(() => policy.cleanup()); result.expectedPermissions = policy.expectedPermissions;
    const identity = { canonicalRoot: root, cwd: root, accountId: 'no-account-test', accountEpoch: 1, policyDigest: policy.policyDigest };
    const workers = CodexSupervisor.controlledForTests({ commandNetworkPosture: posture, allowUnauthenticatedModel: true, identity, model: 'runtime-deterministic', requestTimeoutMs: 10000, turnTimeoutMs: 45000, launch: async () => {
      await verify(binary);
      const launch = await policy.launchArguments(binary);
      const config = ['model_provider="runtime_deterministic"', 'model="runtime-deterministic"', 'model_providers.runtime_deterministic.name="Owned deterministic peer"', `model_providers.runtime_deterministic.base_url="http://127.0.0.1:${(peer.address() as { port: number }).port}/v1"`, 'model_providers.runtime_deterministic.wire_api="responses"', 'model_providers.runtime_deterministic.requires_openai_auth=false', 'model_providers.runtime_deterministic.supports_websockets=false', 'model_providers.runtime_deterministic.stream_max_retries=0', 'model_providers.runtime_deterministic.request_max_retries=0', 'features.multi_agent=true'];
      const child = spawn(launch[0]!, [...launch.slice(1), ...config.flatMap(value => ['-c', value])], { cwd: root, env: policy.environment, detached: true, stdio: 'pipe' });
      const closed = new Promise<void>(resolve => child.once('close', () => resolve()));
      const kill = () => { if (child.pid) try { process.kill(-child.pid, 'SIGKILL'); } catch { /* already closed */ } };
      child.on('error', () => {}); child.once('exit', kill);
      let stderrBytes = 0, observedBytes = 0, lines = '';
      child.stderr.on('data', (bytes: Buffer) => { stderrBytes += bytes.length; if (stderrBytes > 65536) kill(); });
      child.stdout.on('data', (bytes: Buffer) => { observedBytes += bytes.length; if (observedBytes > 2000000) return; lines += bytes.toString(); for (let n = lines.indexOf('\n'); n >= 0; n = lines.indexOf('\n')) { const line = lines.slice(0, n); lines = lines.slice(n + 1); try { const message = JSON.parse(line); if (message.id !== undefined && !message.method && message.result) { if (observedPrimary.threadId === undefined && typeof message.result.thread?.id === 'string') observedPrimary.threadId = message.result.thread.id; if (observedPrimary.turnId === undefined && typeof message.result.turn?.id === 'string') observedPrimary.turnId = message.result.turn.id; } if (message.id !== undefined && message.method && safeRequests.length < 16) safeRequests.push(diagnosticCallback(message, expectedHost, observedPrimary)); } catch { /* observer never authorizes */ } } });
      const timer = setTimeout(kill, 60000);
      try { await new Promise<void>((resolve, reject) => { child.once('spawn', resolve); child.once('error', reject); }); } catch { clearTimeout(timer); kill(); await closed; throw new Error('Candidate did not spawn'); }
      return { pid: child.pid!, descendantTracker: new DescendantTracker({ leaderPid: child.pid!, intervalMs: 100, maxDurationMs: 90000 }), permissionProfile: policy.permissionProfile, policyDigest: policy.policyDigest, expectedPermissions: policy.expectedPermissions, transport: { stdin: child.stdin, stdout: child.stdout, close: async () => { clearTimeout(timer); kill(); await closed; result.processClosed = true; } } };
    } });
    const originalWait = workers.wait.bind(workers);
    workers.wait = observeDiagnosticFailure(originalWait, failure => { result.actorFailure = failure; });
    cleanups.push(() => workers.close());
    const socketPath = join(broker, 's.sock'), server = await startSupervisorServer({ socketPath, supervisor: workers }); cleanups.push(() => server.close());
    const privateClient = new SupervisorClient({ socketPath, credential: server.credential });
    // Controlled-worker binding sends prompt text; this trusted adapter supplies the actual private JSON envelope.
    const supervisor = { acquire: (id: string, prompt: string) => privateClient.acquire(id, JSON.stringify({ prompt })), inventory: privateClient.inventory.bind(privateClient), reconnect: privateClient.reconnect.bind(privateClient), wait: privateClient.wait.bind(privateClient), retire: privateClient.retire.bind(privateClient), pendingNetworkApprovals: privateClient.pendingNetworkApprovals.bind(privateClient), replyNetworkApproval: privateClient.replyNetworkApproval.bind(privateClient) };
    const compatibility = fixtureCompatibility;
    result.compatibility = compatibility;
    const consent = new HostedConsentStore({ canonicalRoot: root, codexHome: home });
    let delegated: DelegatedRuntime;
    const approvals = new ApprovalStore({ canonicalRoot: root, storageRoot: join(broker, 'approvals'), consent, isLive: binding => delegated.isApprovalLive(binding) });
    const binding = { identity, compatibility, supervisor, consent, retirement: new WorkerRetirementCoordinator({ directory: join(broker, 'retirement') }), approvals, commandNetworkPosture: posture, approvalForwardingEnabled: true, evidenceClass: 'controlled-worker' as const };
    delegated = new DelegatedRuntime({ daemonId: 'exact-network-fixture', projects: new Map([['network-project', binding]]) });
    const runtimeDirectory = join(broker, 'runtime');
    const projects = new ProjectRegistry(runtimeDirectory), sessions = new SessionStore(runtimeDirectory, projects), engines = new EngineRegistry();
    const residency = new ResidencyCoordinator({ async listStatus() { return []; }, async load() {}, async unload() {} }, runtimeDirectory);
    const service = new RuntimeService(projects, sessions, engines, residency, new TurnCoordinator(projects, sessions, engines, residency), new AuthRegistry(runtimeDirectory), { async get() { return undefined; }, async status() { return { configured: false }; }, async set() {}, async remove() {} });
    const registered = await service.registerProject(manifestPath, 'parent-fixture-operator', 'exact-network-fixture-only');
    const daemon = new RuntimeDaemon({ socketPath: join(broker, 'd.sock'), runtimeDirectory, service, delegated }); await daemon.start(); cleanups.push(() => daemon.stop());
    const client = new RuntimeClient({ socketPath: join(broker, 'd.sock'), tokenFile: registered.tokenFile });
    await client.grantDelegatedConsent('network-project', compatibility, { posture, approvedBy: 'parent-fixture-operator', explicitUserAct: true });
    result.consentRecorded = true; result.bindingEvidenceClass = 'controlled-worker';
    phase = 'public-runtime-turn';
    let settled = false, successfulTerminal = false;
    const terminal = client.runDelegatedTurn('network-project', compatibility, { turnId: 'network-turn', prompt: 'Perform the deterministic authorized network canary once and finish.' }).then(value => { successfulTerminal = value.terminal.outcome === 'completed'; settled = true; }, error => { result.terminalFailure = diagnosticFailure(error); settled = true; });
    const deadline = Date.now() + 50000;
    while (!settled && Date.now() < deadline) {
      let prompts: Awaited<ReturnType<typeof client.pendingDelegatedApprovals>> = [];
      try { prompts = await client.pendingDelegatedApprovals('network-project', 'network-turn'); } catch (error) { result.approvalPollFailure = diagnosticFailure(error); if (settled) break; }
      for (const rawPrompt of prompts) {
        const prompt = rawPrompt as { requestId: string; binding: { workerGeneration: string }; networkApprovalContext: { host: string; protocol: string } };
        approvalCount++;
        if (posture !== 'ask-per-destination' || prompt.networkApprovalContext.host !== expectedHost || prompt.networkApprovalContext.protocol !== 'http' || approvalCount > 1) throw new Error('Unattributed or duplicate destination approval');
        result.approval = { requestId: prompt.requestId, workerGeneration: prompt.binding.workerGeneration, destination: expectedHost, choice: selected };
        await expect(client.decideDelegatedApproval('network-project', prompt.requestId, compatibility, { turnId: 'network-turn', workerGeneration: 'wrong-generation', decision: 'allow', approvedBy: 'parent-fixture-operator', explicitUserAct: true })).rejects.toMatchObject({ code: 'FORBIDDEN' });
        result.staleGenerationRejected = true;
        if (selected === 'ask-cancel') {
          const pendingRecord = await approvals.read(prompt.requestId, prompt.binding as Parameters<typeof approvals.read>[1]);
          expect(pendingRecord.decision).toBeUndefined();
          const interruptAck = await client.interruptDelegatedTurn('network-project', 'network-turn', compatibility); result.interruptAcknowledgement = verifyInterruptAcknowledgement(interruptAck, 'network-turn', prompt.binding.workerGeneration); result.cancelled = true; result.commandElapsedMs = commandIssuedAt === undefined ? null : Date.now() - commandIssuedAt; result.commandBudgetMs = 10000; result.commandWithinBudget = typeof result.commandElapsedMs === 'number' && result.commandElapsedMs <= 10000;
          await expect(approvals.read(prompt.requestId, prompt.binding as Parameters<typeof approvals.read>[1])).rejects.toMatchObject({ code: 'FORBIDDEN', status: 403 });
          result.inactiveApprovalReadRejected = true;
          await terminal; // Audit after the original turn has settled, never from interrupt ACK alone.
          result.cancellationAudit = await auditInterruptedApproval(broker, pendingRecord.request);
          result.workerClosedBeforeCancellationAudit = result.processClosed === true;
          result.cancellationEvidenceComplete = (result.cancellationAudit as Awaited<ReturnType<typeof auditInterruptedApproval>>).complete && result.workerClosedBeforeCancellationAudit === true && result.inactiveApprovalReadRejected === true;
          break;
        }
        const decision = selected === 'ask-allow' ? 'allow' : 'deny';
        await client.decideDelegatedApproval('network-project', prompt.requestId, compatibility, { turnId: 'network-turn', workerGeneration: prompt.binding.workerGeneration, decision, approvedBy: 'parent-fixture-operator', explicitUserAct: true });
        const stored = await approvals.read(prompt.requestId, prompt.binding as Parameters<typeof approvals.read>[1]);
        result.storedAttributionProven = stored.decision?.decision === decision && stored.decision.approvedBy === 'parent-fixture-operator'; result.decisionSent = decision;
      }
      if (!settled) await new Promise(resolve => setTimeout(resolve, 25));
    }
    if (!settled) { await client.interruptDelegatedTurn('network-project', 'network-turn', compatibility); result.deadlineExpired = true; }
    await terminal;
    result.successfulTerminal = successfulTerminal; result.modelRequests = modelRequests;
    const wantsAccess = selected === 'on' || selected === 'ask-allow';
    result.passed = wantsAccess ? successfulTerminal && commandStarted && commandFinished && curlStatus === 0 && (publicTarget ? result.httpStatus === 200 : destinationHits === 1) && commandReturnedMarker : (publicTarget || destinationHits === 0) && !commandReturnedMarker && (selected === 'ask-cancel' ? result.cancelled === true : successfulTerminal && commandStarted && commandFinished && curlStatus !== undefined && curlStatus > 0 && curlStatus <= 255);
    if (posture === 'ask-per-destination') result.passed = result.passed === true && approvalCount === 1 && result.staleGenerationRejected === true && (selected === 'ask-cancel' ? result.cancellationEvidenceComplete === true : result.storedAttributionProven === true);
    if (nativeChild) { result.nativeDescendantNetworkProven = result.passed === true && typeof result.nativeChildId === 'string' && result.commandEmittedFor === 'native-child'; result.passed = result.nativeDescendantNetworkProven; }
    await verify(binary); await verify(supplied); result.supplyRevalidated = true;
  } catch (error) { result.failurePhase = phase; result.fixtureFailure = diagnosticFailure(error); const value = error as { code?: unknown; status?: unknown }; result.failureCode = typeof value.code === 'string' && /^[A-Z_]{1,64}$/.test(value.code) ? value.code : 'UNCLASSIFIED'; if (typeof value.status === 'number') result.failureStatus = value.status; }
  finally {
    result.destinationHits = publicTarget ? null : destinationHits; result.responseBodyPersisted = !publicTarget; result.requestShape = { method: 'GET', query: false, body: false, credentials: false, cookies: false, redirectsFollowed: false, maxResponseBytes: 16384 }; result.commandReturnedMarker = commandReturnedMarker; result.approvalCount = approvalCount; result.serverRequests = safeRequests;
    let failures = 0; for (const cleanup of cleanups.reverse()) try { await cleanup(); } catch { failures++; }
    result.profileElapsedMs = Date.now() - profileStartedAt; result.profileBudgetMs = 60000; result.profileWithinBudget = Number(result.profileElapsedMs) <= 60000;
    result.cleanupFailures = failures; try { result.sourcesAfter = await pins(); result.sourceStable = result.sourcesBefore !== undefined && JSON.stringify(result.sourcesBefore) === JSON.stringify(result.sourcesAfter); } catch { result.sourceStable = false; result.sourcePinFailure = true; }
    result.passed = result.passed === true && failures === 0 && result.processClosed === true && result.sourceStable === true && result.supplyRevalidated === true && result.modelPeerFailure !== true && result.profileWithinBudget === true && result.commandWithinBudget === true;
    await mkdir(evidenceDirectory, { recursive: true, mode: 0o700 }); await writeFile(join(evidenceDirectory, 'EXACT_NETWORK_RUNTIME_CANARY.json'), JSON.stringify(result, null, 2) + '\n', { mode: 0o600, flag: 'wx' });
  }
  expect(result.passed, 'Owned destination command/approval canary failed; inspect calibrated evidence').toBe(true);
}, 90000);
