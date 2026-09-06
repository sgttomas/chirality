import { beforeEach, expect, it, vi } from 'vitest';
const control = vi.hoisted(() => ({ failure: 'fd-mode' }));
vi.mock('node:fs/promises', async () => {
  const actual = await vi.importActual<typeof import('node:fs/promises')>('node:fs/promises');
  return { ...actual,
    open: async (...args: Parameters<typeof actual.open>) => {
      const handle = await actual.open(...args);
      if (args[0] !== '/private/etc/ssl/openssl.cnf') return handle;
      return { stat: async () => {
        const info = await handle.stat();
        if (control.failure === 'fd-mode') info.mode |= 0o022;
        if (control.failure === 'fd-owner') info.uid = 501;
        return info;
      }, read: handle.read.bind(handle), close: handle.close.bind(handle) };
    },
    lstat: async (...args: Parameters<typeof actual.lstat>) => {
      const info = await actual.lstat(...args);
      if (args[0] === '/private/etc/ssl/openssl.cnf' && control.failure === 'path-replaced') Object.assign(info, { ino: Number(info.ino) + 1 });
      return info;
    }
  };
});
import { mkdir, mkdtemp, realpath, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { prepareCodexNativePolicy } from '../packages/daemon/src/codex-containment.js';
beforeEach(() => { control.failure = 'fd-mode'; });
it.skipIf(process.platform !== 'darwin').each(['fd-mode', 'fd-owner', 'path-replaced'])('rejects observed immutable identity drift: %s', async failure => {
  control.failure = failure;
  const base = await mkdtemp(join(await realpath(tmpdir()), 'immutable-identity-'));
  const root = join(base, 'project'), broker = join(base, 'broker'), worker = join(broker, 'worker'), home = join(worker, 'codex');
  await mkdir(root); await mkdir(broker, { mode: 0o700 }); await mkdir(worker, { mode: 0o700 }); await mkdir(home, { mode: 0o700 });
  try {
    await expect(prepareCodexNativePolicy({ canonicalRoot: root, privateDirectory: worker, codexHome: home,
      immutableReadRoots: ['/private/etc/ssl/openssl.cnf'], protectedPaths: [broker] })).rejects.toThrow('Immutable file changed');
  } finally { await rm(base, { recursive: true, force: true }); }
});

it.runIf(process.platform !== 'darwin')('rejects native policy on unsupported platforms before macOS file access', async () => {
  await expect(prepareCodexNativePolicy({ canonicalRoot: '/unsupported-platform/project',
    privateDirectory: '/unsupported-platform/worker', codexHome: '/unsupported-platform/worker/codex',
    immutableReadRoots: ['/private/etc/ssl/openssl.cnf'], protectedPaths: ['/unsupported-platform/broker']
  })).rejects.toThrow('Native policy requires macOS Seatbelt verification');
});
