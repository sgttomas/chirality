import path from 'node:path';

/** The ordinary Finder/Dock application identity. */
export const DESKTOP_GUI_BUNDLE_IDENTIFIER = 'com.chirality.app';

/**
 * The nested daemon application's identity and stable package layout.
 *
 * The helper owns its executable rather than symlinking the GUI executable.
 * macOS resolves a symlinked executable back to the GUI bundle and collapses
 * both processes onto one LaunchServices identity, which is the defect this
 * layout removes.
 */
export const RUNTIME_HELPER_BUNDLE_IDENTIFIER =
  'com.chirality.app.runtime-helper';
export const RUNTIME_HELPER_BUNDLE_DIRECTORY_NAME =
  'Chirality Runtime Helper.app';
// Electron's macOS bootstrap requires CFBundleExecutable to match CFBundleName
// in order to locate `<name> Helper.app`. The containing helper bundle and its
// identifier remain distinct even though the native executable name is shared.
export const RUNTIME_HELPER_EXECUTABLE_NAME = 'Chirality';

export function resolveRuntimeHelperExecutable(
  desktopExecutable: string
): string {
  const contentsDirectory = path.resolve(
    path.dirname(desktopExecutable),
    '..'
  );
  return path.join(
    contentsDirectory,
    'Library',
    'LoginItems',
    RUNTIME_HELPER_BUNDLE_DIRECTORY_NAME,
    'Contents',
    'MacOS',
    RUNTIME_HELPER_EXECUTABLE_NAME
  );
}

export function isRuntimeHelperExecutable(executablePath: string): boolean {
  return path.basename(executablePath) === RUNTIME_HELPER_EXECUTABLE_NAME &&
    path.basename(path.resolve(executablePath, '..', '..', '..')) ===
      RUNTIME_HELPER_BUNDLE_DIRECTORY_NAME;
}
