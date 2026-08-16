import { describe, expect, it } from 'vitest';
import { verifyPackagedRuntimeSources } from '../../../scripts/verify-packaged-dependency-boundary.mjs';

const desktopSources = [
  '../electron/main.ts',
  '../electron/runtime-host.ts',
  '../../../../runtime/packages/client/src/client.ts',
  '../../../../runtime/packages/daemon/src/runtime-daemon.ts',
  '../../../../runtime/packages/engine-claude/src/index.ts',
  '../../../../runtime/packages/engine-pi-omlx/src/pi-omlx-engine.ts'
];
const cliSources = [
  '../../../../runtime/packages/cli/src/bin.ts',
  '../../../../runtime/packages/cli/src/cli.ts',
  '../../../../runtime/packages/client/src/client.ts'
];
const packagedEntries = new Set(['/dist-electron/main.js', '/dist-electron/main.js.map']);

describe('packaged Root runtime source proof', () => {
  it('accepts Root adapters in the desktop daemon and a client-only CLI', () => {
    expect(
      verifyPackagedRuntimeSources({ desktopSources, cliSources, packagedEntries }).failures
    ).toEqual([]);
  });

  it('rejects a missing promoted adapter or server code embedded in the CLI client', () => {
    const result = verifyPackagedRuntimeSources({
      desktopSources: desktopSources.filter((source) => !source.includes('engine-claude')),
      cliSources: [...cliSources, '../../../../runtime/packages/daemon/src/runtime-daemon.ts'],
      packagedEntries
    });

    expect(result.failures).toEqual(
      expect.arrayContaining([
        expect.stringContaining('desktop bundle is missing source runtime/packages/engine-claude'),
        expect.stringContaining('CLI client bundle unexpectedly embeds server source')
      ])
    );
  });
});
