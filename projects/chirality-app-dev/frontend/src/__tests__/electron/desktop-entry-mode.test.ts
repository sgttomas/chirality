import { describe, expect, it } from 'vitest';

import { resolveDesktopEntryMode } from '../../../electron/desktop-entry-mode';

describe('Electron fixed entry modes', () => {
  it('selects packaged GUI, daemon, and protected CLI only at argv index one', () => {
    expect(resolveDesktopEntryMode(['/app/Chirality'], true)).toEqual({ mode: 'gui' });
    expect(resolveDesktopEntryMode(['/app/Chirality', '--runtime-daemon'], true)).toEqual({
      mode: 'runtime-daemon'
    });
    expect(
      resolveDesktopEntryMode(['/app/Chirality', '--runtime-cli', 'project', 'list'], true)
    ).toEqual({ mode: 'runtime-cli', arguments: ['project', 'list'] });
  });

  it('accounts for the development app entry at argv index one', () => {
    expect(
      resolveDesktopEntryMode(['/electron', '/source/dist-electron/main.js', '--runtime-cli', '--help'], false)
    ).toEqual({ mode: 'runtime-cli', arguments: ['--help'] });
  });

  it('rejects conflicting, repeated, displaced, and argument-bearing daemon modes', () => {
    for (const argv of [
      ['/app/Chirality', '--runtime-cli', '--runtime-daemon'],
      ['/app/Chirality', '--runtime-cli', '--runtime-cli'],
      ['/app/Chirality', 'caller.js', '--runtime-cli'],
      ['/app/Chirality', '--runtime-daemon', 'extra']
    ]) {
      expect(resolveDesktopEntryMode(argv, true).mode).toBe('invalid');
    }
  });
});
