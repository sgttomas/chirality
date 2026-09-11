import { mkdtemp, rm, writeFile } from 'node:fs/promises';
import { createServer, type Server } from 'node:net';
import path from 'node:path';
import { afterEach, describe, expect, it, vi } from 'vitest';
import {
  decideDaemonActivate,
  observeRendererPortEvidence,
  probeLoopbackPort,
  type RendererPortEvidence
} from '../../../electron/daemon-activate-policy';
import { RENDERER_PORT_RECORD_FILENAME } from '../../../electron/renderer-server-port';

const cleanup: Array<() => Promise<void>> = [];
afterEach(async () => {
  for (const close of cleanup.splice(0).reverse()) await close().catch(() => undefined);
});

function listen(): Promise<{ server: Server; port: number }> {
  return new Promise((resolve, reject) => {
    const server = createServer();
    server.once('error', reject);
    server.listen(0, '127.0.0.1', () => {
      const address = server.address();
      if (!address || typeof address === 'string') { reject(new Error('no port')); return; }
      cleanup.push(() => new Promise<void>((done) => server.close(() => done())));
      resolve({ server, port: address.port });
    });
  });
}

async function userDataWithRecord(record: string): Promise<string> {
  const directory = await mkdtemp('/tmp/daemon-activate-');
  cleanup.push(() => rm(directory, { recursive: true, force: true }));
  await writeFile(path.join(directory, RENDERER_PORT_RECORD_FILENAME), record, { mode: 0o600 });
  return directory;
}

const recordFor = (port: number): string =>
  `${JSON.stringify({ schema: 'chirality.renderer-port/v1', host: '127.0.0.1', port })}\n`;

describe('decideDaemonActivate', () => {
  it('ignores the activation only on positive evidence that the saved renderer port is listening', () => {
    expect(decideDaemonActivate({ kind: 'listening', port: 41234 })).toEqual({
      action: 'ignore', reason: 'gui-running', port: 41234
    });
  });

  it.each<RendererPortEvidence>([
    { kind: 'absent' },
    { kind: 'unreadable', error: 'renderer port record permissions must be owner-only' },
    { kind: 'closed', port: 41234, error: 'ECONNREFUSED' },
    { kind: 'unknown', port: 41234 }
  ])('spawns and carries the evidence for %j', (evidence) => {
    expect(decideDaemonActivate(evidence)).toEqual({ action: 'spawn', evidence });
  });
});

describe('observeRendererPortEvidence', () => {
  it('reports a listening saved port through the real record reader and a real loopback probe', async () => {
    const { port } = await listen();
    const userDataDirectory = await userDataWithRecord(recordFor(port));
    await expect(observeRendererPortEvidence({ userDataDirectory })).resolves.toEqual({ kind: 'listening', port });
  });

  it('reports a closed saved port once the GUI that owned it is gone', async () => {
    const { server, port } = await listen();
    const userDataDirectory = await userDataWithRecord(recordFor(port));
    await new Promise<void>((done) => server.close(() => done()));
    await expect(observeRendererPortEvidence({ userDataDirectory })).resolves.toMatchObject({ kind: 'closed', port });
  });

  it('reports an absent record without probing anything', async () => {
    const userDataDirectory = await mkdtemp('/tmp/daemon-activate-');
    cleanup.push(() => rm(userDataDirectory, { recursive: true, force: true }));
    const probe = vi.fn();
    await expect(observeRendererPortEvidence({ userDataDirectory, probe })).resolves.toEqual({ kind: 'absent' });
    expect(probe).not.toHaveBeenCalled();
  });

  it('does not trust an invalid record and never probes its port', async () => {
    const userDataDirectory = await userDataWithRecord(recordFor(80));
    const probe = vi.fn();
    const evidence = await observeRendererPortEvidence({ userDataDirectory, probe });
    expect(evidence).toMatchObject({ kind: 'unreadable' });
    expect(probe).not.toHaveBeenCalled();
    expect(decideDaemonActivate(evidence).action).toBe('spawn');
  });

  it('treats a probe that does not settle as unknown, which spawns', async () => {
    const readRecord = vi.fn(async () => ({ schema: 'chirality.renderer-port/v1' as const, host: '127.0.0.1' as const, port: 41234 }));
    const probe = vi.fn(async () => ({ result: 'unknown' as const }));
    const evidence = await observeRendererPortEvidence({ userDataDirectory: '/nowhere', readRecord, probe });
    expect(evidence).toEqual({ kind: 'unknown', port: 41234 });
    expect(probe).toHaveBeenCalledWith(41234);
    expect(decideDaemonActivate(evidence).action).toBe('spawn');
  });
});

describe('probeLoopbackPort', () => {
  it('connects and closes without sending bytes, then reports refused once the port is closed', async () => {
    const { server, port } = await listen();
    const received: Buffer[] = [];
    server.on('connection', (socket) => socket.on('data', (chunk: Buffer) => received.push(chunk)));
    await expect(probeLoopbackPort(port)).resolves.toEqual({ result: 'listening' });
    expect(received).toHaveLength(0);
    await new Promise<void>((done) => server.close(() => done()));
    await expect(probeLoopbackPort(port)).resolves.toMatchObject({ result: 'closed', error: 'ECONNREFUSED' });
  });
});
