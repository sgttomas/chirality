import { copyFileSync, existsSync, readFileSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';

const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804';
const EVIDENCE = `${ROOT}/evidence/attempt8-runtime`;
const session = process.argv[2];
const branch = process.argv[3];
const branches = new Set(['PRE_CONTROLLER_NO_SESSION_B', 'CONTROLLER_NO_LLDB_SPAWN', 'LLDB_TERMINAL_BEFORE_ATTACH', 'POST_START_ABNORMAL_LLDB_TERMINAL', 'NORMAL_EXACT_DETACH', 'FORCED_WATCHDOG_TERMINAL', 'WATCHDOG_SIGNAL_ACCEPTED_RACE_TERMINAL', 'UNSAFE_TO_SIGNAL_AT_ABSOLUTE_DEADLINE']);
if (!['A', 'B', 'BOTH'].includes(session) || !branches.has(branch)) throw new Error('typed session and branch required');
const digest = (file) => createHash('sha256').update(readFileSync(file)).digest('hex');
const noSessionB = branch === 'PRE_CONTROLLER_NO_SESSION_B' || branch === 'CONTROLLER_NO_LLDB_SPAWN';
const selected = session === 'BOTH' ? ['A', 'B'] : [session];
for (const selectedSession of selected) {
  let files;
  if (selectedSession === 'A') {
    files = [['controller.stdout.bin', 'session-a.stdout.bin'], ['controller.stderr.bin', 'session-a.stderr.bin']];
  } else if (noSessionB) {
    writeFileSync(`${EVIDENCE}/session-b-absent.json`, `${JSON.stringify({ schema: 'chirality-dapp92-transcript-absence-r5/v1', branch, session: 'B', state: 'NO_SESSION_CREATED' }, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
    continue;
  } else {
    files = [['c197.input.bin', 'session-b.input.bin'], ['lldb.stdout.bin', 'session-b.stdout.bin'], ['lldb.stderr.bin', 'session-b.stderr.bin']];
  }
  const manifest = [];
  for (const [sourceName, targetName] of files) {
    const source = `${EVIDENCE}/${sourceName}`;
    const target = `${EVIDENCE}/${targetName}`;
    if (!existsSync(source)) throw new Error(`missing exact transcript input ${sourceName}`);
    copyFileSync(source, target, 1);
    manifest.push({ sourceName, targetName, sha256: digest(target), bytes: readFileSync(target).length });
  }
  writeFileSync(`${EVIDENCE}/session-${selectedSession.toLowerCase()}-transcript-manifest.json`, `${JSON.stringify({ schema: 'chirality-dapp92-transcript-capture-r5/v1', branch, session: selectedSession, files: manifest }, null, 2)}\n`, { flag: 'wx', mode: 0o600 });
}
