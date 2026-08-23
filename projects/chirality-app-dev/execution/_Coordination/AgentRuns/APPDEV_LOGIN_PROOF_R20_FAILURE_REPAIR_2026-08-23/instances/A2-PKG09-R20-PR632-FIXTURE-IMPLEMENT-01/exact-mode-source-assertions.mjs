import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';

const testPath =
  'projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts';
const proofPath =
  'projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs';
const testSource = await readFile(testPath, 'utf8');
const proofSource = await readFile(proofPath);
const blockStart = testSource.indexOf(
  "const runtimeDirectory = path.join(sessionRoot, 'runtime-data', 'runtime');"
);
const blockEnd = testSource.indexOf('if (state.installError) throw state.installError;', blockStart);
if (blockStart < 0 || blockEnd < 0) throw new Error('Fake packaged-install block not found');

const block = testSource.slice(blockStart, blockEnd);
const counts = {
  mkdir: (block.match(/await mkdir\(/g) ?? []).length,
  privateDirectoryMode: (block.match(/\{ recursive: true, mode: 0o700 \}/g) ?? []).length,
  writeFile: (block.match(/await writeFile\(/g) ?? []).length,
  privateFileMode: (block.match(/mode: 0o600/g) ?? []).length
};
if (
  counts.mkdir !== 2 ||
  counts.privateDirectoryMode !== 2 ||
  counts.writeFile !== 3 ||
  counts.privateFileMode !== 3
) {
  throw new Error(`Unexpected fixture mode inventory: ${JSON.stringify(counts)}`);
}

const proofSha256 = createHash('sha256').update(proofSource).digest('hex');
if (proofSha256 !== 'f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306') {
  throw new Error(`Product proof script changed: ${proofSha256}`);
}

console.log(
  JSON.stringify({
    status: 'PASS',
    counts,
    directories: {
      runtime: '0700 via recursive logs creation',
      logs: '0700',
      auth: '0700 via recursive tokens creation',
      tokens: '0700'
    },
    files: {
      'daemon.stdout.log': '0600',
      'daemon.stderr.log': '0600',
      'operator.token': '0600'
    },
    proofSha256
  })
);
