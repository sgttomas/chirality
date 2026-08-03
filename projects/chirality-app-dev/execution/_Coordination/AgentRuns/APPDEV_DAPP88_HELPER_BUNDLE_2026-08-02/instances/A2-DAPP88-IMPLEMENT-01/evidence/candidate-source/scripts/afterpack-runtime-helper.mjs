#!/usr/bin/env node

/**
 * Materialize the distinct runtime-daemon application selected by D-APP-88.
 *
 * A helper-local copy of Electron's main Mach-O is load-bearing. A symlinked
 * executable resolves back to the GUI bundle identity. A symlinked Frameworks
 * directory is also deliberately forbidden: the accepted F1 predecessor drill
 * showed Electron aborting before application logging when Frameworks was a
 * symlink. The minimal real framework set below is the main executable's exact
 * non-system dependency closure. Resources may be shared by symlink; that arm
 * started the daemon successfully in the predecessor drill.
 */

import { execFileSync } from 'node:child_process';
import {
  constants,
  copyFileSync,
  cpSync,
  existsSync,
  lstatSync,
  mkdirSync,
  readdirSync,
  readlinkSync,
  rmSync,
  symlinkSync
} from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

export const DESKTOP_GUI_BUNDLE_IDENTIFIER = 'com.chirality.app';
export const RUNTIME_HELPER_BUNDLE_IDENTIFIER =
  'com.chirality.app.runtime-helper';
export const RUNTIME_HELPER_BUNDLE_DIRECTORY_NAME =
  'Chirality Runtime Helper.app';
// Electron's macOS helper lookup requires executableName === CFBundleName.
export const RUNTIME_HELPER_EXECUTABLE_NAME = 'Chirality';

const REQUIRED_FRAMEWORK_ENTRIES = [
  'Electron Framework.framework',
  'Mantle.framework',
  'ReactiveObjC.framework',
  'Squirrel.framework'
];
const ELECTRON_CHILD_HELPER_DIRECTORY_NAME = 'Chirality Helper.app';

function readPlistValue(plistPath, key) {
  return execFileSync('plutil', ['-extract', key, 'raw', '-o', '-', plistPath], {
    encoding: 'utf8'
  }).trim();
}

function replacePlistString(plistPath, key, value) {
  execFileSync('plutil', ['-replace', key, '-string', value, plistPath]);
}

function copyClone(source, destination) {
  cpSync(source, destination, {
    recursive: true,
    preserveTimestamps: true,
    verbatimSymlinks: true,
    mode: constants.COPYFILE_FICLONE
  });
}

export function createRuntimeHelperBundle(appPath) {
  const contentsDirectory = path.join(appPath, 'Contents');
  const parentPlist = path.join(contentsDirectory, 'Info.plist');
  const parentIdentifier = readPlistValue(parentPlist, 'CFBundleIdentifier');
  if (parentIdentifier !== DESKTOP_GUI_BUNDLE_IDENTIFIER) {
    throw new Error(
      `Unexpected desktop bundle identifier ${JSON.stringify(parentIdentifier)}; expected ${DESKTOP_GUI_BUNDLE_IDENTIFIER}`
    );
  }

  const parentExecutableName = readPlistValue(parentPlist, 'CFBundleExecutable');
  const parentExecutable = path.join(
    contentsDirectory,
    'MacOS',
    parentExecutableName
  );
  if (!existsSync(parentExecutable)) {
    throw new Error(`Desktop executable is missing: ${parentExecutable}`);
  }

  const parentFrameworks = path.join(contentsDirectory, 'Frameworks');
  // Remove the exact experimental predecessor location so an incremental
  // electron-builder output cannot accidentally ship two top-level runtime
  // helpers. The final manifest requires exactly the LoginItems bundle below.
  rmSync(
    path.join(parentFrameworks, RUNTIME_HELPER_BUNDLE_DIRECTORY_NAME),
    { recursive: true, force: true }
  );
  const bundlePath = path.join(
    contentsDirectory,
    'Library',
    'LoginItems',
    RUNTIME_HELPER_BUNDLE_DIRECTORY_NAME
  );
  const helperContents = path.join(bundlePath, 'Contents');
  const helperMacOS = path.join(helperContents, 'MacOS');
  const helperFrameworks = path.join(helperContents, 'Frameworks');
  const helperExecutable = path.join(
    helperMacOS,
    RUNTIME_HELPER_EXECUTABLE_NAME
  );
  const helperPlist = path.join(helperContents, 'Info.plist');

  rmSync(bundlePath, { recursive: true, force: true });
  mkdirSync(helperMacOS, { recursive: true, mode: 0o755 });
  mkdirSync(helperFrameworks, { recursive: true, mode: 0o755 });

  copyFileSync(
    parentExecutable,
    helperExecutable,
    constants.COPYFILE_FICLONE
  );
  for (const entry of REQUIRED_FRAMEWORK_ENTRIES) {
    const source = path.join(parentFrameworks, entry);
    if (!existsSync(source)) {
      throw new Error(`Required Electron framework entry is missing: ${source}`);
    }
    copyClone(source, path.join(helperFrameworks, entry));
  }
  // Electron resolves CHILD_PROCESS_EXE before application JavaScript runs.
  // Keep the conventional generic helper next to the helper-local framework;
  // its five-level MainApplicationBundlePath climb then lands on this distinct
  // runtime application. Preserve Electron's framework/helper identifiers:
  // Chromium's framework resource lookup depends on those native identities.
  copyClone(
    path.join(parentFrameworks, ELECTRON_CHILD_HELPER_DIRECTORY_NAME),
    path.join(helperFrameworks, ELECTRON_CHILD_HELPER_DIRECTORY_NAME)
  );

  // The helper consumes the exact same asar, unpacked native modules,
  // instruction root and runtime CLI as the GUI. This is a directory symlink,
  // not an executable or Frameworks symlink, and was the working F1 arm.
  symlinkSync('../../../../Resources', path.join(helperContents, 'Resources'));

  copyFileSync(parentPlist, helperPlist, constants.COPYFILE_FICLONE);
  replacePlistString(
    helperPlist,
    'CFBundleDisplayName',
    'Chirality Runtime Helper'
  );
  replacePlistString(
    helperPlist,
    'CFBundleExecutable',
    RUNTIME_HELPER_EXECUTABLE_NAME
  );
  replacePlistString(
    helperPlist,
    'CFBundleIdentifier',
    RUNTIME_HELPER_BUNDLE_IDENTIFIER
  );
  // CFBundleName intentionally remains inherited. Electron's application name
  // and safeStorage namespace therefore stay derived from shared package
  // metadata, matching the accepted cross-identity continuity evidence.
  execFileSync('plutil', ['-insert', 'LSUIElement', '-bool', 'true', helperPlist]);
  execFileSync('plutil', ['-lint', helperPlist], { stdio: 'ignore' });

  const resourcesLink = path.join(helperContents, 'Resources');
  if (!lstatSync(resourcesLink).isSymbolicLink()) {
    throw new Error(`Helper Resources is not a symlink: ${resourcesLink}`);
  }
  if (lstatSync(helperFrameworks).isSymbolicLink()) {
    throw new Error(`Helper Frameworks must be a real directory: ${helperFrameworks}`);
  }

  const rejectAbsoluteSymlinks = (directory) => {
    for (const entry of readdirSync(directory, { withFileTypes: true })) {
      const entryPath = path.join(directory, entry.name);
      if (entry.isSymbolicLink()) {
        const target = readlinkSync(entryPath);
        if (path.isAbsolute(target)) {
          throw new Error(`Helper contains an absolute symlink: ${entryPath} -> ${target}`);
        }
        continue;
      }
      if (entry.isDirectory()) {
        rejectAbsoluteSymlinks(entryPath);
      }
    }
  };
  rejectAbsoluteSymlinks(helperContents);

  const helperBundles = [];
  const visit = (directory) => {
    for (const entry of readdirSync(directory, { withFileTypes: true })) {
      if (!entry.isDirectory()) {
        continue;
      }
      const entryPath = path.join(directory, entry.name);
      if (entry.name === RUNTIME_HELPER_BUNDLE_DIRECTORY_NAME) {
        helperBundles.push(entryPath);
        continue;
      }
      visit(entryPath);
    }
  };
  visit(contentsDirectory);
  if (helperBundles.length !== 1 || helperBundles[0] !== bundlePath) {
    throw new Error(
      `Package must contain exactly one runtime helper at ${bundlePath}; found ${JSON.stringify(helperBundles)}`
    );
  }

  return {
    appPath,
    bundlePath,
    executablePath: helperExecutable,
    guiBundleIdentifier: parentIdentifier,
    helperBundleIdentifier: readPlistValue(
      helperPlist,
      'CFBundleIdentifier'
    ),
    bundleName: readPlistValue(helperPlist, 'CFBundleName'),
    lsUiElement: readPlistValue(helperPlist, 'LSUIElement') === 'true',
    copiedExecutableBytes: lstatSync(helperExecutable).size,
    frameworkEntries: [...REQUIRED_FRAMEWORK_ENTRIES],
    childHelperStrategy: 'helper-local-generic-electron-child',
    resourcesLinkTarget: readlinkSync(resourcesLink)
  };
}

export default async function afterPack(context) {
  if (context.electronPlatformName !== 'darwin') {
    return;
  }
  const appPath = path.join(
    context.appOutDir,
    `${context.packager.appInfo.productFilename}.app`
  );
  const created = createRuntimeHelperBundle(appPath);
  console.log(
    `  • runtime helper bundle  identifier=${created.helperBundleIdentifier} path=${path.relative(context.appOutDir, created.bundlePath)}`
  );
}

const invokedPath = process.argv[1]
  ? path.resolve(process.argv[1])
  : undefined;
if (invokedPath === fileURLToPath(import.meta.url)) {
  const appPath = process.argv[2];
  if (!appPath) {
    console.error('usage: afterpack-runtime-helper.mjs <path-to-Chirality.app>');
    process.exit(2);
  }
  console.log(
    JSON.stringify(createRuntimeHelperBundle(path.resolve(appPath)), null, 2)
  );
}
