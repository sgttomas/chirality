import { app } from 'electron';
import { chmod, mkdir, rename, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';

function quoteForShell(value: string): string {
  return `'${value.replaceAll("'", "'\"'\"'")}'`;
}

export function resolveBundledCliEntry(): string {
  return app.isPackaged
    ? path.join(process.resourcesPath, 'runtime-cli', 'chirality-cli.mjs')
    : path.resolve(__dirname, '..', 'dist-runtime', 'chirality-cli.mjs');
}

export function renderCliLauncher(input: {
  desktopExecutable: string;
  cliEntry: string;
}): string {
  const desktopExecutable = quoteForShell(path.resolve(input.desktopExecutable));
  const cliEntry = quoteForShell(path.resolve(input.cliEntry));
  return `#!/bin/zsh
set -eu
desktop_executable=${desktopExecutable}
cli_entry=${cliEntry}
export ELECTRON_RUN_AS_NODE=1
if [[ "\${1:-}" == "daemon" && "\${2:-}" == "install" ]]; then
  for argument in "$@"; do
    if [[ "$argument" == "--executable" || "$argument" == --executable=* ]]; then
      exec "$desktop_executable" "$cli_entry" "$@"
    fi
  done
  exec "$desktop_executable" "$cli_entry" "$@" --executable "$desktop_executable"
fi
exec "$desktop_executable" "$cli_entry" "$@"
`;
}

export async function installBundledCliLauncher(
  destination = path.join(os.homedir(), '.local', 'bin', 'chirality')
): Promise<string> {
  const directory = path.dirname(destination);
  await mkdir(directory, { recursive: true, mode: 0o755 });
  const temporary = path.join(
    directory,
    `.chirality.${process.pid}.${Date.now().toString(36)}.tmp`
  );
  const launcher = renderCliLauncher({
    desktopExecutable: app.getPath('exe'),
    cliEntry: resolveBundledCliEntry()
  });
  await writeFile(temporary, launcher, { encoding: 'utf8', mode: 0o700, flag: 'wx' });
  await chmod(temporary, 0o700);
  await rename(temporary, destination);
  await chmod(destination, 0o700);
  return destination;
}
