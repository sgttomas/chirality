import { chmod, mkdir, mkdtemp, realpath, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import type { ProjectStatus } from '@chirality/runtime-contracts';

import {
  applyDesktopProjectBinding,
  DESKTOP_PROJECT_ID,
  prepareDesktopHarnessEnvironment,
  resolveDesktopProjectBinding
} from '../../../electron/desktop-project-client';

let fixtureRoot: string;
let runtimeDirectory: string;
let projectRoot: string;
let manifestPath: string;
let tokenFile: string;

function status(overrides: Partial<ProjectStatus> = {}): ProjectStatus {
  return {
    project: {
      projectId: DESKTOP_PROJECT_ID,
      displayName: 'Chirality App Development',
      canonicalRoot: projectRoot,
      manifestPath,
      manifestHash: 'manifest-hash',
      registeredAt: '2026-07-22T00:00:00.000Z',
      approval: {
        approvedBy: 'owner',
        approvalReference: 'D-APP-73'
      },
      clientId: 'project-fixture',
      enabledAdapterIds: ['claude-agent-sdk', 'pi'],
      legacySessionRoots: []
    },
    manifestDrift: false,
    adaptersEnabled: true,
    ...overrides
  };
}

beforeEach(async () => {
  fixtureRoot = await realpath(
    await mkdtemp(path.join(os.tmpdir(), 'chirality-desktop-project-'))
  );
  runtimeDirectory = path.join(fixtureRoot, 'runtime');
  projectRoot = path.join(fixtureRoot, 'app-dev');
  manifestPath = path.join(projectRoot, 'chirality.project.json');
  tokenFile = path.join(
    runtimeDirectory,
    'auth',
    'tokens',
    'project-fixture.token'
  );
  await mkdir(projectRoot, { recursive: true });
  await mkdir(path.dirname(tokenFile), { recursive: true });
  await writeFile(manifestPath, '{}', 'utf8');
  await writeFile(tokenFile, 'project-token\n', { encoding: 'utf8', mode: 0o600 });
  await chmod(tokenFile, 0o600);
});

afterEach(async () => {
  await import('node:fs/promises').then(({ rm }) =>
    rm(fixtureRoot, { recursive: true, force: true })
  );
});

describe('electron/desktop-project-client', () => {
  it('clears operator authority and passes only the fixed project binding to Next', () => {
    const environment = {
      CHIRALITY_RUNTIME_TOKEN_FILE: '/runtime/auth/tokens/operator.token',
      CHIRALITY_RUNTIME_PROJECT_ROOT: '/stale/root'
    };

    prepareDesktopHarnessEnvironment(environment, '/runtime/control.sock');
    expect(environment).toEqual({
      CHIRALITY_RUNTIME_SOCKET_PATH: '/runtime/control.sock',
      CHIRALITY_RUNTIME_PROJECT_ID: DESKTOP_PROJECT_ID
    });

    applyDesktopProjectBinding(environment, {
      projectId: DESKTOP_PROJECT_ID,
      projectRoot: '/repo/projects/chirality-app-dev',
      tokenFile: '/runtime/auth/tokens/project-fixture.token'
    });
    expect(environment).toEqual({
      CHIRALITY_RUNTIME_SOCKET_PATH: '/runtime/control.sock',
      CHIRALITY_RUNTIME_PROJECT_ID: DESKTOP_PROJECT_ID,
      CHIRALITY_RUNTIME_PROJECT_ROOT: '/repo/projects/chirality-app-dev',
      CHIRALITY_RUNTIME_TOKEN_FILE: '/runtime/auth/tokens/project-fixture.token'
    });
    expect(environment.CHIRALITY_RUNTIME_TOKEN_FILE).not.toContain('operator.token');
  });

  it('resolves and verifies only the registered app-dev project token', async () => {
    const projectStatus = vi.fn().mockResolvedValue(status());
    const scopedProjectStatus = vi.fn().mockResolvedValue(status());
    const createScopedClient = vi.fn(() => ({
      projectStatus: scopedProjectStatus
    }));

    await expect(
      resolveDesktopProjectBinding({
        operatorClient: { projectStatus },
        runtimeDirectory,
        socketPath: '/runtime/control.sock',
        createScopedClient
      })
    ).resolves.toEqual({
      projectId: DESKTOP_PROJECT_ID,
      projectRoot,
      tokenFile
    });
    expect(projectStatus).toHaveBeenCalledWith(DESKTOP_PROJECT_ID);
    expect(createScopedClient).toHaveBeenCalledWith({
      socketPath: '/runtime/control.sock',
      tokenFile
    });
    expect(tokenFile).not.toContain('operator.token');
  });

  it('fails closed on manifest drift before binding a renderer client', async () => {
    await expect(
      resolveDesktopProjectBinding({
        operatorClient: {
          projectStatus: vi.fn().mockResolvedValue(
            status({ manifestDrift: true, adaptersEnabled: false })
          )
        },
        runtimeDirectory,
        socketPath: '/runtime/control.sock',
        createScopedClient: vi.fn()
      })
    ).rejects.toThrow('unregistered, disabled, or has manifest drift');
  });

  it('rejects a malformed registry client ID instead of deriving an arbitrary path', async () => {
    const malformed = status();
    malformed.project.clientId = '../../operator';

    await expect(
      resolveDesktopProjectBinding({
        operatorClient: {
          projectStatus: vi.fn().mockResolvedValue(malformed)
        },
        runtimeDirectory,
        socketPath: '/runtime/control.sock'
      })
    ).rejects.toThrow('client identifier is malformed');
  });

  it('rejects a token file with group or world permissions', async () => {
    await chmod(tokenFile, 0o644);

    await expect(
      resolveDesktopProjectBinding({
        operatorClient: {
          projectStatus: vi.fn().mockResolvedValue(status())
        },
        runtimeDirectory,
        socketPath: '/runtime/control.sock'
      })
    ).rejects.toThrow('not private and user-owned');
  });

  it('verifies the scoped token resolves back to the same registration', async () => {
    const scoped = status();
    scoped.project.manifestHash = 'other-hash';

    await expect(
      resolveDesktopProjectBinding({
        operatorClient: {
          projectStatus: vi.fn().mockResolvedValue(status())
        },
        runtimeDirectory,
        socketPath: '/runtime/control.sock',
        createScopedClient: () => ({
          projectStatus: vi.fn().mockResolvedValue(scoped)
        })
      })
    ).rejects.toThrow('different registration');
  });
});
