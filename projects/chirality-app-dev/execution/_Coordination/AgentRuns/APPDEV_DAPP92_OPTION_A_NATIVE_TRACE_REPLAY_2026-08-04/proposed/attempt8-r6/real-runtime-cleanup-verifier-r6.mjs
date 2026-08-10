import { existsSync, readFileSync, writeFileSync } from 'node:fs';
const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804';
const EVIDENCE = `${ROOT}/evidence/attempt8-runtime`;
const PROTOCOL = `${ROOT}/protocol`;
const cleanup = JSON.parse(readFileSync(`${EVIDENCE}/controller-cleanup-r6.json`, 'utf8'));
const proof = JSON.parse(readFileSync(`${PROTOCOL}/session-terminal-proof.json`, 'utf8'));
if (cleanup.schema !== 'chirality-dapp92-controller-cleanup-r6/v1' || cleanup.status !== 'ALL_CONTROLLER_CHILDREN_TERMINAL' || cleanup.failures.length !== 0 || cleanup.callbackErrors.length !== 0) throw new Error('controller cleanup incomplete');
for (const name of ['registration', 'stale', 'gui', 'helper']) {
  const child = cleanup[name];
  if (child?.terminal !== true) throw new Error(`${name} not terminal`);
  if (child.present && (child.exit?.observedEvent !== 'close' || child.exit?.streamsDrained !== true)) throw new Error(`${name} lacks drained close proof`);
}
if (proof.schema !== 'chirality-dapp92-session-terminal-proof-r6/v1' || proof.terminalSafeForCleanup !== true || !existsSync(`${PROTOCOL}/cleanup-permission.json`)) throw new Error('terminal branch proof/permission missing');
writeFileSync(`${EVIDENCE}/cleanup-verifier-r6.json`, `${JSON.stringify({ schema: 'chirality-dapp92-cleanup-verifier-r6/v1', state: 'VERIFIED_ALL_OWNED_CHILDREN_TERMINAL', branch: proof.state }, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
