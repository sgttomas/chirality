import { readFile } from 'node:fs/promises';
import path from 'node:path';
import { describe, expect, it, vi } from 'vitest';

import { resolvePackagedDaemonInstructionRoot } from '../../../electron/daemon-instruction-root';

describe('electron/daemon-instruction-root', () => {
  it('uses the registered manifest root instead of packaged resources', async () => {
    const resolveProjectRoots = vi.fn().mockResolvedValue({
      workingRoot: '/registered/project',
      instructionRoot: '/registered/instructions'
    });

    await expect(
      resolvePackagedDaemonInstructionRoot({
        projectId: 'chirality-app-dev',
        packagedResourcesPath: '/Applications/Chirality.app/Contents/Resources',
        resolveProjectRoots
      })
    ).resolves.toEqual({
      instructionRoot: path.resolve('/registered/instructions'),
      source: 'registered-project-manifest'
    });
    expect(resolveProjectRoots).toHaveBeenCalledWith('chirality-app-dev');
  });

  it('falls back to packaged resources only when manifest resolution is unavailable', async () => {
    const error = Object.assign(new Error('registration unavailable'), {
      code: 'PROJECT_NOT_FOUND'
    });

    await expect(
      resolvePackagedDaemonInstructionRoot({
        projectId: 'chirality-app-dev',
        packagedResourcesPath: '/Applications/Chirality.app/Contents/Resources',
        resolveProjectRoots: vi.fn().mockRejectedValue(error)
      })
    ).resolves.toEqual({
      instructionRoot: path.resolve('/Applications/Chirality.app/Contents/Resources'),
      source: 'packaged-resources-fallback',
      reason: 'PROJECT_NOT_FOUND'
    });
  });

  it('does not disclose unclassified error text in a fallback reason', async () => {
    await expect(
      resolvePackagedDaemonInstructionRoot({
        projectId: 'chirality-app-dev',
        packagedResourcesPath: '/packaged/resources',
        resolveProjectRoots: vi
          .fn()
          .mockRejectedValue(new Error('secret-bearing implementation detail'))
      })
    ).resolves.toEqual({
      instructionRoot: path.resolve('/packaged/resources'),
      source: 'packaged-resources-fallback',
      reason: 'MANIFEST_RESOLUTION_UNAVAILABLE'
    });
  });

  it('wires packaged daemon startup through the registry resolver and structured fallback log', async () => {
    const mainSource = await readFile(path.resolve(process.cwd(), 'electron', 'main.ts'), 'utf8');
    const initializeDaemon = mainSource.slice(
      mainSource.indexOf('async function initializeDaemon()'),
      mainSource.indexOf('/**\n * Release everything this process owns')
    );

    expect(initializeDaemon).toContain('resolvePackagedDaemonInstructionRoot({');
    expect(initializeDaemon).toContain('resolveProjectRoots: (projectId) => projects.roots(projectId)');
    expect(initializeDaemon).toContain("desktopLogger.warn('runtime.daemon.instruction_root.fallback'");
    expect(initializeDaemon).not.toContain(
      'process.env.CHIRALITY_INSTRUCTION_ROOT = path.resolve(process.resourcesPath)'
    );
  });
});
