import { createHash, createHmac } from 'node:crypto';
import { appendFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';

const require = createRequire(import.meta.url);
const { verifyRegularFileIdentity } = require('../native-load-probe.cjs');
const GENERATION = '11111111-1111-4111-8111-111111111111';
const CHALLENGE = Buffer.alloc(32, 0x43);
const BEARER = Buffer.alloc(32, 0x42);
const REMOTE_TERMINALS = new Set(['peer-invalidated', 'peer-interrupted', 'peer-requirement-rejected']);
let pressureHoldUsed = false;

function exactArgs(argv) {
  const allowed = new Set(['--role', '--addon', '--addon-sha256', '--wrapper', '--wrapper-sha256', '--peer-requirement', '--log', '--diagnostic', '--request-id', '--mode']);
  if (argv.length % 2) throw new Error('invalid-arguments');
  const output = Object.create(null);
  for (let index = 0; index < argv.length; index += 2) {
    if (!allowed.has(argv[index]) || Object.hasOwn(output, argv[index])) throw new Error('invalid-arguments');
    output[argv[index]] = argv[index + 1];
  }
  for (const name of ['--role', '--addon', '--addon-sha256', '--wrapper', '--wrapper-sha256', '--peer-requirement']) if (!output[name]) throw new Error('invalid-arguments');
  return output;
}

function unwrap(result, label) {
  if (!result || result.state !== 'available') throw new Error(`${label}:${result?.reason ?? 'unavailable'}`);
  return result.value;
}
function proof(challenge, nonce) { return createHmac('sha256', challenge).update(nonce).digest(); }
function emit(record, log) {
  const line = `${JSON.stringify(record)}\n`;
  if (log) appendFileSync(log, line, { encoding: 'utf8', mode: 0o600 }); else process.stdout.write(line);
}
function diagnostic(args, event, detail = {}) { if (args['--diagnostic']) emit({ event, requestId: args['--request-id'], ...detail }, args['--diagnostic']); }
function wait(milliseconds) { return new Promise((resolve) => setTimeout(resolve, milliseconds)); }
function deadline(promise, milliseconds, label) {
  let timer;
  return Promise.race([promise, new Promise((_, reject) => { timer = setTimeout(() => reject(new Error(`timeout:${label}`)), milliseconds); })]).finally(() => clearTimeout(timer));
}

async function loadPublicBinding(args) {
  const wrapper = verifyRegularFileIdentity(args['--wrapper'], args['--wrapper-sha256']);
  const addon = verifyRegularFileIdentity(args['--addon'], args['--addon-sha256']);
  const api = await import(pathToFileURL(wrapper.path).href);
  const binding = unwrap(api.loadNativeAdmissionBinding(true, addon.path), 'native-binding');
  if (binding.createHostXpcServer === undefined || binding.createHostXpcClient === undefined) throw new Error('public-host-xpc-api-missing');
  return binding;
}

async function runServer(args, binding) {
  const log = args['--log'];
  if (!log) throw new Error('server-log-required');
  let port;
  const pending = new Set();
  port = unwrap(binding.createHostXpcServer({
    peerRequirement: args['--peer-requirement'], expectedEuid: process.geteuid(),
    onAdmitted(connectionId) { emit({ event: 'admitted', connectionId }, log); },
    onInvalidated(connectionId, reason) { emit({ event: 'invalidated', connectionId, reason }, log); },
    async onCeremonyOpen({ connectionId, requestId }) {
      emit({ event: 'open', connectionId, requestId }, log);
      if (requestId.startsWith('pressure-') && !pressureHoldUsed) { pressureHoldUsed = true; Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, 750); }
      else if (requestId === 'late-callback') await wait(750);
      return { requestId, challenge: Buffer.from(CHALLENGE), generation: GENERATION };
    },
    onCeremonyFinish({ connectionId, requestId, hostNonce, proof: supplied }) {
      if (!proof(CHALLENGE, hostNonce).equals(supplied)) throw new Error('synthetic-proof-mismatch');
      emit({ event: 'finish', connectionId, requestId }, log);
      if (!requestId.startsWith('pressure-')) {
        const task = wait(25).then(async () => {
          const ping = await port.ping(connectionId, { requestId: `ping-${requestId}`, sequence: 1n });
          emit({ event: 'pong', connectionId, requestId: ping.requestId, sequence: ping.sequence.toString() }, log);
          if (requestId === 'correct-close') await port.closeConnection(connectionId, 'lease-closed');
        }).catch((error) => emit({ event: 'server-operation-failed', requestId, reason: error.message }, log));
        pending.add(task); task.finally(() => pending.delete(task));
      }
      return { requestId, bearer: Buffer.from(BEARER), generation: GENERATION, scopes: ['account:read', 'account:control'] };
    }
  }), 'host-server');
  emit({ event: 'ready', service: port.service }, log);
  const close = async (signal) => {
    try { await Promise.allSettled([...pending]); await port.close(); emit({ event: 'closed', signal }, log); process.exitCode = 0; }
    catch (error) { emit({ event: 'close-failed', reason: error.code ?? error.message }, log); process.exitCode = 1; }
  };
  process.once('SIGTERM', () => { void close('SIGTERM'); });
  process.once('SIGINT', () => { void close('SIGINT'); });
  await new Promise(() => {});
}

function clientConfig(args, invalidated, onPing = ({ requestId, sequence }) => ({ requestId, sequence })) {
  return { peerRequirement: args['--peer-requirement'], expectedEuid: process.geteuid(), onInvalidated: invalidated, onPing };
}
async function closeRequired(args, port) {
  try { await port.close(); diagnostic(args, 'close-completed'); }
  catch (error) { diagnostic(args, 'close-failed', { reason: String(error?.message ?? error) }); throw error; }
}

async function runPressure(args, binding) {
  const ports = [];
  try {
    const attempts = Array.from({ length: 65 }, async (_, index) => {
      const pressureId = `pressure-${String(index).padStart(2, '0')}`;
      const port = unwrap(binding.createHostXpcClient(clientConfig(args, () => {})), 'pressure-client');
      ports.push(port); diagnostic(args, 'client-created', { pressureId }); diagnostic(args, 'provision-invoked', { pressureId });
      return port.provision({ requestId: pressureId, onChallenge({ requestId: observed, challenge }) {
        if (observed !== pressureId) throw new Error('pressure-request-mismatch');
        const hostNonce = createHash('sha256').update(pressureId).digest();
        return { requestId: pressureId, hostNonce, proof: proof(challenge, hostNonce) };
      } });
    });
    const settled = await deadline(Promise.allSettled(attempts), 8000, 'pressure-settlement');
    const rejected = settled.filter((item) => item.status === 'rejected');
    if (rejected.some((item) => !/Host XPC unavailable|host-xpc|delivery|closed/u.test(String(item.reason?.message ?? item.reason)))) throw new Error('pressure-unexpected-rejection');
    const closes = await Promise.allSettled(ports.map((port) => port.close()));
    const rejectedCloses = closes.filter((item) => item.status === 'rejected');
    if (rejectedCloses.some((item) => item.reason?.code !== 'delivery-unavailable')) throw new Error('pressure-close-failed');
    diagnostic(args, 'close-completed', { count: ports.length });
    emit({ result: 'PASS', mode: 'pressure', attempts: 65, fulfilled: settled.length - rejected.length, provisionTerminallyRejected: rejected.length, closeTerminallyRejected: rejectedCloses.length, terminallyRejected: rejected.length + rejectedCloses.length });
  } catch (error) {
    const closes = await Promise.allSettled(ports.map((port) => port.close()));
    diagnostic(args, 'close-after-failure', { rejected: closes.filter((item) => item.status === 'rejected').length });
    throw error;
  }
}

async function runPendingClose(args, binding) {
  const port = unwrap(binding.createHostXpcClient(clientConfig(args, () => {})), 'pending-close-client');
  diagnostic(args, 'client-created');
  let callbackRan = false;
  const provision = port.provision({ requestId: args['--request-id'], onChallenge() {
    callbackRan = true; diagnostic(args, 'challenge-observed');
    const hostNonce = Buffer.alloc(32, 0x4e);
    return { requestId: args['--request-id'], hostNonce, proof: proof(CHALLENGE, hostNonce) };
  } });
  diagnostic(args, 'provision-invoked');
  const settlement = provision.then(() => ({ state: 'fulfilled' }), (error) => ({ state: 'rejected', reason: String(error?.message ?? error) }));
  await wait(50); await closeRequired(args, port);
  if ((await deadline(settlement, 1000, 'pending-close-rejection')).state !== 'rejected') throw new Error('pending-provision-resurrected');
  await wait(900);
  if (callbackRan) throw new Error('late-challenge-delivered');
  emit({ result: 'PASS', mode: 'pending-close', requestId: args['--request-id'] });
}

async function runOrdinary(args, binding) {
  const requestId = args['--request-id'];
  let invalidate;
  const invalidation = new Promise((resolve) => { invalidate = resolve; });
  let challengeObserved = false;
  let grantObserved = false;
  let pingObserved;
  const ping = new Promise((resolve) => { pingObserved = resolve; });
  const port = unwrap(binding.createHostXpcClient(clientConfig(
    args,
    (reason) => { diagnostic(args, 'invalidated', { reason }); invalidate(reason); },
    ({ requestId: pingId, sequence }) => { diagnostic(args, 'ping-observed', { pingId, sequence: sequence.toString() }); pingObserved(); return { requestId: pingId, sequence }; }
  )), 'host-client');
  diagnostic(args, 'client-created'); diagnostic(args, 'provision-invoked');
  const provision = port.provision({ requestId, onChallenge({ requestId: observed, challenge, generation }) {
    challengeObserved = true; diagnostic(args, 'challenge-observed');
    if (observed !== requestId || generation !== GENERATION || challenge.length !== 32) throw new Error('challenge-binding-mismatch');
    const hostNonce = createHash('sha256').update(requestId).digest();
    return { requestId, hostNonce, proof: proof(challenge, hostNonce) };
  } });
  const settlement = provision.then((grant) => ({ state: 'fulfilled', grant }), (error) => ({ state: 'rejected', code: String(error?.code ?? ''), reason: String(error?.message ?? error) }));
  try {
    if (args['--mode'] === 'wrong-peer') {
      const observation = await Promise.race([settlement, invalidation.then((reason) => ({ state: 'remote-terminal', reason })), wait(3000).then(() => ({ state: 'observation-expired' }))]);
      if (observation.state === 'fulfilled') throw new Error('wrong-peer-admitted');
      if (challengeObserved || grantObserved) throw new Error('wrong-peer-reached-ceremony');
      if (observation.state === 'rejected') {
        const reason = await Promise.race([invalidation, wait(250).then(() => null)]);
        if (!REMOTE_TERMINALS.has(reason)) throw new Error(`wrong-peer-untyped-terminal:${observation.code || 'none'}`);
        await closeRequired(args, port);
        emit({ result: 'PASS', mode: args['--mode'], requestId, disposition: 'remote-terminal', invalidation: reason }); return;
      }
      if (observation.state === 'remote-terminal') {
        if (!REMOTE_TERMINALS.has(observation.reason)) throw new Error(`wrong-peer-invalidated-as:${observation.reason}`);
        if ((await deadline(settlement, 1000, 'wrong-peer-terminal-settlement')).state !== 'rejected') throw new Error('wrong-peer-terminal-fulfilled');
        await closeRequired(args, port);
        emit({ result: 'PASS', mode: args['--mode'], requestId, disposition: 'remote-terminal', invalidation: observation.reason }); return;
      }
      await closeRequired(args, port);
      if ((await deadline(settlement, 1000, 'wrong-peer-local-close-settlement')).state !== 'rejected' || challengeObserved || grantObserved) throw new Error('wrong-peer-local-close-invalid');
      emit({ result: 'PASS', mode: args['--mode'], requestId, disposition: 'observation-expired-local-close' }); return;
    }
    const grant = await deadline(provision, 5000, 'provision');
    grantObserved = true; diagnostic(args, 'grant-observed');
    if (grant.requestId !== requestId || grant.generation !== GENERATION || grant.bearer.length !== 32 || JSON.stringify(grant.scopes) !== JSON.stringify(['account:read', 'account:control'])) throw new Error('grant-binding-mismatch');
    if (args['--mode'] === 'server-close') {
      const reason = await deadline(invalidation, 3000, 'server-close');
      await port.provision({ requestId: `${requestId}-late`, onChallenge() { throw new Error('late-callback-ran'); } }).then(() => { throw new Error('closed-client-reprovisioned'); }, () => undefined);
      await closeRequired(args, port);
      emit({ result: 'PASS', mode: args['--mode'], requestId, invalidation: reason }); return;
    }
    await deadline(ping, 3000, 'client-close-ping');
    await closeRequired(args, port); await port.close();
    await port.provision({ requestId: `${requestId}-late`, onChallenge() { throw new Error('late-callback-ran'); } }).then(() => { throw new Error('closed-client-reprovisioned'); }, () => undefined);
    emit({ result: 'PASS', mode: args['--mode'], requestId });
  } catch (error) {
    diagnostic(args, 'client-failed', { reason: String(error?.message ?? error) });
    try { await closeRequired(args, port); } catch {}
    throw error;
  }
}

async function runClient(args, binding) {
  if (!args['--request-id'] || !['server-close', 'client-close', 'wrong-peer', 'pressure', 'pending-close'].includes(args['--mode'])) throw new Error('invalid-client-case');
  diagnostic(args, 'client-binding-loaded');
  if (args['--mode'] === 'pressure') return runPressure(args, binding);
  if (args['--mode'] === 'pending-close') return runPendingClose(args, binding);
  return runOrdinary(args, binding);
}

export async function main(argv = process.argv.slice(2)) {
  const args = exactArgs(argv); diagnostic(args, 'load-started');
  const binding = await loadPublicBinding(args); diagnostic(args, 'load-completed');
  if (args['--role'] === 'server') return runServer(args, binding);
  if (args['--role'] === 'client') return runClient(args, binding);
  throw new Error('invalid-role');
}

if (import.meta.url === pathToFileURL(process.argv[1]).href) {
  main().catch((error) => {
    let args = {}; try { args = exactArgs(process.argv.slice(2)); } catch {}
    diagnostic(args, 'driver-failed', { reason: error instanceof Error ? error.message : 'unknown-failure' });
    emit({ result: 'FAIL', reason: error instanceof Error ? error.message : 'unknown-failure' }); process.exitCode = 1;
  });
}
