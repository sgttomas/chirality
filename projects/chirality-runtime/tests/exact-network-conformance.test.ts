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
import { startSupervisorServer, SupervisorClient } from '../packages/daemon/src/supervisor-server.js';

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

it.runIf(process.env.CHIRALITY_RUN_EXACT_NETWORK === '1')('actual primary command network via private approval bridge to owned destination', async () => {
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
  const supply = await verify(supplied);
  const base = await realpath(await mkdtemp(join(await realpath('/tmp'), 'enc-')));
  const root = join(base, 'p'), broker = join(base, 'r'), worker = join(broker, 'w'), home = join(worker, 'h');
  const cleanups: (() => Promise<unknown>)[] = [() => rm(base, { recursive: true, force: true })];
  const result: Record<string, unknown> = { schema: 'chirality-exact-primary-network/v1', evidenceClass: controlled ? 'supplier-candidate-unaccepted' : 'accepted-supply', supplySha256: supply.sha256, supplySize: Number(supply.identity.size), scenario: selected, commandNetworkPosture: posture, launchEvidence: 'test-only-no-account-exact-vendor-factory', managerModel: 'owned-loopback-deterministic-Responses', target: publicTarget ? 'http://example.com/' : 'owned-loopback-HTTP', targetAuthorization: publicTarget ? 'IMPLEMENTATION_AMENDMENT_13' : 'owned-fixture', publicZeroNetworkTrafficProven: false, approvalEvidence: 'primary-private-protocol-only', storedAttributionProven: false, nativeDescendantNetworkProven: false, accountUsed: false, passed: false };
  let phase = 'setup', destinationHits = 0, commandReturnedMarker = false, commandStarted = false, commandFinished = false, curlStatus: number | undefined, approvalCount = 0;
  const safeRequests: unknown[] = [];
  const sources = ['tests/exact-network-conformance.test.ts', 'packages/daemon/src/codex-session.ts', 'packages/daemon/src/codex-supervisor.ts', 'packages/daemon/src/codex-containment.ts', 'packages/daemon/src/supervisor-server.ts'];
  const pins = async () => Object.fromEntries(await Promise.all(sources.map(async path => [path, createHash('sha256').update(await readFile(path)).digest('hex')])));
  result.sourcesBefore = await pins();
  try {
    await mkdir(root, { mode: 0o700 }); await mkdir(worker, { recursive: true, mode: 0o700 }); await chmod(broker, 0o700); await mkdir(home, { mode: 0o700 });
    const destination = createServer((req, res) => { if (req.method !== 'GET' || req.url !== '/canary') { res.writeHead(404).end(); return; } destinationHits++; res.writeHead(200, { 'Content-Type': 'text/plain' }).end(marker); });
    await new Promise<void>(resolve => destination.listen(0, '127.0.0.1', resolve));
    cleanups.push(() => new Promise<void>(resolve => { destination.closeAllConnections(); destination.close(() => resolve()); }));
    const destinationUrl = publicTarget ? 'http://example.com/' : `http://127.0.0.1:${(destination.address() as { port: number }).port}/canary`;
    let modelRequests = 0, issuedCallId: string | undefined;
    let commandIssuedAt: number | undefined;
    const peer = createServer(async (req, res) => {
      try {
        if (req.method !== 'POST' || req.url !== '/v1/responses' || req.headers.authorization) throw new Error('Unexpected model request');
        const chunks: Buffer[] = []; let bytes = 0;
        for await (const raw of req) { const chunk = Buffer.from(raw); bytes += chunk.length; if (bytes > 2000000) throw new Error('Model request bound'); chunks.push(chunk); }
        const raw = Buffer.concat(chunks), body = JSON.parse((req.headers['content-encoding'] === 'gzip' ? gunzipSync(raw, { maxOutputLength: 4000000 }) : raw).toString());
        if (++modelRequests > 8 || !Array.isArray(body.tools) || !Array.isArray(body.input)) throw new Error('Unexpected model shape');
        const output = body.input.find((item: any) => item.type === 'function_call_output' && item.call_id === issuedCallId);
        let item: Record<string, unknown>;
        if (output) {
          result.commandElapsedMs = commandIssuedAt === undefined ? null : Date.now() - commandIssuedAt;
          result.commandBudgetMs = 10000; result.commandWithinBudget = typeof result.commandElapsedMs === 'number' && result.commandElapsedMs <= 10000;
          const commandOutput = typeof output.output === 'string' ? output.output : JSON.stringify(output.output);
          commandReturnedMarker = commandOutput.includes(expectedMarker);
          const statusMatch = /NETWORK_HTTP_STATUS:([0-9]{3})/.exec(commandOutput); result.httpStatus = statusMatch ? Number(statusMatch[1]) : null;
          const evidence = commandEvidence(commandOutput); commandStarted = evidence.started; commandFinished = evidence.finished; curlStatus = evidence.curlStatus;
          // A vendor rejection begins at the top-level tool output, unlike HTTP bytes within a command transcript.
          const supplierError = supplierErrorText(commandOutput);
          result.supplierPolicyDiagnostic = supplierError || null;
          const retainedOutput = publicTarget ? supplierError || commandOutput.split('\n').filter(line => /^(?:NETWORK_COMMAND_STARTED|NETWORK_COMMAND_FINISHED:[0-9]{1,3}|NETWORK_HTTP_STATUS:[0-9]{3}|curl: )/.test(line)).join('\n') : commandOutput;
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
    const workers = CodexSupervisor.controlledForTests({ commandNetworkPosture: posture, allowUnauthenticatedModel: true, identity: { canonicalRoot: root, cwd: root, accountId: 'no-account-test', accountEpoch: 1, policyDigest: policy.policyDigest }, model: 'runtime-deterministic', requestTimeoutMs: 10000, turnTimeoutMs: 45000, launch: async () => {
      await verify(binary);
      const launch = await policy.launchArguments(binary);
      const config = ['model_provider="runtime_deterministic"', 'model="runtime-deterministic"', 'model_providers.runtime_deterministic.name="Owned deterministic peer"', `model_providers.runtime_deterministic.base_url="http://127.0.0.1:${(peer.address() as { port: number }).port}/v1"`, 'model_providers.runtime_deterministic.wire_api="responses"', 'model_providers.runtime_deterministic.requires_openai_auth=false', 'model_providers.runtime_deterministic.supports_websockets=false', 'model_providers.runtime_deterministic.stream_max_retries=0', 'model_providers.runtime_deterministic.request_max_retries=0'];
      const child = spawn(launch[0]!, [...launch.slice(1), ...config.flatMap(value => ['-c', value])], { cwd: root, env: policy.environment, detached: true, stdio: 'pipe' });
      const closed = new Promise<void>(resolve => child.once('close', () => resolve()));
      const kill = () => { if (child.pid) try { process.kill(-child.pid, 'SIGKILL'); } catch { /* already closed */ } };
      child.on('error', () => {}); child.once('exit', kill);
      let stderrBytes = 0, observedBytes = 0, lines = '';
      child.stderr.on('data', (bytes: Buffer) => { stderrBytes += bytes.length; if (stderrBytes > 65536) kill(); });
      child.stdout.on('data', (bytes: Buffer) => { observedBytes += bytes.length; if (observedBytes > 2000000) return; lines += bytes.toString(); for (let n = lines.indexOf('\n'); n >= 0; n = lines.indexOf('\n')) { const line = lines.slice(0, n); lines = lines.slice(n + 1); try { const message = JSON.parse(line); if (message.id !== undefined && message.method && safeRequests.length < 16) safeRequests.push({ method: String(message.method).slice(0, 128), parameterKeys: Object.keys(message.params ?? {}).slice(0, 32), networkContext: message.params?.networkApprovalContext ? { host: message.params.networkApprovalContext.host === expectedHost ? expectedHost : 'OTHER', protocol: message.params.networkApprovalContext.protocol === 'http' ? 'http' : 'OTHER' } : undefined }); } catch { /* observer never authorizes */ } } });
      const timer = setTimeout(kill, 60000);
      try { await new Promise<void>((resolve, reject) => { child.once('spawn', resolve); child.once('error', reject); }); } catch { clearTimeout(timer); kill(); await closed; throw new Error('Candidate did not spawn'); }
      return { pid: child.pid!, permissionProfile: policy.permissionProfile, policyDigest: policy.policyDigest, expectedPermissions: policy.expectedPermissions, transport: { stdin: child.stdin, stdout: child.stdout, close: async () => { clearTimeout(timer); kill(); await closed; result.processClosed = true; } } };
    } });
    cleanups.push(() => workers.close());
    const socketPath = join(broker, 's.sock'), server = await startSupervisorServer({ socketPath, supervisor: workers }); cleanups.push(() => server.close());
    const client = new SupervisorClient({ socketPath, credential: server.credential });
    phase = 'acquire'; const handle = await client.acquire('network-primary', JSON.stringify({ prompt: 'Run the deterministic authorized destination command once and finish.' }));
    phase = 'command-and-approval';
    let settled = false, successfulTerminal = false;
    const terminal = client.wait(handle.workerId, handle.generation).then(value => { successfulTerminal = value.exitCode === 0; settled = true; }, () => { settled = true; });
    const deadline = Date.now() + 50000;
    while (!settled && Date.now() < deadline) {
      const prompts = await client.pendingNetworkApprovals(handle.workerId, handle.generation);
      for (const prompt of prompts) {
        approvalCount++;
        if (posture !== 'ask-per-destination' || prompt.networkApprovalContext.host !== expectedHost || prompt.networkApprovalContext.protocol !== 'http' || approvalCount > 1) throw new Error('Unattributed or duplicate destination approval');
        result.approval = { threadId: prompt.threadId, turnId: prompt.turnId, destination: expectedHost, choice: selected };
        if (selected === 'ask-cancel') { await client.retire(handle.workerId, handle.generation); result.cancelled = true; result.commandElapsedMs = commandIssuedAt === undefined ? null : Date.now() - commandIssuedAt; result.commandBudgetMs = 10000; result.commandWithinBudget = typeof result.commandElapsedMs === 'number' && result.commandElapsedMs <= 10000; break; }
        const decision = selected === 'ask-allow' ? 'allow' : 'deny';
        await client.replyNetworkApproval(handle.workerId, handle.generation, prompt.approvalId, decision); result.decisionSent = decision;
      }
      if (!settled) await new Promise(resolve => setTimeout(resolve, 25));
    }
    if (!settled) { await client.retire(handle.workerId, handle.generation); result.deadlineExpired = true; }
    await terminal;
    result.successfulTerminal = successfulTerminal; result.modelRequests = modelRequests;
    const wantsAccess = selected === 'on' || selected === 'ask-allow';
    result.passed = wantsAccess ? successfulTerminal && commandStarted && commandFinished && curlStatus === 0 && (publicTarget ? result.httpStatus === 200 : destinationHits === 1) && commandReturnedMarker : (publicTarget || destinationHits === 0) && !commandReturnedMarker && (selected === 'ask-cancel' ? result.cancelled === true : successfulTerminal && commandStarted && commandFinished && curlStatus !== undefined && curlStatus > 0 && curlStatus <= 255);
    if (posture === 'ask-per-destination') result.passed = result.passed === true && approvalCount === 1;
    await verify(binary); await verify(supplied); result.supplyRevalidated = true;
  } catch { result.failurePhase = phase; }
  finally {
    result.destinationHits = publicTarget ? null : destinationHits; result.responseBodyPersisted = !publicTarget; result.requestShape = { method: 'GET', query: false, body: false, credentials: false, cookies: false, redirectsFollowed: false, maxResponseBytes: 16384 }; result.commandReturnedMarker = commandReturnedMarker; result.approvalCount = approvalCount; result.serverRequests = safeRequests;
    let failures = 0; for (const cleanup of cleanups.reverse()) try { await cleanup(); } catch { failures++; }
    result.profileElapsedMs = Date.now() - profileStartedAt; result.profileBudgetMs = 60000; result.profileWithinBudget = Number(result.profileElapsedMs) <= 60000;
    result.cleanupFailures = failures; result.sourcesAfter = await pins(); result.sourceStable = JSON.stringify(result.sourcesBefore) === JSON.stringify(result.sourcesAfter);
    result.passed = result.passed === true && failures === 0 && result.processClosed === true && result.sourceStable === true && result.supplyRevalidated === true && result.modelPeerFailure !== true && result.profileWithinBudget === true && result.commandWithinBudget === true;
    await mkdir(evidenceDirectory, { recursive: true, mode: 0o700 }); await writeFile(join(evidenceDirectory, 'EXACT_NETWORK_CANARY.json'), JSON.stringify(result, null, 2) + '\n', { mode: 0o600, flag: 'wx' });
  }
  expect(result.passed, 'Owned destination command/approval canary failed; inspect calibrated evidence').toBe(true);
}, 90000);
