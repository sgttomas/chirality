import { EventEmitter } from 'node:events';
import { describe, expect, it } from 'vitest';

import {
  buildElectronBuilderArgs,
  runElectronPack
} from '../../../scripts/pack-electron-with-supply.mjs';

describe('pack-electron-with-supply', () => {
  it('passes exactly one spaces-safe electronDist argument without a shell', async () => {
    const directory = '/Users/example/Library/Caches/chirality/electron dist';
    const calls: Array<{ command: string; args: string[]; options: Record<string, unknown> }> = [];
    const spawnProcess = (
      command: string,
      args: string[],
      options: Record<string, unknown>
    ) => {
      calls.push({ command, args, options });
      const child = new EventEmitter();
      queueMicrotask(() => child.emit('exit', 0, null));
      return child;
    };

    await runElectronPack({
      verify: async () => directory,
      spawnProcess: spawnProcess as never,
      env: { NODE_ENV: 'test', PATH: '/usr/bin' }
    });

    expect(calls).toHaveLength(1);
    expect(calls[0]?.command).toBe('electron-builder');
    expect(calls[0]?.args).toEqual(buildElectronBuilderArgs(directory));
    expect(calls[0]?.args.filter((arg) => arg.startsWith('-c.electronDist='))).toEqual([
      `-c.electronDist=${directory}`
    ]);
    expect(calls[0]?.options.shell).toBe(false);
    expect(calls[0]?.options.env).toMatchObject({ CSC_IDENTITY_AUTO_DISCOVERY: 'false' });
  });
});
