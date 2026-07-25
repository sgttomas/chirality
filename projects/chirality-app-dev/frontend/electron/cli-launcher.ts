import { app } from 'electron';
import { chmod, mkdir, readFile, rename, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import {
  daemonPostureEnvironment,
  resolveDesktopDaemonPosture
} from './desktop-daemon-posture';

/** Opt out of installing the launcher entirely (verification runs, CI). */
export const SKIP_CLI_LAUNCHER_ENV = 'CHIRALITY_SKIP_CLI_LAUNCHER';

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
  /**
   * Values the CLI needs in order to address the same runtime directory *and the
   * same LaunchAgent job* as the app.
   *
   * Rendered as *conditional* exports, so an externally supplied value still
   * wins — required so an isolated run (verification drills, an alternate
   * runtime root) is never silently redirected at the operator's real state.
   * Pinning only the runtime directory was not enough: the CLI still resolved
   * the default label and the package's historical `crash-only` restart posture,
   * so `chirality daemon install` reinstated the defect the in-app install fixes
   * and every verb addressed the operator's job regardless of isolation (V-D2).
   */
  pinnedEnvironment: Readonly<Record<string, string>>;
}): string {
  const desktopExecutable = quoteForShell(path.resolve(input.desktopExecutable));
  const cliEntry = quoteForShell(path.resolve(input.cliEntry));
  // Sorted so the rendered file is deterministic: byte-stability is what lets the
  // idempotent install below skip a rewrite.
  const pinnedExports = Object.keys(input.pinnedEnvironment)
    .sort()
    .map((name) => {
      const raw = input.pinnedEnvironment[name] ?? '';
      // Directory values are resolved; posture values pass through verbatim.
      const value = quoteForShell(name.endsWith('_USER_DATA') ? path.resolve(raw) : raw);
      return `if [[ -z "\${${name}:-}" ]]; then\n  export ${name}=${value}\nfi`;
    })
    .join('\n');
  return `#!/bin/zsh
set -eu
desktop_executable=${desktopExecutable}
cli_entry=${cliEntry}
export ELECTRON_RUN_AS_NODE=1
${pinnedExports}
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

export type CliLauncherInstallResult =
  | { status: 'written'; path: string }
  | { status: 'unchanged'; path: string }
  | { status: 'skipped'; path: string; reason: 'opted-out' };

/**
 * Install `~/.local/bin/chirality`, pinned to this bundle and this posture.
 *
 * Idempotent by content (V-D3). Every packaged launch previously rewrote the file
 * unconditionally with no override, so a verification run had to physically deny
 * write access to `~/.local/bin` to protect the operator's copy, and an ordinary
 * relaunch churned the file for nothing. The write now happens only when the
 * rendered content actually differs, and `CHIRALITY_SKIP_CLI_LAUNCHER=1` opts out
 * entirely.
 */
export async function installBundledCliLauncher(
  destination = path.join(os.homedir(), '.local', 'bin', 'chirality'),
  environment: Readonly<Record<string, string | undefined>> = process.env
): Promise<CliLauncherInstallResult> {
  if (environment[SKIP_CLI_LAUNCHER_ENV]?.trim()) {
    return { status: 'skipped', path: destination, reason: 'opted-out' };
  }

  const posture = resolveDesktopDaemonPosture(environment, app.getPath('userData'));
  const launcher = renderCliLauncher({
    desktopExecutable: app.getPath('exe'),
    cliEntry: resolveBundledCliEntry(),
    pinnedEnvironment: daemonPostureEnvironment(posture)
  });

  const existing = await readFile(destination, 'utf8').catch(() => undefined);
  if (existing === launcher) {
    return { status: 'unchanged', path: destination };
  }

  const directory = path.dirname(destination);
  await mkdir(directory, { recursive: true, mode: 0o755 });
  const temporary = path.join(
    directory,
    `.chirality.${process.pid}.${Date.now().toString(36)}.tmp`
  );
  await writeFile(temporary, launcher, { encoding: 'utf8', mode: 0o700, flag: 'wx' });
  await chmod(temporary, 0o700);
  await rename(temporary, destination);
  await chmod(destination, 0o700);
  return { status: 'written', path: destination };
}
