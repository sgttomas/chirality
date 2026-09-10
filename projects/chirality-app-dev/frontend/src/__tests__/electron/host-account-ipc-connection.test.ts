import { createServer } from 'node:http';
import { mkdtemp, realpath, rm } from 'node:fs/promises';
import path from 'node:path';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { createHostAccountClient } from '@chirality/runtime-daemon';
import { performHostAccountOperation } from '../../../electron/host-account-ipc';

let temporaryRoot: string | undefined;
afterEach(async () => {
  if (temporaryRoot) await rm(temporaryRoot, { recursive: true, force: true });
  temporaryRoot = undefined;
});

describe('host account IPC to real Runtime client operation mapping', () => {
  it('maps a registered root through the real signed-request client on one transport', async () => {
    temporaryRoot = await realpath(await mkdtemp('/tmp/account-connect-'));
    const socketPath = path.join(temporaryRoot, 'control.sock');
    const observed = vi.fn();
    const server = createServer((request, response) => {
      const chunks: Buffer[] = [];
      request.on('data', (chunk: Buffer) => chunks.push(chunk));
      request.on('end', () => {
        observed({
          method: request.method,
          path: request.url,
          body: Buffer.concat(chunks).toString('utf8'),
          hasBearer: request.headers.authorization?.startsWith('Bearer ') === true,
          hasProof: typeof request.headers['x-chirality-account-proof'] === 'string'
        });
        response.writeHead(200, { 'content-type': 'application/json' });
        response.end(JSON.stringify({
          schema: 'chirality-hosted-bootstrap-status/v1',
          projectId: 'registered-project',
          ceremony: 'ready-to-start',
          admission: 'unavailable',
          canStartLogin: true
        }));
      });
    });
    await new Promise<void>((resolve, reject) => {
      server.once('error', reject);
      server.listen(socketPath, resolve);
    });

    const client = createHostAccountClient({
      socketPath,
      signingPredicate: {
        schema: 'chirality.host-account-signing-predicate/v1',
        serviceName: 'com.chirality.app.runtime.account-host',
        bundleId: 'com.chirality.app',
        teamId: '8A7JL35U4S',
        peerRequirement: 'identifier "com.chirality.app" and anchor apple generic'
      },
      expectedEuid: 501,
      nativeAdmission: {
        createHostXpcClient: () => ({
          async provision({ requestId, onChallenge }) {
            await onChallenge({
              requestId,
              challenge: Buffer.alloc(32, 1),
              generation: '00000000-0000-4000-8000-000000000001'
            });
            return {
              requestId,
              bearer: Buffer.alloc(32, 2),
              generation: '00000000-0000-4000-8000-000000000001',
              scopes: ['account:read', 'account:control']
            };
          },
          close: vi.fn(async () => undefined)
        })
      }
    });
    await client.start();
    const project = {
      projectId: 'registered-project',
      displayName: 'Registered project',
      canonicalRoot: temporaryRoot,
      manifestPath: path.join(temporaryRoot, '.chirality', 'project.json'),
      manifestHash: 'a'.repeat(64),
      registeredAt: '2026-09-10T00:00:00.000Z',
      approval: { approvedBy: 'owner', approvalReference: 'decision' },
      clientId: 'client',
      enabledAdapterIds: ['codex-app-server'],
      legacySessionRoots: []
    };
    const runtimeClient = {
      listProjects: vi.fn(async () => [{ project, manifestDrift: false, adaptersEnabled: true }]),
      projectStatus: vi.fn(async () => ({ project, manifestDrift: false, adaptersEnabled: true }))
    };
    try {
      await expect(performHostAccountOperation(
        { operation: 'grant-provider-network-consent', projectRoot: temporaryRoot },
        { runtimeClient, accountClient: () => client }
      )).resolves.toMatchObject({
        ok: true,
        value: { registration: 'registered', projectId: project.projectId }
      });
      expect(observed).toHaveBeenCalledWith({
        method: 'POST',
        path: '/v3/projects/registered-project/hosted-bootstrap/provider-network-consent',
        body: '{"consent":true}',
        hasBearer: true,
        hasProof: true
      });
    } finally {
      await client.close();
      await new Promise<void>((resolve, reject) => server.close((error) => error ? reject(error) : resolve()));
    }
  });
});
