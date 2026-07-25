import { describe, expect, it, vi } from 'vitest';

vi.mock('electron', () => ({
  app: {
    getPath: vi.fn(() => '/Applications/Chirality.app/Contents/MacOS/Chirality'),
    isPackaged: true
  }
}));

import { renderCliLauncher } from '../../../electron/cli-launcher';

describe('electron/cli-launcher', () => {
  it('uses Electron embedded Node and pins daemon install to the desktop executable', () => {
    const source = renderCliLauncher({
      desktopExecutable: "/Applications/Chirality O'Brien.app/Contents/MacOS/Chirality",
      cliEntry: '/Applications/Chirality.app/Contents/Resources/runtime-cli/chirality-cli.mjs',
      userDataDirectory: '/Users/example/Library/Application Support/chirality-frontend'
    });

    expect(source).toContain('export ELECTRON_RUN_AS_NODE=1');
    expect(source).toContain('--executable "$desktop_executable"');
    expect(source).toContain('exec "$desktop_executable" "$cli_entry" "$@"');
    expect(source).toContain(`O'"'"'Brien`);
  });

  it("pins CHIRALITY_USER_DATA to the app's userData directory without overriding an explicit value", () => {
    const source = renderCliLauncher({
      desktopExecutable: '/Applications/Chirality.app/Contents/MacOS/Chirality',
      cliEntry: '/Applications/Chirality.app/Contents/Resources/runtime-cli/chirality-cli.mjs',
      userDataDirectory: '/Users/example/Library/Application Support/chirality-frontend'
    });

    expect(source).toContain(
      "app_user_data='/Users/example/Library/Application Support/chirality-frontend'"
    );
    expect(source).toContain('if [[ -z "${CHIRALITY_USER_DATA:-}" ]]; then');
    expect(source).toContain('export CHIRALITY_USER_DATA="$app_user_data"');
  });

  it('shell-quotes a userData directory containing a single quote', () => {
    const source = renderCliLauncher({
      desktopExecutable: '/Applications/Chirality.app/Contents/MacOS/Chirality',
      cliEntry: '/Applications/Chirality.app/Contents/Resources/runtime-cli/chirality-cli.mjs',
      userDataDirectory: "/Users/o'brien/Library/Application Support/chirality-frontend"
    });

    expect(source).toContain(
      `app_user_data='/Users/o'"'"'brien/Library/Application Support/chirality-frontend'`
    );
  });
});
