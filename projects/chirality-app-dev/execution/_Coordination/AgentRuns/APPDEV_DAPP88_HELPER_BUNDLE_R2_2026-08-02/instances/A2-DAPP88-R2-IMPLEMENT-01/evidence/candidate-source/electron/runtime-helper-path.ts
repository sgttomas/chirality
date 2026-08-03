import path from 'node:path';

// Do not end this product name in " Helper": electron-builder deliberately
// strips that suffix from a macOS main executable because it is reserved for
// Chromium child helpers. "Service" keeps product, bundle, and executable names
// identical while the bundle identifier retains the runtime-helper identity.
export const RUNTIME_HELPER_PRODUCT_NAME = 'Chirality Runtime Service';
export const RUNTIME_HELPER_BUNDLE_NAME = `${RUNTIME_HELPER_PRODUCT_NAME}.app`;
export const RUNTIME_HELPER_EXECUTABLE_NAME = RUNTIME_HELPER_PRODUCT_NAME;
export const RUNTIME_HELPER_BUNDLE_ID = 'com.chirality.app.runtime-helper';

/** Resolve the embedded standalone helper from the packaged GUI executable. */
export function resolveRuntimeHelperExecutable(desktopExecutable: string): string {
  const contentsDirectory = path.resolve(path.dirname(desktopExecutable), '..');
  return path.join(
    contentsDirectory,
    'Library',
    'LoginItems',
    RUNTIME_HELPER_BUNDLE_NAME,
    'Contents',
    'MacOS',
    RUNTIME_HELPER_EXECUTABLE_NAME
  );
}
