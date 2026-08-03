import { describe, expect, it } from 'vitest';
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import {
  DESKTOP_GUI_BUNDLE_IDENTIFIER,
  isRuntimeHelperExecutable,
  resolveRuntimeHelperExecutable,
  RUNTIME_HELPER_BUNDLE_DIRECTORY_NAME,
  RUNTIME_HELPER_BUNDLE_IDENTIFIER,
  RUNTIME_HELPER_EXECUTABLE_NAME
} from '../../../electron/runtime-helper-bundle';

const GUI_EXECUTABLE = '/Applications/Chirality.app/Contents/MacOS/Chirality';
const HELPER_EXECUTABLE =
  '/Applications/Chirality.app/Contents/Library/LoginItems/Chirality Runtime Helper.app/Contents/MacOS/Chirality';

describe('electron/runtime-helper-bundle', () => {
  it('resolves the nested helper without collapsing onto the GUI executable', () => {
    expect(resolveRuntimeHelperExecutable(GUI_EXECUTABLE)).toBe(
      HELPER_EXECUTABLE
    );
    expect(resolveRuntimeHelperExecutable(GUI_EXECUTABLE)).not.toBe(
      GUI_EXECUTABLE
    );
  });

  it('recognizes only the helper-local executable posture', () => {
    expect(isRuntimeHelperExecutable(HELPER_EXECUTABLE)).toBe(true);
    expect(isRuntimeHelperExecutable(GUI_EXECUTABLE)).toBe(false);
    expect(
      isRuntimeHelperExecutable(
        '/tmp/Chirality Runtime Helper.app/Contents/MacOS/not-the-helper'
      )
    ).toBe(false);
  });

  it('keeps runtime constants synchronized with the afterPack hook', async () => {
    const hook = await readFile(
      path.resolve(process.cwd(), 'scripts', 'afterpack-runtime-helper.mjs'),
      'utf8'
    );

    for (const value of [
      DESKTOP_GUI_BUNDLE_IDENTIFIER,
      RUNTIME_HELPER_BUNDLE_IDENTIFIER,
      RUNTIME_HELPER_BUNDLE_DIRECTORY_NAME,
      RUNTIME_HELPER_EXECUTABLE_NAME
    ]) {
      expect(hook).toContain(`'${value}'`);
    }
    expect(hook).toContain("'Chirality Helper.app'");
  });
});
