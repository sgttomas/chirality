import { cp, lstat, mkdir, rm } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const frontendRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const helperBundleName = 'Chirality Runtime Service.app';

export default async function embedRuntimeHelper(context) {
  if (context.electronPlatformName !== 'darwin') {
    return;
  }
  if (context.arch !== 3) {
    throw new Error(`Unsupported runtime helper architecture: ${context.arch}`);
  }

  const source = path.join(
    frontendRoot,
    'dist-runtime-helper',
    'mac-arm64',
    helperBundleName
  );
  const destinationDirectory = path.join(
    context.appOutDir,
    'Chirality.app',
    'Contents',
    'Library',
    'LoginItems'
  );
  const destination = path.join(destinationDirectory, helperBundleName);

  const sourceState = await lstat(source).catch(() => undefined);
  if (!sourceState?.isDirectory()) {
    throw new Error(`Standalone runtime helper bundle is missing: ${source}`);
  }

  await mkdir(destinationDirectory, { recursive: true });
  await rm(destination, { recursive: true, force: true });
  await cp(source, destination, {
    recursive: true,
    dereference: false,
    verbatimSymlinks: true,
    preserveTimestamps: true
  });
}
