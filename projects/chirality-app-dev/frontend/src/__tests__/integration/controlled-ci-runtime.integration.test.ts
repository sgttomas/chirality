import { execFile, spawn, type ChildProcess } from 'node:child_process';
import { mkdir, mkdtemp, readFile, rm, stat, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { promisify } from 'node:util';
import { afterEach, describe, expect, it } from 'vitest';
import { RuntimeClient } from '@chirality/runtime-client';
import type { UIEvent } from '@chirality/runtime-contracts';
import { CONTROLLED_CI_PURPOSE } from '../../../scripts/controlled-ci-runtime';

const execFileAsync = promisify(execFile);
const roots: string[] = [];
const stops: Array<() => Promise<void>> = [];

async function waitForFile(filePath: string): Promise<void> {
  for (let attempt = 0; attempt < 100; attempt += 1) {
    if (await stat(filePath).then(() => true, () => false)) return;
    await new Promise((resolve) => setTimeout(resolve, 20));
  }
  throw new Error(`Timed out waiting for ${filePath}`);
}

async function stopChild(child: ChildProcess): Promise<void> {
  if (child.exitCode !== null) return;
  child.kill('SIGTERM');
  await new Promise<void>((resolve) => child.once('exit', () => resolve()));
}

afterEach(async () => {
  await Promise.all(stops.splice(0).map((stop) => stop().catch(() => undefined)));
  await Promise.all(roots.splice(0).map((root) => rm(root, { recursive: true, force: true })));
});

async function drain(source: Awaited<ReturnType<RuntimeClient['turnSession']>>): Promise<UIEvent[]> {
  const events: UIEvent[] = [];
  for await (const event of source) events.push(event);
  return events;
}

describe('controlled CI runtime', () => {
  it('builds an isolated graph and serves registered project turns over the real daemon socket', async () => {
    const frontendRoot = path.resolve(process.cwd());
    const repositoryRoot = path.resolve(frontendRoot, '..', '..', '..');
    await execFileAsync(process.execPath, [path.join(frontendRoot, 'scripts', 'build-controlled-ci-runtime.mjs')], {
      cwd: frontendRoot
    });

    const metadata = JSON.parse(await readFile(path.join(frontendRoot, 'out', 'controlled-ci', 'controlled-runtime.meta.json'), 'utf8')) as {
      inputs: Record<string, unknown>;
    };
    const sources = Object.keys(metadata.inputs).join('\n');
    expect(sources).toContain('scripts/controlled-ci-runtime.ts');
    expect(sources).toContain('packages/daemon/src/runtime-daemon.ts');
    expect(sources).not.toMatch(/electron\/main\.ts|runtime-host|engine-pi-omlx|engine-claude|hosted-private-|native-admission|codex-/u);

    const pkg = JSON.parse(await readFile(path.join(frontendRoot, 'package.json'), 'utf8')) as {
      build: { files: string[]; extraResources: Array<{ from: string }> };
    };
    expect(pkg.build.files.some((item) => !item.startsWith('!') && (item === '**/*' || item.startsWith('out/')))).toBe(false);
    expect(pkg.build.extraResources.some((item) => item.from.includes('out/controlled-ci'))).toBe(false);

    const root = await mkdtemp(path.join(os.tmpdir(), 'chirality-controlled-ci-'));
    roots.push(root);
    const runtimeDirectory = path.join(root, 'runtime');
    const socketPath = path.join(runtimeDirectory, 'control.sock');
    const projectRoot = path.join(root, 'project');
    await mkdir(projectRoot, { recursive: true });
    await writeFile(path.join(projectRoot, 'AGENTS.md'), '# Controlled CI fixture\n');
    const projectId = 'controlled-ci-fixture';
    const manifestPath = path.join(projectRoot, 'chirality.project.json');
    await writeFile(manifestPath, `${JSON.stringify({
      schemaVersion: 'chirality.project/v2',
      projectId,
      displayName: 'Controlled CI fixture',
      workingRoot: '.',
      instructionRoot: { mode: 'runtime' },
      defaultExecutionRoot: '.',
      profiles: { domain: [], capability: [], dataBoundary: [] },
      enabledAdapterIds: ['stub'],
      embeddedUi: { declared: false }
    })}\n`);

    const controlledEntry = path.join(frontendRoot, 'out', 'controlled-ci', 'controlled-runtime.mjs');
    const rejected = await execFileAsync(process.execPath, [controlledEntry], {
      cwd: frontendRoot,
      env: {
        ...process.env,
        CHIRALITY_CONTROLLED_CI_RUNTIME: 'ordinary-runtime',
        CHIRALITY_RUNTIME_DIRECTORY: runtimeDirectory,
        CHIRALITY_RUNTIME_SOCKET_PATH: socketPath,
        CHIRALITY_INSTRUCTION_ROOT: repositoryRoot
      }
    }).then(() => undefined, (error: unknown) => error);
    expect(String(rejected)).toContain(`CHIRALITY_CONTROLLED_CI_RUNTIME must equal ${CONTROLLED_CI_PURPOSE}`);

    const child = spawn(process.execPath, [controlledEntry], {
      cwd: frontendRoot,
      env: {
        ...process.env,
        CHIRALITY_CONTROLLED_CI_RUNTIME: CONTROLLED_CI_PURPOSE,
        CHIRALITY_RUNTIME_DIRECTORY: runtimeDirectory,
        CHIRALITY_RUNTIME_SOCKET_PATH: socketPath,
        CHIRALITY_INSTRUCTION_ROOT: repositoryRoot,
        CHIRALITY_STUB_CHUNK_DELAY_MS: '0'
      },
      stdio: ['ignore', 'pipe', 'pipe']
    });
    stops.push(() => stopChild(child));
    const operatorTokenFile = path.join(runtimeDirectory, 'auth', 'tokens', 'operator.token');
    await waitForFile(operatorTokenFile);
    const registrationResult = await execFileAsync(process.execPath, [
      path.join(frontendRoot, 'out', 'controlled-ci', 'chirality-cli.mjs'),
      'project', 'register', '--manifest', manifestPath,
      '--approved-by', 'controlled-ci-test', '--approval-reference', CONTROLLED_CI_PURPOSE, '--json'
    ], {
      cwd: repositoryRoot,
      env: {
        ...process.env,
        CHIRALITY_RUNTIME_SOCKET_PATH: socketPath,
        CHIRALITY_RUNTIME_TOKEN_FILE: operatorTokenFile
      }
    });
    const registration = JSON.parse(registrationResult.stdout) as { tokenFile: string };
    const project = new RuntimeClient({ socketPath, tokenFile: registration.tokenFile });
    expect((await project.listProjects()).map((item) => item.project.projectId)).toContain(projectId);
    const session = await project.createSession(projectId, { projectId });
    const events = await drain(await project.turnSession(projectId, session.sessionId, {
      message: 'CONTROLLED_CI_SOCKET_TURN'
    }));
    expect(events).toContainEqual(expect.objectContaining({
      type: 'session:init',
      data: expect.objectContaining({ adapterId: 'stub', providerId: 'stub', model: 'controlled-ci' })
    }));
    expect(events).toContainEqual({ type: 'chat:complete', data: { text: 'CONTROLLED_CI_SOCKET_TURN' } });
    expect(events.at(-1)).toEqual({ type: 'process:exit', data: { exitCode: 0 } });
  }, 30_000);
});
