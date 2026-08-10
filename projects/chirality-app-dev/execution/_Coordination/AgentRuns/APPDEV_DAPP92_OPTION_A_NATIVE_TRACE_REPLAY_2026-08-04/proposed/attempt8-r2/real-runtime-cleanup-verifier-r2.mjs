import { existsSync, readFileSync, writeFileSync } from 'node:fs';

const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804';
const EVIDENCE = `${ROOT}/evidence/attempt8-runtime`;
const PROTOCOL = `${ROOT}/protocol`;
const cleanupPath = `${EVIDENCE}/controller-cleanup-r2.json`;
if (!existsSync(cleanupPath)) throw new Error('controller cleanup receipt missing');
const cleanup = JSON.parse(readFileSync(cleanupPath, 'utf8'));
if (cleanup.schema !== 'chirality-dapp92-controller-cleanup-r2/v1' || cleanup.status !== 'ALL_CONTROLLER_CHILDREN_REAPED') throw new Error('controller cleanup is not safe');
const controllerExists = existsSync(`${PROTOCOL}/controller.json`);
if (!controllerExists) {
  const pre = JSON.parse(readFileSync(`${PROTOCOL}/pre-controller-cleanup-safe.json`, 'utf8'));
  if (pre.schema !== 'chirality-dapp92-pre-controller-cleanup-safe-r2/v1' || pre.state !== 'NO_CONTROLLER_RECORD_ALL_CHILDREN_REAPED') throw new Error('pre-controller cleanup-safe receipt mismatch');
}
const receipt = {
  schema: 'chirality-dapp92-cleanup-verifier-r2/v1',
  state: 'VERIFIED_CONTROLLER_OWNED_HANDLES_REAPED',
  controllerRecordPresent: controllerExists,
  signaledPids: [],
  note: 'This verifier performs no process signal, PID probe, or process inspection.'
};
writeFileSync(`${EVIDENCE}/cleanup-verifier-r2.json`, `${JSON.stringify(receipt, null, 2)}\n`, { encoding: 'utf8', mode: 0o600, flag: 'wx' });
