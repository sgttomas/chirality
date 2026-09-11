export type DesktopEntryMode =
  | { mode: 'gui' }
  | { mode: 'runtime-daemon' }
  | { mode: 'runtime-cli'; arguments: readonly string[] }
  | { mode: 'invalid'; reason: string };

const RUNTIME_DAEMON_MODE = '--runtime-daemon';
const RUNTIME_CLI_MODE = '--runtime-cli';

/**
 * Select one fixed Electron entry mode. Packaged Electron puts application
 * arguments after the executable; development Electron also inserts the app
 * entry path. Reserved mode flags anywhere except that first application
 * argument are rejected instead of becoming caller-selected JavaScript or a
 * second mode switch.
 */
export function resolveDesktopEntryMode(
  argv: readonly string[],
  packaged: boolean
): DesktopEntryMode {
  const applicationArgumentIndex = packaged ? 1 : 2;
  const applicationArguments = argv.slice(applicationArgumentIndex);
  const selected = applicationArguments[0];
  const reservedPositions = applicationArguments
    .map((argument, index) =>
      argument === RUNTIME_DAEMON_MODE || argument === RUNTIME_CLI_MODE ? index : -1
    )
    .filter((index) => index >= 0);

  if (reservedPositions.some((index) => index !== 0) || reservedPositions.length > 1) {
    return { mode: 'invalid', reason: 'Runtime mode flags must be unique and first.' };
  }
  if (selected === RUNTIME_DAEMON_MODE) {
    if (applicationArguments.length !== 1) {
      return { mode: 'invalid', reason: 'Runtime daemon mode accepts no arguments.' };
    }
    return { mode: 'runtime-daemon' };
  }
  if (selected === RUNTIME_CLI_MODE) {
    return { mode: 'runtime-cli', arguments: applicationArguments.slice(1) };
  }
  return { mode: 'gui' };
}
