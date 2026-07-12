import { copyFile, mkdir, mkdtemp, rm, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { afterEach, describe, expect, it } from 'vitest';

let fixtureRoot = '';

afterEach(async () => {
  if (fixtureRoot) await rm(fixtureRoot, { recursive: true, force: true });
  fixtureRoot = '';
});

async function makeFixture(): Promise<string> {
  fixtureRoot = await mkdtemp(path.join(os.tmpdir(), 'chirality-premerge-'));
  await mkdir(path.join(fixtureRoot, 'scripts'), { recursive: true });
  await copyFile(
    path.resolve(process.cwd(), 'scripts', 'validate-harness-premerge.mjs'),
    path.join(fixtureRoot, 'scripts', 'validate-harness-premerge.mjs')
  );
  return fixtureRoot;
}

async function runWrapper(cwd: string): Promise<{ code: number; output: string }> {
  return new Promise((resolve, reject) => {
    const child = spawn(process.execPath, ['scripts/validate-harness-premerge.mjs'], {
      cwd,
      stdio: ['ignore', 'pipe', 'pipe']
    });
    let output = '';
    child.stdout.on('data', (chunk) => { output += chunk.toString(); });
    child.stderr.on('data', (chunk) => { output += chunk.toString(); });
    child.on('error', reject);
    child.on('close', (code) => resolve({ code: code ?? 1, output }));
  });
}

describe('validate-harness-premerge wrapper failures', () => {
  it('fails closed with RUNTIME_SURFACE_MISSING when the Section 8 script is absent', async () => {
    const cwd = await makeFixture();
    const result = await runWrapper(cwd);

    expect(result.code).not.toBe(0);
    expect(result.output).toContain(
      'RUNTIME_SURFACE_MISSING: frontend/scripts/validate-harness-section8.mjs'
    );
    expect(result.output).toContain('HARNESS_PREMERGE_STATUS=fail');
  });

  it('rejects a Section 8 summary containing the removed regression key', async () => {
    const cwd = await makeFixture();
    const summaryPath = path.join(cwd, 'section8-summary.json');
    const requiredIds = [
      'setup.server_reachable',
      'regression.session_crud',
      'section8.boot_error_taxonomy',
      'section8.smoke_stream',
      'section8.session_persistence_resume',
      'section8.permissions_dontask',
      'section8.interrupt_sigint',
      'section8.sdk_native_stream',
      'regression.api_chat_reachability'
    ];
    await writeFile(
      summaryPath,
      JSON.stringify({ results: requiredIds.map((id) => ({ id, status: 'pass' })) })
    );
    await writeFile(
      path.join(cwd, 'scripts', 'validate-harness-section8.mjs'),
      `console.log('HARNESS_VALIDATION_SUMMARY_PATH=${summaryPath}');\nconsole.log('HARNESS_VALIDATION_STATUS=pass');\n`
    );

    const result = await runWrapper(cwd);
    expect(result.code).not.toBe(0);
    expect(result.output).toContain(
      "Summary includes legacy test id 'regression.api_chat_reachability'"
    );
  });
});
