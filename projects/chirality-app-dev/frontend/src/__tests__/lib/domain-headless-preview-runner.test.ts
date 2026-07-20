import { createHash } from 'node:crypto';
import { chmod, mkdir, mkdtemp, readFile, rm, symlink, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import {
  HEADLESS_RUNNER_STDERR_LIMIT_BYTES,
  HEADLESS_RUNNER_STDOUT_LIMIT_BYTES,
  OPEN_PIPE_STRESS_RUNNER_PATH_ENV,
  OPEN_PIPE_STRESS_RUNNER_SHA256_ENV,
  type HeadlessRunnerEnvironment,
  runConfiguredHeadlessPreview
} from '../../lib/harness/mcp/domain-headless-preview-runner';
import {
  buildChiralityMcpTools,
  domainHeadlessPreviewRunTool
} from '../../lib/harness/mcp/read-tools';
import { replayHarnessEvents } from '../../lib/harness/session-events';

const REQUEST = {
  request: {
    request_id: 'request-1',
    operation: 'solve',
    operation_ref: { ref_type: 'api_operation', ref_id: 'solve' },
    project_ref: { ref_type: 'project', ref_id: 'invented' },
    model_ref: { ref_type: 'model', ref_id: 'invented' },
    unit_system_ref: { ref_type: 'unit_system', ref_id: 'si' },
    load_basis_refs: [{ ref_type: 'load_case', ref_id: 'LC1' }],
    input_manifest_ref: { ref_type: 'audit_manifest', ref_id: 'manifest' },
    requested_outputs: ['result_envelope'],
    privacy: { local_only: true },
    provenance: { source_name: 'invented' },
    professional_boundary: { human_review_required: true },
    tbd_decisions: { process_invocation: 'SETTLED_DEC_065' }
  },
  solve: { preview_model: { model: { nodes: [] } } }
};

function resultJson(input: { blocking?: boolean; padding?: number } = {}): string {
  return JSON.stringify({
    artifact: 'openpipestress.headless_runner_cli_output',
    schema_version: '1.0.0',
    command: 'solve',
    operation: 'solve',
    policy: { policy_ref: 'DEC-065' },
    request_validation: { diagnostics: [] },
    result_validation: { diagnostics: [] },
    diagnostics: input.blocking
      ? [{ code: 'BLOCKED', severity: 'blocking', message: 'invented blocking outcome' }]
      : [],
    ...(input.blocking ? {} : { runner_result: { diagnostics: [] } }),
    ...(input.padding ? { padding: 'x'.repeat(input.padding) } : {})
  });
}

function sha256(value: Buffer | string): string {
  return createHash('sha256').update(value).digest('hex');
}

function shellSingleQuote(value: string): string {
  return `'${value.replaceAll("'", `'"'"'`)}'`;
}

type Fixture = {
  root: string;
  projectRoot: string;
  inputPath: string;
  inputBytes: Buffer;
  sessionRoot: string;
};

let fixture: Fixture;

async function makeRunner(body: string, mode = 0o700): Promise<{ path: string; sha256: string }> {
  const runnerPath = path.join(fixture.root, `runner-${createHash('sha1').update(body).digest('hex')}.sh`);
  const content = `#!/bin/sh\n${body}\n`;
  await writeFile(runnerPath, content, 'utf8');
  await chmod(runnerPath, mode);
  return { path: runnerPath, sha256: sha256(content) };
}

function runnerEnv(runner: { path: string; sha256: string }): HeadlessRunnerEnvironment {
  return {
    [OPEN_PIPE_STRESS_RUNNER_PATH_ENV]: runner.path,
    [OPEN_PIPE_STRESS_RUNNER_SHA256_ENV]: runner.sha256
  };
}

async function makeJsonRunner(input: {
  result?: string;
  exitCode?: number;
  verifyInput?: boolean;
} = {}) {
  const output = input.result ?? resultJson();
  const expectedInputSha = sha256(fixture.inputBytes);
  const verification = input.verifyInput
    ? `actual=$(/usr/bin/shasum -a 256 | /usr/bin/cut -d ' ' -f 1)\n[ "$actual" = "${expectedInputSha}" ] || exit 2`
    : '/bin/cat >/dev/null';
  return makeRunner(
    `${verification}\n/usr/bin/printf %s ${shellSingleQuote(output)}\nexit ${input.exitCode ?? 0}`
  );
}

beforeEach(async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), 'chirality-headless-runner-'));
  const projectRoot = path.join(root, 'project');
  const profileDirectory = path.join(projectRoot, '_DomainEngines', 'profiles');
  const inputPath = path.join(projectRoot, 'runner-input.json');
  const inputBytes = Buffer.from(`${JSON.stringify(REQUEST, null, 2)}\n`, 'utf8');
  const sessionRoot = path.join(root, 'sessions');
  await mkdir(profileDirectory, { recursive: true });
  await writeFile(
    path.join(profileDirectory, 'open_pipe_stress.yaml'),
    'domain_profile:\n  id: "open_pipe_stress"\n  deterministic_tools:\n    - id: "headless_runner"\n',
    'utf8'
  );
  await writeFile(inputPath, inputBytes);
  process.env.CHIRALITY_SESSION_ROOT = sessionRoot;
  fixture = { root, projectRoot, inputPath, inputBytes, sessionRoot };
});

afterEach(async () => {
  delete process.env.CHIRALITY_SESSION_ROOT;
  delete process.env[OPEN_PIPE_STRESS_RUNNER_PATH_ENV];
  delete process.env[OPEN_PIPE_STRESS_RUNNER_SHA256_ENV];
  await rm(fixture.root, { recursive: true, force: true });
});

describe('configured DEC-065 headless runner transport', () => {
  it('delivers the exact complete input bytes to solve and accepts exit 0 JSON', async () => {
    const runner = await makeJsonRunner({ verifyInput: true });
    await expect(
      runConfiguredHeadlessPreview({ requestBytes: fixture.inputBytes, env: runnerEnv(runner) })
    ).resolves.toMatchObject({
      exitCode: 0,
      result: { command: 'solve', operation: 'solve' }
    });
  });

  it('passes argv exactly solve and does not inherit ambient secrets', async () => {
    const output = resultJson();
    const runner = await makeRunner(
      `/bin/cat >/dev/null\n[ "$#" -eq 1 ] || exit 2\n[ "$1" = "solve" ] || exit 2\n[ -z "$TEST_SECRET" ] || exit 2\n/usr/bin/printf %s ${shellSingleQuote(output)}`
    );
    await expect(
      runConfiguredHeadlessPreview({
        requestBytes: fixture.inputBytes,
        env: { ...runnerEnv(runner), TEST_SECRET: 'must-not-cross-child-boundary' }
      })
    ).resolves.toMatchObject({ exitCode: 0 });
  });

  it('preserves exit 1 as a structured blocking outcome using top-level diagnostics', async () => {
    const runner = await makeJsonRunner({ result: resultJson({ blocking: true }), exitCode: 1 });
    await expect(
      runConfiguredHeadlessPreview({ requestBytes: fixture.inputBytes, env: runnerEnv(runner) })
    ).resolves.toMatchObject({ exitCode: 1, result: { diagnostics: [{ severity: 'blocking' }] } });
  });

  it.each([
    [{}, 'HEADLESS_RUNNER_CONFIG_MISSING'],
    [
      {
        [OPEN_PIPE_STRESS_RUNNER_PATH_ENV]: 'relative/runner',
        [OPEN_PIPE_STRESS_RUNNER_SHA256_ENV]: 'a'.repeat(64)
      },
      'HEADLESS_RUNNER_PATH_NOT_ABSOLUTE'
    ],
    [
      {
        [OPEN_PIPE_STRESS_RUNNER_PATH_ENV]: '/definitely/missing/runner',
        [OPEN_PIPE_STRESS_RUNNER_SHA256_ENV]: 'a'.repeat(64)
      },
      'HEADLESS_RUNNER_PATH_INVALID'
    ],
    [
      {
        [OPEN_PIPE_STRESS_RUNNER_PATH_ENV]: '/definitely/missing/runner',
        [OPEN_PIPE_STRESS_RUNNER_SHA256_ENV]: 'A'.repeat(64)
      },
      'HEADLESS_RUNNER_SHA256_INVALID'
    ]
  ])('refuses invalid local configuration %#', async (env, code) => {
    await expect(
      runConfiguredHeadlessPreview({ requestBytes: fixture.inputBytes, env })
    ).rejects.toMatchObject({ message: code });
  });

  it('refuses hash mismatch, non-regular, and non-executable targets', async () => {
    const runner = await makeJsonRunner();
    await expect(
      runConfiguredHeadlessPreview({
        requestBytes: fixture.inputBytes,
        env: {
          ...runnerEnv(runner),
          [OPEN_PIPE_STRESS_RUNNER_SHA256_ENV]: '0'.repeat(64)
        }
      })
    ).rejects.toMatchObject({ message: 'HEADLESS_RUNNER_SHA256_MISMATCH' });

    await expect(
      runConfiguredHeadlessPreview({
        requestBytes: fixture.inputBytes,
        env: {
          [OPEN_PIPE_STRESS_RUNNER_PATH_ENV]: fixture.projectRoot,
          [OPEN_PIPE_STRESS_RUNNER_SHA256_ENV]: '0'.repeat(64)
        }
      })
    ).rejects.toMatchObject({ message: 'HEADLESS_RUNNER_NOT_REGULAR_FILE' });

    const nonExecutable = await makeRunner('/bin/cat >/dev/null', 0o600);
    await expect(
      runConfiguredHeadlessPreview({
        requestBytes: fixture.inputBytes,
        env: runnerEnv(nonExecutable)
      })
    ).rejects.toMatchObject({ message: 'HEADLESS_RUNNER_NOT_EXECUTABLE' });
  });

  it('times out and independently caps stdout and stderr', async () => {
    const timeoutRunner = await makeRunner('/bin/sleep 2');
    await expect(
      runConfiguredHeadlessPreview({
        requestBytes: fixture.inputBytes,
        env: runnerEnv(timeoutRunner),
        timeoutMs: 30
      })
    ).rejects.toMatchObject({ message: 'HEADLESS_RUNNER_TIMEOUT' });

    const stdoutRunner = await makeRunner(
      `/bin/cat >/dev/null\n/usr/bin/yes x | /usr/bin/head -c ${HEADLESS_RUNNER_STDOUT_LIMIT_BYTES + 1}`
    );
    await expect(
      runConfiguredHeadlessPreview({ requestBytes: fixture.inputBytes, env: runnerEnv(stdoutRunner) })
    ).rejects.toMatchObject({ message: 'HEADLESS_RUNNER_STDOUT_OVERSIZE' });

    const stderrRunner = await makeRunner(
      `/bin/cat >/dev/null\n/usr/bin/yes x | /usr/bin/head -c ${HEADLESS_RUNNER_STDERR_LIMIT_BYTES + 1} >&2`
    );
    await expect(
      runConfiguredHeadlessPreview({ requestBytes: fixture.inputBytes, env: runnerEnv(stderrRunner) })
    ).rejects.toMatchObject({ message: 'HEADLESS_RUNNER_STDERR_OVERSIZE' });
  });

  it('maps exit 2, unsupported exits, signals, and result schema mismatch to stable refusals', async () => {
    const exit2 = await makeRunner('/bin/cat >/dev/null\nexit 2');
    await expect(
      runConfiguredHeadlessPreview({ requestBytes: fixture.inputBytes, env: runnerEnv(exit2) })
    ).rejects.toMatchObject({ message: 'HEADLESS_RUNNER_INPUT_REFUSED' });

    const unsupported = await makeRunner('/bin/cat >/dev/null\nexit 9');
    await expect(
      runConfiguredHeadlessPreview({ requestBytes: fixture.inputBytes, env: runnerEnv(unsupported) })
    ).rejects.toMatchObject({ message: 'HEADLESS_RUNNER_EXIT_UNSUPPORTED' });

    const signalled = await makeRunner('/bin/cat >/dev/null\n/bin/kill -TERM $$');
    await expect(
      runConfiguredHeadlessPreview({ requestBytes: fixture.inputBytes, env: runnerEnv(signalled) })
    ).rejects.toMatchObject({ message: 'HEADLESS_RUNNER_SIGNALLED' });

    const mismatch = await makeJsonRunner({ result: JSON.stringify({ command: 'solve' }) });
    await expect(
      runConfiguredHeadlessPreview({ requestBytes: fixture.inputBytes, env: runnerEnv(mismatch) })
    ).rejects.toMatchObject({ message: 'HEADLESS_RUNNER_RESULT_SCHEMA_MISMATCH' });
  });

  it.each(['not-json', '{}{}'])('rejects invalid or non-single stdout JSON', async (stdout) => {
    const runner = await makeJsonRunner({ result: stdout });
    await expect(
      runConfiguredHeadlessPreview({ requestBytes: fixture.inputBytes, env: runnerEnv(runner) })
    ).rejects.toMatchObject({ message: 'HEADLESS_RUNNER_RESULT_JSON_INVALID' });
  });

  it('rejects incomplete preview fragments before spawning', async () => {
    const runner = await makeJsonRunner();
    await expect(
      runConfiguredHeadlessPreview({
        requestBytes: Buffer.from(JSON.stringify({ preview_model: {} })),
        env: runnerEnv(runner)
      })
    ).rejects.toMatchObject({ message: 'HEADLESS_RUNNER_INPUT_SCHEMA_MISMATCH' });
  });
});

describe('live domain_headless_preview_run MCP handler', () => {
  async function configureRunner(input: Parameters<typeof makeJsonRunner>[0] = {}) {
    const runner = await makeJsonRunner(input);
    process.env[OPEN_PIPE_STRESS_RUNNER_PATH_ENV] = runner.path;
    process.env[OPEN_PIPE_STRESS_RUNNER_SHA256_ENV] = runner.sha256;
    return runner;
  }

  const context = () => ({
    projectRoot: fixture.projectRoot,
    sessionId: 'sess-headless-preview',
    mode: 'readOnly'
  });

  it('uses the read permission/event/redaction/result pipeline and marks exit 1 non-successful', async () => {
    await configureRunner({ result: resultJson({ blocking: true }), exitCode: 1 });
    const result = await domainHeadlessPreviewRunTool(context(), {
      profileId: 'open_pipe_stress',
      runnerInputRef: 'runner-input.json'
    });
    expect(result.isError).toBe(true);
    const replay = await replayHarnessEvents('sess-headless-preview');
    expect(replay.events.map((event) => event.type)).toEqual([
      'tool.started',
      'tool.permission',
      'tool.completed'
    ]);
    expect(replay.events[1].data).toMatchObject({
      behavior: 'allow',
      toolName: 'mcp__chirality__domain_headless_preview_run',
      pathScope: 'project-root-read'
    });
    expect(JSON.stringify(replay.events)).not.toContain(process.env[OPEN_PIPE_STRESS_RUNNER_PATH_ENV]);
  });

  it('persists oversized results through the normal redacted artifact pipeline', async () => {
    await configureRunner({ result: resultJson({ padding: 80 * 1024 }) });
    await domainHeadlessPreviewRunTool(context(), {
      profileId: 'open_pipe_stress',
      runnerInputRef: 'runner-input.json'
    });
    const replay = await replayHarnessEvents('sess-headless-preview');
    const completed = replay.events.at(-1);
    expect(completed?.type).toBe('tool.completed');
    expect(completed?.data).toMatchObject({
      resultMetadata: { budgetClass: 'requires-artifact-overflow', outputPersisted: true },
      artifactMetadata: { redacted: true, retentionPolicy: 'session-lifetime' }
    });
  });

  it.each([
    ['pec', 'HEADLESS_RUNNER_PROFILE_REFUSED'],
    ['unknown', 'HEADLESS_RUNNER_PROFILE_REFUSED'],
    ['', 'HEADLESS_RUNNER_PROFILE_REFUSED']
  ])('refuses profileId %j', async (profileId, errorCode) => {
    await configureRunner();
    await expect(
      domainHeadlessPreviewRunTool(context(), {
        profileId,
        runnerInputRef: 'runner-input.json'
      })
    ).rejects.toMatchObject({ details: { errorCode } });
  });

  it('requires the live registry profile marker and headless_runner declaration', async () => {
    await configureRunner();
    await writeFile(
      path.join(fixture.projectRoot, '_DomainEngines', 'profiles', 'open_pipe_stress.yaml'),
      'domain_profile:\n  id: "open_pipe_stress"\n  deterministic_tools: []\n',
      'utf8'
    );
    await expect(
      domainHeadlessPreviewRunTool(context(), {
        profileId: 'open_pipe_stress',
        runnerInputRef: 'runner-input.json'
      })
    ).rejects.toMatchObject({ message: 'profileId does not expose the requested deterministic tool' });

    await writeFile(
      path.join(fixture.projectRoot, '_DomainEngines', 'profiles', 'open_pipe_stress.yaml'),
      'domain_profile:\n  id: "pec"\n  deterministic_tools:\n    - id: "headless_runner"\n',
      'utf8'
    );
    await expect(
      domainHeadlessPreviewRunTool(context(), {
        profileId: 'open_pipe_stress',
        runnerInputRef: 'runner-input.json'
      })
    ).rejects.toMatchObject({ message: 'profile file does not match the registered profileId' });
  });

  it('refuses missing, outside, symlink, and non-file runnerInputRef values', async () => {
    await configureRunner();
    const outsidePath = path.join(fixture.root, 'outside.json');
    await writeFile(outsidePath, fixture.inputBytes);
    const symlinkPath = path.join(fixture.projectRoot, 'linked-input.json');
    await symlink(outsidePath, symlinkPath);

    for (const runnerInputRef of [
      'missing.json',
      outsidePath,
      'linked-input.json',
      '_DomainEngines'
    ]) {
      await expect(
        domainHeadlessPreviewRunTool(context(), {
          profileId: 'open_pipe_stress',
          runnerInputRef
        })
      ).rejects.toMatchObject({ type: 'INVALID_REQUEST' });
    }
  });

  it('refuses an omitted runnerInputRef before permission or process execution', async () => {
    await configureRunner();
    await expect(
      domainHeadlessPreviewRunTool(context(), {
        profileId: 'open_pipe_stress'
      } as never)
    ).rejects.toMatchObject({
      message: 'runnerInputRef is required',
      details: { errorCode: 'HEADLESS_RUNNER_INPUT_REF_MISSING' }
    });
  });

  it('registers only the read-only exclusive open_pipe_stress handler', () => {
    const definitions = buildChiralityMcpTools({
      context: context(),
      allowedToolNames: ['mcp__chirality__domain_headless_preview_run']
    });
    expect(definitions.map((definition) => (definition as { name: string }).name)).toEqual([
      'domain_headless_preview_run'
    ]);
  });

  it('does not alter the exact runnerInputRef bytes', async () => {
    await configureRunner({ verifyInput: true });
    const before = await readFile(fixture.inputPath);
    const result = await domainHeadlessPreviewRunTool(context(), {
      profileId: 'open_pipe_stress',
      runnerInputRef: 'runner-input.json'
    });
    expect(result.isError).not.toBe(true);
    await expect(readFile(fixture.inputPath)).resolves.toEqual(before);
  });
});
