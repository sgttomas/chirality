import path from 'node:path';
import { describe, expect, it, vi } from 'vitest';

const runtimeDaemonConstructor = vi.hoisted(() => vi.fn());

vi.mock('electron', () => ({
  app: {
    getPath: vi.fn(() => `/tmp/${'x'.repeat(120)}`),
    isPackaged: false
  },
  safeStorage: {
    isEncryptionAvailable: vi.fn(() => false)
  }
}));

vi.mock('@chirality/runtime-daemon', () => ({
  RuntimeDaemon: class {
    constructor(input: unknown) {
      runtimeDaemonConstructor(input);
    }
  }
}));

import {
  MACOS_UNIX_SOCKET_PATH_MAX_BYTES,
  assertRuntimeSocketPathSupported,
  startRuntimeHost
} from '../../../electron/runtime-host';

function pathWithBytes(targetBytes: number, unicode = false): string {
  const prefix = '/tmp/';
  const remaining = targetBytes - Buffer.byteLength(prefix, 'utf8');
  const tail = unicode ? `${'a'.repeat(remaining - 2)}é` : 'a'.repeat(remaining);
  const value = `${prefix}${tail}`;
  expect(Buffer.byteLength(value, 'utf8')).toBe(targetBytes);
  return value;
}

describe('runtime-host macOS socket-path boundary', () => {
  it('accepts 103 bytes, rejects 104 bytes, and counts UTF-8 bytes', () => {
    expect(
      assertRuntimeSocketPathSupported(
        pathWithBytes(MACOS_UNIX_SOCKET_PATH_MAX_BYTES),
        'darwin'
      )
    ).toEqual({ measuredBytes: 103, maximumBytes: 103 });
    for (const socketPath of [pathWithBytes(104), pathWithBytes(104, true)]) {
      expect(() => assertRuntimeSocketPathSupported(socketPath, 'darwin')).toThrow(
        'Runtime control socket path is 104 UTF-8 bytes; macOS maximum is 103 bytes'
      );
    }
    expect(() => assertRuntimeSocketPathSupported(pathWithBytes(104), 'linux')).not.toThrow();
  });

  it('rejects before RuntimeDaemon construction or listen can be attempted', async () => {
    const expectedSocketPath = path.join(`/tmp/${'x'.repeat(120)}`, 'runtime', 'control.sock');
    const measuredBytes = Buffer.byteLength(expectedSocketPath, 'utf8');
    const platform = vi.spyOn(process, 'platform', 'get').mockReturnValue('darwin');

    try {
      await expect(startRuntimeHost()).rejects.toThrow(
        `Runtime control socket path is ${measuredBytes} UTF-8 bytes; macOS maximum is 103 bytes`
      );
      expect(runtimeDaemonConstructor).not.toHaveBeenCalled();
    } finally {
      platform.mockRestore();
    }
  });
});
