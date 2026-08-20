import { mkdir, mkdtemp, readFile, realpath, rm, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, describe, expect, it } from 'vitest';

import {
  allocateDarwinProofTempRoot,
  cleanupActiveProcesses,
  darwinUnixSocketPathMaxBytes,
  logTextOffset,
  main,
  runCommand,
  sameAppIdentity,
  sliceLogFromOffset,
  startProcess,
  validateExpectedAppIdentityMarker
} from '../../../scripts/run-packaged-daemon-instruction-root-proof.mjs';

const tempRoots: string[] = [];

async function tempRoot(): Promise<string> {
  const root = await mkdtemp(path.join(os.tmpdir(), 'chirality-daemon-proof-test-'));
  tempRoots.push(root);
  return root;
}

afterEach(async () => {
  await cleanupActiveProcesses({ termGraceMs: 50, forceGraceMs: 1_000 });
  await Promise.all(tempRoots.splice(0).map((root) => rm(root, { recursive: true, force: true })));
});

describe('packaged daemon instruction-root proof harness', () => {
  it('allocates the runtime tree beneath the bounded canonical macOS temp prefix', async () => {
    let requestedPrefix = '';
    const allocation = await allocateDarwinProofTempRoot({
      canonicalize: (async (candidate: string) => candidate) as typeof realpath,
      makeTemp: (async (prefix: string) => {
        requestedPrefix = prefix;
        return `${prefix}ABC123`;
      }) as typeof mkdtemp
    });

    expect(requestedPrefix).toBe('/private/tmp/ch-d100-');
    expect(allocation.tempRoot).toBe('/private/tmp/ch-d100-ABC123');
    expect(allocation.userData).toBe('/private/tmp/ch-d100-ABC123/u');
    expect(allocation.controlSocketPath).toBe(
      '/private/tmp/ch-d100-ABC123/u/runtime/control.sock'
    );
    expect(allocation.controlSocketPathBytes).toBe(
      Buffer.byteLength(allocation.controlSocketPath, 'utf8')
    );
    expect(allocation.controlSocketPathBytes).toBeLessThanOrEqual(
      darwinUnixSocketPathMaxBytes
    );
  });

  it('applies a deadline to commands and confirms terminal cleanup', async () => {
    const root = await tempRoot();
    await expect(
      runCommand({
        executable: process.execPath,
        args: ['-e', 'setInterval(() => undefined, 1000)'],
        cwd: root,
        env: process.env,
        deadlineMs: 50,
        label: 'deadline fixture'
      })
    ).rejects.toThrow('exceeded deadline');
    await expect(cleanupActiveProcesses()).resolves.toBeUndefined();
  });

  it('escalates cleanup from SIGTERM to SIGKILL and awaits exit', async () => {
    const root = await tempRoot();
    const running = startProcess({
      executable: process.execPath,
      args: [
        '-e',
        "process.on('SIGTERM', () => undefined); process.stdout.write('READY\\n'); setInterval(() => undefined, 1000)"
      ],
      cwd: root,
      env: process.env,
      deadlineMs: 10_000,
      label: 'SIGTERM-resistant fixture'
    });
    while (!running.stdout().includes('READY')) {
      await new Promise((resolve) => setTimeout(resolve, 10));
    }

    await expect(
      cleanupActiveProcesses({ termGraceMs: 50, forceGraceMs: 1_000 })
    ).resolves.toBeUndefined();
    await expect(running.exited).resolves.toMatchObject({ signal: 'SIGKILL' });
  });

  it('binds content identity to the exact canonical app path and bytes', () => {
    const identity = {
      schema: 'chirality-packaged-app-identity/v1',
      appPath: '/exact/Chirality.app',
      files: [{ relativePath: 'Contents/Resources/app.asar', bytes: 10, sha256: 'abc' }],
      sha256: 'identity-a'
    };
    expect(sameAppIdentity(identity, structuredClone(identity))).toBe(true);
    expect(sameAppIdentity(identity, { ...identity, appPath: '/stale/Chirality.app' })).toBe(false);
    expect(sameAppIdentity(identity, { ...identity, sha256: 'identity-b' })).toBe(false);

    const now = Date.parse('2026-08-19T12:00:00.000Z');
    const freshMarker = {
      kind: 'current-invocation',
      invocationId: 'current-pack',
      capturedAt: new Date(now - 1_000).toISOString(),
      identity
    };
    expect(validateExpectedAppIdentityMarker(freshMarker, now)).toEqual(identity);
    expect(() =>
      validateExpectedAppIdentityMarker(
        { ...freshMarker, capturedAt: new Date(now - 11 * 60 * 1_000).toISOString() },
        now
      )
    ).toThrow('stale');
  });

  it('invalidates a stale PASS and atomically records FAIL for an invalid skip-pack run', async () => {
    const root = await tempRoot();
    const outputRoot = path.join(root, 'evidence');
    await mkdir(outputRoot, { recursive: true });
    const summaryPath = path.join(outputRoot, 'summary.json');
    await writeFile(summaryPath, '{"status":"PASS","invocationId":"stale"}\n', 'utf8');

    await expect(main(['--skip-pack', '--output-root', outputRoot])).rejects.toThrow(
      '--skip-pack requires --expected-app-identity'
    );
    const summary = JSON.parse(await readFile(summaryPath, 'utf8'));
    expect(summary.status).toBe('FAIL');
    expect(summary.invocationId).not.toBe('stale');
    expect(summary.error).toContain('--skip-pack requires --expected-app-identity');
  });

  it('uses JavaScript string offsets for logs containing non-ASCII text', () => {
    const prefix = 'préflight 🙂\n';
    const appended = '2026-08-19 [info] runtime.daemon.instruction_root.resolved {}\n';
    const offset = logTextOffset(prefix);

    expect(Buffer.byteLength(prefix, 'utf8')).toBeGreaterThan(offset);
    expect(sliceLogFromOffset(prefix + appended, offset)).toBe(appended);
  });
});
