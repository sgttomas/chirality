#!/usr/bin/env node

import { spawn } from 'node:child_process';
import { createHash, randomUUID } from 'node:crypto';
import { createWriteStream } from 'node:fs';
import {
  access,
  chmod,
  mkdir,
  mkdtemp,
  readFile,
  readdir,
  realpath,
  rm,
  stat,
  writeFile
} from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';
import { fileURLToPath } from 'node:url';
import { RuntimeClient } from '@chirality/runtime-client';

const SCRIPT_PATH = fileURLToPath(import.meta.url);
const FRONTEND_ROOT = path.resolve(path.dirname(SCRIPT_PATH), '..');
const DEFAULT_APP_PATH = path.join(FRONTEND_ROOT, 'dist', 'mac-arm64', 'Chirality.app');
const DEFAULT_OUTPUT_ROOT = path.join(
  FRONTEND_ROOT,
  'artifacts',
  'release-verification',
  'packaged-security'
);
const ASAR_CLI = path.join(FRONTEND_ROOT, 'node_modules', '.bin', 'asar');
const LOOPBACK_HOSTS = new Set(['localhost', '127.0.0.1', '::1', '[::1]']);
const PACKAGED_POLICY_MARKERS = [
  'REQ-NET-001',
  'api.anthropic.com',
  'anthropic_protocol_not_allowlisted',
  'anthropic_port_not_allowlisted',
  'host_not_allowlisted',
  'Blocked renderer outbound request by network policy',
  'Attachment exceeds per-file size limit',
  'Attachment exceeds per-turn size budget',
  'symbolic links are rejected',
  'ATTACHMENT_FAILURE',
  'Content-Security-Policy',
  'renderer.window_open.denied',
  'renderer.navigation.denied'
];
const BLOCKED_PROBE_URL = 'https://example.com/chirality-packaged-security-blocked';
const LOOPBACK_PROBE_URL = 'http://127.0.0.1:9/chirality-packaged-security-loopback';
// The page can no longer reach the REQ-NET-001 egress layer for a foreign host
// (the CSP's connect-src 'self' stops it first), so this request is issued from
// the main process through the window's session, where onBeforeRequest denies
// it (anthropic_port_not_allowlisted:8443). The example.com probe above is the
// CSP-layer observation.
const EGRESS_PROBE_URL = 'https://api.anthropic.com:8443/chirality-packaged-security-egress-blocked';

function nowIso() {
  return new Date().toISOString();
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function readArgValue(argv, index, flagName) {
  const value = argv[index];
  if (!value || value.startsWith('--')) throw new Error(`Missing value for ${flagName}`);
  return value;
}

export function parseArgs(argv) {
  const options = {};
  for (let index = 0; index < argv.length; index += 1) {
    const token = argv[index];
    if (token === '--app-path') {
      options.appPath = readArgValue(argv, index + 1, token);
      index += 1;
    } else if (token === '--output-root') {
      options.outputRoot = readArgValue(argv, index + 1, token);
      index += 1;
    } else if (token === '--source-revision') {
      options.sourceRevision = readArgValue(argv, index + 1, token);
      index += 1;
    } else if (token === '--capture-seconds') {
      const parsed = Number.parseInt(readArgValue(argv, index + 1, token), 10);
      if (!Number.isSafeInteger(parsed) || parsed < 3 || parsed > 120) {
        throw new Error('--capture-seconds must be an integer from 3 through 120');
      }
      options.captureSeconds = parsed;
      index += 1;
    } else if (token === '--help') {
      options.help = true;
    } else {
      throw new Error(`Unknown argument: ${token}`);
    }
  }
  return {
    appPath: path.resolve(options.appPath ?? DEFAULT_APP_PATH),
    outputRoot: path.resolve(options.outputRoot ?? DEFAULT_OUTPUT_ROOT),
    sourceRevision: options.sourceRevision,
    captureSeconds: options.captureSeconds ?? 12,
    help: options.help === true
  };
}

function usage() {
  return `Usage: node ./scripts/run-packaged-security-proof.mjs [options]\n\nOptions:\n  --app-path <path>         Freshly built Chirality.app\n  --output-root <path>      Retained proof directory\n  --source-revision <sha>   Expected Git HEAD (default: current HEAD)\n  --capture-seconds <n>     Packaged network capture window (default: 12)\n  --help                    Show this message\n`;
}

async function runCommand(command, args, options = {}) {
  return new Promise((resolve, reject) => {
    const child = spawn(command, args, {
      cwd: options.cwd,
      env: options.env,
      stdio: ['ignore', 'pipe', 'pipe']
    });
    let stdout = '';
    let stderr = '';
    child.stdout.on('data', (chunk) => { stdout += chunk.toString(); });
    child.stderr.on('data', (chunk) => { stderr += chunk.toString(); });
    child.once('error', reject);
    child.once('close', (code, signal) => resolve({ code: code ?? 1, signal, stdout, stderr }));
  });
}

async function sha256File(filePath) {
  return createHash('sha256').update(await readFile(filePath)).digest('hex');
}

async function captureAppIdentity(appPath, sourceRevision) {
  const canonicalAppPath = await realpath(appPath);
  const relativeFiles = [
    'Contents/MacOS/Chirality',
    'Contents/Resources/app.asar',
    'Contents/Resources/runtime-cli/chirality-cli.mjs'
  ];
  const files = [];
  for (const relativePath of relativeFiles) {
    const absolutePath = await realpath(path.join(canonicalAppPath, relativePath));
    const metadata = await stat(absolutePath);
    if (!metadata.isFile()) throw new Error(`Packaged identity target is not a file: ${absolutePath}`);
    files.push({ relativePath, bytes: metadata.size, sha256: await sha256File(absolutePath) });
  }
  const identityBasis = JSON.stringify({ sourceRevision, files });
  return {
    schema: 'chirality-packaged-security-subject/v1',
    appPath: canonicalAppPath,
    sourceRevision,
    files,
    identitySha256: createHash('sha256').update(identityBasis).digest('hex')
  };
}

async function extractPackagedMain(appPath, extractionRoot) {
  const asarPath = path.join(appPath, 'Contents', 'Resources', 'app.asar');
  await access(ASAR_CLI);
  const result = await runCommand(ASAR_CLI, ['extract-file', asarPath, 'dist-electron/main.js'], {
    cwd: extractionRoot
  });
  if (result.code !== 0) {
    throw new Error(`asar extract-file failed (${result.code}): ${result.stderr.trim()}`);
  }
  return readFile(path.join(extractionRoot, 'main.js'), 'utf8');
}

export function inspectPackagedPolicyMarkers(packagedMain) {
  const markers = PACKAGED_POLICY_MARKERS.map((marker) => ({
    marker,
    present: packagedMain.includes(marker)
  }));
  return {
    markers,
    allPresent: markers.every((entry) => entry.present)
  };
}

function startLoggedProcess({ label, command, args, env, logPath }) {
  const child = spawn(command, args, {
    cwd: FRONTEND_ROOT,
    env,
    stdio: ['ignore', 'pipe', 'pipe']
  });
  // Truncate, never append: every log-derived observation below must come from
  // this run alone, or a stale file from an earlier run could satisfy a check
  // the current bundle did not.
  const stream = createWriteStream(logPath, { flags: 'w', mode: 0o600 });
  let captured = '';
  const append = (chunk) => {
    const text = chunk.toString();
    captured += text;
    stream.write(text);
  };
  stream.write(`[${nowIso()}] START ${label}: ${command} ${args.join(' ')}\n`);
  child.stdout.on('data', append);
  child.stderr.on('data', append);
  const closed = new Promise((resolve) => {
    child.once('close', (code, signal) => {
      stream.write(`[${nowIso()}] EXIT ${label}: code=${code ?? 'null'} signal=${signal ?? 'null'}\n`);
      resolve({ code, signal });
    });
  });
  return { child, stream, closed, captured: () => captured };
}

async function stopProcess(processRecord, label) {
  const child = processRecord?.child;
  if (!child) {
    return { label, started: false, confirmedStopped: false, streamClosed: false };
  }

  const isStopped = () => child.exitCode !== null || child.signalCode !== null;
  let signalSent = null;
  if (!isStopped()) {
    signalSent = 'SIGTERM';
    child.kill('SIGTERM');
  }
  const deadline = Date.now() + 10_000;
  while (!isStopped() && Date.now() < deadline) await sleep(100);
  if (!isStopped()) {
    signalSent = 'SIGKILL';
    child.kill('SIGKILL');
    const killDeadline = Date.now() + 2_000;
    while (!isStopped() && Date.now() < killDeadline) await sleep(100);
  }
  if (isStopped()) await processRecord.closed;
  const streamClosed = await new Promise((resolve) => {
    processRecord.stream.end(() => resolve(true));
    processRecord.stream.once('error', () => resolve(false));
  });
  return {
    label,
    started: true,
    pid: child.pid,
    signalSent,
    exitCode: child.exitCode,
    signalCode: child.signalCode,
    confirmedStopped: isStopped(),
    streamClosed
  };
}

async function waitForPath(filePath, processRecord, timeoutMs = 30_000) {
  const deadline = Date.now() + timeoutMs;
  while (Date.now() < deadline) {
    if (processRecord.child.exitCode !== null) {
      throw new Error(`Process exited before required path appeared: ${filePath}`);
    }
    try {
      await access(filePath);
      return;
    } catch {
      await sleep(200);
    }
  }
  throw new Error(`Timed out waiting for path: ${filePath}`);
}

function parseProcessTable(output) {
  return output.split(/\r?\n/).flatMap((line) => {
    const match = line.match(/^\s*(\d+)\s+(\d+)\s+(.*)$/);
    return match ? [{ pid: Number(match[1]), ppid: Number(match[2]), command: match[3] }] : [];
  });
}

export function descendantProcessIds(processRows, roots) {
  const selected = new Set(roots.filter((pid) => Number.isSafeInteger(pid) && pid > 0));
  let changed = true;
  while (changed) {
    changed = false;
    for (const row of processRows) {
      if (selected.has(row.ppid) && !selected.has(row.pid)) {
        selected.add(row.pid);
        changed = true;
      }
    }
  }
  return [...selected].sort((left, right) => left - right);
}

function parseRemoteHost(endpoint) {
  if (endpoint.startsWith('[')) {
    const close = endpoint.indexOf(']');
    return close > 0 ? endpoint.slice(1, close) : endpoint;
  }
  const colon = endpoint.lastIndexOf(':');
  return colon > 0 ? endpoint.slice(0, colon) : endpoint;
}

export function parseLsofOutbound(output) {
  return output.split(/\r?\n/).flatMap((line) => {
    const arrow = line.indexOf('->');
    if (arrow === -1) return [];
    const endpoint = line.slice(arrow + 2).trim().split(/\s+/)[0] ?? '';
    const host = parseRemoteHost(endpoint).toLowerCase();
    return [{
      endpoint,
      host,
      class: LOOPBACK_HOSTS.has(host) ? 'loopback' : 'external-non-allowlisted',
      line
    }];
  });
}

async function captureTcpSnapshot(rootPids) {
  const ps = await runCommand('ps', ['-axo', 'pid=,ppid=,command=']);
  if (ps.code !== 0) throw new Error(`ps failed: ${ps.stderr.trim()}`);
  const processRows = parseProcessTable(ps.stdout);
  const pids = descendantProcessIds(processRows, rootPids);
  if (pids.length === 0) return { at: nowIso(), pids, endpoints: [] };
  const lsof = await runCommand('lsof', [
    '-nP', '-a', '-p', pids.join(','), '-iTCP', '-sTCP:ESTABLISHED,SYN_SENT,CLOSE_WAIT'
  ]);
  const endpoints = lsof.code === 0 || lsof.code === 1 ? parseLsofOutbound(lsof.stdout) : [];
  if (lsof.code !== 0 && lsof.code !== 1) throw new Error(`lsof failed: ${lsof.stderr.trim()}`);
  return {
    at: nowIso(),
    pids,
    processes: processRows.filter((row) => pids.includes(row.pid)),
    endpoints
  };
}

function extractMarkedPayloads(logText, marker) {
  return logText.split(/\r?\n/).flatMap((line) => {
    const index = line.indexOf(marker);
    if (index === -1) return [];
    try {
      return [JSON.parse(line.slice(index + marker.length).trim())];
    } catch {
      return [{ parseError: true }];
    }
  });
}

function extractProbePayloads(logText) {
  return extractMarkedPayloads(logText, '[network-policy-probe]');
}

function probeResultFailed(probePayloads, url) {
  return probePayloads.some((payload) =>
    Array.isArray(payload.results) && payload.results.some((result) =>
      result.url === url && result.ok === false
    )
  );
}

export function summarizeNetworkEvidence(logText, snapshots) {
  const blockedDiagnostics = (logText.match(/Blocked renderer outbound request by network policy/g) ?? []).length;
  const egressDiagnostics = (logText.match(/anthropic_port_not_allowlisted:8443/g) ?? []).length;
  const probePayloads = extractProbePayloads(logText);
  const endpoints = snapshots.flatMap((snapshot) => snapshot.endpoints ?? []);
  const unique = [...new Map(endpoints.map((entry) => [entry.endpoint, entry])).values()];
  const nonAllowlisted = unique.filter((entry) => entry.class !== 'loopback');
  const blockedProbeObserved = probeResultFailed(probePayloads, BLOCKED_PROBE_URL);
  const loopbackProbeObserved = probeResultFailed(probePayloads, LOOPBACK_PROBE_URL);
  const egressPayloads = extractMarkedPayloads(logText, '[egress-layer-probe]');
  const egressProbeObserved = egressPayloads.some(
    (payload) =>
      payload?.policy === 'REQ-NET-001' &&
      payload?.destination?.hostname === 'api.anthropic.com' &&
      payload?.outcome === 'rejected'
  );
  return {
    snapshotCount: snapshots.length,
    sampledProcessIds: [...new Set(snapshots.flatMap((snapshot) => snapshot.pids ?? []))].sort(),
    uniqueOutboundTcp: unique.map(({ line: _line, ...entry }) => entry),
    nonAllowlistedOutboundTcp: nonAllowlisted.map(({ line: _line, ...entry }) => entry),
    blockedRendererDiagnostics: blockedDiagnostics,
    egressLayerDiagnostics: egressDiagnostics,
    probePayloadCount: probePayloads.length,
    egressProbePayloadCount: egressPayloads.length,
    blockedProbeObserved,
    loopbackProbeObserved,
    egressProbeObserved,
    pass:
      snapshots.length > 0 &&
      nonAllowlisted.length === 0 &&
      blockedDiagnostics > 0 &&
      egressDiagnostics > 0 &&
      blockedProbeObserved &&
      loopbackProbeObserved &&
      egressProbeObserved
  };
}

/**
 * Renderer hardening evidence (G-CSP): the document's CSP header as the page
 * itself sees it, a denied window.open, the CSP violation raised by a blocked
 * fetch, the main-process denial lines, and — as important — no violation
 * against the app's own resources.
 */
export function summarizeRendererSecurityEvidence(logText) {
  const payloads = extractMarkedPayloads(logText, '[renderer-security-probe]');
  const payload = payloads.find((entry) => entry && entry.policy === 'G-CSP' && !entry.error) ?? null;
  const cspHeader = typeof payload?.cspHeader === 'string' ? payload.cspHeader : null;
  const cspHeaderPresent =
    cspHeader !== null &&
    cspHeader.includes("default-src 'self'") &&
    cspHeader.includes("connect-src 'self'") &&
    cspHeader.includes("frame-src 'none'") &&
    cspHeader.includes("object-src 'none'") &&
    !cspHeader.includes("'unsafe-eval'");
  const violations = Array.isArray(payload?.violations) ? payload.violations : [];
  const expectedViolation = (violation) =>
    typeof violation?.blockedURI === 'string' && violation.blockedURI.startsWith('https://example.com');
  const cspViolationObserved = violations.some(
    (violation) => expectedViolation(violation) && violation.effectiveDirective === 'connect-src'
  );
  const unexpectedViolations = violations.filter((violation) => !expectedViolation(violation));
  const windowOpenReturnedNull = payload?.windowOpen?.returned === 'null';
  const windowOpenDeniedLogged = logText.includes('renderer.window_open.denied');
  const navigationDeniedLogged = logText.includes('renderer.navigation.denied');
  return {
    probePayloadCount: payloads.length,
    cspHeader,
    cspHeaderPresent,
    cspViolationObserved,
    unexpectedViolations,
    windowOpenReturnedNull,
    windowOpenDeniedLogged,
    navigationAttempted: typeof payload?.navigationAttempted === 'string',
    navigationDeniedLogged,
    pass:
      payload !== null &&
      cspHeaderPresent &&
      cspViolationObserved &&
      unexpectedViolations.length === 0 &&
      windowOpenReturnedNull &&
      windowOpenDeniedLogged &&
      navigationDeniedLogged
  };
}

export function sensitiveMaterialFindings(text, values) {
  return values.flatMap(({ label, value }) => {
    const variants = [...new Set([value, encodeURIComponent(value)])];
    return variants.flatMap((variant) => text.includes(variant) ? [{ label, sha256: createHash('sha256').update(variant).digest('hex') }] : []);
  });
}

export function credentialProviderIsolation(statuses) {
  return (
    statuses.beforeOmlx.configured === false &&
    statuses.afterStoreOmlx.configured === false &&
    statuses.afterRemoveOmlx.configured === false
  );
}

export function evaluateCredentialEvidence(fixtureCredential, retainedSurfaces) {
  return Object.entries(retainedSurfaces).flatMap(([surface, text]) =>
    sensitiveMaterialFindings(String(text ?? ''), [
      { label: `fixture-credential:${surface}`, value: fixtureCredential }
    ])
  );
}

export function packagedProofPass({
  identityPresent,
  packagedPolicyPass,
  credentialProofPass,
  networkProofPass,
  rendererSecurityProofPass,
  cleanupPass,
  metadataLeakFindingCount
}) {
  return (
    identityPresent &&
    packagedPolicyPass &&
    credentialProofPass &&
    networkProofPass &&
    rendererSecurityProofPass === true &&
    cleanupPass &&
    metadataLeakFindingCount === 0
  );
}

async function runCredentialProof({ client, userDataRoot }) {
  const fixtureCredential = `packaged-proof-${randomUUID()}`;
  const credentialPath = path.join(userDataRoot, 'credentials', 'api-key.enc');
  const beforeAnthropic = await client.credentialStatus('anthropic');
  const beforeOmlx = await client.credentialStatus('omlx');
  const stored = await client.storeCredential('anthropic', fixtureCredential);
  const afterStore = await client.credentialStatus('anthropic');
  const afterStoreOmlx = await client.credentialStatus('omlx');
  const storedBytes = await readFile(credentialPath);
  const storedMetadata = await stat(credentialPath);
  const removed = await client.removeCredential('anthropic');
  const afterRemove = await client.credentialStatus('anthropic');
  const afterRemoveOmlx = await client.credentialStatus('omlx');
  let credentialFilePresentAfterRemove = true;
  try { await access(credentialPath); } catch { credentialFilePresentAfterRemove = false; }
  const rawStored = storedBytes.toString('utf8');
  const providerIsolation = credentialProviderIsolation({
    beforeOmlx,
    afterStoreOmlx,
    afterRemoveOmlx
  });
  const proof = {
    fixtureCredentialSha256: createHash('sha256').update(fixtureCredential).digest('hex'),
    before: { anthropic: beforeAnthropic, omlx: beforeOmlx },
    afterStore: { anthropic: afterStore, omlx: afterStoreOmlx },
    storedMutation: stored,
    encryptedBlob: {
      bytes: storedBytes.length,
      sha256: createHash('sha256').update(storedBytes).digest('hex'),
      ownerOnlyMode: (storedMetadata.mode & 0o777) === 0o600,
      excludesPlaintextFixture: !rawStored.includes(fixtureCredential)
    },
    removedMutation: removed,
    afterRemove: { anthropic: afterRemove, omlx: afterRemoveOmlx },
    credentialFilePresentAfterRemove,
    providerIsolation,
    mutationPass:
      beforeAnthropic.configured === false &&
      beforeOmlx.configured === false &&
      stored.configured === true &&
      afterStore.configured === true &&
      afterStoreOmlx.configured === false &&
      storedBytes.length > 0 &&
      (storedMetadata.mode & 0o777) === 0o600 &&
      !rawStored.includes(fixtureCredential) &&
      removed.configured === false &&
      afterRemove.configured === false &&
      afterRemoveOmlx.configured === false &&
      !credentialFilePresentAfterRemove &&
      providerIsolation
  };
  return { fixtureCredential, rawStored, proof };
}

async function currentGitRevision() {
  const result = await runCommand('git', ['rev-parse', 'HEAD'], { cwd: FRONTEND_ROOT });
  if (result.code !== 0) throw new Error(`git rev-parse failed: ${result.stderr.trim()}`);
  return result.stdout.trim();
}

async function writeJson(filePath, value) {
  await writeFile(filePath, `${JSON.stringify(value, null, 2)}\n`, 'utf8');
}

async function readEmittedArtifacts(rootPath, relativePath = '') {
  const directoryPath = path.join(rootPath, relativePath);
  const entries = await readdir(directoryPath, { withFileTypes: true });
  const artifacts = {};
  for (const entry of entries) {
    const childRelativePath = path.join(relativePath, entry.name);
    if (entry.isDirectory()) {
      Object.assign(artifacts, await readEmittedArtifacts(rootPath, childRelativePath));
    } else if (entry.isFile()) {
      artifacts[childRelativePath] = (await readFile(path.join(rootPath, childRelativePath))).toString('utf8');
    }
  }
  return artifacts;
}

export async function runProof(args) {
  const startedAt = nowIso();
  const sourceRevision = await currentGitRevision();
  if (args.sourceRevision && args.sourceRevision !== sourceRevision) {
    throw new Error(`Source revision mismatch: expected ${args.sourceRevision}, current ${sourceRevision}`);
  }
  await mkdir(args.outputRoot, { recursive: true });
  // AF_UNIX paths are short on macOS. `/tmp` is the system's canonical short
  // alias for the longer per-user temp path returned by os.tmpdir().
  const tempRoot = await mkdtemp(path.join('/tmp', 'chirality-psp-'));
  const userDataRoot = path.join(tempRoot, 'user-data');
  const extractionRoot = path.join(tempRoot, 'asar-extract');
  await mkdir(userDataRoot, { recursive: true, mode: 0o700 });
  await chmod(userDataRoot, 0o700);
  await mkdir(extractionRoot, { recursive: true });

  const identity = await captureAppIdentity(args.appPath, sourceRevision);
  const packagedMain = await extractPackagedMain(args.appPath, extractionRoot);
  const packagedPolicy = inspectPackagedPolicyMarkers(packagedMain);
  const executablePath = path.join(identity.appPath, 'Contents', 'MacOS', 'Chirality');
  const daemonLogPath = path.join(args.outputRoot, 'packaged-daemon.log');
  const guiLogPath = path.join(args.outputRoot, 'packaged-gui.log');
  const socketPath = path.join(userDataRoot, 'runtime', 'control.sock');
  const tokenFile = path.join(userDataRoot, 'runtime', 'auth', 'tokens', 'operator.token');
  const cleanEnv = { ...process.env };
  delete cleanEnv.ANTHROPIC_API_KEY;
  delete cleanEnv.CHIRALITY_ANTHROPIC_API_KEY;
  delete cleanEnv.CHIRALITY_OMLX_API_KEY;
  const proofEnv = {
    ...cleanEnv,
    CHIRALITY_USER_DATA: userDataRoot,
    CHIRALITY_SKIP_CLI_LAUNCHER: '1',
    CHIRALITY_NETWORK_POLICY_PROBE_URLS: [BLOCKED_PROBE_URL, LOOPBACK_PROBE_URL].join(','),
    CHIRALITY_NETWORK_POLICY_PROBE_DELAY_MS: '1000',
    CHIRALITY_NETWORK_POLICY_PROBE_TIMEOUT_MS: '3000',
    CHIRALITY_RENDERER_SECURITY_PROBE: '1',
    CHIRALITY_RENDERER_SECURITY_PROBE_DELAY_MS: '1500',
    CHIRALITY_EGRESS_LAYER_PROBE_URL: EGRESS_PROBE_URL
  };

  let daemon;
  let gui;
  let credentialInternal;
  let snapshots = [];
  let operationError;
  try {
    daemon = startLoggedProcess({
      label: 'packaged-runtime-daemon',
      command: executablePath,
      args: ['--runtime-daemon'],
      env: proofEnv,
      logPath: daemonLogPath
    });
    await waitForPath(socketPath, daemon);
    await waitForPath(tokenFile, daemon);
    const client = new RuntimeClient({ socketPath, tokenFile });
    await client.daemonStatus();

    credentialInternal = await runCredentialProof({
      client,
      userDataRoot
    });

    gui = startLoggedProcess({
      label: 'packaged-gui',
      command: executablePath,
      args: [],
      env: proofEnv,
      logPath: guiLogPath
    });
    const deadline = Date.now() + args.captureSeconds * 1000;
    while (Date.now() < deadline && gui.child.exitCode === null && gui.child.signalCode === null) {
      snapshots.push(await captureTcpSnapshot([daemon.child.pid, gui.child.pid]));
      const combined = `${gui.captured()}\n${daemon.captured()}`;
      if (
        combined.includes('Blocked renderer outbound request by network policy') &&
        combined.includes('[network-policy-probe]') &&
        combined.includes('[renderer-security-probe]') &&
        combined.includes('[egress-layer-probe]') &&
        combined.includes('renderer.navigation.denied') &&
        snapshots.length >= 4
      ) break;
      await sleep(300);
    }
    await writeJson(path.join(args.outputRoot, 'tcp-snapshots.json'), snapshots);
  } catch (error) {
    operationError = error;
  }

  const guiShutdown = await stopProcess(gui, 'packaged GUI').catch((error) => ({
    label: 'packaged GUI',
    started: Boolean(gui),
    confirmedStopped: false,
    streamClosed: false,
    error: error instanceof Error ? error.message : String(error)
  }));
  const daemonShutdown = await stopProcess(daemon, 'packaged runtime daemon').catch((error) => ({
    label: 'packaged runtime daemon',
    started: Boolean(daemon),
    confirmedStopped: false,
    streamClosed: false,
    error: error instanceof Error ? error.message : String(error)
  }));
  let tempRootRemoved = false;
  let tempRootRemovalError = null;
  try {
    await rm(tempRoot, { recursive: true, force: true });
    tempRootRemoved = true;
  } catch (error) {
    tempRootRemovalError = error instanceof Error ? error.message : String(error);
  }
  const cleanup = {
    gui: guiShutdown,
    daemon: daemonShutdown,
    tempRootRemoved,
    tempRootRemovalError,
    pass:
      guiShutdown.started === true &&
      guiShutdown.confirmedStopped === true &&
      guiShutdown.streamClosed === true &&
      daemonShutdown.started === true &&
      daemonShutdown.confirmedStopped === true &&
      daemonShutdown.streamClosed === true &&
      tempRootRemoved
  };
  await writeJson(path.join(args.outputRoot, 'cleanup.json'), cleanup);

  if (operationError) {
    throw new Error(
      `${operationError instanceof Error ? operationError.message : String(operationError)}; cleanup=${cleanup.pass ? 'confirmed' : 'FAILED'}`
    );
  }

  const daemonLog = await readFile(daemonLogPath, 'utf8');
  const guiLog = await readFile(guiLogPath, 'utf8');
  const combinedClosedLogs = `${daemonLog}\n${guiLog}`;
  const emittedArtifacts = await readEmittedArtifacts(args.outputRoot);
  const retainedSurfaces = {
    encryptedCredentialArtifact: credentialInternal.rawStored,
    ...Object.fromEntries(
      Object.entries(emittedArtifacts).map(([artifactPath, text]) => [`emitted:${artifactPath}`, text])
    )
  };
  const retainedSecretFindings = evaluateCredentialEvidence(
    credentialInternal.fixtureCredential,
    retainedSurfaces
  );
  const credentialProof = {
    ...credentialInternal.proof,
    retainedSecretFindings,
    evidenceSurfacesScannedAfterStreamClosure: Object.keys(retainedSurfaces),
    pass: credentialInternal.proof.mutationPass && retainedSecretFindings.length === 0
  };
  const networkProof = summarizeNetworkEvidence(combinedClosedLogs, snapshots);
  const rendererSecurityProof = summarizeRendererSecurityEvidence(combinedClosedLogs);
  const genericSensitiveFindings = [
    /https?:\/\/[^\s/@:]+:[^\s/@]+@/u,
    /[?&](?:api[_-]?key|token|credential|password)=/iu
  ].flatMap((pattern) => pattern.test(combinedClosedLogs) ? [{ pattern: pattern.source }] : []);
  const summary = {
    schema: 'chirality-packaged-security-proof/v1',
    status: packagedProofPass({
      identityPresent: Boolean(identity),
      packagedPolicyPass: packagedPolicy.allPresent,
      credentialProofPass: credentialProof.pass,
      networkProofPass: networkProof.pass,
      rendererSecurityProofPass: rendererSecurityProof.pass,
      cleanupPass: cleanup.pass,
      metadataLeakFindingCount: genericSensitiveFindings.length
    }) ? 'pass' : 'fail',
    startedAt,
    completedAt: nowIso(),
    proofBoundary: 'fresh-unsigned-packaged-app-network-safeStorage-renderer-hardening-and-security-byte-presence',
    artifactIdentity: identity,
    packagedPolicy,
    credentialProof,
    networkProof,
    rendererSecurityProof,
    cleanup,
    retainedMetadataLeakFindings: genericSensitiveFindings,
    exclusions: {
      realCredentialsUsed: false,
      signingOrNotarization: false,
      distributionOrPublication: false,
      ownerUserDataTouched: false,
      providerScopeExpanded: false
    }
  };
  await writeJson(path.join(args.outputRoot, 'summary.json'), summary);
  if (summary.status !== 'pass') process.exitCode = 1;
  return summary;
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help) {
    process.stdout.write(usage());
    return;
  }
  const summary = await runProof(args);
  process.stdout.write(`packaged security proof status: ${summary.status}\n`);
  process.stdout.write(`summary: ${path.join(args.outputRoot, 'summary.json')}\n`);
}

if (process.argv[1] && path.resolve(process.argv[1]) === SCRIPT_PATH) {
  main().catch((error) => {
    console.error(error instanceof Error ? error.message : String(error));
    process.exitCode = 1;
  });
}
