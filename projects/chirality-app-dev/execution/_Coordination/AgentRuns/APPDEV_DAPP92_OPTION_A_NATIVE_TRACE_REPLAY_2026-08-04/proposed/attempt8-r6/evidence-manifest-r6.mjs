import { readdirSync, readFileSync, statSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { relative, resolve } from 'node:path';

const root = '/Users/ryan/.codex/worktrees/7388/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04/evidence/attempt8-runtime-r6';
const output = `${root}/EVIDENCE_MANIFEST.sha256`;
const files = [];
function walk(directory) {
  for (const name of readdirSync(directory).sort()) {
    const file = resolve(directory, name);
    const status = statSync(file, { throwIfNoEntry: true });
    if (status.isDirectory()) walk(file);
    else if (status.isFile() && file !== output) files.push(file);
    else throw new Error(`unsupported evidence entry ${file}`);
  }
}
walk(root);
files.sort((a, b) => Buffer.from(relative(root, a)).compare(Buffer.from(relative(root, b))));
const lines = files.map((file) => `${createHash('sha256').update(readFileSync(file)).digest('hex')}  ${relative(root, file)}`);
writeFileSync(output, `${lines.join('\n')}\n`, { flag: 'wx', mode: 0o600 });
if (readFileSync(output, 'utf8') !== `${lines.join('\n')}\n`) throw new Error('durable evidence manifest readback mismatch');
