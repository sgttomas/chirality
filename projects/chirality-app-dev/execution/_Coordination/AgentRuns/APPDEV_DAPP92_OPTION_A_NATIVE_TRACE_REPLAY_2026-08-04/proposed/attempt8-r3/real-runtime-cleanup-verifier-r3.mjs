import { existsSync, readFileSync, writeFileSync } from 'node:fs';
const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804'; const EVIDENCE = `${ROOT}/evidence/attempt8-runtime`; const PROTOCOL = `${ROOT}/protocol`;
const cleanup = JSON.parse(readFileSync(`${EVIDENCE}/controller-cleanup-r3.json`, 'utf8'));
if (cleanup.schema !== 'chirality-dapp92-controller-cleanup-r3/v1' || cleanup.status !== 'ALL_CONTROLLER_CHILDREN_REAPED' || cleanup.failures.length !== 0) throw new Error('controller cleanup incomplete');
if (existsSync(`${PROTOCOL}/lldb-spawn-attempt.json`) && !existsSync(`${PROTOCOL}/detached.json`)) throw new Error('debugger terminal proof missing');
if (!existsSync(`${PROTOCOL}/lldb-spawn-attempt.json`) && !existsSync(`${PROTOCOL}/no-debugger-start-cleanup-safe-r3.json`)) throw new Error('no-debugger cleanup-safe proof missing');
writeFileSync(`${EVIDENCE}/cleanup-verifier-r3.json`, `${JSON.stringify({ schema: 'chirality-dapp92-cleanup-verifier-r3/v1', state: 'VERIFIED_ALL_OWNED_CHILDREN_REAPED', signalsIssued: [] }, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
