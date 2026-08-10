import { existsSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { readFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';

const REPO = '/Users/ryan/.codex/worktrees/7388/chirality';
const ROOT = '/private/tmp/chirality-dapp92-option-a-20260804';
const expected = new Map([
  ['projects/chirality-app-dev/frontend/electron/cli-launcher.ts', '850f7b00bd50af669d2cb6c1963c9b5f9b47f5a30badeda754752f3b896d335b'],
  ['projects/chirality-app-dev/frontend/electron/main.ts', '16ad6688abaebd0bb1bfe04921a7eb1d20601bf2f2af983153da3c734f44ad1f'],
  ['projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts', '5006bef6922295eb24c54f4a034f2d42929c71b80704b4fe03f8e7e5af36026a'],
  ['projects/chirality-app-dev/frontend/package.json', '1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53'],
  ['projects/chirality-app-dev/frontend/package-lock.json', '5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56'],
  ['projects/chirality-app-dev/frontend/scripts/build-electron.mjs', 'a6759be00c3bf2aaf9bd172657d723cf724bae33aa9a1941724cc173eaee5558'],
  ['projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts', '1918ae7dc10c12608a0d591db565f538a9ed91289e2b78eb728483d9c7cf91e9'],
  ['projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts', 'f8b6d8c2d5c2d8f947e585dd5d99a85a9b207a7277de8ddcb2214cab92136be6']
]);
for (const [path, hash] of expected) if (createHash('sha256').update(readFileSync(`${REPO}/${path}`)).digest('hex') !== hash) throw new Error(`baseline hash mismatch: ${path}`);
const status = spawnSync('/usr/bin/git', ['status', '--short', '--untracked-files=all', '--', 'projects/chirality-app-dev/frontend'], { cwd: REPO, encoding: 'utf8', timeout: 10000 });
if (status.status !== 0 || status.signal !== null || status.error || status.stdout !== '') throw new Error('frontend Git status not exactly empty');
for (const path of ['electron-builder.runtime-helper.json', 'electron/runtime-helper-entry.ts', 'electron/runtime-helper-path.ts', 'scripts/embed-runtime-helper.mjs', 'src/__tests__/electron/runtime-helper-packaging.test.ts', 'node_modules', 'dist', 'dist-runtime-helper', 'dist-electron', 'dist-runtime', '.next']) if (existsSync(`${REPO}/projects/chirality-app-dev/frontend/${path}`)) throw new Error(`derivative remains: ${path}`);
writeFileSync(`${ROOT}/TEMP_DELETE_ALLOWED`, 'chirality-dapp92-rollback-verified-r4/v1\n', { flag: 'wx', mode: 0o600 });
