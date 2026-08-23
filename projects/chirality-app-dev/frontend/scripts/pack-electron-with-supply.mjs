import { spawn } from 'node:child_process';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

import { verifyElectronDist } from './verify-electron-dist.mjs';

export function buildElectronBuilderArgs(electronDistDirectory) {
  if (typeof electronDistDirectory !== 'string' || electronDistDirectory.length === 0) {
    throw new Error('Verified Electron distribution directory is required');
  }
  return [
    '--mac',
    '--arm64',
    '--dir',
    '--publish',
    'never',
    `-c.electronDist=${electronDistDirectory}`
  ];
}

function spawnAndWait(command, args, options, spawnProcess) {
  return new Promise((resolve, reject) => {
    const child = spawnProcess(command, args, options);
    child.once('error', reject);
    child.once('exit', (code, signal) => {
      if (code === 0) {
        resolve();
        return;
      }
      reject(
        new Error(
          signal
            ? `electron-builder terminated by signal ${signal}`
            : `electron-builder exited with status ${String(code)}`
        )
      );
    });
  });
}

export async function runElectronPack({
  verify = verifyElectronDist,
  spawnProcess = spawn,
  env = process.env
} = {}) {
  const electronDistDirectory = await verify();
  const args = buildElectronBuilderArgs(electronDistDirectory);
  await spawnAndWait(
    'electron-builder',
    args,
    {
      stdio: 'inherit',
      shell: false,
      env: { ...env, CSC_IDENTITY_AUTO_DISCOVERY: 'false' }
    },
    spawnProcess
  );
}

const isMain =
  process.argv[1] && pathToFileURL(path.resolve(process.argv[1])).href === import.meta.url;
if (isMain) {
  try {
    await runElectronPack();
  } catch (error) {
    process.stderr.write(`Offline Electron packaging failed: ${error.message}\n`);
    process.exitCode = 1;
  }
}
